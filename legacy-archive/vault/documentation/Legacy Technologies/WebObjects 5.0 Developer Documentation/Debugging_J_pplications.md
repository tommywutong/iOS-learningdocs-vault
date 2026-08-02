---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Advanced/Debugging_J_pplications.html
archived_at: '2026-07-15T08:13:58.234091Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Advanced_Tasks.md)[![Next](attachments/JavaClient/Images/next.gif)](Customizing__Assistants.md)

## Debugging Java Client WebObjects Applications

It can be difficult to debug Java Client WebObjects applications
because these applications have a client side and a server side.
Each side runs in a totally different process and in a different
virtual machine (VM), so you can't debug the one side by running
a debugger for the other side.

### Debugging Server Code

To debug the server side of a Java Client application use
the standard debugging features of Project Builder. Start the debugger
by clicking the Debug button (the spray-can icon). You can use this
procedure to perform debugging tasks in all your server side classes.

See the documentation for Project Builder for details on its
debugging features.

### Debugging Client Code

Project Builder currently provides no support for debugging
the client side of a Java Client application. Instead, use the Java
debugger `jdb` (included
with the JDK) in a shell window.

Once your code has compiled, start up the client application
with `AppletViewer` or
with the `java` interpreter
(see ["Running a Java Client Application"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/iBuilding_an_Application.html) in the tutorial) with the -debug flag. These tools
then print a "password" that you can use later to attach `jdb` to
your client application. To attach `jdb`,
open another shell and enter the following command:

`jdb -password` _password_

Please refer to the `jdb` documentation
for information on setting breakpoints and performing other debugging
tasks. As with running an application, your CLASSPATH environment
variable has to specify the location of all Java classes used in
your application.

If you don't want to attach to a running client application,
you can start up `jdb` using `AppletViewer` or
the interpreter through a class name, for example:

`jdb sun.applet.AppletViewer` _URL_

`jdb com.webobjects.eoapplication.EOApplication` _-applicattionURL
URL_

The advantage of starting up `jdb` like
this is that you can set breakpoints before your application is
executed; `jdb` stops before
it executes the main function of the given class.

|  |
| --- |
| __Note:__ Use the -WOAutoOpenInBrowser NO flag when starting up your server application to prevent the client application from automatically launching in your default browser. |

[![Previous](attachments/JavaClient/Images/previous.gif)](Advanced_Tasks.md)[![Next](attachments/JavaClient/Images/next.gif)](Customizing__Assistants.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
