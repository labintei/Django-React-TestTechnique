import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from './ChatAsideBar.module.css';
import AuthService from '../../services/Auth.service';

const ChatAsideBar = () => {
    const [roomName, setRoomName] = useState('');
    const [rooms, setRooms] = useState(["room1","room2","room3","room4"]);
    const [popuphidden, setPopuphidden] = useState(false);

    useEffect(() => {
        const fetchChatrooms = async () => {
          try {
            const response = await AuthService.getChatRooms();
            console.log(response);
            // setRooms(response.data);
          } catch (error) {
            console.error('Error fetching chatrooms:', error);
          }
        };
        fetchChatrooms();
    }, []);
    
    const handleCreateRoom = () => {
        setRoomName('');
        setPopuphidden(false)

    };

    return (
        <div className={styles.container}>
            <button onClick={() => setPopuphidden(true)}>Create Room</button>
            {/* Render the list of rooms */}
            {rooms.map((room, index) => (
                <div key={index}>{room}</div>
            ))}
            {popuphidden && <div className={styles.popup}>
                <div className={styles.closeButton} onClick={() => setPopuphidden(false)}>X</div>
                <div>Create your own room</div>
                <input
                    type="text"
                    value={roomName}
                    onChange={(e) => setRoomName(e.target.value)}
                    placeholder="Enter room name"
                />
                <button onClick={handleCreateRoom}>Submit</button>
            </div>}
            {/* <div >Popup</div> */}
        </div>
    );
};

export default ChatAsideBar;