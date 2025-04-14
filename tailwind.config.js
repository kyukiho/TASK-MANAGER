/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/**/*.{html,js,jsx,ts,tsx}", // Adjust paths based on your project structure
    ],
    theme: {
        extend: {
            colors: {
                primary: '#1D4ED8', // Example custom color
                secondary: '#9333EA',
            },
            spacing: {
                '128': '32rem', // Example custom spacing
            },
        },
    },
    plugins: [],
};