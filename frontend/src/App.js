import React, { Component } from 'react';
import { Checkbox } from 'carbon-components-react'
// import './app.scss'

class App extends Component {
  state = {
    data: null
  };

  async componentDidMount() {
    try {
      // const res = await fetch('https://reqbin.com/echo/post/json',
      //   {
      //     method: 'POST',
      //     body: JSON.stringify({
      //       "Id": 12345,
      //       "Customer": "John Smith",
      //       "Quantity": 1,
      //       "Price": 10.00
      //     })
      //   });
      // const data = await res.json();
      const data = {
        "hello": "good"
      }
      console.log(data)
      this.setState({
        data: data
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {JSON.stringify(this.state.data)}
        <p>test</p>
        <fieldset className="bx--fieldset">
          <legend className="bx--label">Checkbox heading</legend>
          <Checkbox defaultChecked labelText="Checkbox label" id="checked" />
          <Checkbox labelText="Checkbox label" id="checked-2" />
        </fieldset>
      </div>
    );
  }
}

export default App;