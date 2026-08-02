---
title: Networking Programming Topics
apple_id: TP40012488
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Articles/ResolvingDNSHostnames.html
archived_at: '2026-07-15T08:18:51.150437Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Networking Programming Topics](Introduction.md)


[Next](Overriding%20TLS%20Chain%20Validation%20Correctly.md)[Previous](Using%20Sockets%20and%20Socket%20Streams.md)

# Resolving DNS Hostnames

This article explains how to resolve a DNS hostname in a way that offers you maximum flexibility.

There are three primary APIs in OS X and iOS for resolving hostnames: `NSHost` (only in OS X), `CFHost`, and the POSIX resolver API.

- NSHost—Although passing `NSHost` is a common way to pass hostnames to other APIs, using `NSHost` to resolve addresses yourself is generally discouraged because it is a synchronous API. Thus, using it on the main thread can cause serious performance degradation. Because this API is discouraged, its use is not described here.
- CFHost—The `CFHost` API allows you to perform resolution asynchronously, and is the preferred way to resolve hostnames if you must resolve them yourself.
- POSIX—The POSIX layer provides several functions for resolving hostnames. These functions should be used only if you are writing portable code that must be shared with non-Apple platforms or if you are integrating your code with existing POSIX networking code.

To resolve a host with `CFHost`:

1. Create a [CFHostRef](https://developer.apple.com/documentation/cfnetwork/cfhostref) object by calling [CFHostCreateWithName](https://developer.apple.com/documentation/cfnetwork/1426488-cfhostcreatewithname).
2. Call [CFHostSetClient](https://developer.apple.com/documentation/cfnetwork/1426540-cfhostsetclient) and provide the context object of your choice and a callback function that will be called when resolution completes.
3. Call [CFHostScheduleWithRunLoop](https://developer.apple.com/documentation/cfnetwork/1426596-cfhostschedulewithrunloop) to schedule the resolver on your run loop.
4. Call [CFHostStartInfoResolution](https://developer.apple.com/documentation/cfnetwork/1426672-cfhoststartinforesolution) to tell the resolver to start resolving, passing [kCFHostAddresses](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype/kcfhostaddresses) as the second parameter to indicate that you want it to return IP addresses.
5. Wait for the resolver to call your callback. Within your callback, obtain the results by calling [CFHostGetAddressing](https://developer.apple.com/documentation/cfnetwork/1426861-cfhostgetaddressing). This function returns an array of [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) objects, each of which contains a POSIX `sockaddr` structure.

The process for reverse name resolution (translating an IP address into a hostname) is similar, except that you call [CFHostCreateWithAddress](https://developer.apple.com/documentation/cfnetwork/1426421-cfhostcreatewithaddress) to create the object, pass [kCFHostNames](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype/kcfhostnames) to [CFHostStartInfoResolution](https://developer.apple.com/documentation/cfnetwork/1426672-cfhoststartinforesolution), and call [CFHostGetNames](https://developer.apple.com/documentation/cfnetwork/1426909-cfhostgetnames) to retrieve the results.

If you intend to use POSIX calls to resolve hostnames, be aware that these calls are synchronous and should not be used on the main thread in a GUI app. Instead, you should either create a separate POSIX thread or a GCD task and perform these calls within that context.

POSIX defines three functions in `<netdb.h>` for resolving hostnames:

__[getaddrinfo](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getaddrinfo.3.html#//apple_ref/doc/man/3/getaddrinfo)__: Returns all the resolved addresses for a given hostname. This function is the preferred way to obtain address information at the POSIX level. You can find sample code in its man page (linked above).

__Important:__ Some older DNS servers do not reply to IPv6 lookup requests with an error. The POSIX `getaddrinfo` function attempts to hide this misbehavior by canceling outstanding IPv6 queries shortly after receiving a successful IPv4 reply. If your app would benefit from continuing to receive IPv6 addresses until you connect successfully (rather than stopping as soon as you have an IPv4 address that might or might not work), then you should use an asynchronous API such as `CFHost`.

__[gethostbyname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/gethostbyname.3.html#//apple_ref/doc/man/3/gethostbyname)__: Returns a single IPv4 address for a given hostname. This function is discouraged for new development because it is limited to IPv4 addresses.

__[gethostbyname2](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/gethostbyname2.3.html#//apple_ref/doc/man/3/gethostbyname2)__: Returns a single address for a given hostname in the specified address family (`AF_INET`, `AF_INET6`, and so on).

Although this function allows you to get around the IPv4 limitations of `gethostbyname`, it still limits your ability to try multiple addresses at once and choose the fastest one. Thus, this function is primarily intended as a nearly drop-in replacement for `gethostbyname` in existing code. The `getaddrinfo` is preferred for use in new code.

For reverse name resolution (translating an IP address into a hostname), POSIX provides [getnameinfo](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getnameinfo.3.html#//apple_ref/doc/man/3/getnameinfo) and [gethostbyaddr](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/gethostbyaddr.3.html#//apple_ref/doc/man/3/gethostbyaddr). The `getnameinfo` function is preferred because it is more flexible.

To learn more about these functions, read their respective man pages, linked above.

[Next](Overriding%20TLS%20Chain%20Validation%20Correctly.md)[Previous](Using%20Sockets%20and%20Socket%20Streams.md)

