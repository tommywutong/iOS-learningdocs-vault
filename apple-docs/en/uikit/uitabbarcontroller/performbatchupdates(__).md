---
title: 'performBatchUpdates(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/performbatchupdates(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/performbatchupdates(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/performbatchupdates%28_%3A%29.json'
content_hash: 'sha256:b3b727276c57c805'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# performBatchUpdates(_:)

<sub>Instance Method</sub>

Animates multiple tab changes as a single update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performBatchUpdates(_ updates: () -> Void)
```

## Discussion

Use this method when you need to make several changes to tab properties simultaneously. Changes made inside the `updates` block are coalesced into a single animated layout pass, preventing intermediate states from being visible to the user.

The `updates` block is called synchronously. You can safely read and write any mutable tab properties inside this block.

## See Also

### Assigning tabs

- [tabs](tabs.md) — An array of tabs that the tab bar displays.
- [- setTabs:animated:](<settabs(__animated_).md>) — Sets the root tabs of the tab bar controller, with an option to animate the change.
