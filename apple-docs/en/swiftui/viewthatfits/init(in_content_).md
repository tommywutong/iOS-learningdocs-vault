---
title: 'init(in:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewthatfits/init(in:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewthatfits/init(in:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewthatfits/init%28in%3Acontent%3A%29.json'
content_hash: 'sha256:c0295725692f2ff5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewThatFits](../viewthatfits.md)

# init(in:content:)

<sub>Initializer</sub>

Produces a view constrained in the given axes from one of several alternatives provided by a content builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(in axes: Axis.Set = [.horizontal, .vertical], @ContentBuilder content: () -> Content)
```

## Parameters

- `axes` — A set of axes to constrain children to. The set may contain [Axis.horizontal](../axis/horizontal.md), [Axis.vertical](../axis/vertical.md), or both of these. `ViewThatFits` chooses the first child whose size fits within the proposed size on these axes. If `axes` is an empty set, `ViewThatFits` uses the first child view. By default, `ViewThatFits` uses both axes.

- `content` — A content builder that provides the child views for this container, in order of preference. The builder chooses the first child view that fits within the proposed width, height, or both, as defined by `axes`.
