---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-43.html
archived_at: '2026-07-15T08:05:00.274207Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Performance%20Testing.md) [!](Recording%20a%20Session.md) [!](Improving%20Performance.md)

---

# Playing Back a Session

Once you have recorded a session with your application, you can use the __Playback__
command-line tool to simulate users accessing the application. This Java tool is part of the PlaybackManager project, which must be compiled for the tool to exist.

To play back a recorded session:

1. Add the following directory to your CLASSPATH environment variable:
`
NEXT_ROOT/Library/WebObjects/Applications/PlaybackManager.woa/WebServerResources/Java`2. In a separate shell, start the application as you normally would (do _not_
   use the__-WORecordingPath__
   flag here). When you start the application you can use adaptors or direct connect.

3. Start the __Playback__
   java tool by entering a command similar to the following:
`java com.apple.client.playback.Playback -r /tmp/tape1.rec`

The Playback class must be found in the Java classpath. When the PlayBack Manager project has been compiled, the __Playback__
tool bytecode is in the subdirectory __Playback Manager.woa/WebServerResources/Java.__

Alternatively, you can explictly give the class path on the command line, as in this example:

`` java -classpath ".:$NEXT_ROOT/Library/WebObjects/Applications/PlaybackManager.woa/WebServerResources/Java:`javaconfig DefaultClasspath`" com.apple.client.playback.Playback -r /tmp/tape1.rec ``

The __Playback__
tool plays the recorded session repeatedly until you explicitly stop it (for example, by pressing Control-C in a command shell window). You can run several instances of the tool at the same time to put more load on the server. To manage multiple instances it's better to use the Playback Manager application.

If you want, you can specify other options of the __Playback__
tool. The following list describes these options:

#### __-h__ _hostname_

Sets the host to send the requests to (the default is __localhost__
).

####  __-p__ _adaptorPath_

Sends requests using the specified adaptor path instead of the recorded URL. For example, suppose you recorded a session using a Netscape server whose cgi-bin directory is named __cgi-bin__
and you want to play it back using the Microsoft Internet Information Server, whose cgi-bin directory is named __Scripts__
and whose adaptor is named __WebObjects.dll__
. Your adaptor path is __/Scripts/WebObjects.dll.__

####  __-port__ _portNumber_

Sets the port the requests are sent to (the default is 80).

####  __-c__ _limit_

Limits the number of times to repeat the session playback (there is no limit by default).

#### __-s__ _sleepTime_

Sets the interval between requests in seconds (the default is zero).

####  __-diff__ _percents_

Sets the percentage difference between received and recorded response sizes (the default is 5%).

####  __-d__

Turns debugging on.

####  __-r__ _recordingDir_

Sets the recording directory.

#### __-help__

Prints a summary of options

Here is an example of a command beginning a playback session using direct connect:

`java -classpath com.apple.client.playback.Playback -d -h mymachine -r /tmp/tape1.rec -port 3456 -diff 20`

Additional information on the Playback Manager can be found in _NEXT_ROOT_
__/Library/WebObjects/Applications/PlaybackManager.woa/Resources/ReadMe.html__
.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Performance%20Testing.md) [!](Recording%20a%20Session.md) [!](Improving%20Performance.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
