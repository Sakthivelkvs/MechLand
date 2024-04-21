let preveiwContainer = document.querySelector('.products-preview');
let previewBox = preveiwContainer.querySelectorAll('.preview');

document.querySelectorAll('.products-container .product').forEach(product =>{
  product.onclick = () =>{
    preveiwContainer.style.display = 'flex';
    let name = product.getAttribute('data-name');zz
    previewBox.forEach(preview =>{
      let target = preview.getAttribute('data-target');
      if(name == target){
        preview.classList.add('active');
      }else {
        preview.classList.remove('active'); // Ensure other previews are not active
      }
    });
  };
});

document.querySelectorAll('.products-preview .preview .fa-times').forEach(closeButton => {
  closeButton.onclick = () => {
     closeButton.closest('.preview').classList.remove('active');
     preveiwContainer.style.display = 'none';
  };
});


previewBox.forEach(close =>{
  close.querySelector('.fa-times').onclick = () =>{
    close.classList.remove('active');
    preveiwContainer.style.display = 'none';
  };
});