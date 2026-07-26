---
title: LayoutSubviews
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutsubviews
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubviews.json'
content_hash: 'sha256:f04c61401c4c0939'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LayoutSubviews

<sub>Structure</sub>

A collection of proxy values that represent the subviews of a layout view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LayoutSubviews
```

## Overview

You receive a `LayoutSubviews` input to your implementations of [Layout](layout.md) protocol methods, like [placeSubviews(in:proposal:subviews:cache:)](<layout/placesubviews(in_proposal_subviews_cache_).md>) and [sizeThatFits(proposal:subviews:cache:)](<layout/sizethatfits(proposal_subviews_cache_).md>). The `subviews` parameter (which the protocol aliases to the [Subviews](layout/subviews.md) type) is a collection that contains proxies for the layout’s subviews (of type [LayoutSubview](layoutsubview.md)). The proxies appear in the collection in the same order that they appear in the [ContentBuilder](contentbuilder.md) input to the layout container. Use the proxies to perform layout operations.

Access the proxies in the collection as you would the contents of any Swift random-access collection. For example, you can enumerate all of the subviews and their indices to inspect or operate on them:

```swift
for (index, subview) in subviews.enumerated() {
    // ...
}
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Equatable](../swift/equatable.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Getting the layout direction

- [layoutDirection](layoutsubviews/layoutdirection.md) — The layout direction inherited by the container view.

### Accessing subviews

- [subscript(_:)](<layoutsubviews/subscript(__).md>) — Gets the subview proxies in the specified range.
- [startIndex](layoutsubviews/startindex.md) — The index of the first subview.
- [endIndex](layoutsubviews/endindex.md) — An index that’s one higher than the last subview.
- [Element](layoutsubviews/element.md) — A type that contains a proxy value.
- [Index](layoutsubviews/index.md) — A type that you can use to index proxy values.
- [SubSequence](layoutsubviews/subsequence.md) — A type that contains a subsequence of proxy values.

## See Also

### Creating a custom layout container

- [Composing custom layouts with SwiftUI](composing-custom-layouts-with-swiftui.md) — Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [Layout](layout.md) — A type that defines the geometry of a collection of views.
- [LayoutSubview](layoutsubview.md) — A proxy that represents one subview of a layout.
