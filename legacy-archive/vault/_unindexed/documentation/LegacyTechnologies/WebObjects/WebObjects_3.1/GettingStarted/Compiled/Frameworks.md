---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/Frameworks.html
archived_at: '2026-07-15T07:48:16.446382Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](mainMethod.md)

## Frameworks

The following table lists the frameworks Project Builder includes in a WebObjectsApplication project. These are the frameworks that your program is linked with when you build. They must be included no matter what language you're using.

| __ Framework__ | __ Contains__ |
|  WebObjects |  Contains the WebObjects classes. |
|  Foundation |  Contains the NeXT root class (NextObject or NSObject), plus other basic object classes that most applications use. |
|  EOAccess |  Contains the Enterprise Objects Access Layer. You need this framework only if you are writing a database application or if you are writing any WebObjects application that runs on Windows NT. |
|  EOControl |  Contains the Enterprise Objects Control Layer, which is the bridge between the database access layer and the interface layer. You need this framework only if you are writing a database application. |

```
```

[!Table of Contents](compiled.book.md) [!Next Section](CustomClasses.md)
