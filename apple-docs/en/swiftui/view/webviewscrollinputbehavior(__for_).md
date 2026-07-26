---
title: 'webViewScrollInputBehavior(_:for:)'
framework: WebKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/webviewscrollinputbehavior(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/webviewscrollinputbehavior(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/webviewscrollinputbehavior%28_%3Afor%3A%29.json'
content_hash: 'sha256:8bbe8d5331b802ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# webViewScrollInputBehavior(_:for:)

<sub>Instance Method</sub>

Enables or disables scrolling in web views when using particular inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func webViewScrollInputBehavior(_ behavior: ScrollInputBehavior, for input: ScrollInputKind) -> some View

```

## Parameters

- `behavior` — Whether scrolling should be enabled or disabled for this input.

- `input` — The input for which to enable or disable scrolling.

## Return Value

A view with the configured scroll input behavior for web views.

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
- [webViewScrollPosition(_:)](<webviewscrollposition(__).md>) — Associates a binding to a scroll position with the web view.
- [webViewTextSelection(_:)](<webviewtextselection(__).md>) — Determines whether to allow people to select or otherwise interact with text.
