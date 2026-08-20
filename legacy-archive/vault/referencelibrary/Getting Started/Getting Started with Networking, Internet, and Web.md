---
title: Getting Started with Networking, Internet, and Web
apple_id: TP40008807
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2009-05-27'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_NetworkingInternetWeb/_index.html
archived_at: '2026-07-18T02:39:24.938893Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

OS X provides a wide variety of APIs and tools for developing web content and applications for the web. There are Web 2.0 technologies for creating and manipulating web content for Safari on the desktop, Safari on iOS, and Dashboard. There are also web client APIs available to Cocoa and Carbon application developers to access web services and display and edit web content in desktop applications. Java is available for web server development. There are also plenty of third-party APIs and tools for web server development available on OS X (such as PHP, Perl, Python, JSP, and MySQL).

OS X also offers a rich set of networking APIs that provide advanced features while maintaining compatibility with open standards. OS X supports networking at all levels of development, from high-level Cocoa applications to the kernel. You can use Apple’s networking APIs to develop software that accomplishes a wide range of networking tasks, from providing access to web services within your application to writing a device driver for a network hardware device.

### Start Here

__Want to create a Dashboard widget?__

- Read [Dashcode User Guide](../../documentation/Apple%20Applications/Dashcode%20User%20Guide/Introduction%20to%20Dashcode%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojs) to create widgets and iOS web applications.

__Want to embed a webpage in your Cocoa application?__

- Read [WebKit Objective-C Programming Guide](../../documentation/Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i) for concepts and tasks.

__Want to create webpages for Safari on any platform?__

- Read [Safari Web Content Guide](../../documentation/Apple%20Applications/Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr) to create web content that is compatible and optimized for Safari on any platform.
- Read [Safari Web Inspector Guide](../../documentation/Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu) to test your webpages.

__Want to develop a network application with Core Foundation?__

- Read [CFNetwork Programming Guide](../../documentation/Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs) to take advantage of network protocols such as HTTP, HTTPS, and FTP.

__Want to develop a network application with Cocoa?__

- Read URL Loading System to take advantage of high-level wrappers around common URL-based tasks.
- Read [Stream Programming Guide](../../documentation/Cocoa/Stream%20Programming%20Guide/Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dq2i) to use input and output streams in your application.

### Go In Depth

__Using HTML, CSS, and JavaScript__

- Read [Safari HTML Reference](../../documentation/Apple%20Applications/Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz) and [Safari CSS Reference](../../documentation/Apple%20Applications/Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq) for information on HTML and CSS support in Safari.
- Read [WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483), WebKit DOM Reference, and [Safari DOM Extensions Reference](https://developer.apple.com/documentation/webkitjs) for the JavaScript APIs that allow you to access the Document Object Model (DOM).
- Read [Safari CSS Visual Effects Guide](../../documentation/Internet%20Web/Safari%20CSS%20Visual%20Effects%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzs) for information on adding transitions, animations, and using transforms.
- Read [Safari Client-Side Storage and Offline Applications Programming Guide](../../documentation/iPhone/Safari%20Client-Side%20Storage%20and%20Offline%20Applications%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjw) to learn various ways to store data locally.

__Accessing web content from a Cocoa application__

- Read [WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483) (for concepts) and [WebKit Objective-C Programming Guide](../../documentation/Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i) for (Objective-C tasks) to access the Document Object Model (DOM) from Objective-C.
- Read [XML Programming Topics for Core Foundation](../../documentation/Core%20Foundation/XML%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20XML%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeztq2i) and [Property List Programming Topics for Core Foundation](../../documentation/Core%20Foundation/Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i) for information on using XML in your applications.
- Read URL Loading System for information on using URLs in your applications.

__Writing a Safari plug-in__

- Read [WebKit Plug-In Programming Topics](../../documentation/Internet%20Web/WebKit%20Plug-In%20Programming%20Topics/Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmrr) if you are writing plug-ins using Objective-C.

__Using Web Services__

- Read [Web Services Core Programming Guide](../../documentation/Networking/Web%20Services%20Core%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobv) for details on how to access WSDL web services from your applications.
- Read [XML-RPC and SOAP Programming Guide](../../documentation/Apple%20Script/XML-RPC%20and%20SOAP%20Programming%20Guide/Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrw) for how to use AppleScript and the Apple Event Manager in OS X to make remote procedure calls using the XML-RPC and SOAP protocols.

__Creating a Web Server__

- Read [Java Development Guide for Mac](../../documentation/Java/Java%20Development%20Guide%20for%20Mac/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbs) for information on Apple’s support for Java development tools.
- Visit the [MySQL site](http://www.mysql.com/), the [MacPorts Project](http://www.macports.org/), and the [Comprehensive Perl Archive Network](http://www.cpan.org/) for information on third-party tools such as MySQL and Perl.

__Developing Client/Server Network Applications__

- Read [Bonjour Overview](../../documentation/Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i) and [NSNetServices and CFNetServices Programming Guide](../../documentation/Networking/NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw) to develop zero-configuration, Bonjour-enabled applications for OS X. Read [DNS Service Discovery Programming Guide](../../documentation/Networking/DNS%20Service%20Discovery%20Programming%20Guide/Introduction%20to%20DNS%20Service%20Discovery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnru) to develop Bonjour-enabled software on Linux, on Windows, using Java, or at the socket level on OS X.
- Read [System Configuration Programming Guidelines](../../documentation/Networking/System%20Configuration%20Programming%20Guidelines/Introduction%20to%20System%20Configuration%20Programming%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrv) for information on determining and configuring network preferences.
- Read [Distributed Objects Programming Topics](../../documentation/Cocoa/Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i) to take advantage of remote procedure calls in Cocoa.

__Developing In-Kernel Networking Software__

- Read [Network Device Driver Programming Guide](../../documentation/Device%20Drivers/Network%20Device%20Driver%20Programming%20Guide/Introduction%20to%20Network%20Device%20Driver%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjt) for information on developing network drivers with I/O Kit.
- Read [Network Kernel Extensions Programming Guide](../../documentation/Darwin/Network%20Kernel%20Extensions%20Programming%20Guide/Introduction%20to%20Network%20Kernel%20Extensions%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjy) for details on developing network kernel extensions, such as a custom firewall.
- Read `kpi_socket.h` in the KPI Reference for more information on using socket-level network communications from kernel code.

### Ready for More?

The Snow Leopard Reference Library holds plenty more resources that make your job easier. To narrow the list of resources, you can set filters to focus on specific resource types (such as guides or sample code) or on specific topics (such as user experience or data management).

