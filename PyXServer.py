import asyncio
from aiohttp import web
import os

class PyXServer:
    def __init__(self):
        # Create the web application
        self.app = web.Application()

        # Adding Routes
        self.app.add_routes([
            web.get('/', self.handle_home),
            web.get('/about', self.handle_about),
            web.get('/static/{filename}', self.handle_static)
        ])

    # Handle request for Home page
    async def handle_home(self, request):
        return web.Response(text="Welcome to PyXServer! This is the Home page.")

    # Handle request for About page
    async def handle_about(self, request):
        return web.Response(text="PyXServer is a high-performance Python web server using aiohttp!")

    # Handle static file requests
    async def handle_static(self, request):
        filename = request.match_info.get('filename')
        file_path = os.path.join('static', filename)

        if os.path.exists(file_path):
            return web.FileResponse(file_path)
        else:
            return web.Response(status=404, text="File Not Found")

    # Method to start the server
    def run(self, host='127.0.0.1', port=8080):
        print(f"PyXServer running on {host}:{port}...")
        web.run_app(self.app, host=host, port=port)

# Static file directory creation (if it doesn't exist)
def create_static_directory():
    if not os.path.exists('static'):
        os.makedirs('static')
        print("Created static directory for serving files.")

# Main function to run the server
if __name__ == '__main__':
    create_static_directory()

    # Create server instance and start
    server = PyXServer()
    server.run()
