---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-29.html
archived_at: '2026-07-15T08:04:51.759877Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Starting%20and%20Stopping%20an%20Application%20Instance.md) [!](Setting%20Command-Line%20Arguments%20in%20Monitor.md) [!](Monitor%20Option%20Summary.md)

---

#### Starting Up Applications From the Command Line

The syntax for starting a WebObjects application from a command shell window is:

> _AppExecutable_
>
>
> [
> -WODebuggingEnabled YES
> |
> NO
> ]
>
> [
> -WOAutoOpenInBrowser YES
> |
> NO
> ]
> [
> -WOMonitorEnabled YES|NO
> [
> -WOMonitorHost
> _hostname_
>
> |subnet
> ]]
>
> [
> -WOCachingEnabled YES
> |
> NO
> ]
> [[
> -WOAdaptor
> _adaptorClass_
> ] [
> -WOPort
> _portNumber_
> ]
> [
> -WOListenQueueSize
> _listenQueueSize_
> ]]
> [
> -WOWorkerThreadCount
> _int_
> ]
> [-WOOtherAdaptors
> _plist_
> ]
> [
> -WOCGIAdaptorURL path
> ] [
> -WOApplicationBaseURL
> _path_
> ]
> [
> -WOFrameworksBaseURL
> _path_
> ] [
> -NSProjectSearchPath
> _plist_
> ]
> [
> -WOIncludeCommentsInResponses YES
> |
> NO
> ] [
> -WOSessionTimeout
> _seconds_
> ]

The _AppExecutable_
variable represents the name of the WebObjects application executable to run. You should enter the command from the directory containing the executable. Compiled applications should either be located in  ___NEXT_ROOT___
__/Local/Library/WebObjects/Applications__
(recommended) or under  ___DOC_ROOT___
__/WebObjects__
. For scripted applications, go to the application's __.woa__
directory and execute __WODefaultApp__
, which is located in  ___NEXT_ROOT___
__/Library/WebObjects/Executables__
.

The following table describes each command-line option:

|  Option | Description |
| --- | --- |
| -WODebuggingEnabled   YES|NO | Sets whether the application prints messages to standard error during startup. By default, this option is enabled.  WOApplication, WOComponent, and WOSession define a __debugWithFormat:__ method (__debugString__ in Java). This method is similar to __logWithFormat:__ except that it only prints messages if the __WODebuggingEnabled__ option is on. |
| -WOAutoOpenInBrowser   YES|NO | Sets whether the application automatically opens a web browser window to the application's URL (starting up the browser if necessary). By default, this option is enabled. |
| -WOMonitorEnabled   YES|NO | Enables or disables monitoring. By default, this option is disabled. If this option is enabled and you manually start an application, the application tries to find a running WOMonitor. |
| -WOCachingEnabled   YES|NO | Requests that the application cache component definitions (templates) instead of reparsing HTML and declaration files upon each new HTTP request. By default, this option is disabled. |
| -WOAdaptor adaptorClass | The WOAdaptor class name. The default is WOMultiThreadedAdaptor. |
| -WOPort portNumber | The socket port used to connect to an application instance. This option is independent of the adaptor option. A portNumber of -1 means use an arbitrary high port number; however, you cannot specify -1 as the value on the command line; to set the value to -1, you must use the __defaults__ command. |
| -WOListenQueueSize listenQueueSize | The depth of the listen queue. The default is 5, meaning that while the application process is handling a request, up to five other requests can be in the socket buffer before the socket starts refusing them. If the application is expected to experience "spikes" in its processing load, it might be a good idea to increase the listen queue depth. Increasing this default does not necessarily improve performance or allow the application to serve more requests at sustained high loads. For more information, see [Increasing the Listen Queue Depth](Increasing%20the%20Listen%20Queue%20Depth.md#apple-geztqmzw). |
| -WOWorkerThreadCount int | Maximum number of worker threads for a multithreaded application. The default worker thread count is 8. Setting this count to 0 results in single-threaded (WebObjects 3.5-style) request dispatch. |
| -WOOtherAdaptors plist | Use this option to attach additional adaptors (other than the one specified by __-WOAdaptor__ ) to the application. The plist option is an array of dictionaries written in property-list format. |
| -WOCGIAdaptorURL   path | The absolute URL that points to the WebObjects CGI adaptor. |
| -WOApplicationBaseURL  _aURL_ | The URL where your application's resources are located under the web server's document root. You may place your application anywhere under the document root. This option is required when you're using a web server. If you install the application in a subdirectory of _DOC_ROOT_ __/WebObjects__ , you should set this to point to the exact location of the application directory. If you don't set the application's base URL, your application can still run but it cannot find image files and other web server resources. |
| -WOFrameworksBaseURL  _aURL_ | The location of frameworks under your document root if you're using a web server. The default is __/WebObjects/Frameworks__ (as it was in release 3.5). All frameworks that your application uses must be in this directory. |
| -NSProjectSearchPath  pList | An array of paths in which your project directories are located. (The array is written in property-list format.) The default is a single item: ".."  If you specify this option, WebObjects looks in the locations you specify for a project that has the same name as the application or framework being loaded. If it finds a project, it uses the images, scripted components, and other resources from the project directory instead of from the application or framework's main bundle. This way, you can modify images and scripted components in your project and test them without having to rebuild the application. |
| -WOIncludeComments  InResponses YES|NO | Sets whether the HTML parser includes comments from the components' HTML files in the responses. The default is YES. |
| -WOSessionTimeout _timeout_ | Sets the timeout interval for sessions. By default, they now time out after 3600 seconds. |
| -WORecordingPath _path_ | Enables session recording and sets the location where the recording file is to be stored. Automatically creates a directory, if one doesn't exist. An extensions of ".rec" is appended to the specified path. See [Recording a Session](Recording%20a%20Session.md#apple-g43dsmrq) for more information. |

You can also set these options programmatically or by using the __defaults__
utility. Be careful when setting options programmatically. Most options require knowledge of the environment in which the application runs, and the appropriate values change if you move the application to a different machine. For example, you should never set the __WOPort__
option programmatically.

__Notes__

The web server uses the  ___DOC_ROOT_
and__
ApplicationName
arguments to build URLs, so you should use forward slashes as opposed to a backslashes when specifying these arguments.

As a convenience, you could create a shell script that starts WebObjects applications when the server machine is booted. You could also create another shell script that you can run at the command line to start applications.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Starting%20and%20Stopping%20an%20Application%20Instance.md) [!](Setting%20Command-Line%20Arguments%20in%20Monitor.md) [!](Monitor%20Option%20Summary.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
