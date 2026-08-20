---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOApplication.html
archived_at: '2026-07-18T01:28:50.854825Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOAdaptor.md)
[!](WOAssociation.md)

---

# WOApplication

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

The primary role of the WOApplication class is to coordinate the handling of HTTP requests. Each application must have exactly one WOApplication object (or, simply, application object). The application object receives client requests from an HTTP server adaptor, manages the processing that generates a response, and returns that response-typically an object representing a web page-to the adaptor. The adaptor, in turn, forwards the response in a suitable form to the HTTP server that originated the request.

In handling requests, an application object creates and manages one or more sessions; a session (represented by a WOSession object) dedicates resources to a period of access by a single user and stores persistent state during that period. Conceptually, each cycle of the request-response loop (or transaction) takes place within a session.

Besides acting as a facilitator between the adaptor and the rest of the application during request handling, WOApplication performs many secondary functions. It returns pages based on component name, caches page instances and component definitions, provides some facilities for error handling and script debugging, coordinates the different levels of multi-threaded execution, and furnishes a variety of data.

Typical deployment schemes balance the processing load by having multiple application instances per server adaptor. A single application, in turn, can interact with multiple adaptors; for example, an application can simultaneously communicate with secure-socket and Distributed Object adaptors as well as HTTP adaptors.

You can instantiate ready-made application objects from the WOApplication class or you can obtain the application object from a custom subclass of WOApplication. Custom WOApplication subclasses are common in WebObjects applications since there is often a need to override the [`awake`](#apple-g43tany), [`sleep`](#apple-haytioi), and request-handling methods. Compiled WOApplication subclasses can take any name, but if the name is anything other than "Application" you must implement your own `main` function to instantiate the application object from this class. However, if the class name is "Application," you don't need to modify `main`. In scripted applications, the code in the `Application.wos` file becomes the implementation logic of a WOApplication subclass automatically created at run time; the application object is instantiated from this subclass.

---

## Method Types

**Constructors**

**[WOApplication](#apple-geytembxge)**

**Obtaining attributes**

**[adaptorsDispatchRequestsConcurrently](#apple-g43dqni)

**[allowsConcurrentRequestHandling](#apple-g43dsmq)

**[isConcurrentRequestHandlingEnabled](#apple-haztoma)

**[baseURL](#apple-g43tcni)

**[name](#apple-g44dsoi)

**[number](#apple-g44tanq)

**[path](#apple-g44tgni)**************

**Locking**

**[lock](#apple-g44dkni)

**[unlock](#apple-hazdimq)

**[lockRequestHandling](#apple-g44dmmq)

**[unlockRequestHandling](#apple-hazdioi)********

**Managing adaptors**

**[adaptorWithName](#apple-g43doma)

**[adaptors](#apple-g43dony)****

**Managing sessions**

**[setSessionStore](#apple-haytenq)

**[sessionStore](#apple-haydmnq)

**[saveSessionForContext](#apple-haydina)

**[restoreSessionWithID](#apple-haydema)

**[createSessionForRequest](#apple-g43temy)**********

**Managing pages**

**[setPageCacheSize](#apple-gy2tgnby)

**[pageCacheSize](#apple-g44tcna)

**[permanentPageCacheSize](#apple-ge3tinjw)

**[setPermanentPageCacheSize](#apple-ge3tkmjx)

**[setPageRefreshOnBacktrackEnabled](#apple-haytamq)

**[isPageRefreshOnBacktrackEnabled](#apple-g44dgmq)

**[pageWithName](#apple-g44temi)

**[pageWithName](#apple-g44teoa)****************

**Creating elements**

**[dynamicElementWithName](#apple-g43tkmq)**

**Running**

**[runLoop](#apple-ge3tcobw)

**[run](#apple-haydeoa)

**[setTimeOut](#apple-haytimq)

**[timeOut](#apple-haytsni)

**[terminate](#apple-haytooi)

**[isTerminating](#apple-g44dioa)************

**Handling requests**

**[dispatchRequest](#apple-g43tini)

**[awake](#apple-g43tany)

**[takeValuesFromRequest](#apple-haytomi)

**[invokeActionForRequest](#apple-ge4dsnry)

**[appendToResponse](#apple-g43tama)

**[sleep](#apple-haytioi)************

**Handling errors**

**[handleSessionCreationErrorInContext](#apple-g43tqma)

**[handlePageRestorationErrorInContext](#apple-g43tomy)

**[handleSessionRestorationErrorInContext](#apple-g43tqny)

**[handleException](#apple-g43tkoi)********

**Backward compatibility**

**[requiresWOF35RequestHandling](#apple-g44tsny)

**[requiresWOF35TemplateParser](#apple-haydana)****

**Scripted class support**

**[scriptedClassNameWithPath](#apple-haydkmi)

**[scriptedClassNameWithPathEncoding](#apple-haydkoa)****

**Script debugging**

**[logString](#apple-geytemjzgm)

**[debugString](#apple-g43tgma)

**[trace](#apple-hazdamy)

**[traceAssignments](#apple-hazdcmi)

**[traceObjectiveCMessages](#apple-hazdcoi)

**[traceScriptedMessages](#apple-hazdeny)

**[traceStatements](#apple-hazdgni)

**[logTakeValueForDeclarationNamed](#apple-ge3dcoju)

**[logSetValueForDeclarationNamed](#apple-ge3deojs)******************

**Statistics report**

**[setStatisticsStore](#apple-haytgna)

**[statisticsStore](#apple-haytmna)

**[statistics](#apple-haytknq)******

**Monitor support**

**[monitoringEnabled](#apple-g44dsmi)

**[activeSessionsCount](#apple-g43dmmq)

**[refuseNewSessions:](#apple-hazdenrq)

**[isRefusingNewSessions](#apple-g44dima)

**[setMinimumActiveSessionsCount](#apple-haydqoa)

**[minimumActiveSessionsCount](#apple-g44dqna)

**[terminateAfterTimeInterval](#apple-haytqny)

**[logToMonitorString](#apple-ge3danbt)****************

**Resource manager support**

**[setResourceManager](#apple-haytcoa)

**[resourceManager](#apple-haydcmq)****

**Request handling**

**[defaultRequestHandler](#apple-haytooi)

**[setDefaultRequestHandler](#apple-haydqma)

**[registerRequestHandler](#apple-g44tkoa)

**[removeRequestHandlerForKey](#apple-geztamrv)

**[registeredRequestHandlerKeys](#apple-g44tmni)

**[requestHandlerForKey:](#apple-g44tsma)

**[handlerForRequest](#apple-g43tsna)**************

**User defaults**

**[loadFrameworks](#apple-gezdmmrq)

**[setLoadFrameworks](#apple-g43dcoi)

**[isDebuggingEnabled](#apple-ge3dsnby)

**[setDebuggingEnabled](#apple-ge2tmnrz)

**[autoOpenInBrowser](#apple-g42dimq)

**[setAutoOpenInBrowser](#apple-geydi)

**[isDirectConnectEnabled](#apple-gezdkoju)

**[setDirectConnectEnabled](#apple-gq3dknjq)

**[cgiAdaptorURL](#apple-g42dioi)

**[setCGIAdaptorURL](#apple-ha3tgoa)

**[isCachingEnabled](#apple-g42dqna)

**[setCachingEnabled](#apple-g42toma)

**[applicationBaseURL](#apple-g42deoa)

**[setApplicationBaseURL](#apple-g42tiny)

**[frameworksBaseURL](#apple-g42doma)

**[setFrameworksBaseURL](#apple-g42tsoa)

**[recordingPath](#apple-gezdmobq)

**[setRecordingPath](#apple-gezdonrs)

**[projectSearchPath](#apple-gezdmnjw)

**[setProjectSearchPath](#apple-gezdonzr)

**[isMonitorEnabled](#apple-g42dsoa)

**[setMonitorEnabled](#apple-gezdomru)

**[monitorHost](#apple-g42tcmq)

**[setMonitorHost](#apple-g43denq)

**[SMTPHost](#apple-geztknjx)

**[setSMTPHost](#apple-gezdqmbq)

**[adaptor](#apple-ge3a)

**[setAdaptor](#apple-geytemrug4)

**[port](#apple-g42tcoi)

**[setPort](#apple-g43dgmy)

**[listenQueueSize](#apple-ge3dombw)

**[setListenQueueSize](#apple-g43dcmq)

**[workerThreadCount](#apple-g43dkna)

**[setWorkerThreadCount](#apple-g43diny)

**[additionalAdaptors](#apple-g42dcna)

**[setAdditionalAdaptors](#apple-g42tima)

**[includeCommentsInResponses](#apple-g42dony)

**[setIncludeCommentsInResponses:](#apple-g43dani)

**[componentRequestHandlerKey](#apple-g42dknq)

**[setComponentRequestHandlerKey](#apple-g42tony)

**[directActionRequestHandlerKey](#apple-g42dmmy)

**[setDirectActionRequestHandlerKey](#apple-g42tsmi)

**[resourceRequestHandlerKey](#apple-g42tenq)

**[setResourceRequestHandlerKey](#apple-g43dima)

**[sessionTimeout](#apple-ge3tgnru)

**[setSessionTimeOut](#apple-ge3timjv)********************************************************************************************

---

## Constructors

---

### WOApplication

public `WOApplication`()

Creates and initializes application attributes and initializes the adaptor or adaptors specified on the command line. If no adaptor is specified, WODefaultAdaptor is made the default adaptor. Some of the more interesting attribute initializations are:

- Session store is in the server.
- Page cache size is 30 pages.
- Client caching of pages is enabled ([`isPageRefreshOnBacktrackEnabled`](#apple-g44dgmq) returns false).

A exception is thrown if initialization does not succeed.

__Note:__
The global variable "WOApp" is initialized in this method.

#

---

### adaptor

public static java.lang.String `adaptor`()

Returns the class name of the primary adaptor. This is the cover method for the user default WOAdaptor.

__See also:__
[`setAdaptor`](#apple-geytemrug4)

---

### additionalAdaptors

public static NSArray `additionalAdaptors`()

Returns an array of adaptor description dictionaries. This is the cover method for the user default WOAdditionalAdaptors.

__See also:__
[`setAdditionalAdaptors`](#apple-g42tima)

---

### application

public static WOApplication `application`()

Returns a WOApplication object.You may call this method, but do not override it.

---

### applicationBaseURL

public static java.lang.String `applicationBaseURL`()

Returns a path to where the current application may be found under the document root (either the project or the `.woa` wrapper). This is the cover method for the user default WOApplicationBaseURL.

__See also:__
[`setApplicationBaseURL`](#apple-g42tiny)

---

### autoOpenInBrowser

public static boolean `autoOpenInBrowser`()

Returns whether automatic browser launching is enabled. By default, automatic browser launching is enabled.

---

### cgiAdaptorURL

public static java.lang.String `cgiAdaptorURL`()

Returns the URL for the web server including the path to the WebObjects CGI adaptor (for example, `http://localhost/cgi-bin/WebObjects`). This URL is used by the direct connect feature only. This is the cover for the user default WOCGIAdaptorURL.

__See also:__
[`setCGIAdaptorURL`](#apple-ha3tgoa)

---

### componentRequestHandlerKey

public static java.lang.String `componentRequestHandlerKey`()

Returns the key which identifies URLs directed at component-action-based requests. By default, this method returns the string "wo".

---

### directActionRequestHandlerKey

public static java.lang.String `directActionRequestHandlerKey`()

Returns the key which identifies URLs directed at component-based requests. By default, this method returns the string "wa".

---

### frameworksBaseURL

public static java.lang.String `frameworksBaseURL`()

Returns a path to where all frameworks may be found under the document root. This value is used to determine URLs that should be generated to reference Web Server Resources in those frameworks. This is the cover method for the user default WOFrameworksBaseURL.

__See also:__
[`setFrameworksBaseURL`](#apple-g42tsoa)

---

### includeCommentsInResponses

public static boolean `includeCommentsInResponses`()

Returns whether or not HTML comments are appended to the response. This is the cover method for the user default WOIncludeCommentsInResponses.

__See also:__
[`setIncludeCommentsInResponses:`](#apple-g43dani)

---

### isCachingEnabled

public static boolean `isCachingEnabled`()

Returns whether or not component caching is enabled. If this is enabled, changes to a component will be reparsed after being saved (assuming the project is under the NSProjectSearchPath). Note that this has no effect on page caching. This is the cover method for the user default WOCachingEnabled.

__See also:__
[`setCachingEnabled`](#apple-g42toma), [`pageCacheSize`](#apple-g44tcna)

---

### isDebuggingEnabled

public static boolean `isDebuggingEnabled`()

Returns whether or not debugging is enabled. If true, [`debugString`](#apple-g43tgma) prints out. Most startup-time status message are supressed if this method returns false. By default, debugging is enabled. This is the cover method for the user default WODebuggingEnabled.

__See also:__
[`setDebuggingEnabled`](#apple-ge2tmnrz), [`debugString`](#apple-g43tgma)

---

### isDirectConnectEnabled

public static boolean `isDirectConnectEnabled`()

Returns whether or not direct connect is enabled. By default it is enabled. For more information, see [`setDirectConnectEnabled`](#apple-gq3dknjq).

__See also:__
[`cgiAdaptorURL`](#apple-g42dioi)

---

### isMonitorEnabled

public static boolean `isMonitorEnabled`()

Returns whether or not the application can communicate with a Monitor application. It returns true if the application can contact Monitor upon startup and subsequently let Monitor gather statistics. It returns false if no comunication with Monitor can take place. By default, it can communicate with a Monitor application. 'This is a cover method for the user default WOMonitorEnabled.

__See also:__
[`setMonitorEnabled`](#apple-gezdomru), [`monitorHost`](#apple-g42tcmq), [`setMonitorHost`](#apple-g43denq)

---

### listenQueueSize

public static java.lang.Number `listenQueueSize`()

Returns the size of the listen queue which will created by the primary adaptor (usually WODefaultAdaptor). This is the cover method for the user default WOListenQueueSize.

__See also:__
[`setListenQueueSize`](#apple-g43dcmq)

---

### loadFrameworks

public static NSArray `loadFrameworks`()

Returns the array of frameworks to be loaded during application initialization.

__See also:__
[`setLoadFrameworks`](#apple-g43dcoi)

---

### logString

public static void `logString`(java.lang.String _aString_)

Prints a message to the standard error device (stderr). The message can include formatted variable data using String's concatenation feature, for example:

> ```
> int i = 500;
> ```

> ```
> float f = 2.045;
> ```

> ```
> WOApplication.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

__See also:__
[`logToMonitorString`](#apple-ge3danbt)

---

### monitorHost

public static java.lang.String `monitorHost`()

Returns the host on which Monitor is assumed to be running. This value is used during initialization if [`isMonitorEnabled`](#apple-g42dsoa) returns true. This is a cover for the user default WOMonitorHost.

__See also:__
[`setMonitorHost`](#apple-g43denq), [`isMonitorEnabled`](#apple-g42dsoa)

---

### port

public static java.lang.Number `port`()

Returns the port number on which the primary adaptor will listen (usually WODefaultAdaptor). This is the cover method for the user default WOPort.

__See also:__
[`setPort`](#apple-g43dgmy)

---

### projectSearchPath

public static NSArray `projectSearchPath`()

Returns an array of file system paths which are searched for projects for rapid turnaround mode. This is the cover method for the user default NSProjectSearchPath.

__See also:__
[`setProjectSearchPath`](#apple-gezdonzr)

---

### recordingPath

public static java.lang.String `recordingPath`()

Returns a file system path which is where the recording information should be saved. By default, this method returns nil.

If this method returns a path, all requests and responses are recorded in the HTTP format in numbered files (`0000-request`, `0000-response`, `0001-request`, `0001-response`, and so on), and saved under the recording path specified. This directory is then used by the Playback tool to test the application. You will most likely set this as a command line argument (`-WORecordingPath pathname`), exercise your application to record a scenario you would like to test, and then stop the application. Afterward you can restart the application without the WORecordingPath argument, and point Playback to the recording directory just created to replay your sequence of requests and compare the responses received with the ones recorded.

__See also:__
[`setRecordingPath`](#apple-gezdonrs)

---

### resourceRequestHandlerKey

public static java.lang.String `resourceRequestHandlerKey`()

Returns the key which identifies URLs directed through the resource request handler. Resource requests are only used during development of an application when the application is being run without an HTTP server.

__See also:__
[`setResourceRequestHandlerKey`](#apple-g43dima)

---

### sessionTimeout

public static java.lang.Number `sessionTimeOut`()

Returns the number (of seconds) which will be used as the default timeout for each newly created session. You may either override this method, change the user default WOSessionTimeOut, or set the session timeout in your session's `init` method.

__See also:__
[`setSessionTimeOut`](#apple-ge3timjv)

---

### setAdaptor

public static void `setAdaptor`(java.lang.String _anAdaptorName_)

Sets the the class name of the primary adaptor to _anAdaptorName_.

__See also:__
[`adaptor`](#apple-ge3a)

---

### setAdditionalAdaptors

public static void `setAdditionalAdaptors`(NSArray _anAdaptorPlist_)

Sets the array of adaptor description dictionaries to _anAdaptorPlist_. Each adaptor description dictionary must have "WOAdaptor" defined, which is the name of the adaptor class. Other attributes such as WOPort may also be specified, but are adaptor specific. For example WOWorkerThreadCount is specific to the WODefaultAdaptor class and may not apply for all adaptors.

__See also:__
[`additionalAdaptors`](#apple-g42dcna)

---

### setApplicationBaseURL

public static void `setApplicationBaseURL`(java.lang.String _aBaseURL_)

Sets to _aBaseURL_ the path to which the current application may be found under the document root (either the project or the `.woa` wrapper).

__See also:__
[`applicationBaseURL`](#apple-g42deoa)

---

### setAutoOpenInBrowser

public static void `setAutoOpenInBrowser`(boolean _isEnabled_)

Controls whether starting up this application also launches a web browser. If _isEnabled_ is `true`, the application launches the web browser. If `false`, the application does not launch the browser. Browser launching is enabled by default as long as there is a WOAdaptorURL key in the file `NeXT_ROOT/NextLibrary/WOAdaptors/Configuration/WebServerConfig.plist`.

To disable web browser launching, you must send this message in your subclass's constructor.

__See also:__
[`autoOpenInBrowser`](#apple-g42dimq)

---

### setCGIAdaptorURL

public static void `setCGIAdaptorURL`(java.lang.String _aURL_)

Sets the URL for the web server to _aURL_. The URL must include the path to the WebObjects CGI adaptor (for example, `http://localhost/cgi-bin/WebObjects`). This URL is used by the direct connect feature only..

__See also:__
[`cgiAdaptorURL`](#apple-g42dioi)

---

### setCachingEnabled

public static void `setCachingEnabled`(boolean _flag_)

Sets whether or not component caching is enabled. If this is enabled, changes to a component will be reparsed after being saved (assuming the project is under the NSProjectSearchPath). Note that this has no effect on page caching.

__See also:__
[`isCachingEnabled`](#apple-g42dqna), [`pageCacheSize`](#apple-g44tcna)

---

### setComponentRequestHandlerKey

public static void `setComponentRequestHandlerKey`(java.lang.String _key_)

Sets the component request handler key. This affects all URLs generated during [`appendToResponse`](#apple-g43tama): of component-based actions.

__See also:__
[`componentRequestHandlerKey`](#apple-g42dknq)

---

### setDebuggingEnabled

public static void `setDebuggingEnabled`(boolean _flag_)

Sets whether or not debugging is enabled. If true, [`debugString`](#apple-g43tgma) prints out. Most startup-time status message are supressed if this method returns false. By default, debugging is enabled.

__See also:__
[`isDebuggingEnabled`](#apple-ge3dsnby), [`debugString`](#apple-g43tgma)

---

### setDirectActionRequestHandlerKey

public static void `setDirectActionRequestHandlerKey`(java.lang.String _key_)

Sets the Direct Action request handler key. This affects all URLs generated during [`appendToResponse`](#apple-g43tama): of direct actions.

__See also:__
[`directActionRequestHandlerKey`](#apple-g42dmmy)

---

### setDirectConnectEnabled

public static void `setDirectConnectEnabled`(boolean _flag_)

Sets whether or not direct connect is enabled. By default it is enabled.

Direct connect actually transforms your application in a simple web server of its own. In particular, it is then able to find and return its images and resources as if it were a web server. It is very useful in development mode: You don't need a web server. Just point your URL to the port where your application is listening, and the application will handle all urls.

If this flag is true, the following happens:

- When using [`autoOpenInBrowser`](#apple-g42dimq), a direct connect URL will be used.
- When using [WOMailDelivery](WOMailDelivery.md) to mail pages with dynamic links in them, these links will be generated with a complete direct connect URL format. People receiving these mails will be able to access the application with direct connect.
- _All files on the system are accessible through the resource request handler._ On the other hand, if this flag is false, the resource request handler can be used to retrieve data objects from memory only, and no more reading in the file system is permitted (secure mode for deployment).

__See also:__
[`isDirectConnectEnabled`](#apple-gezdkoju), [`cgiAdaptorURL`](#apple-g42dioi)

---

### setFrameworksBaseURL

public static void `setFrameworksBaseURL`(java.lang.String _aString_)

Sets to _aString_ the path to where all frameworks may be found under the document root. This value is used to determine URLs that should be generated to reference Web Server Resources in those frameworks.

__See also:__
[`frameworksBaseURL`](#apple-g42doma)

---

### setIncludeCommentsInResponses:

public static void `setIncludeCommentsInResponses`(boolean _flag_)

Sets whether or not HTML comments are appended to the response.

__See also:__
[`includeCommentsInResponses`](#apple-g42dony)

---

### setListenQueueSize

public static void `setListenQueueSize`(java.lang.Number _aListenQueueSize_)

Sets the size of the listen queue which will created by the primary adaptor (usually WODefaultAdaptor).

__See also:__
[`listenQueueSize`](#apple-ge3dombw)

---

### setLoadFrameworks

public static void `setLoadFrameworks`(NSArray _frameworkList_)

Sets the array of frameworks to be loaded during application initialization.

__See also:__
[`loadFrameworks`](#apple-gezdmmrq)

---

### setMonitorEnabled

public static void `setMonitorEnabled`(boolean _flag_)

Sets whether or not the application will communicate with a Monitor application. If _flag_ is true, the application can contact Monitor upon startup and subsequently let Monitor gather statistics. If _flag_ is false, no comunication with Monitor can take place. By default, it can communicate with a Monitor application.

__See also:__
[`isMonitorEnabled`](#apple-g42dsoa)

---

### setMonitorHost

public static void `setMonitorHost`(java.lang.String _hostName_)

Sets the host on which Monitor is assumed to be running. This value is used during initialization if [`isMonitorEnabled`](#apple-g42dsoa) returns true.

__See also:__
[`monitorHost`](#apple-g42tcmq), [`isMonitorEnabled`](#apple-g42dsoa)

---

### setPort

public static void `setPort`(java.lang.Number _port_)

Sets the port number on which the primary adaptor will listen (usually WODefaultAdaptor).

__See also:__
[`port`](#apple-g42tcoi)

---

### setProjectSearchPath

public static void `setProjectSearchPath`(NSArray _searchPath_)

Sets the array of file system paths which are searched for projects for rapid turnaround mode.

__See also:__
[`projectSearchPath`](#apple-gezdmnjw)

---

### setRecordingPath

public static void `setRecordingPath`(java.lang.String _path_)

Sets the file system path where the recording information should be saved. Use nil as the path if you don't want to save recording information. By default, recording information is not saved.

If you save recording information, all requests and responses are recorded in the HTTP format in numbered files (`0000-request`, `0000-response`, `0001-request`, `0001-response`, and so on), and saved under the recording path specified. This directory is then used by the Playback tool to test the application. You will most likely set this as a command line argument (`-WORecordingPath pathname`), exercise your application to record a scenario you would like to test, and then stop the application. Afterward you can restart the application without the WORecordingPath argument, and point Playback to the recording directory just created to replay your sequence of requests and compare the responses received with the ones recorded.

__See also:__
[`recordingPath`](#apple-gezdmobq)

---

### setResourceRequestHandlerKey

public static void `setResourceRequestHandlerKey`(java.lang.String _key_)

Sets the resource request handler key. This affects all URLs generated during [`appendToResponse`](#apple-g43tama): of resources.

__See also:__
[`resourceRequestHandlerKey`](#apple-g42tenq)

---

### setSessionTimeOut

public void `setSessionTImeOut`(java.lang.Number _aTimeOut_)

Accessor to set the default session timeOut.

__See also:__
[`sessionTimeout`](#apple-ge3tgnru)

---

### setSMTPHost

public static void `setSMTPHost`(java.lang.String _hostName_)

Sets the name of the host that will be used to send e-mail messages created by [WOMailDelivery](WOMailDelivery.md).

__See also:__
[`SMTPHost`](#apple-geztknjx)

---

### setWorkerThreadCount

public static void `setWorkerThreadCount`(java.lang.Number _aWorkerThreadCount_)

SEts the count of worker threads which will created by the primary adaptor (usually WODefaultAdaptor). A worker thread count of 0 implies single-threaded mode.

__See also:__
[`workerThreadCount`](#apple-g43dkna)

---

### SMTPHost

public static java.lang.String `SMTPHost`()

Returns the name of the host that will be used to send e-mail messages created by [WOMailDelivery](WOMailDelivery.md). This is the cover method for the user default WOSMTPHost.

__See also:__
[`setSMTPHost`](#apple-gezdqmbq)

---

### workerThreadCount

public static java.lang.Number `workerThreadCount`()

Returns the count of worker threads which will created by the primary adaptor (usually WODefaultAdaptor). A worker thread count of 0 implies single-threaded mode. This is the cover method for the user default WOWorkerThreadCount.

__See also:__
[`setWorkerThreadCount`](#apple-g43diny)

---

## Instance Methods

---

### activeSessionsCount

public int `activeSessionsCount`()

Returns the number of sessions that are currently active. (A session is active if it has not yet timed out.)

The number returned here is only accurate if the application stores state in memory in the server, which is the default. If you use a custom state-storage strategy, there may be no way to tell how many sessions are active for a given application instance.

__See also:__
[`minimumActiveSessionsCount`](#apple-g44dqna), [`setMinimumActiveSessionsCount`](#apple-haydqoa)

---

### adaptorWithName

public WOAdaptor `adaptorWithName`(java.lang.String _aName_, NSDictionary _someArguments_)

Invoked during the constructor to create an adaptor. If you subclass WOAdaptor, you specify the WOAdaptor subclass you want the application to use with the `-a` option on the application's command line. When WOApplication encounters the `-a` option, it invokes this method. This method looks for a subclass of WOAdaptor with the name _aName_ (which was supplied as the `-a` option's argument), and if such a class exists, a new instance is created. The _someArguments_ array is populated with any adaptor-specific options (such as `-p` or `-q`) that follow the adaptor name on the command line. See the [WOAdaptor](WOAdaptor.md) class for more information.

__See also:__
[`adaptors`](#apple-g43dony)

---

### adaptors

public NSArray `adaptors`()

Returns the current list of application adaptors. A WOApplication can have multiple adaptors. (To associate the WOApplication with multiple adaptors, you specify each adaptor on the application's command line using the `-a` option.) This allows you to design an application that can not only listen to a socket for incoming HTTP requests (using the WODefaultAdaptor), but can also receive remote request messages using more advanced RPC mechanisms such as DO, CORBA, and DCOM.

---

### adaptorsDispatchRequestsConcurrently

public boolean `adaptorsDispatchRequestsConcurrently`()

Returns true if at least one adaptor contains multiple threads and will attempt to concurrently invoke the request handlers.

---

### allowsConcurrentRequestHandling

public boolean `allowsConcurrentRequestHandling`()

Override to return true if concurrent request handling is allowed.

---

### appendToResponse

public void `appendToResponse`(WOResponse _aResponse_, WOContext _aContext_)

The WOApplication object sends this message to itself to initiate the last phase of request handling. This occurs right after the `invokeActionForRequest:inContext:`: method has completed, typically with the return a response page. In the append-to-response phase, the application objects (particularly the response component itself) generate the HTML content of the page. WOApplication's default implementation of this method forwards the message to the session object.

__See also:__
[`invokeActionForRequest`](#apple-ge4dsnry)

---

### awake

public void `awake`()

Invoked at the beginning of each cycle of the request-response loop, affording the opportunity to perform initializations with application-wide scope. Since the default implementation does nothing, overridden implementations do not have to call `super`.

__See also:__
[`sleep`](#apple-haytioi)

---

### baseURL

public java.lang.String `baseURL`()

Returns the application URL relative to the server's document root, for example:

> ```
> WebObjects/Examples/HelloWorld.woa.
> ```

__See also:__
[`name`](#apple-g44dsoi), [`path`](#apple-g44tgni)

---

### createSessionForRequest

public WOSession `createSessionForRequest`(WORequest _aRequest_)

Creates and returns a WOSession object to manage a session for the application. The method goes through several steps to locate the class to use for instantiating this object:

- First it looks for a compiled class of name "Session" that is a subclass of WOSession.
- If such a class does not exist, it looks for a "`.wos`" script with the name of "Session" in the application wrapper ("`.woa`" directory).
- If the `Session.wos` script exists, the method parses the script and dynamically adds a scripted-class subclass of WOSession to the runtime.

The method then returns an allocated and initialized (using the default WOSession constructor) session instance of the selected class. It throws an exception if it is unable to create a new session.

__Note:__
An implication of the foregoing description is that the names of compiled WOSession subclasses
should be "Session"; if not, you will have to override this method to use the proper class to create the
session object.

__See also:__
[`restoreSessionWithID`](#apple-haydema), [`saveSessionForContext`](#apple-haydina)

---

### debugString

public void `debugString`(java.lang.String _aFormatString_)

Prints a message to the standard error device (stderr), if `WODebuggingEnabled` is true. The message can include formatted variable data using String's concatenation feature.

You control whether this method displays output with the `WODebuggingEnabled` user default option. If `WODebuggingEnabled` is true, then the `debugString` messages display their output. If `WODebuggingEnabled` is false, the `debugString` messages don\xd5 t display their output.

---

### defaultRequestHandler

public WORequestHandler `defaultRequestHandler`()

Returns the request handler to be used when no request handler key was found in the URL or WORequest. This method returns the WOComponent request handler by default. When an application is contacted for the first time it is usually via a URL like the following:

> ```
> http://somehost/cgi-bin/WebObjects/AppName.woa
> ```

The way that URLs of that type are handled is determined by the default request handler.

---

### dispatchRequest

public WOResponse `dispatchRequest`(WORequest _aRequest_)

The main entry point for any given interaction. Invoked by the adaptor.

---

### dynamicElementWithName

public WODynamicElement `dynamicElementWithName`(java.lang.String _aName_, NSDictionary _someAssociations_,
WOElement _anElement_NSArray _languages_)

Creates and returns a WODynamicElement object based on the element's name, a dictionary of associations, and a template of elements. This method is invoked automatically to provide a WODynamicElement object that represents a `WEBOBJECT` element in the HTML template. You don't ordinarily invoke `dynamicElementWithName:associations:template:languages:`, but you might override it to substitute your own WODynamicElement or reusable component for one of the built-in WODynamicElements.

The arguments _aName_ and _someAssociations_ are derived from a corresponding line in the declarations file. _aName_ is a String that identifies the kind of element to create. Generally _aName_ specifies a built-in WODynamicElement such as WOString, but it may also identify a reusable component. (For more information, see the chapter "Using Reusable Components" in the _WebObjects Developer's Guide_.) For example, in the `dynamicElementWithName:associations:template:languages:` message for the following declaration:

> ```
> APP_STRING: WOString {value = applicationString;};
> ```

_aName_ contains the string "WOString".

The _someAssociations_ dictionary contains an entry for each attribute specified in the corresponding declaration. For the declaration above, _someAssociations_ contains a single entry for WOString's value attribute. The keys of _someAssociations_ are the attribute names and the values are WOAssociation objects.

WOApplication's implementation of `dynamicElementWithName:associations:template:languages:` first searches for a WODynamicElement named _aName_. If a WODynamicElement is found, the method creates an instance and returns it. Otherwise, it searches for a component-either scripted or compiled-to return instead. If neither are found, this method returns `null`.

---

### handleException

public WOResponse `handleException`(java.lang.Throwable _anException_, WOContext _aContext_)

Invoked when an exception occurs within the request-response loop. The default behavior displays a page with debugging information. You can override this method to catch exceptions and display a "friendlier" error page.

__See also:__
[`handleSessionCreationErrorInContext`](#apple-g43tqma), [`handleSessionRestorationErrorInContext`](#apple-g43tqny)

---

### handlePageRestorationErrorInContext

public WOResponse `handlePageRestorationErrorInContext`(WOContext _aContext_)

Invoked when a page (WOComponent) instance cannot be restored, which typically happens when a user backtracks too far. Specifically, this method is invoked when the following occurs: the request is not the first of a session, page restoration by context ID fails, and page re-creation is disabled. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See also:__
[`handleException`](#apple-g43tkoi), [`handleSessionCreationErrorInContext`](#apple-g43tqma),
[`handleSessionRestorationErrorInContext`](#apple-g43tqny)

---

### handleSessionCreationErrorInContext

public WOResponse `handleSessionCreationErrorInContext`(WOContext _aContext_)

Invoked when a session (WOSession) instance cannot be created. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See also:__
[`handleException`](#apple-g43tkoi), [`handlePageRestorationErrorInContext`](#apple-g43tomy),
[`handleSessionRestorationErrorInContext`](#apple-g43tqny)

---

### handleSessionRestorationErrorInContext

public WOResponse `handleSessionRestorationErrorInContext`(WOContext _aContext_)

Invoked when a session (WOSession) instance cannot be restored, which typically happens when the session times out. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See also:__
[`handleException`](#apple-g43tkoi), [`handlePageRestorationErrorInContext`](#apple-g43tomy),
[`handleSessionCreationErrorInContext`](#apple-g43tqma)

---

### handlerForRequest

public WORequestHandler `handlerForRequest`(WORequest _aRequest_)

Returns the request handler used to handle a given request.

__See also:__
[`registerRequestHandler`](#apple-g44tkoa)_,_ [`registeredRequestHandlerKeys`](#apple-g44tmni)_,_ [`requestHandlerForKey:`](#apple-g44tsma)

---

### invokeActionForRequest

public WOElement `invokeAction`(WORequest _aRequest_, WOContext _aContext_)

The WOApplication object sends this message to itself to initiate the middle phase of request handling. In this phase, the message is propagated through the objects of the application until the dynamic element that has received the user action (for instance, a click on a button) responds to the message by triggering the method in the request component that is bound to the action. The default WOApplication implementation of this method forwards the message to the session object.

__See also:__
[`appendToResponse`](#apple-g43tama)

---

### isConcurrentRequestHandlingEnabled

public boolean `isConcurrentRequestHandlingEnabled`()

Returns whether component-definition caching is enabled. The default is `false`.

---

### isPageRefreshOnBacktrackEnabled

public boolean `isPageRefreshOnBacktrackEnabled`()

Returns whether caching of pages is disabled in the client. If so, the client does not restore request pages from its cache but re-creates them "from scratch" by resending the URL to the server. This flag is set to `false` by default.

__See also:__
[`setPageRefreshOnBacktrackEnabled`](#apple-haytamq)

---

### isRefusingNewSessions

public boolean `isRefusingNewSessions`()

Returns `true` if the application instance is refusing new sessions, and `false` otherwise. When the application instance refuses new sessions, the WebObjects adaptor tries to start the session in another instance of the same application. If no other instance is running and accepting new sessions, the user receives an error message.

---

### isTerminating

public boolean `isTerminating`()

Returns whether the application will terminate at the end of the current request-response loop.

__See also:__
[`setTimeOut`](#apple-haytimq), [`terminate`](#apple-haytooi), [`terminateAfterTimeInterval`](#apple-haytqny), [`timeOut`](#apple-haytsni)

---

### lock

public void `lock`()

Locks the application object.

---

### lockRequestHandling

public void `lockRequestHandling`()

Serializes request handler access if concurrent request handling isn't enabled.

---

### logSetValueForDeclarationNamed

public void `logSetValueForDeclarationNamed`(java.lang.String _aDeclarationName_, java.lang.String _aDeclarationType_, java.lang.String _aBindingName_, java.lang.String _anAssociationDescription_, java.lang.Object _aValue_)

Formats and logs a message anytime a value is set through a WOAssociation, when WODebug is set to true for the declaration in which the association appears. (Setting a value means the child component/element is setting a value in the parent). See [`logTakeValueForDeclarationNamed`](#apple-ge3dcoju) for a description of each of the arguments to this method.

---

### logTakeValueForDeclarationNamed

public void `logTakeValueForDeclarationNamed`(java.lang.String _aDeclarationName_, java.lang.String _aDeclarationType_, java.lang.String _aBindingName_, java.lang.String _anAssociationDescription_, java.lang.Object _aValue_)

Formats and logs a message anytime a value is "taken" through a WOAssociation , when WODebug is set to true for the declaration in which the association appears. (Taking a value means the child component/element is taking a value from the parent). Override this method to alter the format of the log message. The arguments of this method are defined in the following example of a WebObjects declaration.

> ```
> aDeclarationName : aDeclarationType {
> ```

> ```
> aBindingName = anAssociationDescription;
> ```

> ```
> }
> ```

Also, _aValue_ is the value which is being pushed to or pulled from the child to the parent.

---

### logToMonitorString

public void `logToMonitorString`(java.lang.String _aFormat_)

Same as [`logString`](#apple-geytemjzgm) but prints the string to the Monitor application's standard error. That is, the message is displayed in the command-shell window that was used to launch the Monitor application.

You use this method to log messages about significant events when the application is ready to be deployed and you will use Monitor regularly to monitor the application. Otherwise, use [`logString`](#apple-geytemjzgm). If the Monitor application is not running or if this application instance is not being monitored, this method does nothing.

---

### minimumActiveSessionsCount

public int `minimumActiveSessionsCount`()

Returns the minimum number of active sessions allowed. If the number of active sessions is less than or equal to this number and [`isRefusingNewSessions`](#apple-g44dima) is `true`, the application instance terminates. The default is 0.

__See also:__
[`activeSessionsCount`](#apple-g43dmmq), [`refuseNewSessions:`](#apple-hazdenrq), [`setMinimumActiveSessionsCount`](#apple-haydqoa)

---

### monitoringEnabled

public boolean `monitoringEnabled`()

Returns `true` if the application is "monitorable" by the Monitor application, and `false` otherwise. An application is "monitorable" if it was able to find a running Monitor upon startup and it is able to successfully communicate with that Monitor.

By default, all applications are monitorable if the Monitor application is running on the same machine as the application. You can specifically disable monitoring using the `-WOMonitorEnabled NO` option on the application command line. If you want the application to be monitorable and the Monitor is running on another host, you can start up the application through Monitor, or you can specify Monitor's host on the application command line this way:

> ```
> MyApp.exe -WOMonitorEnabled YES -WOMonitorHost monitorHost ...
> ```

__See also:__
[`logToMonitorString`](#apple-ge3danbt), the online document _ServingWebObjects_

---

### name

public java.lang.String `name`()

Returns the name of the application, which is the name of the executable (without the `.exe` extension).

__See also:__
[`baseURL`](#apple-g43tcni), [`path`](#apple-g44tgni)

---

### number

public java.lang.String `number`()

Returns `"-1"`. This is provided for backwards compatibility only.

---

### pageCacheSize

public int `pageCacheSize`()

Returns the size of the internal cache for page instances. The default size is 30 instances.

__See also:__
: [`setPageCacheSize`](#apple-gy2tgnby)

---

### pageWithName

public WOComponent `pageWithName`(java.lang.String _aName_, WORequest _aRequest_)

Returns a new page instance (a WOComponent object) identified by _aName_. If _aName_ is `null`, the "Main" component is assumed. If the method cannot create a valid page instance, it throws an exception.

As part of its implementation, this method creates a context with _aRequest_ and calls [`pageWithName`](#apple-g44teoa).

__See also:__
[`restorePageForContextID`](WOSession.md#apple-geyds) (WOSession), [`savePage`](WOSession.md#apple-geytg) (WOSession)

---

### pageWithName

public WOComponent `pageWithName`(java.lang.String _aName_, WOContext _aContext_)

Returns a new page instance (a WOComponent object) identified by _aName_. If _aName_ is `null`, the "Main" component is assumed. If the method cannot create a valid page instance, it throws an exception.

__See also:__
[`pageWithName`](#apple-g44temi), [`restorePageForContextID`](WOSession.md#apple-geyds) (WOSession), [`savePage`](WOSession.md#apple-geytg) (WOSession)

---

### path

public java.lang.String `path`()

Returns the filesystem path of the application, which is an absolute path and includes the "`.woa`" extension; for example "`C:/NETSCAPE/ns-home/docs/WebObjects/Examples/HelloWorld.woa`" is a typical application path.

__See also:__
[`baseURL`](#apple-g43tcni), [`name`](#apple-g44dsoi)

---

### permanentPageCacheSize

public int `permanentPageCacheSize`()

Returns the permanent page cache size. The default is 30. The permanent page cache holds pages which should not fall out of the regular page cache. For example, a control page in a frameset should exist for the duration of a session.

__See also:__
[`savePageInPermanentCache`](WOSession.md#apple-ge2tgnjx) (WOApplication)

---

### refuseNewSessions:

public void `refuseNewSessions`(boolean _flag_)

Controls whether this application instance will create a session when it receives an HTTP request from a new user. If _flag_ is `true`, the application does not create new sessions; when it receives a request from a new user, it refuses that request, and the adaptor must try to find another application instance that can process the request. If _flag_ is `false`, the application creates new sessions. `false` is the default.

You use this method with `setMinimumActiveSessionsCount:` to gracefully shut down application instances. Use `setMinimumActiveSessionsCount:` to set the active session minimum to a certain number. When number of active sessions reaches the number you set and `isRefusingNewSessions` returns `true`, the application terminates.

__See also:__
[`activeSessionsCount`](#apple-g43dmmq), [`isRefusingNewSessions`](#apple-g44dima), [`minimumActiveSessionsCount`](#apple-g44dqna),
[`setMinimumActiveSessionsCount`](#apple-haydqoa)

---

### registerRequestHandler

public void `registerRequestHandler`(WORequestHandler _aHandler_, java.lang.String _aKey_)

Registers a new request handler. _aKey_ must specify a key which can be found in the URLs following the instance number or application name.

__See also:__
[`removeRequestHandlerForKey`](#apple-geztamrv), [`registeredRequestHandlerKeys`](#apple-g44tmni), [`requestHandlerForKey:`](#apple-g44tsma)

---

### registeredRequestHandlerKeys

public NSArray `registeredRequestHandlerKeys`()

Returns an array of strings containing the keys of all of the registered request handlers.

__See also:__
[`handlerForRequest`](#apple-g43tsna), [`requestHandlerForKey:`](#apple-g44tsma)

---

### removeRequestHandlerForKey

public WORequestHandler `removeRequestHandlerForKey`(java.lang.String _aRequestHandlerKey_)

Removes the specified request handler from the application.

__See also:__
[`registerRequestHandler`](#apple-g44tkoa), [`requestHandlerForKey:`](#apple-g44tsma)

---

### requestHandlerForKey:

public WORequestHandler `requestHandlerForKey`(java.lang.String _key_)

Returns the request handler used to handle requests containing the specified key.

__See also:__
[`handlerForRequest`](#apple-g43tsna), [`registerRequestHandler`](#apple-g44tkoa), [`registeredRequestHandlerKeys`](#apple-g44tmni)

---

### requiresWOF35RequestHandling

public boolean `requiresWOF35RequestHandling`()

For backward compatibility, if your project depends upon features or side effects of the old request handling, you will want to override this method and return true. By default, it returns false.

---

### requiresWOF35TemplateParser

public boolean `requiresWOF35TemplateParser`()

For backward compatibility, if your project depends upon features or side effects removed from the new, 4.0 template parser, you will want to override this method and return true. By default, it returns false.

---

### resourceManager

public WOResourceManager `resourceManager`()

Returns the WOResourceManager object that the application uses to manage resources.

__See also:__
[`setResourceManager`](#apple-haytcoa)

---

### restoreSessionWithID

public void `restoreSessionWithID`(java.lang.String _aSessionID_, WOContext _aContext_)

Restores the WOSession object representing a session. In normal request handling, this method is invoked at the start of a cycle of the request-response loop. The default implementation simply invokes WOSessionStore's [`checkoutSessionWithID`](WOSessionStore.md#apple-gu3toni) method, but raises an exception if the WOSessionStore object is missing.

__See also:__
[`createSessionForRequest`](#apple-g43temy), [`saveSessionForContext`](#apple-haydina)

---

### run

public void `run`()

Runs the application in a near-indefinite run loop in the default run-loop mode. Before starting the run loop, the method sends [`registerForEvents`](WOAdaptor.md#apple-gu2daoa) to the application's adaptors so that they can begin receiving run-loop events. Normally, [`run`](#apple-haydeoa) is invoked in the main function.

__See also:__
[`setTimeOut`](#apple-haytimq), [`terminate`](#apple-haytooi), [`terminateAfterTimeInterval`](#apple-haytqny)

---

### runLoop

public NSRunLoop runLoop()

Returns the application's run loop. Use this method when you need a run loop for such things as registering timers.

---

### saveSessionForContext

public void `saveSessionForContext`(WOContext _aContext_)

Called at the end of the request handling loop, when the current session object needs to be saved. The default implementation simply invokes WOSessionStore's [`checkinSessionForContext`](WOSessionStore.md#apple-gm3tmna) method, but throws an exception if the WOSessionStore object is missing.

__See also:__
[`restoreSessionWithID`](#apple-haydema)

---

### scriptedClassNameWithPath

public java.lang.String `scriptedClassNameWithPath`(java.lang.String _aPath_)

Loads a Webscript-based class with the pathname _aPath_ into the application. The specified script is parsed assuming the default string encoding, and the class and categories found in the script file are dynamically added to the runtime.

---

### scriptedClassNameWithPathEncoding

public java.lang.String `scriptedClassNameWithPathEncoding`(java.lang.String _aPath_,
int _anEncoding_)

Loads a scripted class with the pathname _aPath_ using the encoding _anEncoding_. The class and categories found in the script file are dynamically added to the runtime. The script must use the `@interface/@implementation` syntax.

---

### sessionStore

public WOSessionStore `sessionStore`()

Returns the application's current WOSessionStore object (which, by default, stores state in the server).

__See also:__
[`setSessionStore`](#apple-haytenq)

---

### setDefaultRequestHandler

public void `setDefaultRequestHandler`(WORequestHandler _aHandler_)

> ```
> Sets the default request handler.
> ```

__See also:__
[`defaultRequestHandler`](#apple-haytooi)

---

### setMinimumActiveSessionsCount

public void `setMinimumActiveSessionsCount`(int _anInt_)

Sets the minimum number of active sessions to _anInt_. The default is 0.

You use this method to gracefully shut down application instances. If the active sessions count reaches this number and isRefusingNewSessions returns `true`, the application terminates. You might want to terminate application instances periodically for performance reasons; some applications leak a certain amount of memory per transaction, and shutting down and restarting instances of those applications can free up that memory.

__See also:__
[`activeSessionsCount`](#apple-g43dmmq), [`isRefusingNewSessions`](#apple-g44dima), [`minimumActiveSessionsCount`](#apple-g44dqna),
[`refuseNewSessions:`](#apple-hazdenrq)

---

### setPageCacheSize

public void `setPageCacheSize`(int _anInt_)

Sets whether caching of page instances will occur and the number of pages the cache will hold. When page-instance caching is enabled, the application stores the WOComponent instance corresponding to the response page in the session. When the page is backtracked to, it restores it from the session and makes it the request page. The state of the page is retained. By default, page-instance caching is enabled, with a cache limit of 30 pages.

You turn page-instance caching off by invoking this method with an argument of zero. In this case, when the user backtracks to a page, the page is not stored in the session and so must be re-created "from scratch."

__See also:__
[`pageCacheSize`](#apple-g44tcna)

---

### setPageRefreshOnBacktrackEnabled

public void `setPageRefreshOnBacktrackEnabled`(boolean _flag_)

When _flag_ is `true`, disables caching of pages by the client by setting the page's expiration-time header to the current date and time. (By default, this attribute is set to `false`.) Disabling of client caching affects what happens during backtracking. With client caching turned off, the browser resends the URL to the server for the page requested by backtracking. The application must return a new page to the browser (corresponding to a new WOComponent instance). This behavior is desirable when you do not want the user to backtrack to a page that might be obsolete because of changes that have occurred in the session.

When this flag is turned on and a request corresponding to a client backtrack occurs, the retrieved page will only be asked to regenerate its response. The first two phases of a normal request-response loop (value extraction from the request and action invocation) do not occur.

See Caching Strategies in the class description for further details.

__See also:__
[`isPageRefreshOnBacktrackEnabled`](#apple-g44dgmq)

---

### setPermanentPageCacheSize

public void `setPermanentPageCacheSize`(int _aSize_)

Sets the permanentPageCacheSize to aSize

__See also:__
[`permanentPageCacheSize`](#apple-ge3tinjw)

---

### setResourceManager

public void `setResourceManager`(WOResourceManager _aResourceManager_)

Sets the WOResourceManager object to _aResourceManager_. WOResourceManager objects search for and retrieve resources from the application directory and from shared framework directories.

__See also:__
[`resourceManager`](#apple-haydcmq)

---

### setSessionStore

public void `setSessionStore`(WOSessionStore _aSessionStore_)

Set the session-store object for the application. By default, an object that stores session state in process memory (that is, in the server) is used. The session-store object specifies the state storage strategy for the whole application. This object is responsible for making session objects persistent. You should set the session store object when the application starts up, before the first request is handled.

__See also:__
[`sessionStore`](#apple-haydmnq)

---

### setStatisticsStore

public void `setStatisticsStore`(WOStatisticsStore _aStatisticsStore_)

Sets the WOStatisticsStore object to _aStatisticsStore_. WOStatisticsStore objects record application statistics while the application runs.

__See also:__
[`statisticsStore`](#apple-haytmna)

---

### setTimeOut

public void `setTimeOut`(double _aTimeInterval_)

Sets the number of seconds the application can experience inactivity (no HTTP requests) before it terminates execution.

This method differs from [`terminateAfterTimeInterval`](#apple-haytqny) in that with this method, the application must be idle for _aTimeInterval_ seconds for the application to terminate.[`terminateAfterTimeInterval`](#apple-haytqny) terminates the application whether it is active or not.

__See also:__
[`timeOut`](#apple-haytsni)

---

### sleep

public void `sleep`()

Invoked at the conclusion of a request-handling cycle to give an application the opportunity for deallocating objects created and initialized in its awake method. The default implementation does nothing.

---

### statistics

public NSDictionary `statistics`()

Returns a copy of the dictionary containing the application statistics maintained by WOStatisticsStore. This method is used by the Monitor application to retrieve application statistics. If you need to access the statistics internally, use this message instead:

> ```
> WOApplication.application().statisticsStore().statistics()
> ```

---

### statisticsStore

public WOStatisticsStore `statisticsStore`()

Returns the WOStatisticsStore object, which records statistics while the application runs.

__See also:__
[`setStatisticsStore`](#apple-haytgna)

---

### takeValuesFromRequest

public void `takeValuesFromRequest`(WORequest _aRequest_, WOContext _aContext_)

The component action request handler sends this message to the WOApplication to start the first phase of request handling. In this phase, the message is propagated to the session and component objects involved in the request as well as the request page's dynamic elements. Each dynamic element acquires any entered data or changed state (such as a check in a check box) associated with an attribute and assigns the value to the variable bound to the attribute. The default WOApplication implementation of this method forwards the message to the session object.

__See also:__
[`appendToResponse`](#apple-g43tama), [`invokeActionForRequest`](#apple-ge4dsnry)

---

### terminate

public void `terminate`()

Terminates the application process. Termination does not take place until the handling of the current request has completed.

__See also:__
[`isTerminating`](#apple-g44dioa), [`setTimeOut`](#apple-haytimq)

---

### terminateAfterTimeInterval

public void `terminateAfterTimeInterval`(double _aTimeInterval_)

Sets the application to terminate itself after _aTimeInterval_ seconds has elapsed. After the specified time interval has elapsed, the application immediately stops all current processing. If any sessions are active, users may lose information.

This method differs from [`setTimeOut`](#apple-haytimq) in that it does not set idle time; `terminateAfterTimeInterval:`: shuts down the application regardless of whether it is idle.

---

### timeOut

public double `timeOut`()

Returns the application's time-out interval: a period (in seconds) of inactivity before the application terminates execution. The default application time-out interval is a very large number.

__See also:__
[`setTimeOut`](#apple-haytimq)

---

### trace

public void `trace`(boolean _flag_)

If _flag_ is `true`, prints all trace messages (messages for scripted messages, compiled messages, and all statements in the application) to the standard error device. If _flag_ is `false`, stops printing all trace messages.

__See also:__
[`traceAssignments`](#apple-hazdcmi), [`traceObjectiveCMessages`](#apple-hazdcoi):, [`traceScriptedMessages`](#apple-hazdeny), [`traceStatements`](#apple-hazdgni)

---

### traceAssignments

public void `traceAssignments`(boolean _flag_)

If _flag_ is `true`, prints a message to the standard error device every time an assignment statement is executed. If _flag_ is `false`, stops printing trace assignment messages.

__See also:__
[`trace`](#apple-hazdamy), [`traceObjectiveCMessages`](#apple-hazdcoi):, [`traceScriptedMessages`](#apple-hazdeny), [`traceStatements`](#apple-hazdgni)

---

### traceObjectiveCMessages

public void `traceObjectiveCMessages`(boolean _flag_)

If _flag_ is `true`, prints a message to the standard error device every time a message is sent to a compiled class from Webscript. If _flag_ is `false`, stops printing these messages.

__See also:__
[`trace`](#apple-hazdamy), [`traceAssignments`](#apple-hazdcmi), [`traceScriptedMessages`](#apple-hazdeny), [`traceStatements`](#apple-hazdgni)

---

### traceScriptedMessages

public void `traceScriptedMessages`(boolean _flag_)

If _flag_ is `true`, prints a message to the standard error device every time a message is sent to a scripted class from Webscript. If _flag_ is `false`, stops printing trace scripted method messages.

__See also:__
[`trace`](#apple-hazdamy), [`traceAssignments`](#apple-hazdcmi), [`traceObjectiveCMessages`](#apple-hazdcoi), [`traceStatements`](#apple-hazdgni)

---

### traceStatements

public void `traceStatements`(boolean _flag_)

If _flag_ is `true`, prints a message to the standard error device every time a statement in the application is executed from Webscript. If _flag_ is `false`, stops printing trace statement messages.

__See also:__
[`trace`](#apple-hazdamy), [`traceAssignments`](#apple-hazdcmi), [`traceObjectiveCMessages`](#apple-hazdcoi), [`traceScriptedMessages`](#apple-hazdeny)

---

### unlock

public void `unlock`()

Unlocks the application object.

---

### unlockRequestHandling

public void `unlockRequestHandling`()

Disables serialized request handler access if concurrent request handling isn't enabled.

---

# Notifications

---

### WOApplicationDidFinishLaunchingNotification

Posted just before the application begins waiting for requests. The notification contains the application instance.

---

### WOApplicationWillFinishLaunchingNotification

Posted when an application has finished its `init` method. Register to receive this notification if you have an object that wishes to set various setting in the application. For example, if you have a WORequestHandler implemented in a framework and you want to register it with the WOApplication, you would register to receive this notification and then implement a method that register your WORequestHandler with the application.

The notification contains the application instance.

---

[!](WOAdaptor.md)
[!](WOAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
