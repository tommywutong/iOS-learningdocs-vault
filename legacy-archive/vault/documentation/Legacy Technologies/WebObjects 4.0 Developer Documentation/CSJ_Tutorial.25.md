---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.25.html
archived_at: '2026-07-15T07:59:52.294645Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.24.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.26.md)

###  Debugging Client Code

Project Builder currently provides no support for debugging the client side of a Java Client application. Instead, use the Java debugger __jdb__
(included with the JDK) in a shell window.

Before you can debug client code, compile your Java classes with the
-g
flag specified. To do this, either "make debug" your project or enter
OTHER_JAVAC_FLAGS=-g
as a build argument in Project Builder's Build Options panel.

Once your code has compiled, start up the client application with __appletviewer__
or with the __java__
interpreter (see "[Running a Java Client Application](CSJ_Tutorial.19.md#apple-gmzdmmzz)
" in the tutorial) with the
-debug
flag . These tools then print a "password" that you can use later to attach __jdb__
to your client application. To attach __jdb__
, open another shell and enter the following command:

`jdb -password
password`

Please refer to the __jdb__
documentation for information on setting breakpoints and performing other debugging tasks. As with running an application, your CLASSPATH environment variable has to specify the location of all Java classes used in your application.

If you don't want to attach to a running client application, you can start up __jdb__
using __appletviewer__
or the interpreter through a class name, for example:

`jdb sun.applet.AppletViewer
URL`

`jdb com.apple.client.eointerface.EOApplication
URL`

The advantage of starting up __jdb__
like this is that you can set breakpoints before your application is executed; __jdb__
stops before it executes the main function of the given class.

__Note:__ Use the
-WOAutoOpenInBrowser NO
flag when starting up your server application to prevent the client application from automatically launching in your default browser.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.24.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.26.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
