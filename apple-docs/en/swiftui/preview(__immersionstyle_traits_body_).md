---
title: 'Preview(_:immersionStyle:traits:body:)'
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/preview(_:immersionstyle:traits:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/preview(_:immersionstyle:traits:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preview%28_%3Aimmersionstyle%3Atraits%3Abody%3A%29.json'
content_hash: 'sha256:a3b99145feb9ba96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Preview(_:immersionStyle:traits:body:)

<sub>Macro</sub>

Creates a preview of a SwiftUI view in an immersive space.

<sub>visionOS</sub>

```swift
@freestanding(declaration) macro Preview<Style>(_ name: String? = nil, immersionStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., @ContentBuilder body: @escaping @MainActor () -> any View) where Style : ImmersionStyle
```

## Parameters

- `name` — An optional display name for the preview. If you don’t specify a name, the canvas labels the preview using the line number where the preview appears in source.

- `immersionStyle` — The [ImmersionStyle](immersionstyle.md) to use for the preview. Use this input to display the view as if it appears in an immersive space that has the specified style.

- `traits` — An optional list of [PreviewTrait](../developertoolssupport/previewtrait.md) instances that customize the appearance of the preview.

- `body` — A [ContentBuilder](contentbuilder.md) that produces a SwiftUI view to preview. You typically specify one of your app’s custom views and optionally any inputs, model data, modifiers, and enclosing views that the custom view needs for normal operation.

## Overview

This preview macro behaves like [Preview(_:traits:_:body:)](<preview(__traits___body_).md>), except that it also enables you to define a scene context for the view. Specifically, it places the view in an immersive space with the specified immersion style, like the [mixed](immersionstyle/mixed.md) style:

```swift
#Preview("Mixed immersive space", immersionStyle: .mixed) {
   ContentView()
}
```

Use this preview macro when the view needs scene context to behave as it would during normal operation of your app.

Other preview macros provide different customization options. For example, if you want to see how the view appears in a window rather than an immersive space, you can use [Preview(_:windowStyle:traits:body:)](<preview(__windowstyle_traits_body_).md>). If you want to add custom, fixed viewpoints to an immersive space preview, use [Preview(_:immersionStyle:traits:body:cameras:)](<preview(__immersionstyle_traits_body_cameras_).md>).

## See Also

### Creating a preview in the context of a scene

- [Preview(_:immersionStyle:traits:body:cameras:)](<preview(__immersionstyle_traits_body_cameras_).md>) — Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.
- [Preview(_:windowStyle:traits:body:)](<preview(__windowstyle_traits_body_).md>) — Creates a preview of a SwiftUI view in a window.
- [Preview(_:windowStyle:traits:body:cameras:)](<preview(__windowstyle_traits_body_cameras_).md>) — Creates a preview of a SwiftUI view in a window with custom viewpoints.
