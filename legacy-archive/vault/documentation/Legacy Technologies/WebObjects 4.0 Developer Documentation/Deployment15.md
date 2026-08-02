---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Deployment15.html
archived_at: '2026-07-18T01:20:04.304494Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Installing%20Applications.md)

## Dynamically Loading Frameworks

When you run your WebObjects applications, you can specify extra frameworks to be dynamically loaded using the WOLoadFrameworks command-line option. You use this option as follows:

```
./HelloWorld -WOLoadFrameworks "(aFramework, bFramework, ...)"
```


The ".framework" extension is optional. If you specify a relative path to the framework (as in the example above), directories in your DYLD_FRAMEWORK_PATH are checked and, if the framework isn't found there, the directories specified by the NSProjectSearchPath are checked. Frameworks specified using WOLoadFrameworks are loaded just after the application class has been initialized. Each framework is loaded by invoking the framework's principal class' __init__ method; you'll need to set the NSPrincipalClass in your framework's __CustomInfo.plist__ in order to take advantage of this feature.
[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](The%20WebScript%20Language.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
