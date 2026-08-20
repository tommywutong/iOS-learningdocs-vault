---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.02.html
archived_at: '2026-07-15T07:57:58.177652Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Compatibility%20With%20Earlier%20Releases-2.md)

# File Location Changes

Enterprise Objects Framework 3.0 is the first release of Enterprise Objects Framework that runs on Rhapsody and on Yellow Box for Windows NT instead of OpenStep 4.2. Because of this change, the locations of Enterprise Objects Framework files have changed.
On Rhapsody, Enterprise Objects Framework files are installed in the __System__ folder. On Windows NT, you still choose a folder in which to install the software, and the __NEXT_ROOT__ environment variable points to that folder. The default has changed to __C:\Apple__.
The following table lists new directory names relative to the __System__ folder or __NEXT_ROOT__ and what each directory contains.

|  __Location__ |  Contains |
|  Developer/Applications |  The EOModeler application. |
|  Developer/Examples/EnterpriseObjects |  Enterprise Objects Framework examples. |
|  Developer/Examples/WebObjects |  WebObjects examples, including examples of using Enterprise Objects Framework with WebObjects. |
|  Documentation/Developer |  Developer documentation for Rhapsody, Yellow Box, Enterprise Objects Framework, and WebObjects. |
|  Library/Frameworks |  Public frameworks such as EOAccess.framework. |
|  Library/Executables |  Framework DLLs (Windows NT systems only). |
|  Library/Java |  Java packages for Yellow Box, WebObjects, and Enterprise Objects Framework. |
|  Local/Library |  Prebuilt example frameworks and executables, sample EOModeler extension bundle, and 3.5 to 4.0 conversion scripts. |

```
```

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Changes%20to%20Java%20API.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
