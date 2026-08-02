---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/ApplicationInit.html
archived_at: '2026-07-15T07:51:14.512301Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](StructureOfInitAwake.md)

## Application Initialization

The application __init__ method is invoked only once, when the application is launched. You perform two main tasks in the application's __init__ method:

- Initialize application variables
- Configure applicationwide settings

For example, the Visitors application has this __init__ method in __Application.wos__:

```
    // WebScript Visitors Application.wos
    - init {
        [super init];
        lastVisitor = @"";
        [self setTimeOut:7200];
        return self;
    }

    // Java Visitors Application.java
    public Application () {
    super();
    ...
    lastVisitor = "";
    setTimeOut(7200);
    ...
    }
```


This method begins by calling the application's __init__ method. Then, it initializes the application variable __lastVisitor__ to be the empty string. (The application has just started, so there has been no last visitor.) Finally, it sets the application to terminate after it has been running 2 hours.
This example sets the application time-out value. You might want to do other configurations in the application object's __init__ method as well. For example, you can control how pages and components are cached and how state is stored. For more information, read the chapter ["Managing State"](../State/StateTOC.md).

The application's __awake__ method is invoked at the start of every cycle of the request-response loop. Therefore, in the __awake__ method, you perform anything that should happen before each and every user request is processed. For example, the DodgeDemo example application keeps track of the number of requests the application has received. It increments and logs that number at the top of the request-response loop:

```
    // WebScript DodgeDemo Application.wos
    - awake {
        ++requestCount;
        [self logWithFormat:@"Now serving request %@", requestCount];
    }

    // Java DodgeDemo Application.java
    public void awake() {
        ++requestCount;
        this.logString("Now serving request " + requestCount);
    }
```

[!Table of Contents](CommonMethods.md) [!Next Section](SessionInit.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
