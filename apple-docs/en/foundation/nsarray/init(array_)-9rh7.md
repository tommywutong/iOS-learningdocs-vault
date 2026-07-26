---
title: 'init(array:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/init(array:)-9rh7'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init(array:)-9rh7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28array%3A%29-9rh7.json'
content_hash: 'sha256:9ac0052180daa9f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init(array:)

<sub>Initializer</sub>

Initializes a newly allocated array by placing in it the objects contained in a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc convenience init(array anArray: NSArray)
```

## Return Value

An array initialized to contain the objects in `anArray``. The returned object might be different than the original receiver.

## Discussion

Discussion: After an immutable array has been initialized in this way, it cannot be modified.
