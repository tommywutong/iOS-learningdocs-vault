---
title: paging
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltargetbehavior/paging
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltargetbehavior/paging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltargetbehavior/paging.json'
content_hash: 'sha256:eef4c23698d8a38b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTargetBehavior](../scrolltargetbehavior.md)

# paging

<sub>Type Property</sub>

The scroll behavior that aligns scroll targets to container-based geometry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var paging: PagingScrollTargetBehavior { get }
```

## Discussion

In the following example, every view in the lazy stack is flexible in both directions and the scroll view settles to container-aligned boundaries.

```swift
ScrollView {
    LazyVStack(spacing: 0.0) {
        ForEach(items) { item in
            FullScreenItem(item)
        }
    }
}
.scrollTargetBehavior(.paging)
```

## See Also

### Getting the scroll target behavior

- [viewAligned](viewaligned.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [viewAligned(limitBehavior:)](<viewaligned(limitbehavior_).md>) — The scroll behavior that aligns scroll targets to view-based geometry.
