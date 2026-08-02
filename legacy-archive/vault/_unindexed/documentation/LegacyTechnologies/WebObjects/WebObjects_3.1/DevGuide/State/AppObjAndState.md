---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/AppObjAndState.html
archived_at: '2026-07-15T07:47:37.869574Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](ObjectsAndState.md)

# The Application Object and Application State

No matter how many client sessions a WebObjects application is serving, it has one and only one application object. Each page (actually each component, as you learned in previous chapters) knows how to access the application object, so this is the logical place to store data that needs to be shared by all components in all sessions of an application.

Application state is typically stored in the application object's instance variables. For example, if you look at __Application.wos__ in the CyberWind example that comes with the WebObjects release, you'll see that the application object keeps track of the number of sessions that have been created, the total number of requests for all sessions, how long the application has been running, and other statistics:

```
id sessionCount;
id requestCount;
id upSince;
id activeSessions;

- init {
    [super init];
    upSince = [NSCalendarDate date];
    [upSince setCalendarFormat:@"%d %b %Y %H:%M:%S"];
    return self;
}

- createSession {
    activeSessions++;
    return [super createSession];
}
```

Components can access this information in a couple of ways. Using "dot notation" you can bind an attribute of a component's dynamic element to the state stored in the application object:

!

__Figure 1.__  Binding a WOString to a Session Variable

A component can also access application variables through its scripted or compiled code:

```
- isLuckyWinner {
    if ([[self application] sessionCount] == 1000)
        return YES;
    return NO;
}
```

Application state is accessible to any component within the application and, of course, persists for as long as the application is running. If your site runs multiple instances of the same application, application state must be accessible to all instances. In this case, application state might be best stored in a file or database, where application instances could easily access it. This approach is also useful as a safeguard against losing application state (such as the number of visitors to the site) if an application instance crashes.

[!Table of Contents](ManagingState.book.md)
[!Next Section](SessionObjAndState.md)
