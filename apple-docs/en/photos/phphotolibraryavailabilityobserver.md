---
title: PHPhotoLibraryAvailabilityObserver
framework: Photos
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotolibraryavailabilityobserver
source_url: 'https://developer.apple.com/documentation/photos/phphotolibraryavailabilityobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibraryavailabilityobserver.json'
content_hash: 'sha256:0bf2c310973d4d95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHPhotoLibraryAvailabilityObserver

<sub>Protocol</sub>

A protocol to adopt to have the system notify your app when the availability of a photo library changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol PHPhotoLibraryAvailabilityObserver : NSObjectProtocol
```

## Overview

Observing changes to the photo library’s availability is primarily of concern with Mac apps created using macOS and Mac Catalyst, where the library may reside on an external drive or in cloud storage.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Observing Availability Changes

- [- photoLibraryDidBecomeUnavailable:](<phphotolibraryavailabilityobserver/photolibrarydidbecomeunavailable(__).md>) — Tells the observer that the photo library’s availability changed.

## See Also

### Observing Library Availability

- [- registerAvailabilityObserver:](<phphotolibrary/register(__)-gm0a.md>) — Registers an object to observe changes to the photo library’s availability.
- [- unregisterAvailabilityObserver:](<phphotolibrary/unregisteravailabilityobserver(__).md>) — Unregisters an object from observing changes to the photo library’s availability.
- [unavailabilityReason](phphotolibrary/unavailabilityreason.md) — An error that describes the reason the photo library isn’t available.
