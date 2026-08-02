---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState14.html
archived_at: '2026-07-15T08:05:41.071460Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](Controlling%20Session%20State.md)

## Setting Session Time-Out

By assigning a time-out value to a session, you can ensure that the session will be deallocated after a specific period of inactivity. WOSession's __setTimeOut__: method lets you set this period and __timeOut__ returns it.
Here's how the session time-out works: After a cycle of the request-response loop, WebObjects associates a timer with the session object that was involved in the request and then puts the session object into the session store. The timer is set to the value returned by the session object's __timeOut__ method. If the timer goes off before the session is asked to handle another request, the session and its resources are deallocated. A user submitting a request to a session that has timed out receives an error message.
By default, a session object's time-out value is set to 3600 seconds. You should set the session time-out for your application to the shortest period that seems reasonable. You can specify the session timeout either with the WOSessionTimeout user default (user defaults such as this can be specified on the command-line when you start your application), or in your session initialization code. For example, to set the time-out to ten minutes, you could send this __setTimeOut__: message in your session's initialization method:

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


The argument to __setTimeOut__: is interpreted as a number of seconds.
At times, a user's choice signals the end of a session (such as when the Yes button is clicked in response to the query, "Do you really want to leave the Intergalactic Web Mall?"). If you are sure a session has ended, you can send a __terminate__ message to the session object, marking it (and the resources it holds) for release.
A session marked for release won't actually be released until the end of the current request-response loop. Other objects may need to know whether a particular request-response loop is their last, so they can close files or do other clean up. They can learn their fate by sending the session object an __isTerminating__ message.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState15.md)
