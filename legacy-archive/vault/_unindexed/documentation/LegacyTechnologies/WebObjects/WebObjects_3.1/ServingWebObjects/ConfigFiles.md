---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/ConfigFiles.html
archived_at: '2026-07-15T07:49:54.752448Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](HTTPAdaptors.md)

# Configuration Files

HTTP adaptors use configuration files to locate WebObjects application processes. There are two types of configuration files: public and private.

The _public configuration file_ provides information about WebObjects applications to the HTTP adaptor. This information tells the adaptor what applications are (or should be) running and allows the adaptor to balance transactions among different instances of the same application.

If you intend to do load balancing, you should use an ASCII text editor to create a public configuration file named __WebObjects.conf__. This file must go in a specific location in the file system depending on adaptor type (see "[Load Balancing](LoadBalancing.md#apple-kjcumnjygyzda)" for details). Each line in the file should conform to the following syntax:

```
    applicationName:instanceNumber@hostName portNumber
```

where:

- _applicationName_ is the path and name of the WebObjects application bundle below the document root of the active HTTP server.
- _instanceNumber_ is the instance number with which the administrator has started or will start the WebObjects application process.
- _hostName_ is the name (or IP address) of the machine on which the WebObjects application process is or will be running.
- _portNumber_ is the socket address at which the WebObjects application is (or will be) running on _hostName_.

For example, the line:

```
    Examples/HelloWorld:1@faux.next.com 3000
```

indicates the there is a process created from _DOCUMENT_ROOT___/Examples/HelloWorld__ running as instance 1 at port 3000 on the machine at address __faux.next.com__. The existence of this line doesn't guarantee that such a process is actually running. An adaptor will attempt to contact instances of an application according to the information specified in the public configuration file. It will fail if no application processes are running---that is, if processes have died or if the administrator has neglected to start WebObjects application processes that correspond to the information in the public configuration file.

Note that application instance numbers and port numbers must be unique to the machine upon which the application is running. This means that there can be two instances of an application with the same instance number as long as they're running on two different machines. Also note that the application path (for instance, "Examples/HelloWorld") uniquely identifies an application inside the configuration file; thus you cannot balance the load between an instance of "HelloWorld" and "Examples/HelloWorld".

For the complete load-balancing procedure, see "[Load Balancing](LoadBalancing.md#apple-kjcumnjygyzda)."

Every time someone manually starts an application or the adaptor autostarts one, a _private configuration file_ is created (if it doesn't exist) and an entry for the newly started application is registered in the file. The private configuration file, also named __WebObjects.conf__, is located in the temporary directory of the system (__/tmp__ for Unix platforms or the directory specified by the TEMP environment variable on Windows NT platforms). The activity associated with the private configuration file is independent of the public configuration file; indeed, if the public configuration file exists, the private configuration file is ignored. However, the adaptor searches the private configuration file for an application instance if it cannot find the public configuration file or if it cannot find the requested WebObjects application in the public configuration file. The adaptor contacts only one instance of an application in the private configuration file; if you manually start HelloWorld, and it's already been started, the entry for HelloWorld in the file is overwritten. (The old process will continue to run, but cannot be contacted.) The adaptor also cannot contact a remote instance of an application using the private configuration file.

The contents of the private configuration file are essentially the same as those of the public configuration file, except that the contents are stored as C structures, and so cannot be directly modified. This file should only be modified by the HTTP adaptor itself.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](AdaptorModes.md)
