---
title: FocusInteractions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusinteractions
source_url: 'https://developer.apple.com/documentation/swiftui/focusinteractions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusinteractions.json'
content_hash: 'sha256:d9d7c0ccba07864e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FocusInteractions

<sub>Structure</sub>

Values describe different focus interactions that a view can support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FocusInteractions
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Creating the interaction types

- [automatic](focusinteractions/automatic.md) — The view supports whatever focus-driven interactions are commonly expected for interactive content on the current platform.
- [activate](focusinteractions/activate.md) — The view has a primary action that can be activated via focus gestures.
- [edit](focusinteractions/edit.md) — The view captures input from non-spatial sources like a keyboard or Digital Crown.

## See Also

### Indicating that a view can receive focus

- [focusable(_:)](<view/focusable(__).md>) — Specifies if the view is focusable.
- [focusable(_:interactions:)](<view/focusable(__interactions_).md>) — Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
