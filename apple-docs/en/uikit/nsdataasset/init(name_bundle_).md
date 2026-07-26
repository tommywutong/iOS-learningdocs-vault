---
title: 'init(name:bundle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdataasset/init(name:bundle:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdataasset/init(name:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdataasset/init%28name%3Abundle%3A%29.json'
content_hash: 'sha256:7cb3435be33961be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDataAsset](../nsdataasset.md)

# init(name:bundle:)

<sub>Initializer</sub>

Initializes and returns an object with a reference to the named data asset that’s in an asset catalog in the specified bundle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(name: NSDataAssetName, bundle: Bundle)
```

## Parameters

- `name` — The name of the data set in the asset catalog.

- `bundle` — The bundle used to store the asset catalog. Pass `nil` for the main bundle. The bundle must be the same as the one used in the Xcode project.

## Return Value

The data asset object for the named data set in the specified bundle, or `nil` if the data set is not found.

## Discussion

If there are multiple data files in the named data set, this method returns the one with attributes that most closely match the current device available screen space.

This method looks in the asset catalog, in the bundle specified by the `bundle` parameter for the named data set.

## See Also

### Initializing the data asset

- [- initWithName:](<init(name_).md>) — Initializes and returns an object with a reference to the named data asset in an asset catalog.
