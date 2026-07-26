---
title: finalize()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsproxy/finalize()
source_url: 'https://developer.apple.com/documentation/foundation/nsproxy/finalize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsproxy/finalize%28%29.json'
content_hash: 'sha256:b12edf553050de74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProxy](../nsproxy.md)

# finalize()

<sub>Instance Method</sub>

The garbage collector invokes this method on the receiver before disposing of the memory it uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finalize()
```

## Discussion

This method behaves as described in the `NSObject` class specification under the [finalize()](<../../objectivec/nsobject-swift.class/finalize().md>) instance method. Note that a `finalize` method must be thread-safe.

## See Also

### Related Documentation

- [- dealloc](<dealloc().md>) — Deallocates the memory occupied by the receiver.
