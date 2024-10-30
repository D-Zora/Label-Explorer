# Label Explorer, GPL-3.0 license
# https://gitee.com/intelligence-vision/label-explorer


from rich.console import Console

console = Console()

__version__ = "v0.0.3"

console.print(
    f"[bold blue] 🚀 欢迎使用 Label Explorer {__version__} \n具体内容参见源码地址：https://gitee.com/intelligence-vision/label-explorer [/bold blue]"
)

__all__ = "__version__"
