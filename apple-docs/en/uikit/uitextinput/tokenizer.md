---
title: tokenizer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/tokenizer
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/tokenizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/tokenizer.json'
content_hash: 'sha256:f67204ac19d75931'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# tokenizer

<sub>Instance Property</sub>

An input tokenizer that provides information about the granularity of text units.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tokenizer: any UITextInputTokenizer { get }
```

## Discussion

Standard units of granularity include characters, words, lines, and paragraphs. In most cases, you may lazily create and assign an instance of a subclass of [UITextInputStringTokenizer](../uitextinputstringtokenizer.md) for this purpose. If you require different behavior than this system-provided tokenizer, you can create a custom tokenizer that adopts the [UITextInputTokenizer](../uitextinputtokenizer.md) protocol.

## See Also

### Tokenizing input text

- [UITextInputTokenizer](../uitextinputtokenizer.md) — A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.
