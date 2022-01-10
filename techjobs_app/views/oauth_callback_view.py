from django.http import HttpRequest
from django.http.response import HttpResponse
from django.template import loader
from kink import inject

from techjobs_app.services.github_oauth_service import GithubOauthService


@inject
def oauth_callback_view(request: HttpRequest, github_oauth: GithubOauthService):
    code = request.GET.get("code")
    state = request.GET.get("state")
    if not state or not code:
        error_template = loader.get_template("oauth_error.html")
        return HttpResponse(error_template.render({}, request), status=401)
    token = github_oauth.get_access_token(code)["access_token"]
    github_oauth.persist_code(state=state, code=code, token=token)

    template = loader.get_template("oauth_callback.html")
    return HttpResponse(template.render({}, request))
