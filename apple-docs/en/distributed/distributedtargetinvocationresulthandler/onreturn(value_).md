---
title: 'onReturn(value:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedtargetinvocationresulthandler/onreturn(value:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationresulthandler/onreturn(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationresulthandler/onreturn%28value%3A%29.json'
content_hash: 'sha256:7278fffb310d34b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationResultHandler](../distributedtargetinvocationresulthandler.md)

# onReturn(value:)

<sub>Instance Method</sub>

Invoked when the distributed target execution returns successfully. The `value` is the return value of the executed distributed invocation target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func onReturn<Success>(value: Success) async throws
```

### Serialization Requirement

Implementations of this method must ensure that the `Success` type parameter conforms to the types’ `SerializationRequirement`.
