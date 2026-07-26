---
title: commit()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencyset/commit()
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencyset/commit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencyset/commit%28%29.json'
content_hash: 'sha256:19170f072e3291d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResidencySet](../mtlresidencyset.md)

# commit()

<sub>Instance Method</sub>

Applies any pending additions to and removals from the residency set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func commit()
```

## Discussion

Call the method when have no other changes to stage, such as with [- addAllocation:](<addallocation(__).md>), [- removeAllocation:](<removeallocation(__).md>), and their sibling methods.
