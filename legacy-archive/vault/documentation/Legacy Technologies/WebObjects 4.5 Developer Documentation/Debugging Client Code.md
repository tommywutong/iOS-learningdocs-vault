---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.38.html
archived_at: '2026-07-15T08:09:16.408878Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Debugging%20Java%20Client%20WebObjects%20Applications.md) [!](Debugging%20Server%20Code.md) [!](Customizing%20Your%20Project%20With%20Wizards.md)

---

#  Debugging Client Code

Project Builder currently provides no support for debugging the client side of a Java Client application. Instead, use the Java debugger __jdb__ (included with the JDK) in a shell window.

Before you can debug client code, compile your Java classes with the
-g
flag specified. To do this, either "make debug" your project or enter
OTHER_JAVAC_FLAGS=-g
as a build argument in Project Builder's Build Options panel.

Once your code has compiled, start up the client application with __appletviewer__ or with the __java__ interpreter (see "[Running a Java Client Application](Running%20a%20Java%20Client%20Application.md#apple-obtwmslehuytambwgy4dk)
" in the tutorial) with the
-debug
flag . These tools then print a "password" that you can use later to attach __jdb__ to your client application. To attach __jdb__, open another shell and enter the following command:

jdb -password _password_

Please refer to the __jdb__ documentation for information on setting breakpoints and performing other debugging tasks. As with running an application, your CLASSPATH environment variable has to specify the location of all Java classes used in your application.

If you don't want to attach to a running client application, you can start up __jdb__ using __appletviewer__ or the interpreter through a class name, for example:

jdb sun.applet.AppletViewer _URL_

jdb com.apple.client.eointerface.EOApplication _URL_

The advantage of starting up __jdb__ like this is that you can set breakpoints before your application is executed; __jdb__ stops before it executes the main function of the given class.

__Note:__

Use the
-WOAutoOpenInBrowser NO
flag when starting up your server application to prevent the client application from automatically launching in your default browser.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Debugging%20Java%20Client%20WebObjects%20Applications.md) [!](Debugging%20Server%20Code.md) [!](Customizing%20Your%20Project%20With%20Wizards.md)
