---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/SessionInit.html
archived_at: '2026-07-15T07:47:29.894831Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](ApplicationInit.md)

# Session Initialization

The session's __init__ method is invoked when the application creates the WOSession object for the current session, which happens when the application receives the first request of a new user. Initialize variables in the session __init__ method that should retain their values between transactions throughout the session. For example, the __Session.wos__ script in the Visitors example initializes the session variable __timeSinceSessionBegain__ before setting up a timer that will result in the variable's value being incremented:

```
id timeSinceSessionBegan;
id timer;
- init
{
    [super init];
    timeSinceSessionBegan = 0;
    timer = [NSTimer scheduledTimerWithTimeInterval:1.0 target:self
    selector:"timeOfSession" userInfo:nil repeats:YES];
    [self setTimeOut:120];
    return self;
}
```

__Note:__  An important side effect of using a timer object in a WebObject's application is that the method invoked when the timer fires is outside the request-response loop. In other words, invocation occurs after the transaction concludes, and thus the method has no access to the WORequest, WOResponse, and WOContext of the transaction.

When a session begins in a scripted application, WebObjects automatically creates an instance of a special subclass of WOSession and adds to it the code from the session script. When you send __init__ to __super__ in an session script, you invoke the __init__ method of the superclass of the instance: WOSession. You can also subclass WOSession and override __init__ to perform any necessary initialization. It is more common, however, to implement the __init__ method in an session script.

The WOSession object's __awake__ method is invoked just after the object is created (and receives __init__) and immediately after being restored for each subsequent transaction.

[!Table of Contents](RunLoop.book.md)
[!Next Section](ComponentInit.md)
