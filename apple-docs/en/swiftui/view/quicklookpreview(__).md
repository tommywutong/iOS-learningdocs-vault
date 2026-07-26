---
title: 'quickLookPreview(_:)'
framework: QuickLook
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, macOS 11.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/quicklookpreview(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/quicklookpreview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/quicklookpreview%28_%3A%29.json'
content_hash: 'sha256:435400e81857fedc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# quickLookPreview(_:)

<sub>Instance Method</sub>

Presents a Quick Look preview of the contents of a single URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func quickLookPreview(_ item: Binding<URL?>) -> some View

```

## Parameters

- `item` — A [Binding](../binding.md) to a URL that should be previewed.

## Return Value

A view that presents the preview of the contents of the URL.

## Discussion

The Quick Look preview appears when you set the binding to a non-`nil` item. When you set the item back to `nil`, Quick Look dismisses the preview.

Upon dismissal by the user, Quick Look automatically sets the item binding to `nil`. Quick Look displays the preview when a non-`nil` item is set. Set `item` to `nil` to dismiss the preview.

## See Also

### Previewing content

- [quickLookPreview(_:in:)](<quicklookpreview(__in_).md>) — Presents a Quick Look preview of the URLs you provide.
