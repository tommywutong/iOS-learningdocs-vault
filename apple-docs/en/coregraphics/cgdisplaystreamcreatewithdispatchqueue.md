---
title: CGDisplayStreamCreateWithDispatchQueue
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamcreatewithdispatchqueue
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamcreatewithdispatchqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamcreatewithdispatchqueue.json'
content_hash: 'sha256:e3430ac74e1c2c28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamCreateWithDispatchQueue

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGDisplayStreamRefCGDisplayStreamCreateWithDispatchQueue(CGDirectDisplayID display, size_t outputWidth, size_t outputHeight, int32_t pixelFormat, CFDictionaryRef properties, dispatch_queue_t queue, CGDisplayStreamFrameAvailableHandler handler);
```

## Parameters

- `display` — The CGDirectDisplayID to use as the source for generated frames

- `outputWidth` — The output width (in pixels, not points) of the frames to be generated.  Must not be zero.

- `outputHeight` — The output height (in pixels, not points) of the frames to be generated.  Must not be zero.

- `pixelFormat` — The desired CoreVideo/CoreMedia-style pixel format of the output IOSurfaces

- `properties` — Any optional properties of the CGDisplayStream

- `queue` — The dispatch_queue_t that will be used to invoke the callback handler.

- `handler` — A block that will be called for frame deliver.

## Return Value

The new CGDisplayStream object.

## Discussion

Creates a new CGDisplayStream intended to be serviced by a block handler

This function creates a new CGDisplayStream that is to be used to get a stream of frame updates from a particular display.
