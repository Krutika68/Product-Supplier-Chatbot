import React from 'react';
import { Provider } from 'react-redux';
import ChatWindow from './components/ChatWindow';
import { createStore } from 'redux';
import chatReducer from './redux/reducer';

const store = createStore(chatReducer);

function App() {
  return (
    <Provider store={store}>
      <ChatWindow />
    </Provider>
  );
}

export default App;
