---
title: streamError
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/streamerror
source_url: 'https://developer.apple.com/documentation/foundation/stream/streamerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/streamerror.json'
content_hash: 'sha256:066d0695bc77b398'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# streamError

<sub>Instance Property</sub>

Returns an `NSError` object representing the stream error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var streamError: (any Error)? { get }
```

## Return Value

An `NSError` object representing the stream error, or `nil` if no error has been encountered.

## See Also

### Getting Stream Information

- [streamStatus](streamstatus.md) — Returns the receiver’s status.
