---
title: 'previewDisplayName(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/previewdisplayname(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/previewdisplayname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/previewdisplayname%28_%3A%29.json'
content_hash: 'sha256:debe7b004fe7a27b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# previewDisplayName(_:)

<sub>Instance Method</sub>

Sets a user visible name to show in the canvas for a preview.

> [!warning] Deprecated
> Use [Preview(_:body:)](<../preview(__body_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func previewDisplayName(_ value: String?) -> some View

```

## Parameters

- `value` — A name for the preview.

## Return Value

A preview that uses the given name.

## Discussion

Apply this modifier to a view inside your [PreviewProvider](../previewprovider.md) implementation to associate a display name with that view’s preview:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDisplayName("Circle")
    }
}
```

![A screenshot of the Xcode preview canvas cropped to just the top of a](../../../../attachments/af4f6594769133bd756945b236c1583e/View-previewDisplayName-1@2x.png)

Add a name when you have multiple previews together in the canvas that you need to tell apart. The default value is `nil`, in which case Xcode displays a default string.

## See Also

### Defining a preview

- [PreviewProvider](../previewprovider.md) — A type that produces view previews in Xcode. _(deprecated)_
- [PreviewPlatform](../previewplatform.md) — Platforms that can run the preview. _(deprecated)_
