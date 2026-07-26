---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentviewerinteraction/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteraction/isenabled.json'
content_hash: 'sha256:64a2873f83577be8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerInteraction](../uilargecontentviewerinteraction.md)

# isEnabled

<sub>Type Property</sub>

A Boolean value that indicates whether the large content viewer is enabled on the device.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var isEnabled: Bool { get }
```

## Discussion

It isn’t necessary to check this value before adding a [UILargeContentViewerInteraction](../uilargecontentviewerinteraction.md) to a view, but it may be helpful if you need to adjust the behavior of coexisting gesture handlers. For example, a button with a long press handler might increase its long press duration so the user can read the text in the large content viewer first.

## See Also

### Detecting the large content viewer

- [UILargeContentViewerInteractionEnabledStatusDidChangeNotification](enabledstatusdidchangenotification.md) — A notification the system posts when it enables or disables the large content viewer.
