---
title: 'Preview(_:traits:arguments:body:)'
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 27.0+ beta, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/preview(_:traits:arguments:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/preview(_:traits:arguments:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preview%28_%3Atraits%3Aarguments%3Abody%3A%29.json'
content_hash: 'sha256:5de45772a087c5dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Preview(_:traits:arguments:body:)

<sub>Macro</sub>

Creates a group of previews of a parameterized SwiftUI view, varying its inputs over the provided arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(declaration) macro Preview<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @ContentBuilder body: @escaping @MainActor (T) -> any View)
```

## Parameters

- `name` — An optional display name for the preview. If you don’t specify a name, the canvas labels the preview using the line number where the preview appears in source.

- `traits` — Optional [PreviewTrait](../developertoolssupport/previewtrait.md) instances that customizes the appearance of the preview.

- `arguments` — An array of inputs to pass into the preview’s `body`.

- `body` — A [ContentBuilder](contentbuilder.md) mapping an argument to a SwiftUI view to preview.

## See Also

### Creating a preview

- [Preview(_:body:)](<preview(__body_).md>) — Creates a preview of a SwiftUI view.
- [Preview(_:traits:_:body:)](<preview(__traits___body_).md>) — Creates a preview of a SwiftUI view using the specified traits.
- [Preview(_:traits:body:cameras:)](<preview(__traits_body_cameras_).md>) — Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.
