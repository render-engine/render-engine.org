from pathlib import Path

from render_engine import BasePageParser, Blog, Page, Site
from render_engine_markdown import MarkdownPageParser

app = Site()
app.output_path = "output"

app.static_paths = list(map(Path, ("styles", "img", "scripts")))

app.site_vars.update(
    {
        "SITE_TITLE": "Render Engine",
        "SITE_URL": "https://render-engine.org",
    }
)


@app.page
class Index(Page):
    template = "index.html"
    content_path = "content/index.md"
    Parser: type[BasePageParser] = MarkdownPageParser


@app.collection
class News(Blog):
    content_path: str = "content/news"  # path to content files
    routes: list[str] = ["news"]  # route to collection page
    Parser: type[BasePageParser] = MarkdownPageParser
    template: str = "news.html"


if __name__ == "__main__":
    app.render()
