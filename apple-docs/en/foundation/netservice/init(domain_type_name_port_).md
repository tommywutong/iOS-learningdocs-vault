---
title: 'init(domain:type:name:port:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservice/init(domain:type:name:port:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/init(domain:type:name:port:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/init%28domain%3Atype%3Aname%3Aport%3A%29.json'
content_hash: 'sha256:276ad53d5f38a596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# init(domain:type:name:port:)

<sub>Initializer</sub>

Initializes the receiver for publishing a network service of type `type` at the socket location specified by `domain`, `name`, and `port`.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(domain: String, type: String, name: String, port: Int32)
```

## Parameters

- `domain` — The domain for the service. To use the default registration domains, pass in an empty string (`@""`). To limit registration to the local domain, use `@"local."`. You can also use a `NSNetServiceBrowser` object to obtain a list of possible domains in which you can publish your service.

- `type` — The network service type. `type` must contain both the service type and transport layer information. To ensure that the mDNS responder searches for services, as opposed to hosts, prefix both the service name and transport layer name with an underscore character (”_”). For example, to search for an HTTP service on TCP, you would use the type string “`_http._tcp.`”. Note that the period character at the end of the string, which indicates that the domain name is an absolute name, is required.

- `name` — The name by which the service is identified to the network. The name must be unique. If you pass the empty string (`@""`), the system automatically advertises your service using the computer name as the service name.

- `port` — The port on which the service is published. If you specify the `NSNetServiceListenForConnections` flag, you may pass zero (`0`), in which case the service automatically allocates an arbitrary (ephemeral) port for your service. When the delegate’s [- netServiceDidPublish:](<../netservicedelegate/netservicedidpublish(__).md>) is called, you can determine the actual port chosen by calling the service object’s [NetService](../netservice.md) method or accessing the corresponding property. If your app is listening for connections on its own, the value of `port` must be a port number acquired by your application for the service.

## Discussion

You use this method to create a service that you wish to publish on the network. Although you can also use this method to create a service you wish to resolve on the network, it is generally more appropriate to use the [- initWithDomain:type:name:](<init(domain_type_name_).md>) method instead.

When publishing a service, you must provide valid arguments in order to advertise your service correctly. If the host computer has access to multiple registration domains, you must create separate `NSNetService` objects for each domain. If you attempt to publish in a domain for which you do not have registration authority, your request may be denied.

It is acceptable to use an empty string for the `domain` argument when publishing or browsing a service, but do not rely on this for resolution.

This method is the designated initializer.

## See Also

### Creating Network Services

- [- initWithDomain:type:name:](<init(domain_type_name_).md>) — Returns the receiver, initialized as a network service of a given type and sets the initial host information. _(deprecated)_
