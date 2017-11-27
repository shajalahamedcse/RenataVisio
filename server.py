from flask import Flask, render_template, Response, jsonify, request
from camera import VideoCamera

app = Flask(__name__)

video_camera = None
global_frame = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture_status', methods=['POST'])
def capture_status():
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera()

    json = request.get_json()
    print(json)

    status = json['status']
    #train=json['train']
    #print(train)

    if status =="true":
        video_camera.capture("image/train.jpg")
        return jsonify(result="captured")

#Testing
@app.route('/train_status', methods=['POST'])
def train_status():
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera()

    json = request.get_json()
    print(json)

    status = json['train']
    #train=json['train']
    print(status)

    if status =="true":
        video_camera.capture("for_match.jpg")
        return jsonify(result="matching") 

def video_stream():
    global video_camera 
    global global_frame

    if video_camera == None:
        video_camera = VideoCamera()
        
    while True:
        frame = video_camera.get_frame()

        if frame != None:
            global_frame = frame
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')


#@app.route('/image_viewer')
#def get_gallery():
#    return "<img src='image/train.jpg'/>"
                         

@app.route('/video_viewer')
def video_viewer():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)