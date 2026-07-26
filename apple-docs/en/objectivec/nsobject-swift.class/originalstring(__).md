---
title: 'originalString(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/originalstring(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/originalstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/originalstring%28_%3A%29.json'
content_hash: 'sha256:9918d810489a5129'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# originalString(_:)

<sub>Instance Method</sub>

Return the string that consists of the precomposed Unicode characters.

<sub>macOS</sub>

```swift
func originalString(_ sender: Any!) -> NSAttributedString!
```

## Parameters

- `sender` — The client object requesting the original string.

## Return Value

The original string of precomposed unicode characters. If an input method stores the original input text, it returns that text. The return value is an attributed string so that the input method can restore changes they made to the font, and other attributes, if necessary. The returned object should be an autoreleased object.
