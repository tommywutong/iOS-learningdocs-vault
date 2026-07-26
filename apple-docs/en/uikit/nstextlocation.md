---
title: NSTextLocation
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlocation
source_url: 'https://developer.apple.com/documentation/uikit/nstextlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlocation.json'
content_hash: 'sha256:ffce610b7dabbf98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextLocation

<sub>Protocol</sub>

An interface you implement that represents an abstract location inside your document’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
protocol NSTextLocation : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Comparing text locations

- [- compare:](<nstextlocation/compare(__).md>) — Compares and returns the logical ordering to location.

### Instance Properties

- [hash](nstextlocation/hash.md) — Must be consistent with results from `isEqual:` while also avoiding hash collisions.

### Instance Methods

- [- isEqual:](<nstextlocation/isequal(__).md>) — Returns `true` for locations representing the same document position.

## See Also

### Location and selection

- [NSTextRange](nstextrange.md) — A class that represents a contiguous range between two locations inside document contents.
- [NSTextSelection](nstextselection.md) — A class that represents a single logical selection context that corresponds to an insertion point.
- [NSTextSelectionNavigation](nstextselectionnavigation.md) — An interface you use to expose methods for obtaining results from actions performed on text selections.
