---
title: 'init(textInput:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputstringtokenizer/init(textinput:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer/init(textinput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputstringtokenizer/init%28textinput%3A%29.json'
content_hash: 'sha256:529b827d731ac6cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputStringTokenizer](../uitextinputstringtokenizer.md)

# init(textInput:)

<sub>Initializer</sub>

Returns an object initialized with the document object that directly communicates with the text input system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(textInput: any UIResponder & UITextInput)
```

## Parameters

- `textInput` — The document object in the application that adopts the [UITextInput](../uitextinput.md) protocol for the purposes of communicating with the text input system.

## Return Value

An instance of a subclass of [UITextInputStringTokenizer](../uitextinputstringtokenizer.md), or `nil` if the object couldn’t be created.

## Discussion

The subclass of [UITextInputStringTokenizer](../uitextinputstringtokenizer.md) shouldn’t retain `textInput`; the tokenizer should always have a lifetime bounded by that of the [UITextInput](../uitextinput.md)-conforming object and a retaining reference would create a retain cycle.
