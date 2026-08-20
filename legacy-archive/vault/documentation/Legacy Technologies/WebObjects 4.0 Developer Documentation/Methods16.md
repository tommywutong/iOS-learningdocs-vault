---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods16.html
archived_at: '2026-07-18T01:20:17.147316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods15.md)

### Component Awake

The component __awake__ method is invoked immediately after the __init__ method and each time the component object is restored from the page cache. Just as in __init__, you can implement an __awake__ method that initializes component variables. For example, a component might have a __shoppingCart__ variable that is a snapshot of the session's __shoppingCart__ variable. Each time the component is restored from the cache, its __shoppingCart__ variable should be updated with the session's __shoppingCart__:

```
// WebScript Car.wos
- awake {
    shoppingCart = [[self session] shoppingCart];
}
```


In general, you use __init__ or the component's constructor to initialize component instance variables instead of __awake__ because __init__ is invoked only at component initialization time, whereas __awake__ is potentially invoked much more than that. If, however, you want to minimize the amount of state stored between cycles of the component action
request-response loop, you might choose to initialize component instance variables in __awake__ and then deallocate them in __sleep__ (by setting them to __nil__ in WebScript or __null__ in Java). For more information, see the chapter ["Managing State"](Managing%20State.md#apple-heytena).

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods17.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
