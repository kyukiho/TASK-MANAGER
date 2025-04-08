// src/index.js
import App from './App'; 
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './store/store'; // 正确导入命名导出

const root = createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
