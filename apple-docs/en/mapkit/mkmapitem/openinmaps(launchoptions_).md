---
title: 'openInMaps(launchOptions:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitem/openinmaps(launchoptions:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/openinmaps(launchoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/openinmaps%28launchoptions%3A%29.json'
content_hash: 'sha256:6d3afa9ddba2246d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# openInMaps(launchOptions:)

<sub>Instance Method</sub>

Opens the Maps app and displays the map item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func openInMaps(launchOptions: [String : Any]? = nil) -> Bool
```

## Parameters

- `launchOptions` — Additional information that the Maps app can use to configure the map display. For example, you can use the launch options to specify the visible map region and the map type. For a list of keys you can put into this dictionary, see [Launch options dictionary keys](../launch-options-dictionary-keys.md). This parameter may be `nil`.

## Return Value

[true](../../swift/true.md) if the Maps app successfully opens the map item, or [false](../../swift/false.md) if there’s an error.

## Discussion

You use this method to pass the map item to the Maps app. If your map item contains descriptive information about the location (such as a name or URL), the Maps app displays that information at the specified coordinate.

If you specify the [MKLaunchOptionsDirectionsModeKey](../mklaunchoptionsdirectionsmodekey.md) option in the `launchOptions` dictionary, the Maps app interprets that as an attempt to map from the user’s current location to the location that the map item specifies.

> [!note] Note
> This is a blocking call and the system suspends interaction with your app until the Maps app finishes launching.

If you don’t include the [MKLaunchOptionsMapCenterKey](../mklaunchoptionsmapcenterkey.md) and [MKLaunchOptionsMapSpanKey](../mklaunchoptionsmapspankey.md) keys in your `launchOptions` dictionary, the Maps app constructs a region around the map item. It uses that region to set the visible portion of the map.

## See Also

### Launching the Maps app

- [+ openMapsWithItems:launchOptions:](<openmaps(with_launchoptions_).md>) — Opens the Maps app and displays the specified map items.
- [+ openMapsWithItems:launchOptions:completionHandler:](<openmaps(with_launchoptions_completionhandler_).md>) — Opens the Maps app using the specified map items and options.
- [+ openMapsWithItems:launchOptions:fromScene:completionHandler:](<openmaps(with_launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified map items and options.
- [- openInMapsWithLaunchOptions:completionHandler:](<openinmaps(launchoptions_completionhandler_).md>) — Opens the Maps app and displays the map item.
- [- openInMapsWithLaunchOptions:fromScene:completionHandler:](<openinmaps(launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified options.
