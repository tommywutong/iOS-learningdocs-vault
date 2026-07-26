---
title: MTLCounterSet
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterset
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterset.json'
content_hash: 'sha256:917abc989a87989e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterSet

<sub>Protocol</sub>

A collection of individual counters a GPU device supports for a counter set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLCounterSet : NSObjectProtocol, Sendable
```

## Overview

You can determine which counter sets a GPU supports by checking an [MTLDevice](mtldevice.md) instance’s [counterSets](mtldevice/countersets.md) property. A counter set’s [name](mtlcounterset/name.md) property typically matches one of the common counter set names that [MTLCommonCounterSet](mtlcommoncounterset.md) defines. Check whether a GPU device supports a specific counter by comparing elements of the [counters](mtlcounterset/counters.md) property with a counter’s common name that [MTLCommonCounter](mtlcommoncounter.md) defines.

> [!important] Important
> Some GPUs may only support some of the counters within a counter set.

For more information, see [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying a counter set

- [name](mtlcounterset/name.md) — The name of the GPU’s counter set instance.

### Checking which counters a GPU supports

- [counters](mtlcounterset/counters.md) — An array of the counter instances a GPU device supports.

## See Also

### Counters and counter sets

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md) — Check whether a GPU produces the runtime performance data you want to sample.
- [MTLCommonCounterSet](mtlcommoncounterset.md) — The name of a specific counter set that a GPU device can support.
- [MTLCounter](mtlcounter.md) — An individual counter a GPU device lists within one of its counter sets.
- [MTLCommonCounter](mtlcommoncounter.md) — The name of a specific counter that can appear in a GPU device’s counter sets.
