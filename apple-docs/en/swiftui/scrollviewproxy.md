---
title: ScrollViewProxy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollviewproxy
source_url: 'https://developer.apple.com/documentation/swiftui/scrollviewproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollviewproxy.json'
content_hash: 'sha256:6f814d459ba5a7b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollViewProxy

<sub>Structure</sub>

A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollViewProxy
```

## Overview

You don’t create instances of `ScrollViewProxy` directly. Instead, your [ScrollViewReader](scrollviewreader.md) receives an instance of `ScrollViewProxy` in its `content` content builder. You use actions within this content builder, such as button and gesture handlers or the [onChange(of:perform:)](<view/onchange(of_perform_).md>) method, to call the proxy’s [scrollTo(_:anchor:)](<scrollviewproxy/scrollto(__anchor_).md>) method.

## Topics

### Performing scrolling

- [scrollTo(_:anchor:)](<scrollviewproxy/scrollto(__anchor_).md>) — Scans all scroll views contained by the proxy for the first with a child view with identifier `id`, and then scrolls to that view.

## See Also

### Creating a scroll view

- [ScrollView](scrollview.md) — A scrollable view.
- [ScrollViewReader](scrollviewreader.md) — A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.
