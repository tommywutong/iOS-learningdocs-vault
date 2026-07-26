---
title: 'inputText(_:key:modifiers:client:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/inputtext(_:key:modifiers:client:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inputtext(_:key:modifiers:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/inputtext%28_%3Akey%3Amodifiers%3Aclient%3A%29.json'
content_hash: 'sha256:dd9e0eb752d3df20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# inputText(_:key:modifiers:client:)

<sub>Instance Method</sub>

Receives Unicode, the key code that generated it, and any modifier flags.

<sub>macOS</sub>

```swift
func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool
```

## Parameters

- `string` — The text input by the client.

- `keyCode` — The key code for the associated Unicode.

- `flags` — The modifier flags.

- `sender` — The client object.

## Return Value

[YES](../yes.md) if the input is  accepted; otherwise [NO](../no.md).
