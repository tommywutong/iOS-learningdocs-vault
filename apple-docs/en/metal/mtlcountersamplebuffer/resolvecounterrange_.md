---
title: 'resolveCounterRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcountersamplebuffer/resolvecounterrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/resolvecounterrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffer/resolvecounterrange%3A.json'
content_hash: 'sha256:100720cb56fb252b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md)

# resolveCounterRange:

<sub>Instance Method</sub>

Transforms samples of a GPU’s counter set from the driver’s internal format to a standard Metal data structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (NSData *) resolveCounterRange:(NSRange) range;
```

## Parameters

- `range` — A range that indicates which sample instances the method resolves in the counter sample buffer.

## Return Value

An [NSData](../../foundation/nsdata.md) instance if the method successfully resolves the range of samples in the buffer; otherwise, `nil`.

## Discussion

You can only call this method on a counter sample buffer that you create with [MTLStorageModeShared](../mtlstoragemode/shared.md) (see [storageMode](../mtlcountersamplebufferdescriptor/storagemode.md)). For an example of how and when to use this method, see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md).

> [!note] Note
> The GPU stores [MTLCounterErrorValue](../mtlcountererrorvalue.md) in `destinationBuffer` each time it encounters an error resolving a sample.
