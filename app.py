import json
import requests
from pydantic import BaseModel, Field

endpoint_url = 'https://develop-ainft-baby-shark-brooklyn-ainize-team.endpoint.ainize.ai/chat'

class ChatInput(BaseModel):
    input_text: str = Field(
        ...,
        title="Input Text",
        description="Input text to chat.",
        max_length=9999,
    )


class ChatOutput(BaseModel):
    output: str


def get_output(input_text: str) -> str:
    try:
        params = {
            'text': input_text
        }
        response = requests.get(endpoint_url, params=params)
        output = response.json()['message']
    except Exception as e:
        output = f'Endpoint API Internal error occurs : {e}'

    return output


def babyshark_brooklyn_ainft_chat(input: ChatInput) -> ChatOutput:
    input_text = input.input_text  # input_text
    output_text = get_output(input_text)

    return ChatOutput(output=output_text)