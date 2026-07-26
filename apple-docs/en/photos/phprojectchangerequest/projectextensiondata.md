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
doc_path: /documentation/photos/phprojectchangerequest/projectextensiondata
source_url: 'https://developer.apple.com/documentation/photos/phprojectchangerequest/projectextensiondata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phprojectchangerequest/projectextensiondata.json'
content_hash: 'sha256:9af77646e62be3c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHProjectChangeRequest](../phprojectchangerequest.md)

# projectExtensionData

<sub>Instance Property</sub>

Compressed project-specific data to use in the change request.

<sub>macOS</sub>

```swift
var projectExtensionData: Data { get set }
```

## Discussion

The total size of stored data is limited to 5 MB; attempting to store more data will result in an error. Don’t include rasterized images that can be locally cached. Limit stored data to compressed project-specific data.

## See Also

### Creating Change Requests

- [- initWithProject:](<init(project_).md>) — Creates a change request around the specified project.
- [title](title.md) — The title of the change request.
