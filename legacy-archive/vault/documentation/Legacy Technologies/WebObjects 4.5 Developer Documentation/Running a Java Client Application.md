---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.24.html
archived_at: '2026-07-15T08:09:02.109564Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Building%20and%20Testing%20Your%20Application.md) [!](Building%20the%20Application.md) [!](What%20if%20It%20Doesn%27t%20Work.md)

---

#   Running a Java Client Application

A Java Client application is really two applications; one application is on the server and the other is on the client, and they must be running concurrently. You start the server application as you do any WebObjects application in one of the following ways:

- 

  Using Project Builder (during development and testing phases)
- 

  From the command line
- 

  Using the Monitor application (the preferred deployment mechanism)

For the procedures for the last two alternatives, check _Serving WebObjects_. You can launch the server application from Project Builder using the Launch panel.

1. 

   Launch the application with Project Builder.

   Click the Launch button on the main window.

   Click the Launch button on the Launch panel

   !

After starting the server application, start the client application; there are several ways to do this:

- 

  __Using the Java interpreter (java)__: To start the client as a stand-alone Java application outside a browser, use the __java__ interpreter. The syntax for using java to start a Java Client application is:

  java [-classpath classpath]
  com.apple.client.eoapplication.EOApplication
  -applicationURLurl
  [-page pageName]

  You might want to create a script file to make this command automatic and hidden.

  It might not be necessary to specify the
  -classpath
  option, but if the interpreter cannot find classes, you must either modify your CLASSPATH environment variable or add the
  -classpath
  option to the command. The
  -applicationURL
  option specifies the application's URL that you would also use in a browser and the -
  page
  option specifies the name of the page that contains the WOJavaClientApplet component. If pageName is not specified, "Main" is assumed.

  Please note that "com.apple.client.eoapplication.EOApplication" is the name of the class that contains the static main function that is usually used to start up a Java Client WebObjects application. If you have a different main function you must specify the name of the class that implements it instead.
- 

  __Using Microsoft Internet Explorer browsers__

  : To use your Java Client application in this browser, you must use version 4.0 or higher. To view the debugging output, launch Internet Explorer, choose Internet Options from the View menu, enable both Java Logging and Java Console in the Advanced options display, restart Internet Explorer, and select View
  !
   Java Console. You should use Sun's Java Plug-in with Internet Explorer because there are bugs in the browser's Java implementation such as known problems with combo boxes. In addition, if you start a new applet in a browser that has run another applet, the new applet freezes because the browser's Java virtual machine is not restarted. You will need to restart the browser every time you launch your application; quit the browser and then launch the client. This procedure is not necessary if you use Sun's Java Plug-in. If you wish, WebObjects can automatically launch the browser for you.

- 

  __Using Netscape browsers__: To run your Java Client application with a Netscape browser, you currently have to use Sun's Java Plug-in. If you wish, WebObjects can automatically launch the browser for you.
- 

  __Using appletviewer__: The JDK's __appletviewer__ tool is very useful during development because it minimizes your start-up time by removing the need to launch a browser. It also lets you view the debugging output inside the shell where you run __appletviewer__. To use the tool, copy the URL of the server application (displayed in the console output) and paste it a shell window as the argument, for example:

  appletviewer http://_<host>_:1234/WebObjects/MyApp

  If you are running __appletviewer__ on the same machine as the WebObjects application, _<host>_ is "localhost"; otherwise it is the host name of the machine on which the application is running.

There are a few considerations to keep in mind when running a Java Client WebObjects application:

- 

  You can specify
  -WOAutoOpenInBrowser NO
  on the command line to avoid auto-launching a browser when you start up your server application.
- 

  The CLASSPATH environment variable must be correctly set so your application can find all necessary Java classes. If you're using __appletviewer__ or the Java interpreter, you need to include the directory containing your client-side classes. The following CLASSPATH works for a development environment where the client application is running on the server.

  On Mac OS X Server, type the following into the Terminal window from which you execute __appletviewer__ or the Java interpreter.

  setenv CLASSPATH "/System/Library/Java:/System/Library/F
  rameworks/JavaVM.framework/Classes/swingall.jar:<Direct
  oryContainingStudioManager>/StudioManager/StudioManager
  .woa/WebServerResources/Java"

  On Windows NT, type the following into the Bourne Shell from which you execute __appletviewer__ or the Java interpreter..

  export CLASSPATH="C:\Apple\Library\JDK\lib\swingall.jar;
  C:\Apple\Library\Java;C:_<DirectoryContainingStudioManag
  er>_
  \StudioManager\StudioManager.woa\WebServerResources\
  Java"
- 

  If you run the application in a Microsoft Internet Explorer or Netscape browser, you may have to use Sun's Java Plug-in. These browsers currently do not implement the AWT specification exactly or have bugs that prevent Java Client applications from working correctly. In particular, Microsoft Internet Explorer does not reset the Java virtual machine which can cause the application to freeze. To use the plug-in, open the Web component containing your application's WOJavaClientApplet in WebObjectsBuilder and set the __useJavaPlugin__ binding to YES. The first time you start an application using the plug-in, the browser will ask you to download the plug-in (the concrete behavior depends on the browser). Afterwards, the plug-in is loaded automatically. Please refer to Sun's documentation at __http://java.sun.com/products__ for more information.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Building%20and%20Testing%20Your%20Application.md) [!](Building%20the%20Application.md) [!](What%20if%20It%20Doesn%27t%20Work.md)
