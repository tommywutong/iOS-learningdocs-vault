---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript4.html
archived_at: '2026-07-15T08:06:35.314770Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript3.md)

### Variables and Scope

Each kind of variable has a different scope and a different lifetime. Local variables are only visible inside the block of text in which they are declared. In the example above, __localVariable1__ is declared at the top of a method. It is accessible within the entire body of that method, including the __while__ loop. It is created upon entry into the method and released upon exit. __localVariable2__, on the other hand, is declared in the __while__ loop construct. You can only access it within the curly braces for the __while__ loop, not within the rest of the method.
The scope of an instance variable is object-wide. That means that any method in the object can access any instance variable. You can't directly access an instance variable outside of the object that owns it; you must use an accessor method instead. See ["Accessor Methods"](WebScript8.md#apple-gyztmny).

The lifetime of an instance variable is the same as the lifetime of the object. When the object is created, all of its instance variables are created as well and their values persist throughout the life of the object. Instance variables are not freed until the object is freed.
As you learned in the chapter ["Common Methods"](Common%20Methods.md#apple-heydqmi):

- A WOApplication is created when you started a WebObjects application
- A WOSession is created each time a different user accesses that application during the component action request-response loop
- A WOComponent is created the first time a user accesses that page in the application
- A WODirectAction is created at the beginning of each direct action request-response loop cycle.

Thus, the variables you declare at the top of the application script (__Application.wos__) exist as long as the application is running. The variables you declare at the top of the session script (__Session.wos__) exist for the length of one session. As new users access your application, new sessions are created, so new copies of the session's instance variables are created too. These copies of instance variables are private to each session; one session does not know about the instance variables of another session. As sessions expire, their instance variables are freed. The variables you declare at the top of a component script are created and released as that component is created and released. Finally, the variables you declare at the top of a direct action script (__DirectAction.wos__) are created at the beginning of the direct action request-response loop cycle and released at the end of the cycle.
__Note:__  Just how often a particular component object is created depends on whether the application object is caching pages. For more information, see ["WebObjects Viewed Through Its Classes"](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy).

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript5.md)
