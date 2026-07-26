---
title: 'onWebViewImmersiveEnvironmentRequest(shouldAllow:present:dismiss:)'
framework: WebKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/onwebviewimmersiveenvironmentrequest(shouldallow:present:dismiss:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onwebviewimmersiveenvironmentrequest(shouldallow:present:dismiss:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onwebviewimmersiveenvironmentrequest%28shouldallow%3Apresent%3Adismiss%3A%29.json'
content_hash: 'sha256:cd21deba735c7f0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onWebViewImmersiveEnvironmentRequest(shouldAllow:present:dismiss:)

<sub>Instance Method</sub>

Manages the lifecycle of immersive environments requested by websites.

<sub>visionOS</sub>

```swift
nonisolated func onWebViewImmersiveEnvironmentRequest(shouldAllow: @escaping @MainActor @Sendable (WebPage.FrameInfo) async -> Bool, present: @escaping @MainActor @Sendable (WebPage.ImmersiveEnvironment) async throws -> Void, dismiss: @escaping @MainActor @Sendable (WebPage.ImmersiveEnvironment) async -> Void) -> some View

```

## Parameters

- `shouldAllow` — An async closure called when a website requests an immersive environment. This can be used to request user consent or apply custom authorization logic. It receives the source `WebPage.FrameInfo` and should return `true` to allow the environment presentation, or `false` to deny it.

- `present` — An async throwing closure called after the environment has loaded and is ready for presentation. It receives the `WebPage.ImmersiveEnvironment`. Use this to open an Immersive Space containing a `WebViewImmersiveEnvironmentView` initialized with this environment. If another immersive space is already being presented, dismiss it first. This closure should return after the presentation transition completes.

- `dismiss` — An async closure called when the website or the application asks to dismiss the immersive environment. It receives the `WebPage.ImmersiveEnvironment` to dismiss. This closure should return after the dismissal transition completes.

## Return Value

A modified view that manages immersive environment lifecycle.

## Discussion

Use this modifier to control authorization, presentation, and dismissal of immersive environments from websites.

## See Also

### Displaying web content

- [WebView](../../webkit/webview-swift.struct.md) — A view that displays some web content.
- [WebPage](../../webkit/webpage.md) — An object that controls and manages the behavior of interactive web content.
- [webViewBackForwardNavigationGestures(_:)](<webviewbackforwardnavigationgestures(__).md>) — Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [webViewContentBackground(_:)](<webviewcontentbackground(__).md>) — Specifies the visibility of the webpage’s natural background color within this view.
- [webViewContextMenu(menu:)](<webviewcontextmenu(menu_).md>) — Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [webViewElementFullscreenBehavior(_:)](<webviewelementfullscreenbehavior(__).md>) — Determines whether a web view can display content full screen.
- [webViewLinkPreviews(_:)](<webviewlinkpreviews(__).md>) — Determines whether pressing a link displays a preview of the destination for the link.
- [webViewMagnificationGestures(_:)](<webviewmagnificationgestures(__).md>) — Determines whether magnify gestures change the view’s magnification.
- [webViewOnScrollGeometryChange(for:of:action:)](<webviewonscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [webViewScrollInputBehavior(_:for:)](<webviewscrollinputbehavior(__for_).md>) — Enables or disables scrolling in web views when using particular inputs.
- [webViewScrollPosition(_:)](<webviewscrollposition(__).md>) — Associates a binding to a scroll position with the web view.
- [webViewTextSelection(_:)](<webviewtextselection(__).md>) — Determines whether to allow people to select or otherwise interact with text.
