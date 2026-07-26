---
title: 'handle(_:client:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/handle(_:client:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/handle(_:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/handle%28_%3Aclient%3A%29.json'
content_hash: 'sha256:874e19919e88ba6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# handle(_:client:)

<sub>Instance Method</sub>

Handles key down and mouse events.

<sub>macOS</sub>

```swift
func handle(_ event: NSEvent!, client sender: Any!) -> Bool
```

## Parameters

- `event` — The event to handle.

- `sender` — The client object sending the event.

## Return Value

[YES](../yes.md) if the event is handled; otherwise [NO](../no.md).
