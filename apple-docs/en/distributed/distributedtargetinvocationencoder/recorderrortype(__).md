---
title: 'recordErrorType(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedtargetinvocationencoder/recorderrortype(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/recorderrortype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationencoder/recorderrortype%28_%3A%29.json'
content_hash: 'sha256:b02c175d525d2070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationEncoder](../distributedtargetinvocationencoder.md)

# recordErrorType(_:)

<sub>Instance Method</sub>

Record the error type of the distributed method. This method will not be invoked if the target is not throwing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func recordErrorType<E>(_ type: E.Type) throws where E : Error
```

## Parameters

- `type` — The type of error that was declared to be thrown by the invocation target. Currently this can only ever be `Error.self`.
