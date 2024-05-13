

const Chatroom = () => {

    const [messages, setMessages] = useState([]);

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
}

// // Usage example:
// const chat = new Chatroom();
// chat.addMessage("Hello!");
// chat.addMessage("How are you?");
// console.log(chat.getMessages());