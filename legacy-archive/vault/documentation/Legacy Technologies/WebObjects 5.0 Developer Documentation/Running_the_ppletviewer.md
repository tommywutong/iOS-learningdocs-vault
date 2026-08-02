---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/Running_the_ppletviewer.html
archived_at: '2026-07-15T08:12:31.083704Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Customizing_ebAssistant.md)[![Next](attachments/DirectToWeb/Images/next.gif)](WebAssistant_Overview.md)

## Running the WebAssistant With appletviewer

You can launch WebAssistant using the Java program `appletviewer`.
Follow these steps:

1. Launch your
   application with the command-line option D2WWebAssistantEnabled
   set to YES.
2. In the console output look for a line similar to the following:

   ```
   DirectToWeb WebAssistant launch line: appletviewer http://localhost:51508/ cgi-bin/WebObjects/D2WTutorial.woa/wa/D2WActions/openWebAssistant
   ```
3. Open a shell such as provided by the Terminal application
   on Mac OS X.
4. Copy the string from "appletviewer" to "openWebAssistant"
   to the shell and press Return (or Enter).

   If the port number
   is -1, look in the console output for the actual port number of
   the application and substitute that.

When you complete this procedure, WebAssistant launches and
connects to your application. If you stop and restart the Direct
to Web application, the WebAssistant will re-connect to it provided
it is running on the same port.

A standalone WebAssistant has exactly the same functionality
as one launched inside your browser. However, if the browser you
are using is not Java-enabled, your pages are not automatically
refreshed after you click Update. You must either click your browser's "reload"
or "refresh" button or (when you are picking a new type of page,
such as a MasterDetails page instead of a ListPage), you will have
to re-navigate to the same page.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Customizing_ebAssistant.md)[![Next](attachments/DirectToWeb/Images/next.gif)](WebAssistant_Overview.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
