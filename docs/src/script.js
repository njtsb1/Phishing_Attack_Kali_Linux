// Localized Translation Dictionaries Dataset Modules
const i18nDictionary = {
    "en-US": {
        loginUserPlaceholder: "Phone number or email address",
        loginPassPlaceholder: "Password",
        loginBtn: "Log In",
        forgotPassword: "Forgotten Password?",
        backToRegister: "Back",
        createNewAccount: "Create New Account",
        orText: "OR",
        registerTitle: "Create a new account",
        registerSubtitle: "It's quick and easy.",
        firstNamePlaceholder: "First name",
        surnamePlaceholder: "Surname",
        contactPlaceholder: "Mobile number or email address",
        newPasswordPlaceholder: "New password",
        dobLabel: "Date of birth",
        genderLabel: "Gender",
        genderFemale: "Female",
        genderMale: "Male",
        genderCustom: "Custom",
        termsDisclaimer: "By clicking Sign Up, you agree to our Terms, Data Policy and Cookies Policy. You may receive SMS notifications from us.",
        signUpBtn: "Sign Up",
        alreadyHaveAccount: "Already have an account?",
        logOut: "Log Out",
        welcomeUser: "Hello, ",
        notificationsTitle: "Notifications",
        dashboardNav: "Dashboard Navigation"
    },
    "pt-BR": {
        loginUserPlaceholder: "Número de celular ou e-mail",
        loginPassPlaceholder: "Senha",
        loginBtn: "Entrar",
        forgotPassword: "Esqueceu a senha?",
        backToRegister: "Voltar",
        createNewAccount: "Criar nova conta",
        orText: "OU",
        registerTitle: "Criar uma nova conta",
        registerSubtitle: "É rápido e fácil.",
        firstNamePlaceholder: "Nome",
        surnamePlaceholder: "Sobrenome",
        contactPlaceholder: "Celular ou e-mail",
        newPasswordPlaceholder: "Nova senha",
        dobLabel: "Data de nascimento",
        genderLabel: "Gênero",
        genderFemale: "Feminino",
        genderMale: "Masculino",
        genderCustom: "Personalizado",
        termsDisclaimer: "Ao clicar em Cadastre-se, você concorda com nossos Termos, Política de Dados e Política de Cookies. Você pode receber notificações por SMS.",
        signUpBtn: "Cadastre-se",
        alreadyHaveAccount: "Já tem uma conta?",
        logOut: "Sair",
        welcomeUser: "Olá, ",
        notificationsTitle: "Notificações",
        dashboardNav: "Navegação do Painel"
    },
    "es-ES": {
        loginUserPlaceholder: "Número de celular o correo electrónico",
        loginPassPlaceholder: "Contraseña",
        loginBtn: "Iniciar sesión",
        forgotPassword: "¿Has olvidado la contraseña?",
        backToRegister: "Volver",
        createNewAccount: "Crear cuenta nueva",
        orText: "O",
        registerTitle: "Crear una cuenta nueva",
        registerSubtitle: "Es rápido y fácil.",
        firstNamePlaceholder: "Nombre",
        surnamePlaceholder: "Apellido",
        contactPlaceholder: "Celular o correo electrónico",
        newPasswordPlaceholder: "Contraseña nueva",
        dobLabel: "Fecha de nacimiento",
        genderLabel: "Sexo",
        genderFemale: "Mujer",
        genderMale: "Hombre",
        genderCustom: "Personalizado",
        termsDisclaimer: "Al hacer clic en Registrarte, aceptas nuestras Condiciones, la Política de datos y la Política de cookies. Es posible que te enviemos notificaciones por SMS.",
        signUpBtn: "Registrarte",
        alreadyHaveAccount: "¿Ya tienes una cuenta?",
        logOut: "Cerrar sesión",
        welcomeUser: "Hola, ",
        notificationsTitle: "Notificaciones",
        dashboardNav: "Navegación del Panel"
    }
};

// State Engine Tracker Variables
let currentLanguage = "en-US";
const userDatabase = {};
let authenticatedUser = null;

document.addEventListener("DOMContentLoaded", () => {
    // Populate Form Select Elements Options Loops
    populateDropdowns();
    
    // Wire Active UI Event Handler Listeners
    setupNavigationListeners();
    setupFormHandlers();
    setupPreferenceControls();
});

// Dropdowns Content Generators Function
function populateDropdowns() {
    const daySelect = document.getElementById("dob-day");
    const monthSelect = document.getElementById("dob-month");
    const yearSelect = document.getElementById("dob-year");
    
    const monthsShort = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    
    for (let d = 1; d <= 31; d++) {
        daySelect.add(new Option(d, d));
    }
    daySelect.value = "17";
    
    monthsShort.forEach((m, idx) => {
        monthSelect.add(new Option(m, m));
    });
    monthSelect.value = "Jan";
    
    const currentYear = 2026;
    for (let y = currentYear; y >= 1905; y--) {
        yearSelect.add(new Option(y, y));
    }
    yearSelect.value = "1995";
}

// Global View Switching Module Engine Route
function switchView(targetViewId) {
    document.querySelectorAll(".view-section").forEach(view => {
        view.classList.remove("active-view");
    });
    const target = document.getElementById(targetViewId);
    if (target) {
        target.classList.add("active-view");
        window.scrollTo(0, 0);
    }
}

// Router Anchors Links Binding Maps
function setupNavigationListeners() {
    document.getElementById("go-to-register-btn").addEventListener("click", () => switchView("page-register"));
    document.getElementById("go-to-register-link").addEventListener("click", () => switchView("page-register"));
    document.getElementById("back-to-login").addEventListener("click", () => switchView("page-login"));
    
    document.getElementById("logout-btn").addEventListener("click", () => {
        authenticatedUser = null;
        switchView("page-login");
    });
    
    // Bind Card Alerts for Classical Visual References
    document.querySelectorAll(".grid-card").forEach(card => {
        card.addEventListener("click", () => {
            const desc = card.getAttribute("data-desc");
            alert(desc);
        });
    });
}

// Internal Database Forms Submissions Lógicas Engine
function setupFormHandlers() {
    const regForm = document.getElementById("register-form");
    const loginForm = document.getElementById("login-form");
    
    regForm.addEventListener("submit", (e) => {
        e.preventDefault();
        
        const contact = document.getElementById("reg-contact").value.trim();
        const fname = document.getElementById("reg-firstname").value.trim();
        const password = document.getElementById("reg-password").value.trim();
        
        userDatabase[contact] = {
            firstName: fname,
            password: password
        };
        
        alert(currentLanguage === "pt-BR" ? "Conta criada com sucesso!" : "Account created successfully!");
        regForm.reset();
        populateDropdowns(); // Re-establish markers defaults
        switchView("page-login");
    });
    
    loginForm.addEventListener("submit", (e) => {
        e.preventDefault();
        
        const user = document.getElementById("login-username").value.trim();
        const pass = document.getElementById("login-password").value.trim();
        
        if (userDatabase[user] && userDatabase[user].password === pass) {
            authenticatedUser = userDatabase[user];
            document.getElementById("user-welcome").textContent = `${i18nDictionary[currentLanguage].welcomeUser}${authenticatedUser.firstName}`;
            loginForm.reset();
            switchView("page-home");
        } else {
            alert(currentLanguage === "pt-BR" ? "Credenciais inválidas!" : "Invalid credentials!");
        }
    });
}

// Context Preferences Handlers Engine Layout
function setupPreferenceControls() {
    const themeBtn = document.getElementById("theme-toggle");
    const langSelect = document.getElementById("lang-select");
    
    themeBtn.addEventListener("click", () => {
        const docHtml = document.documentElement;
        const currentTheme = docHtml.getAttribute("data-theme");
        const nextTheme = currentTheme === "dark" ? "light" : "dark";
        
        docHtml.setAttribute("data-theme", nextTheme);
        themeBtn.querySelector(".theme-icon").textContent = nextTheme === "dark" ? "🌙" : "☀️";
        themeBtn.setAttribute("aria-label", nextTheme === "dark" ? "Toggle light theme" : "Toggle dark theme");
    });
    
    langSelect.addEventListener("change", (e) => {
        currentLanguage = e.target.value;
        translateDOMEnvironment();
    });
}

// Text Refresher Interceptor Processor Translations Engine
function translateDOMEnvironment() {
    const dataset = i18nDictionary[currentLanguage];
    if (!dataset) return;
    
    // Handle inline element strings
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (dataset[key]) el.textContent = dataset[key];
    });
    
    // Handle structural attributes inputs placeholders
    document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
        const key = el.getAttribute("data-i18n-placeholder");
        if (dataset[key]) el.setAttribute("placeholder", dataset[key]);
    });
    
    // Handle specialized access attributes keys
    document.querySelectorAll("[data-i18n-aria-label]").forEach(el => {
        const key = el.getAttribute("data-i18n-aria-label");
        if (dataset[key]) el.setAttribute("aria-label", dataset[key]);
    });
    
    // Sync context references for dynamically tracked runtime welcome panels labels
    if (authenticatedUser) {
        document.getElementById("user-welcome").textContent = `${dataset.welcomeUser}${authenticatedUser.firstName}`;
    }
}