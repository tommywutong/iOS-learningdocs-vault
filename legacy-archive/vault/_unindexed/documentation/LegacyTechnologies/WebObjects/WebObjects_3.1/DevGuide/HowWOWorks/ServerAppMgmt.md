---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/ServerAppMgmt.html
archived_at: '2026-07-15T07:46:57.211788Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](WideAngleView.md)

# __Server and Application Management__

The HTTP sends a request to the application's adaptor, a WOAdaptor object . This object packages the incoming HTTP request in a WORequest object and forwards it to the application object (WOApplication) in a __handleRequest__ message. The application initiates and manages the process of request handling and returns the completed response (WOResponse) to the adaptor, which gives it to the HTTP server in a form the server can understand.

!

**- WOAdaptor**
: An abstract class that defines the interface for objects mediating the exchange of data between an HTTP server and a WebObjects application.

**- WOApplication**
: Objects of this class (or subclass) receive requests from the adaptor and initiate and coordinate the request-handling process, at the end of which they return a response to the adaptor. They also create dynamic elements "on the fly" and manage adaptors, sessions, application resources, and pages.


```

```

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](SessionMgt.md)
