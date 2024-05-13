import React from 'react';

const Home = () => {
    const handleLogout = () => {
        // Add your logout logic here
    };

    return (
        <div>
            <h1>Welcome to the Chatroom!</h1>
            <p>Start chatting with your friends.</p>
            
            {/* Add your chatroom components here */}
            
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

export default Home;