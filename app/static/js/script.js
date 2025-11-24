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

    // Close modal
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Click outside modal to close
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
