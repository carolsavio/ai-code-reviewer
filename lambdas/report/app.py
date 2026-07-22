def lambda_handler(event, context):

    review = event["review"]


    report = {
        "title": "AI Code Review Report",

        "score": review.get(
            "score",
            0
        ),

        "summary": review.get(
            "summary",
            ""
        ),

        "issues_count": len(
            review.get(
                "issues",
                []
            )
        ),

        "issues": review.get(
            "issues",
            []
        ),

        "suggestions": review.get(
            "suggestions",
            []
        )
    }


    return report