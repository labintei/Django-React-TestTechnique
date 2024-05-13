
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';
let authToken = null;

class AuthService {

    token = "testundeuxundeux";

    user = null;

    isAuthenticated = false;

    async getTokenRegistration(username, password) {
        try {
            const response = await axios.post(`${API_URL}register/`, { login: username, password });
            AuthService.isAuthenticated = true;
            AuthService.token = response.data.token;
            console.log("Register response");
            console.log(AuthService.token);
            return response.data;
          } catch (error) {
            throw new Error('Sign-up failed');
        }
    };  

    async registerUser (username, password) {
        let token = await this.getTokenRegistration(username, password);
        this.isAuthenticated = true;
        // this.loginUser(username, password);
        console.log("this is the token");
        console.log(token);
    };

    async getChatRooms () {
        try {
            console.log("Get Rooms Chat");
            console.log(AuthService.token);
            // const response = await axios.get(`${API_URL}chatrooms/`, { headers: { 
            //     Authorization: 
            //         `Bearer ${AuthService.token}`, 
            //         'Content-Type': 'application/json'}});
            
            const response = await axios.options(`${API_URL}options/`, { headers: {
                Authorization: 
                    `Bearer ${AuthService.token}`, 
                    'Content-Type': 'application/json'}, date : {text: "test"}});
            return response.data;
          } catch (error) {
            throw new Error('Get chatrooms failed');
        }
    };

    logUser (username, password) {
        try {
            const response = this.loginUser   
            return response.data;
          } catch (error) {
            throw new Error('Login failed');
        }
    };

    // async loginUser (username, password) {
    //     try {
    //         const response = await axios.post(`${API_URL}login/`, { login: username, password });
    //         AuthService.isAuthenticated = true;
    //         this.isAuthenticated = true;
    //         this.token = response.data.token;
    //         console.log("this is the answer");
    //         console.log(response.data);
    //         return response.data;
    //       } catch (error) {
    //         throw new Error('Login failed');
    //     }
    // };

    // logoutUser (username, password) {
    //     try {
    //         const response = axios.post(`${API_URL}logout/`);
    //         AuthService.isAuthenticated = false;
    //         return response.data;
    //       }
    //         catch (error) {
    //             throw new Error('Logout failed');
    //     }
    // };

    // Add any additional methods or functionality as needed

}

export default new AuthService();

// try {
        //     const response = axios.post(`${API_URL}register/`, { login: username, password });
        //     AuthService.isAuthenticated = true;
        //     console.log("this is the answer");
        //     console.log(response.data);
        //     return response.data;
        //   } catch (error) {
        //     throw new Error('Sign-up failed');
        // }