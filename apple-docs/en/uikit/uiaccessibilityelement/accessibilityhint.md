---
title: accessibilityHint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityelement/accessibilityhint
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilityhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityelement/accessibilityhint.json'
content_hash: 'sha256:7e3da1012c353e03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityElement](../uiaccessibilityelement.md)

# accessibilityHint

<sub>Instance Property</sub>

A string that briefly describes the result of performing an action on the accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessibilityHint: String? { get set }
```

## Discussion

The hint is a brief, localized description of the result of performing an action on the element without identifying the element or the action. For example, the hint for a table row that contains an email message might be “Selects the message,” but not “Tap this row to select the message.”

By default, standard UIKit controls and views have system-provided hints. If you provide a custom control or view, however, you need to set this property appropriately so that assistive applications can supply accurate information to users with disabilities.

## See Also

### Accessing the attributes of an accessibility element

- [accessibilityLabel](accessibilitylabel.md) — A string that succinctly identifies the accessibility element.
- [accessibilityValue](accessibilityvalue.md) — A string that represents the current value of the accessibility element.
- [accessibilityFrame](accessibilityframe.md) — The frame of the accessibility element, in screen coordinates.
- [accessibilityFrameInContainerSpace](accessibilityframeincontainerspace.md) — The frame of the accessibility element, in the coordinate space of its container view.
- [accessibilityTraits](accessibilitytraits.md) — The combination of traits that best characterize the accessibility element.
