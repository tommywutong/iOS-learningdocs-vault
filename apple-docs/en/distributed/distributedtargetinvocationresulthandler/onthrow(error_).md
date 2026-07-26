---
title: 'onThrow(error:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedtargetinvocationresulthandler/onthrow(error:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationresulthandler/onthrow(error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationresulthandler/onthrow%28error%3A%29.json'
content_hash: 'sha256:714f4d3d03bc7055'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationResultHandler](../distributedtargetinvocationresulthandler.md)

# onThrow(error:)

<sub>Instance Method</sub>

Invoked when the distributed target execution of a target has thrown an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func onThrow<Err>(error: Err) async throws where Err : Error
```

## Discussion

It is not guaranteed that the error conform to the [SerializationRequirement](serializationrequirement.md); This guarantee is only given to return values (and offered by `onReturn`).
