---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects9.html
archived_at: '2026-07-18T01:20:43.703893Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](The%20Parts%20of%20a%20WebObjects%20Application.md)

## Classes

The "Classes" suitcase contains the various compiled or scripted custom classes for the objects that make up your application. As well, Classes contains an Application class and a Session class.
The Application object is responsible for receiving requests from the adaptor and forwarding them on to a _request handler_-a dispatcher that passes requests to the appropriate session and component and receives responses back. When a response comes back from the request handler, the Application object passes the response back to the adaptor. The Application object also manages adaptors, sessions, application resources, and components.
_Sessions_ are periods during which a particular user is accessing your application. Because users on different clients may be accessing your application at the same time, a single application may host more than one session at a time. Session objects encapsulate the state of a single session. These objects persist between the cycles of the request-response loop, and store (and restore) the pages of a session, the values of session variables, and any other state that components need to persist throughout a session. As well, each session has its own copy of the components that its user has requested.
If your application makes use of the Enterprise Objects Framework, your application's enterprise object classes appear in the Classes suitcase. The Enterprise Objects Framework keeps the state of these objects in sync with your external data store (typically, a relational database), freeing you to concentrate on writing your business logic.
Many of the remaining classes that fall into Project Builder's Classes suitcase correspond to your Web Components; these contain the code that defines each component's behavior.
With WebObjects, you can write your code in one of three programming languages: Java (_myClass___.java__), Objective-C (_myClass___.m__), and WebScript (_myClass___.wos__). Because Java and Objective-C require compilation, they aren't as well suited to rapid prototyping as an interpreted language. For this reason WebObjects provides a scripting language named WebScript; it is described in the chapter ["The WebScript Language"](WebScript9.md#apple-geytanbs).

You can mix and match languages. It's common to use WebScript to write your presentation logic and use Java or Objective-C to write your business logic. Many simple applications are written entirely in WebScript. Some programmers prototype using WebScript and then create a compiled version of the same application to improve performance.
__Note:__  Framework class names are the same regardless of which language you use, but method names sometimes differ between Java and WebScript. (Objective-C uses the same method names as WebScript.) This book generally uses the WebScript names for methods. Usually, you can discern the Java name from the WebScript name, and vice versa. The following table tells you how to do so. Where the mapping is not obvious, this book notes both the Java and WebScript/Objective-C names.

|  |  WebScript/Objective-C Name |  Java Name |
|  Methods with no arguments |  _method_ |  _method_ |
|  Single-argument methods |  _method___:__ |  _method_ |
|  Multiple-argument methods |  _methodWithArg1:arg2:_ |  _methodWithArg1_ |

```
```

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects10.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
