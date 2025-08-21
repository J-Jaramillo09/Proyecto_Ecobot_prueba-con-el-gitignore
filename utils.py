import urllib.parse

def extraer_video_id(url):
    parsed_url = urllib.parse.urlparse(url)

    # Caso: youtu.be/VIDEO_ID
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    # Caso: youtube.com/watch?v=VIDEO_ID
    elif parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        query = urllib.parse.parse_qs(parsed_url.query)
        return query.get("v", [""])[0]

    return None
