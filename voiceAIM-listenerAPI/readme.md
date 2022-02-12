# Voice-AIM

>> This repo contains the code for both server side API and client side application.

## Listener-API

This is the server side API which is made with flask.

#### Requirements
- python3.5 +
- ansible
- terraform
- awscli v2 (configured)


```
# Launch the api

cd ListenerAPI
python3 app.py
```


## voice_cloud

This is the client side application that uses your voice commands to decide actions to be performed.

```
# compile the application

cd voice_cloud
flutter run
```

*(Attach your device via usb and enable usb debugging)*

---

Check chapter 7 of the [report](https://github.com/ayedaemon/voiceAIM-listenerAPI/blob/master/report_ppt/VoiceAIM%20project%20report.pdf) for sample screenshots.
