document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#contactForm');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const submitButton = form.querySelector('button[type="submit"]');
        
        try {
            submitButton.disabled = true;
            submitButton.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Gönderiliyor...';
            
            const response = await fetch('/api/contact/', {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                showAlert('success', 'Mesajınız başarıyla gönderildi!');
                form.reset();
            } else {
                throw new Error('Bir hata oluştu');
            }
        } catch (error) {
            showAlert('danger', 'Mesaj gönderilirken bir hata oluştu. Lütfen tekrar deneyin.');
        } finally {
            submitButton.disabled = false;
            submitButton.innerHTML = 'Gönder';
        }
    });
    
    function showAlert(type, message) {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        form.insertAdjacentElement('beforebegin', alert);
        
        setTimeout(() => {
            alert.remove();
        }, 5000);
    }
}); 