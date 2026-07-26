---
title: MTLDeviceLocation.unspecified
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicelocation/unspecified
source_url: 'https://developer.apple.com/documentation/metal/mtldevicelocation/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicelocation/unspecified.json'
content_hash: 'sha256:9240fd82eadc3ae1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDeviceLocation](../mtldevicelocation.md)

# MTLDeviceLocation.unspecified

<sub>Case</sub>

A value that indicates the system can’t determine how the GPU connects to it.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
case unspecified
```

## See Also

### Determining the GPU’s location

- [MTLDeviceLocationBuiltIn](builtin.md) — A location that indicates the GPU is permanently connected to the system internally. _(deprecated)_
- [MTLDeviceLocationSlot](slot.md) — A GPU location that indicates a person connected the GPU to a system’s internal slot. _(deprecated)_
- [MTLDeviceLocationExternal](external.md) — A GPU location that indicates a person connected the GPU to the system with an external interface, such as Thunderbolt. _(deprecated)_
