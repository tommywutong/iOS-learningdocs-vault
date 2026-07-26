---
title: 'init(domain:type:name:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservice/init(domain:type:name:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/init(domain:type:name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/init%28domain%3Atype%3Aname%3A%29.json'
content_hash: 'sha256:141b0c1cb339423a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# init(domain:type:name:)

<sub>Initializer</sub>

Returns the receiver, initialized as a network service of a given type and sets the initial host information.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(domain: String, type: String, name: String)
```

## Parameters

- `domain` — The domain for the service. To resolve in the default domains, pass in an empty string (`@""`). To limit resolution to the local domain, use `@"local."`. If you are creating this object to resolve a service whose information your app stored previously, you should set this to the domain in which the service was originally discovered. You can also use a `NSNetServiceBrowser` object to obtain a list of possible domains in which you can discover and resolve services.

- `type` — The network service type. `type` must contain both the service type and transport layer information. To ensure that the mDNS responder searches for services, as opposed to hosts, prefix both the service name and transport layer name with an underscore character (”_”). For example, to search for an HTTP service on TCP, you would use the type string “`_http._tcp.`”. Note that the period character at the end of the string, which indicates that the domain name is an absolute name, is required.

- `name` — The name of the service to resolve.

## Return Value

The receiver, initialized as a network service named `name` of type `type` in the domain `domain`.

## Discussion

This method is the appropriate initializer to use to resolve a service—to publish a service, use [- initWithDomain:type:name:port:](<init(domain_type_name_port_).md>).

If you know the values for `domain`, `type`, and `name` of the service you wish to connect to, you can create an `NSNetService` object using this initializer and call [- resolveWithTimeout:](<resolve(withtimeout_).md>) on the result.

You cannot use this initializer to publish a service. This initializer passes an invalid port number to the designated initializer, which prevents the service from being registered. Calling [- publish](<publish().md>) on an `NSNetService` object initialized with this method generates a call to your delegate’s [- netService:didNotPublish:](<../netservicedelegate/netservice(__didnotpublish_).md>) method with an [NSNetServicesBadArgumentError](errorcode-swift.enum/badargumenterror.md) error.

## See Also

### Related Documentation

- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Introduction.html#//apple_ref/doc/uid/TP40002736)
- [Bonjour Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html#//apple_ref/doc/uid/10000119i)

### Creating Network Services

- [- initWithDomain:type:name:port:](<init(domain_type_name_port_).md>) — Initializes the receiver for publishing a network service of type `type` at the socket location specified by `domain`, `name`, and `port`. _(deprecated)_
