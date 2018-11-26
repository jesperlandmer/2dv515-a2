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
  };
}

export function postGenerateHCluster() {
  return {
    type: H_CLUSTER_GENERATE,
    payload: axios.post(`${H_CLUSTER_ROOT}/generate`),
  };
}
