---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects16.html
archived_at: '2026-07-18T01:20:39.349093Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](WhatIsWebObjects15.md)

## Frameworks

Project Builder's Frameworks suitcase contains any custom frameworks you may have developed (perhaps containing business-specific classes that you've packaged into a framework for re-use) along with the standard frameworks supplied with WebObjects.
Nearly all WebObjects applications employ the frameworks listed in the following table. Applications that don't make use of the Enterprise Objects Framework don't need EOAccess and EOControl.

|  Framework |  Description |
|  WebObjects |  Used by all WebObjects applications, this framework contains the application, session, component, and adaptor classes, as well as classes that perform request handling and state management. |
|  WOExtensions |  This framework serves as a repository of reusable components that you can use to enhance your application's user interface. This framework also contains components that display application statistics and notify you when exceptions are raised within your application. Source code for this framework is also supplied as an example. |
|  DirectToWeb |  A framework for dynamically generating user interfaces (pages or parts of pages) based upon the structure of your database as specified in your model. |
|  EOAccess |  Allows your application to interact with database servers at a high level of abstraction. Provides a fine level of control over database operations while allowing to you work with database records as objects. |
|  EOControl |  These classes allow you to write enterprise objects that have no dependencies on the user interface and the storage mechanism being used. |
|  Foundation |  An operating system-independence layer that provides memory management, fundamental object behavior, access to lower-level services, and classes that implement important features such as collections, strings, and threads. |

```
```


In Java, WebObjects classes are in the package __com.apple.yellow.webobjects__. Similar packages corresponding to the other frameworks listed above can be found under __com.apple.yellow__.

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](Developing%20a%20WebObjects%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
