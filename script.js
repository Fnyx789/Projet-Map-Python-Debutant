function newpage() {
    // Création des données pour les paramètres
    let data = {
        date: document.getElementById('date').value,
        time: document.getElementById('time').value,
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
    };
    // Conversion des données en chaîne de paramètres
    const params = new URLSearchParams(data).toString();
    // Redirection vers la nouvelle page avec les paramètres dans l'URL
    window.open("Confirmation.html?" + params, '_blank');
}



// peut etre qu'il faudrait que j'arrive à récuperer les éléments directemenrt de mon JS pour less mettres dans la DB => SQL
// Pourquoi je ne peux pas ajouter ma page PHP dans mon html 
// Comment installer un DB lite SLQ
// 