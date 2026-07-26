---
title: UIFocusItemDeferralMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitemdeferralmode
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemdeferralmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemdeferralmode.json'
content_hash: 'sha256:607f908e264a3ae6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusItemDeferralMode

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIFocusItemDeferralMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIFocusItemDeferralModeAlways](uifocusitemdeferralmode/always.md) — Always defer focus for this item, even if deferral is disabled right now. This means a programmatic update to this item would result in focus disappearing until the user interacts with the focus engine again.
- [UIFocusItemDeferralModeAutomatic](uifocusitemdeferralmode/automatic.md) — Use the system default behavior.
- [UIFocusItemDeferralModeNever](uifocusitemdeferralmode/never.md) — Never defer focus for this item. When a programmatic focus update lands on this item, it will always be and appear focused even if focus deferral is currently enabled.

### Initializers

- [init(rawValue:)](<uifocusitemdeferralmode/init(rawvalue_).md>)

## See Also

### Enumerations

- [ExpandedStatus](uiaccessibility/expandedstatus.md)
- [ComponentSize](uitextformattingviewcontroller/componentsize.md) — Sizes of text formatting view controller components.
- [UIBarMinimizationBehavior](uibarminimizationbehavior.md) _(beta)_
- [UIBarMinimizationRestorationBehavior](uibarminimizationrestorationbehavior.md) _(beta)_
- [UIBarMinimizationSafeAreaAdjustment](uibarminimizationsafeareaadjustment.md) _(beta)_
