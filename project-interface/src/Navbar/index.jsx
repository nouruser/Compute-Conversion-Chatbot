import { auth } from "../firebase"
import firebase from "../firebase"
import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"
import { Profile } from "./Profile"
import { AnimatePresence, motion } from "framer-motion"


const Navbar = () => {

    const { displayName, photoURL } = auth.currentUser;
    const [show, setShow] = useState(false)
    return (

        <>
            <AnimatePresence >
                {!show ? (<motion.div onClick={() => setShow(!show)} layoutId='profile' className="fixed h-15 p-2 px-4 gap-3  z-30  top-2 right-2  border-2 border-gray rounded-xl bg-white flex items-center">
                    
                    <motion.img
                        layoutId='image'
                        className="rounded-2xl h-10"
                        src={photoURL} />
                    <p className="text-xl">{displayName}</p>

                </motion.div>)
                    :
                    (<Profile setShow={setShow} />)}
            </AnimatePresence>

        </>
    )
}

export default Navbar