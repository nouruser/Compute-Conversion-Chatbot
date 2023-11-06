import React, { useState, useEffect, useRef } from 'react';
import { query, collection, orderBy, onSnapshot, doc, addDoc, serverTimestamp, getDoc } from 'firebase/firestore';
import { Message,SendMessage } from '.';
import Navbar from '../Navbar';
import { db, auth } from '../firebase';

export const ChatRoom = () => {
  const [messages, setMessages] = useState([]);
  const [count, setCount] = useState(1);
  const scroll = useRef();

  const getMessages = async () => {
    const userMessagesRef = doc(db, 'messages', auth.currentUser.uid);
    try {
      const userMessagesSnapshot = await getDoc(userMessagesRef);
      const userMessagesData = userMessagesSnapshot.data();
      if (userMessagesData && userMessagesSnapshot.exists()) {
        setMessages(userMessagesData.messages);
      }
    } catch (error) {
      console.error('Error getting messages:', error);
    }
  };

  useEffect(() => {

    getMessages();
    scroll.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
  }, [count]);

  return (
    <>
      <Navbar />
      <main className="fixed bottom-[70px] top-[10px] w-full max-w-screen-lg bg-white rounded-2xl pt-10 px-4 overflow-y-auto flex flex-col justify-start gap-5">
        {messages.map((message) => (
          <Message key={message.id} message={message} scroll={scroll} />
        ))}
        <span ref={scroll} className="h-10 w-10 mb-[100px]"></span>
      </main>
      <SendMessage count={count} setCount={setCount} setMessages={setMessages} />
    </>
  );
};
