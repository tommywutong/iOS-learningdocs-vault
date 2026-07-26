---
title: container
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/container
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/container'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/container.json'
content_hash: 'sha256:a0f02044b4f63045'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# container

<sub>Instance Property</sub>

Sets the container specifier of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var container: NSScriptObjectSpecifier? { get set }
```

## Parameters

- `objSpecifier` — The container specifier for the receiver.

## See Also

### Getting, testing, and setting containers

- [containerClassDescription](containerclassdescription.md) — Sets the class description of the receiver’s container specifier to a given specifier.
- [containerIsObjectBeingTested](containerisobjectbeingtested.md) — Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.
- [containerIsRangeContainerObject](containerisrangecontainerobject.md) — Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.
