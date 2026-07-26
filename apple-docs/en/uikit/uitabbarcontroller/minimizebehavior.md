---
title: UITabBarController.MinimizeBehavior
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/minimizebehavior
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/minimizebehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/minimizebehavior.json'
content_hash: 'sha256:a40b0325e3d9418e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# UITabBarController.MinimizeBehavior

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum MinimizeBehavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UITabBarMinimizeBehaviorAutomatic](minimizebehavior/automatic.md) — Resolves to the system default minimize behavior.
- [UITabBarMinimizeBehaviorNever](minimizebehavior/never.md) — The tab bar does not minimize.
- [UITabBarMinimizeBehaviorOnScrollDown](minimizebehavior/onscrolldown.md) — The tab bar minimizes when scrolling down, and expands when scrolling back up.
- [UITabBarMinimizeBehaviorOnScrollUp](minimizebehavior/onscrollup.md) — The tab bar minimizes when scrolling up, and expands when scrolling back down. Recommended if the scroll view content is aligned to the bottom.

### Initializers

- [init(rawValue:)](<minimizebehavior/init(rawvalue_).md>)

## See Also

### Customizing the tab bar behavior

- [delegate](delegate.md) — The tab bar controller’s delegate object.
- [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md) — A set of methods you implement to customize the behavior of a tab bar.
- [tabBarMinimizeBehavior](tabbarminimizebehavior.md) — Defines the minimize behavior for the tab bar, if it is supported.
