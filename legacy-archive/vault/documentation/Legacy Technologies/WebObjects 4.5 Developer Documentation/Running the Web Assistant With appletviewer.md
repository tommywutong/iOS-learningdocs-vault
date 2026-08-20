---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.65.html
archived_at: '2026-07-15T08:11:18.715609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Web%20Assistant%20Overview.md)

---

#   Running the Web Assistant With appletviewer

If you browser is incapable of running applets, or if you want to run the Web Assistant in a different machine from your browser, you can launch the Web Assistant using the Java program __appletviewer__
. To do this:

1. 

   Launch your application with the command-line option
   D2WWebAssistantEnabled
   set to
   YES
   .
2. 

   In the console output look for a line similar to the following:

   Jul 23 10:29:48 D2WTest[527] Server-side WebAssistant launch line:
   appletviewer http://localhost:8888/cgi-
   bin/WebObjects/D2WTest.woa/wa/D2WActions/openWebAssistant
3. 

   Open a shell such as provided by the Terminal application on Mac OS X Server systems or the Bourne Shell on Yellow Box for Windows systems.
4. 

   Copy the string from "appletviewer" to "openWebAssistant" to the shell and press Return (or Enter).

   If the port number is -1, look in the console output for the actual port number of the application and substitute that.

When you complete this procedure, the Web Assistant launches and is connected to your application. If you stop and restart the Direct to Web application, the Web Assistant will re-connect to it provided it is running on the same port.

A standalone Web Assistant has exactly the same functionality as one launched inside your browser. However, if the browser you are using is not Java-enabled, your pages are not automatically refreshed after you click Update. You must either click your browser's "reload" or "refresh" button or (when you are picking a new type of page, such as a MasterDetails page instead of a ListPage), you will have to re-navigate to the same page.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Web%20Assistant%20Overview.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
