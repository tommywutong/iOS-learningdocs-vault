---
title: 'formUnion(_:edges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewspacing/formunion(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewspacing/formunion(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewspacing/formunion%28_%3Aedges%3A%29.json'
content_hash: 'sha256:720c668ac33d2b3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewSpacing](../viewspacing.md)

# formUnion(_:edges:)

<sub>Instance Method</sub>

Merges the spacing preferences of another spacing instance with this instance for a specified set of edges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formUnion(_ other: ViewSpacing, edges: Edge.Set = .all)
```

## Parameters

- `other` — Another spacing preferences instances to merge with this one.

- `edges` — The edges to merge. Edges that you don’t specify are unchanged after the method completes.

## Discussion

When you merge another spacing preference instance with this one, this instance ends up with the greater of its original value or the other instance’s value for each of the specified edges. You can call the method repeatedly with each value in a collection to merge a collection of preferences. The result has the smallest preferences on each edge that meets the largest requirements of all the inputs for that edge.

If you want to merge preferences without modifying the original instance, use [union(_:edges:)](<union(__edges_).md>) instead.

## See Also

### Merging spacing instances

- [union(_:edges:)](<union(__edges_).md>) — Gets a new value that merges the spacing preferences of another spacing instance with this instance for a specified set of edges.
