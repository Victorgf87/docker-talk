# Add Prometheus-community repo
helm repo add Prometheus-community \
https://prometheus-community.github.io/helm-charts

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update


helm repo add elastic https://helm.elastic.co
helm repo update

Using VScode Kubernetes plugin:
- Install eck-operator
- Install eck-operator-crds 2.6.1
- Install eck-elasticsearch
- Install eck-kibana


1. Check Kibana status
  $ kubectl get kibana eck-kibana-1676021859 -n default

2. Check Kibana pod status
  $ kubectl get pods --namespace=default -l kibana.k8s.elastic.co/name=eck-kibana-1676021859



kubectl get nodes
kubectl drain <node-name>
kubectl delete node <node-name>

sudo microk8s reset --destroy-storage


microk8s leave
microk8s.kubectl get nodes
microk8s remove-node <name-of-the-node>