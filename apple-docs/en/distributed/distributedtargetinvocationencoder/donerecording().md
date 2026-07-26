---
title: doneRecording()
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedtargetinvocationencoder/donerecording()
source_url: 'https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/donerecording()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedtargetinvocationencoder/donerecording%28%29.json'
content_hash: 'sha256:e3408018e6c96bb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedTargetInvocationEncoder](../distributedtargetinvocationencoder.md)

# doneRecording()

<sub>Instance Method</sub>

Invoked to signal to the encoder that no further `record...` calls will be made on it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func doneRecording() throws
```

## Discussion

Useful if the encoder needs to perform some “final” task before the underlying message is considered complete, e.g. computing a checksum, or some additional message signing or finalization step.
