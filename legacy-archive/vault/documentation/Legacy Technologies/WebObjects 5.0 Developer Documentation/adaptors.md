---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeploymentAdditions/adaptors.html
archived_at: '2026-07-15T08:12:19.071889Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

__WebObjects Adaptors__

This document describes changes made to the WebObjects adaptor since WebObjects 4.5 Update 3.

__Supported Configurations__

The list of web server configurations supported by the adaptor in the WebObjects 5 release includes:

|  |  |  |
| --- | --- | --- |
| Operating System | Web Server | Adaptor type |
| Mac OS X | Apache | plugin |
| Solaris | Apache | plugin |
| Solaris | Netscape (NSAPI) | plugin |
| Windows 2000 | IIS | plugin |
| Windows 2000 | Netscape (NSAPI) | plugin |
| all of the above | any | CGI |

Refer to [http://til.info.apple.com/techinfo.nsf/artnum/n72598](http://til.info.apple.com/techinfo.nsf/artnum/n72598) for specific operating system and web server version information.

__Nomenclature__

In this document, the term "adaptor" is used to describe functionality which applies generally to any of the supported configurations listed above. For functionality which is specific to a particular web server or operating system, the web server and/or operating system is specified, as in "Apache adaptor" or "NSAPI adaptor". The combination of operating system and web server is together referred to as a "platform".

The adaptors obtain configuration information from multiple sources. Some options are read only when the adaptor initializes; these are referred to as "startup options". Some information is updated periodically over the lifetime of the adaptor process; these are referred to as "configuration options", or simply "configuration". Another type of configuration information is specified as settings in the source code; these are referred to as "compile-time options". Changing a compile-time option typically requires changing a source file in the adaptor project and recompiling the _entire_ project.

__Adaptor Overview__

The WebObjects adaptor source consists of a number of files which are common to all platforms, and a relatively small amount of code which interfaces with the specific runtime environment. It is important to note the differences between the various platforms' execution environments. The CGI adaptor is a single threaded process which runs only long enough to process one request. The Apache web server is a single threaded process which runs for many requests, and typically there are many Apache adaptors running simultaneously in different processes. The Apache and CGI adaptors must be able to properly operate in a multiprocess environment. The IIS and Netscape web servers are multithreaded and run for many requests. The IIS and Netscape adaptors must be able to properly operate in a multithreaded environment. Since most of the adaptor code is common to all platforms it must be carefully written to behave well in all circumstances (multiprocess vs single process, multithreaded vs single threaded). Many of the limitations of the adaptors in WebObjects 4.5 can be attributed to problems associated with assumptions about the execution environment that do not generalize well. Addressing these issues has been a priority for the adaptor changes in WebObjects 5.

Each platform's adaptor has its own way to obtain startup options, and the set of options may vary between platforms. One important startup option is the config URL, which specifies where the configuration is obtained.

  The configuration specifies the available application instances and settings, and is updated periodically. The configuration may be obtained either from wotaskd or from a static file. If the configuration is obtained from wotaskd, it may be from either a specific list of machines or from all machines that answer a multicast request. In WebObjects 4.5, the default config URL specified a multicast query. For WebObjects 5, this default has been changed to specify a query to wotaskd only on the machine running the adaptor.
__Adaptor Operation__

The main function performed by the WebObjects adaptor is to act as a bridge between the web server and the application instance(s). When the adaptor receives a request, it normally performs the following basic operations:

1) reads the entire contents of the request and performs some basic validation

2) determines which application instance should receive the request

3) sends the request to the instance

4) reads a response from the instance

5) sends the response back to the user

If something goes wrong during this process, such as a communications failure with a particular instance, the adaptors implement various failure recovery mechanisms. These failure recovery mechanisms have changed since WebObjects 4.5. The behavior in WebObjects 5 is described below.

One useful method for obtaining information about the operation of the adaptors is through adaptor logging. Adaptor logging is enabled by creating a file named "logWebObjects" (this name is a compile-time option) in the system's temporary directory (typically /tmp, or C:\TEMP on Windows). The log information is then written by default to a file named "WebObjects.log", also in the system's temporary directory, though the log file may be changed either as a compile-time option or a startup option on some platforms. (The other important way to obtain information about the status of the adaptor is the WOAdaptorInfo page, formerly known as the 'xyzzy' page.)

__Changes since WebObjects 4.5__

This section describes changes to the adaptors since WebObjects 4.5 Update 3.

__Persistent Shared Adaptor State__

One substantial change to the adaptors is the addition of support for persistent shared state backed by the filesystem. (Currently this support is implemented on all UNIX platforms, but not on the Windows platforms.) The purpose of this shared state support is to enable use of some adaptor features which require shared or persistent state on platforms where it is not inherent, such as Apache or CGI. When the persistent shared state is enabled, all of the adaptor's configuration state information is stored in a file in the filesystem which is memory mapped as shared memory in all the adaptor processes. (Currently this file is named WOAdaptorState and resides in the system's temporary directory.)

Support for persistent shared state is a compile-time option. It may be disabled by defining the preprocessor macro DISABLE_SHARED_MEMORY in the appropriate Makefile. Shared state is enabled by default for Apache on Mac OS X and Mac OS X Server, and for CGI on all platforms except Windows.

When an adaptor process initializes, the state file is created if it does not already exist, and is mapped into the adaptor process' address space. All access to adaptor configuration information refers to the memory mapped from this file. Access to this information is synchronized using a combination of mutexes to provide synchronization between threads in a single adaptor process and file locking to provide synchronization between different processes. If customizations to the adaptor are required for a particular deployment, care should be taken to ensure that the proper synchronization semantics are observed. (Refer to documentation in the adaptor source, in particular the comments in appcfg.h.)

There is no valuable information in the state file. It is always safe to stop the web server, delete the state file, and restart the web server. (In rare instances this may be the only way to "reset" the adaptor to a clean state.) Furthermore, the adaptor state file depends on some of the compile-time options. In general, different builds of the adaptor may not be able to share the same state file, particularly if the size or arrangement of certain data structures is modified. If a new adaptor binary is installed the state file should be cleared by simply removing it from the filesystem. If this is not done the adaptor may fail to initialize properly, and will not service requests.

It is possible for the information in the persistent state file to become out of sync with the rest of the system. For example, if a particular Apache process begins processing a request but crashes before completing it then that request remains marked active in the state file forever. (This appears as a persistent active request in the WOAdaptorInfo page, and has the side effect of preventing an instance which has been shut down or deleted from being removed from the configuration.) Administrators can recover from this situation by removing the state file and restarting the web server.

In practice, the Apache adaptor realizes the greatest benefit from sharing state. In WebObjects 4.5 each Apache process performs load balancing and queries wotaskd to update the configuration independently of the others. In WebObjects 5 only one Apache process queries wotaskd to update the configuration for all Apache processes simultaneously. Additionally, load balancing is performed globally, so round robin scheduling selects instances in a round robin manner regardless of which Apache process services the request. In the case of CGI, because the CGI adaptor maps the configuration from the state file not every CGI process needs to query wotaskd. Similarly, CGI can perform proper round robin load balancing.

The shared state file is created with restricted permissions for security reasons. The permissions are read/write by owner only. Additionally, the CGI adaptor may execute as a different user than the plugin adaptor. So switching from a plugin to CGI or vice versa may require removing the state file (so it can be recreated) or changing its permissions. It is even possible to configure the CGI adaptor and a plugin adaptor to concurrently use the same shared state file if the permissions are set correctly. However, if the adaptor cannot access the shared state file it fails to initialize and will not service requests. (The failure is recorded in the adaptor log.)

(Even though state information is shared between adaptor processes, connections to instances are not shared. If connection pooling is enabled each adaptor process maintains its own connection pool. In practice, this is primarily of concern only in the case of the Apache adaptor. On a busy deployment site each Apache process may hold open a connection to each instance, resulting in a large number of open connections.)

__Configuration__

The runtime configurable settings have changed since WebObjects 4.5. This section provides an overview of the settings in the WebObjects 5 release. (See also the woadaptor.dtd and woadaptor.xml files in the adaptor source.)

As part of the changes to support the shared adaptor state, all data structures which store configuration information are of fixed size. This means there are limits on the maximum lengths of application names and redirection URLs, as well as a limit on the number of concurrent applications and instances which the adaptor can retain. These limits are all compile-time options, and may be adjusted by modifying the file config.h and rebuilding the adaptor.

Adaptor level settings

Adaptor level settings are currently all compile-time options only, set in the file config.h.

Application level settings

The following are the application level settings and their meanings as of this writing:

scheduler - which scheduling algorithm to use for new requests; currently random, roundrobin, or loadaveraging.

redirect URL - if a request cannot be serviced by an instance due to some error, a redirection to this URL is returned

additional args - an "additional arguments" setting is present but not used by the adaptor. It is for use by customer extensions.

app name - specifies the name of the application being configured

retry count - specifies the number of times a request is retried if a communications failure occurs

dead interval - if a communication failure occurs, this specifies the minimum time in seconds to wait before attempting to schedule a request for the particular instance

pool size - specifies the maximum number of simultaneous connections a particular adaptor process should keep open to each configured instance

URL version - specifies whether the app uses version 3 or version 4 URLs

Instance level settings

The following are the instance level settings and their meanings as of this writing:

instance number - a unique identifier for each particular instance

host - the name of the host on which the instance is running

additional args - an "additional arguments" setting is present but not used by the adaptor. It is for use by customer extensions.

port - the port number on which the instance is listening for new requests

send buffer size - size of the TCP send buffer on the connection to the instance

receive buffer size - size of the TCP receive buffer on the connection to the instance

send timeout - if data cannot be sent to an instance due to a busy connection, this specifies the maximum time to wait for the connection to accept new data. If this timeout is exceeded an error is generated.

receive timeout - when reading a response from an instance and no data is available to read, this specifies the maximum time to wait for more data to become available. If this time is exceeded an error is generated.

connect timeout - specifies the maximum time to wait for a connection to become ready to use

(Note that with the current non-blocking sockets transport implementation, send timeouts and connect timeouts are unlikely to occur.)

__Development Instances vs Deployment Instances__

The WebObjects 5 version of the adaptor makes a distinction between development instances and deployment instances. An instance with a negative instance number is considered a development instance, while instances with positive instance numbers are considered deployment instances. The adaptor only load balances requests to deployment instances, and never selects a development instance.

Instance numbers are made known to the adaptor in the configuration read either from wotaskd or from a static file. wotaskd keeps track of all running instances, and reports instances which have been set up using Monitor as deployment instances. Other instances (those started by hand or in ProjectBuilder, for example) are reported as development instances.

If a request specifies an instance number for a development instance the request is processed normally. This allows administrators to start and test instances in a deployment environment without exposing the development instance to users. Both development and deployment instances are listed in the WOAdaptorInfo page, and this page contains links to connect to individual instances, either Direct Connect or through the adaptor.

The adaptor tries to load balance whenever a request does not specify an instance or the request specifies an invalid instance. It is possible to specify a development instance in the request and have the adaptor load balance the request to a deployment instance if the development instance is unavailable.

__WOAdaptorInfo page__

The WebObjects 4.5 adaptor includes support for a page which displays information about the adaptor's current status. In WebObjects 4.5 this page was commonly known as the "xyzzy" page. In WebObjects 5 this page is referred to as the WOAdaptorInfo page. Furthermore, it is no longer returned by a "magic" request to the adaptor. Instead, if the WOAdaptorInfo page is enabled it is returned when a request does not specify an application or specifies an unknown application. (The WOAdaptorInfo page is disabled by default.) Finally, the content of the WOAdaptorInfo page has been modified to be more readable, and to include hyperlinks to connect to all known instances (either using Direct Connect or through the web server).

For the CGI adaptor, some environment variable names have changed between WebObjects 4.5 and WebObjects 5. The environment variable "WO_XYZZY_USERNAME" has been renamed "WO_ADAPTOR_INFO_USERNAME", and the environment variable "WO_XYZZY_PASSWORD" has been renamed "WO_ADAPTOR_INFO_PASSWORD".

The WOAdaptorInfo page displays all application and instance settings in the configuration. Additionally, the WOAdaptorInfo page displays the following statistics for each instance:

active reqs - The number of requests currently being serviced. This is the number of requests which have been sent to the instance for which the adaptor has not yet received a response (or timed out).

served - The total number of requests serviced by the instance.

conn pool peak - The peak number of connections to the instance in any single adaptor process. (Typically this is 1 for Apache or CGI.)

conn pool reused - The number of times a pooled connection to the instance has been reused.

refusing timeout - The amount of time (in seconds) the adaptor will wait before the load balancing can select the instance. This timer gets set to a nonzero value if the adaptor receives a response from an instance indicating the instance is refusing new sessions.

dead timeout - If this time is nonzero it indicates a communications failure has occurred with the instance. The timer is initialized with the configured dead interval for the application. The dead timeout indicates the remaining time from the dead interval.

__Miscellaneous Changes__

This section lists other changes in the adaptors since WebObjects 4.5

The instance level setting "refuseNewSessions" has been eliminated. An instance can still be set to refuse new sessions, but this is reported to the adaptor directly from the instance itself rather than through the adaptor configuration.

All adaptor level settings have been eliminated. Adaptor level configuration is performed at compile-time only.

The plist (WebObjects.conf) style configuration file parser has been deprecated. The source is still included for sites which require this format, but it is not compiled by default.

In WebObjects 4.5 the adaptor never "forgot" about an instance. If an instance was deleted it was marked deleted but it still appeared in the xyzzy page. In WebObjects 5 the adaptor can forget about an instance, so it will disappear from the WOAdaptorInfo page after deletion. (Note that a pending request locks the instance into the adaptor configuration. The adaptor cannot remove the instance until all pending requests have completed.)

The apache.conf file that accompanies the Apache adaptor is no longer a full Apache config file as it was in WebObjects 4.5. Instead, it contains only the WebObjects-specific config. This file should be appended to the Apache config to enable WebObjects. The options which can be set in this file and their meanings remain unchanged, though some default values have changed (in particular, the name of the WOAdaptorInfo page).

The adaptor project makefiles have been rewritten. The new adaptor makefiles do not depend on the ProjectBuilder makefiles.

The WebObjects 4.5 adaptor included several communications transports which were historical and not used. These have been removed. The transport currently in use is the non-blocking sockets transport.

The load averaging load balancer has been modified. Now, an "effective load" is computed which is the "reported load" from the last instance response, minus an age factor based on how much time has passed since the instance has serviced a request. The effective load, reported load, and load age are reported on the WOAdaptorInfo page.

__Failover__

This section describes how the WebObjects 5 adaptor behaves when handling request/response errors.

In the normal case when a request comes to the adaptor the following things happen:

1) The adaptor selects an instance to receive the request. If the request was directed to a specific instance, that instance is selected. Otherwise the load balancer configured for the application is invoked to select the instance.

2) The request is sent to the instance.

3) The adaptor reads a response from the instance.

4) The adaptor sends the response back to the user.

There are many places where things might go wrong along the way. The selected instance might be refusing new sessions, or it might not be currently running, or it might crash or hang while processing the request. Typically if something goes wrong the adaptor tries to send the request to a different instance.

There are two types of request/response failures: communications failures and redirections due to an instance refusing new sessions. These are handled slightly differently by the adaptors. But in either case if no valid response can be generated from any instance the adaptor returns an error response. Additionally, the instance selection may fail.

__Selection Failures__

Normally the adaptor invokes the load balancer configured for the particular application to select an instance. The load balancer may fail to select an instance. (For example, all instances may be refusing new sessions.) If this happens the adaptor falls back to a more basic method: try each one on the list in turn. Unlike the load balancers, this fallback method ignores the refusing new sessions flag. This is an attempt to ensure that all options are exhausted before returning an error to the user, as some instance may have started accepting new sessions. In effect the adaptor double checks that instances marked as refusing are still refusing new sessions. (If the instance is still refusing it returns a redirection, discussed below.) No instance is ever selected more than once for a particular request. If no instance can be selected the request fails.

Note that if a request specifies an instance number that instance is selected first and the load balancer is not invoked to select the instance. The instance specified in the request is tried first regardless of whether it is marked as refusing new sessions. In this way it is possible to contact a specific instance. If, however, the specified instance fails to respond or refuses the request then the load balancer chooses subsequent instances to try, as above.

__Communications Failures__

A communications failure is any abnormal condition encountered during sending a request or receiving a response. Some examples of situations which generate communications failures:

- The instance is not running, therefore the adaptor cannot connect to it.

- The instance crashes, so the adaptor cannot read a response.

- The instance hangs, so the adaptor times out waiting for a response.

- A network problem might cause the adaptor to time out either sending a request or receiving a response.

- Connection pooling is enabled and the instance has restarted.

If the adaptors encounter a communications failure while processing a request/response transaction to a particular instance, that instance is marked as dead (and hence unusable for the term specified by the configured dead interval) and a failure count for the request is incremented. If the failure count is less than the configured retry count for that application then a new instance is selected and the request is sent to the new instance. If the failure count exceeds the retry count, or there is no instance that can be selected then the request fails.

If connection pooling is in use and wotaskd is performing instance scheduling, then when an instance restarts the first reuse of a pooled connection to the instance will fail. This causes the instance to be marked dead. The same situation occurs if an instance crashes and is restarted.

__Redirections (Refusing New Sessions)__

Instances which are refusing new sessions generate a redirection response if the request would require that a new session be created. If the adaptor receives such a response the redirection is handled internally by the adaptor and is not returned to the user. (In this case there was no communications failure, so the failure count is not incremented and the redirection is not applied towards the retry count as was described above.) The instance in question is marked as refusing new sessions, a different instance is selected, and the request is sent to the new instance. If no new instance can be selected the request fails.

The redirection response from the instance is the only mechanism by which the adaptor learns the instance is refusing new sessions. When this happens the adaptor waits for a period of time (determined by the instance, based on its session timeout and active sessions) before attempting to schedule the instance again. The remaining "refusing timeout" is visible on the WOAdaptorInfo page.

__Failed Requests__

If the request fails then the adaptor returns a redirection to the redirect URL configured for the application. (The redirect URL is configured using Monitor, or the XML adaptor config file). If there is no redirect URL specified for the application then the adaptor returns a static html page with an error message.

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
