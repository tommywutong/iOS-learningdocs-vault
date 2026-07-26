---
title: UITraitOverrides
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitoverrides-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uitraitoverrides-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitoverrides-swift.struct.json'
content_hash: 'sha256:68b9a7cde03fb219'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitOverrides

<sub>Structure</sub>

A mutable container of traits you use to set trait changes for an object and its descendants.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UITraitOverrides
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Escapable](../swift/escapable.md), [UIMutableTraits](uimutabletraits-13ja5.md)

## Topics

### Inspecting overrides

- [contains(_:)](<uitraitoverrides-swift.struct/contains(__).md>) — Returns a Boolean value that indicates whether the trait overrides contain a change for the trait you provide.

### Removing overrides

- [remove(_:)](<uitraitoverrides-swift.struct/remove(__).md>) — Removes the change for the trait you provide.

## See Also

### Overriding trait values

- [traitOverrides](uipresentationcontroller/traitoverrides-629ka.md)
