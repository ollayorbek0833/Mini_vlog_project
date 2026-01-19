from urllib.parse import parse_qs

from db.connection import get_vlogs, add_vlog, delete_vlog, get_vlog_by_id
from handlers.not_found import not_found
from utils.redirect import redirect
from utils.response import response


def post_list():
    vlogs = get_vlogs()
    vlog_html = ""
    for vlog_id, title, desc, time in vlogs:
        vlog_html += f"""
        <div style="border:1px solid #ccc;padding:10px;margin:10px 0;border-radius:6px;">
        <a href="/vlog?id={vlog_id}" style="text-decoration:none;color:inherit;">
            <h2>{title}</h2>
            <p>{desc}</p>
            <small>{time}</small>
        </a>

        <form method="POST" action="/delete" style="margin-top:10px;">
            <input type="hidden" name="id" value="{vlog_id}">
            <button type="submit"
                style="background:#ff4d4f;color:white;border:none;
                       padding:6px 12px;border-radius:4px;cursor:pointer;">
                🗑 Delete
            </button>
        </form>
    </div>
    """

    body = f"""
    <html>
      <head>
        <title>Socket Vlogs</title>
      </head>
      <body>
        <h1>🎥 My Vlogs</h1>

        <form method="POST">
          <input name="title" placeholder="Vlog title" required><br><br>
          <textarea name="description" placeholder="Vlog description" required></textarea><br><br>
          <button type="submit">➕ Add Vlog</button>
        </form>

        <hr>
        {vlog_html}
      </body>
    </html>
    """
    return response(body)

def create_post(body):
    data = parse_qs(body)
    title = data.get('title', [""])[0]
    desc = data.get('description', [""])[0]

    if title and desc:
        add_vlog(title, desc)

    return post_list()

def get_post(id):
    vlog = get_vlog_by_id(id)
    if not vlog:
        return not_found()
    db_id, title,desc, time = vlog

    body = f"""
        <html>
          <head>
            <title>{title}</title>
          </head>
          <body>
            <a href="/">⬅ Back</a>
            <h1>{title}</h1>
            <p>{desc}</p>
            <small>{time}</small>
          </body>
        </html>
        """
    return response(body)


def delete_post(id):
    delete_vlog(id)
    return redirect('/')