---
title: Getting Started with WebObjects
apple_id: TP30001104
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-07-11'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_WebObjects/_index.html
archived_at: '2026-07-18T02:39:35.952827Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

WebObjects is a suite of tools and object-oriented frameworks that enable you to create and deploy web applications and web services for Mac OS X. Using the APIs and tools that WebObjects provides, and developing in Java, you can:

- Create database-driven web applications with dynamic page content
- Create HTML-based web applications that are scalable and reusable
- Create JavaServer Pages (JSP) and servlets
- Create distributed applications that perform web services

You can save time developing these applications using rapid prototyping tools. Finally, a number of deployment options are available.

### Start Here

If you are new to web client-server technologies, read the ADC topic page for [WebObjects](https://developer.apple.com/tools/webobjects/).

If you are new to WebObjects development, read [WebObjects Overview](../../documentation/Web%20Objects/WebObjects%20Overview/Introduction%20to%20WebObjects%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamby) to see how WebObjects works. You'll get an overview of how a three-tiered web application works and guidelines on selecting an approach that is best for your type of application.

### Choose a Learning Path

You have a wide range of APIs and tools to choose from when developing and deploying web applications for Mac OS X. Which tools and learning paths you choose depends on the type of web application you want to create. For example, if you develop web applications, especially database-driven web applications with dynamic page content, you want to use Enterprise Objects (EOF). WebObjects supports all types of applications, including HTML content and web services applications.

#### HTML-Based Web Applications

Typically, you use WebObjects to develop an HTML-based web application in which users view and edit content using a native web browser. The HTML pages can be dynamic based on the state of enterprise objects.

- If you are new to WebObjects and want to begin developing an HTML-based web application, read [WebObjects Web Applications Programming Guide](../../documentation/Web%20Objects/WebObjects%20Web%20Applications%20Programming%20Guide/Introduction%20to%20WebObjects%20Web%20Applications%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjq) for details on concepts and tasks.
- If you want to build a quick prototype of your HTML-based web application, read [WebObjects Direct to Web Guide](../../documentation/Web%20Objects/WebObjects%20Direct%20to%20Web%20Guide/Introduction%20to%20WebObjects%20Direct%20to%20Web%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjv).
- If you are using dynamic elements and prebuilt custom components, read WebObjects Dynamic Elements Reference, WebObjects Extensions Reference, and WebObjects 5.4 Reference.

Also, see [WebObjects Application Properties Reference](../../documentation/Web%20Objects/WebObjects%20Application%20Properties%20Reference/Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamrq) for both development and deployment WebObjects application command-line arguments.

#### J2EE Applications

WebObjects also supports integration with J2EE development tools and applications.

- If you want to deploy your WebObjects applications inside a servlet container or want to take advantage of WebObjects components (both standard and custom) in your JSP pages, read [WebObjects J2EE Programming Guide](../../documentation/Web%20Objects/WebObjects%20J2EE%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjt).

#### Web Services

A web service is a distributed application that provides some service through operations it defines to a consumer, a desktop application, or another web application. Web services is built on top of an industrywide messaging standard called SOAP.

- If you want to implement a web service or use a web service from your WebObjects application, read [WebObjects Web Services Programming Guide](../../documentation/Web%20Objects/WebObjects%20Web%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjz).

#### Database-Driven Applications

A common reason for using WebObjects is to create dynamic web content based on your enterprise objects stored in a back-end database. Enterprise Objects handles the mapping of database records to enterprise objects for you. You can use Enterprise Objects with any of the WebObjects approaches.

- If you are building a custom application and using the Enterprise Objects classes in your code, read [WebObjects Enterprise Objects Programming Guide](../../documentation/Web%20Objects/WebObjects%20Enterprise%20Objects%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjr) to understand better how this technology works. Read WebObjects 5.4 Reference for API descriptions.

#### Deployment Options

If you want to deploy a WebObjects application or service, read [WebObjects Deployment Guide Using JavaMonitor](../../documentation/Web%20Objects/WebObjects%20Deployment%20Guide%20Using%20JavaMonitor/Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambz). Also, see [WebObjects Application Properties Reference](../../documentation/Web%20Objects/WebObjects%20Application%20Properties%20Reference/Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamrq) for both web application, wotaskd, and Java Monitor command-line arguments.

#### Java Development

If you are new to Java development, read [Java for WebObjects Developers](https://developer.apple.com/library/archive/documentation/WebObjects/JavaForWODev/JavaForWODev.pdf) and Getting Started with Java for more information on Apple’s support for J2SE, J2EE, and other Java development tools.

#### Developing WebObjects Tools

If you are developing a third-party WebObjects tool to create EOModel and WOComponent objects, read WebObjects File Format Reference for a description of the file formats supported by WebObjects.

### Next Steps

The [WebObjects Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000438) includes the following high-level resource pages, which you can bookmark for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000436-TP30000592)

  Conceptual and how-to information for WebObjects.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000436-TP30000592)

  Focused, detailed descriptions in reference format for WebObjects.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000436-TP30000592)

  Notes containing the latest news about new or changed features in WebObjects.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000436-TP30000592)

  Sample applications demonstrating a wide variety of WebObjects API and techniques. If you have installed the WebObjects developer package, you might also want to check out the project examples in `/Developer/Examples/JavaWebObjects`.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000436-TP30000592)

  Programming topics, code snippets, and FAQs by Apple’s support engineers.
- Mailing Lists

  The WebObjects mailing list ([webobjects-dev](http://lists.apple.com/mailman/listinfo/webobjects-dev)) is an excellent place to discuss issues or topics with fellow WebObjects developers. There’s also a WebObjects deployment mailing list ([webobjects-deploy](http://lists.apple.com/mailman/listinfo/webobjects-deploy)) and a WebObjects announcement mailing list ([webobjects-announce](http://lists.apple.com/mailman/listinfo/webobjects-announce)). You can also subscribe to third-party Mac OS X and WebObjects mailing lists such as the [Omni Group Mailing Lists](http://www.omnigroup.com/developer/mailinglists/).

