---
title: streamStatus
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/streamstatus
source_url: 'https://developer.apple.com/documentation/foundation/stream/streamstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/streamstatus.json'
content_hash: 'sha256:8e89b5d47f323eb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# streamStatus

<sub>Instance Property</sub>

Returns the receiver’s status.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var streamStatus: Stream.Status { get }
```

## Return Value

The receiver’s status.

## Discussion

See Constants for a description of the available NSStreamStatus constants.

## See Also

### Getting Stream Information

- [streamError](streamerror.md) — Returns an `NSError` object representing the stream error.
