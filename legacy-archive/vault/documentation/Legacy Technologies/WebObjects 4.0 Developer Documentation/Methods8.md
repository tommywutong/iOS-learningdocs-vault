---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods8.html
archived_at: '2026-07-18T01:20:18.092418Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods7.md)

## Application Initialization

The application __init__ method is invoked only once, when the application is launched. You perform two main tasks in the application's __init__ method:

- Initialize application variables
- Configure applicationwide settings

For example:

```
// WebScript Application.wos
- init {
        self = [super init];
        lastVisitor = @"";
        [self setDefaultRequestHandler:
            [self requestHandlerForKey:
            [WOApplication directActionRequestHandlerKey]]];
        return self;
}
// Java Application.java
public Application () {
    super();
    ...
    lastVisitor = "";
    setDefaultRequestHandler(requestHandlerForKey
        (WOApplication.directActionRequestHandlerKey()));
    ...
}
```


This method begins by calling the superclass's __init__ method. Then, it initializes the application variable __lastVisitor__ to be the empty string. (The application has just started, so there has been no last visitor.) Finally, it sets the default request handler to be the WODirectActionRequestHandler. WODirectActionRequestHandler handles requests for direct actions like the one shown in ["Direct Actions"](Methods3.md#apple-gy3dimi). You set it to be the default request handler if you want to have initial requests go through the "defaultAction" of DirectAction.

You might want to do other configurations in the application object's __init__ method as well. For example, you can control how pages and components are cached and how state is stored. For more information, read the chapter ["Managing State"](Managing%20State.md#apple-heytena).

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
