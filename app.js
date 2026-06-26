const API_URL = "https://qr-menu-project-1fv4.onrender.com";
const RESTAURANT_ID = "shashlychnaya_one";

const modal = document.getElementById('dish-modal');
const closeButton = document.querySelector('.close-button');

async function loadMenu() {
    try {
        const response = await fetch(`${API_URL}/api/menu/${RESTAURANT_ID}`);
        const data = await response.json();
        
        if (data.error) {
            console.error(data.error);
            return;
        }

        const container = document.getElementById('menu-content');
        container.innerHTML = ""; 

        data.categories.forEach(category => {
            // Категория
            const catTitle = document.createElement('h2');
            catTitle.className = 'category-title';
            catTitle.innerText = category.category_name;
            container.appendChild(catTitle);

            // Блюда
            category.items.forEach(item => {
                const card = document.createElement('div');
                card.className = 'dish-card';
                
                // Ссылка на картинку через эндпоинт статики FastAPI
                const imageUrl = `${API_URL}/static/images/${item.image}`;

                card.innerHTML = `
                    <div class="dish-info">
                        <h3>${item.name}</h3>
                        <p>${item.description}</p>
                        <span class="price-tag">${item.price} ₸</span>
                    </div>
                    <img src="${imageUrl}" alt="${item.name}" class="dish-img">
                `;

                // Обработчик клика на карточку
                card.addEventListener('click', () => openModal(item, imageUrl));
                
                container.appendChild(card);
            });
        });

    } catch (error) {
        console.error("Ошибка загрузки меню:", error);
    }
}

function openModal(item, imageUrl) {
    document.getElementById('modal-image').src = imageUrl;
    document.getElementById('modal-title').innerText = item.name;
    document.getElementById('modal-price').innerText = `${item.price} ₸`;
    document.getElementById('modal-full-description').innerText = item.full_description || "Описание готовится...";
    
    modal.style.display = 'block';
}

closeButton.addEventListener('click', () => {
    modal.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

document.addEventListener("DOMContentLoaded", loadMenu);