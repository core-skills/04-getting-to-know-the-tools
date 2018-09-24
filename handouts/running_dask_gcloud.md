We assume that you're running on Google Cloud - you should have an account set up and a project ready to go. You will need to enable the kubernetes API in Google Cloud to be able to create kubernetes clusters.

### Install tools

Install gcloud SDK and k8s tools using brew

```bash
$ brew cask install google-cloud-sdk
$ brew install kubernetes-cli kubernetes-helm
```

Use `upgrade` instead of `install` if already installed

Then set up config

```bash
$ gcloud config list
```
```
[compute]
region = australia-southeast1
zone = australia-southeast1-b
[core]
account = jess.c.robertson@gmail.com
disable_usage_reporting = True
project = jess-test-project
```

Then we can set the relevant project and this should give us access to the relevant k8s APIs

```bash
$ gcloud config set project core-skills-binder
```
```
Updated property [core/project].
```

### Spin up kubernetes cluster

Then we can spin up the k8s cluster with

```bash
$ gcloud container clusters create test-dask \
	--num-nodes=4 \
	--machine-type=n1-standards-2
```

```
# snip warning messages
Creating cluster test-dask...⠧
```

Check that things are running

```bash
$ kubectl get node
```
```
NAME                                       STATUS    ROLES     AGE       VERSION
gke-test-dask-default-pool-b33d6013-dnmd   Ready     <none>    24m       v1.9.7-gke.6
gke-test-dask-default-pool-b33d6013-rj5p   Ready     <none>    25m       v1.9.7-gke.6
gke-test-dask-default-pool-b33d6013-skqs   Ready     <none>    24m       v1.9.7-gke.6
gke-test-dask-default-pool-b33d6013-t2r0   Ready     <none>    25m       v1.9.7-gke.6
```

Then give your account super-user permissions
```bash
$ kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user=jesse.robertson@csiro.au
```
```
clusterrolebinding.rbac.authorization.k8s.io/cluster-admin-binding created
```

### Sort out helm

Next we can initialize helm on our cluster

```bash
$ kubectl --namespace kube-system create sa tiller
```
```
serviceaccount/tiller created
```
```bash
$ kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
```
```
clusterrolebinding.rbac.authorization.k8s.io/tiller created
```
```bash
$ helm init --service-account tiller
```
```
$HELM_HOME has been configured at /Users/jess/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
Happy Helming!
```

and we're good to go! You can make sure that you've got things installed correctly using 

```bash
$ helm version
```
```
Client: &version.Version{SemVer:"v2.10.0", GitCommit:"9ad53aac42165a5fadc6c87be0dea6b115f93090", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.10.0", GitCommit:"9ad53aac42165a5fadc6c87be0dea6b115f93090", GitTreeState:"clean"}
```

### Installing dask

Then we just use the helm chart to install dask on our cluster. We've got some extra config values that we want the chart to use:

```yaml
# file: dask-config.yaml
# Worker config
worker:
  replicas: 8
  resources:
    limits:
      cpu: 2
      memory: 7.5G
    requests:
      cpu: 2
      memory: 7.5G
  env:
    - name: EXTRA_CONDA_PACKAGES
      value: numba xarray -c conda-forge
    - name: EXTRA_PIP_PACKAGES
      value: s3fs dask-ml --upgrade

# We want to keep the same packages on the worker and jupyter environments
jupyter:
  enabled: true
  env:
    - name: EXTRA_CONDA_PACKAGES
      value: numba xarray matplotlib -c conda-forge
    - name: EXTRA_PIP_PACKAGES
      value: s3fs dask-ml --upgrade
```

This means that we can just deploy using the following

```bash
$ helm repo update
$ export NAME=analytics
$ helm install --name $NAME stable/dask -f dask-config.yaml
```
```
NAME:   analytics
LAST DEPLOYED: Mon Sep 24 08:22:13 2018
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/ConfigMap
NAME                                       DATA  AGE
analytics-dask-jupyter-config  1     0s

==> v1/Service
NAME                                  TYPE          CLUSTER-IP     EXTERNAL-IP  PORT(S)                      AGE
analytics-dask-jupyter    LoadBalancer  10.39.251.125  <pending>    80:30598/TCP                 0s
analytics-dask-scheduler  LoadBalancer  10.39.240.115  <pending>    8786:30203/TCP,80:31661/TCP  0s

==> v1beta2/Deployment
NAME                                  DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
analytics-dask-jupyter    1        1        1           0          0s
analytics-dask-scheduler  1        1        1           0          0s
analytics-dask-worker     3        3        3           0          0s

==> v1/Pod(related)
NAME                                                   READY  STATUS             RESTARTS  AGE
analytics-dask-jupyter-5df785b4f6-6nvfj    0/1    ContainerCreating  0         0s
analytics-dask-scheduler-54979bfb76-ntmzs  0/1    ContainerCreating  0         0s
analytics-dask-worker-76cd548cdd-5dzfb     0/1    ContainerCreating  0         0s
analytics-dask-worker-76cd548cdd-kblcq     0/1    ContainerCreating  0         0s
analytics-dask-worker-76cd548cdd-nkvv5     0/1    ContainerCreating  0         0s


NOTES:
Thank you for installing DASK, released at name: analytics.

To learn more about the release, try:

  $ helm status analytics  # information about running pods and this message
  $ helm get analytics     # get full Kubernetes specification

This release includes a Dask scheduler, 3 Dask workers, and 1 Jupyter servers.

The Jupyter notebook server and Dask scheduler expose external services to
which you can connect to manage notebooks, or connect directly to the Dask
cluster.   You can get these addresses by running the following:

  export DASK_SCHEDULER=$(kubectl get svc --namespace default analytics-dask-scheduler -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
  export DASK_SCHEDULER_UI_IP=$(kubectl get svc --namespace default analytics-dask-scheduler -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
  export JUPYTER_NOTEBOOK_IP=$(kubectl get svc --namespace default analytics-dask-jupyter -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
  echo http://$JUPYTER_NOTEBOOK_IP:80 -- Jupyter notebook
  echo http://$DASK_SCHEDULER_UI_IP:80  -- Dask dashboard
  echo http://$DASK_SCHEDULER:8786    -- Dask Client connection

  NOTE: The default password to login to the notebook server is `dask`.

  NOTE: It may take a few minutes for the LoadBalancer IP to be available, until that the commands below will not work.
  You can watch the status by running 'kubectl get svc --namespace default -w analytics-dask-jupyter'
```

 Verify with

 ```bash
 $ kubectl get (pods|services)
 ```

Then we can configure our shell using thie following:

```bash
$ export DASK_SCHEDULER=$(kubectl get svc --namespace default ${NAME}-dask-scheduler -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ export DASK_SCHEDULER_UI_IP=$(kubectl get svc --namespace default ${NAME}-dask-scheduler -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ export JUPYTER_NOTEBOOK_IP=$(kubectl get svc --namespace default ${NAME}-dask-jupyter -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ echo http://$JUPYTER_NOTEBOOK_IP:80 -- Jupyter notebook
$ echo http://$DASK_SCHEDULER_UI_IP:80  -- Dask dashboard
$ echo http://$DASK_SCHEDULER:8786    -- Dask Client connection
```

