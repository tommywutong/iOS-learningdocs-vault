---
title: UIFocusItemDeferralMode.always
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitemdeferralmode/always
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemdeferralmode/always'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemdeferralmode/always.json'
content_hash: 'sha256:598c7ec4e67942bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItemDeferralMode](../uifocusitemdeferralmode.md)

# UIFocusItemDeferralMode.always

<sub>Case</sub>

Always defer focus for this item, even if deferral is disabled right now. This means a programmatic update to this item would result in focus disappearing until the user interacts with the focus engine again.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case always
```
