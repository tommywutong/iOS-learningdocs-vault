---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/viewspacing/init()
source_url: 'https://developer.apple.com/documentation/swiftui/viewspacing/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewspacing/init%28%29.json'
content_hash: 'sha256:a354feb201dfea3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewSpacing](../viewspacing.md)

# init()

<sub>Initializer</sub>

Initializes an instance with default spacing values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

Use this initializer to create a spacing preferences instance with default values. Then use [formUnion(_:edges:)](<formunion(__edges_).md>) to combine preferences from other views with the new instance. You typically do this in a custom layout’s implementation of the [spacing(subviews:cache:)](<../layout/spacing(subviews_cache_).md>) method.

## See Also

### Creating spacing instances

- [zero](zero.md) — A view spacing instance that contains zero on all edges.
