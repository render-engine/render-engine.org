from pathlib import Path
from typing import Callable, Any

from render_engine import BasePageParser, Blog, Page, Site
from render_engine_markdown import MarkdownPageParser
from re_plugin_pack import LatestEntries

MD_EXTRAS: list[str] = [
    "link-shortrefs",
]

app = Site()
app.output_path = "output"

app.static_paths = list(map(Path, ("styles", "img", "scripts")))

app.site_vars.update(
    {
        "SITE_TITLE": "Render Engine",
        "SITE_URL": "https://render-engine.org",
        "bottom_nav": {
            "Home": "/index.html",
            "News": "/news",
        },
    }
)


@app.page
class Index(Page):
    template = "index.html"
    content_path = "content/index.md"
    Parser: type[BasePageParser] = MarkdownPageParser
    parser_extras: dict[str, list[str]] = {"markdown_extras": MD_EXTRAS}
    plugins: list[tuple[Callable, dict[str, Any]] | Callable] = [
        (
            LatestEntries,
            {
                "news": -1,
            },
        )
    ]


@app.collection
class News(Blog):
    content_path: str = "content/news"  # path to content files
    routes: list[str] = ["news"]  # route to collection page
    Parser: type[BasePageParser] = MarkdownPageParser
    template: str = "news.html"
    parser_extras: dict[str, list[str]] = {"markdown_extras": MD_EXTRAS}


if __name__ == "__main__":
    app.render()
