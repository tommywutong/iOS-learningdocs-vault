---
title: 'init(_:_:background:overlayAccessoryView:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/documentgrouplaunchscene/init(_:_:background:overlayaccessoryview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:_:background:overlayaccessoryview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgrouplaunchscene/init%28_%3A_%3Abackground%3Aoverlayaccessoryview%3A%29.json'
content_hash: 'sha256:68677287ac2bb273'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroupLaunchScene](../documentgrouplaunchscene.md)

# init(_:_:background:overlayAccessoryView:)

<sub>Initializer</sub>

Creates a launch scene for document-based applications with a title, a set of actions, a background, and an overlay accessory view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ title: LocalizedStringResource, @ContentBuilder _ actions: () -> Actions, @ContentBuilder background: () -> some View, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View)
```

## Parameters

- `title` — A resource to use for the view title.

- `actions` — A content builder for returning the view’s actions.

- `background` — The background of the scene.

- `overlayAccessoryView` — A content builder for returning the view’s overlay accessory view.

## Discussion

Use a `DocumentGroupLaunchScene` alongside any [DocumentGroup](../documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [DocumentLaunchView](../documentlaunchview.md).

## See Also

### Creating a launch scene with a background view

- [init(_:_:background:)](<init(____background_).md>) — Creates a launch scene for document-based applications with a title, a set of actions, and a background.
- [init(_:_:background:backgroundAccessoryView:)](<init(____background_backgroundaccessoryview_).md>) — Creates a launch scene for document-based applications with a title, a set of actions, a background, and a background accessory view.
- [init(_:_:background:backgroundAccessoryView:overlayAccessoryView:)](<init(____background_backgroundaccessoryview_overlayaccessoryview_).md>) — Creates a launch scene for document-based applications with a title, a set of actions, and a background.
