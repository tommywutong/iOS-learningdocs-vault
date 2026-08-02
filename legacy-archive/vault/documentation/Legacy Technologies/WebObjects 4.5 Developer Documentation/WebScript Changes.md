---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.42.html
archived_at: '2026-07-15T08:09:42.908463Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Troubleshooting%20WebObjects%204%20Request%20Handling.md) [!](Uninstalling%20WebObjects.md)

---

#   WebScript Changes

In WebObjects 3.5, WebScript would always evaluate both sides of an "&&" or "||" expression. In WebObjects 4, these expressions are short-circuited, so that only the left side is evaluated unless evaluation of the right side is necessary in order to determine the result. For example:

    (YES || <this will NOT evaluate>)

    (NO  || <this will evaluate>)

    (YES && <this will evaluate>)

    (NO  && <this will NOT evaluate>)

To aid in the debugging process, WebObjects 4 has a WebScript 3.5 compatibility mode. This mode is controlled by a method in WOApplication named
requiresWOF35Scripting
. By default, this method returns NO; override it to return YES to get backward compatibility.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Troubleshooting%20WebObjects%204%20Request%20Handling.md) [!](Uninstalling%20WebObjects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
