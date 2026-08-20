---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/DynEl/DeclarationsFile.html
archived_at: '2026-07-15T07:51:31.087386Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](Bindings.md)

## Declarations File Syntax

As you've seen, the __.wod__ file specifies nearly all of the information necessary to create a dynamic element. Because you usually create dynamic elements and their bindings using WebObjects Builder, you normally don't have to worry about the syntax of the __.wod__ file. However, here it is for the curious:

```
elementName : elementType { attribute = value; attribute = value };
```


Notice that the last attribute/value pair before a closing brace (}) does not end with a semicolon (;).
As described in the previous section, _value_ can be a constant, variable, or method. It can also be a string of messages joined by a dot, similar to the Java syntax for sending messages but without the parentheses. For example:

```
application.upSince.description
```

[!Table of Contents](DynElTOC.md) [!Next Section](ClientSide.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
