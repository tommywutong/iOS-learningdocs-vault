---
title: 'openInMaps(launchOptions:completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 14.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitem/openinmaps(launchoptions:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/openinmaps(launchoptions:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/openinmaps%28launchoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:ed67c44774de810c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# openInMaps(launchOptions:completionHandler:)

<sub>Instance Method</sub>

Opens the Maps app and displays the map item.

<sub>macOS</sub>

```swift
func openInMaps(launchOptions: [String : Any]? = nil, completionHandler completion: (@Sendable (Bool) -> Void)? = nil)
```

<sub>macOS</sub>

```swift
func openInMaps(launchOptions: [String : Any]? = nil) async -> Bool
```

## Parameters

- `launchOptions` — A dictionary of launch options to pass to the Maps app.

- `completion` — A completion block the system calls that indicates whether the request was successful.

## See Also

### Launching the Maps app

- [+ openMapsWithItems:launchOptions:](<openmaps(with_launchoptions_).md>) — Opens the Maps app and displays the specified map items.
- [+ openMapsWithItems:launchOptions:completionHandler:](<openmaps(with_launchoptions_completionhandler_).md>) — Opens the Maps app using the specified map items and options.
- [+ openMapsWithItems:launchOptions:fromScene:completionHandler:](<openmaps(with_launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified map items and options.
- [- openInMapsWithLaunchOptions:](<openinmaps(launchoptions_).md>) — Opens the Maps app and displays the map item.
- [- openInMapsWithLaunchOptions:fromScene:completionHandler:](<openinmaps(launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified options.
