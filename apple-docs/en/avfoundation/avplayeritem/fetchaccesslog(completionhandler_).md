---
title: 'fetchAccessLog(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/fetchaccesslog(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/fetchaccesslog(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/fetchaccesslog%28completionhandler%3A%29.json'
content_hash: 'sha256:1fd9502568293419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# fetchAccessLog(completionHandler:)

<sub>Instance Method</sub>

Asynchronously retrieves the access log without blocking the calling thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func fetchAccessLog(completionHandler: @escaping @Sendable (sending AVPlayerItemAccessLog?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var accessLog: AVPlayerItemAccessLog? { get async }
```

## Parameters

- `completionHandler` — A block that is called with the access log. May be called with nil if no logging information is available.

## Discussion

An AVPlayerItemAccessLog provides methods to retrieve the network access log in a format suitable for serialization. If nil is returned then there is no logging information currently available for this AVPlayerItem. An AVPlayerItemNewAccessLogEntryNotification will be posted when new logging information becomes available. However, accessLog might already return a non-nil value even before the first notification is posted.
