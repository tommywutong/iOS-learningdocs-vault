---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/SessionInit.html
archived_at: '2026-07-15T07:51:16.493185Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](ApplicationInit.md)

## Session Initialization

A session object is created each time the application receives a request from a new user. An application may have multiple sessions running concurrently. The session ends when a session time-out value is reached.
In the session object's __init__ method, you set the session's time-out value and initialize variables that should have unique values for each session. For example, in the CyberWind application, each session keeps track of which number it is. These values are changed in the session object's __init__ method:

```
    //From CyberWind Session.wos
    - init {
        [super init];
        [self setTimeOut:120]; // session idle time is 2 minutes.
        [[self application] setSessionCount:[[self application]
            sessionCount + 1];
        sessionNumber = [[self application] sessionCount];
        return self;
    }

    //From CyberWindJava Session.java
    public Session() {
        super();
        Application application = (Application)application();
        this.setTimeOut(120);
        application.setSessionCount(application.sessionCount() + 1);
        sessionNumber = application.sessionCount();
    }
```


The session object's __awake__ method is invoked each time the user associated with the session makes a new request. After the application object has performed its own __awake__ method, it restores the appropriate session object and sends it the __awake__ message too.
The CyberWind application keeps track of the number of requests per session. It increments the number in the session's __awake__ method.

```
    - awake {
        requestCount++;
    }
```

[!Table of Contents](CommonMethods.md) [!Next Section](ComponentInit.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
