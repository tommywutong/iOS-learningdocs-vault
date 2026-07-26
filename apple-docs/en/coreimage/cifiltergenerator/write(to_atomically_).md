---
title: 'write(to:atomically:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/write(to:atomically:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/write(to:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/write%28to%3Aatomically%3A%29.json'
content_hash: 'sha256:e2e18b364d632e31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# write(to:atomically:)

<sub>Instance Method</sub>

Archives a filter generator object to a filter generator file.

<sub>macOS</sub>

```swift
func write(to aURL: URL, atomically flag: Bool) -> Bool
```

## Parameters

- `aURL` — A  location for the file generator file.

- `flag` — Pass `true` to specify that Core Image should create an interim file to avoid overwriting an existing file.

## Return Value

Returns `true` if the object is successfully archived to the file.

## Discussion

Use this method to save your filter chain to a file for later use.
