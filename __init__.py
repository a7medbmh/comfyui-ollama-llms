from .ollama_chat import OllamaService
from .concatenate import ConcatenateText
from .ollama_vision import LlavaVision
from typing import ClassVar


class Image:
    serialize_model: ClassVar[None] = None


NODE_CLASS_MAPPINGS = {
    "ollama": OllamaService,
    "ConcatenateText": ConcatenateText,
    "llava": LlavaVision,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ollama": "Ollama Chat",
    "ConcatenateText": "Concatenate Text Prompts LLMs",
    "llava": "Ollama Vision",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
