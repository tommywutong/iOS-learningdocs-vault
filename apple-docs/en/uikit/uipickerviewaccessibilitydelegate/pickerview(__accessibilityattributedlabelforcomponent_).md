---
title: 'pickerView(_:accessibilityAttributedLabelForComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedlabelforcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedlabelforcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview%28_%3Aaccessibilityattributedlabelforcomponent%3A%29.json'
content_hash: 'sha256:5ea366aa4dfe9e11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewAccessibilityDelegate](../uipickerviewaccessibilitydelegate.md)

# pickerView(_:accessibilityAttributedLabelForComponent:)

<sub>Instance Method</sub>

Returns an attributed string that identifies the picker view component.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, accessibilityAttributedLabelForComponent component: Int) -> NSAttributedString?
```

## Parameters

- `pickerView` — The picker view object.

- `component` — The component in the picker view that requires a label.

## Return Value

The attributed string that identifies the picker view component

## Discussion

Use this method to provide descriptive information for the components of a picker view. Your attributed string may include the [UIAccessibilitySpeechAttributeLanguage](../uiaccessibilityspeechattributelanguage.md) attribute, which lets you use different language synthesizers for different parts of the string. The system prefers this method over the [- pickerView:accessibilityLabelForComponent:](<pickerview(__accessibilitylabelforcomponent_).md>) method. For in-depth information on how to create an appropriate descriptive string, see [Crafting Useful Labels and Hints](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Making_Application_Accessible/Making_Application_Accessible.html#//apple_ref/doc/uid/TP40008785-CH102-SW6).

## See Also

### Providing descriptive information

- [- pickerView:accessibilityLabelForComponent:](<pickerview(__accessibilitylabelforcomponent_).md>) — Returns a string that identifies the picker view component.
- [- pickerView:accessibilityHintForComponent:](<pickerview(__accessibilityhintforcomponent_).md>) — Returns a string that describes the result of performing an action on the component.
- [- pickerView:accessibilityAttributedHintForComponent:](<pickerview(__accessibilityattributedhintforcomponent_).md>) — Returns an attributed string that describes the result of performing an action on the specified component.
- [- pickerView:accessibilityUserInputLabelsForComponent:](<pickerview(__accessibilityuserinputlabelsforcomponent_).md>)
- [- pickerView:accessibilityAttributedUserInputLabelsForComponent:](<pickerview(__accessibilityattributeduserinputlabelsforcomponent_).md>)
