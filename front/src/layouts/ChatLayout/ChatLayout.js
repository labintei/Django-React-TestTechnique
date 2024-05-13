import React from 'react';
import styles from './ChatLayout.module.css';
import ChatAsideBar from '../../components/ChatAsideBar/ChatAsideBar';

const ChatLayout = () => {
    return (
        <div className={styles.layout}>
            <div className={styles.header}></div>
            <div className={styles.content}>
                <div className={styles.aside}>
                    <ChatAsideBar></ChatAsideBar>
                </div>
                
                <div className={styles.chat}></div>
            </div>
        </div>
    );
};

export default ChatLayout;