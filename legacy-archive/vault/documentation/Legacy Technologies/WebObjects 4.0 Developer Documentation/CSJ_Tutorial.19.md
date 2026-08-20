---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.19.html
archived_at: '2026-07-15T07:59:30.368730Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.18.md) | [Back Up One Level](CSJ_Tutorial.16.md) | [Next](CSJ_Tutorial.1a.md)

###   Running a Java Client Application

A Java Client application is really two applications; one application is on the server and the other is on the client, and they must be running concurrently. You start the server application as you do any WebObjects application in one of the following ways:

- Using Project Builder (during development and testing phases)

- From the command line
  - Using the Monitor application (the preferred deployment mechanism)

    For the procedures for the last two alternatives, check _Serving WebObjects_
    . You can launch the server application from Project Builder using the Launch panel.

    __1. Launch the application with Project Builder.__
    > 
    >
    > Click the Launch button on the main window.
    >
    > 
    >
    > Click the Launch button on the Launch panel
    >
    > ###### 
    >
    > !
    >
    > 
    >
    > After starting the server application, start the client application; there are several ways to do this:
    >
    > 
    >
    > - __Using the Java interpreter (java)__
    >   : To start the client as a stand-alone Java application outside a browser, use the __java__
    >   interpreter. The syntax for using java to start a Java Client application is:
    >   `
    >
    >   java [-classpath classpath]
    >   com.apple.client.eointerface.EOApplication url
    >   [pageName]`
    >
    >   
    >
    >   You might want to create a script file to make this command automatic and hidden.
    >
    >   
    >
    >   It might not be necessary to specify the
    >   -classpath
    >   option, but if the interpreter cannot find classes, you must either modify your CLASSPATH environment variable or add the
    >   -classpath
    >   option to the command. The url option is the application's URL that you would also use in a browser and pageName is the name of the page that contains the WOJavaClientApplet component. If pageName is not specified, "Main" is assumed.
    >
    >   
    >
    >   Please note that "com.apple.client.eointerface.EOApplication" is the name of the class that contains the static main function that is usually used to start up a Java Client WebObjects application. If you have a different main function you must specify the name of the class that implements it instead.
    >
    >   
    >
    >   __- Using Microsoft Internet Explorer browsers__
    >   
    >
    >   : To use your Java Client application in this browser, you must use version 4.0 or higher. To view the debugging output, launch Internet Explorer, choose Internet Options from the View menu, enable both Java Logging and Java Console in the Advanced options display, restart Internet Explorer, and select View !
    >   Java Console. It is recommended that you use Sun's Java Plug-in with Internet Explorer because there are bugs in the browser's Java implementation such as known problems with combo boxes. In addition, if you start a new applet in a browser that has run another applet, the new applet freezes because the browser's Java virtual machine is not restarted. You will need to restart the browser every time you launch your application; quit the browser and then launch the client. This procedure is not necessary if you use Sun's Java Plug-in. If you wish, WebObjects can automatically launch the browser for you.
    >
    >   
    >
    >   __- Using Netscape browsers__
    >   : To run your Java Client application with a Netscape browser, you currently have to use Sun's Java Plug-in. If you wish, WebObjects can automatically launch the browser for you.
    >
    >   
    >
    >   __- Using appletviewer__
    >   : The JDK's __appletviewer__
    >   tool is very useful during development because it minimizes your start-up time by removing the need to launch a browser. It also lets you view the debugging output inside the shell where you run __appletviewer__
    >   . To use the tool, copy the URL of the server application (displayed in the console output) and paste it a shell window as the argument, for example:
    >
    >   
    >
    >   `appletviewer http://
    >   <host>
    >   :1234/WebObjects/MyApp`
    >
    >   
    >
    >   If you are running __appletviewer__
    >   on the same machine as the WebObjects application, _<host>_
    >   is "localhost"; otherwise it is the host name of the machine on which the application is running.
    >
    >   There are a few considerations to keep in mind when running a Java Client WebObjects application:
    >
    > 
    >
    > - You can specify
    >   -WOAutoOpenInBrowser NO
    >   on the command line to avoid auto-launching a browser when you start up your server application.
    >
    >   
    > - The CLASSPATH environment variable must be correctly set so your application can find all necessary Java classes. If classes cannot be found, you should modify your CLASSPATH. The installer should correctly configure the CLASSPATH.
    >
    >   
    > - If you run the application in a Microsoft Internet Explorer or Netscape browser, you may have to use Sun's Java Plug-in. These browsers currently do not implement the AWT specification exactly or have bugs that prevent Java Client applications from working correctly. In particular, Microsoft Internet Explorer does not reset the Java virtual machine which can cause the application to freeze. To use the plug-in, open the Web component containing your application's WOJavaClientApplet in WebObjectsBuilder and set the __useJavaPlugin__
    >   binding to YES. The first time you start an application using the plug-in, the browser will ask you to download the plug-in (the concrete behavior depends on the browser). Afterwards, the plug-in is loaded automatically. Please refer to Sun's documentation at [__http://java.sun.com/products__](http://java.sun.com/products)
    >   for more information.
    >
    > ---
    >
    > \xA9 1999 Apple Computer, Inc.
    >
    > [Previous](CSJ_Tutorial.18.md) | [Back Up One Level](CSJ_Tutorial.16.md) | [Next](CSJ_Tutorial.1a.md)
    >
    > 
    >
    > Copyright © 2016 Apple Inc. All rights reserved.
    >
    > - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
    > - [Privacy Policy](http://www.apple.com/privacy/)
