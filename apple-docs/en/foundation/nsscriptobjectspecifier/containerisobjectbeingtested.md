---
title: containerIsObjectBeingTested
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/containerisobjectbeingtested
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/containerisobjectbeingtested'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/containerisobjectbeingtested.json'
content_hash: 'sha256:f28326872220ecb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# containerIsObjectBeingTested

<sub>Instance Property</sub>

Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.

<sub>Mac Catalyst, macOS</sub>

```swift
var containerIsObjectBeingTested: Bool { get set }
```

## Discussion

If the receiver’s container specifier is `nil` and `flag` is [true](../../swift/true.md), sets the receiver’s container to be an object involved in a filter reference (for example, `whose color is blue`). If the receiver’s container specifier is `nil` and `flag` is [false](../../swift/false.md), sets the receiver’s container to be the top-level object.

If `flag` is [true](../../swift/true.md) [containerIsRangeContainerObject](containerisrangecontainerobject.md) should not also be invoked with an argument of [true](../../swift/true.md).

## See Also

### Getting, testing, and setting containers

- [containerClassDescription](containerclassdescription.md) — Sets the class description of the receiver’s container specifier to a given specifier.
- [containerIsRangeContainerObject](containerisrangecontainerobject.md) — Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.
- [containerSpecifier](container.md) — Sets the container specifier of the receiver.
