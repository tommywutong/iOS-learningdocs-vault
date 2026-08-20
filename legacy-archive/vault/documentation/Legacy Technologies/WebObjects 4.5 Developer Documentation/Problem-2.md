---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.32.html
archived_at: '2026-07-15T08:09:36.901669Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Problems%20With%20Scripted%20Applications.md) [!](Problem.md) [!](Problems%20With%20Compiled%20Applications.md)

---

#  Problem

A simple scripted application won't run properly.

#  Checklist

1. 

   Try using direct-connect to access your WebObjects application.
2. 

   Check that you can load a static page.

   __Corrective action:__

   If your browser displays a message saying that it was unable to connect or that the connection was refused, your HTTP server is probably not running. Check that your server is running. Otherwise, see [See Checking the Installation](Checking%20the%20Installation.md#apple-giztsmbt)
   for information on how to fix your installation of WebObjects.
3. 

   __Check that the WebObjects adaptor is functioning.__

   Check that the WebObjects adaptor is installed correctly and can run. Use your browser to open this URL (which specifies the WebObjects adaptor, but fails to specify an application name):

   http://localhost/cgi-bin/WebObjects

   (You may need to replace "localhost" with the name of the host running your HTTP server. You may also need to replace "cgi-bin" with the actual name of the directory that contains scripts and CGI programs on your server.) If the WebObjects adaptor is installed correctly, it displays a list of WebObjects applications running on the local machine.

   If the adaptor is installed incorrectly or can't run, the browser will instead display a message indicating that the requested object cannot be located. The message may look like this:

   404 Not Found
   The requested URL /cgi-bin/WebObjects was not found on this server.

   __Corrective action:__

   Make sure you've supplied the right names in the URL for the host ("localhost" in the example above) and for the cgi-bin directory (sometimes named "Scripts" or "cgiPrograms" rather than "cgi-bin"). Otherwise, see [Checking the Installation](Checking%20the%20Installation.md#apple-giztsmbt)

   for information on how to fix your installation of WebObjects.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Problems%20With%20Scripted%20Applications.md) [!](Problem.md) [!](Problems%20With%20Compiled%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
