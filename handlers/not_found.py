from vlog_project.utils.response import response


def not_found():
    with open("template/not_found.html", "r", encoding="utf-8") as f:
        body = f.read()
    return response(body)
