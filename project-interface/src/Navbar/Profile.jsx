import React from 'react';
import { motion } from 'framer-motion';
import { MdOutlineCancel } from 'react-icons/md';
import { useNavigate } from 'react-router-dom';
import firebase, { auth } from '../firebase'



export const Profile = ({ setShow }) => {
    const navigate = useNavigate()
    const currentColor = "black"
    return (
        <motion.div
            layoutId='profile'
            className="nav-item z-50 absolute border-2 right-2 top-2  bg-white  p-6 rounded-xl "
            // animate={{ y: 0, opacity: 1, transition: { default: { duration: 1, ease: [0, 0.71, 0.2, 1.01] } } }} initial={{ y: +60, opacity: 0 }} exit={{ y: -60, opacity: 0 }}
        >
            <button
                onClick={() => setShow(false)}
                className=' rounded-full flex items-center justify-center hover:shadow-lg absolute top-4 right-4 bg-blue-500 h-8 w-8'
            >
                <MdOutlineCancel className='fill-white' />
            </button>
            <div className="flex gap-5 items-center mt-4 border-color border-b-1 pb-6">
                <motion.img
                    layoutId='image'
                    className="rounded-full h-24 w-24"
                    src={auth.currentUser.photoURL}
                    alt="user-profile"
                />
                <div>
                    <p className="font-semibold text-xl dark:text-gray-600">Oussama AFTYS </p>
                    <p className="text-gray-500 text-sm dark:text-gray-400">  Administrator   </p>
                    <p className="text-gray-500 text-sm font-semibold dark:text-gray-400"> oussamaaftys@gmail.com </p>
                </div>
            </div>
            <div className="border-b-2 border-gray-300 w-full" />

            <div className="mt-5 relative h-12">
                <button
                    className=' absolute m-auto bg-blue-500 text-white  rounded-xl hover:shadow-md h-12 text-xl w-full'
                    onClick={() => {
                        firebase.auth().signOut().then(() => {
                            navigate("/Login")
                        })
                    }}>
                    Logout
                </button>
            </div>
        </motion.div >
    );
};


