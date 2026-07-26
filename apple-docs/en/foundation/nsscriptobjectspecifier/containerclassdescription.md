---
title: containerClassDescription
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/containerclassdescription
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/containerclassdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/containerclassdescription.json'
content_hash: 'sha256:f6b90384e89bebff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# containerClassDescription

<sub>Instance Property</sub>

Sets the class description of the receiver’s container specifier to a given specifier.

<sub>Mac Catalyst, macOS</sub>

```swift
var containerClassDescription: NSScriptClassDescription? { get set }
```

## Parameters

- `classDescription` — The class description of the receiver’s container specifier.

## See Also

### Getting, testing, and setting containers

- [containerIsObjectBeingTested](containerisobjectbeingtested.md) — Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.
- [containerIsRangeContainerObject](containerisrangecontainerobject.md) — Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.
- [containerSpecifier](container.md) — Sets the container specifier of the receiver.
