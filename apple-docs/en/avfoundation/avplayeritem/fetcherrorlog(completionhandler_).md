---
title: 'fetchErrorLog(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/fetcherrorlog(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/fetcherrorlog(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/fetcherrorlog%28completionhandler%3A%29.json'
content_hash: 'sha256:55a9cd8cc8c1b3ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# fetchErrorLog(completionHandler:)

<sub>Instance Method</sub>

Asynchronously retrieves the error log without blocking the calling thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func fetchErrorLog(completionHandler: @escaping @Sendable (sending AVPlayerItemErrorLog?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var errorLog: AVPlayerItemErrorLog? { get async }
```

## Parameters

- `completionHandler` — A block that is called with the error log. May be called with nil if no logging information is available.

## Discussion

An AVPlayerItemErrorLog provides methods to retrieve the error log in a format suitable for serialization. If nil is returned then there is no logging information currently available for this AVPlayerItem.
