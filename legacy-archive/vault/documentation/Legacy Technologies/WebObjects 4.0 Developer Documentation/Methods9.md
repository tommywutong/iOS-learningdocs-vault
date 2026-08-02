---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods9.html
archived_at: '2026-07-18T01:20:18.173252Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods8.md)

## Session Initialization

A session object is created each time the application receives a component action request from a new user. An application may have multiple sessions running concurrently. The session ends when a session time-out value is reached.
__Note:__  By default, applications create session objects during the first cycle of the request-response loop. This is because by default, the first request is handled by the component action request handler, which creates a session. If you change the default request handler to the direct action request handler, you do not have a session object. See ["WebObjects Viewed Through Its Classes"](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy) for clarification.

In the session object's __init__ method, you set the session's time-out value and initialize variables that should have unique values for each session. For example, if you wanted to have each session keep track of what number it is, you could do so in the session object's __init__ method:

```
//WebScript Session.wos
- init {
        id woApp = [WOApplication application];
        self = [super init];
        [self setTimeOut:120]; // session idle time is 2 minutes.
        [woApp setSessionCount:[woApp sessionCount + 1];
        sessionNumber = [woApp sessionCount];
        return self;
}
//Java Session.java
public Session() {
        super();
        Application woApp =
(Application)WOApplication.application();
        this.setTimeOut(120);
        woApp.setSessionCount(woApp.sessionCount() + 1);
        sessionNumber = woApp.sessionCount();
}
```

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods10.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
