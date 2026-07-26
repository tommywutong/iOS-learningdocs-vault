---
title: abort()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.3+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconverter/abort()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverter/abort()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverter/abort%28%29.json'
content_hash: 'sha256:c596d9d52e277091'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPSConverter](../cgpsconverter.md)

# abort()

<sub>Instance Method</sub>

Tells a PostScript converter to abort a conversion at the next available opportunity.

<sub>Mac Catalyst, macOS</sub>

```swift
func abort() -> Bool
```

## Return Value

A Boolean value that indicates whether the converter is currently converting data (`true` if it is).

## See Also

### Instance Methods

- [CGPSConverterConvert](<convert(__consumer_options_).md>) — Uses a PostScript converter to convert PostScript data to PDF data.
