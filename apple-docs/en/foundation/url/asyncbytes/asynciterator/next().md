---
title: next()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/asyncbytes/asynciterator/next()
source_url: 'https://developer.apple.com/documentation/foundation/url/asyncbytes/asynciterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/asyncbytes/asynciterator/next%28%29.json'
content_hash: 'sha256:8f2aedec6435d999'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [URL](../../../url.md) · [AsyncBytes](../../asyncbytes.md) · [AsyncIterator](../asynciterator.md)

# next()

<sub>Instance Method</sub>

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws -> UInt8?
```

## Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.
