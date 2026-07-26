---
title: 'init(hash:isEqual:retain:release:describe:notAKeyMarker:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmaptablekeycallbacks/init(hash:isequal:retain:release:describe:notakeymarker:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks/init(hash:isequal:retain:release:describe:notakeymarker:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablekeycallbacks/init%28hash%3Aisequal%3Aretain%3Arelease%3Adescribe%3Anotakeymarker%3A%29.json'
content_hash: 'sha256:66bcf79345bf5fc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTableKeyCallBacks](../nsmaptablekeycallbacks.md)

# init(hash:isEqual:retain:release:describe:notAKeyMarker:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(hash: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Int)?, isEqual: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?, retain: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Void)?, release: ((NSMapTable<AnyObject, AnyObject>, UnsafeMutableRawPointer) -> Void)?, describe: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> String?)?, notAKeyMarker: UnsafeRawPointer?)
```
