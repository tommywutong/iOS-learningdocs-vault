---
title: 'setDelegate(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachport/setdelegate(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/setdelegate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/setdelegate%28_%3A%29.json'
content_hash: 'sha256:849da2317dea9434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# setDelegate(_:)

<sub>Instance Method</sub>

Sets the receiver’s delegate to a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDelegate(_ anObject: (any NSMachPortDelegate)?)
```

## Parameters

- `anObject` — The delegate for the receiver.

## See Also

### Getting and Setting the Delegate

- [- delegate](<delegate().md>) — Returns the receiver’s delegate.
