---
title: 'quickLookPreview(_:in:)'
framework: QuickLook
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, macOS 11.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/quicklookpreview(_:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/quicklookpreview(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/quicklookpreview%28_%3Ain%3A%29.json'
content_hash: 'sha256:c5de8050a347d0d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# quickLookPreview(_:in:)

<sub>Instance Method</sub>

Presents a Quick Look preview of the URLs you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func quickLookPreview<Items>(_ selection: Binding<Items.Element?>, in items: Items) -> some View where Items : RandomAccessCollection, Items.Element == URL

```

## Parameters

- `selection` — A [Binding](../binding.md) to an element that’s part of the items collection. This is the URL that you currently want to preview.

- `items` — A collection of URLs to preview.

## Return Value

A view that presents the preview of the contents of the URL.

## Discussion

The Quick Look preview appears when you set the binding to a non-`nil` item. When you set the item back to `nil`, Quick Look dismisses the preview. If the value of the selection binding isn’t contained in the items collection, Quick Look treats it the same as a `nil` selection.

Quick Look updates the value of the selection binding to match the URL of the file the user is previewing. Upon dismissal by the user, Quick Look automatically sets the item binding to `nil`.

## See Also

### Previewing content

- [quickLookPreview(_:)](<quicklookpreview(__).md>) — Presents a Quick Look preview of the contents of a single URL.
