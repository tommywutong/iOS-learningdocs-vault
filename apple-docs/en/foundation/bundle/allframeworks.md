---
title: allFrameworks
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/allframeworks
source_url: 'https://developer.apple.com/documentation/foundation/bundle/allframeworks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/allframeworks.json'
content_hash: 'sha256:5920a4ceb9b19544'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# allFrameworks

<sub>Type Property</sub>

Returns an array of all of the application’s bundles that represent frameworks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var allFrameworks: [Bundle] { get }
```

## Return Value

An array of all of the application’s bundles that represent frameworks. Only frameworks with one or more Objective-C classes in them are included.

## Discussion

The returned array includes frameworks that are linked into an application when the application is built and bundles for frameworks that have been dynamically created.

## See Also

### Getting standard bundle objects

- [mainBundle](main.md) — Returns the bundle object that contains the current executable.
- [allBundles](allbundles.md) — Returns an array of all the application’s non-framework bundles.
