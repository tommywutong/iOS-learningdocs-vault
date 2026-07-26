---
title: MTLTimestamp
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltimestamp
source_url: 'https://developer.apple.com/documentation/metal/mtltimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltimestamp.json'
content_hash: 'sha256:0eac7cf97155fe22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTimestamp

<sub>Type Alias</sub>

The number of nanoseconds for a point in absolute time or Mach absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLTimestamp = UInt64
```

## Discussion

The type of absolute time a Metal timestamp uses can vary with a system’s configuration, but it’s consistent for a configuration.

## See Also

### Timestamp data

- [Converting GPU timestamps into CPU time](converting-gpu-timestamps-into-cpu-time.md) — Correlate GPU events with CPU timelines by calculating the CPU time equivalents for GPU timestamps.
