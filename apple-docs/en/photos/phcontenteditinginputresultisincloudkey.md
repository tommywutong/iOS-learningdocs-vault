---
title: PHContentEditingInputResultIsInCloudKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginputresultisincloudkey
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputresultisincloudkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputresultisincloudkey.json'
content_hash: 'sha256:3b5631e5b7e63c0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHContentEditingInputResultIsInCloudKey

<sub>Global Variable</sub>

A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHContentEditingInputResultIsInCloudKey: String
```

## Discussion

If `true`, no asset data was provided because the asset data must be downloaded from iCloud. To do this, submit another request, specifying `true` for the [networkAccessAllowed](phcontenteditinginputrequestoptions/isnetworkaccessallowed.md) option.

## See Also

### Constants

- [PHContentEditingInputCancelledKey](phcontenteditinginputcancelledkey.md) — A Boolean value indicating whether the image request was canceled. (`NSNumber`)
- [PHContentEditingInputErrorKey](phcontenteditinginputerrorkey.md) — An error that occurred while attempting to load the asset data. (`NSError`)
