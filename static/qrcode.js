// 버튼 클릭 시 실행
document.getElementById("generateBtn").addEventListener("click", async () => {
    const response = await fetch("/generate_qr", {
        method: "POST"
    });
    if (response.ok) {
        const blob = await response.blob();

        // Blob을 URL로 변환하여 이미지 표시
        const imgUrl = URL.createObjectURL(blob);
        let qrImage = document.getElementById("qrImage");
        qrImage.src = imgUrl;
        qrImage.classList.remove("d-none");
    } else {
        alert("QR 코드 생성에 실패했습니다.");
    }
});
