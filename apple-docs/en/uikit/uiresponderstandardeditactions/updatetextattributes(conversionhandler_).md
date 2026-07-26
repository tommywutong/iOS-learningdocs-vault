---
title: 'updateTextAttributes(conversionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/updatetextattributes(conversionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/updatetextattributes(conversionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/updatetextattributes%28conversionhandler%3A%29.json'
content_hash: 'sha256:4c9613e8c1131abb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# updateTextAttributes(conversionHandler:)

<sub>Instance Method</sub>

Tells your app to update the attributes of the currently selected text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func updateTextAttributes(conversionHandler: ([NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any])
```

## Parameters

- `conversionHandler` — A handler block that you execute to retrieve the new attributes selected by the user. This block returns a dictionary containing the new values to apply to the text selection, and it takes the following parameter: - **attributes** — The dictionary of attributes that your app supports for the selected text. Specify all of the attributes and their current values.

## Discussion

Implement this method if your app supports attributes that aren’t represented by other action methods such as [- toggleBoldface:](<toggleboldface(__).md>). The system calls this method to let responders know that the user or system applied new attributes for you to apply the current selection. In your implementation of this method, get the dictionary of the attributes associated with the selected content and pass it as a parameter to the `conversionHandler` block. When the block returns, apply the returned attributes to the selected text.
