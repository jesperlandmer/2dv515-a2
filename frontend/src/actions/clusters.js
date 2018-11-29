/* eslint-disable default-case */
import axios from 'axios';

import { K_CLUSTER, H_CLUSTER, H_CLUSTER_GENERATE } from '../constants/actionTypes';
import { K_CLUSTER_ROOT, H_CLUSTER_ROOT } from '../constants/environment';

export function fetchKClusters(numOfClusters) {
  return {
    type: K_CLUSTER,
    payload: axios.get(`${K_CLUSTER_ROOT}/${numOfClusters}`),
  };
}

export function fetchHClusters() {
  return {
    type: H_CLUSTER,
    payload: axios.get(`${H_CLUSTER_ROOT}`),
  };
}
