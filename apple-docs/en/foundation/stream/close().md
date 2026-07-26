---
title: close()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/close()
source_url: 'https://developer.apple.com/documentation/foundation/stream/close()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/close%28%29.json'
content_hash: 'sha256:1272af6d8d0da9d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# close()

<sub>Instance Method</sub>

Closes the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func close()
```

## Discussion

Closing the stream terminates the flow of bytes and releases system resources that were reserved for the stream when it was opened. If the stream has been scheduled on a run loop, closing the stream implicitly removes the stream from the run loop. A stream that is closed can still be queried for its properties.

## See Also

### Using Streams

- [- open](<open().md>) — Opens the receiving stream.
