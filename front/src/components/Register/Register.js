import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import AuthService from '../../services/Auth.service';


function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate(); 
    // const history = useHistory(); // Initialize useHistory hook

    const handleUsernameChange = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = async (e) => {    
        e.preventDefault(); // Prevent default form submission behavior

        try {
            await AuthService.registerUser(username, password);
            navigate('/home');
        } catch (error) {
            console.error(error);
            // Handle registration error
        }
    };

    return (
        <div className='container'>
            <h2>Register</h2>
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
                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default Register;
