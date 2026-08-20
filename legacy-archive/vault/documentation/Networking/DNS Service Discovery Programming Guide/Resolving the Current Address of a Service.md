---
title: DNS Service Discovery Programming Guide
apple_id: TP30000964
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_api/Articles/resolving.html
archived_at: '2026-07-15T08:18:31.362977Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNS Service Discovery Programming Guide](Introduction%20to%20DNS%20Service%20Discovery.md)


[Next](Enumerating%20Domains.md)[Previous](Browsing%20for%20Network%20Services.md)

# Resolving the Current Address of a Service

This article describes how to use [DNSServiceResolve](https://developer.apple.com/documentation/dnssd/1804744-dnsserviceresolve) to get information about a service based on its name, type, and domain.

Once you have the name, registration type, and domain of a service, you can get information about the service, such as the interface(s) on which the service is registered, the full domain name of the service, name of the host that provides the service, and the content of the service’s primary TXT record, by calling [DNSServiceResolve](https://developer.apple.com/documentation/dnssd/1804744-dnsserviceresolve).

To resolve a service name to its hostname and port, call `DNSServiceResolve`. The parameters for making this call consist of the following:

- An uninitialized service discovery reference
- The index of the interface on which you want to resolve the service; pass the value that was passed to your callback function for [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse), or `0` to resolve on all available interfaces
- The service name to be resolved; pass a value that was passed to your callback function for `DNSServiceBrowse`
- The registration type of the service to be resolved; pass the value that was passed to your callback function for `DNSServiceBrowse`
- The domain in which the service is registered; pass the value that was passed to your callback function for `DNSServiceBrowse`
- The callback function that is to be called to provide information on the success or failure of the resolution
- A user-defined context value that will be passed to the callback function when it is called, or `NULL`

If the resolution can be started, `DNSServiceResolve` initializes the service discovery reference and creates a socket that is used to communicate with the `mDNSResponder` daemon. Use the service discovery reference to call [DNSServiceRefSockFD](https://developer.apple.com/documentation/dnssd/1804698-dnsservicerefsockfd) and get the socket descriptor for the socket.

If [DNSServiceResolve](https://developer.apple.com/documentation/dnssd/1804744-dnsserviceresolve) returns error-free, you need to have `mDNSResponder` resolve the service discovery reference and run a callback function when it has received a response. There are two techniques to set up the callback function: asynchronously and synchronously.

To get a response from `mDNSResponder` asynchronously, set up a run or a `select` loop using the socket descriptor. The loop will be notified whenever a response from the `mDNSResponder` daemon becomes available. When the loop indicates that a response is available, call [DNSServiceProcessResult](https://developer.apple.com/documentation/dnssd/1804696-dnsserviceprocessresult) and pass to it the service discovery reference initialized by `DNSServiceResolve`. `DNSServiceProcessResult` will call the callback function associated with the service discovery reference. The `mDNSResponder` daemon will provide a response for each service that it resolves on a per-interface basis.

If you want to run the callback function synchronously instead of setting up a run loop or a `select` loop, you can call `DNSServiceResolve` and immediately call `DNSServiceProcessResult`. The `DNSServiceProcessResult` function will block until the `mDNSResponder` daemon has a response, at which time the callback specified when `DNSServiceResolve` was called will be invoked. This entire process should probably be run within a loop of its own for each service you wish to resolve.

In addition to the service discovery reference and flags that are not currently used, your callback will be called with the following parameters:

- The interface index on which the service was resolved; use the `if_nametoindex` family of calls to relate the index to an interface name
- An error code that indicates whether the resolution was successful; if the resolution was successful, the remaining parameters contain valid data
- The full domain name of the service, suitable for passing to special purpose functions that take a full domain name as a parameter
- The hostname of the machine that provides the service, suitable for passing to [gethostbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/gethostbyname.3.html#//apple_ref/doc/man/3/gethostbyname) or [DNSServiceQueryRecord](https://developer.apple.com/documentation/dnssd/1804747-dnsservicequeryrecord) to get the host’s IP address
- The port number in network byte order on which the service accepts connections
- The length of the TXT record for the service
- The primary TXT record for the service in standard TXT record format (that is, a length byte followed by data, followed by a length byte, followed by data, and so on)
- The user-defined context information that was passed to `DNSServiceResolve`

Your run loop or `select` loop will be notified for each interface on which the service is resolved and for each TXT record associated with the service.

When the desired results have been obtained, you must terminate the resolution. Remove the socket descriptor from the run loop or the `select` loop and call [DNSServiceRefDeallocate](https://developer.apple.com/documentation/dnssd/1804697-dnsservicerefdeallocate), passing to it the service discovery reference that was initialized when `DNSServiceResolve` was called. The service discovery reference is invalidated, and memory associated with the reference is deallocated. The socket that underlies the connection with the `mDNSResponder` daemon is closed, thereby terminating your application’s connection with the daemon.

[Next](Enumerating%20Domains.md)[Previous](Browsing%20for%20Network%20Services.md)

