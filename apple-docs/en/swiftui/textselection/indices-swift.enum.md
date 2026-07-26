---
title: TextSelection.Indices
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselection/indices-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/textselection/indices-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselection/indices-swift.enum.json'
content_hash: 'sha256:9e313070322c17ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextSelection](../textselection.md)

# TextSelection.Indices

<sub>Enumeration</sub>

The indices of the current selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Indices
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Enumeration Cases

- [TextSelection.Indices.multiSelection(_:)](<indices-swift.enum/multiselection(__).md>) — The range-set of the selections.
- [TextSelection.Indices.selection(_:)](<indices-swift.enum/selection(__).md>) — The range of the single selection. This may also an represent insertion points if `range.lowerBound == range.upperBound`.
