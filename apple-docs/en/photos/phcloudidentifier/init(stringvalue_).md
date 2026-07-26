---
title: 'init(stringValue:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phcloudidentifier/init(stringvalue:)'
source_url: 'https://developer.apple.com/documentation/photos/phcloudidentifier/init(stringvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcloudidentifier/init%28stringvalue%3A%29.json'
content_hash: 'sha256:c1bab7c08647cbc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCloudIdentifier](../phcloudidentifier.md)

# init(stringValue:)

<sub>Initializer</sub>

Deserializes a cloud identifier from its string value.

> [!warning] Deprecated
> Use initWithArchivalStringValue: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(stringValue: String)
```

## See Also

### Using Cloud Identifiers

- [stringValue](stringvalue.md) — A string version of the cloud identifier to use in serialization. _(deprecated)_
- [notFoundIdentifier](notfound.md) — The global identifier used in an array slot for items that couldn’t be found. _(deprecated)_
