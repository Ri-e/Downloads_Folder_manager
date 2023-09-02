


while True:

    import os
    import re
    src = "/home/adi/Downloads"
    dst_img = "/home/adi/Downloads/img"
    dst_docs = "/home/adi/Downloads/docs"
    dst_mp3 =  "/home/adi/Downloads/music"
    dst_video = "/home/adi/Downloads/video"
    dst_app = "/home/adi/Downloads/apps"

    #img
    if os.path.isdir("/home/adi/Downloads/img"):

        pass
    else :
        os.mkdir("/home/adi/Downloads/img")
    #docs
    if os.path.isdir("/home/adi/Downloads/docs"):

        pass
    else :
        os.mkdir("/home/adi/Downloads/docs")

    #music
    if os.path.isdir("/home/adi/Downloads/music"):
        pass
    else :
        os.mkdir("/home/adi/Downloads/music")  

    #video

    if os.path.isdir("/home/adi/Downloads/video"):
        pass
    else :
        os.mkdir("/home/adi/Downloads/video")  

    # app
    if os.path.isdir("/home/adi/Downloads/apps"):
        pass
    else :
        os.mkdir("/home/adi/Downloads/apps")  



    #list
    imgs = [".png", ".jpg"]
    doc = [".pdf", ".css"]
    music = [".mp3"]
    video = [".mp4"]
    app = [".deb", ".gz", ".tar"]
    
    #main
    main = os.listdir(src)
    for i in main:
        ext = os.path.splitext(i)
        if ext[1] in imgs:
            src_path = os.path.join(src, i)
            dst_path = os.path.join(dst_img, i)
            os.rename(src_path, dst_path)
        elif ext[1] in doc:
            src_path = os.path.join(src, i)
            dst_path = os.path.join(dst_docs, i)
            os.rename(src_path, dst_path)
        elif ext[1] in music:
            src_path = os.path.join(src, i)
            dst_path = os.path.join(dst_mp3, i)
            os.rename(src_path, dst_path)
        elif ext[1] in video:
            src_path = os.path.join(src, i)
            dst_path = os.path.join(dst_video, i)
            os.rename(src_path, dst_path)  
        elif ext[1] in video:
            src_path = os.path.join(src, i)
            dst_path = os.path.join(dst_apps, i)
            os.rename(src_path, dst_path)  
























# import os
# import re
# src = "/home/adi/Downloads"
# dst_img = "/home/adi/Downloads/img"
# dst_docs = "/home/adi/Downloads/docs"
# dst_mp3 =  "/home/adi/Downloads/music"
# dst_video = "/home/adi/Downloads/video"

# #img
# if os.path.isdir("/home/adi/Downloads/img"):

#     print("img_pass")
# else :
#     os.mkdir("/home/adi/Downloads/img")
# #docs
# if os.path.isdir("/home/adi/Downloads/docs"):

#     print("docs_pass")
# else :
#     os.mkdir("/home/adi/Downloads/docs")

# #music
# if os.path.isdir("/home/adi/Downloads/music"):

#     print("music_pass")
# else :
#     os.mkdir("/home/adi/Downloads/music")  

# #video

# if os.path.isdir("/home/adi/Downloads/video"):

#     print("video_pass")
# else :
#     os.mkdir("/home/adi/Downloads/video")  

# #list
# imgs = [".png", ".jpg"]
# doc = [".pdf", ".css"]
# music = [".mp3"]
# video = [".mp4"]
# #main
# main = os.listdir(src)
# for i in main:
#     ext = os.path.splitext(i)
#     if ext[1] in imgs:
#         src_path = os.path.join(src, i)
#         dst_path = os.path.join(dst_img, i)
#         os.rename(src_path, dst_path)
#     elif ext[1] in doc:
#         src_path = os.path.join(src, i)
#         dst_path = os.path.join(dst_docs, i)
#         os.rename(src_path, dst_path)
#     elif ext[1] in music:
#         src_path = os.path.join(src, i)
#         dst_path = os.path.join(dst_mp3, i)
#         os.rename(src_path, dst_path)   