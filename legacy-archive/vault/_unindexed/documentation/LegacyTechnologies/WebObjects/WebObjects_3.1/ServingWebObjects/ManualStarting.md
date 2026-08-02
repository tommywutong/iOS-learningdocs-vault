---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/ManualStarting.html
archived_at: '2026-07-15T07:50:00.364217Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](AdminTasks.md)

# Manually Starting WebObjects Applications

You manually start WebObjects applications when load balancing, when debugging applications, when your application requires special adaptors, or for similar reasons. You manually start applications from a _shell_, a type of program that accepts entered commands. For convenience, the Bourne shell supplied with WebObjects on Windows NT is assumed in this and other procedures.

## __Syntax and Arguments__

The syntax for starting __WODefaultApp__ and compiled WebObjects applications from a shell program is:

> _ApplicationName_ `[-c] [[-a` AdaptorClass`] [-n` InstanceNumber`] [-p` PortNumber`] [-q` ListenQueueDepth`]] [-d` DocumentRoot`]` ApplicationDirectory

**_ApplicationName_**

: The name of the compiled WebObjects application executable to run, or __WODefaultApp__. You must either connect to the directory containing the executable or supply the path to that directory. Compiled applications must either be located in the document root or in __NextLibrary/WOApps__. __WODefaultApp__ is located in __NextLibrary/Executables__.

: All WebObjects applications are managed by an application object which, through inheritance from WOApplication, knows how to process the arguments specified on the command line. __WODefaultApp__ is a generic WebObjects application that is used to interpret scripted applications. One __WODefaultApp__ process must run for each instance of a scripted WebObjects application. __WODefaultApp__ will not start an application on a remote host.

**`-c`**
: Requests that the application cache component definitions (page templates) instead of reparsing HTML, declaration, and script files upon each new HTTP request. By default, applications do not cache component definitions. This setting ensures that during development of scripted applications programmers can modify a component's logic and see the result without having to relaunch the application. If you are deploying applications, however, you should turn on page caching by specifying this flag when you launch the application.

**-a _AdaptorClass_**
: The class of an adaptor that the application will use to communicate with the server. You can specify multiple adaptors, as long as they are of different types. (For example, you could have a separate adaptor with its own port for communicating directly with Java applets on the browser.) If you specify multiple HTTP adaptors, only the last one specified will be made the active one).

The subsequent three arguments belong to the adaptor specified in _AdaptorClass_; the first two of these are used in load balancing: You cannot specify adaptor arguments unless you specify an adaptor class.

**-n _InstanceNumber_**
: A positive integer that uniquely identifies an application instance with which the adaptor will communicate. If you do not specify an instance number, the adaptor specified in _AdaptorClass_ creates one using random number generation. If a URL does not specify the instance number, the application is presumed to run on the server machine as a single instance application, as if it had been autostarted. If you specify _AdaptorClass_ for the purpose of load balancing, you must specify an instance number.

**-p _PortNumber_**
: Specifies the socket port used to communicate with an application instance. Port numbers must be over 1024 since numbers between zero and 1024 are reserved. If you specify _AdaptorClass_ for the purpose of load balancing, you must specify a port number.

**-q _ListenQueueDepth_**
: Specifies the queue depth on a TCP/IP socket at the entrance of the application. The default listen-queue depth is 4, meaning that while the application process is handling a request, up to four other requests can be in the socket buffer before the socket starts refusing them. If the application is expected to experience "spikes" in its processing load, it might be a good idea to increase the listen queue depth. Increasing this default does not necessarily improve performance or allow the application to serve more requests at sustained high loads.

**-d _DocumentRoot_**
: The document root of the server, which can be different from the _DOCUMENT_ROOT_ specified for a given web server. This argument is required and must come right before _ApplicationDirectory_ (that is, it is position-dependent).

**_ApplicationDirectory_**
: Specifies the directory path of an application relative to _DOCUMENT_ROOT___/WebObjects__. This path is required.

## __Examples__

The following example starts the scripted application TimeOff on Windows NT for the Netscape 1.1 server:

> ```
> > C:\NeXT\NextLibrary\Executables\WODefaultApp -d C:/NETSCAPE/ns-home/docs   Examples/TimeOff
> ```

The following example starts a compiled WebObjects example application on Mach, assigning it the default HTTP (CGI) adaptor and specifying port and instance numbers for that adaptor.

> ```
> > HelloWorldCompiled -a WODefaultAdaptor -n 1 -p 3000  -d /NextLibrary/WebServer/htdocs Examples/HelloWorldCompiled
> ```

You can start a compiled application in __NextLibrary/WOApps__ but the path to the application in WOApps should match _exactly_ the path to the application under _DOCUMENT_ROOT___/WebObjects__. In other words, if you have an "Examples" directory under _DOCUMENT_ROOT___/WebObjects__, there should be an "Examples" subdirectory in __NextLibrary/WOApps__.

## __Notes__

Since the Web server uses _DocumentRoot_ and _ApplicationDirectory_ argument to build URLs, you should use forward slashes as opposed to a backslashes when specifying these arguments.

As a convenience, you might create a shell script that starts WebObjects applications when the server machine is booted. You also might create another shell script that you can run at the command line to start applications.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](ManagingProcesses.md)
