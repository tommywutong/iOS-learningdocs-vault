---
title: notFound
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.13+（12.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phcloudidentifier/notfound
source_url: 'https://developer.apple.com/documentation/photos/phcloudidentifier/notfound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcloudidentifier/notfound.json'
content_hash: 'sha256:968419e2edcf2102'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCloudIdentifier](../phcloudidentifier.md)

# notFound

<sub>Type Property</sub>

The global identifier used in an array slot for items that couldn’t be found.

> [!warning] Deprecated
> Check for PHPhotosErrorIdentifierNotFound in PHCloudIdentifierMapping.error

<sub>macOS</sub>

```swift
class var notFound: PHCloudIdentifier { get }
```

## See Also

### Using Cloud Identifiers

- [- initWithStringValue:](<init(stringvalue_).md>) — Deserializes a cloud identifier from its string value. _(deprecated)_
- [stringValue](stringvalue.md) — A string version of the cloud identifier to use in serialization. _(deprecated)_
