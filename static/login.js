async function login_rq() {
  let from = document.getElementsByClassName('input-field');
  const formData = new FormData();
  for (let i = 0; i < from.length; i++) {
    formData.append(from[i].id, from[i].value);
  }
  const response = await fetch("/login", {
    method: "POST",
    body: formData,
  });
  console.log(response);
  if (response.ok) {
    alert("로그인 성공");
    location.href = "/mypage";
  } else {
    alert("로그인 실패");
  }
} 