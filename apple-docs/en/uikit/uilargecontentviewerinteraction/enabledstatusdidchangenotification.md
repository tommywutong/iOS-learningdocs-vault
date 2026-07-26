---
title: enabledStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentviewerinteraction/enabledstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/enabledstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteraction/enabledstatusdidchangenotification.json'
content_hash: 'sha256:85550ef793be8282'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerInteraction](../uilargecontentviewerinteraction.md)

# enabledStatusDidChangeNotification

<sub>Type Property</sub>

A notification the system posts when it enables or disables the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let enabledStatusDidChangeNotification: NSNotification.Name
```

## Discussion

Observe this notification to know whether to enable or disable your custom interaction behaviors. For example, if you add an interaction to a button that needs to cooperate with other gesture recognizers when the large content viewer settings are enabled. This notification lets you enable or disable the interaction accordingly.

## See Also

### Detecting the large content viewer

- [enabled](isenabled.md) — A Boolean value that indicates whether the large content viewer is enabled on the device.
