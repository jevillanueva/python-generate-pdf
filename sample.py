import os
import time
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE_PATH = "/app/files"


def time_gen():
    return round(time.time() * 1000)


# WEB
HTML("https://weasyprint.org/").write_pdf(
    os.path.join(BASE_PATH, f"{time_gen()}-weasyprint.pdf")
)

# STATIC STRING
font_config = FontConfiguration()
html = HTML(string="<h1>The title</h1>")
css = CSS(
    string="""
    @page {
        size: Letter; /* Change from the default size of A4 */
        margin: 3cm;
    }
    @font-face {
        font-family: Gentium;
        src: url(https://example.com/fonts/Gentium.otf);
    }
    h1 { font-family: Gentium }""",
    font_config=font_config,
)
html.write_pdf(
    os.path.join(BASE_PATH, f"{time_gen()}.pdf"),
    stylesheets=[css],
    font_config=font_config,
)

# STATIC FILE
html = HTML(filename=os.path.join(".", "templates", "static_sample.html"))
css = CSS(
    string="""
    @page {
        size: Letter; 
        margin: 1cm;
    }
    @font-face {
        font-family: serif;
    }"""
)
html.write_pdf(
    os.path.join(BASE_PATH, f"{time_gen()}-static.pdf"),
    stylesheets=[css],
    font_config=font_config,
)

# USING JINJA2
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template(os.path.join(".", "templates", "sample.html"))
template_vars = {
    "title": "National Report",
    "datatable": [
        ["Name", "Amount", "Value"],
        ["John Doe", 70000, "$7,000"],
        ["Jane Doe", 80000, "$8,000"],
    ],
}
html_out = template.render(template_vars)
css = CSS(filename=os.path.join(".", "templates", "css", "jinja_style.css"))
html.write_pdf
HTML(string=html_out).write_pdf(
    os.path.join(BASE_PATH, f"{time_gen()}-jinja.pdf"),
    stylesheets=[css],
)
