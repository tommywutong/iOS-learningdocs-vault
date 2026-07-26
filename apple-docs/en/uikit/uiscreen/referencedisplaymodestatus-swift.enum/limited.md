---
title: UIScreen.ReferenceDisplayModeStatus.limited
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum/limited
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum/limited'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum/limited.json'
content_hash: 'sha256:42829c1a58ab9017'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScreen](../../uiscreen.md) · [ReferenceDisplayModeStatus](../referencedisplaymodestatus-swift.enum.md)

# UIScreen.ReferenceDisplayModeStatus.limited

<sub>Case</sub>

A status that indicates the screen’s in a limited reference display mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case limited
```

## Discussion

The screen may be unable to provide an accurate reference display mode due to thermal or power constraints.

## See Also

### Statuses

- [UIScreenReferenceDisplayModeStatusNotSupported](notsupported.md) — A status that indicates the screen doesn’t provide a reference display mode.
- [UIScreenReferenceDisplayModeStatusNotEnabled](notenabled.md) — A status that indicates the screen provides a reference display mode but it’s in a disabled state.
- [UIScreenReferenceDisplayModeStatusEnabled](enabled.md) — A status that indicates the screen’s in an accurate reference display mode.
