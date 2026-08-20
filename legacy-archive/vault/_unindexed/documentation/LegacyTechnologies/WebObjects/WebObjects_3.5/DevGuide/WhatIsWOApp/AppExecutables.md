---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WhatIsWOApp/AppExecutables.html
archived_at: '2026-07-15T07:52:40.795804Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WhatIsWOApp.md) [!Previous Section](Adaptors.md)

## The WebObjects Application Executable

An application executable is an executable file, provided by you or by WebObjects, that receives incoming requests from the adaptor and responds to them, usually by returning a dynamically generated HTML page.
If your application is written entirely in WebScript, it can use the default application executable, _NeXT_ROOT___/NextLibrary/Executables/WODefaultApp__, provided as part of the WebObjects package. If your application contains compiled code, you build your own executable and use it in place of __WODefaultApp__.
WebObjects applications are event driven, but instead of responding to mouse and keyboard events, they respond to HTTP requests. A WebObjects application receives a request, responds to it, and then waits for the next request. The application continues to respond to requests until it terminates. During each cycle of this _request-response loop_, the application extracts the user input from the request, invokes an action if one is associated with the user's action, and generates a response-usually an HTML page (see [Figure 8](#apple-gy3tomy)).

!Figure 8. The Request-Response Loop

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
