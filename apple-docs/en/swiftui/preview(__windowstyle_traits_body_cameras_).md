---
title: 'Preview(_:windowStyle:traits:body:cameras:)'
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/preview(_:windowstyle:traits:body:cameras:)'
source_url: 'https://developer.apple.com/documentation/swiftui/preview(_:windowstyle:traits:body:cameras:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preview%28_%3Awindowstyle%3Atraits%3Abody%3Acameras%3A%29.json'
content_hash: 'sha256:6701937ed80b8cbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Preview(_:windowStyle:traits:body:cameras:)

<sub>Macro</sub>

Creates a preview of a SwiftUI view in a window with custom viewpoints.

<sub>visionOS</sub>

```swift
@freestanding(declaration) macro Preview<Style>(_ name: String? = nil, windowStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., @ContentBuilder body: @escaping @MainActor () -> any View, @PreviewCameraBuilder cameras: () -> [PreviewCamera]) where Style : WindowStyle
```

## Parameters

- `name` — An optional display name for the preview. If you don’t specify a name, the canvas labels the preview using the line number where the preview appears in source.

- `windowStyle` — The [WindowStyle](windowstyle.md) to use for the preview. Use this input to display the view as if it appears in a window that has the specified style.

- `traits` — An optional list of [PreviewTrait](../developertoolssupport/previewtrait.md) instances that customize the appearance of the preview.

- `body` — A [ContentBuilder](contentbuilder.md) that produces a SwiftUI view to preview. You typically specify one of your app’s custom views and optionally any inputs, model data, modifiers, and enclosing views that the custom view needs for normal operation.

- `cameras` — One or more preview cameras that indicate the custom, fixed viewpoints that you want to be able to view the preview from. The first of these replaces the front viewpoint as the default.

## Overview

This preview macro behaves like [Preview(_:windowStyle:traits:body:)](<preview(__windowstyle_traits_body_).md>) combined with [Preview(_:traits:body:cameras:)](<preview(__traits_body_cameras_).md>): it enables you to define a window scene context for the view, and also to define custom, fixed viewpoints for the preview:

```swift
#Preview("Volume", windowStyle: .volumetric) {
   ContentView()
} cameras: {
   PreviewCamera(from: .front)
   PreviewCamera(from: .top, zoom: 2)
   PreviewCamera(from: .leading, zoom: 0.5, name: "close up")
}
```

See those other preview macros for more information about using scenes and cameras in your preview. If you want to preview in an immersive space rather than a window, use [Preview(_:immersionStyle:traits:body:cameras:)](<preview(__immersionstyle_traits_body_cameras_).md>).

## See Also

### Creating a preview in the context of a scene

- [Preview(_:immersionStyle:traits:body:)](<preview(__immersionstyle_traits_body_).md>) — Creates a preview of a SwiftUI view in an immersive space.
- [Preview(_:immersionStyle:traits:body:cameras:)](<preview(__immersionstyle_traits_body_cameras_).md>) — Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.
- [Preview(_:windowStyle:traits:body:)](<preview(__windowstyle_traits_body_).md>) — Creates a preview of a SwiftUI view in a window.
