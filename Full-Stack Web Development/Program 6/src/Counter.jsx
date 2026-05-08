import React, { useState, useEffect } from 'react';

const Counter = () => {
    const [count, setCount] = useState(0);

    // Simulate fetching initial data for the Counter component
    useEffect(() => {
    setTimeout(() => {
        setCount(0);  // Set initial value after 2 seconds
     }, 2000);
     }, []);

     return (
            <div>
            <h1>Counter: {count}</h1>
            <button onClick={() => setCount(count + 1)}>Increment</button>
            <button onClick={() => setCount(count - 1)}>Decrement</button>
            <button onClick={() => setCount(count * 2)}>Double</button>
              <button onClick={() => setCount(0)}>Reset</button>
         </div>
         );
};

export default Counter;

