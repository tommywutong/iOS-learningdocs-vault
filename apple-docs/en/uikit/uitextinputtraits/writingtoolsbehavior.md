---
title: writingToolsBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/writingtoolsbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/writingtoolsbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/writingtoolsbehavior.json'
content_hash: 'sha256:39d26305118b09d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# writingToolsBehavior

<sub>Instance Property</sub>

The writing tools experience to support in the current view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional var writingToolsBehavior: UIWritingToolsBehavior { get set }
```

## Discussion

Use this property to specify the type of experience to display when someone engages writing tools for a text input view. The system does its best to provide the requested UI, but might offer a more limited experience if required capabilities aren’t available. The default value of this property is [UIWritingToolsBehaviorDefault](../uiwritingtoolsbehavior/default.md), which lets the system choose the most appropriate experience for the current device.

Set the value of this property to [UIWritingToolsBehaviorNone](../uiwritingtoolsbehavior/none.md) if you want to prevent someone from using the writing tools with your view.

## See Also

### Configuring the writing tools experience

- [UIWritingToolsBehavior](../uiwritingtoolsbehavior.md) — Constants that specify the writing tools experience for the underlying view.
