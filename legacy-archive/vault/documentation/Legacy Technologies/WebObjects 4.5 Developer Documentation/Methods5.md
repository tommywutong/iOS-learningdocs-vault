---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods5.html
archived_at: '2026-07-15T08:05:57.186787Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods4.md)

### Setting the Default Request Handler

If a request URL doesn't have a request handler key (as is the case with the initial URL used to begin a session with a WebObjects application), WOApplication uses whatever its default request handler is set to be. By default, the default request handler is WOComponentRequestHandler. If you want to write an application entirely using direct actions, set the default request handler in your WOApplication's __init__ method or constructor in this way:

```
// Java implementation
public WOApplication() {
    super();
    ...
    setDefaultRequestHandler(requestHandlerForKey(
        WOApplication.directActionRequestHandlerKey()));
    ...
}
//WebScript implementation
- init {
    self = [super init];
    ...
    [self setDefaultRequestHandler:[self requestHandlerForKey:
        [WOApplication directActionRequestHandlerKey]]];
    ...
    return self;
}
```

[!Table of Contents](Common%20Methods.md) [!Next Section](Initialization%20and%20Deallocation%20Methods.md)
