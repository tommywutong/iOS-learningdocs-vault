---
title: 'resolveCounterRange(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcountersamplebuffer/resolvecounterrange(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/resolvecounterrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffer/resolvecounterrange%28_%3A%29.json'
content_hash: 'sha256:f08d9d0eb837e48a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md)

# resolveCounterRange(_:)

<sub>Instance Method</sub>

Transforms samples of a GPU’s counter set from the driver’s internal format to a standard Metal data structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resolveCounterRange(_ range: Range<Int>) throws -> Data?
```

## Parameters

- `range` — A range that indicates which sample instances the method resolves in the counter sample buffer.

## Return Value

A [Data](../../foundation/data.md) instance in Swift, or an [NSData](../../foundation/nsdata.md) instance in Objective-C, if the method successfully resolves the range of samples in the buffer; otherwise, `nil`.

## Discussion

You can only call this method on a counter sample buffer that you create with [MTLStorageModeShared](../mtlstoragemode/shared.md) (see [storageMode](../mtlcountersamplebufferdescriptor/storagemode.md)). For an example of how and when to use this method, see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md).

> [!note] Note
> The GPU stores [MTLCounterErrorValue](../mtlcountererrorvalue.md) in `destinationBuffer` each time it encounters an error resolving a sample.
