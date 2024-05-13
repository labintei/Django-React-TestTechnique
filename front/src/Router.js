import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './components/Home/Home';
import ChatLayout from './layouts/ChatLayout/ChatLayout';
import Login from './components/Login/Login';
import Register from './components/Register/Register';
import PrivateRoute from './PrivateRoute';

// Define your router component
const AppRouter = () => {

    return (
        <Router>
            <Routes>
                <Route exact path="/" element={<Navigate to="/login" />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/home" element={<PrivateRoute Component={ChatLayout} />} />
            </Routes>
        </Router>
    );
};

export default AppRouter;
