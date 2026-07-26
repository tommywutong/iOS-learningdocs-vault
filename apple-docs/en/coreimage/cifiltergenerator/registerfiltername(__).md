---
title: 'registerFilterName(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/registerfiltername(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/registerfiltername(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/registerfiltername%28_%3A%29.json'
content_hash: 'sha256:3f94c4d95a6972af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# registerFilterName(_:)

<sub>Instance Method</sub>

Registers the name associated with a filter chain.

<sub>macOS</sub>

```swift
func registerFilterName(_ name: String)
```

## Parameters

- `name` — A unique name for the filter chain you want to register.

## Discussion

This method allows you to register the filter chain as a named filter in the Core Image filter repository. You can then create a `CIFilter` object from it using the [+ filterWithName:](<../cifilter-swift.class/init(name_).md>) method of the [CIFilter](../cifilter-swift.class.md) class.
