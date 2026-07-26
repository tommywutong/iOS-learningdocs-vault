---
title: 'pickerView(_:accessibilityAttributedUserInputLabelsForComponent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributeduserinputlabelsforcomponent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributeduserinputlabelsforcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview%28_%3Aaccessibilityattributeduserinputlabelsforcomponent%3A%29.json'
content_hash: 'sha256:dd0d7dfaca5e1655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPickerViewAccessibilityDelegate](../uipickerviewaccessibilitydelegate.md)

# pickerView(_:accessibilityAttributedUserInputLabelsForComponent:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pickerView(_ pickerView: UIPickerView, accessibilityAttributedUserInputLabelsForComponent component: Int) -> [NSAttributedString]
```

## See Also

### Providing descriptive information

- [- pickerView:accessibilityLabelForComponent:](<pickerview(__accessibilitylabelforcomponent_).md>) — Returns a string that identifies the picker view component.
- [- pickerView:accessibilityAttributedLabelForComponent:](<pickerview(__accessibilityattributedlabelforcomponent_).md>) — Returns an attributed string that identifies the picker view component.
- [- pickerView:accessibilityHintForComponent:](<pickerview(__accessibilityhintforcomponent_).md>) — Returns a string that describes the result of performing an action on the component.
- [- pickerView:accessibilityAttributedHintForComponent:](<pickerview(__accessibilityattributedhintforcomponent_).md>) — Returns an attributed string that describes the result of performing an action on the specified component.
- [- pickerView:accessibilityUserInputLabelsForComponent:](<pickerview(__accessibilityuserinputlabelsforcomponent_).md>)
