---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Deployment15.html
archived_at: '2026-07-15T08:05:19.963952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Installing%20Applications.md)

## Dynamically Loading Frameworks

When you run your WebObjects applications, you can specify extra frameworks to be dynamically loaded using the WOLoadFrameworks command-line option. You use this option as follows:

```
./HelloWorld -WOLoadFrameworks "(aFramework, bFramework, ...)"
```


The ".framework" extension is optional. If you specify a relative path to the framework (as in the example above), directories in your DYLD_FRAMEWORK_PATH are checked and, if the framework isn't found there, the directories specified by the NSProjectSearchPath are checked. Frameworks specified using WOLoadFrameworks are loaded just after the application class has been initialized. Each framework is loaded by invoking the framework's principal class' __init__ method; you'll need to set the NSPrincipalClass in your framework's __CustomInfo.plist__ in order to take advantage of this feature.
[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](The%20WebScript%20Language.md)
