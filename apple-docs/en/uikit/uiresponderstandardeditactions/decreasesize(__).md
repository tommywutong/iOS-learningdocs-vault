---
title: 'decreaseSize(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/decreasesize(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/decreasesize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/decreasesize%28_%3A%29.json'
content_hash: 'sha256:6ad66ae977d46cb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# decreaseSize(_:)

<sub>Instance Method</sub>

Decreases the size of the current object by one unit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func decreaseSize(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

Use this method to decrease the size of the selected text or other content. You are responsible for defining the magnitude of the change.

## See Also

### Handling size changes

- [- increaseSize:](<increasesize(__).md>) — Increases the size of the current object by one unit.
