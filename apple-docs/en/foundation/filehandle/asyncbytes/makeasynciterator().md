---
title: makeAsyncIterator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/asyncbytes/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/asyncbytes/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/asyncbytes/makeasynciterator%28%29.json'
content_hash: 'sha256:ca981be342eff517'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileHandle](../../filehandle.md) · [AsyncBytes](../asyncbytes.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> FileHandle.AsyncBytes.Iterator
```

## Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.
