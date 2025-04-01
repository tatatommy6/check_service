document.querySelectorAll('.btn').forEach((button) => {
    button.addEventListener('click', function() {
        const activeButton = document.querySelector('.btn.active');
        activeButton.classList.remove('active');
        this.classList.add('active');
        
        const activeBar = document.querySelector('.active-bar');
        const buttonRect = this.getBoundingClientRect();
        activeBar.style.left = `${buttonRect.left}px`;
        activeBar.style.width = `${buttonRect.width}px`;
    });
});