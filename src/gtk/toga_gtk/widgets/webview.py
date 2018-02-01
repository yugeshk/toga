import gi

from gi.repository import Gtk

# The following import will fail if WebKit or it's API wrappers aren't
# installed; handle failure gracefully
# (see https://github.com/pybee/toga/issues/26)
# Accept any API version greater than 3.0
WebKit2 = None
for version in ['4.0', '3.0']:
    try:
        gi.require_version('WebKit2', version)
        from gi.repository import WebKit2

        break
    except (ImportError, ValueError):
        pass

from .base import Widget


class WebView(Widget):
    """ GTK WebView implementation.

    TODO: WebView is not displaying anything when setting a url.
    """

    def create(self):
        if WebKit2 is None:
            raise RuntimeError(
                "Import 'from gi.repository import WebKit' failed;" +
                " may need to install gir1.2-webkit2-4.0 or gir1.2-webkit2-3.0.")

        self.native = Gtk.ScrolledWindow()
        self.native.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.native.interface = self.interface

        self.webview = WebKit2.WebView()

        self.native.add(self.webview)
        self.native.set_min_content_width(200)
        self.native.set_min_content_height(200)
        # self.native.connect('show', lambda event: self.rehint())

    def set_url(self, value):
        if value:
            self.webview.load_uri(value)

    def set_user_agent(self, value):
        raise NotImplementedError()
        # self.native.user_agent = value if value else "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"

    def set_content(self, root_url, content):
        self.webview.load_html(content, root_url)

    def set_user_agent(self, value):
        self.native.customUserAgent = value if value else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"

    def get_dom(self):
        raise NotImplementedError()

    def evaluate(self, javascript):
        return self.webview.run_javascript(javascript, None, None, None)
