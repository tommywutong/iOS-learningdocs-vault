---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Deployment/TerminateApp.html
archived_at: '2026-07-15T07:51:26.584813Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Deployment.md) [!Previous Section](ErrorHandling.md)

# Automatically Terminating an Application

Unless an application is very carefully constructed, the longer it runs, the more memory it consumes. As more memory is consumed, the server machine's performance begins to degrade. For this reason, you may find that performance is greatly improved if you occasionally stop an application instance and start a new one.
You can stop an application manually using the Monitor application (described in the online document [_Serving WebObjects_](../../ServingWebObjects/ServingWebObjectsTOC.md)). Or you can include code in the application to have it automatically terminate itself under certain conditions. Either way, you might want to turn on application auto-recovery in the Monitor application; that way, when the application dies, it automatically restarts.

- __Idle time.__ If no users are accessing the application, you might want to shut it down until a user requests it. To do so, use WOApplication's __setTimeOut:__ method. This method shuts down the application after it has been idle for a given number of seconds.

```
    public Application() {
        super();
        this.setTimeOut(2*60*60); //shut down if idle 2 hours
        ...
    }
```

- __Running time.__ You can have an application terminate itself after a specific amount of time has elapsed, regardless of whether it is idle or not using the __terminateAfterTimeInterval:__ method. For example, the following application will terminate after 24 hours.

```
    public Application() {
        super();
        this.terminateAfterTimeInterval(24*60*60);
        ...
    }
```


After the specified time limit has elapsed, __terminateAfterTimeInterval:__ immediately stops all current processing. If any sessions are active, users may lose information.

- __Session count.__ An application can also terminate if the number of active sessions falls below a certain number. Use __setMinimumActiveSessionsCount:__ to set this number, and then send __refuseNewSessions:__ to prevent the application from creating more sessions. For example, if you want to shut down your application after 24 hours but you want any current users to be able to end their sessions first, you might write the following code:

```
    // WebScript Application.wos
    id startDate;
    - init {
        [super init];
        [self setMinimumActiveSessionCount:1];
        return self;
    }

    - sleep {
        if (!startDate) // get the start date from statisticsStore
        {
            [[[self statisticsStore] statistics]
                objectForKey:@"StartedAt"];
        }
        // Compare start date to current date. If the difference is
        // greater than 24 hours, refuse any new sessions.
        if (([[NSDate date] timeIntervalSinceReferenceDate] -
            [startDate timeIntervalSinceReferenceDate]) > 86400)
        {
            [self refuseNewSessions:YES];
        }
    }
```


When the application's active session count falls below the minimum of one session, it will terminate. Sending __refuseNewSessions:__ guarantees that the active session count will eventually fall below the minimum.

[!Table of Contents](Deployment.md) [!Next Section](Performance.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
