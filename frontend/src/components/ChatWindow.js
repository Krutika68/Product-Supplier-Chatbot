import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addMessage } from '../redux/actions'; // Redux action to store messages
import axios from 'axios';
import { TextField, Button, Box } from '@mui/material';

const ChatWindow = () => {
  const [input, setInput] = useState('');
  const messages = useSelector((state) => state.messages); // Get messages from Redux store
  const dispatch = useDispatch();

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (input) {
      // Dispatch user's message to Redux
      dispatch(addMessage({ text: input, sender: 'user' }));

      // Call the backend API for chatbot response
      try {
        const response = await axios.post('http://localhost:8000/chat', { query: input });
        dispatch(addMessage({ text: response.data.response, sender: 'bot' }));
      } catch (error) {
        console.error('Error fetching chatbot response:', error);
      }
      setInput(''); // Reset input field
    }
  };

  return (
    <Box>
      <div className="chat-history">
        {messages.map((msg, idx) => (
          <div key={idx} className={msg.sender}>
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Enter your query"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          fullWidth
        />
        <Button type="submit" variant="contained">Send</Button>
      </form>
    </Box>
  );
};

export default ChatWindow;
