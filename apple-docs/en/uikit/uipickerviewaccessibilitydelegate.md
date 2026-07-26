---
title: UIPickerViewAccessibilityDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerviewaccessibilitydelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewaccessibilitydelegate.json'
content_hash: 'sha256:5d828f2baa91805f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPickerViewAccessibilityDelegate

<sub>Protocol</sub>

A set of methods you can implement to provide accessibility information for individual components of a picker view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPickerViewAccessibilityDelegate : UIPickerViewDelegate
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIPickerViewDelegate](uipickerviewdelegate.md)

## Topics

### Providing descriptive information

- [- pickerView:accessibilityLabelForComponent:](<uipickerviewaccessibilitydelegate/pickerview(__accessibilitylabelforcomponent_).md>) — Returns a string that identifies the picker view component.
- [- pickerView:accessibilityAttributedLabelForComponent:](<uipickerviewaccessibilitydelegate/pickerview(__accessibilityattributedlabelforcomponent_).md>) — Returns an attributed string that identifies the picker view component.
- [- pickerView:accessibilityHintForComponent:](<uipickerviewaccessibilitydelegate/pickerview(__accessibilityhintforcomponent_).md>) — Returns a string that describes the result of performing an action on the component.
- [- pickerView:accessibilityAttributedHintForComponent:](<uipickerviewaccessibilitydelegate/pickerview(__accessibilityattributedhintforcomponent_).md>) — Returns an attributed string that describes the result of performing an action on the specified component.
- [- pickerView:accessibilityUserInputLabelsForComponent:](<uipickerviewaccessibilitydelegate/pickerview(__accessibilityuserinputlabelsforcomponent_).md>)
- [- pickerView:accessibilityAttributedUserInputLabelsForComponent:](<uipickerviewaccessibilitydelegate/pickerview(__accessibilityattributeduserinputlabelsforcomponent_).md>)

## See Also

### Elements

- [UIAccessibilityElement](uiaccessibilityelement.md) — An element that should be accessible to users with disabilities, but that isn’t accessible by default.
- [UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md) — A set of methods you can implement to provide accessibility information for a scroll view.
