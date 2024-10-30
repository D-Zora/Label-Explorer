const video = document.getElementById("camera");
const captureBtn = document.getElementById("capture-image");
const imgTag = document.getElementById("image");

captureBtn.addEventListener("click", () => {
    const canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
    const dataURL = canvas.toDataURL();
    console.log(dataURL);
    imgTag.src = dataURL;
})

navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
    // console.log(stream);
    video.srcObject = stream;
})