---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-41.html
archived_at: '2026-07-15T08:04:59.266083Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Administrative%20Tasks.md) [!](Accessing%20the%20Application%20Statistics%20Page.md) [!](Recording%20a%20Session.md)

---

# Performance Testing

WebObjects comes with a set of tools that allows you to record a session and then play it back. Using these tools, you can test your application setup to determine whether you have the appropriate number of instances running, the appropriate amount of memory allocated, and so on. The performance tools include:

- The default application adaptor that, when the __-WORecordingPath__
  flag is set to YES, enables the recording of sessions
- A command-line Java tool that plays back recorded sessions
- A Playback Manager application that can play back sets of sessions (___NEXT_ROOT___
  __/Library/WebObjects/Applications/PlaybackManager.woa__
  )

These tools are not designed to handle automated functional testing, only performance testing. They simply save requests and play them back after substituting the appropriate session and context identifiers. This means that the playback tools expect the application to return the same page and content as when it was recorded.

This section focuses on recording and playing back sessions from the command line. For information on the Playback Manager application, consult the application's online help.

#### [Recording a Session](Recording%20a%20Session.md#apple-obtwmslefu4tanjt)

#### [Playing Back a Session](Playing%20Back%20a%20Session.md#apple-obtwmslefu4tanrs)

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Administrative%20Tasks.md) [!](Accessing%20the%20Application%20Statistics%20Page.md) [!](Recording%20a%20Session.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
