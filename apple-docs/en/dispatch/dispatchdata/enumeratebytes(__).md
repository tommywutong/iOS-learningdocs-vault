---
title: 'enumerateBytes(_:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS, Swift 4.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/enumeratebytes(_:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/enumeratebytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/enumeratebytes%28_%3A%29.json'
content_hash: 'sha256:d7192edb4f0f0f5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# enumerateBytes(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateBytes(_ block: (UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)
```

## See Also

### Iterating Over the Buffer Contents

- [makeIterator()](<makeiterator().md>)
