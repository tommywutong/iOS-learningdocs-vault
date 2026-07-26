---
title: dealloc()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsproxy/dealloc()
source_url: 'https://developer.apple.com/documentation/foundation/nsproxy/dealloc()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsproxy/dealloc%28%29.json'
content_hash: 'sha256:5ddd3028b64cb5e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProxy](../nsproxy.md)

# dealloc()

<sub>Instance Method</sub>

Deallocates the memory occupied by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dealloc()
```

## Discussion

This method behaves as described in the `NSObject` class specification under the [dealloc](../../objectivec/nsobject-swift.class/dealloc.md) instance method.

## See Also

### Related Documentation

- [- finalize](<finalize().md>) — The garbage collector invokes this method on the receiver before disposing of the memory it uses.
