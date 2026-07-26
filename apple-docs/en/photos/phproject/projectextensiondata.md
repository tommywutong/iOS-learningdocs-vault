---
title: projectExtensionData
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phproject/projectextensiondata
source_url: 'https://developer.apple.com/documentation/photos/phproject/projectextensiondata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phproject/projectextensiondata.json'
content_hash: 'sha256:8f3c7d91803e8032'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHProject](../phproject.md)

# projectExtensionData

<sub>Instance Property</sub>

Data associated with the project extension.

<sub>macOS</sub>

```swift
var projectExtensionData: Data { get }
```

## Discussion

The total size of stored data is limited to 5 MB; attempting to store more data will result in an error. Don’t include rasterized images that can be locally cached. Limit stored data to compressed project-specific data.

## See Also

### Project Extension Properties

- [hasProjectPreview](hasprojectpreview.md) — A property that indicates whether a project preview was previously set.
