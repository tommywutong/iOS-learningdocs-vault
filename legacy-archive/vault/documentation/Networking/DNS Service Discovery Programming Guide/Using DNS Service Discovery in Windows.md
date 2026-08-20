---
title: DNS Service Discovery Programming Guide
apple_id: TP30000964
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_api/Articles/UsingDNSServiceDiscoveryinWindows.html
archived_at: '2026-07-15T08:18:29.112005Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNS Service Discovery Programming Guide](Introduction%20to%20DNS%20Service%20Discovery.md)


[Next](Document%20Revision%20History.md)[Previous](Enumerating%20Domains.md)

# Using DNS Service Discovery in Windows

DNS Service Discovery was written with cross-platform compatibility in mind. Therefore, all of the DNS Service Discovery API calls that are valid in OS X and iOS are also valid in Windows. The difference between the two platforms lies in how each handles run loops. The next two sections will explain what changes need to be made to write programs that take advantage of DNS Service Discovery in Windows. Before reading these sections, you’ll want to become familiar with the DNS Service Discovery API and Microsoft Foundation classes, if you are not already.

To properly incorporate DNS Service Discovery in a Windows graphical user interface, use the WinSock `WSAAsyncSelect` function. The `WSAAsyncSelect` function integrates socket-based network events into the Windows message loop. To use this in your Windows code, you should first create and initialize a `DNSServiceRef` object. Then, call the function `WSAAsyncSelect` to associate your `DNSServiceRef` object’s socket with the Windows message loop. `WSAAsyncSelect` requires four arguments: a socket to your `DNSServiceRef` object, a window to receive the message, a message to be sent when the event occurs, and a bitmask for the network events you are interested in. A simple example of this is provided below. In the example, you can see how to create a `NULL` `DNSServiceRef` object, initialize that reference with `DNSServiceBrowse`, and then add it to the work loop with `WSAAsyncSelect`.

```swift
// create blank DNSServiceRef
e = new ServiceHandlerEntry;
...
// initialize the DNSServiceRef for browsing
err = DNSServiceBrowse( &e->ref, 0, 0, e->type, NULL, BrowseCallBack, e );

// add browsing to the work loop with WSAAsyncSelect
//  where m_hWnd is the window, WM_PRIVATE_SERVICE_EVENT is the message and
//  FD_READ and FD_CLOSE are bitmasks for reading and closing sockets
err = WSAAsyncSelect((SOCKET) DNSServiceRefSockFD(e->ref),
                    m_hWnd,
                    WM_PRIVATE_SERVICE_EVENT,
                    FD_READ|FD_CLOSE);
```


Creating a Windows command-line program using DNS Service Discovery is similar to creating one for OS X or iOS. Windows, like OS X and iOS, has support for the `select` system call. This function is used to determine when results are available from the DNS Service Discovery API functions. More information about using the `select` loop with DNS Service Discovery is available in [Registering and Terminating a Service](Registering%20and%20Terminating%20a%20Service.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinzyfvjvomi), [Browsing for Network Services](Browsing%20for%20Network%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobwfvjvomi), and [Resolving the Current Address of a Service](Resolving%20the%20Current%20Address%20of%20a%20Service.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobxfvjvomi).

[Next](Document%20Revision%20History.md)[Previous](Enumerating%20Domains.md)

