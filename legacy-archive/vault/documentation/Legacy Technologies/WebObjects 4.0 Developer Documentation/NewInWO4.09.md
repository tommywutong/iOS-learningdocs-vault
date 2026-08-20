---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.09.html
archived_at: '2026-07-15T07:59:04.678343Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Running%20an%20Application%20on%20WebObjects%204.0.md)

## Command-Line Options

WebObjects 4.0 uses the Foundation NSUserDefaults object to specify application command-line options. As a consequence, all options have been renamed. The following table lists the WebObjects 3.5 options with their new names.

|  Old Option |  New Option |  Description |
|  -debug  ON|OFF |  -WODebuggingEnabled  YES|NO |  Sets whether the application prints messages to standard error during startup. By default, this option is enabled.  WOApplication, WOComponent, and WOSession define a new debugWithFormat: method (debugString in Java). This method is similar to logWithFormat: except that it only prints messages if the WODebuggingEnabled option is on |
|  -browser  ON|OFF |  -WOAutoOpenInBrowser  YES|NO |  Sets whether the application automatically opens a web browser window to the application's URL (starting up the browser if necessary). By default, this option is enabled. |
|  -m  ON|OFF |  -WOMonitorEnabled  YES|NO |  Enables or disables monitoring. By default, this option is disabled. If this option is enabled and you manually start an application, the application tries to find a running Monitor. |
|  -mhost  _hostName_ | subnet |  -WOMonitorHost  _hostName_ | subnet |  If the __WOMonitorEnabled__ option is on and you use this option, the application tries to find a running Monitor on the machine named _hostName_ instead of on the local machine. If subnet is used, the application looks for a running Monitor in its network subnet. |
|  -c |  -WOCachingEnabled  YES|NO |  Requests that the application cache component definitions (templates) instead of reparsing HTML and declaration files upon each new HTTP request. By default, this option is disabled. |
|  -d _documentRoot_ |  None |  You are no longer required to specify the document root. |
|  -a _adaptorClass_ |  -WOAdaptor _adaptorClass_ |  The WOAdaptor class name. The default is now WOMultiThreadedAdaptor. See the section [Support for Multithreaded Applications](Support%20for%20Multithreaded%20Applications.md#apple-giytknry) for more information on WOMultiThreadedAdaptor. |
|  -i _instanceNumber_ |  None |  You are no longer required to specify instance numbers when load-balancing applications. The instance number is now private to the configuration file. |
|  -p _portNumber_ |  -WOPort _portNumber_ |  The socket port used to connect to an application instance. Unlike previous versions of WebObjects, this option is independent of the adaptor option. A _portNumber_ of -1 means use an arbitrary high port number; however, you cannot specify -1 as the value on the command line; to set the value to -1, you must use the defaults command. |
|  -q _listenQueueSize_ |  -WOListenQueueSize _listenQueueSize_ |  The depth of the listen queue. The default has changed from 4 to 5. |
|  None |  -WOWorkerThreadCount _int_ |  Maximum number of worker threads for a multithreaded application. The default worker thread count is 8. Setting this count to 0 results in single-threaded (WebObjects 3.5-style) request dispatch. |
|  None |  -WOOtherAdaptors _plist_ |  Use this option to attach additional adaptors (other than the one specified by -WOAdaptor) to the application. The _plist_ option is an array of dictionaries written in property list format. |
|  None |  -WOCGIAdaptorURL  _path_ |  The absolute URL that points to the WebObjects CGI adaptor. |
|  None |  -WOApplicationBaseURL |  The path from the web server's document root to the directory where your application (or project, if in rapid turnaround mode) resides. The default is "/WebObjects", but you may place your application anywhere under the document root. See [Rapid Turnaround Mode](Rapid%20Turnaround%20Mode.md#apple-gm3dcnbq) for more a complete discussion of this option. |
|  None |  -WOFrameworksBaseURL |  The location of frameworks under your document root if you're using a web server. The default is /WebObjects/Frameworks (as it was in release 3.5). All frameworks that your application uses must be in this directory. |
|  None |  -NSProjectSearchPath _pList_ |  An array of paths in which your project directories are located. (The array is written in property list format.) The default is a single item: ".."  If you specify this option, WebObjects looks in the locations you specify for a project that has the same name as the application or framework being loaded. If it finds a project, it uses the images, scripted components, and other resources from the project directory instead of from the application or framework's main bundle. This way, you can modify images and scripted components in your project and test them without having to rebuild the application. |
|  None |  -WOIncludeComments InResponses YES|NO |  Sets whether the HTML parser includes comments from the components' HTML files in the responses. The default is YES. See [Troubleshooting WebObjects 4.0 Template Parsing](NewInWO4.04.md#apple-giytanbx) for more information. |
|  None |  -WOSessionTimeOut _timeout_ |  Sets the timeout interval for sessions. By default, they now time out after 3600 seconds (in prior releases of WebObjects, sessions never timed out by default). |

```
```


As with all user defaults, you can set them three ways: on the application's command line, using the __defaults__ utility, or programmatically.
Be careful when setting options programmatically. Most options require knowledge of the environment in which the application runs, and the appropriate values change if you move the application to a different machine. For example, you should never set the __WOPort__ option programmatically.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.010.md)
