---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/error.json'
content_hash: 'sha256:e503129a5718a832'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# error

<sub>Instance Property</sub>

An error that describes the reason looping failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The value of this property is `nil` unless the looper’s [status](status-swift.property.md) changes to [AVPlayerLooperStatusFailed](status-swift.enum/failed.md). If this occurs, this property value contains an error object that provides the details of the error that prevented looping.
