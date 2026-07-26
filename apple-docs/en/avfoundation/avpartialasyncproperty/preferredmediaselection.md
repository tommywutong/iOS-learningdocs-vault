---
title: preferredMediaSelection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/preferredmediaselection
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredmediaselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/preferredmediaselection.json'
content_hash: 'sha256:efe54cd0e125a21d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# preferredMediaSelection

<sub>Type Property</sub>

The default media selections for the media selection groups of an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var preferredMediaSelection: AVAsyncProperty<Root, AVMediaSelection> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading media selections

- [allMediaSelections](allmediaselections.md) — The available media selections for an asset.
- [availableMediaCharacteristicsWithMediaSelectionOptions](availablemediacharacteristicswithmediaselectionoptions.md) — The media characteristics that provide media selection options.
- [- loadMediaSelectionGroupForMediaCharacteristic:completionHandler:](<../avasset/loadmediaselectiongroup(for_completionhandler_).md>) — Loads a media selection group that contains one or more options with the specified media characteristic.
