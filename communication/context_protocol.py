# communication/context_protocol.py

import requests

class ModelContextProtocol:
    """
    Defines how AI agents interact with external context providers.
    """

    @staticmethod
    def fetch_context_data(api_url: str, params=None):
        """
        Retrieves context data from external APIs.
        """
        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException:
            return None
