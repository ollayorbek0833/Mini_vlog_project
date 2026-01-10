from vlog_project.handlers.not_found import not_found
from vlog_project.handlers.post import post_list, create_post, delete_post, get_post


def handle_request(raw_request:bytes) -> bytes:
    try:
        text = raw_request.decode("utf-8", errors="ignore")
        line = text.split("\r\n",1)[0]
        _,_,body = text.partition("\r\n\r\n")
        method, path, _ = line.split(" ")
    except Exception as error:
        print("error:" + str(error))
        return not_found()

    if method == "GET" and path =='/':
        return post_list()

    if method == "POST" and path == '/':
        return create_post(body)

    if method == "POST" and path == '/delete':
        vlog_id = int(body.split("=")[1])
        return delete_post(vlog_id)

    if method == "GET" and path.startswith("/vlog"):
        vlog_id = int(path.split("=",1)[1])
        return get_post(vlog_id)


    return not_found()