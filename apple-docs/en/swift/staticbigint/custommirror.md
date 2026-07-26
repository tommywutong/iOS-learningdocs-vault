---
title: customMirror
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticbigint/custommirror
source_url: 'https://developer.apple.com/documentation/swift/staticbigint/custommirror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticbigint/custommirror.json'
content_hash: 'sha256:fdfa53ea809cd913'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticBigInt](../staticbigint.md)

# customMirror

<sub>Instance Property</sub>

The custom mirror for this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var customMirror: Mirror { get }
```

## Discussion

If this type has value semantics, the mirror should be unaffected by subsequent mutations of the instance.
