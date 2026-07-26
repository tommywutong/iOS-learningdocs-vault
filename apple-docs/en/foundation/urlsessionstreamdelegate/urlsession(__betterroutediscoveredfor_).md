---
title: 'urlSession(_:betterRouteDiscoveredFor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionstreamdelegate/urlsession(_:betterroutediscoveredfor:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/urlsession(_:betterroutediscoveredfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamdelegate/urlsession%28_%3Abetterroutediscoveredfor%3A%29.json'
content_hash: 'sha256:6b229889d09f4c70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamDelegate](../urlsessionstreamdelegate.md)

# urlSession(_:betterRouteDiscoveredFor:)

<sub>Instance Method</sub>

Tells the delegate that a better route to the host has been detected for the stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, betterRouteDiscoveredFor streamTask: URLSessionStreamTask)
```

## Parameters

- `session` — The session of the stream task that discovered a better route.

- `streamTask` — The stream task that discovered a better route.

## Discussion

This method is called when the URL loading system determines that a better route to the endpoint host is available. For example, this method may be called when a Wi-Fi interface becomes available.

You should consider completing pending work and creating a new stream task in order to take advantage of better routes when they become available.
