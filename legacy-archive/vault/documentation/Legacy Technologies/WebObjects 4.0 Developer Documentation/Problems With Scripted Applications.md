---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.9.html
archived_at: '2026-07-15T08:00:24.867458Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md) [!Previous Section](Troubleshooting.md)

#   Problems With Scripted Applications

Scripted example applications (HelloWorld, TimeOff, etc.) are the simplest ones and don't contain compiled code.

#####  -------------------------------------------------------------------------------------------------------------

##  Problem

The web browser does not launch or launches the incorrect URL

##  Checklist

1. 

   __Check the debugging statements printed in the command-shell window.__

> 
>
> When you launch a WebObjects application from the command line, the application computes its own URL, launches the web browser, and enters the URL in the browser. It prints messages about the values it computes to standard output.

> 
>
> Check the standard output (the command-shell window) for these messages (among others):

> ```
> The applicationPath: /System/Developer/Examples/WebObjects/WebScript/HelloWorldThe applicationBaseURL: /WebObjects/HelloWorldOpening application's URL in Browser: url
> ```

> 
>
> __Corrective action:__

> 
>
> If you see these messages but your web browser doesn't launch, you might not have a browser installed on your system, or WebObjects cannot find the browser. This is always true on Solaris and HP-UX. If the URL looks correct (as described below), open your browser and type that URL into it.

> 
>
> If you see a message that says "No Adaptor URL in WebServerConfig.plist," either the __WebServerConfig.plist__
> file is missing, or the __WOAdaptorURL__
> key is missing from it. The file should look something like this:

> ```
> {
> ```

> ```
> \xDD\xDD\xDDDocumentRoot = "/Apple/Library/WebServer/Documents";
> ```

> ```
> \xDD\xDD\xDDWOAdaptorURL = "http://localhost/cgi-bin/WebObjects";
> ```

> ```
> }
> ```

> 
>
> If __WOAdaptorURL__
> is missing, the web browser does not launch when you launch a WebObjects application. You can enter __WOAdaptorURL__
> or you can type the URL in the browser and connect to the running application that way.

> 
>
> This base URL value of __WOAdaptorURL__
> is of the form:

> ```
> http://localhost/cgi-bin/WebObjects
> ```

> 
>
> _cgi-bin_ is the name of your HTTP server's cgi-bin directory. You specify this name when you configure your HTTP server. The _cgi-bin_ directory name is often __cgi-bin__
> , but it may have a different name. For example, the Microsoft Internet Information Server uses the name __Scripts__
> .

> 
>
> _WebObjects_ is the name of the WebObjects CGI adaptor as you see it in your HTTP server's cgi-bin directory. Usually, the name is WebObjects. If you're using Windows NT, the adaptor name might be __WebObjects.exe__
> (however, some older Netscape servers don't use the __.exe__
> extension.)

> 
>
> If the base URL's cgi-bin and WebObjects adaptor names look correct, consider the __localhost__
> value. On most sites, __localhost__
> accesses the server on the local host. However, some sites require a domain name as well (__http://localhost.apple.com__
> ). If your HTTP server isn't running on your local machine, use the host name of the machine running the server in place of "localhost" in the URL above, and make sure a WebObjects adaptor is installed on that machine.

#####  -------------------------------------------------------------------------------------------------------------

##  Problem

A simple scripted application won't run properly.

##  Checklist

1. 

   Try using direct-connect to access your WebObjects application.
2. 

   __Check that you can load a static page.__

> 
>
> __Corrective action:__

> 
>
> If your browser displays a message saying that it was unable to connect or that the connection was refused, your HTTP server is probably not running. Check that your server is running. Otherwise, see _[Checking the Installation](Troubleshooting.md#apple-giztsmbt)_ for information on how to fix your installation of WebObjects.

1. 

   __Check that the WebObjects adaptor is functioning.__

> 
>
> Check that the WebObjects adaptor is installed correctly and can run. Use your browser to open this URL (which specifies the WebObjects adaptor, but fails to specify an application name):

> ```
> http://localhost/cgi-bin/WebObjects
> ```

> 
>
> (You may need to replace "localhost" with the name of the host running your HTTP server. You may also need to replace "cgi-bin" with the actual name of the directory that contains scripts and CGI programs on your server.) If the WebObjects adaptor is installed correctly, it returns the following error message:

> ```
> Invalid application name
> ```

> 
>
> If the adaptor is installed incorrectly or can't run, the browser will instead display a message indicating that the requested object cannot be located. The message may look like this:

> ```
> 404 Not FoundThe requested URL /cgi-bin/WebObjects was not found on this server.
> ```

> 
>
> __Corrective action:__

> 
>
> Make sure you've supplied the right names in the URL for the host ("localhost" in the example above) and for the cgi-bin directory (sometimes named "Scripts" or "cgiPrograms" rather than "cgi-bin"). Otherwise, see _[Checking the Installation](Troubleshooting.md#apple-giztsmbt)_for information on how to fix your installation of WebObjects.

[!Table of Contents](About%20This%20Document.md) [!Next Section](Problems%20With%20Compiled%20Applications.md)
