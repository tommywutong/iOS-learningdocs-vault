---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-42.html
archived_at: '2026-07-15T08:04:59.760681Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Performance%20Testing.md) [!](Performance%20Testing.md) [!](Playing%20Back%20a%20Session.md)

---

# Recording a Session

When a WebObjects application is launched in recording mode, it saves each request and response made to a recording file (which has an extension of __.rec__
). You specify the path designating this file with the __-WORecordingPath__
flag, which also serves as a switch to turn on recording. The application automatically appends the __.rec__
extension to the given filename and creates a directory, if one doesn't exist, with the given path.

To run an application in recording mode:

1. Start the application on a command line similar to the following:
`myApplication -WOAutoOpenInBrowser NO -WORecordingPath /tmp/TestMyApp/tape1`

This command creates the file __/tmp/TestMyApp/tape1.rec__
.

2. Using a web browser, run a session of your WebObjects application.

You might want to record what you believe to be a typical session, or you might want to record a session that puts a maximum load on your application. For example, you may want to record a session that performs as many database fetches as possible. As you run the application, the WebObjects recording adaptor writes each request and response to the recording file.

Keep in mind that all request and responses are saved to disk, so it's recommended that only one user (that is, one session) access the application while recording is underway. You can later play back a recorded session multiple times to simulate more users.

3. Stop the application to stop recording

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Performance%20Testing.md) [!](Performance%20Testing.md) [!](Playing%20Back%20a%20Session.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
