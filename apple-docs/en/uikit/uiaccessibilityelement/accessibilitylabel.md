---
title: accessibilityLabel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityelement/accessibilitylabel
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilitylabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityelement/accessibilitylabel.json'
content_hash: 'sha256:3850f90e14957fe4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityElement](../uiaccessibilityelement.md)

# accessibilityLabel

<sub>Instance Property</sub>

A string that succinctly identifies the accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessibilityLabel: String? { get set }
```

## Discussion

The label is a very short, localized string that identifies the accessibility element, but does not include the type of the control or view. For example, the label for a Save button is “Save,” not “Save button.”

By default, standard UIKit controls and views have labels that derive from their titles. If you provide a custom control or view, however, you need to set this property appropriately so that assistive applications can supply accurate information to users with disabilities.

## See Also

### Accessing the attributes of an accessibility element

- [accessibilityHint](accessibilityhint.md) — A string that briefly describes the result of performing an action on the accessibility element.
- [accessibilityValue](accessibilityvalue.md) — A string that represents the current value of the accessibility element.
- [accessibilityFrame](accessibilityframe.md) — The frame of the accessibility element, in screen coordinates.
- [accessibilityFrameInContainerSpace](accessibilityframeincontainerspace.md) — The frame of the accessibility element, in the coordinate space of its container view.
- [accessibilityTraits](accessibilitytraits.md) — The combination of traits that best characterize the accessibility element.
