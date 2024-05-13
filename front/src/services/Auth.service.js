
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';
let authToken = null;

class AuthService {

    token = "testundeuxundeux";

    user = null;

    isAuthenticated = false;

    async getTokenRegistration(username, password) {
        try {
            const response = await axios.post(`${API_URL}register/`, { username: username, password: password });
            AuthService.isAuthenticated = true;
            return response.data;
          } catch (error) {
            throw new Error('Sign-up failed');
        }
    };  

    async registerUser (username, password) {
        let token = await this.getTokenRegistration(username, password);
        this.isAuthenticated = true;
        this.user = token && token.user && token.user.username ? token.user.username : null;
        this.token = token && token.access ? token.access : null;
    };

    async createChatRoom (roomName) {
        console.log("AuthService.token")
        console.log(this.token);
        try {
                const response = await axios.post(`${API_URL}chatrooms/`, 
                { 
                    title: roomName, 
                    user: AuthService.user
                },
                {
                    headers: {
                    'Authorization': `Bearer ${this.token}`,
                    }
                }
                ).then(response => {
                    // Handle successful response
                  })
                  .catch(error => {
                    if (error.response) {
                      console.error('Error data:', error.response.data);
                      console.error('Error status:', error.response.status);
                      console.error('Error headers:', error.response.headers);
                    } else if (error.request) {
                  
                      console.error('Error request:', error.request);
                    } else {
                      // Something happened in setting up the request that triggered an Error
                      console.error('Error message:', error.message);
                    }
                    console.error('Error config:', error.config);
                  });
                return response.data;
            } catch (error) {
                // throw new Error('Create chatroom failed');
            }
        
    }

    async logUser (username, password) {
        try {
            const token = await axios.post(`${API_URL}login/`, { username: username, password: password }); 
            return token;
          } catch (error) {
            throw new Error('Login failed');
        }
    };

    async login (username, password) {
        let token = await this.logUser(username, password);
        token = token.data;
        this.isAuthenticated = true;
        console.log("token")
        console.log(token);
        this.user = token && token.user && token.user.username ? token.user.username : null;
        this.token = token && token.access ? token.access : null;
    }

}

export default new AuthService();