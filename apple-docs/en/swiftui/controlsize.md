---
title: ControlSize
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 10.15+, tvOS 15.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlsize
source_url: 'https://developer.apple.com/documentation/swiftui/controlsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlsize.json'
content_hash: 'sha256:5c3d00fca175b794'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ControlSize

<sub>Enumeration</sub>

The size classes, like regular or small, that you can apply to controls within a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ControlSize
```

## Relationships

- **Conforms To**: [CaseIterable](../swift/caseiterable.md), [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting control sizes

- [ControlSize.mini](controlsize/mini.md) — A control version that is minimally sized.
- [ControlSize.small](controlsize/small.md) — A control version that is proportionally smaller size for space-constrained views.
- [ControlSize.regular](controlsize/regular.md) — A control version that is the default size.
- [ControlSize.large](controlsize/large.md) — A control version that is prominently sized.
- [ControlSize.extraLarge](controlsize/extralarge.md) — A control version that is substantially sized. The largest control size. Resolves to [ControlSize.large](controlsize/large.md) on platforms other than visionOS.

### Initializers

- [init(_:)](<controlsize/init(__).md>) — Creates a control size from its NSControl.ControlSize equivalent.

## See Also

### Sizing controls

- [controlSize(_:)](<view/controlsize(__).md>) — Sets the size for controls within this view.
- [controlSize](environmentvalues/controlsize.md) — The size to apply to controls within a view.
