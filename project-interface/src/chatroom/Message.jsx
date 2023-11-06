import React, { useEffect } from 'react';
import { motion } from 'framer-motion';
import { auth, db } from '../firebase'

export const Message = ({ message, scroll }) => {

  const {text,uid} = message;
  const sent = (uid === "user");
  useEffect(() => { scroll.current.scrollIntoView({ behavior: 'smooth' }) }, []);

  return (
    <div
      className={`flex items-start   relative justify-start gap-3  px-4 ${sent ? 'flex-row-reverse' : ''}`} >
      {/* <img src={photoURL || 'anonymos.jpeg'} className="w-10 h-10 rounded-full" />  */}
      <motion.div

        initial={{ opacity: 0, scale: 0.5 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{
          default: {
            duration: 0.3,
            ease: [0, 0.71, 0.2, 1.01]
          },
          scale: {
            type: "easeIn",
            damping: 5,
            stiffness: 100,
            restDelta: 0.001
          }
        }}
        style={{ backgroundColor: sent ? "#2563eb" : "gray", maxWidth: "200px", wordWrap: "break-word" }}
        className={!sent ?
          ` leading-6 text-white  ma px-4  py-2 flex justify-center items-center rounded-r-2xl rounded-bl-2xl ` :
          ` leading-6 text-white px-4  py-2 flex justify-center items-center rounded-l-2xl rounded-br-2xl ml-4`
        }>
        <p className='text-xl'>{text}</p>
      </motion.div>
    </div>
  )
};
