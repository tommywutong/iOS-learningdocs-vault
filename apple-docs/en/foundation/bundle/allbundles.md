---
title: allBundles
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/allbundles
source_url: 'https://developer.apple.com/documentation/foundation/bundle/allbundles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/allbundles.json'
content_hash: 'sha256:f489ee3d2fa7d05e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# allBundles

<sub>Type Property</sub>

Returns an array of all the application’s non-framework bundles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var allBundles: [Bundle] { get }
```

## Return Value

An array of all the application’s non-framework bundles.

## Discussion

The returned array includes the main bundle and all bundles that have been dynamically created but doesn’t contain any bundles that represent frameworks.

## See Also

### Getting standard bundle objects

- [mainBundle](main.md) — Returns the bundle object that contains the current executable.
- [allFrameworks](allframeworks.md) — Returns an array of all of the application’s bundles that represent frameworks.
