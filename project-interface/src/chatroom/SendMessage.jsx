import React, { useState } from 'react';
import { doc, setDoc, collection, addDoc, updateDoc, arrayUnion, getDoc, serverTimestamp } from 'firebase/firestore';
import { auth, db } from '../firebase';
import axios from 'axios';

export const SendMessage = ({ count, setCount }) => {
  const [input, setInput] = useState('');

  const sendMessage = async (e) => {
    e.preventDefault();
    if (input === '') {
      alert('Please enter a valid message');
      return;
    }
  
    const { uid, displayName, photoURL } = auth.currentUser;
    const userMessagesRef = doc(db, 'messages', uid);
    const test = input;
    setInput('');
  
    const userMessagesSnapshot = await getDoc(userMessagesRef);
  
    if (userMessagesSnapshot.exists()) {
      await updateDoc(userMessagesRef, {
        messages: arrayUnion({
          text: test,
          name: displayName,
          uid: 'user',
          photoURL,
          timestamp: new Date()
        })
      });
    } else {
      await setDoc(userMessagesRef, {
        messages: [{
          text: test,
          name: displayName,
          uid: 'user',
          photoURL,
          timestamp: new Date()
        }]
      });
    }
  
    
    setCount((prevCount) => prevCount + 1);
    await new Promise((resolve) => setTimeout(resolve, 1000)); // Add a delay of 1 second (1000 milliseconds)
    try {const response = await axios.post('http://localhost:5000/message', {
      message: test
    });
    await updateDoc(userMessagesRef, {
      messages: arrayUnion({
        text: response.data.response,
        name: 'chat-bot',
        uid: 'chatbot',
        photoURL,
        timestamp: new Date()
      })
    });
    }catch{
      await updateDoc(userMessagesRef, {
        messages: arrayUnion({
          text: "une error produced while trying to treat  your command! please try again.",
          name: 'chat-bot',
          uid: 'chatbot',
          photoURL,
          timestamp: new Date()
        })
      });

    }
  
    setCount((prevCount) => prevCount + 1);
  };
  

  return (
    <form
      className="fixed flex gap-2 mx-auto w-full max-w-screen-lg h-[40px] bottom-2 justify-around w-full flex items-center text-lg"
      onSubmit={sendMessage}
    >
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        type="text"
        placeholder="Message"
        className="w-5/6 h-[40px] text-lg bg-gray-100 text-black outline-none rounded-full pr-[10px] text-center"
      />
      <button
        type="submit"
        className="h-[40px] w-1/6 bg-gray-500 rounded-full text-white flex items-center justify-center p-3 inline-block disabled:opacity-50 disabled:cursor-not-allowed"
      >
        Send
      </button>
    </form>
  );
};
