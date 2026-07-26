---
title: sourceDescription
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieventattribution/sourcedescription
source_url: 'https://developer.apple.com/documentation/uikit/uieventattribution/sourcedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieventattribution/sourcedescription.json'
content_hash: 'sha256:b7f75044071b9222'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEventAttribution](../uieventattribution.md)

# sourceDescription

<sub>Instance Property</sub>

A string describing the source tapped to launch the external link.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceDescription: String { get }
```

## Discussion

This property contains a description of the attribution source. For example, for an ad, `sourceDescription` describes the content of the advertisement that the user tapped.

The system may truncate this field if it’s longer than 100 characters.

## See Also

### Setting attribution details

- [destinationURL](destinationurl.md) — The destination URL to attribute.
- [purchaser](purchaser.md) — The entity that purchased the ad or content.
- [reportEndpoint](reportendpoint.md) — The URL that receives attribution data.
- [sourceIdentifier](sourceidentifier.md) — A number that identifies the source of the attribution.
