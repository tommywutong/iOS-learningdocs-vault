---
title: Network Services Location Manager (Legacy)
apple_id: TP40000914
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSL/NSL1/NSL1.html
archived_at: '2026-07-15T08:18:15.911027Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Tasks.md)

# Introduction

The Network Services Location Manager provides a protocol-independent way for applications to discover available network services with minimal network traffic. This document describes the programming interface for the Network Services Location Manager for Mac OS X 10.2.

The following changes have been made in the Network Services Location Manager for Mac OS X 10.2:

- Instead of sending search, service registration, and service deregistration requests to Network Services Location plug-ins, the Network Services Location Manager now sends these requests to Open Directory.
- In previous versions of the Network Services Location Manager, the default neighborhoods was obtained by creating a value of type `NSLNeighborhood` whose `name` component was `NULL` and passing that `NSLNeighborhood` value as the `neighborhood` parameter to `NSLStartNeighborhoodLookup`. With this version of the Network Services Location Manager, passing `NULL` as the `neighborhood` parameter to `NSLStartNeighborhoodLookup` gets the default neighborhoods.
- To get top-level services only, you can now pass `NULL` as the `neighborhood` parameter to the `NSLStartServicesLookup` function.
- The `NSLGetNameFromNeighborhood` function now returns a null-terminated string containing the neighborhood’s name.
- When calling `NSLMakeNewNeighborhood` to create a neighborhood, you can pass `NULL` as the protocolList parameter. Passing `NULL` means that you no longer have to create a protocol list. For compatibility with earlier versions of the Network Services Location Manager, you can still create a protocol list, but searches using the resulting neighborhood are not limited to the protocols specified in the protocol list.

The Network Services Location Manager provides

- an easy way to dynamically discover traditional and non-traditional network services
- support for accepted and proposed industry standards
- a flexible, expandable architecture that can be easily leveraged by client and server applications

A wide variety of applications become easier to use when they call the Network Services Location Manager. For example,

- Instead of requiring the user to type a URL to locate a web server, a browser application that calls the Network Services Location Manager could have an “Open Location” command that polls the network for Hypertext Transfer Protocol (HTTP) servers and displays a list of HTTP universal resource locators (URLs) from which the user can select a particular URL.
- Collaboration software, such as a video-conferencing server, would register itself as an available service on the corporate Intranet. The users of client video-conferencing software could then search the Intranet for available conferences and join a particular conference without having to remember a cryptic URL or Internet Protocol (IP) address.

The Network Services Location Manager acts as an intermediary between the providers of network services and applications that want information about such services. It also registers network services that make registration requests.

You can use the Network Services Location Manager to

- add network-service search functionality to your application
- register a network service with the Network Services Location Manager so that it can be found in searches

This version the Network Services Location Manager runs only on Power PC computers on which Mac OS X is installed. Before your application calls the Network Services Location Manager, it should verify that Mac OS X is running.

If your Mac OS X application only calls `NSLStandardGetURL`, you need only link to the Carbon library. To build a Mac OS X application that calls Network Services Location Manager functions other than `NSLStandardGetURL`, link to `/System/Library/Frameworks/CoreServices.framework`.

To build an application that calls the Network Services Location Manager and that runs on both Mac OS 9 and Mac OS X, link to the Carbon library only.

The Network Services Location Manager uses Open Directory to locate network services, as shown in [Figure 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydemjufu2dgojqha).

__Figure 1-1__  Search for a network service

!

Applications that search for services can focus the search by specifying two values:

- a services list, a Network Services Location Manager data type that specifies one or more services that are to be searched for
- a neighborhood, a Network Services Location Manager data type that defines the boundaries for searches. Neighborhoods are established by administrators when they set up their networks for NBP and SLP. When an application calls the Network Services Location Manager’s `NSLStandardGetURL` function to display a dialog box that allows users to look for services, users can supplement the neighborhoods in which searches are conducted by adding neighborhoods to a list of favorite neighborhoods. Applications that don’t call `NSLStandardGetURL` call NSLStartNeighborhoodLookup to get a list of available neighborhoods.

A neighborhood is abstract information about where services may reside. In Mac OS X 10.2 and later, a neighborhood consists of one or more Open Directory “nodes.” A node can be an SLP scope, a DNS domain, an AppleTalk zone, a Windows neighborhood, or a directory published by NetInfo, LDAP, or a third-party Open Directory plug-in. The Network Services Location Manager works with Open Directory to query these nodes for information about services. The Network Services Location Manager uses nodes to abstract a consistent view of the network that can be browsed in a way that is independent of the caller.

The following steps outline the conduct of a search for a service:

1. The application creates a search request and calls the Network Services Location Manager’s `NSLStartServicesLookup` function.
2. The Network Services Location Manager receives the request and passes it to Open Directory, which passes the request to the appropriate Open Directory plug-in.
3. The Open Directory plug-in that receives the request starts to look for the requested services.
4. Providers of the requested services send their responses to the Open Directory plug-in, which makes the responses available to Open Directory.
5. Open Directory passes the responses to the Network Services Location Manager.
6. The Network Services Location Manager passes the responses to the application that called `NSLStartServiceLookup.`

Applications that provide services register themselves with the Network Services Location Manager as shown in [Figure 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydemjufu2dimbxgq) so that they can be found by applications that use their services.

__Figure 1-2__  Flow of a service registration

!

The following steps outline the flow of a service registration:

1. The application creates a value that specifies the URL to register. It may call the Network Services Location Manager utility function, `NSLHexEncodeText`, to encode portions of the URL that may contain characters (such as spaces) that are not allowed in URLs. Then the application calls the Network Services Location Manager’s `NSLStandardRegisterURL` function to register the URL. In most cases, applications pass a null value as the neighborhood. Passing a null value causes the Network Services Location Manager to register the service in the appropriate local neighborhood.
2. The Network Services Location Manager receives the request and passes it to the Open Directory SLP plug-in.
3. If the Open Directory SLP plug-in can register the URL, it returns a value indicating that the service was registered successfully, which the Network Services Location Manager passes to the calling application.

[Next](Tasks.md)

