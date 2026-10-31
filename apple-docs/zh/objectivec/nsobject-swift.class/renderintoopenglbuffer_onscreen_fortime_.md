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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# renderIntoOpenGLBuffer:onScreen:forTime:

<sub>实例方法</sub>

为要发送到“信息”的每一帧调用。此方法不会在主线程上调用。

<sub>macOS</sub>

```objc
- (BOOL) renderIntoOpenGLBuffer:(CVOpenGLBufferRef) buffer onScreen:(int *) screenInOut forTime:(CVTimeStamp *) timeStamp;
```

## 参数

- `buffer` — 要填充的 OpenGL 缓冲区。接收者应调用 `CVOpenGLBufferAttach()`，然后进行渲染。

- `screenInOut` — 为获得最高效率而建议传给 `CVOpenGLBufferAttach()` 的虚拟屏幕编号。委托可以使用不同的屏幕编号，但必须在返回前将该值写回 screenInOut。

- `timeStamp` — 应渲染缓冲区的帧时间。

## 返回值

若缓冲区已成功填充新帧数据则返回 `YES`。若无任何更改或遇到错误则返回 `NO`。
