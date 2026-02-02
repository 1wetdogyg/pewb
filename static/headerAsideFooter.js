const header = document.querySelector("header");
const aside  = document.querySelector("aside");
const footer = document.querySelector("footer");

header.innerHTML = `
<div class="logo">
    <img src="/imagenes/sistema-solar.png" alt="Logo Sistema Solar">
</div>
<nav>
    <ul class="nav">
        <li><a href="#">Planetas</a></li>
        <li><a href="#">Cometas</a></li>
        <li><a href="#">El Sol</a></li>
    </ul>
</nav>
`;

aside.innerHTML = `
<h2>Más datos</h2>
<ul>
    <li><a href="/templates/mercurio.html">Mercurio</a></li>
    <li><a href="/templates/venus.html">Venus</a></li>
    <li><a href="/templates/index.html">Tierra</a></li>
    <li><a href="/templates/index.html">index</a></li>
    <li><a href="#">Júpiter</a></li>
    <li><a href="#">Saturno</a></li>
    <li><a href="#">Urano</a></li>
    <li><a href="#">Neptuno</a></li>
</ul>
`;

footer.innerHTML = `
<p>© 2025 - Sistema Solar | Diseñado por PerroMojao</p>
`;
