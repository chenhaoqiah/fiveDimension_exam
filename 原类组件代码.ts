import React, { Component } from 'react';

class MyComponent extends Component {
  state = {
    count: 0,
  };

  componentDidMount() {
    console.log('Component mounted');
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.count !== this.state.count) {
      console.log(`Count updated from ${prevState.count} to ${this.state.count}`);
    }
  }

  componentWillUnmount() {
    console.log('Component will unmount');
  }

  handleIncrement = () => {
    this.setState((prevState) => ({ count: prevState.count + 1 }));
  };

  render() {
    return (
      <div>
        <h1>Count: {this.state.count}</h1>
        <button onClick={this.handleIncrement}>Increment</button>
      </div>
    );
  }
}

export default MyComponent;