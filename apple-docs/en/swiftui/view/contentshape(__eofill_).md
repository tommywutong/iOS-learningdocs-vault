---
title: 'contentShape(_:eoFill:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/contentshape(_:eofill:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/contentshape(_:eofill:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/contentshape%28_%3Aeofill%3A%29.json'
content_hash: 'sha256:4d0045c54ead976a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# contentShape(_:eoFill:)

<sub>Instance Method</sub>

Defines the content shape for hit testing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func contentShape<S>(_ shape: S, eoFill: Bool = false) -> some View where S : Shape

```

## Parameters

- `shape` — The hit testing shape for the view.

- `eoFill` — A Boolean that indicates whether the shape is interpreted with the even-odd winding number rule.

## Return Value

A view that uses the given shape for hit testing.

## See Also

### Controlling hit testing

- [allowsTightening(_:)](<allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [contentShape(_:_:eoFill:)](<contentshape(____eofill_).md>) — Sets the content shape for this view.
- [ContentShapeKinds](../contentshapekinds.md) — A kind for the content shape of a view.
