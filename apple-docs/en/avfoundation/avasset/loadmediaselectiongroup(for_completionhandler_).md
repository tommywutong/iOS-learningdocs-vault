---
title: 'loadMediaSelectionGroup(for:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasset/loadmediaselectiongroup(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/loadmediaselectiongroup(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/loadmediaselectiongroup%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:601478b2aa339b47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# loadMediaSelectionGroup(for:completionHandler:)

<sub>Instance Method</sub>

Loads a media selection group that contains one or more options with the specified media characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadMediaSelectionGroup(for mediaCharacteristic: AVMediaCharacteristic, completionHandler: @escaping @Sendable (AVMediaSelectionGroup?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadMediaSelectionGroup(for mediaCharacteristic: AVMediaCharacteristic) async throws -> AVMediaSelectionGroup?
```

## Parameters

- `mediaCharacteristic` — A media characteristic to load the available media selection options for. The supported characterisics are: - [AVMediaCharacteristicAudible](../avmediacharacteristic/audible.md) to return the group of available options for audio media in various languages and for various purposes, such as descriptive audio - [AVMediaCharacteristicLegible](../avmediacharacteristic/legible.md) to return the group of available options for subtitles in various languages and for various purposes - [AVMediaCharacteristicVisual](../avmediacharacteristic/visual.md) to return the group of available options for video media

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **mediaSelectionGroup** — The loaded media selection group, or `nil` if no group is available or if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading media selections

- [allMediaSelections](../avpartialasyncproperty/allmediaselections.md) — The available media selections for an asset.
- [preferredMediaSelection](../avpartialasyncproperty/preferredmediaselection.md) — The default media selections for the media selection groups of an asset.
- [availableMediaCharacteristicsWithMediaSelectionOptions](../avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md) — The media characteristics that provide media selection options.
