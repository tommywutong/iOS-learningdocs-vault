---
title: kCGDisplayStreamSourceRect
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgdisplaystreamsourcerect
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamsourcerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgdisplaystreamsourcerect.json'
content_hash: 'sha256:a56208842cc77ede'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGDisplayStreamSourceRect

<sub>Global Variable</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CFStringRef const kCGDisplayStreamSourceRect;
```

## Discussion

This may be used to request a subregion of the display to be provided as the source of the display stream.  Use CGRectCreateDictionaryRepresentation to convert from a CGRect to the value used here.   Note: The coordinate system for the source rectangle is specified in display logical coordinates and not in pixels, in order to match the normal convention on HiDPI displays.
