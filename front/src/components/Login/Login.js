import React, { useState } from 'react';
import AuthService from '../../services/Auth.service';
import { useNavigate } from 'react-router-dom';

import './Login.css';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate(); 

    const handleUsernameChange = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = async (e) => {    
        try {
            await AuthService.loginUser(username, password);
            console.log("Way to home :", AuthService.isAuthenticated);
            navigate('/home');
        } catch (error) {
            console.error(error);
        }
        e.preventDefault();
        // Add your login logic here
    };

    return (
        <div className='container'>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={handleUsernameChange}
                    />
                </div>
                <div>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={handlePasswordChange}
                    />
                </div>
                <div>
                    <a href="/register">Don't have an account? Register here</a>
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login;