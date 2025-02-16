# communication/agent_protocol.py

import json

class AgentCommunicationProtocol:
    """
    Defines the standardized messaging structure for AI agents.
    """

    @staticmethod
    def create_message(sender: str, receiver: str, message_type: str, content: dict):
        """
        Constructs a message packet for agent communication.
        """
        return json.dumps({
            "sender": sender,
            "receiver": receiver,
            "type": message_type,
            "content": content
        })

    @staticmethod
    def parse_message(raw_message: str):
        """
        Parses incoming agent messages.
        """
        try:
            return json.loads(raw_message)
        except json.JSONDecodeError:
            return None
