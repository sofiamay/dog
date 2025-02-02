module.exports = {
  extends: ["airbnb", "prettier"],
  plugins: ["prettier"],
  rules: {
    "prettier/prettier": ["error"],
  },
  env: {
    browser: true,
    node: true,
  },
};
