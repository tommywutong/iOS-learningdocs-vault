---
title: 'commitComposition(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/commitcomposition(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commitcomposition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commitcomposition%28_%3A%29.json'
content_hash: 'sha256:8a03dc9d11e8f568'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitComposition(_:)

<sub>Instance Method</sub>

Informs the controller that the composition should be committed.

<sub>macOS</sub>

```swift
func commitComposition(_ sender: Any!)
```

## Parameters

- `sender` — The client object requesting the input method to commit the composition.

## Discussion

If an input method implements this method, it is called when the client wants to end the composition session immediately. A typical response would be to call the `insertText` method of the client and then clean up any per-session buffers and variables. After receiving this message an input method should consider the given composition session finished.
