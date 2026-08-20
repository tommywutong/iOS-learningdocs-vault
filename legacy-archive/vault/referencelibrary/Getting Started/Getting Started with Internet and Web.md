---
title: Getting Started with Internet and Web
apple_id: TP30001123
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-11-19'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_WebInternet/_index.html
archived_at: '2026-07-18T02:39:35.876453Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Mac OS X provides a wide variety of APIs and tools for developing web content and applications for the web. There are Web 2.0 technologies for creating and manipulating web content for Safari on the desktop, Safari on iPhone OS, and Dashboard. There are also web client APIs available to Cocoa and Carbon application developers to access web services and display and edit web content in desktop applications. There is WebObjects or pure Java to implement web server applications. There are also plenty of third-party APIs and tools for web server development available on Mac OS X (such as, PHP, Perl, Python, JSP, and MySQL).

### Start Here

Before you begin to write any code, it’s a good idea to be familiar with the underlying Internet and web technologies. Start by reading [Internet & Web](https://developer.apple.com/internet/index.html) for an overview of the tools available on Mac OS X.

### Choose a Learning Path

There is a vast set of technologies related to Internet & Web development. The subheadings in this section identify four distinct paths of Internet & Web development. Choose the path that is most appropriate for your project.

#### Creating Web Content

If you are creating or editing _web content_—files or data types that are transmitted by web server applications and displayed by web client applications—for Safari on the desktop, Safari on iPhone OS, or Dashboard, then use Web 2.0 technologies that include access to the Canvas element and Document Object Model (DOM). If you are new to JavaScript on Mac OS X, read [Apple JavaScript Coding Guidelines](../../documentation/Apple%20JavaScript%20Coding%20Guidelines/Introduction%20to%20Apple%20JavaScript%20Coding%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3daoby).

- __If you are creating JavaScript content to display in any Safari-based application,__ read [WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483) for concepts and tasks, and WebKit DOM Reference for API details. If you want to use the Quartz Composer WebKit plug-in, read [Quartz Composer WebKit Plug-in JavaScript Reference](../../documentation/Internet%20Web/Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference/Introduction%20to%20Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjx).
- __If you are creating HTML and CSS web content for Safari-based applications,__ read [Safari HTML Reference](../../documentation/Apple%20Applications/Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz) and [Safari CSS Reference](../../documentation/Apple%20Applications/Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq) for information on HTML and CSS support in Safari.
- __If you want to add visual effects to your web content,__ read [Safari CSS Visual Effects Guide](../../documentation/Internet%20Web/Safari%20CSS%20Visual%20Effects%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzs) for information on adding transitions, animations, and using transforms.
- __If you want to add audio and video to your web content,__ read [HTML Scripting Guide for QuickTime](../../documentation/Quick%20Time/HTML%20Scripting%20Guide%20for%20QuickTime/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmrv) and JavaScript Scripting Guide for QuickTime.
- __If you want to store data locally using JavaScript,__ read [Safari Client-Side Storage and Offline Applications Programming Guide](../../documentation/iPhone/Safari%20Client-Side%20Storage%20and%20Offline%20Applications%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjw) for the different ways you can store data locally.
- __If you are creating Dashboard applications, called widgets,__ read [Dashcode User Guide](../../documentation/Apple%20Applications/Dashcode%20User%20Guide/Introduction%20to%20Dashcode%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojs).

#### Creating Web Content for iPhone OS

If you are creating web content or applications specifically for iPhone OS, go to [Web Apps Dev Center](https://developer.apple.com/webapps) for details on creating web content for these handheld devices with touch screens.

#### Developing Web Client Applications

If you are developing _web client_ applications using Cocoa or Carbon, you can use the WebKit to display and edit web content in your windows. If you just want to send requests to a web services application, there’s an API for that, too. There are also C, Objective-C, and Java APIs for using web standards such as XML and URL in your applications. If you are new to Cocoa or Carbon development, read Getting Started with Cocoa or [Getting Started with Carbon](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Carbon/_index.html#//apple_ref/doc/uid/TP30001086) for links to additional resources.

- __If you are displaying or editing web content using Objective-C,__ read [WebKit Objective-C Programming Guide](../../documentation/Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i) for concepts and tasks, and [WebKit Objective-C Framework Reference](https://developer.apple.com/documentation/webkit) for API details. You can also read URL Loading System to learn more about the WebKit underpinnings.
- __If you are accessing the Document Object Model (DOM) from Objective-C,__ read [WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483) for concepts and [WebKit Objective-C Programming Guide](../../documentation/Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i) for Objective-C tasks.
- __If you are writing plug-ins using Objective-C,__ read WebKit C Reference.
- __If you are displaying or editing web content using C,__ read WebKit C Reference and [Carbon-Cocoa Integration Guide](../../documentation/Cocoa/Carbon-Cocoa%20Integration%20Guide/Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojt). You can also find articles on using the WebKit from Carbon applications in [WebKit Objective-C Programming Guide](../../documentation/Cocoa/WebKit%20Objective-C%20Programming%20Guide/Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3di2i).
- __If you are using web services in your applications,__ read [Web Services Core Programming Guide](../../documentation/Networking/Web%20Services%20Core%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobv) for details on how to access WSDL web services from your applications. Read [XML-RPC and SOAP Programming Guide](../../documentation/Apple%20Script/XML-RPC%20and%20SOAP%20Programming%20Guide/Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrw) for how to use AppleScript and the Apple Event Manager in Mac OS X to make remote procedure calls using the XML-RPC and SOAP protocols.
- __If you are accessing web content in your application using Objective-C or Java,__ read [XML Programming Topics for Core Foundation](../../documentation/Core%20Foundation/XML%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20XML%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeztq2i) and [Property List Programming Topics for Core Foundation](../../documentation/Core%20Foundation/Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i) for information on using XML in your applications. Read URL Loading System for information on using URLs in your applications.
- __If you are accessing web content in your application using C,__ read [XML Programming Topics for Core Foundation](../../documentation/Core%20Foundation/XML%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20XML%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeztq2i) and [Property List Programming Topics for Core Foundation](../../documentation/Core%20Foundation/Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i).

#### Developing Web Server Applications

If you are developing _web server_ applications, especially database-driven web applications, you want access to all the J2SE and J2EE development and deployment tools, including WebObjects, EOF, and JavaServer. WebObjects is specifically designed for implementing database-driven dynamic web content. You can easily turn any HTML-based WebObjects application into a web services application by simply using an assistant.

- __If you are creating dynamic, database-driven web applications or web services,__ read [WebObjects Overview](../../documentation/Web%20Objects/WebObjects%20Overview/Introduction%20to%20WebObjects%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamby) and [WebObjects Web Applications Programming Guide](../../documentation/Web%20Objects/WebObjects%20Web%20Applications%20Programming%20Guide/Introduction%20to%20WebObjects%20Web%20Applications%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjq) for specific information on using WebObjects to build and deploy web applications. Read [Getting Started with WebObjects](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_WebObjects/_index.html#//apple_ref/doc/uid/TP30001104) for a quick introduction to different ways of using this technology.
- __If you are creating web server Java applications,__ read Getting Started with Java for information on Apple’s support for J2SE, J2EE, Java Web Start, and other Java development tools.
- __If you are using third-party tools, such as MySQL or Perl, to develop web applications on Mac OS X,__ some useful websites are [mysql.com](http://www.mysql.com/), [macports.org](http://www.macports.org/), and [cpan.org](http://www.cpan.org/).

### Next Steps

The [Internet & Web Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000469) includes the following high-level resource pages, which you can bookmark for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000469)

  Conceptual and how-to information for developing web server and client applications, and Internet and web content.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000469)

  Focused, detailed descriptions in reference format for Internet and web, including Java technologies and low-level APIs for handling XML and URLs.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000469)

  Late-breaking news and highlights of new or changed features in the latest release.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000469)

  Samples demonstrating how to use APIs and tools.
- [Technical Note](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000469)

  Late-breaking documents on issues related to Internet and web.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000469)

  Programming tips, code snippets, & FAQs by Apple’s support engineers.

