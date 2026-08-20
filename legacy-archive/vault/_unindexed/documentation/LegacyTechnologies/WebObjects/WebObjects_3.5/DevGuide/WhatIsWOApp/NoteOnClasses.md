---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WhatIsWOApp/NoteOnClasses.html
archived_at: '2026-07-15T07:52:43.739453Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WhatIsWOApp.md) [!Previous Section](SessionCode.md)

## A Note on WebObjects Classes

True to its name, WebObjects is an object-oriented environment for writing web applications. Therefore, when you write a component, an application file, or a session file, you are really writing a class. This is true whether you use WebScript, Java, or Objective-C. You can learn about these classes and where they are used by reading the chapter ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md).

Components are subclasses of a class named WOComponent. For example, in [Figure 1](Components.md#apple-g43de) the component directory creates a WOComponent subclass named Main. Application files create subclasses of a class named WOApplication, and session files create subclasses of a class named WOSession.

WOComponent, WOApplication, and WOSession are defined, along with other classes, in the WebObjects Framework in _NeXT_ROOT___/NextLibrary/Frameworks/WebObjects.framework__. (_NeXT_ROOT_ is an environment variable defined at installation time. On Windows NT systems, it is __C:\NeXT__ by default. On Mach systems, the _NeXT_ROOT_ environment variable is undefined, but you can think of it as being the root directory __/__.)
In Java, WebObjects classes have different names. The names shown previously are the WebScript names. (Objective-C uses the same names as WebScript.) In Java, WOComponent is called Component, WOApplication is WebApplication, and WOSession is WebSession. The Java classes are contained in the package __next.wo__.
__Note:__  This book generally uses the WebScript names for classes and methods. Usually, you can easily discern the Java name from the WebScript name, and vice versa. The following table tells you how to do so.

| ____ | __ WebScript/Objective-C Name__ | __ Java Name__ |
|  Class names |  WO_Class_ |  _Class_ (or __next.wo.___Class_) |
|  Zero-argument methods |  _method_ |  _method_ |
|  Single-argument methods |  _method___:__ |  _method_ |
|  Multiple-argument methods |  _methodWithArg1___:___arg2___:__ |  _methodWithArg1_ |

```
```


Where the mapping is not obvious, this book notes both the Java and WebScript/Objective-C names.

[!Table of Contents](WhatIsWOApp.md) [!Next Section](AppDir.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
