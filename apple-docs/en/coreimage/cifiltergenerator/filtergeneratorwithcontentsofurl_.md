---
title: 'filterGeneratorWithContentsOfURL:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/filtergeneratorwithcontentsofurl:'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/filtergeneratorwithcontentsofurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/filtergeneratorwithcontentsofurl%3A.json'
content_hash: 'sha256:fa45356994a03ccd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# filterGeneratorWithContentsOfURL:

<sub>Type Method</sub>

Creates and returns a filter generator object and initializes it with the contents of a filter generator file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIFilterGenerator *) filterGeneratorWithContentsOfURL:(NSURL *) aURL;
```

## Parameters

- `aURL` — The location of a filter generator file.

## Return Value

A [CIFilterGenerator](../cifiltergenerator.md) object;  returns `nil` if the file can’t be read.

## See Also

### Creating Filter Generator Objects

- [filterGenerator](filtergenerator.md) — Creates and returns an empty filter generator object.
