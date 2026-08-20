---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.30.html
archived_at: '2026-07-15T08:09:36.395748Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Problems%20With%20Scripted%20Applications.md) [!](Problems%20With%20Scripted%20Applications.md) [!](Problem-2.md)

---

#  Problem

The web browser does not launch or launches the incorrect URL

#  Checklist

1. 

   Check the debugging statements printed in the command-shell window.

   When you launch a WebObjects application from the command line, the application computes its own URL, launches the web browser, and enters the URL in the browser. It prints messages about the values it computes to standard output.

   Check the standard output (the command-shell window) for these messages (among others):

   The applicationPath:
   /System/Developer/Examples/WebObjects/WebScript/HelloWorld
   The applicationBaseURL: /WebObjects/HelloWorld
   Opening application's URL in Browser:
   _url_

   __Corrective action:__

   If you see these messages but your web browser doesn't launch, you might not have a browser installed on your system, or WebObjects cannot find the browser. This is always true on Solaris and HP-UX. If the URL looks correct (as described below), open your browser and type that URL into it.

   If you see a message that says "No Adaptor URL in WebServerConfig.plist," either the
   WebServerConfig.plist
   file is missing, or the
   WOAdaptorURL
   key is missing from it. The file should look something like this:

   {

      DocumentRoot = "/Apple/Library/WebServer/Documents";

      WOAdaptorURL = "http://localhost/cgi-bin/WebObjects";

   }

   If
   WOAdaptorURL
   is missing, the web browser does not launch when you launch a WebObjects application. You can enter
   WOAdaptorURL
   or you can type the URL in the browser and connect to the running application that way.

   This base URL value of
   WOAdaptorURL
   is of the form:

   http://localhost/
   _cgi-bin_

   /
   _WebObjects_

   _cgi-bin_
   is the name of your HTTP server's cgi-bin directory. You specify this name when you configure your HTTP server. The _cgi-bin_
   directory name is often
   cgi-bin
   , but it may have a different name. For example, the Microsoft Internet Information Server uses the name
   Scripts
   .

   _WebObjects_
   is the name of the WebObjects CGI adaptor as you see it in your HTTP server's cgi-bin directory. Usually, the name is WebObjects. If you're using Windows NT, the adaptor name might be
   WebObjects.exe
   (however, some older Netscape servers don't use the
   .exe
   extension.)

   If the base URL's cgi-bin and WebObjects adaptor names look correct, consider the
   localhost
   value. On most sites,
   localhost
   accesses the server on the local host. However, some sites require a domain name as well (
   http://localhost.apple.com
   ). If your HTTP server isn't running on your local machine, use the host name of the machine running the server in place of "localhost" in the URL above, and make sure a WebObjects adaptor is installed on that machine.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Problems%20With%20Scripted%20Applications.md) [!](Problems%20With%20Scripted%20Applications.md) [!](Problem-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
