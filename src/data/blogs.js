let blogs = [
  {
    id: 1,
    img: "https://dummyimage.com/423x263",
    title: "Daily dev tips",
    date: "28 Aug 2022",
    content: `# Introduction
The key idea behind microfrontends is to lazy load code at runtime, such that the Angular compiler does not need to know about the lazy loaded feature modules at runtime. This is especially useful, when multiple teams are working on a project and independent deployment is necessary for productivity.

Although this is the key idea, this won’t work like that out-of-the-box, because Angular is not able to resolve the dependency at compile time. Webpack can be used to do some magic things under the hood, such that lazy loading works with the help of a module federation plugin.`,
  },
  {
    id: 2,
    img: "https://dummyimage.com/423x263",
    title: "Is react slow",
    date: "30 Aug 2022",
    content: `# Introduction
The key idea behind microfrontends is to lazy load code at runtime, such that the Angular compiler does not need to know about the lazy loaded feature modules at runtime. This is especially useful, when multiple teams are working on a project and independent deployment is necessary for productivity.

Although this is the key idea, this won’t work like that out-of-the-box, because Angular is not able to resolve the dependency at compile time. Webpack can be used to do some magic things under the hood, such that lazy loading works with the help of a module federation plugin.`,
  },
  {
    id: 3,
    img: "https://dummyimage.com/423x263",
    title: "How to svelte",
    date: "5 Sep 2022",
    content: `# Introduction
The key idea behind microfrontends is to lazy load code at runtime, such that the Angular compiler does not need to know about the lazy loaded feature modules at runtime. This is especially useful, when multiple teams are working on a project and independent deployment is necessary for productivity.

Although this is the key idea, this won’t work like that out-of-the-box, because Angular is not able to resolve the dependency at compile time. Webpack can be used to do some magic things under the hood, such that lazy loading works with the help of a module federation plugin.`,
  },
  {
    id: 4,
    img: "https://dummyimage.com/423x263",
    title: "React routing",
    date: "10 Sep 2022",
    content: `# Introduction
The key idea behind microfrontends is to lazy load code at runtime, such that the Angular compiler does not need to know about the lazy loaded feature modules at runtime. This is especially useful, when multiple teams are working on a project and independent deployment is necessary for productivity.

Although this is the key idea, this won’t work like that out-of-the-box, because Angular is not able to resolve the dependency at compile time. Webpack can be used to do some magic things under the hood, such that lazy loading works with the help of a module federation plugin.`,
  },
];
blogs = [];

export default blogs;
