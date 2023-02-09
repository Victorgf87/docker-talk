# Add Prometheus-community repo
helm repo add Prometheus-community \
https://prometheus-community.github.io/helm-charts

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack --namespace kubernetes-monitoring



kubectl port-forward prometheus-deployment-74dc6c7466-96bsq 8080:9090 -n monitoring