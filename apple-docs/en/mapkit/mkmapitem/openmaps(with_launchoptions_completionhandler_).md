---
title: 'openMaps(with:launchOptions:completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 14.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitem/openmaps(with:launchoptions:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/openmaps(with:launchoptions:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/openmaps%28with%3Alaunchoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:0b81cfd77c1fb06a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# openMaps(with:launchOptions:completionHandler:)

<sub>Type Method</sub>

Opens the Maps app using the specified map items and options.

<sub>macOS</sub>

```swift
class func openMaps(with mapItems: [MKMapItem], launchOptions: [String : Any]? = nil, completionHandler completion: (@Sendable (Bool) -> Void)? = nil)
```

<sub>macOS</sub>

```swift
class func openMaps(with mapItems: [MKMapItem], launchOptions: [String : Any]? = nil) async -> Bool
```

## Parameters

- `mapItems` — An array of map items to open in the Maps app.

- `launchOptions` — A dictionary of launch options to pass to the Maps app.

- `completion` — A completion block the system calls that indicates whether the request was successful.

## See Also

### Launching the Maps app

- [+ openMapsWithItems:launchOptions:](<openmaps(with_launchoptions_).md>) — Opens the Maps app and displays the specified map items.
- [+ openMapsWithItems:launchOptions:fromScene:completionHandler:](<openmaps(with_launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified map items and options.
- [- openInMapsWithLaunchOptions:](<openinmaps(launchoptions_).md>) — Opens the Maps app and displays the map item.
- [- openInMapsWithLaunchOptions:completionHandler:](<openinmaps(launchoptions_completionhandler_).md>) — Opens the Maps app and displays the map item.
- [- openInMapsWithLaunchOptions:fromScene:completionHandler:](<openinmaps(launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified options.
