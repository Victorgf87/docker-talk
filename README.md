# Add Prometheus-community repo
helm repo add Prometheus-community \
https://prometheus-community.github.io/helm-charts

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack --namespace kubernetes-monitoring