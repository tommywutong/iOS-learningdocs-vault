---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements4.html
archived_at: '2026-07-18T01:20:09.862074Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](DynamicElements3.md)

## Declarations File Syntax

As you've seen, the __.wod__ file specifies nearly all of the information necessary to create a dynamic element. Because you usually create dynamic elements and their bindings using WebObjects Builder, you normally don't have to worry about the syntax of the __.wod__ file. However, here it is for the curious:

```
elementName : elementType{attribute =value; attribute =value; ...};
```


As described in the previous section, _value_ can be a constant, variable, or method. It can also be a string of keys joined by a dot, similar to the Java syntax for sending messages but without the parentheses. For example:

```
application.upSince.description
```

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](Client-Side%20Java%20Components.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
