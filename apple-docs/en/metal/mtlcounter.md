---
title: MTLCounter
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounter
source_url: 'https://developer.apple.com/documentation/metal/mtlcounter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounter.json'
content_hash: 'sha256:e636d77907ec79de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounter

<sub>Protocol</sub>

An individual counter a GPU device lists within one of its counter sets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLCounter : NSObjectProtocol, Sendable
```

## Overview

You can determine which counters a GPU supports within a counter set (see [MTLCounterSet](mtlcounterset.md)) by checking the elements of its [counters](mtlcounterset/counters.md) property. A counter’s [name](mtlcounter/name.md) property typically matches one of the common counter set names that [MTLCommonCounter](mtlcommoncounter.md) defines. For more information, see [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying a counter

- [name](mtlcounter/name.md) — The name of a GPU’s counter instance.

## See Also

### Counters and counter sets

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md) — Check whether a GPU produces the runtime performance data you want to sample.
- [MTLCounterSet](mtlcounterset.md) — A collection of individual counters a GPU device supports for a counter set.
- [MTLCommonCounterSet](mtlcommoncounterset.md) — The name of a specific counter set that a GPU device can support.
- [MTLCommonCounter](mtlcommoncounter.md) — The name of a specific counter that can appear in a GPU device’s counter sets.
