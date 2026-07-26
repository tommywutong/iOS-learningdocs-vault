---
title: 'webViewScrollPosition(_:)'
framework: WebKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/webviewscrollposition(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/webviewscrollposition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/webviewscrollposition%28_%3A%29.json'
content_hash: 'sha256:00cac3c629bd4365'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# webViewScrollPosition(_:)

<sub>Instance Method</sub>

Associates a binding to a scroll position with the web view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func webViewScrollPosition(_ position: Binding<ScrollPosition>) -> some View

```

## Discussion

> [!note] Note
> `WebView` does not support scrolling to a view with an identity. It only supports scrolling to a concrete offset, or to an edge.

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
- [webViewOnScrollGeometryChange(for:of:action:)](<webviewonscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [webViewScrollInputBehavior(_:for:)](<webviewscrollinputbehavior(__for_).md>) — Enables or disables scrolling in web views when using particular inputs.
- [webViewTextSelection(_:)](<webviewtextselection(__).md>) — Determines whether to allow people to select or otherwise interact with text.
