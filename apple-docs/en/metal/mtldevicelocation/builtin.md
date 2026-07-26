---
title: MTLDeviceLocation.builtIn
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicelocation/builtin
source_url: 'https://developer.apple.com/documentation/metal/mtldevicelocation/builtin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicelocation/builtin.json'
content_hash: 'sha256:451fb79345fba5d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDeviceLocation](../mtldevicelocation.md)

# MTLDeviceLocation.builtIn

<sub>Case</sub>

A location that indicates the GPU is permanently connected to the system internally.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
case builtIn
```

## See Also

### Determining the GPU’s location

- [MTLDeviceLocationSlot](slot.md) — A GPU location that indicates a person connected the GPU to a system’s internal slot. _(deprecated)_
- [MTLDeviceLocationExternal](external.md) — A GPU location that indicates a person connected the GPU to the system with an external interface, such as Thunderbolt. _(deprecated)_
- [MTLDeviceLocationUnspecified](unspecified.md) — A value that indicates the system can’t determine how the GPU connects to it. _(deprecated)_
