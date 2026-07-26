---
title: PHContentEditingInputErrorKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginputerrorkey
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputerrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputerrorkey.json'
content_hash: 'sha256:04b93b434303ee53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHContentEditingInputErrorKey

<sub>Global Variable</sub>

An error that occurred while attempting to load the asset data. (`NSError`)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHContentEditingInputErrorKey: String
```

## Discussion

Photos provides an error object for this key if it cannot provide asset data for your handler block’s `contentEditingInput` parameter. Examine the error object for information about the cause of the error.

## See Also

### Constants

- [PHContentEditingInputResultIsInCloudKey](phcontenteditinginputresultisincloudkey.md) — A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)
- [PHContentEditingInputCancelledKey](phcontenteditinginputcancelledkey.md) — A Boolean value indicating whether the image request was canceled. (`NSNumber`)
