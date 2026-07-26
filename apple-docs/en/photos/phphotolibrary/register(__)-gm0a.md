---
title: 'register(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/register(_:)-gm0a'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-gm0a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/register%28_%3A%29-gm0a.json'
content_hash: 'sha256:8410069858af6f9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# register(_:)

<sub>Instance Method</sub>

Registers an object to observe changes to the photo library’s availability.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func register(_ observer: any PHPhotoLibraryAvailabilityObserver)
```

## Parameters

- `observer` — The observer object to register.

## See Also

### Observing Library Availability

- [- unregisterAvailabilityObserver:](<unregisteravailabilityobserver(__).md>) — Unregisters an object from observing changes to the photo library’s availability.
- [PHPhotoLibraryAvailabilityObserver](../phphotolibraryavailabilityobserver.md) — A protocol to adopt to have the system notify your app when the availability of a photo library changes.
- [unavailabilityReason](unavailabilityreason.md) — An error that describes the reason the photo library isn’t available.
