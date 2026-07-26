---
title: 'webViewOnScrollGeometryChange(for:of:action:)'
framework: WebKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/webviewonscrollgeometrychange(for:of:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/webviewonscrollgeometrychange(for:of:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/webviewonscrollgeometrychange%28for%3Aof%3Aaction%3A%29.json'
content_hash: 'sha256:12b41fec58c5ec36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# webViewOnScrollGeometryChange(for:of:action:)

<sub>Instance Method</sub>

Adds an action to be performed when a value, created from a scroll geometry, changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func webViewOnScrollGeometryChange<T>(for type: T.Type, of transform: @escaping (ScrollGeometry) -> T, action: @escaping (T, T) -> Void) -> some View where T : Hashable

```

## Parameters

- `type` — The type of value transformed from a [ScrollGeometry](../scrollgeometry.md).

- `transform` — A closure that transforms a [ScrollGeometry](../scrollgeometry.md) to your type.

- `action` — A closure to run when the transformed data changes.

## Return Value

A view that invokes the action when the relevant part of a web view’s scroll geometry changes.

## Discussion

> [!note] Note
> The content size of web content may exceed the current size of the view’s frame, however it will never be smaller than it.

## See Also

### Displaying web content

- [WebView](../../webkit/webview-swift.struct.md) — A view that displays some web content.
- [WebPage](../../webkit/webpage.md) — An object that controls and manages the behavior of interactive web content.
- [onWebViewImmersiveEnvironmentRequest(shouldAllow:present:dismiss:)](<onwebviewimmersiveenvironmentrequest(shouldallow_present_dismiss_).md>) — Manages the lifecycle of immersive environments requested by websites. _(beta)_
- [webViewBackForwardNavigationGestures(_:)](<webviewbackforwardnavigationgestures(__).md>) — Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [webViewContentBackground(_:)](<webviewcontentbackground(__).md>) — Specifies the visibility of the webpage’s natural background color within this view.
- [webViewContextMenu(menu:)](<webviewcontextmenu(menu_).md>) — Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [webViewElementFullscreenBehavior(_:)](<webviewelementfullscreenbehavior(__).md>) — Determines whether a web view can display content full screen.
- [webViewLinkPreviews(_:)](<webviewlinkpreviews(__).md>) — Determines whether pressing a link displays a preview of the destination for the link.
- [webViewMagnificationGestures(_:)](<webviewmagnificationgestures(__).md>) — Determines whether magnify gestures change the view’s magnification.
- [webViewScrollInputBehavior(_:for:)](<webviewscrollinputbehavior(__for_).md>) — Enables or disables scrolling in web views when using particular inputs.
- [webViewScrollPosition(_:)](<webviewscrollposition(__).md>) — Associates a binding to a scroll position with the web view.
- [webViewTextSelection(_:)](<webviewtextselection(__).md>) — Determines whether to allow people to select or otherwise interact with text.
