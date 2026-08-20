---
title: XML-RPC and SOAP Programming Guide
apple_id: TP30001126
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/soapXMLRPC/chapter1/soapXMLRPC_intro.html
archived_at: '2026-07-15T05:20:44.730564Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md)

# Introduction to XML-RPC and SOAP Programming Guide

_XML-RPC and SOAP Programming Guide_ describes how to use Apple Script and the Apple Event Manager in OS X to make remote procedure calls using the XML-RPC and SOAP (Simple Object Access Protocol) protocols.

_XML-RPC_ is a protocol for using XML and HTTP to make remote procedure calls over the Internet. _SOAP (Simple Object Access Protocol)_ is a remote procedure call protocol designed for exchanging information in a distributed environment, where a server may consist of a hierarchy of objects.

This book describes only how to send XML-RPC and SOAP requests, not how to serve them.

The sample code in this book can be adapted for Carbon applications, Cocoa applications, simple tools, or other code. However, there is no specific Cocoa class support provided.

To take full advantage of this document, you should be familiar with AppleScript, either through writing AppleScript scripts or creating scriptable applications. You can learn more about these topics in AppleScript Documentation. In particular, see _[AppleScript Overview](../AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_ and _[Apple Events Programming Guide](../Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

You should also be familiar with the XML-RPC and SOAP protocols. You can find information on these protocols at third-party websites. For example, the XML-RPC specification is currently described at [http://www.xmlrpc.com/spec](http://www.xmlrpc.com/spec) and the SOAP specification at [http://www.w3.org/TR/](http://www.w3.org/TR/).

This document is organized into the following chapters:

- [About AppleScript’s Support for XML-RPC and SOAP](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temjnkrifqusfiyytami) provides a brief introduction to the XML-RPC and SOAP protocols, then describes the scripting support in OS X version 10.1 (and later) for these protocols, including the syntax for script statements and the APIs for making remote procedure calls from applications or other code.
- [Making Remote Procedure Calls From Scripts](Making%20Remote%20Procedure%20Calls%20From%20Scripts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3temznkrifqusfiyytami) provides sample scripts and step by step descriptions for making XML-RPC and SOAP requests from scripts.
- [Making Remote Procedure Calls From Applications](Making%20Remote%20Procedure%20Calls%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfuxs6ylqobwgkx3smvtc6zdpmmxxk2lef4zdambqge3tenbnkrifqusfiyytami) provides sample code and step by step descriptions for making XML-RPC and SOAP requests from applications and other code.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrwfvbuqmrqguwviucykjcummjqge) describes the history of this book.

[Next](About%20AppleScript%E2%80%99s%20Support%20for%20XML-RPC%20and%20SOAP.md)

