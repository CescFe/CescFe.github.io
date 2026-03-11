// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-principal",
    title: "principal",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-diccionaris",
          title: "diccionaris",
          description: "els diccionaris i vocabularis de Francesc Ferrer Pastor",
          section: "Navigation",
          handler: () => {
            window.location.href = "/diccionaris/";
          },
        },{id: "nav-distribuïdors",
          title: "distribuïdors",
          description: "t&#39;interessa algún dels nostres llibres? ací t&#39;indiquem on pots adquirir-los",
          section: "Navigation",
          handler: () => {
            window.location.href = "/distribu%C3%AFdors/";
          },
        },{id: "nav-col-leccions",
          title: "col·leccions",
          description: "un llistat amb les diferents col·leccions de Denes",
          section: "Navigation",
          handler: () => {
            window.location.href = "/col-leccions/";
          },
        },{id: "nav-material-biblioteca",
          title: "material biblioteca",
          description: "el material de biblioteca de Denes",
          section: "Navigation",
          handler: () => {
            window.location.href = "/material-biblioteca/";
          },
        },{id: "nav-francesc-ferrer-pastor",
          title: "Francesc Ferrer Pastor",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/francesc-ferrer-pastor/";
          },
        },{id: "post-recopilació-de-rondalles-de-francesc-ferrer-pastor",
        
          title: "Recopilació de rondalles de Francesc Ferrer Pastor",
        
        description: "Recull de rondalles en PDF de Francesc Ferrer Pastor.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/assets/pdf/rondalles_ferrer_pastor.pdf";
          
        },
      },{id: "post-homenatge-a-francesc-ferrer-pastor",
        
          title: "Homenatge a Francesc Ferrer Pastor",
        
        description: "Francesc Ferrer Pastor&#39;:&#39; una vida dedicada al seu poble i a la seua llengua.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/homenatge-ferrer-pastor/";
          
        },
      },{id: "post-guia-pràctica-de-verbs-valencians",
        
          title: "Guia Pràctica de Verbs Valencians",
        
        description: "Guia pràctica de verbs valencians, amb flexions i conjugacions.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/guia-practica-verbs-valencians/";
          
        },
      },{id: "post-francesc-ferrer-pastor-l-39-home-que-xiuxiuejava-paraules-1918-2020",
        
          title: "Francesc Ferrer Pastor: l&#39;home que xiuxiuejava paraules (1918-2020)",
        
        description: "Imatges de l&#39;exposició Francesc Ferrer Pastor: l&#39;home que xiuxiuejava paraules (1918-2020).",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/exposicio-ferrer-pastor-xiuxiuejava-paraules/";
          
        },
      },{id: "post-google-gemini-updates-flash-1-5-gemma-2-and-project-astra",
        
          title: 'Google Gemini updates: Flash 1.5, Gemma 2 and Project Astra <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "We’re sharing updates across our Gemini family of models and a glimpse of Project Astra, our vision for the future of AI assistants.",
        section: "Posts",
        handler: () => {
          
            window.open("https://blog.google/technology/ai/google-gemini-update-flash-ai-assistant-io-2024/", "_blank");
          
        },
      },{id: "post-displaying-external-posts-on-your-al-folio-blog",
        
          title: 'Displaying External Posts on Your al-folio Blog <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.open("https://medium.com/@al-folio/displaying-external-posts-on-your-al-folio-blog-b60a1d241a0a?source=rss-17feae71c3c4------2", "_blank");
          
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%64%65%6E%65%73@%65%64%69%74%6F%72%69%61%6C%64%65%6E%65%73.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-facebook',
        title: 'Facebook',
        section: 'Socials',
        handler: () => {
          window.open("https://facebook.com/2419640394775198", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
