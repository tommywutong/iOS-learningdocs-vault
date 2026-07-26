---
title: 'candidates(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/candidates(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/candidates(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/candidates%28_%3A%29.json'
content_hash: 'sha256:f6ba1f749866ec7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# candidates(_:)

<sub>Instance Method</sub>

Returns an array of candidates.

<sub>macOS</sub>

```swift
func candidates(_ sender: Any!) -> [Any]!
```

## Parameters

- `sender` — The client object requesting the candidates.

## Return Value

An array of candidates. The returned array should be an autoreleased object.

## Discussion

An input method should look up its currently composed string and return a list of candidate strings that the composed string might map to.
