import { auth } from "./firebase";
import './App.css';
import { AnimatePresence } from 'framer-motion';
import { BrowserRouter, Routes, Route, Navigate, useNavigate } from 'react-router-dom';
import { ChatRoom } from './chatroom';
import { onAuthStateChanged } from 'firebase/auth';
import { useEffect } from 'react';
import Login from './Login';
import Signup from './Signup';

const PrivateRoute = ({ auth, children }) => {
  return auth ? (
    <>{children}</>
  ) : (
    <Navigate to="/Login" replace={true} />
  );
};

export default function App() {
  // const navigate=useNavigate()
  // const checkUserSignIn = () => {
  //   onAuthStateChanged(auth, (user) => {
  //     if (user) {
  //       navigate("/Login");
  //     } else {
  //       // Handle the case when the user is not signed in
  //     }
  //   });
  // };

  // useEffect(() => {
  //   checkUserSignIn();
  // }, []);

  return (
    <div className="min-h-screen w-screen bg-gray-200 flex flex-col  pb-[130px] pt-[60px] items-center justify-start gap-4">
      <BrowserRouter>
          <Routes>
            <Route path="/Login" element={<Login />} />
            <Route path="/Signup" element={<Signup />} />
            <Route
              path="/"
              element={<PrivateRoute auth={auth}><ChatRoom /></PrivateRoute>}
            />
          </Routes>
      </BrowserRouter>
    </div>
  );
}
