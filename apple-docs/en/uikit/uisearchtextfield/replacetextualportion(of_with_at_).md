---
title: 'replaceTextualPortion(of:with:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtextfield/replacetextualportion(of:with:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/replacetextualportion(of:with:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/replacetextualportion%28of%3Awith%3Aat%3A%29.json'
content_hash: 'sha256:64d9e58acbac64ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# replaceTextualPortion(of:with:at:)

<sub>Instance Method</sub>

Converts text in a search field into a search token.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func replaceTextualPortion(of textRange: UITextRange, with token: UISearchToken, at tokenIndex: Int)
```

## Parameters

- `textRange` — The text to remove.

- `token` — The token to add.

- `tokenIndex` — The location for the added token.

## Discussion

This method removes any text in the specified range, inserts the provided token at the specified index, and selects the newly inserted token. Prefer using this convenience method over performing each step with other methods. When your app calls [- replaceTextualPortionOfRange:withToken:atIndex:](<replacetextualportion(of_with_at_).md>), UIKit commits any marked text before modifying the text, and creates a single undo group.

This method doesn’t remove any tokens in the `textRange`, so you don’t have to manually trim the [selectedTextRange](../uitextinput/selectedtextrange.md) before you use it in this method.

## See Also

### Converting text into tokens

- [textualRange](textualrange.md) — The range of the field’s text content.
