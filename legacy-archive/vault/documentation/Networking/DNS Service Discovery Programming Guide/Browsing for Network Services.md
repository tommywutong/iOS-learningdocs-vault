---
title: DNS Service Discovery Programming Guide
apple_id: TP30000964
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_api/Articles/browse.html
archived_at: '2026-07-15T08:18:29.752968Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNS Service Discovery Programming Guide](Introduction%20to%20DNS%20Service%20Discovery.md)


[Next](Resolving%20the%20Current%20Address%20of%20a%20Service.md)[Previous](Registering%20and%20Terminating%20a%20Service.md)

# Browsing for Network Services

Browsing for services using this API is fairly simple. You can find out what services of a given type are available in a given domain with a single function call.

To browse for available services, call [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse). The parameters for making this call consist of the following:

- An uninitialized service discovery reference.
- The index for the interface you want to browse; pass `0` to browse all available interfaces, pass `–1` to browse for services on the local host only, or pass the number that represents the interface you want to browse (use the `if_nametoindex` family of calls to get the number).
- The registration type of the service you want to browse; the registration type is the service type followed by a dot, followed by the protocol (for example, `_printer._tcp`).
- The domain to browse; pass `NULL` to browse the domain(s) specified by the user as acceptable for browsing or pass a domain name to only browse that domain.
- The callback function that is to be called to provide information on the success or failure of the browse and to provide search results, such as a service that has been found or a service that is no longer available.
- A user-defined context value that will be passed to the callback function when it is called, or `NULL`.

If the browse can be started, `DNSServiceBrowse` initializes the service discovery reference and creates a socket that is used to communicate with the `mDNSResponder` daemon. Use the service discovery reference to call [DNSServiceRefSockFD](https://developer.apple.com/documentation/dnssd/1804698-dnsservicerefsockfd) and get the socket descriptor for the socket.

Use the socket descriptor to set up a run loop or a `select` loop that will indicate when a response from the `mDNSResponder` daemon becomes available. The response may indicate that a service instance matching the specified type, domain, and interface has been found or that a service instance that was previously found is no longer available. When the loop indicates that the `mDNSResponder` daemon has responded, call [DNSServiceProcessResult](https://developer.apple.com/documentation/dnssd/1804696-dnsserviceprocessresult) and pass to it the service discovery reference initialized by `DNSServiceBrowse`. `DNSServiceProcessResult` will call the callback function associated with the service discovery reference.

Your callback will be called with the following parameters:

- The service discovery reference that was initialized by `DNSServiceBrowse`.
- Flags that provide information about a service that has been found or that is no longer available and browsing status. For example, [kDNSServiceFlagsAdd](https://developer.apple.com/documentation/dnssd/1823436-anonymous/kdnsserviceflagsadd) indicates that the service parameter contains the name of a service that has been found; you should add it to your list of available services. If `kDNSServiceFlagsAdd` is not set, the service specified by the service parameter is no longer available and should be removed from your list of available services. Browsing status is indicated by the [kDNSServiceFlagsMoreComing](https://developer.apple.com/documentation/dnssd/1823436-anonymous/kdnsserviceflagsmorecoming) flag. When it is set, your callback function will be called again immediately, so you should not update your user interface. When `kDNSServiceFlagsMoreComing` is not set, your callback function will not be called again immediately, so you have time to update your user interface.
- The index of the interface on which the service was discovered.
- An error code that indicates whether browsing was successful; if browsing was successful, the remaining parameters contain valid data.
- The name of the service that was found, if browsing was successful.
- The registration type, if browsing was successful.
- The domain in which the service was discovered, if browsing was successful.
- The user-defined context information that was passed to [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse).

To browse in multiple domains, or for multiple service types, call [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse) for each domain and service type of interest. Your application is responsible for keeping track of the responses.

If your application needs to leave the browser interface visible the entire time your application is running, as iTunes and iChat do, then you typically will call `DNSServiceBrowse` once per session. Whenever a new service becomes available or an existing service becomes unavailable, data is sent to your callback function, so you can simply leave the callback active, and your list of services will always be up to date. This information typically changes infrequently, so the callback usually does not use much CPU time.

However, if you application does not need to constantly show the list of available services, in a situation such as the printer dialog, then you should call `DNSServiceBrowse` and terminate the browsing when you are finished.

When you call [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse), it initializes a service discovery reference and opens a socket-based connection with the `mDNSResponder` daemon. For this reason, if you choose to deactivate your callback and repeat the search as needed, be sure to call [DNSServiceRefDeallocate](https://developer.apple.com/documentation/dnssd/1804697-dnsservicerefdeallocate) to deallocate the reference before calling `DNSServiceBrowse` again. Otherwise, you will leak memory and sockets for every search.

The actual IP address and port of a given service instance will change more frequently than the service name. Each time you use the service, you should resolve the current address of a service instance just prior to using the service. See the next section, [Resolving the Current Address of a Service](Resolving%20the%20Current%20Address%20of%20a%20Service.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobxfvjvomi).

To terminate browsing, remove the socket descriptor from the run loop or the `select` loop and call [DNSServiceRefDeallocate](https://developer.apple.com/documentation/dnssd/1804697-dnsservicerefdeallocate), passing to it the service discovery reference that was initialized when [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse) was called. Browsing is halted, the service discovery reference is invalidated, and memory associated with the reference is deallocated. The socket that underlies the connection with the `mDNSResponder` daemon is closed, thereby terminating your application’s connection with the daemon.

[Next](Resolving%20the%20Current%20Address%20of%20a%20Service.md)[Previous](Registering%20and%20Terminating%20a%20Service.md)

