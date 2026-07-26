---
title: 'Preview(_:traits:body:cameras:)'
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/preview(_:traits:body:cameras:)'
source_url: 'https://developer.apple.com/documentation/swiftui/preview(_:traits:body:cameras:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preview%28_%3Atraits%3Abody%3Acameras%3A%29.json'
content_hash: 'sha256:f0fc95bffc204637'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Preview(_:traits:body:cameras:)

<sub>Macro</sub>

Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.

<sub>visionOS</sub>

```swift
@freestanding(declaration) macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., @ContentBuilder body: @escaping @MainActor () -> any View, @PreviewCameraBuilder cameras: () -> [PreviewCamera])
```

## Parameters

- `name` — An optional display name for the preview. If you don’t specify a name, the canvas labels the preview using the line number where the preview appears in source.

- `traits` — An optional list of [PreviewTrait](../developertoolssupport/previewtrait.md) instances that customize the appearance of the preview.

- `body` — A [ContentBuilder](contentbuilder.md) that produces a SwiftUI view to preview. You typically specify one of your app’s custom views and optionally any inputs, model data, modifiers, and enclosing views that the custom view needs for normal operation.

- `cameras` — One or more preview cameras that indicate the custom, fixed viewpoints that you want to be able to view the preview from. The first of these replaces the front viewpoint as the default.

## Overview

This macro behaves like [Preview(_:traits:_:body:)](<preview(__traits___body_).md>) except that it also enables you to specify one or more [PreviewCamera](../developertoolssupport/previewcamera.md) instances that define custom, fixed viewpoints from which to view the preview:

```swift
#Preview {
    ContentView()
} cameras: {
    PreviewCamera(from: .bottomLeadingBack, name: "Corner 1")
    PreviewCamera(from: .topTrailingFront, name: "Corner 2")
}
```

If you use one of the preview macros that doesn’t include a `cameras` closure, the canvas displays the preview from the front by default. It also provides a camera picker to choose other standard, fixed viewpoints — like the top or the back. When you do specify one or more preview cameras, the canvas adds a submenu to the camera picker that lists the viewpoints that you define, like Corner 1 and Corner 2 in the above example. The canvas also displays the preview from the first of these custom viewpoints by default when it loads the preview.

> [!note] Note
> In addition to using fixed camera perspectives, you can also interactively alter the viewpoint of a preview in the canvas using controls like those that Simulator provides. For more information, see doc://com.apple.documentation/documentation/visionOS/interacting-with-your-app-in-the-visionos-simulator.

Other preview macros provide different customization options. For example, if you want to preview the view as it would appear in a particular kind of scene, you can use [Preview(_:immersionStyle:traits:body:cameras:)](<preview(__immersionstyle_traits_body_cameras_).md>) or [Preview(_:windowStyle:traits:body:cameras:)](<preview(__windowstyle_traits_body_cameras_).md>).

## See Also

### Creating a preview

- [Preview(_:body:)](<preview(__body_).md>) — Creates a preview of a SwiftUI view.
- [Preview(_:traits:_:body:)](<preview(__traits___body_).md>) — Creates a preview of a SwiftUI view using the specified traits.
- [Preview(_:traits:arguments:body:)](<preview(__traits_arguments_body_).md>) — Creates a group of previews of a parameterized SwiftUI view, varying its inputs over the provided arguments.
