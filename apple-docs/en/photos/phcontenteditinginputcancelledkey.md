---
title: PHContentEditingInputCancelledKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginputcancelledkey
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputcancelledkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputcancelledkey.json'
content_hash: 'sha256:b5cc240455d861c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHContentEditingInputCancelledKey

<sub>Global Variable</sub>

A Boolean value indicating whether the image request was canceled. (`NSNumber`)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHContentEditingInputCancelledKey: String
```

## Discussion

If you call the [- cancelContentEditingInputRequest:](<phasset/cancelcontenteditinginputrequest(__).md>) method to cancel a request, Photos calls your result handler block with the value `true` for this key.

## See Also

### Constants

- [PHContentEditingInputResultIsInCloudKey](phcontenteditinginputresultisincloudkey.md) — A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)
- [PHContentEditingInputErrorKey](phcontenteditinginputerrorkey.md) — An error that occurred while attempting to load the asset data. (`NSError`)
