---
title: 'pickerView(_:accessibilityLabelForComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview%28_%3Aaccessibilitylabelforcomponent%3A%29.json'
content_hash: 'sha256:4edcf930505e2a5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewAccessibilityDelegate](../uipickerviewaccessibilitydelegate.md)

# pickerView(_:accessibilityLabelForComponent:)

<sub>Instance Method</sub>

Returns a string that identifies the picker view component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String?
```

## Parameters

- `pickerView` — The picker view object.

- `component` — The component in the picker view that requires a label.

## Return Value

A succinct label, in a localized string, that identifies the picker view component.

## Discussion

Implement this optional method to ensure that the accessibility element representing the picker view provides an appropriate label for each component. The system prefers the [- pickerView:accessibilityAttributedLabelForComponent:](<pickerview(__accessibilityattributedlabelforcomponent_).md>) method over this one. For in-depth information on how to create an appropriate label, see [Crafting Useful Labels and Hints](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Making_Application_Accessible/Making_Application_Accessible.html#//apple_ref/doc/uid/TP40008785-CH102-SW6).

## See Also

### Providing descriptive information

- [- pickerView:accessibilityAttributedLabelForComponent:](<pickerview(__accessibilityattributedlabelforcomponent_).md>) — Returns an attributed string that identifies the picker view component.
- [- pickerView:accessibilityHintForComponent:](<pickerview(__accessibilityhintforcomponent_).md>) — Returns a string that describes the result of performing an action on the component.
- [- pickerView:accessibilityAttributedHintForComponent:](<pickerview(__accessibilityattributedhintforcomponent_).md>) — Returns an attributed string that describes the result of performing an action on the specified component.
- [- pickerView:accessibilityUserInputLabelsForComponent:](<pickerview(__accessibilityuserinputlabelsforcomponent_).md>)
- [- pickerView:accessibilityAttributedUserInputLabelsForComponent:](<pickerview(__accessibilityattributeduserinputlabelsforcomponent_).md>)
