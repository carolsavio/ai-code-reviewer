import boto3
import json


bedrock = boto3.client("bedrock-runtime")


MODEL_ID = "MODEL_ID = "amazon.nova-lite-v1:0""


def lambda_handler(event, context):

    language = event["language"]
    code = event["code"]

    prompt = f"""
You are a senior software engineer performing a code review.

Analyze the following {language} code.

Evaluate:

- readability
- bugs
- security issues
- performance
- best practices

Return ONLY valid JSON.

Use exactly this format:

{{
    "score": 0,
    "summary": "",
    "issues": [],
    "suggestions": []
}}

Code:

{code}
"""

    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    )


    review_text = (
        response["output"]
        ["message"]
        ["content"][0]
        ["text"]
    )


    # Remove markdown caso o modelo retorne ```json
    review_text = review_text.replace("```json", "")
    review_text = review_text.replace("```", "")

    review = json.loads(review_text.strip())


    return {
        "language": language,
        "code": code,
        "review": review
    }