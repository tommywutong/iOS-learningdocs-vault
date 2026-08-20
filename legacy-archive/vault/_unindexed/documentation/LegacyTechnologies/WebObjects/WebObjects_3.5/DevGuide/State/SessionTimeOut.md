---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/SessionTimeOut.html
archived_at: '2026-07-15T07:52:19.823886Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](ControllingSessionState.md)

## Setting Session Time-Out

By assigning a time-out value to a session, you can ensure that the session will be deallocated after a specific period of inactivity. WOSession's setTimeOut: method lets you set this period and timeOut returns it.
Here's how the session time-out works: After a cycle of the request-response loop, WebObjects associates a timer with the session object that was involved in the request and then puts the session object into the session store. The timer is set to the value returned by the session object's timeOut method. If the timer goes off before the session is asked to handle another request, the session and its resources are deallocated. A user submitting a request to a session that has timed out receives an error message:!Figure 35. A Session Time-Out Error Message
By default, a session object's time-out value is so large that sessions effectively never expire. You should set the session time-out for your application to the shortest period that seems reasonable. For example, to set the time-out to ten minutes, you could send this setTimeOut: message in your session's initialization method:

```
    // WebScript Session.wos
    - init {
        [super init];
        [self setTimeOut:600];
        return self;
    }
    // Java Session.java
    public Session() {
        super();
        this.setTimeOut(600);
    }
```


The argument to setTimeOut: is interpreted as a number of seconds.
At times, a user's choice signals the end of a session (such as when the Yes button is clicked in response to the query, "Do you really want to leave the Intergalactic Web Mall?"). If you are sure a session has ended, you can send a terminate message to the session object, marking it (and the resources it holds) for release.
A session marked for release won't actually be released until the end of the current request-response loop. Other objects may need to know whether a particular request-response loop is their last, so they can close files or do other clean up. They can learn their fate by sending the session object an isTerminating message.

[!Table of Contents](StateTOC.md) [!Next Section](SessionAwake.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
