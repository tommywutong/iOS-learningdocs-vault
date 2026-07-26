---
title: MTLDeviceLocation.slot
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicelocation/slot
source_url: 'https://developer.apple.com/documentation/metal/mtldevicelocation/slot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicelocation/slot.json'
content_hash: 'sha256:c1a5dcfa15617302'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDeviceLocation](../mtldevicelocation.md)

# MTLDeviceLocation.slot

<sub>Case</sub>

A GPU location that indicates a person connected the GPU to a system’s internal slot.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
case slot
```

## See Also

### Determining the GPU’s location

- [MTLDeviceLocationBuiltIn](builtin.md) — A location that indicates the GPU is permanently connected to the system internally. _(deprecated)_
- [MTLDeviceLocationExternal](external.md) — A GPU location that indicates a person connected the GPU to the system with an external interface, such as Thunderbolt. _(deprecated)_
- [MTLDeviceLocationUnspecified](unspecified.md) — A value that indicates the system can’t determine how the GPU connects to it. _(deprecated)_
