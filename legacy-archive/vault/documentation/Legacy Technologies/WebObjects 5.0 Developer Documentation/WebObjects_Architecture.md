---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/WebObjects_Architecture.html
archived_at: '2026-07-15T08:15:14.249917Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](A_Programme__WebObjects.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Developing__Application.md)

## WebObjects Architecture

When you run a WebObjects application, it communicates with
the Web browser through the chain of processes shown in [Figure 4-3](#apple-infeessfiveek).

__Figure
4-3 WebObjects HTML-based application
communication chain__

![[image: ../Art/CommunicationChain.gif]](../Art/CommunicationChain.gif)

Here is a brief description of these processes:

- __A
  Web browser.__ WebObjects supports all Web browsers that
  conform to HTML 3.2. Of course, if your application uses more advanced
  features like JavaScript or QuickTime, the users' browsers must
  support these features.
- __A Web server.__ WebObjects supports any
  HTTP server that uses the Common Gateway Interface (CGI), the Netscape
  Server API (NSAPI), the Internet Server API (ISAPI), or the Apache
  module API. Although necessary for deployment, you don't actually
  need a Web server while you develop your WebObjects applications.
- __A WebObjects adaptor.__ A WebObjects
  adaptor connects WebObjects applications to the Web by acting as
  an intermediary between Web applications and HTTP servers. Note
  that the WebObjects adaptor may not be a separate process but plug-in
  to the Web server.
- __A WebObjects application process.__ The
  application process receives incoming requests and responds to them,
  usually by returning a dynamically generated HTML page. You can
  run multiple instances of this process if one instance is insufficient
  to handle the application load. The application process is made
  up of your code and the WebObjects frameworks.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](A_Programme__WebObjects.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Developing__Application.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
