---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WebScript23.html
archived_at: '2026-07-18T01:20:36.915107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript%20for%20Objective-C%20Developers.md)

## Accessing WebScript Methods From Objective-C Code

As stated previously, you can mix WebScript and Objective-C code. Often, programmers use WebScript for component logic, and then supply the bulk of the application (the "business logic") in compiled code.
To access Objective-C code from a WebScript file, you simply use the Objective-C class like any other class:

```
id myObject = [[MyCustomObjCClass alloc] init];
```


To access a WebScript object from Objective-C code, you simply get the object that implements the method and send it a message. If you're accessing a method in the application script, you can use this WOApplication method to access the object:

```
[[WOApplication application] applicationScriptMethod];
```


To avoid compiler warnings when accessing WebScript objects from Objective-C, create a header file for the scripted component as though it were compiled. This step isn't strictly required, of course-your code will still build, you'll just get warnings.
[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
