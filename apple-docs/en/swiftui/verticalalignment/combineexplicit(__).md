---
title: 'combineExplicit(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/verticalalignment/combineexplicit(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/verticalalignment/combineexplicit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalalignment/combineexplicit%28_%3A%29.json'
content_hash: 'sha256:a08a2c0b22489258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VerticalAlignment](../verticalalignment.md)

# combineExplicit(_:)

<sub>Instance Method</sub>

Merges a sequence of explicit alignment values produced by this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func combineExplicit<S>(_ values: S) -> CGFloat? where S : Sequence, S.Element == CGFloat?
```

## Discussion

For most alignment types, this method returns the mean of all non-`nil` values. However, some types use other rules. For example, [firstTextBaseline](firsttextbaseline.md) returns the minimum value, while [lastTextBaseline](lasttextbaseline.md) returns the maximum value.

## See Also

### Creating a custom alignment

- [init(_:)](<init(__).md>) — Creates a custom vertical alignment of the specified type.
