---
title: endResidency()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/endresidency()
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/endresidency()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/endresidency%28%29.json'
content_hash: 'sha256:72ea0d62876d0b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# endResidency()

<sub>Instance Method</sub>

Informs Metal that the residency set’s allocations no longer need to be resident, and that it can reuse the memory for other allocations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func endResidency()
```
