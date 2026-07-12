import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            user_label = request.user.get_username()
        else:
            user_label = "anonymous"

        logger.info(
            f"{request.method} {request.path} -> {response.status_code} (user: {user_label})"
        )

        return response