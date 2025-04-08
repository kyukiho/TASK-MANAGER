// src/features/auth/authThunks.js
import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../../api/firebase';
import { setLoading, setError, setUser } from './authSlice';

export const loginUser = (credentials) => async (dispatch) => {
  try {
    dispatch(setLoading(true));
    const userCredential = await signInWithEmailAndPassword(
      auth,
      credentials.email,
      credentials.password
    );
    
    dispatch(setUser({
      uid: userCredential.user.uid,
      email: userCredential.user.email
    }));
  } catch (error) {
    let errorMessage = '登录失败，请重试';
    switch(error.code) {
      case 'auth/user-not-found':
        errorMessage = '用户不存在';
        break;
      case 'auth/wrong-password':
        errorMessage = '密码错误';
        break;
    }
    dispatch(setError(errorMessage));
  } finally {
    dispatch(setLoading(false));
  }
};