---
title: 'unregisterAvailabilityObserver(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/unregisteravailabilityobserver(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/unregisteravailabilityobserver(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/unregisteravailabilityobserver%28_%3A%29.json'
content_hash: 'sha256:53c24f79316e9def'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# unregisterAvailabilityObserver(_:)

<sub>Instance Method</sub>

Unregisters an object from observing changes to the photo library’s availability.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func unregisterAvailabilityObserver(_ observer: any PHPhotoLibraryAvailabilityObserver)
```

## Parameters

- `observer` — The observer object to unregister.

## See Also

### Observing Library Availability

- [- registerAvailabilityObserver:](<register(__)-gm0a.md>) — Registers an object to observe changes to the photo library’s availability.
- [PHPhotoLibraryAvailabilityObserver](../phphotolibraryavailabilityobserver.md) — A protocol to adopt to have the system notify your app when the availability of a photo library changes.
- [unavailabilityReason](unavailabilityreason.md) — An error that describes the reason the photo library isn’t available.
