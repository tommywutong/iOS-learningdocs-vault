---
title: 'init(_:backgroundStyle:_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/documentgrouplaunchscene/init(_:backgroundstyle:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene/init(_:backgroundstyle:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgrouplaunchscene/init%28_%3Abackgroundstyle%3A_%3A%29.json'
content_hash: 'sha256:0b535120a9d88ace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroupLaunchScene](../documentgrouplaunchscene.md)

# init(_:backgroundStyle:_:)

<sub>Initializer</sub>

Creates a launch scene for document-based applications with a title, a background style, and a set of actions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@export(implementation) nonisolated init<B>(_ title: LocalizedStringResource, backgroundStyle: B = BackgroundStyle(), @ContentBuilder _ actions: () -> Actions = { DefaultDocumentGroupLaunchActions() }) where B : ShapeStyle
```

## Parameters

- `title` — A resource to use for the view title.

- `backgroundStyle` — A background style of the view.

- `actions` — A content builder for returning the view’s actions.

## Discussion

Use a `DocumentGroupLaunchScene` alongside any [DocumentGroup](../documentgroup.md) scenes. If you don’t implement a `DocumentGroup` in the app declaration, you can get the same design by implementing a [DocumentLaunchView](../documentlaunchview.md).

## See Also

### Creating a launch scene with a background style

- [init(_:backgroundStyle:_:backgroundAccessoryView:)](<init(__backgroundstyle___backgroundaccessoryview_).md>) — Creates a launch scene for document-based applications with a title, a background style, a set of actions, and a background accessory view.
- [init(_:backgroundStyle:_:backgroundAccessoryView:overlayAccessoryView:)](<init(__backgroundstyle___backgroundaccessoryview_overlayaccessoryview_).md>) — Creates a launch scene for document-based applications with a title, a background style, a set of actions, and background and overlay accessory views.
- [init(_:backgroundStyle:_:overlayAccessoryView:)](<init(__backgroundstyle___overlayaccessoryview_).md>) — Creates a launch scene for document-based applications with a title, a background style, a set of actions, and an overlay accessory view.
