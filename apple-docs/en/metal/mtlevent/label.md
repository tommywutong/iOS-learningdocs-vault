---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlevent/label
source_url: 'https://developer.apple.com/documentation/metal/mtlevent/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlevent/label.json'
content_hash: 'sha256:1baaccb011d8bea2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLEvent](../mtlevent.md)

# label

<sub>Instance Property</sub>

A string that identifies the event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the event

- [device](device.md) — The device object that created the event.
