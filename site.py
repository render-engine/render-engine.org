from pathlib import Path

from render_engine import BasePageParser, Blog, Page, Site
from render_engine_markdown import MarkdownPageParser

site = Site()
site.output_path = "output"

site.static_paths = list(map(Path, ("styles", "img", "scripts")))

site.site_vars.update(
    {
        "SITE_TITLE": "Render Engine",
        "SITE_URL": "https://render-engine.org",
    }
)


@site.page
class Index(Page):
    template = "index.html"
    content_path = "content/index.md"
    parser: type[BasePageParser] = MarkdownPageParser


@site.collection
class News(Blog):
    content_path: str = "content/news"  # path to content files
    routes: list[str] = ["news"]  # route to collection page
    pageParser: type[BasePageParser] = MarkdownPageParser
    template: str = "news.html"


if __name__ == "__main__":
    site.render()
