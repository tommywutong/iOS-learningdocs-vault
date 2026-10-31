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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# renderIntoPixelBuffer:forTime:

<sub>实例方法</sub>

<sub>macOS</sub>

```objc
- (BOOL) renderIntoPixelBuffer:(CVPixelBufferRef) buffer forTime:(CVTimeStamp *) timeStamp;
```

## 参数

- `buffer` — 要填充的像素缓冲区。尺寸可能变化：请每次都使用 CVPixelBufferGetWidth() 和 CVPixelBufferGetHeight()。

- `timeStamp` — 应渲染缓冲区的帧时间。

## 返回值

若缓冲区已成功填充新帧数据则返回 YES。若无任何更改或遇到错误则返回 NO。

## 讨论

为要发送到“信息”的每一帧调用。此方法不会在主线程上调用。
