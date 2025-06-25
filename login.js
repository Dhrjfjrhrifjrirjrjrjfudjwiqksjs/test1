function login() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const meldung = document.getElementById("meldung");
  
    if (username === "marcel" && password === "test123") {
      window.location.href = "profil.html";
    } else {
      meldung.innerText = "Benutzername oder Passwort ist falsch!";
    }
  }
  