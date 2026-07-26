---
title: 'inputText(_:client:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/inputtext(_:client:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inputtext(_:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/inputtext%28_%3Aclient%3A%29.json'
content_hash: 'sha256:a318365861469724'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# inputText(_:client:)

<sub>Instance Method</sub>

Handles key down events that do not map to an action method.

<sub>macOS</sub>

```swift
func inputText(_ string: String!, client sender: Any!) -> Bool
```

## Parameters

- `string` — The key down event, which is the text input by the client.

- `sender` — The client object sending the key down events.

## Return Value

[YES](../yes.md) if the input is accepted; otherwise [NO](../no.md).

## Discussion

An input method should implement this method when using key binding (that is, it implements [- didCommandBySelector:client:](<didcommand(by_client_).md>)).
