---
title: 'replacingUnspecifiedDimensions(by:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/proposedviewsize/replacingunspecifieddimensions(by:)'
source_url: 'https://developer.apple.com/documentation/swiftui/proposedviewsize/replacingunspecifieddimensions(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/proposedviewsize/replacingunspecifieddimensions%28by%3A%29.json'
content_hash: 'sha256:1428670c81c7418d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProposedViewSize](../proposedviewsize.md)

# replacingUnspecifiedDimensions(by:)

<sub>Instance Method</sub>

Creates a new proposal that replaces unspecified dimensions in this proposal with the corresponding dimension of the specified size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingUnspecifiedDimensions(by size: CGSize = CGSize(width: 10, height: 10)) -> CGSize
```

## Parameters

- `size` — A set of concrete values to use for the size proposal in place of any unspecified dimensions. The default value is `10` for both dimensions.

## Return Value

A new, fully specified size proposal.

## Discussion

Use the default value to prevent a flexible view from disappearing into a zero-sized frame, and ensure the unspecified value remains visible during debugging.
