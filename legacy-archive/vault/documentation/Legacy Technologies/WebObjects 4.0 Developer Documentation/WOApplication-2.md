---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOApplication.html
archived_at: '2026-07-18T01:28:53.181054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOAdaptor-2.md)
[!](WOAssociation-2.md)

---

# WOApplication

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOApplication.h

---

## Class Description

The primary role of the WOApplication class is to coordinate the handling of HTTP requests. Each application must have exactly one WOApplication object (or, simply, application object). The application object receives client requests from an HTTP server adaptor, manages the processing that generates a response, and returns that response-typically an object representing a web page-to the adaptor. The adaptor, in turn, forwards the response in a suitable form to the HTTP server that originated the request.

In handling requests, an application object creates and manages one or more sessions; a session (represented by a WOSession object) dedicates resources to a period of access by a single user and stores persistent state during that period. Conceptually, each cycle of the request-response loop (or transaction) takes place within a session.

Besides acting as a facilitator between the adaptor and the rest of the application during request handling, WOApplication performs many secondary functions. It returns pages based on component name, caches page instances and component definitions, provides some facilities for error handling and script debugging, coordinates the different levels of multi-threaded execution, and furnishes a variety of data.

Typical deployment schemes balance the processing load by having multiple application instances per server adaptor. A single application, in turn, can interact with multiple adaptors; for example, an application can simultaneously communicate with secure-socket and Distributed Object adaptors as well as HTTP adaptors.

You can instantiate ready-made application objects from the WOApplication class or you can obtain the application object from a custom subclass of WOApplication. Custom WOApplication subclasses are common in WebObjects applications since there is often a need to override the [__awake__](#apple-g43tany), [__sleep__](#apple-haytioi), [__init__](#apple-geydsojygm), and request-handling methods. Compiled WOApplication subclasses can take any name, but if the name is anything other than "Application" you must implement your own __main__  function to instantiate the application object from this class. However, if the class name is "Application," you don't need to modify __main__ . In scripted applications, the code in the __Application.wos__  file becomes the implementation logic of a WOApplication subclass automatically created at run time; the application object is instantiated from this subclass.

---

# Adopted Protocols

**NSLocking**

**- lock

**- unlock****

---

## Method Types

**Creating**

**[- init](#apple-geydsojygm)

**[+ application](#apple-g42dema)****

**Obtaining attributes**

**[- adaptorsDispatchRequestsConcurrently](#apple-g43dqni)

**[- allowsConcurrentRequestHandling](#apple-g43dsmq)

**[- isConcurrentRequestHandlingEnabled](#apple-haztoma)

**[- baseURL](#apple-g43tcni)

**[- name](#apple-g44dsoi)

**[- number](#apple-g44tanq)

**[- path](#apple-g44tgni)**************

**Locking**

**[- lock](#apple-g44dkni)

**[- unlock](#apple-hazdimq)

**[- lockRequestHandling](#apple-g44dmmq)

**[- unlockRequestHandling](#apple-hazdioi)********

**Managing adaptors**

**[- adaptorWithName:arguments:](#apple-g43doma)

**[- adaptors](#apple-g43dony)****

**Managing cache**

**[- setCachingEnabled:](#apple-geytcmruge)

**[- isCachingEnabled](#apple-geytambtgu)****

**Managing sessions**

**[- setSessionStore:](#apple-haytenq)

**[- sessionStore](#apple-haydmnq)

**[- saveSessionForContext:](#apple-haydina)

**[- restoreSessionWithID:inContext:](#apple-haydema)

**[- createSessionForRequest:](#apple-g43temy)**********

**Managing pages**

**[- setPageCacheSize:](#apple-gy2tgnby)

**[- pageCacheSize](#apple-g44tcna)

**[- permanentPageCacheSize](#apple-ge3tinjw)

**[- setPermanentPageCacheSize:](#apple-ge3tkmjx)

**[- setPageRefreshOnBacktrackEnabled:](#apple-haytamq)

**[- isPageRefreshOnBacktrackEnabled](#apple-g44dgmq)

**[- pageWithName:forRequest:](#apple-g44temi)

**[- pageWithName:inContext:](#apple-g44teoa)****************

**Creating elements**

**[- dynamicElementWithName:associations:template:languages:](#apple-g43tkmq)**

**Running**

**[- runLoop](#apple-ge3tcobw)

**[- run](#apple-haydeoa)

**[- setTimeOut:](#apple-haytimq)

**[- timeOut](#apple-haytsni)

**[- terminate](#apple-haytooi)

**[- isTerminating](#apple-g44dioa)************

**Handling requests**

**[- dispatchRequest:](#apple-g43tini)

**[- awake](#apple-g43tany)

**[- takeValuesFromRequest:inContext:](#apple-haytomi)

**[- invokeActionForRequest:inContext:](#apple-ge4dsnry)

**[- appendToResponse:inContext:](#apple-g43tama)

**[- sleep](#apple-haytioi)************

**Handling errors**

**[- handleSessionCreationErrorInContext:](#apple-g43tqma)

**[- handlePageRestorationErrorInContext:](#apple-g43tomy)

**[- handleSessionRestorationErrorInContext:](#apple-g43tqny)

**[- handleException:inContext:](#apple-g43tkoi)********

**Backward compatibility**

**[- requiresWOF35RequestHandling](#apple-g44tsny)

**[- requiresWOF35TemplateParser](#apple-haydana)****

**Scripted class support**

**[- scriptedClassWithPath:](#apple-haydkmi)

**[- scriptedClassWithPath:encoding:](#apple-haydkoa)****

**Script debugging**

**[- logWithFormat:](#apple-geytanbrha)

**[- debugWithFormat:](#apple-g43tgma)

**[- trace:](#apple-hazdamy)

**[- traceAssignments:](#apple-hazdcmi)

**[- traceObjectiveCMessages:](#apple-hazdcoi)

**[- traceScriptedMessages:](#apple-hazdeny)

**[- traceStatements:](#apple-hazdgni)

**[- logTakeValueForDeclarationNamed:type:bindingNamed:
associationDescription:value:](#apple-ge3dcoju)

**[- logSetValueForDeclarationNamed:type:bindingNamed:
associationDescription:value:](#apple-ge3deojs)******************

**Statistics report**

**[- setStatisticsStore:](#apple-haytgna)

**[- statisticsStore](#apple-haytmna)

**[- statistics](#apple-haytknq)******

**Monitor support**

**[- monitoringEnabled](#apple-g44dsmi)

**[- activeSessionsCount](#apple-g43dmmq)

**[- refuseNewSessions:](#apple-hazdenrq)

**[- isRefusingNewSessions](#apple-g44dima)

**[- setMinimumActiveSessionsCount:](#apple-haydqoa)

**[- minimumActiveSessionsCount](#apple-g44dqna)

**[- terminateAfterTimeInterval:](#apple-haytqny)

**[- logToMonitorWithFormat:](#apple-ge3danbt)****************

**Resource manager support**

**[- setResourceManager:](#apple-haytcoa)

**[- resourceManager](#apple-haydcmq)****

**Request handling**

**[- defaultRequestHandler](#apple-haytooi)

**[- setDefaultRequestHandler:](#apple-haydqma)

**[- registerRequestHandler:forKey:](#apple-g44tkoa)

**[- removeRequestHandlerForKey:](#apple-geztamrv)

**[- registeredRequestHandlerKeys](#apple-g44tmni)

**[- requestHandlerForKey:](#apple-g44tsma)

**[- handlerForRequest:](#apple-g43tsna)**************

**User defaults**

**[+ loadFrameworks](#apple-gezdmmrq)

**[+ setLoadFrameworks:](#apple-g43dcoi)

**[+ isDebuggingEnabled](#apple-ge3dsnby)

**[+ setDebuggingEnabled:](#apple-ge2tmnrz)

**[+ autoOpenInBrowser](#apple-g42dimq)

**[+ setAutoOpenInBrowser:](#apple-geydi)

**[+ isDirectConnectEnabled](#apple-gezdkoju)

**[+ setDirectConnectEnabled:](#apple-gq3dknjq)

**[+ cgiAdaptorURL](#apple-g42dioi)

**[+ setCGIAdaptorURL:](#apple-ha3tgoa)

**[+ isCachingEnabled](#apple-g42dqna)

**[+ setCachingEnabled:](#apple-g42toma)

**[+ applicationBaseURL](#apple-g42deoa)

**[+ setApplicationBaseURL:](#apple-g42tiny)

**[+ frameworksBaseURL](#apple-g42doma)

**[+ setFrameworksBaseURL:](#apple-g42tsoa)

**[+ recordingPath](#apple-gezdmobq)

**[+ setRecordingPath:](#apple-gezdonrs)

**[+ projectSearchPath](#apple-gezdmnjw)

**[+ setProjectSearchPath:](#apple-gezdonzr)

**[+ isMonitorEnabled](#apple-g42dsoa)

**[+ setMonitorEnabled:](#apple-gezdomru)

**[+ monitorHost](#apple-g42tcmq)

**[+ setMonitorHost:](#apple-g43denq)

**[+ SMTPHost](#apple-geztknjx)

**[+ setSMTPHost:](#apple-gezdqmbq)

**[+ adaptor](#apple-ge3a)

**[+ setAdaptor:](#apple-geydqnjsg4)

**[+ port](#apple-g42tcoi)

**[+ setPort:](#apple-g43dgmy)

**[+ listenQueueSize](#apple-ge3dombw)

**[+ setListenQueueSize:](#apple-g43dcmq)

**[+ workerThreadCount](#apple-g43dkna)

**[+ setWorkerThreadCount:](#apple-g43diny)

**[+ additionalAdaptors](#apple-g42dcna)

**[+ setAdditionalAdaptors:](#apple-g42tima)

**[+ includeCommentsInResponses](#apple-g42dony)

**[+ setIncludeCommentsInResponses:](#apple-g43dani)

**[+ componentRequestHandlerKey](#apple-g42dknq)

**[+ setComponentRequestHandlerKey:](#apple-g42tony)

**[+ directActionRequestHandlerKey](#apple-g42dmmy)

**[+ setDirectActionRequestHandlerKey:](#apple-g42tsmi)

**[+ resourceRequestHandlerKey](#apple-g42tenq)

**[+ setResourceRequestHandlerKey:](#apple-g43dima)

**[+ sessionTimeout](#apple-ge3tgnru)

**[+ setSessionTimeOut:](#apple-geydsmrsga)********************************************************************************************

---

## Class Methods

---

### adaptor

+ (NSString \*)__adaptor__

Returns the class name of the primary adaptor. This is the cover method for the user default WOAdaptor.

__See also:__
[+ __setAdaptor:__](#apple-geydqnjsg4)

---

### additionalAdaptors

+ (NSArray \*)__additionalAdaptors__

Returns an array of adaptor description dictionaries. This is the cover method for the user default WOAdditionalAdaptors.

__See also:__
[+ __setAdditionalAdaptors:__](#apple-g42tima)

---

### application

+ (WOApplication \*)__application__

Initializes and returns a WOApplication object. This initializes application attributes and initializes the adaptor or adaptors specified on the command line. If no adaptor is specified, WODefaultAdaptor is made the default adaptor. Some of the more interesting attribute initializations are:

- Session store is in the server.
- Page cache size is 30 pages.
- Client caching of pages is enabled ([__isPageRefreshOnBacktrackEnabled__](#apple-g44dgmq) returns NO).
- Component-definition caching is disabled ([__isCachingEnabled__](#apple-geytambtgu) returns NO).

A exception is raised if initialization does not succeed.

You may call this method, but do not override it.

---

### applicationBaseURL

+ (NSString \*)__applicationBaseURL__

Returns a path to where the current application may be found under the document root (either the project or the __.woa__  wrapper). This is the cover method for the user default WOApplicationBaseURL.

__See also:__
[+ __setApplicationBaseURL:__](#apple-g42tiny)

---

### autoOpenInBrowser

+ (BOOL)__autoOpenInBrowser__

Returns whether automatic browser launching is enabled. By default, automatic browser launching is enabled.

---

### cgiAdaptorURL

+ (NSString \*)__cgiAdaptorURL__

Returns the URL for the web server including the path to the WebObjects CGI adaptor (for example, __http://localhost/cgi-bin/WebObjects__ ). This URL is used by the direct connect feature only. This is the cover for the user default WOCGIAdaptorURL.

__See also:__
[+ __setCGIAdaptorURL:__](#apple-ha3tgoa)

---

### componentRequestHandlerKey

+ (NSString \*)__componentRequestHandlerKey__

Returns the key which identifies URLs directed at component-action-based requests. By default, this method returns the string "wo".

---

### directActionRequestHandlerKey

+ (NSString \*)__directActionRequestHandlerKey__

Returns the key which identifies URLs directed at component-based requests. By default, this method returns the string "wa".

---

### frameworksBaseURL

+ (NSString \*)__frameworksBaseURL__

Returns a path to where all frameworks may be found under the document root. This value is used to determine URLs that should be generated to reference Web Server Resources in those frameworks. This is the cover method for the user default WOFrameworksBaseURL.

__See also:__
[+ __setFrameworksBaseURL:__](#apple-g42tsoa)

---

### includeCommentsInResponses

+ (BOOL)__includeCommentsInResponses__

Returns whether or not HTML comments are appended to the response. This is the cover method for the user default WOIncludeCommentsInResponses.

__See also:__
[+ __setIncludeCommentsInResponses:__](#apple-g43dani)

---

### isCachingEnabled

+ (BOOL)__isCachingEnabled__

Returns whether or not component caching is enabled. If this is enabled, changes to a component will be reparsed after being saved (assuming the project is under the NSProjectSearchPath). Note that this has no effect on page caching. This is the cover method for the user default WOCachingEnabled.

__See also:__
[+ __setCachingEnabled:__](#apple-g42toma), [- __pageCacheSize__](#apple-g44tcna), [- __isCachingEnabled__](#apple-geytambtgu)

---

### isDebuggingEnabled

+ (BOOL)__isDebuggingEnabled__

Returns whether or not debugging is enabled. If YES, [__debugWithFormat:__](#apple-g43tgma) prints out. Most startup-time status message are supressed if this method returns NO. By default, debugging is enabled. This is the cover method for the user default WODebuggingEnabled.

__See also:__
[- __setDebuggingEnabled:__](#apple-ge2tmnrz), [- __debugWithFormat:__](#apple-g43tgma)

---

### isDirectConnectEnabled

+ (BOOL)__isDirectConnectEnabled__

Returns whether or not direct connect is enabled. By default it is enabled. For more information, see [__setDirectConnectEnabled:__](#apple-gq3dknjq).

__See also:__
[+ __cgiAdaptorURL__](#apple-g42dioi)

---

### isMonitorEnabled

+ (BOOL)__isMonitorEnabled__

Returns whether or not the application can communicate with a Monitor application. It returns YES if the application can contact Monitor upon startup and subsequently let Monitor gather statistics. It returns NO if no comunication with Monitor can take place. By default, it can communicate with a Monitor application. 'This is a cover method for the user default WOMonitorEnabled.

__See also:__
[+ __setMonitorEnabled:__](#apple-gezdomru), [+ __monitorHost__](#apple-g42tcmq), [+ __setMonitorHost:__](#apple-g43denq)

---

### listenQueueSize

+ (NSNumber \*)__listenQueueSize__

Returns the size of the listen queue which will created by the primary adaptor (usually WODefaultAdaptor). This is the cover method for the user default WOListenQueueSize.

__See also:__
[+ __setListenQueueSize:__](#apple-g43dcmq)

---

### loadFrameworks

+ (NSArray \*)__loadFrameworks__

Returns the array of frameworks to be loaded during application initialization.

__See also:__
[+ __setLoadFrameworks:__](#apple-g43dcoi)

---

### monitorHost

+ (NSString \*)__monitorHost__

Returns the host on which Monitor is assumed to be running. This value is used during initialization if [__isMonitorEnabled__](#apple-g42dsoa) returns YES. This is a cover for the user default WOMonitorHost.

__See also:__
[+ __setMonitorHost:__](#apple-g43denq), [+ __isMonitorEnabled__](#apple-g42dsoa)

---

### port

+ (NSNumber \*)__port__

Returns the port number on which the primary adaptor will listen (usually WODefaultAdaptor). This is the cover method for the user default WOPort.

__See also:__
[+ __setPort:__](#apple-g43dgmy)

---

### projectSearchPath

+ (NSArray \*)__projectSearchPath__

Returns an array of file system paths which are searched for projects for rapid turnaround mode. This is the cover method for the user default NSProjectSearchPath.

__See also:__
[+ __setProjectSearchPath:__](#apple-gezdonzr)

---

### recordingPath

+ (NSString \*)__recordingPath__

Returns a file system path which is where the recording information should be saved. By default, this method returns null.

If this method returns a path, all requests and responses are recorded in the HTTP format in numbered files (__0000-request__ , __0000-response__ , __0001-request__ , __0001-response__ , and so on), and saved under the recording path specified. This directory is then used by the Playback tool to test the application. You will most likely set this as a command line argument (`-WORecordingPath pathname`), exercise your application to record a scenario you would like to test, and then stop the application. Afterward you can restart the application without the WORecordingPath argument, and point Playback to the recording directory just created to replay your sequence of requests and compare the responses received with the ones recorded.

__See also:__
[+ __setRecordingPath:__](#apple-gezdonrs)

---

### resourceRequestHandlerKey

+ (NSString \*)__resourceRequestHandlerKey__

Returns the key which identifies URLs directed through the resource request handler. Resource requests are only used during development of an application when the application is being run without an HTTP server.

__See also:__
[+ __setResourceRequestHandlerKey:__](#apple-g43dima)

---

### sessionTimeout

+ (NSNumber\*)__sessionTimeOut__

Returns the number (of seconds) which will be used as the default timeout for each newly created session. You may either override this method, change the user default WOSessionTimeOut, or set the session timeout in your session's __init__  method.

__See also:__
[+ __setSessionTimeOut:__](#apple-geydsmrsga)

---

### setAdaptor:

+ (void)__setAdaptor:__ (NSString \*)_anAdaptorName_

Sets the the class name of the primary adaptor to _anAdaptorName_.

__See also:__
[+ __adaptor__](#apple-ge3a)

---

### setAdditionalAdaptors:

+ (void)__setAdditionalAdaptors:__ (NSArray \*)_anAdaptorPlist_

Sets the array of adaptor description dictionaries to _anAdaptorPlist_. Each adaptor description dictionary must have "WOAdaptor" defined, which is the name of the adaptor class. Other attributes such as WOPort may also be specified, but are adaptor specific. For example WOWorkerThreadCount is specific to the WODefaultAdaptor class and may not apply for all adaptors.

__See also:__
[+ __additionalAdaptors__](#apple-g42dcna)

---

### setApplicationBaseURL:

+ (void)__setApplicationBaseURL:__ (NSString \*)_aBaseURL_

Sets to _aBaseURL_ the path to which the current application may be found under the document root (either the project or the __.woa__  wrapper).

__See also:__
[+ __applicationBaseURL__](#apple-g42deoa)

---

### setAutoOpenInBrowser:

+ (void)__setAutoOpenInBrowser:__ (BOOL)_isEnabled_

Controls whether starting up this application also launches a web browser. If _isEnabled_ is YES, the application launches the web browser. If NO, the application does not launch the browser. Browser launching is enabled by default as long as there is a WOAdaptorURL key in the file __NeXT_ROOT/NextLibrary/WOAdaptors/Configuration/WebServerConfig.plist__ .

To disable web browser launching, you must send this message in the __init__  method of your application subclass (or application script).

__See also:__
[+ __autoOpenInBrowser__](#apple-g42dimq)

---

### setCGIAdaptorURL:

+ (void)__setCGIAdaptorURL:__ (NSString \*)_aURL_

Sets the URL for the web server to _aURL_. The URL must include the path to the WebObjects CGI adaptor (for example, __http://localhost/cgi-bin/WebObjects__ ). This URL is used by the direct connect feature only..

__See also:__
[+ __cgiAdaptorURL__](#apple-g42dioi)

---

### setCachingEnabled:

+ (void)__setCachingEnabled:__ (BOOL)_flag_

Sets whether or not component caching is enabled. If this is enabled, changes to a component will be reparsed after being saved (assuming the project is under the NSProjectSearchPath). Note that this has no effect on page caching.

__See also:__
[+ __isCachingEnabled__](#apple-g42dqna), [- __pageCacheSize__](#apple-g44tcna), [- __isCachingEnabled__](#apple-geytambtgu)

---

### setComponentRequestHandlerKey:

+ (void)__setComponentRequestHandlerKey:__ (NSString \*)_key_

Sets the component request handler key. This affects all URLs generated during [__appendToResponse:inContext:__](#apple-g43tama): of component-based actions.

__See also:__
[+ __componentRequestHandlerKey__](#apple-g42dknq)

---

### setDebuggingEnabled:

+ (void)__setDebuggingEnabled:__ (BOOL)_flag_

Sets whether or not debugging is enabled. If YES, [__debugWithFormat:__](#apple-g43tgma) prints out. Most startup-time status message are supressed if this method returns NO. By default, debugging is enabled.

__See also:__
[+ __isDebuggingEnabled__](#apple-ge3dsnby), [- __debugWithFormat:__](#apple-g43tgma)

---

### setDirectActionRequestHandlerKey:

+ (void)__setDirectActionRequestHandlerKey:__ (NSString \*)_key_

Sets the Direct Action request handler key. This affects all URLs generated during [__appendToResponse:inContext:__](#apple-g43tama): of direct actions.

__See also:__
[+ __directActionRequestHandlerKey__](#apple-g42dmmy)

---

### setDirectConnectEnabled:

+ (void)__setDirectConnectEnabled:__ (BOOL)_flag_

Sets whether or not direct connect is enabled. By default it is enabled.

Direct connect actually transforms your application in a simple web server of its own. In particular, it is then able to find and return its images and resources as if it were a web server. It is very useful in development mode: You don't need a web server. Just point your URL to the port where your application is listening, and the application will handle all urls.

If this flag is YES, the following happens:

- When using [__autoOpenInBrowser__](#apple-g42dimq), a direct connect URL will be used.
- When using [WOMailDelivery](WOMailDelivery-2.md) to mail pages with dynamic links in them, these links will be generated with a complete direct connect URL format. People receiving these mails will be able to access the application with direct connect.
- _All files on the system are accessible through the resource request handler._ On the other hand, if this flag is NO, the resource request handler can be used to retrieve data objects from memory only, and no more reading in the file system is permitted (secure mode for deployment).

__See also:__
[+ __isDirectConnectEnabled__](#apple-gezdkoju), [+ __cgiAdaptorURL__](#apple-g42dioi)

---

### setFrameworksBaseURL:

+ (void)__setFrameworksBaseURL:__ (NSString \*)_aString_

Sets to _aString_ the path to where all frameworks may be found under the document root. This value is used to determine URLs that should be generated to reference Web Server Resources in those frameworks.

__See also:__
[+ __frameworksBaseURL__](#apple-g42doma)

---

### setIncludeCommentsInResponses:

+ (void)__setIncludeCommentsInResponses:__ (BOOL)_flag_

Sets whether or not HTML comments are appended to the response.

__See also:__
[+ __includeCommentsInResponses__](#apple-g42dony)

---

### setListenQueueSize:

+ (void)__setListenQueueSize:__ (NSNumber \*)_aListenQueueSize_

Sets the size of the listen queue which will created by the primary adaptor (usually WODefaultAdaptor).

__See also:__
[+ __listenQueueSize__](#apple-ge3dombw)

---

### setLoadFrameworks:

+ (void)__setLoadFrameworks:__ (NSArray \*)_frameworkList_

Sets the array of frameworks to be loaded during application initialization.

__See also:__
[+ __loadFrameworks__](#apple-gezdmmrq)

---

### setMonitorEnabled:

+ (void)__setMonitorEnabled:__ (BOOL)_flag_

Sets whether or not the application will communicate with a Monitor application. If _flag_ is YES, the application can contact Monitor upon startup and subsequently let Monitor gather statistics. If _flag_ is NO, no comunication with Monitor can take place. By default, it can communicate with a Monitor application.

__See also:__
[+ __isMonitorEnabled__](#apple-g42dsoa)

---

### setMonitorHost:

+ (void)__setMonitorHost:__ (NSString \*)_hostName_

Sets the host on which Monitor is assumed to be running. This value is used during initialization if [__isMonitorEnabled__](#apple-g42dsoa) returns YES.

__See also:__
[+ __monitorHost__](#apple-g42tcmq), [+ __isMonitorEnabled__](#apple-g42dsoa)

---

### setPort:

+ (void)__setPort:__ (NSNumber \*)_port_

Sets the port number on which the primary adaptor will listen (usually WODefaultAdaptor).

__See also:__
[+ __port__](#apple-g42tcoi)

---

### setProjectSearchPath:

+ (void)__setProjectSearchPath:__ (NSArray)_searchPath_

Sets the array of file system paths which are searched for projects for rapid turnaround mode.

__See also:__
[+ __projectSearchPath__](#apple-gezdmnjw)

---

### setRecordingPath:

+ (void)__setRecordingPath:__ (NSString \*)_path_

Sets the file system path where the recording information should be saved. Use null as the path if you don't want to save recording information. By default, recording information is not saved.

If you save recording information, all requests and responses are recorded in the HTTP format in numbered files (__0000-request__ , __0000-response__ , __0001-request__ , __0001-response__ , and so on), and saved under the recording path specified. This directory is then used by the Playback tool to test the application. You will most likely set this as a command line argument (`-WORecordingPath pathname`), exercise your application to record a scenario you would like to test, and then stop the application. Afterward you can restart the application without the WORecordingPath argument, and point Playback to the recording directory just created to replay your sequence of requests and compare the responses received with the ones recorded.

__See also:__
[+ __recordingPath__](#apple-gezdmobq)

---

### setResourceRequestHandlerKey:

+ (void)__setResourceRequestHandlerKey:__ (NSString \*)_key_

Sets the resource request handler key. This affects all URLs generated during [__appendToResponse:inContext:__](#apple-g43tama): of resources.

__See also:__
[+ __resourceRequestHandlerKey__](#apple-g42tenq)

---

### setSessionTimeOut:

public void __setSessionTImeOut__ (java.lang.Number _aTimeOut_)

+ (void)__setSessionTimeOut:__ (NSNumber\*)_aTimeOut_

Accessor to set the default session timeOut.

__See also:__
[+ __sessionTimeout__](#apple-ge3tgnru)

---

### setSMTPHost:

+ (void)__setSMTPHost:__ (NSString \*)_hostName_

Sets the name of the host that will be used to send e-mail messages created by [WOMailDelivery](WOMailDelivery-2.md).

__See also:__
[+ __SMTPHost__](#apple-geztknjx)

---

### setWorkerThreadCount:

+ (void)__setWorkerThreadCount:__ (NSNumber \*)_aWorkerThreadCount_

SEts the count of worker threads which will created by the primary adaptor (usually WODefaultAdaptor). A worker thread count of 0 implies single-threaded mode.

__See also:__
[+ __workerThreadCount__](#apple-g43dkna)

---

### SMTPHost

+ (NSString \*)__SMTPHost__

Returns the name of the host that will be used to send e-mail messages created by [WOMailDelivery](WOMailDelivery-2.md). This is the cover method for the user default WOSMTPHost.

__See also:__
[+ __setSMTPHost:__](#apple-gezdqmbq)

---

### workerThreadCount

+ (NSNumber \*)__workerThreadCount__

Returns the count of worker threads which will created by the primary adaptor (usually WODefaultAdaptor). A worker thread count of 0 implies single-threaded mode. This is the cover method for the user default WOWorkerThreadCount.

__See also:__
[+ __setWorkerThreadCount:__](#apple-g43diny)

---

## Instance Methods

---

### activeSessionsCount

- (int)__activeSessionsCount__

Returns the number of sessions that are currently active. (A session is active if it has not yet timed out.)

The number returned here is only accurate if the application stores state in memory in the server, which is the default. If you use a custom state-storage strategy, there may be no way to tell how many sessions are active for a given application instance.

__See also:__
[- __minimumActiveSessionsCount__](#apple-g44dqna), [- __setMinimumActiveSessionsCount:__](#apple-haydqoa)

---

### adaptorWithName:arguments:

- (WOAdaptor \*)__adaptorWithName:__ (NSString \*)_aName___arguments:__ (NSDictionary \*)_someArguments_

Invoked during the [__init__](#apple-geydsojygm) method to create an adaptor. If you subclass WOAdaptor, you specify the WOAdaptor subclass you want the application to use with the __-a__  option on the application's command line. When WOApplication encounters the __-a__  option, it invokes this method. This method looks for a subclass of WOAdaptor with the name _aName_ (which was supplied as the __-a__  option's argument), and if such a class exists, a new instance is initialized using the WOAdaptor method __initWithName:arguments:__ . The _someArguments_ array is populated with any adaptor-specific options (such as __-p__  or __-q__ ) that follow the adaptor name on the command line. See the [WOAdaptor](WOAdaptor-2.md) class for more information.

__See also:__
[- __adaptors__](#apple-g43dony)

---

### adaptors

- (NSArray \*)__adaptors__

Returns the current list of application adaptors. A WOApplication can have multiple adaptors. (To associate the WOApplication with multiple adaptors, you specify each adaptor on the application's command line using the __-a__  option.) This allows you to design an application that can not only listen to a socket for incoming HTTP requests (using the WODefaultAdaptor), but can also receive remote request messages using more advanced RPC mechanisms such as DO, CORBA, and DCOM.

---

### adaptorsDispatchRequestsConcurrently

- (BOOL)__adaptorsDispatchRequestsConcurrently__

Returns YES if at least one adaptor contains multiple threads and will attempt to concurrently invoke the request handlers.

---

### allowsConcurrentRequestHandling

- (BOOL)__allowsConcurrentRequestHandling__

Override to return YES if concurrent request handling is allowed.

---

### appendToResponse:inContext:

- (void)__appendToResponse:__ (WOResponse \*)_aResponse_ __inContext:__ (WOContext \*)_aContext_

The WOApplication object sends this message to itself to initiate the last phase of request handling. This occurs right after the __invokeActionForRequest:inContext:__ : method has completed, typically with the return a response page. In the append-to-response phase, the application objects (particularly the response component itself) generate the HTML content of the page. WOApplication's default implementation of this method forwards the message to the session object.

__See also:__
[- __invokeActionForRequest:inContext:__](#apple-ge4dsnry)

---

### awake

- (void)__awake__

Invoked at the beginning of each cycle of the request-response loop, affording the opportunity to perform initializations with application-wide scope. Since the default implementation does nothing, overridden implementations do not have to call __super__ .

__See also:__
[- __sleep__](#apple-haytioi)

---

### baseURL

- (NSString \*)__baseURL__

Returns the application URL relative to the server's document root, for example:

> ```
> WebObjects/Examples/HelloWorld.woa.
> ```

__See also:__
[- __name__](#apple-g44dsoi), [- __path__](#apple-g44tgni)

---

### createSessionForRequest:

- (WOSession \*)__createSessionForRequest:__ (WORequest \*)_aRequest_

Creates and returns a WOSession object to manage a session for the application. The method goes through several steps to locate the class to use for instantiating this object:

- First it looks for a compiled class of name "Session" that is a subclass of WOSession.
- If such a class does not exist, it looks for a "__.wos__ " script with the name of "Session" in the application wrapper ("__.woa__ " directory).
- If the __Session.wos__  script exists, the method parses the script and dynamically adds a scripted-class subclass of WOSession to the runtime.

The method then returns an allocated and initialized (using the default WOSession initializer) session instance of the selected class. It raises an exception if it is unable to create a new session.

__Note:__
An implication of the foregoing description is that the names of compiled WOSession subclasses
should be "Session"; if not, you will have to override this method to use the proper class to create the
session object.

__See also:__
[- __restoreSessionWithID:inContext:__](#apple-haydema), [- __saveSessionForContext:__](#apple-haydina)

---

### debugWithFormat:

- (void)__debugWithFormat:__ (NSString \*)_aFormatString,..._

Prints a message to the standard error device (stderr), if __WODebuggingEnabled__  is YES. The message can include formatted variable data using printf-style conversion specifiers. Note that in WebScript, all variables are objects, so the only conversion specifier allowed is __%@__ . In compiled Objective-C code, all __printf__  conversion specifiers are allowed.

You control whether this method displays output with the __WODebuggingEnabled__  user default option. If __WODebuggingEnabled__  is YES, then the __debugWithStringFormat:__  messages display their output. If __WODebuggingEnabled__  is NO, the __debugWithStringFormat:__  messages don\xd5 t display their output.

---

### defaultRequestHandler

- (WORequestHandler \*)__defaultRequestHandler__

Returns the request handler to be used when no request handler key was found in the URL or WORequest. This method returns the WOComponent request handler by default. When an application is contacted for the first time it is usually via a URL like the following:

> ```
> http://somehost/cgi-bin/WebObjects/AppName.woa
> ```

The way that URLs of that type are handled is determined by the default request handler.

---

### dispatchRequest:

- (WOResponse \*)__dispatchRequest:__ (WORequest \*)_aRequest_

The main entry point for any given interaction. Invoked by the adaptor.

---

### dynamicElementWithName:associations:template:languages:

- (WODynamicElement \*)__dynamicElementWithName:__ (NSString \*)_aName___associations:__ (NSDictionary \*)_someAssociations___template:__ (WOElement \*)_anElement_
__languages:__ (NSArray \*)_languages_

Creates and returns a WODynamicElement object based on the element's name, a dictionary of associations, and a template of elements. This method is invoked automatically to provide a WODynamicElement object that represents a `WEBOBJECT` element in the HTML template. You don't ordinarily invoke __dynamicElementWithName:associations:template:languages:__ , but you might override it to substitute your own WODynamicElement or reusable component for one of the built-in WODynamicElements.

The arguments _aName_ and _someAssociations_ are derived from a corresponding line in the declarations file. _aName_ is an NSString that identifies the kind of element to create. Generally _aName_ specifies a built-in WODynamicElement such as WOString, but it may also identify a reusable component. (For more information, see the chapter "Using Reusable Components" in the _WebObjects Developer's Guide_.) For example, in the __dynamicElementWithName:associations:template:languages:__  message for the following declaration:

> ```
> APP_STRING: WOString {value = applicationString;};
> ```

_aName_ contains the string "WOString".

The _someAssociations_ dictionary contains an entry for each attribute specified in the corresponding declaration. For the declaration above, _someAssociations_ contains a single entry for WOString's value attribute. The keys of _someAssociations_ are the attribute names and the values are WOAssociation objects.

WOApplication's implementation of __dynamicElementWithName:associations:template:languages:__  first searches for a WODynamicElement named _aName_. If a WODynamicElement is found, the method creates an instance using the method [__initWithName:associations:template:__](WODynamicElement-2.md#apple-gu2taoa) and returns it. Otherwise, it searches for a component-either scripted or compiled-to return instead. If neither are found, this method returns __nil__ .

---

### handleException:inContext:

- (WOResponse \*)__handleException:__ (NSException \*)_anException_ __inContext:__ (WOContext \*)_aContext_

Invoked when an exception occurs within the request-response loop. The default behavior displays a page with debugging information. You can override this method to catch exceptions and display a "friendlier" error page. For example, the following code replaces the standard error page with a component named __ErrorPage.wo__ .

> ```
> - (WOResponse *)handleException:(NSException *)anException {
> ```

> ```
> 	WOResponse *response = [[WOResponse alloc] init];
> ```

> ```
> 	WORequest *request = [[self context] request];
> ```

> ```
> 	WOString newURL = [NSString stringWithFormat:@"http://%@%@/%@.woa/-/ErrorPage.wo",
> ```

> ```
> 		[request applicationHost],
> ```

> ```
> 		[request adaptorPrefix],
> ```

> ```
> 		[request applicationName]];
> ```

> ```
>
> ```

> ```
> 	[response setHeader:newURL forKey:@"location"];
> ```

> ```
> 	[response setHeader:@"text/html" forKey:@"content-type"];
> ```

> ```
> 	[response setHeader:@"0" forKey:@"content-length"];
> ```

> ```
> 	[response setStatus:302];
> ```

> ```
> 	return response;
> ```

> ```
> }
> ```

__See also:__
[- __handleSessionCreationErrorInContext:__](#apple-g43tqma), [- __handleSessionRestorationErrorInContext:__](#apple-g43tqny)

---

### handlePageRestorationErrorInContext:

- (WOResponse \*)__handlePageRestorationErrorInContext:__ (WOContext \*)_aContext_

Invoked when a page (WOComponent) instance cannot be restored, which typically happens when a user backtracks too far. Specifically, this method is invoked when the following occurs: the request is not the first of a session, page restoration by context ID fails, and page re-creation is disabled. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See also:__
[- __handleException:inContext:__](#apple-g43tkoi), [- __handleSessionCreationErrorInContext:__](#apple-g43tqma),
[- __handleSessionRestorationErrorInContext:__](#apple-g43tqny)

---

### handleSessionCreationErrorInContext:

- (WOResponse \*)__handleSessionCreationErrorInContext:__ (WOContext \*)_aContext_

Invoked when a session (WOSession) instance cannot be created. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See also:__
[- __handleException:inContext:__](#apple-g43tkoi), [- __handlePageRestorationErrorInContext:__](#apple-g43tomy),
[- __handleSessionRestorationErrorInContext:__](#apple-g43tqny)

---

### handleSessionRestorationErrorInContext:

- (WOResponse \*)__handleSessionRestorationErrorInContext:__ (WOContext \*)_aContext_

Invoked when a session (WOSession) instance cannot be restored, which typically happens when the session times out. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See also:__
[- __handleException:inContext:__](#apple-g43tkoi), [- __handlePageRestorationErrorInContext:__](#apple-g43tomy),
[- __handleSessionCreationErrorInContext:__](#apple-g43tqma)

---

### handlerForRequest:

- (WORequestHandler \*)__handlerForRequest:__ (WORequest \*)_aRequest_

Returns the request handler used to handle a given request.

__See also:__
[- __registerRequestHandler:forKey:__](#apple-g44tkoa)_,_ [- __registeredRequestHandlerKeys__](#apple-g44tmni)_,_[- __requestHandlerForKey:__](#apple-g44tsma)

---

### init

- (id)__init__

Initializes application attributes and initializes the adaptor or adaptors specified on the command line. If no adaptor is specified, WODefaultAdaptor is made the default adaptor. Some of the more interesting attribute initializations are:

- Session store is in the server.
- Page cache size is 30 pages.
- Client caching of pages is enabled ([__isPageRefreshOnBacktrackEnabled__](#apple-g44dgmq) returns NO).
- Component-definition caching is disabled ([__isCachingEnabled__](#apple-geytambtgu) returns NO).

A exception is raised if initialization does not succeed.

__Note:__
The global variable "WOApp" is initialized in this method. Your subclasses of WOApplication
(including Application.wos) should be sure to call __super__ 's [__init__](#apple-geydsojygm) method as their first line of code.

---

### invokeActionForRequest:inContext:

- (WOElement \*)__invokeActionForRequest:__ (WORequest \*)_aRequest___inContext:__ (WOContext \*)_aContext_

The WOApplication object sends this message to itself to initiate the middle phase of request handling. In this phase, the message is propagated through the objects of the application until the dynamic element that has received the user action (for instance, a click on a button) responds to the message by triggering the method in the request component that is bound to the action. The default WOApplication implementation of this method forwards the message to the session object.

__See also:__
[- __appendToResponse:inContext:__](#apple-g43tama)

---

### isCachingEnabled

- (BOOL)__isCachingEnabled__

Returns YES if starting up the application also launches a web browser, and NO otherwise. Browser launching is enabled by default as long as there is a WOAdaptorURL key in the file __NeXT_ROOT/NextLibrary/WOAdaptors/Configuration/WebServerConfig.plist__ .

__See also:__
[+ __setAutoOpenInBrowser:__](#apple-geydi)

---

### isConcurrentRequestHandlingEnabled

- (BOOL)__isConcurrentRequestHandlingEnabled__

Returns whether component-definition caching is enabled. The default is NO.

__See also:__
[- __setCachingEnabled:__](#apple-geytcmruge)

---

### isPageRefreshOnBacktrackEnabled

- (BOOL)__isPageRefreshOnBacktrackEnabled__

Returns whether caching of pages is disabled in the client. If so, the client does not restore request pages from its cache but re-creates them "from scratch" by resending the URL to the server. This flag is set to NO by default.

__See also:__
[- __setPageRefreshOnBacktrackEnabled:__](#apple-haytamq)

---

### isRefusingNewSessions

- (BOOL)__isRefusingNewSessions__

Returns YES if the application instance is refusing new sessions, and NO otherwise. When the application instance refuses new sessions, the WebObjects adaptor tries to start the session in another instance of the same application. If no other instance is running and accepting new sessions, the user receives an error message.

---

### isTerminating

- (BOOL)__isTerminating__

Returns whether the application will terminate at the end of the current request-response loop.

__See also:__
[- __setTimeOut:__](#apple-haytimq), [- __terminate__](#apple-haytooi), [- __terminateAfterTimeInterval:__](#apple-haytqny), [- __timeOut__](#apple-haytsni)

---

### lock

- (void)__lock__

Locks the application object.

---

### lockRequestHandling

- (void)__lockRequestHandling__

Serializes request handler access if concurrent request handling isn't enabled.

---

### logSetValueForDeclarationNamed:type:bindingNamed:associationDescription:value:

- (void)__logSetValueForDeclarationNamed:__ (NSString\*)_aDeclarationName_
__type:__ (NSString\*)_aDeclarationType_ __bindingNamed:__ (NSString\*)_aBindingName_ __associationDescription:__ (NSString\*)_anAssociationDescription_ __value:__ (id)_aValue_

Formats and logs a message anytime a value is set through a WOAssociation, when WODebug is set to YES for the declaration in which the association appears. (Setting a value means the child component/element is setting a value in the parent). See [__logTakeValueForDeclarationNamed:type:bindingNamed:associationDescription:value:__](#apple-ge3dcoju) for a description of each of the arguments to this method.

---

### logTakeValueForDeclarationNamed:type:bindingNamed:associationDescription:value:

- (void)__logTakeValueForDeclarationNamed:__ (NSString\*)_aDeclarationName_
__type:__ (NSString\*)_aDeclarationType_ __bindingNamed:__ (NSString\*)_aBindingName_ __associationDescription:__ (NSString\*)_anAssociationDescription_ __value:__ (id)_aValue_

Formats and logs a message anytime a value is "taken" through a WOAssociation , when WODebug is set to YES for the declaration in which the association appears. (Taking a value means the child component/element is taking a value from the parent). Override this method to alter the format of the log message. The arguments of this method are defined in the following example of a WebObjects declaration.

> ```
> aDeclarationName : aDeclarationType {
> ```

> ```
>     aBindingName = anAssociationDescription;
> ```

> ```
> }
> ```

Also, _aValue_ is the value which is being pushed to or pulled from the child to the parent.

---

### logToMonitorWithFormat:

- (void)__logToMonitorWithFormat:__ (NSString \*)_aFormat,..._

Same as __logWithFormat:__  but prints the string to the Monitor application's standard error. That is, the message is displayed in the command-shell window that was used to launch the Monitor application.

You use this method to log messages about significant events when the application is ready to be deployed and you will use Monitor regularly to monitor the application. Otherwise, use __logWithFormat:__ . If the Monitor application is not running or if this application instance is not being monitored, this method does nothing.

---

### logWithFormat:

- (void)__logWithFormat:__ (NSString \*)_aFormat,..._

Prints a message to the standard error device (stderr). The message can include formatted variable data using printf-style conversion specifiers, for example:

> ```
> id i = 500;
> ```

> ```
> id f = 2.045;
> ```

> ```
> [self logWithFormat:@"Amount = %@, Rate = %@, Total = %@", i, f, i*f];
> ```

Note that in WebScript, all variables are objects, so the only conversion specifier allowed is __%@__  as shown above. In compiled Objective-C code, all __printf__  conversion specifiers are allowed. The equivalent method in Java is __logString__ .

---

### minimumActiveSessionsCount

- (int)__minimumActiveSessionsCount__

Returns the minimum number of active sessions allowed. If the number of active sessions is less than or equal to this number and [__isRefusingNewSessions__](#apple-g44dima) is YES, the application instance terminates. The default is 0.

__See also:__
[- __activeSessionsCount__](#apple-g43dmmq), [- __refuseNewSessions:__](#apple-hazdenrq), [- __setMinimumActiveSessionsCount:__](#apple-haydqoa)

---

### monitoringEnabled

- (BOOL)__monitoringEnabled__

Returns YES if the application is "monitorable" by the Monitor application, and NO otherwise. An application is "monitorable" if it was able to find a running Monitor upon startup and it is able to successfully communicate with that Monitor.

By default, all applications are monitorable if the Monitor application is running on the same machine as the application. You can specifically disable monitoring using the `-WOMonitorEnabled NO` option on the application command line. If you want the application to be monitorable and the Monitor is running on another host, you can start up the application through Monitor, or you can specify Monitor's host on the application command line this way:

> ```
> MyApp.exe -WOMonitorEnabled YES -WOMonitorHost monitorHost ...
> ```

__See also:__
[- __logToMonitorWithFormat:__](#apple-ge3danbt), the online document _ServingWebObjects_

---

### name

- (NSString \*)__name__

Returns the name of the application, which is the name of the executable (without the `.exe` extension).

__See also:__
[- __baseURL__](#apple-g43tcni), [- __path__](#apple-g44tgni)

---

### number

- (NSString \*)__number__

Returns `@"-1"`. This is provided for backwards compatibility only.

---

### pageCacheSize

- (unsigned int)__pageCacheSize__

Returns the size of the internal cache for page instances. The default size is 30 instances.

__See also:__
: [- __setPageCacheSize:__](#apple-gy2tgnby)

---

### pageWithName:forRequest:

- (WOComponent \*)__pageWithName:__ (NSString \*)_aName_ __forRequest:__ (WORequest \*)_aRequest_

Returns a new page instance (a WOComponent object) identified by _aName_. If _aName_ is __nil__ , the "Main" component is assumed. If the method cannot create a valid page instance, it raises an exception.

As part of its implementation, this method creates a context with _aRequest_ and calls [__pageWithName:inContext:__](#apple-g44teoa).

__See also:__
[- __restorePageForContextID:__](WOSession-2.md#apple-geyds) (WOSession), [- __savePage:__](WOSession-2.md#apple-geytg) (WOSession)

---

### pageWithName:inContext:

- (WOComponent \*)__pageWithName:__ (NSString \*)_aName_ __inContext:__ (WOContext \*)_aContext_

Returns a new page instance (a WOComponent object) identified by _aName_. If _aName_ is __nil__ , the "Main" component is assumed. If the method cannot create a valid page instance, it raises an exception.

__See also:__
[__pageWithName:forRequest:__](#apple-g44temi), [- __restorePageForContextID:__](WOSession-2.md#apple-geyds) (WOSession), [- __savePage:__](WOSession-2.md#apple-geytg)
(WOSession)

---

### path

- (NSString \*)__path__

Returns the filesystem path of the application, which is an absolute path and includes the "__.woa__ " extension; for example "__C:/NETSCAPE/ns-home/docs/WebObjects/Examples/HelloWorld.woa__ " is a typical application path.

__See also:__
[- __baseURL__](#apple-g43tcni), [- __name__](#apple-g44dsoi)

---

### permanentPageCacheSize

- (unsigned int)__permanentPageCacheSize__

Returns the permanent page cache size. The default is 30. The permanent page cache holds pages which should not fall out of the regular page cache. For example, a control page in a frameset should exist for the duration of a session.

__See also:__
[__savePageInPermanentCache:__](WOSession-2.md#apple-ge2tgnjx) (WOApplication)

---

### refuseNewSessions:

- (void)__refuseNewSessions:__ (BOOL)_flag_

Controls whether this application instance will create a session when it receives an HTTP request from a new user. If _flag_ is YES, the application does not create new sessions; when it receives a request from a new user, it refuses that request, and the adaptor must try to find another application instance that can process the request. If _flag_ is NO, the application creates new sessions. NO is the default.

You use this method with __setMinimumActiveSessionsCount:__  to gracefully shut down application instances. Use __setMinimumActiveSessionsCount:__  to set the active session minimum to a certain number. When number of active sessions reaches the number you set and __isRefusingNewSessions__  returns YES, the application terminates.

__See also:__
[- __activeSessionsCount__](#apple-g43dmmq), [- __isRefusingNewSessions__](#apple-g44dima), [- __minimumActiveSessionsCount__](#apple-g44dqna),
[- __setMinimumActiveSessionsCount:__](#apple-haydqoa)

---

### registerRequestHandler:forKey:

- (void)__registerRequestHandler:__ (WORequestHandler \*)_aHandler_ __forKey:__ (NSString \*)_aKey_

Registers a new request handler. _aKey_ must specify a key which can be found in the URLs following the instance number or application name.

__See also:__
[- __removeRequestHandlerForKey:__](#apple-geztamrv), [- __registeredRequestHandlerKeys__](#apple-g44tmni),
[- __requestHandlerForKey:__](#apple-g44tsma)

---

### registeredRequestHandlerKeys

- (NSArray \*)__registeredRequestHandlerKeys__

Returns an array of strings containing the keys of all of the registered request handlers.

__See also:__
[- __handlerForRequest:__](#apple-g43tsna), [- __requestHandlerForKey:__](#apple-g44tsma)

---

### removeRequestHandlerForKey:

- (WORequestHandler \*)__removeRequestHandlerForKey:__ (NSString \*)_aRequestHandlerKey_

Removes the specified request handler from the application.

__See also:__
[- __registerRequestHandler:forKey:__](#apple-g44tkoa), [- __requestHandlerForKey:__](#apple-g44tsma)

---

### requestHandlerForKey:

- (WORequestHandler \*)__requestHandlerForKey:__ (NSString \*)_key_

Returns the request handler used to handle requests containing the specified key.

__See also:__
[- __handlerForRequest:__](#apple-g43tsna), [- __registerRequestHandler:forKey:__](#apple-g44tkoa), [- __registeredRequestHandlerKeys__](#apple-g44tmni)

---

### requiresWOF35RequestHandling

- (BOOL)__requiresWOF35RequestHandling__

For backward compatibility, if your project depends upon features or side effects of the old request handling, you will want to override this method and return YES. By default, it returns NO.

---

### requiresWOF35TemplateParser

- (BOOL)__requiresWOF35TemplateParser__

For backward compatibility, if your project depends upon features or side effects removed from the new, 4.0 template parser, you will want to override this method and return YES. By default, it returns NO.

---

### resourceManager

- (WOResourceManager \*)__resourceManager__

Returns the WOResourceManager object that the application uses to manage resources.

__See also:__
[- __setResourceManager:__](#apple-haytcoa)

---

### restoreSessionWithID:inContext:

- (WOSession \*)__restoreSessionWithID:__ (NSString \*)_aSessionID_ __inContext:__ (WOContext \*)_aContext_

Restores the WOSession object representing a session. In normal request handling, this method is invoked at the start of a cycle of the request-response loop. The default implementation simply invokes WOSessionStore's [__checkoutSessionWithID:request:__](WOSessionStore-2.md#apple-gu3toni) method, but raises an exception if the WOSessionStore object is missing.

__See also:__
[- __createSessionForRequest:__](#apple-g43temy), [- __saveSessionForContext:__](#apple-haydina)

---

### run

- (void)__run__

Runs the application in a near-indefinite run loop in the default run-loop mode. Before starting the run loop, the method sends [__registerForEvents__](WOAdaptor-2.md#apple-gu2daoa) to the application's adaptors so that they can begin receiving run-loop events. Normally, [__run__](#apple-haydeoa) is invoked in the main function.

__See also:__
[- __setTimeOut:__](#apple-haytimq), [- __terminate__](#apple-haytooi), [- __terminateAfterTimeInterval:__](#apple-haytqny)

---

### runLoop

- (NSRunLoop \*)__runLoop__

Returns the application's run loop. Use this method when you need a run loop for such things as registering timers.

---

### saveSessionForContext:

- (void)__saveSessionForContext:__ (WOContext \*)_aContext_

Called at the end of the request handling loop, when the current session object needs to be saved. The default implementation simply invokes WOSessionStore's [__checkinSessionForContext:__](WOSessionStore-2.md#apple-gm3tmna) method, but raises an exception if the WOSessionStore object is missing.

__See also:__
[- __restoreSessionWithID:inContext:__](#apple-haydema)

---

### scriptedClassWithPath:

- (Class)__scriptedClassWithPath:__ (NSString \*)_aPath_

Loads a Webscript-based class with the pathname _aPath_ into the application. The specified script is parsed assuming the default string encoding, and the class and categories found in the script file are dynamically added to the runtime.

---

### scriptedClassWithPath:encoding:

- (Class)__scriptedClassWithPath:__ (NSString \*)_aPath_ __encoding:__ (NSStringEncoding)_anEncoding_

Loads a scripted class with the pathname _aPath_ using the encoding _anEncoding_. The class and categories found in the script file are dynamically added to the runtime. The script must use the `@interface/@implementation` syntax.

---

### sessionStore

- (WOSessionStore \*)__sessionStore__

Returns the application's current WOSessionStore object (which, by default, stores state in the server).

__See also:__
[- __setSessionStore:__](#apple-haytenq)

---

### setCachingEnabled:

- (void)__setCachingEnabled:__ (BOOL)_flag_

Enables or disables the caching of component definitions. Component definitions contain templates and other information about pages and subcomponents, and are used to generate instances of those components. When this flag is enabled, the application parses the script (or implementation) file, the HTML, and the declaration (".wod") file of a component once and then stores the resulting component definition. By default, this kind of caching is disabled so that you can edit a scripted component without having to relaunch the application every time to check the results. You should always enable component-definition caching when you deploy an application since performance improves significantly.

Do not confuse this type of caching with page-instance caching (see setPageCacheSize:). Caching Strategies in the class description provides further details.

__See also:__
[- __isCachingEnabled__](#apple-geytambtgu)

---

### setDefaultRequestHandler:

- (void)__setDefaultRequestHandler:__ (WORequestHandler \*)_aHandler_

Sets the default request handler. If, for instance, you want the default request handler to use direct actions, write something like the following:

> ```
> aHandler = [self requestHandlerForKey:@"wa"];[self setDefaultRequestHandler:aHandler];
> ```

__See also:__
[- __defaultRequestHandler__](#apple-haytooi)

---

### setMinimumActiveSessionsCount:

- (void)__setMinimumActiveSessionsCount:__ (int)_anInt_

Sets the minimum number of active sessions to _anInt_. The default is 0.

You use this method to gracefully shut down application instances. If the active sessions count reaches this number and isRefusingNewSessions returns YES, the application terminates. You might want to terminate application instances periodically for performance reasons; some applications leak a certain amount of memory per transaction, and shutting down and restarting instances of those applications can free up that memory.

__See also:__
[- __activeSessionsCount__](#apple-g43dmmq), [- __isRefusingNewSessions__](#apple-g44dima), [- __minimumActiveSessionsCount__](#apple-g44dqna),
[- __refuseNewSessions:__](#apple-hazdenrq)

---

### setPageCacheSize:

- (void)__setPageCacheSize__ :(unsigned int)_anInt_

Sets whether caching of page instances will occur and the number of pages the cache will hold. When page-instance caching is enabled, the application stores the WOComponent instance corresponding to the response page in the session. When the page is backtracked to, it restores it from the session and makes it the request page. The state of the page is retained. By default, page-instance caching is enabled, with a cache limit of 30 pages.

You turn page-instance caching off by invoking this method with an argument of zero. In this case, when the user backtracks to a page, the page is not stored in the session and so must be re-created "from scratch." Do not confuse this type of caching with component-definition caching (see [__setCachingEnabled:__](#apple-geytcmruge)).

__See also:__
[- __pageCacheSize__](#apple-g44tcna)

---

### setPageRefreshOnBacktrackEnabled:

- (void)__setPageRefreshOnBacktrackEnabled:__ (BOOL)_flag_

When _flag_ is YES, disables caching of pages by the client by setting the page's expiration-time header to the current date and time. (By default, this attribute is set to NO.) Disabling of client caching affects what happens during backtracking. With client caching turned off, the browser resends the URL to the server for the page requested by backtracking. The application must return a new page to the browser (corresponding to a new WOComponent instance). This behavior is desirable when you do not want the user to backtrack to a page that might be obsolete because of changes that have occurred in the session.

When this flag is turned on and a request corresponding to a client backtrack occurs, the retrieved page will only be asked to regenerate its response. The first two phases of a normal request-response loop (value extraction from the request and action invocation) do not occur.

See Caching Strategies in the class description for further details.

__See also:__
[- __isPageRefreshOnBacktrackEnabled__](#apple-g44dgmq)

---

### setPermanentPageCacheSize:

- (void)__setPermanentPageCacheSize:__ (unsigned int)_aSize_;

Sets the permanentPageCacheSize to aSize

__See also:__
[- __permanentPageCacheSize__](#apple-ge3tinjw)

---

### setResourceManager:

- (void)__setResourceManager:__ (WOResourceManager \*)_aResourceManager_

Sets the WOResourceManager object to _aResourceManager_. WOResourceManager objects search for and retrieve resources from the application directory and from shared framework directories.

__See also:__
[- __resourceManager__](#apple-haydcmq)

---

### setSessionStore:

- (void)__setSessionStore:__ (WOSessionStore \*)_aSessionStore_

Set the session-store object for the application. By default, an object that stores session state in process memory (that is, in the server) is used. The session-store object specifies the state storage strategy for the whole application. This object is responsible for making session objects persistent. You should set the session store object when the application starts up, before the first request is handled.

__See also:__
[- __sessionStore__](#apple-haydmnq)

---

### setStatisticsStore:

- (void)__setStatisticsStore:__ (WOStatisticsStore \*)_aStatisticsStore_

Sets the WOStatisticsStore object to _aStatisticsStore_. WOStatisticsStore objects record application statistics while the application runs.

__See also:__
[- __statisticsStore__](#apple-haytmna)

---

### setTimeOut:

- (void)__setTimeOut:__ (NSTimeInterval)_aTimeInterval_

Sets the number of seconds the application can experience inactivity (no HTTP requests) before it terminates execution.

This method differs from [__terminateAfterTimeInterval:__](#apple-haytqny) in that with this method, the application must be idle for _aTimeInterval_ seconds for the application to terminate.[__terminateAfterTimeInterval:__](#apple-haytqny) terminates the application whether it is active or not.

__See also:__
[- __timeOut__](#apple-haytsni)

---

### sleep

- (void)__sleep__

Invoked at the conclusion of a request-handling cycle to give an application the opportunity for deallocating objects created and initialized in its awake method. The default implementation does nothing.

---

### statistics

- (bycopyNSDictionary \*)__statistics__

Returns a copy of the dictionary containing the application statistics maintained by WOStatisticsStore. This method is used by the Monitor application to retrieve application statistics. If you need to access the statistics internally, use this message instead:

> ```
> [[[WOApplication application] statisticsStore] statistics]
> ```

---

### statisticsStore

- (WOStatisticsStore \*)__statisticsStore__

Returns the WOStatisticsStore object, which records statistics while the application runs.

__See also:__
[- __setStatisticsStore:__](#apple-haytgna)

---

### takeValuesFromRequest:inContext:

- (void)__takeValuesFromRequest:__ (WORequest \*)_aRequest_ __inContext:__ (WOContext \*)_aContext_

The component action request handler sends this message to the WOApplication to start the first phase of request handling. In this phase, the message is propagated to the session and component objects involved in the request as well as the request page's dynamic elements. Each dynamic element acquires any entered data or changed state (such as a check in a check box) associated with an attribute and assigns the value to the variable bound to the attribute. The default WOApplication implementation of this method forwards the message to the session object.

__See also:__
[- __appendToResponse:inContext:__](#apple-g43tama), [- __invokeActionForRequest:inContext:__](#apple-ge4dsnry)

---

### terminate

- (onewayvoid)__terminate__

Terminates the application process. Termination does not take place until the handling of the current request has completed.

__See also:__
[- __isTerminating__](#apple-g44dioa), [- __setTimeOut:__](#apple-haytimq)

---

### terminateAfterTimeInterval:

- (void)__terminateAfterTimeInterval:__ (NSTimeInterval)_aTimeInterval_

Sets the application to terminate itself after _aTimeInterval_ seconds has elapsed. After the specified time interval has elapsed, the application immediately stops all current processing. If any sessions are active, users may lose information.

This method differs from [__setTimeOut:__](#apple-haytimq) in that it does not set idle time; __terminateAfterTimeInterval:__ : shuts down the application regardless of whether it is idle.

---

### timeOut

- (NSTimeInterval)__timeOut__

Returns the application's time-out interval: a period (in seconds) of inactivity before the application terminates execution. The default application time-out interval is a very large number.

__See also:__
[- __setTimeOut:__](#apple-haytimq)

---

### trace:

- (void)__trace:__ (BOOL)_flag_

If _flag_ is YES, prints all trace messages (messages for scripted messages, compiled messages, and all statements in the application) to the standard error device. If _flag_ is NO, stops printing all trace messages.

__See also:__
[- __traceAssignments:__](#apple-hazdcmi), [- __traceObjectiveCMessages:__](#apple-hazdcoi):, [- __traceScriptedMessages:__](#apple-hazdeny),
[- __traceStatements:__](#apple-hazdgni)

---

### traceAssignments:

- (void)__traceAssignments:__ (BOOL)_flag_

If _flag_ is YES, prints a message to the standard error device every time an assignment statement is executed. If _flag_ is NO, stops printing trace assignment messages.

__See also:__
[- __trace:__](#apple-hazdamy), [- __traceObjectiveCMessages:__](#apple-hazdcoi):, [- __traceScriptedMessages:__](#apple-hazdeny), [- __traceStatements:__](#apple-hazdgni)

---

### traceObjectiveCMessages:

- (void)__traceObjectiveCMessages:__ (BOOL)_flag_

If _flag_ is YES, prints a message to the standard error device every time a message is sent to a compiled class from Webscript. If _flag_ is NO, stops printing these messages.

__See also:__
[- __trace:__](#apple-hazdamy), [- __traceAssignments:__](#apple-hazdcmi), [- __traceScriptedMessages:__](#apple-hazdeny), [- __traceStatements:__](#apple-hazdgni)

---

### traceScriptedMessages:

- (void)__traceScriptedMessages:__ (BOOL)_flag_

If _flag_ is YES, prints a message to the standard error device every time a message is sent to a scripted class from Webscript. If _flag_ is NO, stops printing trace scripted method messages.

__See also:__
[- __trace:__](#apple-hazdamy), [- __traceAssignments:__](#apple-hazdcmi), [- __traceObjectiveCMessages:__](#apple-hazdcoi), [- __traceStatements:__](#apple-hazdgni)

---

### traceStatements:

- (void)__traceStatements:__ (BOOL)_flag_

If _flag_ is YES, prints a message to the standard error device every time a statement in the application is executed from Webscript. If _flag_ is NO, stops printing trace statement messages.

__See also:__
[- __trace:__](#apple-hazdamy), [- __traceAssignments:__](#apple-hazdcmi), [- __traceObjectiveCMessages:__](#apple-hazdcoi), [- __traceScriptedMessages:__](#apple-hazdeny)

---

### unlock

- (void)__unlock__

Unlocks the application object.

---

### unlockRequestHandling

- (void)__unlockRequestHandling__

Disables serialized request handler access if concurrent request handling isn't enabled.

---

# Notifications

---

### WOApplicationDidFinishLaunchingNotification

Posted just before the application begins waiting for requests. The notification contains the application instance.

The notification contains the application instance.

---

### WOApplicationWillFinishLaunchingNotification

Posted when an application has finished its __init__  method. Register to receive this notification if you have an object that wishes to set various setting in the application. For example, if you have a WORequestHandler implemented in a framework and you want to register it with the WOApplication, you would register to receive this notification and then implement a method that register your WORequestHandler with the application.

The notification contains the application instance.

---

[!](WOAdaptor-2.md)
[!](WOAssociation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
