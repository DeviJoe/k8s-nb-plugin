from netbox.plugins import PluginConfig

class K8sConfig(PluginConfig):
    name = 'k8s'
    verbose_name = 'Netbox K8s plugin'
    description = 'Netbox plugin for Kubernetes objects (namespaces as example) and their teams'
    version = '0.1'
    author = 'MWS Team'
    base_url = 'k8s'
    min_version = '3.4.0'