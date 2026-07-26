---
title: volumeAvailableCapacityForImportantUsageKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/volumeavailablecapacityforimportantusagekey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/volumeavailablecapacityforimportantusagekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/volumeavailablecapacityforimportantusagekey.json'
content_hash: 'sha256:73a41c2818920492'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# volumeAvailableCapacityForImportantUsageKey

<sub>Type Property</sub>

Key for the volume’s available capacity in bytes for storing important resources (read-only).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let volumeAvailableCapacityForImportantUsageKey: URLResourceKey
```

## Discussion

> [!important] Important
> This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [Describing use of required reason API](../../bundleresources/describing-use-of-required-reason-api.md).

## See Also

### Volume capacity keys

- [Checking Volume Storage Capacity](../checking-volume-storage-capacity.md) — Confirm that you have enough local storage space for a large amount of data.
- [NSURLVolumeAvailableCapacityKey](volumeavailablecapacitykey.md) — Key for the volume’s available capacity in bytes (read-only).
- [NSURLVolumeAvailableCapacityForOpportunisticUsageKey](volumeavailablecapacityforopportunisticusagekey.md) — Key for the volume’s available capacity in bytes for storing nonessential resources (read-only).
- [NSURLVolumeTotalCapacityKey](volumetotalcapacitykey.md) — Key for the volume’s total capacity in bytes (read-only).
