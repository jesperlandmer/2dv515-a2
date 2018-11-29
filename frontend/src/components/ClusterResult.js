import React, { Component } from 'react';
import { connect } from 'react-redux';
import Tree from 'react-d3-tree';

const mapStateToProps = state => ({
  kclusters: state.clusters.kclusters,
  hclusters: state.clusters.hclusters,
})

class ClusterResult extends Component {

  render() {
    return (
    <div>
        {this.props.kclusters.length > 0 && 
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
        {Object.keys(this.props.hclusters).length > 0 &&
                <div id="treeWrapper" style={{width: '50em', height: '20em'}}>
 
                <Tree data={this.props.hclusters} />
         
              </div>
        }
    </div>
    );
  }
}

export default connect(mapStateToProps)(ClusterResult);
