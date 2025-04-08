// src/pages/Login/index.jsx
import React, { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { 
  faEnvelope, 
  faLock, 
  faEye, 
  faEyeSlash,
  faSpinner
} from '@fortawesome/free-solid-svg-icons';
import { 
  faQq, 
  faWeixin, 
  faGithub 
} from '@fortawesome/free-brands-svg-icons';

const Login = () => {
  const navigate = useNavigate();
  const formRef = useRef(null);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    remember: false
  });
  const [errors, setErrors] = useState({
    email: false,
    password: false
  });
  const [showPassword, setShowPassword] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [loginSuccess, setLoginSuccess] = useState(false);

  // 表单验证
  const validateForm = () => {
    const newErrors = {
      email: !/^\S+@\S+\.\S+$/.test(formData.email),
      password: formData.password.trim() === ''
    };
    setErrors(newErrors);
    return !Object.values(newErrors).some(Boolean);
  };

  // 提交处理
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) {
      formRef.current.classList.add('animate-shake');
      setTimeout(() => {
        formRef.current.classList.remove('animate-shake');
      }, 500);
      return;
    }

    setIsSubmitting(true);
    
    // 模拟 API 调用
    try {
      await new Promise(resolve => setTimeout(resolve, 2000));
      setLoginSuccess(true);
      
      setTimeout(() => {
        navigate('/dashboard');
      }, 1000);
    } catch (error) {
      console.error('登录失败:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  // 输入变化处理
  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
    
    // 实时验证
    if (name === 'email') {
      setErrors(prev => ({
        ...prev,
        email: !/^\S+@\S+\.\S+$/.test(value)
      }));
    }
    if (name === 'password') {
      setErrors(prev => ({
        ...prev,
        password: value.trim() === ''
      }));
    }
  };

  return (
    <div className="min-h-screen gradient-bg flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl p-8 w-full max-w-md card-shadow transition-transform duration-300 hover:scale-[1.02]">
        {/* 头部 */}
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <FontAwesomeIcon 
              icon={faEnvelope} 
              className="text-purple-500 text-3xl"
            />
          </div>
          <h1 className="text-3xl font-bold text-gray-800">邮箱登录</h1>
          <p className="text-gray-500 mt-2">欢迎回来，请登录您的账户</p>
        </div>

        {/* 表单 */}
        <form 
          ref={formRef}
          onSubmit={handleSubmit}
          className="space-y-6"
          noValidate
        >
          {/* 邮箱输入 */}
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
              邮箱地址
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <FontAwesomeIcon icon={faEnvelope} className="text-gray-400" />
              </div>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
                className={`pl-10 w-full px-4 py-3 rounded-lg border ${
                  errors.email ? 'border-red-500' : 'border-gray-300'
                } focus:border-purple-500 input-focus transition-all duration-200`}
                placeholder="请输入您的邮箱"
                disabled={isSubmitting}
              />
              {errors.email && (
                <p className="text-red-500 text-xs mt-1">请输入有效的邮箱地址</p>
              )}
            </div>
          </div>

          {/* 密码输入 */}
          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-1">
              密码
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <FontAwesomeIcon icon={faLock} className="text-gray-400" />
              </div>
              <input
                type={showPassword ? 'text' : 'password'}
                id="password"
                name="password"
                value={formData.password}
                onChange={handleInputChange}
                className={`pl-10 w-full px-4 py-3 rounded-lg border ${
                  errors.password ? 'border-red-500' : 'border-gray-300'
                } focus:border-purple-500 input-focus transition-all duration-200`}
                placeholder="请输入您的密码"
                disabled={isSubmitting}
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-3 text-gray-400 hover:text-gray-600"
              >
                <FontAwesomeIcon icon={showPassword ? faEyeSlash : faEye} />
              </button>
              {errors.password && (
                <p className="text-red-500 text-xs mt-1">密码不能为空</p>
              )}
            </div>
          </div>

          {/* 记住我 & 忘记密码 */}
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <input
                type="checkbox"
                id="remember"
                name="remember"
                checked={formData.remember}
                onChange={handleInputChange}
                className="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300 rounded"
                disabled={isSubmitting}
              />
              <label htmlFor="remember" className="ml-2 block text-sm text-gray-700">
                记住我
              </label>
            </div>
            <a href="#" className="text-sm text-purple-600 hover:text-purple-500 hover:underline">
              忘记密码?
            </a>
          </div>

          {/* 提交按钮 */}
          <button
            type="submit"
            disabled={isSubmitting || loginSuccess}
            className={`w-full text-white py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-purple-400 focus:ring-opacity-50 transition-all duration-200 flex items-center justify-center ${
              loginSuccess 
                ? 'bg-green-500 hover:bg-green-600' 
                : 'bg-gradient-to-r from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700'
            }`}
          >
            {isSubmitting ? (
              <>
                <span>登录中...</span>
                <FontAwesomeIcon 
                  icon={faSpinner} 
                  className="ml-2 animate-spin" 
                />
              </>
            ) : loginSuccess ? (
              '登录成功'
            ) : (
              '登录'
            )}
          </button>

          {/* 注册链接 */}
          <div className="text-center text-sm text-gray-500">
            还没有账户?{' '}
            <a href="#" className="text-purple-600 hover:text-purple-500 hover:underline">
              立即注册
            </a>
          </div>
        </form>

        {/* 第三方登录 */}
        <div className="mt-8 pt-6 border-t border-gray-200">
          <p className="text-xs text-gray-500 text-center">或使用以下方式登录</p>
          <div className="flex justify-center space-x-4 mt-4">
            <button className="w-10 h-10 rounded-full bg-blue-100 text-blue-500 flex items-center justify-center hover:bg-blue-200 transition-colors">
              <FontAwesomeIcon icon={faQq} />
            </button>
            <button className="w-10 h-10 rounded-full bg-red-100 text-red-500 flex items-center justify-center hover:bg-red-200 transition-colors">
              <FontAwesomeIcon icon={faWeixin} />
            </button>
            <button className="w-10 h-10 rounded-full bg-gray-100 text-gray-700 flex items-center justify-center hover:bg-gray-200 transition-colors">
              <FontAwesomeIcon icon={faGithub} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;