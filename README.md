# Nastya Project

A complete development environment setup with all necessary dependencies, tools, and configurations.

## Features

- **Package Management**: Complete `package.json` with all dependencies
- **Linting**: ESLint configuration with Airbnb style guide
- **Development Server**: Webpack dev server setup
- **Testing**: Jest testing framework
- **Process Management**: Nodemon for development
- **Build Tools**: Webpack for bundling

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

## Available Scripts

- `npm start` - Start the application
- `npm run dev` - Start development server with nodemon
- `npm run test` - Run tests with Jest
- `npm run lint` - Lint JavaScript files
- `npm run lint:fix` - Automatically fix linting issues
- `npm run build` - Build for production
- `npm run serve` - Start development server with webpack

## Project Structure

```
.
├── src/                 # Source files
├── test/                # Test files
├── dist/                # Build output
├── config/              # Configuration files
├── package.json         # Project configuration
├── webpack.config.js    # Webpack configuration
├── .eslintrc.json       # ESLint configuration
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Dependencies

- **Core**: Express.js, Lodash
- **Development Tools**: Webpack, Webpack Dev Server, Nodemon
- **Testing**: Jest, Supertest
- **Linting**: ESLint with Airbnb configuration

## Environment Setup

The development environment is ready with:
- ES6+ JavaScript support
- Automatic linting
- Hot reloading development server
- Unit testing framework
- Production build capabilities