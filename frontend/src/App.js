import React, { Component } from 'react';
import { connect } from 'react-redux';

import ClusterSelector from './components/ClusterSelector';
import ClusterResult from './components/ClusterResult';
import logo from './assets/img/logo.svg';

class App extends Component {

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to the Blog Cluster System</h2>
        </div>
        <p className="App-intro">
          Select cluster method to use on the blogset
          <ClusterSelector user={this.props.user}/>
        </p>

        <ClusterResult />
      </div>
    );
  }
}

export default connect()(App);
