---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods19.html
archived_at: '2026-07-15T08:05:54.608708Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods18.md)

### Limitations on Direct Requests

Users can access any page in an application without invoking an action. All they need to do is type in the appropriate URL. For example, you can access the second page of HelloWorld without invoking the __sayHello__ action by opening this URL:

```
http://serverhost/cgi-bin/WebObjects/Examples/HelloWorld.woa/wo/Hello
```


When a WebObjects application receives such a request, it bypasses the user-input (__takeValuesFromRequest:inContext:__) and action-invocation (__invokeActionForRequest:inContext:__) phases because there is no user input to store and no action to invoke. As a result, the object representing the requested page-Hello in this case-generates the response.
By implementing security mechanisms in __invokeActionForRequest:inContext:__, you can prevent users from accessing pages without authorization, but only if those pages are not directly requested in URLs. To prevent users from directly accessing pages in URLs, override __appendToResponse:inContext:__ instead.

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods20.md)
