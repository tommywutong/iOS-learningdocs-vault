---
title: 'init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentlaunchview/init%28_%3Afor%3A_%3Aondocumentopen%3Abackgroundaccessoryview%3Aoverlayaccessoryview%3A%29.json'
content_hash: 'sha256:5732e59d23fd98ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentLaunchView](../documentlaunchview.md)

# init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)

<sub>Initializer</sub>

Creates a view to present when launching document-related user experiences using a localized title, custom actions, and accessory views.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@export(implementation) nonisolated init(_ title: LocalizedStringResource, for contentTypes: [UTType], @ContentBuilder _ actions: () -> Actions, @ContentBuilder onDocumentOpen: @escaping (URL) -> DocumentView, @ContentBuilder backgroundAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View, @ContentBuilder overlayAccessoryView: @escaping (DocumentLaunchGeometryProxy) -> some View)
```

## Parameters

- `title` — A title resource to use for the view title.

- `contentTypes` — Content types that the view can open.

- `actions` — A content builder returning the view’s actions

- `onDocumentOpen` — A closure that handles an open file.

- `backgroundAccessoryView` — A content builder for returning the view’s background accessory view.

- `overlayAccessoryView` — A content builder for returning the view’s overlay accessory view.

## Discussion

> [!note] Note
> An alternative to `DocumentLaunchView` is a scene variant of this API: [DocumentGroupLaunchScene](../documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## See Also

### Creating a launch view with a background view

- [init(_:for:_:onDocumentOpen:)](<init(__for___ondocumentopen_).md>) — Creates a view to present when launching document-related user experiences using a localized title and custom actions.
- [init(_:for:_:onDocumentOpen:background:)](<init(__for___ondocumentopen_background_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:)](<init(__for___ondocumentopen_background_backgroundaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and a background accessory view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:overlayAccessoryView:)](<init(__for___ondocumentopen_background_backgroundaccessoryview_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and accessory views.
- [init(_:for:_:onDocumentOpen:background:overlayAccessoryView:)](<init(__for___ondocumentopen_background_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and an overlay accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:)](<init(__for___ondocumentopen_backgroundaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background accessory view.
- [init(_:for:_:onDocumentOpen:overlayAccessoryView:)](<init(__for___ondocumentopen_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and an overlay accessory view.
