---
title: 'dynamicAnimatorDidPause(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimatordelegate/dynamicanimatordidpause(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/dynamicanimatordidpause(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimatordelegate/dynamicanimatordidpause%28_%3A%29.json'
content_hash: 'sha256:8d57820f1b8e07a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimatorDelegate](../uidynamicanimatordelegate.md)

# dynamicAnimatorDidPause(_:)

<sub>Instance Method</sub>

Called when a dynamic animator pauses the animations for its behaviors’ associated dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func dynamicAnimatorDidPause(_ animator: UIDynamicAnimator)
```

## Parameters

- `animator` — The dynamic animator that paused its animation.

## See Also

### Responding to animation pausing and resumption

- [- dynamicAnimatorWillResume:](<dynamicanimatorwillresume(__).md>) — Called when a dynamic animator is about to resume the animations for its behaviors’ associated dynamic items.
