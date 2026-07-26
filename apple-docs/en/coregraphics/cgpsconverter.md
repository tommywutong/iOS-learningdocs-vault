---
title: CGPSConverter
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconverter
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverter.json'
content_hash: 'sha256:afb67071e40c3777'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverter

<sub>Class</sub>

An opaque data type used to convert PostScript data to PDF data.

<sub>Mac Catalyst, macOS</sub>

```swift
class CGPSConverter
```

## Overview

The PostScript data is supplied by a data provider and written into a data consumer. When you create a PostScript converter object, you can supply callback functions to invoke at various stages of the conversion process.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Initializers

- [CGPSConverterCreate](<cgpsconverter/init(info_callbacks_options_).md>) — Creates a new PostScript converter.

### Instance Properties

- [CGPSConverterIsConverting](cgpsconverter/isconverting.md) — Checks whether the converter is currently converting data.

### Type Properties

- [CGPSConverterGetTypeID](cgpsconverter/typeid.md) — Returns the Core Foundation type identifier for PostScript converters.

### Instance Methods

- [CGPSConverterAbort](<cgpsconverter/abort().md>) — Tells a PostScript converter to abort a conversion at the next available opportunity.
- [CGPSConverterConvert](<cgpsconverter/convert(__consumer_options_).md>) — Uses a PostScript converter to convert PostScript data to PDF data.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
