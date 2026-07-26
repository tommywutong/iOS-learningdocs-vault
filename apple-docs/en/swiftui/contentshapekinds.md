---
title: ContentShapeKinds
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentshapekinds
source_url: 'https://developer.apple.com/documentation/swiftui/contentshapekinds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentshapekinds.json'
content_hash: 'sha256:7bb5f4209c0cb687'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContentShapeKinds

<sub>Structure</sub>

A kind for the content shape of a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ContentShapeKinds
```

## Overview

The kind is used by the system to influence various effects, hit-testing, and more.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting shape kinds

- [interaction](contentshapekinds/interaction.md) — The kind for hit-testing and accessibility.
- [dragPreview](contentshapekinds/dragpreview.md) — The kind for drag and drop previews.
- [contextMenuPreview](contentshapekinds/contextmenupreview.md) — The kind for context menu previews.
- [focusEffect](contentshapekinds/focuseffect.md) — The kind for the focus effect.
- [hoverEffect](contentshapekinds/hovereffect.md) — The kind for hover effects.
- [accessibility](contentshapekinds/accessibility.md) — The kind for accessibility visuals and sorting.

### Creating a set of options

- [init(rawValue:)](<contentshapekinds/init(rawvalue_).md>) — Creates a content shape kind.

## See Also

### Controlling hit testing

- [allowsTightening(_:)](<view/allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [contentShape(_:eoFill:)](<view/contentshape(__eofill_).md>) — Defines the content shape for hit testing.
- [contentShape(_:_:eoFill:)](<view/contentshape(____eofill_).md>) — Sets the content shape for this view.
