---
title: WebView
framework: WebKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/webkit/webview-swift.struct
source_url: 'https://developer.apple.com/documentation/webkit/webview-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webview-swift.struct.json'
content_hash: 'sha256:a63f9c171247ac78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebView

<sub>Structure</sub>

A view that displays some web content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct WebView
```

## Overview

Present HTML, CSS, and JavaScript content alongside your app’s native views with [WebView](webview-swift.struct.md). Specify web content with a [URL](../foundation/url.md) when using the [init(url:)](<webview-swift.struct/init(url_).md>) initializer, or with a [WebPage](webpage.md) when using the [init(_:)](<webview-swift.struct/init(__).md>) initializer, which allows you to fully control the browsing experience. Any updates to the page propagate the information to the view.

[WebView](webview-swift.struct.md) provides a complete browsing experience, including the ability to navigate between different webpages using links, forward and back buttons, and more. When a person clicks a link in your content, the view acts like a browser and displays the content at that link. To customize navigation, use a [WebPage](webpage.md) with your [WebView](webview-swift.struct.md) and customize the [Configuration](webpage/configuration.md), or create a new type that conforms to [NavigationDeciding](webpage/navigationdeciding.md).

The following example displays two different URLs depending on the state of a toggle, and also prevents back-forward navigation gestures:

```swift
import SwiftUI
import WebKit

struct ContentView: View {
    @State private var toggle = false

    private var url: URL? {
        toggle ? URL(string: "https://www.webkit.org") : URL(string: "https://www.swift.org")
    }

    var body: some View {
        WebView(url: url)
            .toolbar {
                Button(buttonName, systemImage: buttonIcon) {
                    toggle.toggle()
                }
            }
            .webViewBackForwardNavigationGestures(.disabled)
    }
}
```

A [WebView](webview-swift.struct.md) is a scrollable view, and behaves similarly to [ScrollView](../swiftui/scrollview.md). Customize scrolling in a [WebView](webview-swift.struct.md) with:

- [scrollBounceBehavior(_:axes:)](<../swiftui/view/scrollbouncebehavior(__axes_).md>)
- [webViewScrollInputBehavior(_:for:)](<../swiftui/view/webviewscrollinputbehavior(__for_).md>)
- [webViewScrollPosition(_:)](<../swiftui/view/webviewscrollposition(__).md>)
- [webViewOnScrollGeometryChange(for:of:action:)](<../swiftui/view/webviewonscrollgeometrychange(for_of_action_).md>)

Customize [WebView](webview-swift.struct.md) display and interactions with view modifiers, such as:

- [webViewBackForwardNavigationGestures(_:)](<../swiftui/view/webviewbackforwardnavigationgestures(__).md>)
- [webViewMagnificationGestures(_:)](<../swiftui/view/webviewmagnificationgestures(__).md>)
- [webViewLinkPreviews(_:)](<../swiftui/view/webviewlinkpreviews(__).md>)
- [webViewTextSelection(_:)](<../swiftui/view/webviewtextselection(__).md>)
- [webViewElementFullscreenBehavior(_:)](<../swiftui/view/webviewelementfullscreenbehavior(__).md>)
- [webViewContextMenu(menu:)](<../swiftui/view/webviewcontextmenu(menu_).md>)
- [webViewContentBackground(_:)](<../swiftui/view/webviewcontentbackground(__).md>)

To further customize and control a web interaction, connect a [WebView](webview-swift.struct.md) to a [WebPage](webpage.md). The following example demonstrates this by configuring the view’s navigation title to be the webpage’s title, which the system updates automatically because [WebPage](webpage.md) is an `Observable` type:

```swift
struct ContentView: View {
    @State private var page = WebPage()

    var body: some View {
        NavigationStack {
            WebView(page)
                .navigationTitle(page.title)
        }
    }
}
```

You can only bind a [WebPage](webpage.md) to a single [WebView](webview-swift.struct.md) at a time.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating web views

- [init(_:)](<webview-swift.struct/init(__).md>) — Create a new WebView.
- [init(url:)](<webview-swift.struct/init(url_).md>) — Create a new WebView with the specified URL.

### Modifying web interactions

- [BackForwardNavigationGesturesBehavior](webview-swift.struct/backforwardnavigationgesturesbehavior.md) — A type that defines the behavior of how horizontal swipe gestures trigger backward and forward page navigation.
- [LinkPreviewBehavior](webview-swift.struct/linkpreviewbehavior.md) — A type specifying the behavior for the presentation of link previews when pressing a link.
- [ActivatedElementInfo](webview-swift.struct/activatedelementinfo.md) — Contains information about an element the user activated in a webpage, which may be used to configure a context menu for that element.
- [ElementFullscreenBehavior](webview-swift.struct/elementfullscreenbehavior.md) — The behavior that determines whether a web view can display content full screen.
- [MagnificationGesturesBehavior](webview-swift.struct/magnificationgesturesbehavior.md) — The options for controlling the behavior for how magnification gestures interact with web views.

## See Also

### Essentials

- [Building a cross-platform web browser](building-a-cross-platform-web-browser.md) — Implement a browser on multiple platforms that loads content, manages navigation history, and saves favorite websites, using WebKit for SwiftUI.
- [WebPage](webpage.md) — An object that controls and manages the behavior of interactive web content.
