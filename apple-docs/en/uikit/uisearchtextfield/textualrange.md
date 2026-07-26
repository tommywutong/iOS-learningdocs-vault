---
title: textualRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfield/textualrange
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/textualrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/textualrange.json'
content_hash: 'sha256:7278d5a695237494'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# textualRange

<sub>Instance Property</sub>

The range of the field’s text content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var textualRange: UITextRange { get }
```

## Discussion

Both tokens and text are included in the range from [beginningOfDocument](../uitextinput/beginningofdocument.md) to [endOfDocument](../uitextinput/endofdocument.md). This property provides convenient access to just the text.

## See Also

### Converting text into tokens

- [- replaceTextualPortionOfRange:withToken:atIndex:](<replacetextualportion(of_with_at_).md>) — Converts text in a search field into a search token.
