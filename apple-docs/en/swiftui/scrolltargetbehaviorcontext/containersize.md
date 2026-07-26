---
title: containerSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltargetbehaviorcontext/containersize
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltargetbehaviorcontext/containersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltargetbehaviorcontext/containersize.json'
content_hash: 'sha256:69e7dee43d8aff52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTargetBehaviorContext](../scrolltargetbehaviorcontext.md)

# containerSize

<sub>Instance Property</sub>

The size of the container of the scrollable view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var containerSize: CGSize { get }
```

## Discussion

This is the size of the bounds of the scroll view subtracting any insets applied to the scroll view (like the safe area).

## See Also

### Getting the scroll target behavior context

- [axes](axes.md) — The axes in which the scrollable view is scrollable.
- [contentSize](contentsize.md) — The size of the content of the scrollable view.
- [originalTarget](originaltarget.md) — The original target when the scroll gesture began.
- [velocity](velocity.md) — The current velocity of the scrollable view’s scroll gesture.
