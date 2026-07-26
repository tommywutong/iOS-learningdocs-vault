---
title: 'updateTarget(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltargetbehavior/updatetarget(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltargetbehavior/updatetarget(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltargetbehavior/updatetarget%28_%3Acontext%3A%29.json'
content_hash: 'sha256:ef8892f479ddc98f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTargetBehavior](../scrolltargetbehavior.md)

# updateTarget(_:context:)

<sub>Instance Method</sub>

Updates the proposed target that a scrollable view should scroll to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func updateTarget(_ target: inout ScrollTarget, context: Self.TargetContext)
```

## Discussion

The system calls this method in two main cases:

- When a scroll gesture ends, it calculates where it would naturally scroll to using its deceleration rate. The system provides this calculated value as the target of this method.
- When a scrollable view’s size changes, it calculates where it should be scrolled given the new size and provides this calculates value as the target of this method.

You can implement this method to override the calculated target which will have the scrollable view scroll to a different position than it would otherwise.

## See Also

### Updating the proposed target

- [TargetContext](targetcontext.md) — The context in which a scroll behavior updates the scroll target.
