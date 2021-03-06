from . import db, app
from .models import Video, Tag

def add_video(path, tags):

    app.app_context().push()
    video = Video(path=path)
    db.session.add(video)
    db.session.commit()
    for tag in tags:
        new_tag = Tag(videoID=video.id, classification=tag)
        db.session.add(new_tag)
    db.session.commit()
    print("Added Video to database")
