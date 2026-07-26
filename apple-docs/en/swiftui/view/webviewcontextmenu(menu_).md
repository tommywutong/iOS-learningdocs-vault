---
title: 'webViewContextMenu(menu:)'
framework: WebKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/webviewcontextmenu(menu:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/webviewcontextmenu(menu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/webviewcontextmenu%28menu%3A%29.json'
content_hash: 'sha256:09ae80a18a777356'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# webViewContextMenu(menu:)

<sub>Instance Method</sub>

Adds an item-based context menu to a WebView, replacing the default set of context menu items.

<sub>macOS</sub>

```swift
nonisolated func webViewContextMenu(@ViewBuilder menu: @escaping @MainActor @Sendable (WebView.ActivatedElementInfo) -> some View) -> some View

```

## Parameters

- `menu` — A closure that produces the menu. The single parameter to the closure describes the type of webpage element that was acted upon.

## Return Value

A view that can display an item-based context menu.

## See Also

### Displaying web content

- [WebView](../../webkit/webview-swift.struct.md) — A view that displays some web content.
- [WebPage](../../webkit/webpage.md) — An object that controls and manages the behavior of interactive web content.
- [onWebViewImmersiveEnvironmentRequest(shouldAllow:present:dismiss:)](<onwebviewimmersiveenvironmentrequest(shouldallow_present_dismiss_).md>) — Manages the lifecycle of immersive environments requested by websites. _(beta)_
- [webViewBackForwardNavigationGestures(_:)](<webviewbackforwardnavigationgestures(__).md>) — Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [webViewContentBackground(_:)](<webviewcontentbackground(__).md>) — Specifies the visibility of the webpage’s natural background color within this view.
- [webViewElementFullscreenBehavior(_:)](<webviewelementfullscreenbehavior(__).md>) — Determines whether a web view can display content full screen.
- [webViewLinkPreviews(_:)](<webviewlinkpreviews(__).md>) — Determines whether pressing a link displays a preview of the destination for the link.
- [webViewMagnificationGestures(_:)](<webviewmagnificationgestures(__).md>) — Determines whether magnify gestures change the view’s magnification.
- [webViewOnScrollGeometryChange(for:of:action:)](<webviewonscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [webViewScrollInputBehavior(_:for:)](<webviewscrollinputbehavior(__for_).md>) — Enables or disables scrolling in web views when using particular inputs.
- [webViewScrollPosition(_:)](<webviewscrollposition(__).md>) — Associates a binding to a scroll position with the web view.
- [webViewTextSelection(_:)](<webviewtextselection(__).md>) — Determines whether to allow people to select or otherwise interact with text.
