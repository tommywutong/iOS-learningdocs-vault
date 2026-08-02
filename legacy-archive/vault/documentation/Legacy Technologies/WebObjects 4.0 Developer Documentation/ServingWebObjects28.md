---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects28.html
archived_at: '2026-07-18T01:23:47.060375Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects27.md)

## Performance Testing

WebObjects comes with a set of tools that allows you to record a session and then play it back. Using these tools, you can test your application setup to determine whether you have the appropriate number of instances running, the appropriate amount of memory allocated, and so on. The performance tools include:

- The default application adaptor that, when the __-WORecordingPath__ flag is set to YES, enables the recording of sessions
- A command-line Java tool that plays back recorded sessions
- A Playback Manager application that can play back sets of sessions (_NEXT_ROOT___/Library/WebObjects/Applications/PlaybackManager.woa__)

The recording tools are not designed to handle automated functional testing, only performance testing. They simply save requests and play them back after substituting the appropriate session and context identifiers. This means that the playback tool expects the application to return the same page and content and when it was recorded.
This section focuses on recording and playing back sessions from the command line. For information on the Playback Manager application, consult the application's online help.

### Recording a Session

When a WebObjects application is launched in recording mode, it saves each request and response made to a recording file (which has an extension of __.rec__). You specify the path designating this file with the __-WORecordingPath__ flag, which also serves as a switch to turn on recording. The application automatically appends the __.rec__ extension to the given filename and creates a directory, if one doesn't exist, with the given path.
To run an application in recording mode:

- Start the application on a command line similar to the following:

```
myApplication -WOAutoOpenInBrowser NO -WORecordingPath
/tmp/TestMyApp/tape1
```


This command creates the file __/tmp/TestMyApp/tape1.rec__.

- Using a web browser, run a session of your WebObjects application.

You might want to record what you believe to be a typical session, or you might want to record a session that puts a maximum load on your application. For example, you may want to record a session that performs as many database fetches as possible. As you run the application, the WebObjects recording adaptor writes each request and response to the recording file.

Keep in mind that all request and responses are saved to disk, so it's recommended that only one user (that is, one session) access the application while recording is underway. You can later play back a recorded session multiple times to simulate more users.

- Stop the application to stop recording

### Playing Back a Session

Once you have recorded a session with your application, you can use the __Playback__ command-line tool to simulate users accessing the application. This Java tool is part of the PlaybackManager project, which must be compiled for the tool to exist.
To play back a recorded session:

- Start the application as you normally would; do _not_ use the __-WORecordingPath__ flag here). When you start the application you can use adaptors or direct connect.
- Start the __Playback__ java tool by entering a command similar to the following:

```
java com.apple.client.playback.Playback -r /tmp/tape1.rec
```


The Playback class must be found in the Java classpath. When the PlayBack Manager project has been compiled, the __Playback__ tool bytecode is in the subdirectory __Playback Manager.woa/WebServerResources/Java.__

Alternatively, you can explictly give the class path on the command line, as in this example:

```
java -classpath
".:/MyProjects/PlaybackManager/PlaybackManager.woa/WebServerResources/Ja
va:`javaconfig DefaultClasspath`" com.apple.client.playback.Playback -r
/tmp/tape1.rec
```


The __Playback__ tool plays the recorded session repeatedly until you explicitly stop it (for example, by pressing Control-C in a command shell window). You can run several instances of the tool at the same time to put more load on the server. To manage multiple instances it's better to use the Playback Manager application.
If you want, you can specify other options of the __Playback__ tool. The following list describes these options:

**____-h__ _hostname___**
: Sets the host to send the requests to (the default is localhost).

**____-p__ _adaptorPath___**
: Sends requests using the specified adaptor path instead of the recorded URL. For example, suppose you recorded a session using a Netscape server whose cgi-bin directory is named __cgi-bin__ and you want to play it back using the Microsoft Internet Information Server, whose cgi-bin directory is named __Scripts__ and whose adaptor is named __WebObjects.dll__. Your adaptor path is __/Scripts/WebObjects.dll.__

**____-port__ _portNumber___**
: Sets the port the requests are sent to (the default is 80).

**____-c__ _limit___**
: Limits the number of times to repeat the session playback (there is no limit by default).

**____-s__ _sleepTime___**
: Sets the interval between requests in seconds (the default is zero).

**____-diff__ _percents___**
: Sets the percentage difference between received and recorded response sizes (the default is 5%).

**____-d____**
: Turns debugging on.

**____-r__ _recordingDir___**
: Sets the recording directory.

**____-help____**
: Prints a summary of options

Here is an example of a command beginning a playback session using direct connect:

```
java -classpath com.apple.client.playback.Playback -d -h mymachine -r
/tmp/tape1.rec -port 3456 -diff 20
```

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects29.md)
