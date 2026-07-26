---
title: UIWritingToolsBehavior.default
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolsbehavior/default
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolsbehavior/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolsbehavior/default.json'
content_hash: 'sha256:b6d0849b27dda924'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsBehavior](../uiwritingtoolsbehavior.md)

# UIWritingToolsBehavior.default

<sub>Case</sub>

An option to let the system determine the best way to enable writing tools for the view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case `default`
```

## Discussion

The system chooses a complete, limited, or none experience based on the device-level support for the feature.

## See Also

### Getting the writing tools behaviors

- [UIWritingToolsBehaviorNone](none.md) — An option to prevent the writing tools from modifying the text in the view.
- [UIWritingToolsBehaviorComplete](complete.md) — An option to provide the complete writing tools experience for the text view.
- [UIWritingToolsBehaviorLimited](limited.md) — An option to provide a limited, overlay-panel experience for the text view.
