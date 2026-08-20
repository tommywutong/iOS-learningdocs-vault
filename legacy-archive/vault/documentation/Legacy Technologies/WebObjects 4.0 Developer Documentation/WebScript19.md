---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WebScript19.html
archived_at: '2026-07-18T01:20:36.086913Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript18.md)

### Raising an Exception

Once an exception is detected, it must be propagated to code that will handle it, called the exception handler. This entire process of handling an exception is referred to as "raising an exception." Exceptions are raised by instantiating an NSException object and sending it a raise message.
NSException objects provide:

- a name - a short string that is used to uniquely identify the exception.
- a reason - a longer string that contains a "human-readable" reason for the exception.
- userInfo - a dictionary used to supply application-specific data to the exception handler. For example, if the return value of a method causes an exception to be raised, you could pass the return value to the exception handler through userInfo.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript20.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
