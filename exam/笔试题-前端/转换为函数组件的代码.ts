import React, { useState, useEffect } from 'react';

const MyComponent: React.FC = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('Component mounted');

    return () => {
      console.log('Component will unmount');
    };
  }, []);

  useEffect(() => {
    console.log(`Count updated to ${count}`);
  }, [count]);

  const handleIncrement = () => {
    setCount((prevCount) => prevCount + 1);
  };

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={handleIncrement}>Increment</button>
    </div>
  );
};

export default MyComponent;