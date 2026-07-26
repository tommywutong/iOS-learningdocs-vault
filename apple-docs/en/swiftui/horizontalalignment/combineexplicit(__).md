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
doc_path: '/documentation/swiftui/horizontalalignment/combineexplicit(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/horizontalalignment/combineexplicit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontalalignment/combineexplicit%28_%3A%29.json'
content_hash: 'sha256:ce1b7a130269398c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HorizontalAlignment](../horizontalalignment.md)

# combineExplicit(_:)

<sub>Instance Method</sub>

Merges a sequence of explicit alignment values produced by this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func combineExplicit<S>(_ values: S) -> CGFloat? where S : Sequence, S.Element == CGFloat?
```

## Discussion

For built-in horizontal alignment types, this method returns the mean of all non-`nil` values.

## See Also

### Creating a custom alignment

- [init(_:)](<init(__).md>) — Creates a custom horizontal alignment of the specified type.
