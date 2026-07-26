---
title: SafeAreaRegions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/safearearegions
source_url: 'https://developer.apple.com/documentation/swiftui/safearearegions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/safearearegions.json'
content_hash: 'sha256:7a8889a3b238cc12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SafeAreaRegions

<sub>Structure</sub>

A set of symbolic safe area regions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct SafeAreaRegions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting safe area regions

- [all](safearearegions/all.md) — All safe area regions.
- [container](safearearegions/container.md) — The safe area defined by the device and containers within the user interface, including elements such as top and bottom bars.
- [keyboard](safearearegions/keyboard.md) — The safe area matching the current extent of any software keyboard displayed over the view content.

## See Also

### Staying in the safe areas

- [ignoresSafeArea(_:edges:)](<view/ignoressafearea(__edges_).md>) — Expands the safe area of a view.
- [ignoresSafeArea(_:edges:alignment:)](<view/ignoressafearea(__edges_alignment_).md>) — Expands the safe area of a view aligning content within the new bounds using the provided alignment. _(beta)_
- [safeAreaInset(edge:alignment:spacing:content:)](<view/safeareainset(edge_alignment_spacing_content_).md>) — Shows the specified content beside the modified view.
- [safeAreaPadding(_:)](<view/safeareapadding(__).md>) — Adds the provided insets into the safe area of this view.
- [safeAreaPadding(_:_:)](<view/safeareapadding(____).md>) — Adds the provided insets into the safe area of this view.
