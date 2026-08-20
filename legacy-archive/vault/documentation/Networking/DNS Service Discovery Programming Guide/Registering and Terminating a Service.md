---
title: DNS Service Discovery Programming Guide
apple_id: TP30000964
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_api/Articles/registering.html
archived_at: '2026-07-15T08:18:30.906311Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNS Service Discovery Programming Guide](Introduction%20to%20DNS%20Service%20Discovery.md)


[Next](Browsing%20for%20Network%20Services.md)[Previous](Introduction%20to%20DNS%20Service%20Discovery.md)

# Registering and Terminating a Service

When your service starts up, you need to register with the `mDNSResponder` daemon so that applications can discover your service. This section provides a general overview of the process, followed by a set of step-by-step instructions.

To register your service, call [DNSServiceRegister](https://developer.apple.com/documentation/dnssd/1804733-dnsserviceregister). The parameters for making this call consist of the following:

- An uninitialized service discovery reference.
- The index for the interface on which you want to register your service; pass `0` to register on all available interfaces, pass `–1` to register on the local machine only (your service will not be available to remote hosts), or pass the number that represents the interface on which you want to register (use the `if_nametoindex` family of calls to get the number).
- Flags that indicate how you want to handle name conflicts. By default, `(`_n_`)` is automatically appended to your service name, where _n_ is a number, if a name conflict occurs. To override this behavior, set the [kDNSServiceFlagsNoAutoRename](https://developer.apple.com/documentation/dnssd/1823436-anonymous/kdnsserviceflagsnoautorename) flag, which will cause your registration callback function to be called so that you can handle name conflicts. The `kDNSServiceFlagsNoAutoRename` flag is only valid if you also explicitly specify a service name.
- The service’s name; you can specify `NULL` to use the computer’s name as the service’s name.
- The service’s registration type.
- The SRV target host name; usually, you’ll pass `NULL` to use the computer’s default host name. Passing `NULL` is the desired behavior in almost every case. However, proxy applications may pass an explicit SRV target other than the computer's host name.
- The port number in network byte order on which the service accepts connections. Passing `0` for the port registers a placeholder service. With a placeholder service, the service will not be discovered by browsing, but a name conflict will occur if another client tries to register the same name. Most applications do not need to use placeholder service.
- The callback function that is to be called to provide information on the success or failure of the registration, or `NULL`.
- A user-defined context value that will be passed to the callback function when it is called, or `NULL`.

Services that require TXT records also pass the raw data of the TXT record and the length of the raw data as parameters. Most services don’t need TXT records and therefore pass `NULL` and `0`, respectively, for these parameters.

Instead of providing a callback function, you may pass `NULL`, in which case, you will not be notified of default values that may be chosen on your behalf and you will not be notified of any asynchronous errors that may prevent the registration of your service. If you pass `NULL` for this parameter, you cannot pass [kDNSServiceFlagsNoAutoRename](https://developer.apple.com/documentation/dnssd/1823436-anonymous/kdnsserviceflagsnoautorename) as the flag parameter. You can de-register a service that is registered without a callback function in the normal way, by calling [DNSServiceRefDeallocate](https://developer.apple.com/documentation/dnssd/1804697-dnsservicerefdeallocate).

If the registration can be started, [DNSServiceRegister](https://developer.apple.com/documentation/dnssd/1804733-dnsserviceregister) initializes the service discovery reference and creates a socket that is used to communicate with the `mDNSResponder` daemon. Use the service discovery reference to call [DNSServiceRefSockFD](https://developer.apple.com/documentation/dnssd/1804698-dnsservicerefsockfd) and get the socket descriptor for the service reference.

Set up a run or `select` loop using the socket descriptor. When the loop indicates that the `mDNSResponder` daemon’s reply is available, call [DNSServiceProcessResult](https://developer.apple.com/documentation/dnssd/1804696-dnsserviceprocessresult) and pass to it the service discovery reference initialized by `DNSServiceRegister`. `DNSServiceProcessResult` will call the callback function associated with the service discovery reference.

Instead of setting up a run loop or a `select` loop, you can call `DNSServiceRegister` and immediately call `DNSServiceProcessResult`. The `DNSServiceProcessResult` function will block until the `mDNSResponder` daemon has a response, at which time the callback specified when `DNSServiceRegister` was called (if any) will be invoked.

In addition to the service discovery reference and flags that are not currently used, your callback will be called with the following parameters:

- An error code that indicates whether the registration was successful; if the registration was successful, the remaining parameters contain valid data
- The service’s name as passed to `DNSServiceRegister` or the name that was chosen if `NULL` was passed to `DNSServiceRegister` as the service’s name
- The registration type as passed to `DNSServiceRegister`
- The domain in which the service was registered
- The user-defined context information that was passed to `DNSServiceRegister`

If the combination of service name, registration type, and domain name resulted in a full domain name that is already in local use and you specified `kDNSServiceFlagsNoAutoRename`, you’ll need to deallocate the service discovery reference, choose another service name and try again, until a locally unique name can be registered.

Upon successful registration, your service is announced to the local network and its access information (IP address, port, and so on) can be found using multicast DNS, either by name or by browsing for services. Using the initialized service discovery reference, you can communicate with the `mDNSResponder` daemon to add a record to the registration information for your service, update an added record, or remove an added record while your service is running. However, you will probably never need to make changes to your registration information because Bonjour handles the common cases, such as waking, sleeping, shutting down, and changing IP addresses.

A rare exception would be the need to update the text record associated with a service. If a text field contains a queue name, for example, and the queue name changes, you would need to update the text record for the service.

You must keep the socket descriptor on the run loop or the `select` loop as long as you expect your callback function to be called.

To terminate your service's registration, remove the socket descriptor from the run loop or the `select` loop and call [DNSServiceRefDeallocate](https://developer.apple.com/documentation/dnssd/1804697-dnsservicerefdeallocate), passing to it the service discovery reference that was initialized when your service was registered. In addition to invalidating the service discovery reference and deallocating the memory associated with it, any resource records that have been added are de-registered and their references are invalidated. The socket that underlies the connection with the `mDNSResponder` daemon is closed, thereby terminating your application’s connection with the daemon.

[Next](Browsing%20for%20Network%20Services.md)[Previous](Introduction%20to%20DNS%20Service%20Discovery.md)

