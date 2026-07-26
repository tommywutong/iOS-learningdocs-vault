---
title: ScrollViewReader
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollviewreader
source_url: 'https://developer.apple.com/documentation/swiftui/scrollviewreader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollviewreader.json'
content_hash: 'sha256:69251297f5927415'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollViewReader

<sub>Structure</sub>

A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct ScrollViewReader<Content> where Content : View
```

## Overview

The scroll view reader’s content content builder receives a [ScrollViewProxy](scrollviewproxy.md) instance; you use the proxy’s [scrollTo(_:anchor:)](<scrollviewproxy/scrollto(__anchor_).md>) to perform scrolling.

The following example creates a [ScrollView](scrollview.md) containing 100 views that together display a color gradient. It also contains two buttons, one each at the top and bottom. The top button tells the [ScrollViewProxy](scrollviewproxy.md) to scroll to the bottom button, and vice versa.

```swift
@Namespace var topID
@Namespace var bottomID

var body: some View {
    ScrollViewReader { proxy in
        ScrollView {
            Button("Scroll to Bottom") {
                withAnimation {
                    proxy.scrollTo(bottomID)
                }
            }
            .id(topID)

            VStack(spacing: 0) {
                ForEach(0..<100) { i in
                    color(fraction: Double(i) / 100)
                        .frame(height: 32)
                }
            }

            Button("Top") {
                withAnimation {
                    proxy.scrollTo(topID)
                }
            }
            .id(bottomID)
        }
    }
}

func color(fraction: Double) -> Color {
    Color(red: fraction, green: 1 - fraction, blue: 0.5)
}
```

![A scroll view, with a button labeled “Scroll to Bottom” at top.](../../../attachments/8735b201580f404d498324837faf9233/SwiftUI-ScrollViewReader-scroll-to-bottom-button@2x.png)

> [!important] Important
> You may not use the [ScrollViewProxy](scrollviewproxy.md) during execution of the `content` content builder; doing so results in a runtime error. Instead, only actions created within `content` can call the proxy, such as gesture handlers or a view’s `onChange(of:perform:)` method.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a scroll view reader

- [init(content:)](<scrollviewreader/init(content_).md>) — Creates an instance that can perform programmatic scrolling of its child scroll views.

### Configuring a scroll view reader

- [content](scrollviewreader/content.md) — The content builder that creates the reader’s content.

## See Also

### Creating a scroll view

- [ScrollView](scrollview.md) — A scrollable view.
- [ScrollViewProxy](scrollviewproxy.md) — A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.
