---
title: 'SecTransformExecuteAsync(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformexecuteasync(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformexecuteasync(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformexecuteasync%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d4de90ace6862d4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformExecuteAsync(_:_:_:)

<sub>Function</sub>

Executes transform or transform group asynchronously.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformExecuteAsync(_ transformRef: SecTransform, _ deliveryQueue: dispatch_queue_t, _ deliveryBlock: @escaping SecMessageBlock)
```

## Parameters

- `transformRef` — The transform to execute.

- `deliveryQueue` — A dispatch queue on which to deliver the results of this transform.

- `deliveryBlock` — A SecMessageBlock to asynchronously receive the results of the transform.

## Discussion

SecTransformExecuteAsync works just like the SecTransformExecute API except that it returns results to the deliveryBlock. There may be multple results depending on the transform. The block knows that the processing is complete when the isFinal parameter is set to true. If an error occurs the block’s error parameter is set and the isFinal parameter will be set to true.
