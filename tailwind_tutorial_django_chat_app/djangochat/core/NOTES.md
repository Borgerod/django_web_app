package.json

    npm init -y

install tailwind 

    npm i tailwindcss 

create src/style.css, then paste:

    @tailwind base;
    @tailwind components;
    @tailwind utilities;


    /* OPTIONAL EKSEMPEL */
    .listIcon {
        @apply h-6 w-6 flex-none fill-sky-100 stroke-sky-500 stroke-2;
    }

create dist/ #optionally "public/", then create:
    - index.html
    - style.css.html

make build-script in package.json:

    #in scripts, add: 
    "build:css": "tailwind build src/style.css -o dist/style.css",

run build-scrit:
    in cmd: 

    npm run build:css