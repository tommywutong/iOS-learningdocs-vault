---
title: 'renderIntoOpenGLBuffer:onScreen:forTime:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/renderintoopenglbuffer:onscreen:fortime:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/renderintoopenglbuffer:onscreen:fortime:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/renderintoopenglbuffer%3Aonscreen%3Afortime%3A.json'
content_hash: 'sha256:bf12d22bb07148fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# renderIntoOpenGLBuffer:onScreen:forTime:

<sub>Instance Method</sub>

Called for each frame to be sent to Messages. This method will not be called on the main thread.

<sub>macOS</sub>

```objc
- (BOOL) renderIntoOpenGLBuffer:(CVOpenGLBufferRef) buffer onScreen:(int *) screenInOut forTime:(CVTimeStamp *) timeStamp;
```

## Parameters

- `buffer` — The OpenGL buffer to fill. The receiver should call `CVOpenGLBufferAttach()`, then render.

- `screenInOut` — The recommended virtual screen number to pass to `CVOpenGLBufferAttach()` for maximum efficiency. The delegate may use a different screen number, but must write that value back into screenInOut before returning.

- `timeStamp` — The frame time for which the buffer should be rendered.

## Return Value

Return `YES` if the buffer was successfully filled with new frame data. Return `NO` if nothing has changed or an error was encountered.
