function displayFileName() {
  const fileInput = document.getElementById('upload');
  const fileNameElement = document.getElementById('file-name');
  const uploadedImageElement = document.getElementById('uploaded-image');

  const file = fileInput.files[0];
  fileNameElement.textContent = file.name;

  const reader = new FileReader();
  reader.onload = function(e) {
    uploadedImageElement.src = e.target.result;
  };
  reader.readAsDataURL(file);
}
function convertImage() {
  const form = document.getElementById('upload-form');
  const formData = new FormData(form);
  
  fetch('', {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': '{{ csrf_token }}',
    }
  })
  .then(response => response.blob())
  .then(blob => {
    const imageUrl = URL.createObjectURL(blob);
    const denoisedImageContainer = document.getElementById('denoised-image-container');
    denoisedImageContainer.innerHTML = `<img src="${imageUrl}" alt="Denoised Image">`;
  })
  .catch(error => console.error('Error:', error));
}


function convertImage() {
  const fileInput = document.getElementById('upload');
  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append('image', file);

  fetch('', {
    method: 'POST',
    body: formData,
  })
    .then(response => response.blob())
    .then(blob => {
      const outputContainer = document.getElementById('output-container');
      outputContainer.innerHTML = '';

      const img = document.createElement('img');
      img.src = URL.createObjectURL(blob);
      img.classList.add('output-image');
      outputContainer.appendChild(img);
    })
    .catch(error => console.log(error));
}
