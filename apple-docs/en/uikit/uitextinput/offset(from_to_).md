---
title: 'offset(from:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/offset(from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/offset(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/offset%28from%3Ato%3A%29.json'
content_hash: 'sha256:dbe04ef4d8a54cf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# offset(from:to:)

<sub>Instance Method</sub>

Returns the number of UTF-16 characters between one text position and another text position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func offset(from: UITextPosition, to toPosition: UITextPosition) -> Int
```

## Parameters

- `from` — A custom object that represents a location within a document.

- `toPosition` — A custom object that represents another location within document.

## Return Value

The number of UTF-16 characters between `fromPosition` and `toPosition`.

## See Also

### Evaluating text positions

- [- comparePosition:toPosition:](<compare(__to_).md>) — Returns how one text position compares to another text position.
