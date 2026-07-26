---
title: 'union(_:edges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewspacing/union(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewspacing/union(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewspacing/union%28_%3Aedges%3A%29.json'
content_hash: 'sha256:e0fb4552bbee4378'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewSpacing](../viewspacing.md)

# union(_:edges:)

<sub>Instance Method</sub>

Gets a new value that merges the spacing preferences of another spacing instance with this instance for a specified set of edges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func union(_ other: ViewSpacing, edges: Edge.Set = .all) -> ViewSpacing
```

## Parameters

- `other` — Another spacing preferences instance to merge with this one.

- `edges` — The edges to merge. Edges that you don’t specify are unchanged after the method completes.

## Return Value

A new view spacing preferences instance with the merged values.

## Discussion

This method behaves like [formUnion(_:edges:)](<formunion(__edges_).md>), except that it creates a copy of the original spacing preferences instance before merging, leaving the original instance unmodified.

## See Also

### Merging spacing instances

- [formUnion(_:edges:)](<formunion(__edges_).md>) — Merges the spacing preferences of another spacing instance with this instance for a specified set of edges.
