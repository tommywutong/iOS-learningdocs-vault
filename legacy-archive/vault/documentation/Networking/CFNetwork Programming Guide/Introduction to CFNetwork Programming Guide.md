---
title: CFNetwork Programming Guide
apple_id: TP30001132
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CFNetwork
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:13.008930Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](CFNetwork%20Concepts.md)

# Introduction to CFNetwork Programming Guide

CFNetwork is a framework in the Core Services framework that provides a library of abstractions for network protocols. These abstractions make it easy to perform a variety of network tasks, such as:

- Working with BSD sockets
- Creating encrypted connections using SSL or TLS
- Resolving DNS hosts
- Working with HTTP, authenticating HTTP and HTTPS servers
- Working with FTP servers
- Publishing, resolving and browsing Bonjour services (described in _[NSNetServices and CFNetServices Programming Guide](../NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_)

This book is intended for developers who want to use network protocols in their applications. In order to fully understand this book, the reader should have a good understanding of network programming concepts such as BSD sockets, streams and HTTP protocols. Additionally, the reader should be familiar OS X programming concepts including run loops. For more information about OS X please read _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

This book contains the following chapters:

- [CFNetwork Concepts](CFNetwork%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqnbnknltcma) describes each of the CFNetwork APIs and how they interact.
- [Working with Streams](Working%20with%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqnrnknltc) describes how to use the CFStream API to send and receive network data.
- [Communicating with HTTP Servers](Communicating%20with%20HTTP%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqnjnknlte) describes how to send and receive HTTP messages.
- [Communicating with Authenticating HTTP Servers](Communicating%20with%20Authenticating%20HTTP%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqobnknltc) describes how to communicate with secure HTTP servers.
- [Working with FTP Servers](Working%20with%20FTP%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqojnknltc) describes how to upload and download files from an FTP server, and how to download directory listings.
- [Using Network Diagnostics](Using%20Network%20Diagnostics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzsfvbuqnznknltc) describes how to add network diagnostics to your application.

For more information about the networking APIs in OS X, read:

- _Getting Started With Networking_

Refer to the following reference documents for CFNetwork:

- _CFFTPStream Reference_ is the reference documentation for the CFFTPStream API.
- _CFHTTPMessage Reference_ is the reference documentation for the CFHTTPMessage API.
- _CFHTTPStream Reference_ is the reference documentation for the CFHTTPStream API.
- _CFHTTPAuthentication Reference_ is the reference documentation for the CFHTTPAuthentication API.
- _CFHost Reference_ is the reference documentation for the CFHost API.
- _CFNetService Reference_ is the reference documentation for the CFNetServices API.
- _CFNetDiagnostics Reference_ is the reference documentation for the CFNetDiagnostics API.

In addition to the documentation provided by Apple, the following is the reference book for socket-level programming:

- _UNIX Network Programming, Volume 1_ (Stevens, Fenner and Rudoff)
[Next](CFNetwork%20Concepts.md)

