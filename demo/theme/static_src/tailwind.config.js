/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    mode:'jit',

    content: [    
        '../../src/**/*.html',
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
    // that is animation class
      animation: {
        fade: 'fadeOut 5s ease-in-out',
      },

      // that is actual animation
      keyframes: theme => ({
        fadeOut: {
          '0%': { backgroundColor: theme('colors.red.300') },
          '100%': { backgroundColor: theme('colors.transparent') },
        },
      }),
        },
        rotate:{
            '-1':'-1deg',
            '-2':'-2deg',
            '-3':'-3deg',
            '-4':'-4deg',
            '-5':'-5deg',
            '-6':'-6deg',
            '-7':'-7deg',
            '-8':'-8deg',
            '-9':'-9deg',
            '-10':'-10deg',
            '-15':'-15deg',
            '-20':'-20deg',
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}