---
title: SceneAccessoryContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/sceneaccessorycontent
source_url: 'https://developer.apple.com/documentation/swiftui/sceneaccessorycontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sceneaccessorycontent.json'
content_hash: 'sha256:b4a33ba26bffaab2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SceneAccessoryContent

<sub>Protocol</sub>

Conforming types represent items which define content for scene accessories.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol SceneAccessoryContent
```

## Relationships

- **Conforming Types**: [EmptyView](emptyview.md), [ExternalNonInteractiveAccessory](externalnoninteractiveaccessory.md), [ForEach](foreach.md), [Group](group.md), [TupleContent](tuplecontent.md)

## Topics

### Associated Types

- [Body](sceneaccessorycontent/body-swift.associatedtype.md) — The type of content representing the body of this scene accessory content. _(beta)_

### Instance Properties

- [body](sceneaccessorycontent/body-swift.property.md) — The composition of content that comprise the accessory content. _(beta)_

### Instance Methods

- [onAvailabilityChange(perform:)](<sceneaccessorycontent/onavailabilitychange(perform_).md>) — Defines a callback for observing the availability of `self`. _(beta)_

## See Also

### Presenting content on an external display

- [sceneAccessory(content:)](<view/sceneaccessory(content_).md>) — Defines any scene accessories associated with `self`. _(beta)_
- [ExternalNonInteractiveAccessory](externalnoninteractiveaccessory.md) — A scene accessory that presents non-interactive content on an external display. _(beta)_
