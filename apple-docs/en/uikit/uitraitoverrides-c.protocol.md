---
title: UITraitOverrides
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitoverrides-c.protocol
source_url: 'https://developer.apple.com/documentation/uikit/uitraitoverrides-c.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitoverrides-c.protocol.json'
content_hash: 'sha256:b3d2f931dc2e5ef0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitOverrides

<sub>Protocol</sub>

A mutable container of traits you use to set trait changes for an object and its descendants.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UITraitOverrides <UIMutableTraits>
```

## Relationships

- **Inherits From**: [UIMutableTraits](uimutabletraits-8l00o.md)

## Topics

### Inspecting overrides

- [containsTrait:](uitraitoverrides-c.protocol/containstrait_.md) — Returns a Boolean value that indicates whether the trait overrides contain a change for the trait you provide.

### Removing overrides

- [removeTrait:](uitraitoverrides-c.protocol/removetrait_.md) — Removes the change for the trait you provide.

## See Also

### Overriding trait values

- [traitOverrides](uipresentationcontroller/traitoverrides-9o0j4.md)
