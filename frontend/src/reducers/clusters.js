import { K_CLUSTER, H_CLUSTER, H_CLUSTER_GENERATE } from '../constants/actionTypes';

const initialState = {
  loading: false,
  clusters: [],
  showHCluster: false,
  message: null
}

export default (state = initialState, action) => {
  switch(action.type) {
    case `${H_CLUSTER_GENERATE}_PENDING`:
      return { ...state, loading: true }
    case `${H_CLUSTER_GENERATE}_REJECTED`:
      return {...state, loading: false, message: 'Failed' }
    case `${H_CLUSTER_GENERATE}_FULFILLED`:
      return {...state, loading: false, message: 'Done!' }

    case `${K_CLUSTER}_REJECTED`:
      return {...state, clusters: [], showHCluster: false }
    case `${K_CLUSTER}_FULFILLED`:
      return {...state, clusters: action.payload.data, showHCluster: false }
    case `${H_CLUSTER}`:
      return {...state, clusters: [], showHCluster: true }
    default:
      return state;
  }
}
