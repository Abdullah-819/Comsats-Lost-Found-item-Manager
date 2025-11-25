document.addEventListener('DOMContentLoaded', () => {
    const items = Array.from(document.querySelectorAll('.item-card'));
    const modal = document.getElementById('itemModal');
    const modalImg = document.getElementById('modal-img');
    const modalName = document.getElementById('modal-name');
    const modalDescription = document.getElementById('modal-description');
    const modalLocation = document.getElementById('modal-location');
    const modalContact = document.getElementById('modal-contact');
    const closeBtn = modal.querySelector('.close-btn');

    let currentIndex = 0;

    // Show modal function
    function showModal(index) {
        const itemCard = items[index];
        const img = itemCard.querySelector('.item-img');
        modalImg.src = img.src;
        modalName.textContent = itemCard.querySelector('h3').textContent;
        modalDescription.textContent = itemCard.querySelector('.item-description').textContent;

        // Safe extraction for location
        const locationPara = itemCard.querySelector('p strong');
        modalLocation.textContent = locationPara ? locationPara.parentNode.textContent.replace('Location:', '').trim() : '';

        // Safe extraction for contact
        const contactPara = Array.from(itemCard.querySelectorAll('p')).find(p => p.textContent.includes('Contact:'));
        modalContact.textContent = contactPara ? contactPara.textContent.replace('Contact:', '').trim() : '';

        modal.style.display = 'block';
        currentIndex = index;
    }

    // Click on any item image
    items.forEach((itemCard, index) => {
        const wrapper = itemCard.querySelector('.img-wrapper');
        wrapper.addEventListener('click', () => showModal(index));
    });

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Arrow navigation & Escape key
    window.addEventListener('keydown', (e) => {
        if (modal.style.display === 'block') {
            if (e.key === 'ArrowRight') {
                currentIndex = (currentIndex + 1) % items.length;
                showModal(currentIndex);
            } else if (e.key === 'ArrowLeft') {
                currentIndex = (currentIndex - 1 + items.length) % items.length;
                showModal(currentIndex);
            } else if (e.key === 'Escape') {
                modal.style.display = 'none';
            }
        }
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('itemModal');
    const modalImg = document.getElementById('modal-img');
    const modalContent = modal.querySelector('.modal-content');
    let currentIndex = 0;
    let items = Array.from(document.querySelectorAll('.item-card'));

    function showModal(index) {
        const itemCard = items[index];
        const img = itemCard.querySelector('.item-img');

        modalImg.src = img.dataset.src || img.src; // lazy load support
        modalImg.onload = () => modalImg.classList.add('fade-in-zoom');

        const name = itemCard.querySelector('h3').textContent;
        const desc = itemCard.querySelector('.item-description').textContent;
        const locationPara = itemCard.querySelector('p strong');
        const location = locationPara ? locationPara.parentNode.textContent.replace('Location:', '').trim() : '';
        const contactPara = Array.from(itemCard.querySelectorAll('p')).find(p => p.textContent.includes('Contact:'));
        const contact = contactPara ? contactPara.textContent.replace('Contact:', '').trim() : '';

        document.getElementById('modal-name').textContent = name;
        document.getElementById('modal-description').textContent = desc;
        document.getElementById('modal-location').textContent = location;
        document.getElementById('modal-contact').textContent = contact;

        modal.style.display = 'block';
        modalContent.style.transform = 'scale(0.9)';
        modalContent.style.opacity = 0;
        setTimeout(() => {
            modalContent.style.transition = 'all 0.4s ease';
            modalContent.style.transform = 'scale(1)';
            modalContent.style.opacity = 1;
        }, 50);
        currentIndex = index;
    }

    items.forEach((itemCard, index) => {
        const wrapper = itemCard.querySelector('.img-wrapper');
        wrapper.addEventListener('click', () => showModal(index));
        itemCard.addEventListener('mousemove', e => {
            const rect = itemCard.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const cx = rect.width / 2;
            const cy = rect.height / 2;
            const dx = (x - cx) / cx;
            const dy = (y - cy) / cy;
            itemCard.style.transform = `rotateX(${dy * 5}deg) rotateY(${dx * 5}deg) translateY(-7px)`;
        });
        itemCard.addEventListener('mouseleave', () => {
            itemCard.style.transform = 'translateY(-7px) rotateX(0deg) rotateY(0deg)';
        });
    });

    const closeBtn = modal.querySelector('.close-btn');
    closeBtn.addEventListener('click', () => modal.style.display = 'none');
    window.addEventListener('click', e => { if(e.target === modal) modal.style.display = 'none'; });

    window.addEventListener('keydown', e => {
        if(modal.style.display === 'block') {
            if(e.key === 'ArrowRight') { currentIndex = (currentIndex + 1) % items.length; showModal(currentIndex); }
            else if(e.key === 'ArrowLeft') { currentIndex = (currentIndex - 1 + items.length) % items.length; showModal(currentIndex); }
            else if(e.key === 'Escape') { modal.style.display = 'none'; }
        }
    });
    let startX = 0;
    modalContent.addEventListener('touchstart', e => { startX = e.touches[0].clientX; });
    modalContent.addEventListener('touchend', e => {
        const endX = e.changedTouches[0].clientX;
        if(endX - startX > 50) { currentIndex = (currentIndex - 1 + items.length) % items.length; showModal(currentIndex); }
        else if(startX - endX > 50) { currentIndex = (currentIndex + 1) % items.length; showModal(currentIndex); }
    });
    const adminBtn = document.querySelector('.admin-btn');
    const roleSelection = document.querySelector('.role-selection');
    const adminLogin = document.querySelector('.login-wrapper');

    if(adminBtn && roleSelection && adminLogin){
        adminBtn.addEventListener('click', e => {
            e.preventDefault();
            roleSelection.style.transition = 'all 0.6s ease';
            roleSelection.style.transform = 'translateX(-100%) rotateY(15deg)';
            roleSelection.style.opacity = 0;
            setTimeout(() => {
                adminLogin.style.display = 'flex';
                adminLogin.style.opacity = 0;
                adminLogin.style.transform = 'translateX(50px)';
                setTimeout(() => {
                    adminLogin.style.transition = 'all 0.6s ease';
                    adminLogin.style.opacity = 1;
                    adminLogin.style.transform = 'translateX(0)';
                }, 50);
            }, 400);
        });
    }
    document.querySelectorAll('button, .role-btn, .action-btn').forEach(btn => {
        btn.addEventListener('click', e => {
            const circle = document.createElement('span');
            circle.classList.add('ripple');
            btn.appendChild(circle);
            const d = Math.max(btn.clientWidth, btn.clientHeight);
            circle.style.width = circle.style.height = `${d}px`;
            circle.style.left = `${e.clientX - btn.getBoundingClientRect().left - d/2}px`;
            circle.style.top = `${e.clientY - btn.getBoundingClientRect().top - d/2}px`;
            setTimeout(() => circle.remove(), 600);
        });
    });
    const particleContainer = document.createElement('div');
    particleContainer.style.position = 'fixed';
    particleContainer.style.top = 0;
    particleContainer.style.left = 0;
    particleContainer.style.width = '100%';
    particleContainer.style.height = '100%';
    particleContainer.style.pointerEvents = 'none';
    particleContainer.style.zIndex = 0;
    document.body.appendChild(particleContainer);

    for(let i=0; i<50; i++){
        const particle = document.createElement('div');
        particle.style.position = 'absolute';
        particle.style.width = particle.style.height = `${Math.random()*4+2}px`;
        particle.style.background = 'rgba(0,238,255,0.3)';
        particle.style.borderRadius = '50%';
        particle.style.top = `${Math.random()*100}%`;
        particle.style.left = `${Math.random()*100}%`;
        particle.style.animation = `float${i} ${3+Math.random()*5}s ease-in-out infinite alternate`;
        particleContainer.appendChild(particle);

        const styleEl = document.createElement('style');
        styleEl.innerHTML = `
            @keyframes float${i} {
                from { transform: translateY(0) translateX(0); }
                to { transform: translateY(-50px) translateX(20px); }
            }
        `;
        document.head.appendChild(styleEl);
    }

});