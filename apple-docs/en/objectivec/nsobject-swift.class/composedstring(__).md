---
title: 'composedString(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/composedstring(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/composedstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/composedstring%28_%3A%29.json'
content_hash: 'sha256:a345ab2365e54e69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# composedString(_:)

<sub>Instance Method</sub>

Return the current composed string.

<sub>macOS</sub>

```swift
func composedString(_ sender: Any!) -> Any!
```

## Parameters

- `sender` — The client object requesting the string.

## Return Value

The current composed string, which can be an `NSString` or `NSAttributedString` object. The returned object should be an autoreleased object.

## Discussion

A composed string refers to the buffer that an input method typically maintains to mirror the text contained in the active inline area. It is called the composed string to reflect the fact that the input method composed the string by converting the characters input by the user. In addition, using the term composed string makes it easier to differentiate between an input method  buffer and the text in the active inline area that the user sees.
