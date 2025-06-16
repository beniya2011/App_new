import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = ({ userId }) => {
  const [data, setData] = useState([]);
  const [source, setSource] = useState("");

  useEffect(() => {
    axios.get(`/get-data?user_id=${userId}`)
      .then(res => {
        setData(res.data.data.records);
        setSource(res.data.source);
      });
  }, [userId]);

  const updateData = () => {
    const newData = { records: ['record_updated_1', 'record_updated_2'] };
    axios.post(`/update-data?user_id=${userId}`, { data: newData })
      .then(() => alert("Cache updated"));
  };

  return (
    <div>
      <h3>Source: {source}</h3>
      <button onClick={updateData}>Update Cache</button>
      <ul>
        {data.slice(0, 10).map((item, i) => <li key={i}>{item}</li>)}
      </ul>
    </div>
  );
};

export default Dashboard;
