// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "Blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "post-type-and-token-causality",
        
          title: "Type and Token Causality",
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/type_and_token";
          
        },
      },{id: "news-passed-the-qualifier-stage-and-am-officially-a-ph-d-candidate",
          title: 'Passed the qualifier stage and am officially a Ph.D. candidate!',
          description: "",
          section: "News",},{id: "news-i-am-joining-the-10th-edition-of-ai-safety-camp",
          title: 'I am joining the 10th edition of AI Safety Camp.',
          description: "",
          section: "News",},{id: "news-presented-our-work-on-detecting-and-characterizing-planning-in-language-models-at-the-2nd-new-england-mechanistic-interpretability-nemi-workshop",
          title: 'Presented our work on Detecting and Characterizing Planning in Language Models at the...',
          description: "",
          section: "News",},{id: "news-i-will-be-at-neurips-2025-presenting-our-work-on-detecting-and-characterizing-planning-in-language-models-at-the-mechanistic-interpretability-workshop",
          title: 'I will be at NeurIPS 2025 presenting our work on Detecting and Characterizing...',
          description: "",
          section: "News",},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%73%61%6E%6B%61%72%61%6E%76@%63%73.%75%6D%61%73%73.%65%64%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/sankaranv", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/sankaranv8", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=DbeHYRcAAAAJ", "_blank");
        },
      },{
        id: 'social-semanticscholar',
        title: 'Semantic Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://www.semanticscholar.org/author/65731722", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/sankaranv8", "_blank");
        },
      },{
        id: 'social-bluesky',
        title: 'Bluesky',
        section: 'Socials',
        handler: () => {
          window.open("https://bsky.app/profile/sankaranv.bsky.social", "_blank");
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
