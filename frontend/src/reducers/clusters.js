import { K_CLUSTER, H_CLUSTER } from '../constants/actionTypes';

const initialState = {
  kclusters: [],
  hclusters: {},
}

export default (state = initialState, action) => {
  switch(action.type) {
    case `${H_CLUSTER}_REJECTED`:
      return {...state, kclusters: [], hclusters: {} }
    case `${H_CLUSTER}_FULFILLED`:
      return {...state, kclusters: [], hclusters: action.payload.data }

    case `${K_CLUSTER}_REJECTED`:
      return {...state, kclusters: [], hclusters: [] }
    case `${K_CLUSTER}_FULFILLED`:
      return {...state, kclusters: action.payload.data, hclusters: {} }
    default:
      return state;
  }
}
