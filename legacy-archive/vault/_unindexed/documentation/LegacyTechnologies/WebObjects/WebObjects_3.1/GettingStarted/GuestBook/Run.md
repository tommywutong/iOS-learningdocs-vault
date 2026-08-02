---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/Run.html
archived_at: '2026-07-15T07:48:48.861566Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](AwakeSleep.md)

# Run the application

If you look at your application in the file system, you can see the files WebObjects Builder created for you. The __Application.wos__ script is directly under the __GuestBook.woa__ directory, and there are three files under __Main.wo__: an HTML file, a script file, and a _declarations file_, which holds the bindings between the script and the HTML file. You might also see files with a __.woo__ extension or files named __API.table__. These are files created and used internally by WebObjects and WebObjects Builder. You'll also see a __Session.wos__ file (for the session script) directly under __GuestBook.woa__, but it is an empty file because GuestBook does not need a session script.

- Launch your web browser (for example, Netscape Navigator).
- Load a URL with the following form:

`http://`_web_server_host_`/`_cgi-bin_directory_`/`_adaptor_`/`_application_directory_

For example, with a web server named Gandhi, a cgi-bin directory named __cgi-bin__, a WebObjects adaptor named __WebObjects__, and an application directory named __GuestBook__, use this URL:

```
http://Gandhi/cgi-bin/WebObjects/GuestBook
```


It's common to store all of your application in one directory under __WebObjects__. If you do this, you must give the path to the application. For example, if you stored the __GuestBook.woa__ directory in the directory _<DocumentRoot>___/WebObjects/MyApps__, the URL would be:

```
http://Gandhi/cgi-bin/WebObjects/MyApps/GuestBook
```


To learn what happens when you run a WebObjects application, see "[Connecting to a WebObjects Application](../../DevGuide/Intro/ConnectingAppToWeb.md)" in the introduction to the _WebObjects Developer's Guide_.

## Troubleshooting

If you have trouble running the application, try running it manually. To do so, open a DOS command window and enter this command:
`%NEXT_ROOT%\NextLibrary\Executables\WODefaultApp -d` _server_`/`_DocumentRoot_ _application_directory_
where __NEXT_ROOT__ is usually __c:\NeXT__, _server_`/`_DocumentRoot_ is the full path of the server's document root directory, and _application_directory_ is the application's directory (relative to the __WebObjects__ directory). For example:
`c:\NeXT\NextLibrary\Executables\WODefaultApp -d c:/netscape/ns-home/docs GuestBook` 
__Note:__ Be sure to use forward slashes in the arguments to __WODefaultApp__.
This command starts up the WebObjects default executable, which runs the GuestBook application and connects it to the WebObjects Framework. Once you have started this executable, go back to your Web browser and reload the URL. Make sure that the URL actually reloads. If necessary, quit the browser and start it up again.
