---
title: DNS Service Discovery Programming Guide
apple_id: TP30000964
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_api/Articles/enumeratingdomains.html
archived_at: '2026-07-15T08:18:30.257698Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNS Service Discovery Programming Guide](Introduction%20to%20DNS%20Service%20Discovery.md)


[Next](Using%20DNS%20Service%20Discovery%20in%20Windows.md)[Previous](Resolving%20the%20Current%20Address%20of%20a%20Service.md)

# Enumerating Domains

The [DNSServiceEnumerateDomains](https://developer.apple.com/documentation/dnssd/1804754-dnsserviceenumeratedomains) function finds domains that are recommended for registration and browsing. Each time your callback is called, information about one domain is provided, along with flags indicating whether to add or remove the domain from your list of domains or indicating that the domain is a default domain, or is no longer the default domain.

The parameters for calling `DNSServiceEnumerateDomains`consist of the following:

- An uninitialized service discovery reference
- A flag that indicates whether you want to enumerate recommended browsing or registration domains
- An interface index that specifies the interface to enumerate; pass `0` to enumerate domains on all interfaces or a positive integer to specify the interface on which to enumerate domains (use the `if_nametoindex` family of calls to get the index of the interface you want to enumerate)
- The callback function that is to be called to provide information on the success or failure of the enumeration
- A user-defined context value that will be passed to the callback function when it is called, or `NULL`

If the enumeration can be started, `DNSServiceEnumerateDomains` initializes the service discovery reference and creates a socket that is used to communicate with the `mDNSResponder` daemon. Use the service discovery reference to call [DNSServiceRefSockFD](https://developer.apple.com/documentation/dnssd/1804698-dnsservicerefsockfd) and get the socket descriptor for the socket.

Set up a run loop or a `select` loop using the socket descriptor. When the loop indicates that a response from the `mDNSResponder` daemon is available, call [DNSServiceProcessResult](https://developer.apple.com/documentation/dnssd/1804696-dnsserviceprocessresult) and pass to it the service discovery reference initialized by `DNSServiceEnumerateDomains`. `DNSServiceProcessResult` will call the callback function associated with the service discovery reference.

Instead of setting up a run or `select` loop, you can call `DNSServiceEnumerate` and immediately call `DNSServiceProcessResult`. The `DNSServiceProcessResult` function will block until the `mDNSResponder` daemon has a response, at which time the callback specified when `DNSServiceEnumerate` was called will be invoked.

Your callback will be called with the following parameters:

- The service discovery reference that was passed to `DNSServiceEnumerateDomains`
- Flags that indicate whether your callback will be called again immediately to pass information about another domain that has been found, whether to add or remove this domain from the list that your application maintains, and whether to add or remove the domain as a default domain
- The index of the interface on which the domain was found
- An error code that indicates whether the enumeration was successful; if the enumeration was successful, the other parameters contain valid data
- The name of the domain that was found
- The user-defined context information that was passed to `DNSServiceEnumerateDomains`

The run loop or the `select` loop will be notified for each recommended domain enumerated on per-interface basis and whenever a domain is added or removed. You are responsible for assembling the daemon’s responses into a list of current recommended domains.

To terminate the enumeration, remove the socket descriptor from the run loop or the `select` loop and call [DNSServiceRefDeallocate](https://developer.apple.com/documentation/dnssd/1804697-dnsservicerefdeallocate), passing to it the service discovery reference that was initialized when `DNSServiceEnumerateDomains` was called. The service discovery reference is invalidated, and memory associated with the reference is deallocated. The socket that underlies the connection with the `mDNSResponder` daemon is closed, thereby terminating your application’s connection with the daemon.

[Next](Using%20DNS%20Service%20Discovery%20in%20Windows.md)[Previous](Resolving%20the%20Current%20Address%20of%20a%20Service.md)

