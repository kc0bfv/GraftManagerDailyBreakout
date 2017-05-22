from __future__ import print_function

import BaseHTTPServer
import urlparse

from Architectures import Architecture
from ManageAllGrafts import ManageAllGrafts

# This is a string that will be ingested by format, so the code can plug
# in appropriate responses and selectors based on what's available
interface_html = """
<html>
<head>
    <title>Graft Manager</title>
    <style>
    .section {{
        border: thin solid black;
        margin: 5px;
        }}
    </style>
</head>
<body>
    <h1>Graft Manager</h1>
    {result}
    <div class="section">
        <h2>Add Graft</h2>
        <form method="get" action="/add">
            <label>Address: <input type="textbox" name="address"></label>
            <br><label>Port: <input type="textbox" name="port"></label>
            <br>Architecture: {architecture_selector}
            <br><input type="submit" value="Add Graft">
        </form>
    </div>
    <div class="section">
        <h2>Command Graft</h2>
        <form method="get" action="/command">
            <label>Command: <input type="textbox" name="command"></label>
            <label>Graft: {graft_selector}</label>
            <br><input type="submit" value="Command Graft">
        </form>
    </div>
    <div class="section">
        <h2>Graft Responses <a href="/">REFRESH</a></h2>
        {graft_responses}
    </div>
</body>
</html>
"""

class GraftHTTPServer(BaseHTTPServer.HTTPServer):
    """
    An HTTPServer that contains a reference to a graft manager
    """
    def __init__(self, *args, **kwargs):
        # Initialize the base class
        # Unfortunately, python2.7 BaseHTTPServer.HTTPServer doesn't seem
        # to inherit from object, so we can't use super
        BaseHTTPServer.HTTPServer.__init__(self, *args, **kwargs)
        self.manager = ManageAllGrafts()

class GraftHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    An HTTPRequestHandler handling graft commands

    Control gets to your code through the do_GET function, below.
    """

    # -------------- Handlers for GET commands -------------- 
    def add_graft(self, param_dict):
        """
        Add a graft based on the contents of param_dict, return something
        to display to the screen

        :param dict param_dict:
            A dictionary with keys corresponding to the names of the HTML
            input fields the user filled in.  Values are 1-entry lists
            (assuming the user didn't craft some bogus input, which is totally
            possible).  The first and only entry in the list is the value
            of whatever the user typed into the corresponding field.  So...
            
            Key "address" - Value ["whatever user typed in to address"]
            Key "port" - Value ["whatever user typed in to port"]
            Key "architecture" - Value ["whatever user selected in arch box"]

        :returns str: Just return some status text - this will be inserted
            as "{result}" in the big HTML template above, so feel free to
            respond with HTML if you feel fancy
        """
        return "PROGRAMMER HASN&apos;T FILLED THIS IN YET"

    def command_graft(self, param_dict):
        """
        Command a graft based on the contents of param_dict, return something
        to display to the screen

        :param dict param_dict:
            A dictionary with keys corresponding to the names of the HTML
            input fields the user filled in.  Values are 1-entry lists
            (assuming the user didn't craft some bogus input, which is totally
            possible).  The first and only entry in the list is the value
            of whatever the user typed into the corresponding field.  So...
            
            Key "command" - Value ["whatever user typed in to command"]
            Key "graft_index" - Value ["whatever user selected in graft box"]

        :returns str: Just return some status text - this will be inserted
            as "{result}" in the big HTML template above, so feel free to
            respond with HTML if you feel fancy
        """
        return "PROGRAMMER HASN&apos;T FILLED THIS IN YET"

    # The code below maps actions from the request URL to functions above using
    # this mapping
    request_handlers = {
            "add": add_graft,
            "command": command_graft,
            }

    # -------------- Handling the rest -------------- 
    def parse_the_request(self):
        """
        Return a tuple of (request, parameter dictionary), from the url

        This is called early on by build_request to parse out the URL
        """
        parsed = urlparse.urlparse(self.path)
        # Get rid of the leading /
        request = parsed.path[1:]
        params = urlparse.parse_qs(parsed.query)
        return request, params

    def build_selector(self, html_name, select_dict):
        """
        Returns an HTML selector based on a dictionary
        :param str html_name: The name tag to use in the html form
        :param dict select_dict:
            Keys are what the browser will put in the GET request
            Values are what the browser will display to the user
        :returns str: The HTML
        """
        option_list = [
                '<option value="{}">{}</option>'.format(key, name) 
                for key, name in select_dict.iteritems()
                ]
        return '<select name="{}">{}</select>'.format(
                html_name, "".join(option_list))

    def build_arch_selector(self):
        """
        Return an HTML selector selecting from available architectures
        """
        # A dictionary of name: name for the names of all subclasses of
        # Architecture.  This is possible because Architecture derives from
        # object
        arch_dict = {sc.__name__: sc.__name__
                for sc in Architecture.__subclasses__()}
        return self.build_selector("architecture", arch_dict)

    def build_graft_selector(self):
        """
        Return an HTML selector selecting from all available grafts
        """
        graft_list = self.server.manager.list_grafts()
        graft_dict = {index: "{} {}".format(addr, port) 
                for index, addr, port in graft_list}
        return self.build_selector("graft_index", graft_dict)

    def build_graft_responses(self):
        """
        Return HTML representing the responses from all grafts
        """
        html = ""

        grafts = self.server.manager.list_grafts()
        for index, addr, port in grafts:
            html += "<div><h3>Graft {} {}</h3>".format(addr, port)
            c_and_rs = self.server.manager.list_graft_responses(index)
            for c_and_r in c_and_rs:
                html += "<div>Command: {} Response: {}</div>".format(
                        c_and_r.command, c_and_r.response)
            html += "</div>"

        return html

    def build_interface(self):
        """
        Return html to send, or None if it was an invalid request

        This gets called by do_GET to build the webpage that gets sent
        """
        request, params = self.parse_the_request()
        print(params)

        # If the user's GET represented a command, handle that command
        if request == "":
            result = ""
        elif request in self.request_handlers:
            result = self.request_handlers[request](self, params)
        else:
            return None
        
        # Build the components to the html
        architecture_selector = self.build_arch_selector()
        graft_selector = self.build_graft_selector()
        graft_responses = self.build_graft_responses()

        # Plug the components in
        html = interface_html.format(result = result,
                architecture_selector = architecture_selector,
                graft_selector = graft_selector,
                graft_responses = graft_responses
                )

        return html

    def do_GET(self):
        """
        Called by the HTTPRequestHandler class, in response to a GET.

        This will be the entry point for the code you're adding to the class.
        The class already has code that you've inherited that determines when
        a web request is a GET request, then calls do_GET with a bunch of
        state already setup on the instance.
        """
        response_html = self.build_interface()

        if response_html is None:
            self.send_response(404)
            return

        self.send_response(200)
        self.send_header("Location", "/")
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(response_html)

def run(port=8000):
    """
    Use this to kick off the server and serve responses.

    The script "runserver.py" is already setup to call this function.
    """
    http = GraftHTTPServer(('', port), GraftHTTPRequestHandler)
    http.serve_forever()
