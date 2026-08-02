---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.5c.html
archived_at: '2026-07-15T08:11:09.195003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](The%20Login%20Page.md)

---

#  Launching a Direct to Web Application

To launch your application from Project Builder:

1. 

   Click !
   in the toolbar in Project Builder's main window to open the Launch panel.
2. 

   Click !
   in the Launch panel to launch your application.

Before you launch the application you might want to set some command line options. For example, when running a Direct to Web Application for deployment, you should turn on caching and disable the Web Assistant (to prevent anyone from connecting to the application using the Web Assistant). To do this, set the
-WOCachingEnabled
and
-D2WWebAssistantEnabled
options, respectively:

1. 

   Click !
   to bring up the Launch Options panel.
   
   !
2. 

   Click the Arguments tab.
3. 

   Click Add to create a new command line and type the entries as shown in the above example. If there is no checkmark under the Use column, double-click the line under Use to set it.

For other command-line options for WebObjects applications, such as
-WOPort
, see _Serving WebObjects_
.

You can test the Direct to Web application using a web browser on a machine remote from the machine on which the application is running (that is, the server). When you launch the application, look in the console output, which is displayed in the Launch panel, for the line containing application's URL.

Jul 28 09:48:52 D2WTest[2777] Your application's URL is:
http://localhost:1234/cgi-bin/WebObjects/D2WTest

Enter the URL in your browser, after substituting the host name of the server machine for "localhost". In fact, you can exclude every thing in the URL after the application port number. For example, if the server host name is "foobar" you would enter the following URL in the browser to load the WebObjects application:

http://foobar:1234/

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](The%20Login%20Page.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
