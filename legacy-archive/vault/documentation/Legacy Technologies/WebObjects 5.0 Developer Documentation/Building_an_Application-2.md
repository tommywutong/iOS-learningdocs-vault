---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Building_an_Application.html
archived_at: '2026-07-15T08:12:19.976989Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Creating_a__ent_Project.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Examining_the_Application.md)

## Building and Running the Application

Building and running the application is just like building
and running any other Java Client application. Simply perform the
following steps.

1. Build the
   application.

   Click ![[image: ../Art/buildicon.gif]](../Art/buildicon.gif)
   in
   Project Builder's main window.
2. Set execution options.

   Click on the Targets tab.

   Click
   the D2JCTutorial target in the Targets list.

   Click the
   Executables tab on the content area.

   Click Add on the
   Arguments panel.

   On the text box type `-WOPort
   8888 -WOAutoOpenInBrowser NO`. These arguments
   facilitate the development process.

   - __WOPort__ Specify
     any port you want. It is not necessary to specify a port, but it
     is convenient. By specifying a port, the application URL (used to
     start the client application) doesn't change between executions.
     If the application URL is always the same, you can start the client
     application with the same command each time.
   - __WOAutoOpenInBrowser__ Specify `NO` so
     the client application is not automatically launched in a browser.
     Java Client applications should be run as Java applications.
3. Start the server application.

   Click ![[image: ../Art/launchicon.gif]](../Art/launchicon.gif)
   in Project Builder's main
   window.
4. Start the client application.

   In a shell, navigate to
   the `D2JCTutorial/build/D2JCTutorial.woa/Contents/MacOS` directory.

   Execute
   the script `D2JCTutorial_Client` with
   the HTTP address of the server application. You can copy it from
   the output that Project Builder produced when it launched the server
   application. The launch command should be similar to the following:

   ```
   ./D2JCTutorial_Client http://ebruce.apple.com:8888
   ```

### If the Client Application Doesn't Start

Verify that your application's URL is correct. Check the
messages in the Run panel. At the bottom, you'll see the following
messages:

```
The URL for webserver connect is:
http://ebruce.apple.com/cgi-bin/WebObjects/D2JCTutorial.woa/-8888
The URL for direct connect is:
http://ebruce.apple.com:8888/cgi-bin/WebObjects/D2JCTutorial
Waiting for requests...
```

Verify that the application URL you use to start the application
has the same host name and port number as the one in the Run panel's
output.

### If the Application Has No Windows

Verify that the project includes the JavaBusinessLogic framework.
Direct to Java Client dynamically generates an application based
on model files. In this application, the model files come from the
JavaBusinessLogic framework.

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Creating_a__ent_Project.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Examining_the_Application.md)

© 2001 Apple Computer, Inc.
