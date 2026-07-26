---
title: 'Preview(_:traits:_:body:)'
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/preview(_:traits:_:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/preview(_:traits:_:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preview%28_%3Atraits%3A_%3Abody%3A%29.json'
content_hash: 'sha256:603fdb5912606c4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Preview(_:traits:_:body:)

<sub>Macro</sub>

Creates a preview of a SwiftUI view using the specified traits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(declaration) macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>, _ additionalTraits: PreviewTrait<Preview.ViewTraits>..., @ContentBuilder body: @escaping @MainActor () -> any View)
```

## Parameters

- `name` — An optional display name for the preview. If you don’t specify a name, the canvas labels the preview using the line number where the preview appears in source.

- `traits` — A [PreviewTrait](../developertoolssupport/previewtrait.md) instance that customizes the appearance of the preview.

- `additionalTraits` — Optional additional traits that further customize the preview.

- `body` — A [ContentBuilder](contentbuilder.md) that produces a SwiftUI view to preview. You typically specify one of your app’s custom views and optionally any inputs, model data, modifiers, and enclosing views that the custom view needs for normal operation.

## Overview

This macro behaves like [Preview(_:body:)](<preview(__body_).md>) except that it also enables you to customize the appearance of the preview by adding one or more traits, which are instances of [PreviewTrait](../developertoolssupport/previewtrait.md). For example, you can display a preview at a fixed size using the [fixedLayout(width:height:)](<../developertoolssupport/previewtrait/fixedlayout(width_height_).md>) trait:

```swift
#Preview(
    "Content",
    traits: .fixedLayout(width: 100, height: 100)
) {
    ContentView()
}
```

The macro ignores traits that don’t apply to the current context. For example, the [portrait](../developertoolssupport/previewtrait/portrait.md) trait has no impact on a visionOS preview.

Other preview macros provide different customization options. For example, if you want to specify a custom viewpoint for the preview, use [Preview(_:traits:body:cameras:)](<preview(__traits_body_cameras_).md>).

## See Also

### Creating a preview

- [Preview(_:body:)](<preview(__body_).md>) — Creates a preview of a SwiftUI view.
- [Preview(_:traits:body:cameras:)](<preview(__traits_body_cameras_).md>) — Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.
- [Preview(_:traits:arguments:body:)](<preview(__traits_arguments_body_).md>) — Creates a group of previews of a parameterized SwiftUI view, varying its inputs over the provided arguments.
