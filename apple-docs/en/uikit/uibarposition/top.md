---
title: UIBarPosition.top
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarposition/top
source_url: 'https://developer.apple.com/documentation/uikit/uibarposition/top'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarposition/top.json'
content_hash: 'sha256:ff0e7877b6b24ac0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarPosition](../uibarposition.md)

# UIBarPosition.top

<sub>Case</sub>

Specifies that the bar is at the top of its containing view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case top
```

## Discussion

The system uses this as a hint to draw directional decoration accordingly. For example, any shadow would be drawn below the bar.

Instances of [UIToolbar](../uitoolbar.md) do not appear with this position on iPhone, but they can on iPad.

## See Also

### Constants

- [UIBarPositionAny](any.md) — Specifies that the position is unspecified.
- [UIBarPositionBottom](bottom.md) — Specifies that the bar is at the bottom of its containing view.
- [UIBarPositionTopAttached](topattached.md) — Specifies that the bar is at the top of the screen, as well as its containing view.
