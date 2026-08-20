---
title: DNS Service Discovery Programming Guide
apple_id: TP30000964
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_api/Introduction.html
archived_at: '2026-07-15T08:18:31.374810Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Registering%20and%20Terminating%20a%20Service.md)

# Introduction to DNS Service Discovery

This document describes how to use the DNS Service Discovery API in your program.

The DNS Service Discovery API helps you to perform three main tasks:

- Registering a service
- Browsing for services
- Resolving service names to host names

In support of these main tasks, this API can directly assist you in performing two subsidiary tasks:

- Enumerating domains (finding recommended service domains)
- Updating registrations (changing your DNS registration data dynamically)

The DNS Service Discovery API is part of Bonjour, Apple’s implementation of zero-configuration networking (ZEROCONF). For an overview of how Bonjour works, please read _[Bonjour Overview](../../Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i)_ prior to using DNS Service Discovery.

This document is meant for developers who want to use Bonjour in their applications. There are a number of reasons to use the DNS Service Discovery API over the Network Services APIs (NSNetServices and CFNetServices):

- You are writing BSD-style applications that will not need to link to higher level frameworks.
- You are writing cross-platform programs (DNS Service Discovery API is available on iOS, OS X, Windows, and other POSIX compatible operating systems).
- You are writing an application that requires special purpose low-level routines, such as registering individual records or being able to use only specific network interfaces.

If none of those features are necessary for your program, it is highly recommended that you take a look at NSNetService and CFNetService first.

This document contains the following articles:

- [Registering and Terminating a Service](Registering%20and%20Terminating%20a%20Service.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinzyfvjvomi) explains how to register and terminate your service with the `mDNSResponder` daemon.
- [Browsing for Network Services](Browsing%20for%20Network%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobwfvjvomi) describes how to browse for services.
- [Resolving the Current Address of a Service](Resolving%20the%20Current%20Address%20of%20a%20Service.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobxfvjvomi) explains how to get information on a service based on its name, registration type, and domain.
- [Enumerating Domains](Enumerating%20Domains.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobyfvjvomi) helps you understand how to find domains recommended for registration and browsing.
- [Using DNS Service Discovery in Windows](Using%20DNS%20Service%20Discovery%20in%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobqfvjvomi) gives an overview for how to implement DNS Service Discovery in a Windows-based application.

The next few paragraphs describe some things you should know about this API before attempting any of the tasks.

Most functions in this API do not return all of their data using their function return or parameter block. Instead, they require you to provide a callback function that can handle data sent asynchronously.

Your callback function may be called multiple times in response to a single function call on your part. For example, you might request a list of available services. Your callback would be called once for each available service that matches your request, then called again whenever a matching service is added or removed.

Some functions return error codes in the usual way, but many do not. In these cases, any error code and status flags are sent to your callback function as part of the asynchronous reply, along with—or instead of—any returned data.

Most of the functions in this API use a common set of parameters to describe services. You will need to supply some or all of these parameters, depending on the purpose of your call. In many cases, you will provide some parameters, such as the domain and type of service, and your callback function will receive data corresponding to other parameters, such as the service name of a matching service.

Here is a list of the common parameters required by the DNS Service Discovery API:

- Name—human readable name of the service, such as `Sales Laser Printer`.
- Registration type—the service type followed by the protocol name and separated by a dot (`.`) ; `_printer._tcp` is an example.
- Domain—the domain for the service, typically `NULL`.

- Full domain name—the name that uniquely identifies a service. A full domain name is the concatenation of the name, registration type, and domain. Because the dot (`.`) character is used as a separator, any dot characters in the name portion of a full domain name must be escaped by a backslash character (`\`). If the name contains a literal backslash, the backslash must also be escaped by a backslash character. Here is an example of a full domain name: `Dr\.Smith’s Home\\Office Server._http._tcp.local`.
- Port—the port number for the service in network byte order.
- Text record—an optional record containing any additional information that may be needed to use the service, such as a print queue name.

The DNS Service Discovery API requires the services of the `mDNSResponder` daemon. OS X (version 10.2 and later) and iOS include an `mDNSResponder` daemon as part of the operating system. Apple also provides the source code for its `mDNSResponder` daemon on [Apple's Open Source site](http://opensource.apple.com/). This API is also available in Bonjour for Windows and (if `mDNSResponder` is installed) in the Linux, Solaris, and FreeBSD operating systems.

The DNS Service Discovery API does not perform network access setup for services. Similarly, the DNS Service Discovery API does not provide a network connection from an application to a service. It allows applications to browse for services, or to ask for them by name, and provides the IP address, port, and so on. You can use BSD sockets to connect to a service over the network.

For additional information on Bonjour, including links to standards, specifications, and resources, see [http://developer.apple.com/networking/bonjour](https://developer.apple.com/networking/bonjour) and read _[Bonjour Overview](../../Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i)_.

Documentation on the Java-based DNS Service Discovery API is available at _DNS Service Discovery Java Reference_.

For information on dynamic update and shared secrets, see [http://www.ietf.org/rfc/rfc2136.txt](http://www.ietf.org/rfc/rfc2136.txt) and [http://www.ietf.org/rfc/rfc2845.txt](http://www.ietf.org/rfc/rfc2845.txt), respectively.

For information Network Address Translation (NAT), see [http://www.ietf.org/rfc/rfc3022.txt](http://www.ietf.org/rfc/rfc3022.txt), and for information on automatic NAT port mapping, see [http://files.dns-sd.org/draft-nat-port-mapping.txt](http://files.dns-sd.org/draft-nat-port-mapping.txt).

For sample code, download the `mDNSResponder` source code at [Apple's Open Source site](http://opensource.apple.com/).

[Next](Registering%20and%20Terminating%20a%20Service.md)

