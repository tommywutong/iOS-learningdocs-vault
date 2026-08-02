---
title: Web Services Core Programming Guide
apple_id: TP30000985
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2009-01-06'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/UsingWebservices/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:27.520871Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Web%20Services.md)

# Introduction

Web services are the interchange of XML-based queries and responses between clients and servers over the Internet or an intranet via standard protocols such as HTTP, HTTPS, or SMTP.

OS X provides support for the client side of these queries and responses, allowing your application to exchange information with remote web servers. Some support for the server side of these operations is also available, primarily the translation between CFTypes and XML for SOAP and XML-RPC protocols.

You can communicate with remote servers using Apple events or the Web Services Core framework. Support is provided for using web services from procedural C, Cocoa, or AppleScript. This document describes using the `WebServicesCore` framework from procedural C or Cocoa. For guidance on using Apple events from AppleScript, see _[XML-RPC and SOAP Programming Guide](../../Apple%20Script/XML-RPC%20and%20SOAP%20Programming%20Guide/Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrw)_.

The web services API has built-in support for SOAP 1.1, SOAP 1.2, and XML-RPC protocols. The API also supports custom serialization schemes, allowing you to work with other standards or proprietary schemes.

If you are writing an application that needs to exchange information with remote servers using XML over HTTP or HTTPS, you should read this document.

This document consists of two chapters:

- [About Web Services](About%20Web%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobvfvbuqmjqgawvgvzr)—a brief introduction to standard methods of exchanging information with remote servers and a general discussion of the web services API.
- [Using the Web Services Core Framework](Using%20the%20Web%20Services%20Core%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobvfvbuqmjqgewvgvzr)—step-by-step examples for accessing web services from a procedural C or Cocoa application using the Web Services Core framework

- _Web Services Core Reference_—the reference to the Web Services Core framework functions, callbacks, data types, constants, and error codes.
- _[XML-RPC and SOAP Programming Guide](../../Apple%20Script/XML-RPC%20and%20SOAP%20Programming%20Guide/Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrw)_—a guide to using AppleScript and Apple events to obtain access to web services.
- _[Event-Driven XML Programming Guide](../../Cocoa/Event-Driven%20XML%20Programming%20Guide/Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dm2i)_—how to use `NSXMLParser` to read in and parse XML.
- [Using SOAP with PHP](https://developer.apple.com/internet/webservices/soapphp.html)—instructions for writing SOAP clients and servers using PHP.
- [Web Services with AppleScript and PERL](https://developer.apple.com/internet/applescript/applescripttoperl.html)—A guide to using AppleScript to access web services and to creating a server using PERL.
[Next](About%20Web%20Services.md)

