---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods10.html
archived_at: '2026-07-18T01:20:16.581002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods9.md)

## Component Initialization

A component object's __init__ method is invoked when the component object is created. Just how often a particular component object is created depends on whether the application object is caching pages. For more information, see ["WebObjects Viewed Through Its Classes"](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy). If page caching is turned on (as it is by default), the application object generally creates the component object once and then restores that object from the cache every time it is involved in a user request. If page caching is turned off, the component object is freed at the end of the request-response loop.

__Note:__  The __pageWithName:__ methods shown in the section ["Action Methods"](Action%20Methods.md#apple-g44daoa) always create a new component object, even if page caching is turned on.

A component object's __init__ method usually initializes component variables. For example, the following method initializes a component variable named __departments__:

```
// WebScript Department.wos
id departments;
- init {
        id departmentsPath;

        [super init];
        departmentsPath = [[[self application] resourceManager]
            pathForResourceNamed:@"Departments.array"
            inFramework:nil
            languages:[[self session] languages]];
        departments = [NSArray
arrayWithContentsOfFile:departmentsPath];
        return self;
}
```

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods11.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
