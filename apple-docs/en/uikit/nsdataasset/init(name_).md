---
title: 'init(name:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdataasset/init(name:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdataasset/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdataasset/init%28name%3A%29.json'
content_hash: 'sha256:df872dd0982e2091'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDataAsset](../nsdataasset.md)

# init(name:)

<sub>Initializer</sub>

Initializes and returns an object with a reference to the named data asset in an asset catalog.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(name: NSDataAssetName)
```

## Parameters

- `name` — The name of the data set in the asset catalog.

## Return Value

The data asset object for the named data set, or `nil` if the data set is not found.

## Discussion

If there are multiple data files in the named data set, this method returns the one with attributes that most closely match the current device available screen space.

This method looks in the asset catalog, in the main bundle for the named data set.

## See Also

### Initializing the data asset

- [- initWithName:bundle:](<init(name_bundle_).md>) — Initializes and returns an object with a reference to the named data asset that’s in an asset catalog in the specified bundle.
