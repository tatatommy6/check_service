async function getQRCode(data) {
    const response = await fetch(`/generate_qr/?data=${encodeURIComponent(data)}`);
    const blob = await response.blob();

    // Blob을 URL로 변환하여 이미지 표시
    const imgUrl = URL.createObjectURL(blob);
    document.getElementById("qrImage").src = imgUrl;
}

// 버튼 클릭 시 실행
document.getElementById("generateBtn").addEventListener("click", () => {
    const inputData = document.getElementById("qrData").value;
    getQRCode(inputData);
});
