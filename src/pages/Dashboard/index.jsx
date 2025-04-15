import React, { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
const Dashboard = () => {
    const navigate = useNavigate();
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        const fetchData = async () => {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/posts');
            if (!response.ok) {
            throw new Error('Network response was not ok');
            }
            const result = await response.json();
            setData(result);
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false);
        }
        };
    
        fetchData();
    }, []);
    
    if (loading) {
        return <div>Loading...</div>;
    }
    
    return (
        <div>
        <h1>Dashboard</h1>
        <ul>
            {data.map(item => (
            <li key={item.id}>{item.title}</li>
            ))}
        </ul>
        </div>
    );
}
export default Dashboard;