---
title: CGDisplayStreamCreate
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamcreate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamcreate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamcreate.json'
content_hash: 'sha256:089758cb7a863051'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamCreate

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGDisplayStreamRefCGDisplayStreamCreate(CGDirectDisplayID display, size_t outputWidth, size_t outputHeight, int32_t pixelFormat, CFDictionaryRef properties, CGDisplayStreamFrameAvailableHandler handler);
```

## Parameters

- `display` — The CGDirectDisplayID to use as the source for generated frames

- `outputWidth` — The output width (in pixels, not points) of the frames to be generated.  Must not be zero.

- `outputHeight` — The output height (in pixels, not points) of the frames to be generated.  Must not be zero.

- `pixelFormat` — The desired CoreVideo/CoreMedia-style pixel format of the output IOSurfaces.  The currently supported values are:

- `properties` — Any optional properties of the CGDisplayStream

- `handler` — A block that will be called for frame deliver.

## Return Value

The new CGDisplayStream object.

## Discussion

Creates a new CGDisplayStream intended to be used with a CFRunLoop

This function creates a new CGDisplayStream that is to be used to get a stream of frame updates from a particular display.

‘BGRA’ Packed Little Endian ARGB8888 ‘l10r’ Packed Little Endian ARGB2101010 ‘420v’ 2-plane “video” range YCbCr 4:2:0 ‘420f’ 2-plane “full” range YCbCr 4:2:0
