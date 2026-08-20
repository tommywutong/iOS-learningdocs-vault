---
title: WebObjects Web Applications Programming Guide
apple_id: TP30001010
resource_type: Guide
platform: macOS
topic: null
technology: WebObjects
published: '2007-07-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Web_Applications/Introduction.html
archived_at: '2026-07-18T02:22:14.699341Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](How%20Web%20Applications%20Work.md)

# Introduction to WebObjects Web Applications Programming Guide

Web applications are a type of WebObjects application that generates HTML-based dynamic webpages accessed via a client-side web browser. Web applications are object-oriented programs written in Java. Webpages are created from templates called web components. Web components are a combination of a WOComponent Java subclass and an HTML template. You create dynamic content in your webpages by adding dynamic elements to web components and binding them to variables and methods in your application. You can create web components graphically using WebObjects Builder or indirectly using Direct to Web. If you use Direct to Web, you can also freeze components, add them to your project, and edit them using WebObjects Builder.

This document focuses on web application programming concepts and tasks. Read this document if you are developing a web application and need to learn more about programming web components, managing state in application and session objects, and using editing contexts. This document also explains how web applications work by tracing the request-response loop and explains how to create web application projects using Xcode. This document covers common tasks that web application developers need to know such as creating an EO model and deploying applications for testing.

This document contains the following articles:

- [How Web Applications Work](How%20Web%20Applications%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenryfvjvomi) describes the architecture of web applications and explains the messages invoked by the request-response loop.
- [Creating Projects](Creating%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenrzfvjvomy) explains the Xcode templates you can use to create a web application.
- [Creating Enterprise Objects](Creating%20Enterprise%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzqfvjvomi) explains how to create a simple Enterprise Objects (EO) model—the first step if you are using a back-end database to populate your webpages with dynamic content.
- [Creating Web Components](Creating%20Web%20Components.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzrfvjvomi) explains how to create and reuse web components from a programmer's perspective. This article also covers more details about the methods invoked by the request-response loop.
- [Using the Application and Session Objects](Using%20the%20Application%20and%20Session%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzsfvjvomq) explains how to use the Application and Session objects in your web application to maintain state.

If you are new to WebObjects, read [How Web Applications Work](How%20Web%20Applications%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenryfvjvomi), [Creating Projects](Creating%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenrzfvjvomy), and [Creating Enterprise Objects](Creating%20Enterprise%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzqfvjvomi) first. Also, read _[WebObjects Builder User Guide](../WebObjects%20Builder%20User%20Guide/Introduction%20to%20WebObjects%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnbq)_ for step-by-step instructions on how to create web components using WebObjects Builder. Read the rest of the articles in this document when you are ready to customize your web application and add advanced features.

For more information on related WebObjects subjects, see these documents"

- _[WebObjects Overview](../WebObjects%20Overview/Introduction%20to%20WebObjects%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamby)_ to learn about other WebObjects technologies.
- _[WebObjects Builder User Guide](../WebObjects%20Builder%20User%20Guide/Introduction%20to%20WebObjects%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnbq)_ for how to create web components graphically.
- _[WebObjects Direct to Web Guide](../WebObjects%20Direct%20to%20Web%20Guide/Introduction%20to%20WebObjects%20Direct%20to%20Web%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjv)_ for how to use Direct to Web to create a web application.
- _[WebObjects Enterprise Objects Programming Guide](../WebObjects%20Enterprise%20Objects%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjr)_ for an in depth description of Enterprise Objects.
- _WebObjects 5.3 Reference_ and for details about the WebObjects and Enterprise Objects APIs.
- _[WebObjects Deployment Guide Using JavaMonitor](../WebObjects%20Deployment%20Guide%20Using%20JavaMonitor/Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambz)_ for details on how to deploy web applications.
[Next](How%20Web%20Applications%20Work.md)

