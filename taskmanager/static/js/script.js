document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav)
  });

  document.addEventListener('DOMContentLoaded', function() {
    let deleteModal = document.querySelectorAll('.modal');
    M.Modal.init(deleteModal);
  });
