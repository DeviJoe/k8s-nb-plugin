from netbox.plugins import PluginMenuButton, PluginMenuItem


menu_items = (
    PluginMenuItem(
        link='plugins:k8s:namespace_list',
        link_text='Namespaces',
    ),
    PluginMenuItem(
        link='plugins:k8s:team_list',
        link_text='Teams',
    ),
)