import React, { useState } from 'react';
import axios from 'axios';
import './ChatBotPage.css'; // Assuming you'll save the CSS in this file

export function ChatBotPage() {
    const [input, setInput] = useState(""); // Store current user input
    const [conversation, setConversation] = useState([]); // Store conversation history

    // Function to handle form submission
    const handleSubmit = async (event) => {
        event.preventDefault();
        
        if (input.trim() === "") return; // Prevent empty submissions

        // Add the user's message to the conversation
        const newMessage = { sender: 'user', text: input };
        setConversation(prev => [...prev, newMessage]);

        // Clear the input field
        setInput("");

        // Send the user's message to the backend in the required format
        try {
            const response = await axios.post('http://localhost:8000/api/chat/', {
                prompt: input,  // Use 'prompt' as the key for the user input
            });

            // Extract the assistant's message content from the backend response
            const botResponseContent = response.data.response[0]?.message?.content || "No response from the assistant";

            // Add the bot's response to the conversation
            const botResponse = { sender: 'bot', text: botResponseContent };
            setConversation(prev => [...prev, botResponse]);

        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    return (
        <div className="chat-container">
            <div className="chat-box">
                {conversation.map((msg, index) => (
                    <div key={index} className={msg.sender === 'user' ? 'user-message' : 'bot-message'}>
                        <div className="message">
                            <strong>{msg.sender === 'user' ? 'You' : 'Bot'}:</strong> {msg.text}
                        </div>
                    </div>
                ))}
            </div>

            <form onSubmit={handleSubmit} className="input-form">
                <textarea 
                    rows="3" 
                    placeholder="What do you want to know?" 
                    value={input} 
                    onChange={(e) => setInput(e.target.value)} // Handle input change
                    className="input-textarea"
                ></textarea>
                <button type="submit" className="submit-button">Submit</button>
            </form>
        </div>
    );
}



