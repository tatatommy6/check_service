let navbar = document.getElementsByClassName('container1')[0];
navbar.innerHTML = `
        <div class="orange-circle"></div>
        
        <div class="navbar navbar-expand-lg">
          <div class="btn-group">
            <button class="btn btn-outline-primary active" id="main">Main</button>
            <button class="btn btn-outline-primary" id="features">Features</button>
            <button class="btn btn-outline-primary" id="login">Login</button>
          </div>
          <div class="active-bar"></div>
        </div>
        <button class="btn btn-primary custom-btn" type="submit">login</button>
        `;//<hr style="border: 1px solid #000000;" id="line">

document.querySelectorAll('.btn').forEach((button) => {
    button.addEventListener('click', function() {
        const activeButton = document.querySelector('.btn.active');
        activeButton.classList.remove('active');
        this.classList.add('active'); // this 아이디어 좋다 클릭한 버튼을 가져오나봐
        
        const activeBar = document.querySelector('.active-bar');
        const buttonRect = this.getBoundingClientRect();
        const left_position = buttonRect.left - 385.4875183105469; // 385.4875183105469는 원래 위치
        console.log(left_position); // 대체 뭔지 까보자
        
        activeBar.style.left = `${left_position}px`;
        activeBar.style.width = `${buttonRect.width}px`;
    });
});