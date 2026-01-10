def redirect(path):
    return (
        "HTTP/1.1 303 See Other\r\n"
        f"Location: {path}\r\n"
        "\r\n"
    )
