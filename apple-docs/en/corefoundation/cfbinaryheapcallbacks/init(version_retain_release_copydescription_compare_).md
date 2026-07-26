---
title: 'init(version:retain:release:copyDescription:compare:)'
framework: Core Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbinaryheapcallbacks/init(version:retain:release:copydescription:compare:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/init(version:retain:release:copydescription:compare:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcallbacks/init%28version%3Aretain%3Arelease%3Acopydescription%3Acompare%3A%29.json'
content_hash: 'sha256:fea9fcecc31e3168'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBinaryHeapCallBacks](../cfbinaryheapcallbacks.md)

# init(version:retain:release:copyDescription:compare:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(version: CFIndex, retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!)
```
