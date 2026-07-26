---
title: requestResidency()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/requestresidency()
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/requestresidency()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/requestresidency%28%29.json'
content_hash: 'sha256:123da88fcdd23fa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# requestResidency()

<sub>Instance Method</sub>

Tells Metal to do as much preparatory work as it can, with the system’s current conditions, to make the set’s resource allocations resident.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestResidency()
```

## Discussion

Call the method anytime after calling a residency set’s [- commit](<commit().md>) method, ideally well before calling the [- commit](<../mtlcommandbuffer/commit().md>) method of any [MTLCommandBuffer](../mtlcommandbuffer.md) that uses it.

The method may postpone some of the necessary steps to make resources resident in scenarios where other apps concurrently need resources in residency.
