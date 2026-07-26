---
title: focusItemDeferralMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitem/focusitemdeferralmode
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem/focusitemdeferralmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem/focusitemdeferralmode.json'
content_hash: 'sha256:7a016a2a1fbc0626'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItem](../uifocusitem.md)

# focusItemDeferralMode

<sub>Instance Property</sub>

If this property is present and returns `UIFocusItemDeferralModeNever`, the focus deferral will not be enabled again after the user engagement timeout has expired if this item is currently focused and programmatic focus updates pointing to this item will be executed immediatly. If it returns `UIFocusItemDeferralModeAlways` focus will always be deferred when this item is supposed to be focused. Does nothing when focus deferral is not supported on the platform.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var focusItemDeferralMode: UIFocusItemDeferralMode { get }
```
