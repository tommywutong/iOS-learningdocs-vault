---
title: kCGDisplayStreamDestinationRect
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgdisplaystreamdestinationrect
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamdestinationrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgdisplaystreamdestinationrect.json'
content_hash: 'sha256:c39d23dd29c7c1a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGDisplayStreamDestinationRect

<sub>Global Variable</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CFStringRef const kCGDisplayStreamDestinationRect;
```

## Discussion

This may be used to request where within the destination buffer the display updates should be placed. Use CGRectCreateDictionaryRepresentation to convert from a CGRect to the value used here.   Note: The coordinate system for the destination rectangle is always specified in output pixels to match the fact that the output buffer size is also specified in terms of pixels.
