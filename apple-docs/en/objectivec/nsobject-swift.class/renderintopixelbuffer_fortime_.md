---
title: 'renderIntoPixelBuffer:forTime:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/renderintopixelbuffer:fortime:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/renderintopixelbuffer:fortime:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/renderintopixelbuffer%3Afortime%3A.json'
content_hash: 'sha256:d523b282d66533d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# renderIntoPixelBuffer:forTime:

<sub>Instance Method</sub>

<sub>macOS</sub>

```objc
- (BOOL) renderIntoPixelBuffer:(CVPixelBufferRef) buffer forTime:(CVTimeStamp *) timeStamp;
```

## Parameters

- `buffer` — The pixel buffer to fill. The dimensions can vary: use CVPixelBufferGetWidth() and CVPixelBufferGetHeight() every time.

- `timeStamp` — The frame time for which the buffer should be rendered.

## Return Value

Return YES if the buffer was successfully filled with new frame data. Return NO if nothing has changed or an error was encountered.

## Discussion

Called for each frame to be sent to Messages. This method will not be called on the main thread.
