---
title: unavailabilityReason
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotolibrary/unavailabilityreason
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/unavailabilityreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/unavailabilityreason.json'
content_hash: 'sha256:43fab6da789ee9eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# unavailabilityReason

<sub>Instance Property</sub>

An error that describes the reason the photo library isn’t available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var unavailabilityReason: (any Error)? { get }
```

## Discussion

This property contains a valid error only when the library is unavailable.

## See Also

### Observing Library Availability

- [- registerAvailabilityObserver:](<register(__)-gm0a.md>) — Registers an object to observe changes to the photo library’s availability.
- [- unregisterAvailabilityObserver:](<unregisteravailabilityobserver(__).md>) — Unregisters an object from observing changes to the photo library’s availability.
- [PHPhotoLibraryAvailabilityObserver](../phphotolibraryavailabilityobserver.md) — A protocol to adopt to have the system notify your app when the availability of a photo library changes.
