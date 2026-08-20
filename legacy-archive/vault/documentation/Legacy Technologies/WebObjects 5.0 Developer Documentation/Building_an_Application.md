---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/Building_an_Application.html
archived_at: '2026-07-15T08:13:58.394048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Creating_th_r_Interface.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Enhancing/index.html)

## Building and Testing Your Application

You have now created a Java Client application-a fairly
trivial one, to be sure, but still one with all the essential ingredients.
Now it is a good idea to build and test your application to catch
any problems. Interface Builder gives you a way to test your user
interface even before any code is compiled. However, to gauge the
complete picture, you still should build your application and test
it.

### Building the Application

You build a Java Client project using Project Builder.

1. Go to the
   Project Builder main window and Make sure that the StudioManager
   target is selected in the target pop-up menu.
2. Click ![[image: ../Art/buildicon.gif]](../Art/buildicon.gif)
   to
   build the application.

If there are any coding or linking errors, the Build pane
displays them; click an error message in the upper part of the pane
to go to the site of the error in the code editor.

![[image: ../Art/buildwitherror.gif]](../Art/buildwitherror.gif)

For information about debugging, see ["Debugging Java Client WebObjects Applications"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Advanced/iDebugging_J_pplications.html).

### Browser Launch by Project Builder

When launching a WebObjects application, Project Builder's
default behavior is to launch your Web browser. Unless you are using
applets, this is not the desired behavior for Java Client applications.
Therefore, you must tell Project Builder not to launch your browser when
you run the StudioManager server-side application.

1. Click the
   Targets tab.
2. Select the StudioManager target in the Targets list.
3. Click the Executables tab in the content area.
4. Click Add on the lower-right corner of the content area.
5. Type `-WOAutoOpenInBrowser NO` in
   the Launch Arguments column of the Arguments panel.

![[image: ../Art/browserdisplay.gif]](../Art/browserdisplay.gif)

### Running a Java Client Application

A Java Client application is really two applications: a server-side
application and a client-side application (or applet); they must
be running concurrently. You start the server application as you
do any WebObjects application in one of the following ways:

- using Project
  Builder (during development and testing)
- from the command line
- using the Monitor application (the preferred deployment mechanism)

For the procedures for the last two options, check _Serving
WebObjects_. You can launch the server application from
Project Builder by clicking the Launch icon.

![[image: ../Art/launchicon.gif]](../Art/launchicon.gif)

After starting the server application, start the client application;
there are several ways to do this:

- __Using
  the Java interpreter (java)__ To start the client as a
  stand-alone Java application outside a browser, use the `java` interpreter.
  The syntax for using `java` to
  start a Java Client application is

  ```
      java [-classpath classpath]      com.apple.client.eoapplication.EOApplication     -applicationURLurl      [-page pageName]
  ```

  You
  might want to create a script file to make this command automatic
  and hidden.

  It might not be necessary to specify the `-classpath` option,
  but if the interpreter cannot find classes, you must either modify
  your `CLASSPATH` environment
  variable or add the `-classpath` option
  to the command. The `-applicationURL` option
  specifies the application's URL that you would also use in a browser
  and the `-page` option
  specifies the name of the page that contains the WOJavaClientApplet
  component. If `pageName` is not
  specified, "Main" is assumed.

  Please note that `com.webobjects.eoapplication.EOApplication` is
  the name of the class that contains the static main function
  that is usually used to start up a Java Client WebObjects application.
  If you have a different main function
  you must specify the name of the class that implements it instead.
- __Running the client launch script__ This
  is another way to launch the client as a stand-alone application.
  The launch script is named after your project, with the `_Client` postfix.
  It's located in your project folder in `build/StudioManager.woa/Contents/MacOS`. The
  script takes as its argument the server application's URL (displayed
  in the console output).

  For example, to run the StudioManager
  client application, you would type something similar to the following
  in your shell:

  ```
  cd ~/Projects/StudioManager/build/StudioManager.woa/Contents/MacOS

  ./StudioManager_Client http://localhost:49387/cgi-bin/WebObjects/StudioManager
  ```
- __Using MRJAppBuilder__ You can use the
  MRJAppBuilder application to build a double-clickable application.
- __Using appletviewer__ The JDK's `appletviewer` tool
  is very useful during development because it minimizes your start-up
  time by removing the need to launch a browser. It also lets you
  view the debugging output inside the shell where you run `appletviewer`. To
  use the tool, copy the URL of the server application (displayed
  in the console output) and paste it in a shell window as the argument,
  for example:

  ```
  appletviewer http://<host>:1234
  ```

  If
  you are running `appletviewer` on
  the same machine as the WebObjects application, _<host>_ is
  "localhost"; otherwise it is the host name of the machine on
  which the application is running.
- __Using browsers__ see explanation below.

There are a few considerations to keep in mind when running
a Java Client WebObjects application:

- You can specify `-WOAutoOpenInBrowser
  NO` on the command line to avoid auto-launching a
  browser when you start up your server application. See ["Browser Launch by Project Builder"](#apple-ijbusr2hindes) for
  more information.
- The `CLASSPATH` environment
  variable must be correctly set so your application can find all
  necessary Java classes. If you're using `appletviewer` or
  the Java interpreter, you need to include the directory containing
  your client-side classes. The following `CLASSPATH` works
  for a development environment where the client application is running
  on the server.

  Type the following command into the Terminal
  window from which you execute `appletviewer` or
  the Java interpreter.

  ```
  setenv CLASSPATH "/System/Library/Java:/System/Library/Frameworks /JavaVM.framework/Classes/swingall.jar:<DirectoryContainingStudioManager >/StudioManager/StudioManager.woa/WebServerResources/Java"
  ```
- `Using Web browsers`:
  If you run the application in a Microsoft Internet Explorer or Netscape
  browser, you have to use Sun's Java Plug-in.

  These browsers
  currently do not implement the J2SE specification exactly or have
  bugs that prevent Java Client applications from working correctly.
  In particular, Microsoft Internet Explorer does not reset the Java
  virtual machine, which can cause the application to freeze. In addition,
  if you start a new applet in a browser that has run another applet,
  the new applet freezes because the browser's Java virtual machine
  is not restarted. You will need to restart the browser every time
  you launch your application, quit the browser and then launch the
  client. This procedure is not necessary if you use Sun's Java
  Plug-in. The first time you start an application using the plug-in,
  the browser will ask you to download the plug-in (the concrete behavior depends
  on the browser). Afterwards, the plug-in is loaded automatically.
  Please refer to Sun's documentation at http://java.sun.com/products for
  more information.

### What If It Doesn't Work?

What if you test-run the application and it doesn't work?

- If no data
  appears in the table, look in the Attributes pane of the Studio EODisplayGroup
  Info window to make sure that "Fetch on load" is selected.
- If the buttons don't have the desired effect, make sure
  that they're connected to the appropriate action method in the
  appropriate object.
- If you get database errors when you try to add and delete
  studios or save changes, make sure that your model is properly specified.
  In particular, check that all of your entities have primary keys.
  Finally, choose Check Consistency from the Model menu in EOModeler
  to confirm that there are no problems in your model.

### What You've Got So Far

Until now you have still not written a single line of code.
However, because of the built-in features of Enterprise Objects
Framework, all of the following have been provided for you:

- automatic
  primary-key generation when you insert a new object

  Every row
  in a database is uniquely identified by the value of its primary-key
  column. When you create a new object in your application and save
  it to the database, you're adding a new row to a database table,
  and this row needs a primary key (that is, it needs to have a unique
  value for the primary-key attribute you set in EOModeler). Enterprise Objects
  Framework handles generating this unique value for you.
- formatting of currency values and dates
- coordinating the user interface with your data

  Enterprise
  Objects Framework keeps all parts of an application synchronized
  with the current view of the data. For example, if you have two
  windows in an application that are displaying the same data and
  you change the values in one window, the other is automatically
  updated to reflect the changes.

### Optional Exercise

Enterprise Objects Framework provides additional action methods
that you can use in connections: fetch (EODisplayGroup)
and refetch (EOEditingContext). Try
adding controls (such as buttons or menu items) to the application
and connecting them to some of these action methods.

[![Previous](attachments/JavaClient/Images/previous.gif)](Creating_th_r_Interface.md)[![Next](attachments/JavaClient/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Enhancing/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
