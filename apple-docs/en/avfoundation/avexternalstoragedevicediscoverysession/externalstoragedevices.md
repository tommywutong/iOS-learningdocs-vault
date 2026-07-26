---
title: externalStorageDevices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevicediscoverysession/externalstoragedevices
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevicediscoverysession/externalstoragedevices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevicediscoverysession/externalstoragedevices.json'
content_hash: 'sha256:3dc902c5bee464f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalStorageDeviceDiscoverySession](../avexternalstoragedevicediscoverysession.md)

# externalStorageDevices

<sub>Instance Property</sub>

An array of external storage devices the session updates as individual devices connect or disconnect from the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var externalStorageDevices: [AVExternalStorageDevice] { get }
```

## Discussion

Your app can monitor the changes to this array with a key-value observation.
