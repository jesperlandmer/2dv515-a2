// use 'proxy' field in package.json to send requests, avoiding CORS issues
// eslint-disable-next-line import/prefer-default-export
export const K_CLUSTER_ROOT = '/api/kcluster';
export const H_CLUSTER_ROOT = '/api/hcluster';

export const clustMethods = {
    'k-cluster': [],
    'h-cluster': ['generate', 'tree'],
}