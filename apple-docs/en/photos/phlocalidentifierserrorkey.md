---
title: PHLocalIdentifiersErrorKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlocalidentifierserrorkey
source_url: 'https://developer.apple.com/documentation/photos/phlocalidentifierserrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlocalidentifierserrorkey.json'
content_hash: 'sha256:bd2d1debd1b863c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLocalIdentifiersErrorKey

<sub>Global Variable</sub>

An error key that retrieves an array of string values representing local identifiers matched to a cloud identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHLocalIdentifiersErrorKey: String
```

## Discussion

Use this key with the [userInfo](../foundation/nserror/userinfo.md) property when encountering the [multipleIdentifiersFound](phphotoserror-swift.struct/multipleidentifiersfound.md) error.

## See Also

### Inspecting an Error

- [errorDomain](phphotoserror-swift.struct/errordomain.md)
- [Code](phphotoserror-swift.struct/code.md) — Error codes for framework operations.
- [Error Constants](../photokit/error-constants.md) — Error code constants for framework operations.
