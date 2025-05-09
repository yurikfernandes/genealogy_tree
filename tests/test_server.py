from genealogy import server

class TestServer:
    def test_server_initialization(self):
        """
        Tests if the server's run function can be correctly imported.
        """
        # We verify if the run function exists and can be called
        assert callable(server.run), "The server's run function is not available"

    def test_server_response(self):
        import threading
        import requests
        import time
        
        # Start the server in a thread to avoid blocking the test
        server_thread = threading.Thread(target=server.run, kwargs={'port': 8081})
        server_thread.daemon = True  # So the test can finish even if the server is still running
        server_thread.start()
        
        # Give time for the server to start
        time.sleep(1)
        
        # Make a request to the server
        response = requests.get('http://localhost:8081')
        assert response.status_code == 200
        assert 'Hello, world!' in response.text