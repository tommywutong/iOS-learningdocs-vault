---
title: 'netService(_:didAcceptConnectionWith:outputStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicedelegate/netservice(_:didacceptconnectionwith:outputstream:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicedelegate/netservice(_:didacceptconnectionwith:outputstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicedelegate/netservice%28_%3Adidacceptconnectionwith%3Aoutputstream%3A%29.json'
content_hash: 'sha256:c31772a4db457363'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceDelegate](../netservicedelegate.md)

# netService(_:didAcceptConnectionWith:outputStream:)

<sub>Instance Method</sub>

Called when a client connects to a service managed by Bonjour.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netService(_ sender: NetService, didAcceptConnectionWith inputStream: InputStream, outputStream: OutputStream)
```

## Parameters

- `sender` — The net service object that the client connected to.

- `inputStream` — A stream object for receiving data from the client.

- `outputStream` — A stream object for sending data to the client.

## Discussion

When you publish a service, if you set the [NSNetServiceListenForConnections](../netservice/options/listenforconnections.md) flag in the service options, the service object accepts connections on behalf of your app. Later, when a client connects to that service, the service object calls this method to provide the app with a pair of streams for communicating with that client.
