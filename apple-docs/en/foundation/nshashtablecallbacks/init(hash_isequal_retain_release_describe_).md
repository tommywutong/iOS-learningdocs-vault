---
title: 'init(hash:isEqual:retain:release:describe:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshashtablecallbacks/init(hash:isequal:retain:release:describe:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablecallbacks/init(hash:isequal:retain:release:describe:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablecallbacks/init%28hash%3Aisequal%3Aretain%3Arelease%3Adescribe%3A%29.json'
content_hash: 'sha256:7caa521c7f87d462'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTableCallBacks](../nshashtablecallbacks.md)

# init(hash:isEqual:retain:release:describe:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(hash: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> Int)?, isEqual: ((NSHashTable<AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?, retain: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> Void)?, release: ((NSHashTable<AnyObject>, UnsafeMutableRawPointer) -> Void)?, describe: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> String?)?)
```
