import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Table } from 'react-bootstrap';

const mapStateToProps = state => ({
  clusters: state.clusters.clusters,
  showHCluster: state.clusters.showHCluster,
})

class ClusterResult extends Component {

  render() {
    return (
    <div>
        {this.props.clusters.length > 0 && 
          this.props.clusters.map((blog, key) => 
            <div style={{ display: 'inline-block', verticalAlign:'top', fontSize: '12px', marginTop: '3vh'}}>
              {blog.cluster.map((b) =>
                blog.cluster[blog.cluster.length - 1].name !== b.name ?
                  <p style={{ marginBottom: 0 }}>{b.name} <br/> -</p>
                  :
                  <p style={{ marginBottom: 0 }}>{b.name}</p>
              )}
            </div>
          )
        }
        {this.props.showHCluster &&
          <img src="/api/hcluster/tree.jpg"></img>
        }
    </div>
    );
  }
}

export default connect(mapStateToProps)(ClusterResult);
