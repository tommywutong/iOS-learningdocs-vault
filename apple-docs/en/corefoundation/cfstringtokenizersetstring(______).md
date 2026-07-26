---
title: 'CFStringTokenizerSetString(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizersetstring(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizersetstring(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizersetstring%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:07cdf8f53437d36c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerSetString(_:_:_:)

<sub>Function</sub>

Sets the string for a tokenizer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerSetString(_ tokenizer: CFStringTokenizer!, _ string: CFString!, _ range: CFRange)
```

## Parameters

- `tokenizer` — A tokenizer.

- `string` — The string for the tokenizer to tokenize.

- `range` — The range of string to tokenize. The range of characters within the string to be tokenized. The specified range must not exceed the length of the string.
