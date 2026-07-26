---
title: containerIsRangeContainerObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/containerisrangecontainerobject
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/containerisrangecontainerobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/containerisrangecontainerobject.json'
content_hash: 'sha256:36e99d2577ec1f54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# containerIsRangeContainerObject

<sub>Instance Property</sub>

Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.

<sub>Mac Catalyst, macOS</sub>

```swift
var containerIsRangeContainerObject: Bool { get set }
```

## Discussion

If the receiver’s container specifier is `nil` and `flag` is [true](../../swift/true.md), sets the receiver’s container to be the container for a range specifier. If the receiver’s container specifier is `nil` and `flag` is [false](../../swift/false.md), sets the receiver’s container to be the top-level object.

If `flag` is [true](../../swift/true.md), [containerIsObjectBeingTested](containerisobjectbeingtested.md) should not also be invoked with an argument of [true](../../swift/true.md).

## See Also

### Getting, testing, and setting containers

- [containerClassDescription](containerclassdescription.md) — Sets the class description of the receiver’s container specifier to a given specifier.
- [containerIsObjectBeingTested](containerisobjectbeingtested.md) — Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.
- [containerSpecifier](container.md) — Sets the container specifier of the receiver.
