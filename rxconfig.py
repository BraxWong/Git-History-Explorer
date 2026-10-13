import reflex as rx

config = rx.Config(
    app_name="Git_History_Explorer",
    app_module_import="git_history_explorer",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)