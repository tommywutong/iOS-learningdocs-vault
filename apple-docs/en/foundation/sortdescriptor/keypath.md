---
title: keyPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/sortdescriptor/keypath
source_url: 'https://developer.apple.com/documentation/foundation/sortdescriptor/keypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortdescriptor/keypath.json'
content_hash: 'sha256:895a27541035f6f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortDescriptor](../sortdescriptor.md)

# keyPath

<sub>Instance Property</sub>

The key path to the field for comparison.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keyPath: PartialKeyPath<Compared>? { get }
```

## Discussion

This value is `nil` when `Compared` is not an NSObject
