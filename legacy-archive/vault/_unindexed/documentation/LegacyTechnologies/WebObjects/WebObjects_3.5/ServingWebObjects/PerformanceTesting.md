---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/PerformanceTesting.html
archived_at: '2026-07-15T07:56:03.570202Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/Statistics.html)[Previous
Section](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/Statistics.html) 

## Performance Testing

The WebObjects package comes with a special adaptor
that allows you to record a session and a tool that helps you play back
a recorded session. Using these tools, you can test your application setup
to determine if you have the appropriate number of instances running, the
appropriate amount of memory allocated, and so on.

__Note:__ You cannot use the recording and playback
tools on applications that use HTML frames.

To use the recording and playback performance testing
tools, do the following:

1. Copy the adaptor __WebObjects-Recording__ from _NeXT_ROOT___/NextLibrary/WOAdaptors/CGI__to your web server's cgi-bin directory. 
2. Use the Monitor to create an instance of the application. 
3. Start the application instance you just created. To do so, open a command-shell
   window and enter the command line as shown in the section "[Starting
   Up Applications From the Command Line](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/ManualStarting.html#4941)." Use the __-n__ option
   (which must be used in conjunction with the __-a__ option) to specify
   the instance number. Also use the __-browser OFF__ option so that the
   application does not automatically launch in your web browser. For example,
   your command line might look like this:

```
        MyApp -a WODefaultAdaptor -n instanceNumber -c -browser OFF
```


4. In your web browser, enter this URL:

```
http://localhost/cgi-bin/WebObjects-Recording/MyApp?file=completePath
```


where _completePath_ is the directory in which you want to store
the recorded session. The adaptor appends a __.rec__ extension to the
path you specify.

5. Using the web browser, run a session of your WebObjects application.
   You may want to record what you believe to be a typical session, or you
   may want to perform a session that would put a maximum load on your system.
   For example, you may want to record a session that performs as many database
   fetches as possible. 

__Important:__ During recording, only one user may be accessing the
application. Your session must not include any backtracking to a previously
displayed page. If you backtrack, you'll get unpredictable results.

As you run the application, the WebObjects recording adaptor records
each request and response to a separate file in the directory you specified.

6. When you have finished the session, close the browser window. To prevent
   accidental calls to the WebObjects-Recording adaptor, remove it from your
   server's cgi-bin directory. 
7. Open a command shell window and enter this command:

```
        WOPlayback -R completePath.rec -H hostname
```


where _completePath___.rec__ is the directory that contains
the recorded session and _hostname_ is the name of the host on which
you want to run the recorded session.

The WOPlayback tool plays the recorded session repeatedly until you
explicitly stop it (for example, by pressing Control-C in a command shell
window). It is possible to run several versions of WOPlayback at the same
time to put more load on the server.

If you want, you can specify other options to the
WOPlayback tool as well. The following is a list of the available options:

**-P _http_port_ **
: The port number of your HTTP server (the default is 80). 

**-C _count_ **
: Plays back the session _count_ number of times instead of indefinitely.

**-S _sleep_time_ **
: The number of seconds to wait in between requests. The default is 0.

**-p _adaptor_path_ **
: Sends request using the _adaptor_path_ instead of the recorded
URL. For example, suppose you recorded a session using a Netscape server
whose cgi-bin directory is named __cgi-bin__ and you want to play it
back using the Microsoft Internet Information Server, whose cgi-bin directory
is named __Scripts__ and has __WebObjects.dll__ as the adaptor name.
Your _adaptor_path_ is

```
                /Scripts/WebObjects.dll
```

If you'd like to improve the average response time
that resulted from this test, read the next section, "[Improving
Performance](PerformanceTuning.md#apple-guydmoi)" for guidelines on how to do so.

[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](PerformanceTuning.md)[Next
Section](PerformanceTuning.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
