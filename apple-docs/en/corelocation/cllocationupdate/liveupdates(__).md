---
title: 'liveUpdates(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationupdate/liveupdates(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdate/liveupdates(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdate/liveupdates%28_%3A%29.json'
content_hash: 'sha256:c9363adc27346e49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationUpdate](../cllocationupdate.md)

# liveUpdates(_:)

<sub>Type Method</sub>

Tells Core Location to start delivering the location updates it produces for the configuration you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func liveUpdates(_ configuration: CLLocationUpdate.LiveConfiguration = .default) -> CLLocationUpdate.Updates
```

## Parameters

- `configuration` — A configuration that describes the updates for the framework to deliver.

## Return Value

[Updates](updates.md) that meet the criteria you specify.

## See Also

### Receiving location updates

- [LiveConfiguration](liveconfiguration.md) — Values for indicating the kind of updates the framework delivers.
- [Updates](updates.md) — A structure that represents an asynchronous sequence of location updates.
