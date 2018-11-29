import React, { Component } from 'react';
import { connect } from 'react-redux';
import { FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap';
import { clustMethods } from '../constants/environment';
import { fetchHClusters, postGenerateHCluster, fetchKClusters } from '../actions/clusters';

const mapStateToProps = state => ({
    loading: state.clusters.loading,
  })

class ClusterSelector extends Component {

    constructor(props) {
        super(props);
        this.state = {
            clustMethod: null,
            numOfClusters: 0,
            algorithm: null,
        }

        this.handleClustChange = this.handleClustChange.bind(this);
        this.handleClustNumChange = this.handleClustNumChange.bind(this);
        this.handleGenerate = this.handleGenerate.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.createTable = this.createTable.bind(this)
    }

    handleClustChange(e) {
        this.setState({ clustMethod: e.target.value });
    }

    handleClustNumChange(e) {
        this.setState({ numOfClusters: e.target.value });
    }

    handleGenerate() {
        const { dispatch } = this.props;
        dispatch(postGenerateHCluster())
    }

    handleSubmit(e) {
        const { dispatch } = this.props;
        const { numOfClusters } = this.state;
        
        if (this.state.clustMethod === 'k-cluster') {
            dispatch(fetchKClusters(numOfClusters))
        } else if (this.state.clustMethod === 'h-cluster') {
            dispatch(fetchHClusters())
        }
    }

    createTable = () => {
        let table = []
        for (let i = 0; i <= 5; i++) {
          table.push(<option key={i} value={i}>{i}</option>)
        }
        return table
    }

  render() {

    return (
        <form style={{ 'margin-top': '50px'}}>
        <ControlLabel>K-cluster or Hierarchical Cluster</ControlLabel>
        <FormGroup controlId="clustMethod">
            <FormControl componentClass="select" placeholder="select" onChange={this.handleClustChange}>
                <option value="select">select</option>
                {Object.keys(clustMethods).map((key, id) => <option key={id} value={key}>{key}</option> )}
            </FormControl>
        </FormGroup>

        {this.state.clustMethod === 'k-cluster' &&
            <div>
                <ControlLabel>Number of clusters</ControlLabel>
                <FormGroup controlId="clustMethod">
                    <FormControl componentClass="select" placeholder="select" onChange={this.handleClustNumChange}>
                        {this.createTable()}
                    </FormControl>
                </FormGroup>
            </div>
        }

        <Button bsStyle="primary" type="button" onClick={this.handleSubmit}>Display Result</Button>
    </form>
    );
  }
}

export default connect(mapStateToProps)(ClusterSelector);
