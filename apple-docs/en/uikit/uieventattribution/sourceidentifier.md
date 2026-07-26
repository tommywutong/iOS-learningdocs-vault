---
title: sourceIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieventattribution/sourceidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uieventattribution/sourceidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieventattribution/sourceidentifier.json'
content_hash: 'sha256:d60696d38aad3c9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEventAttribution](../uieventattribution.md)

# sourceIdentifier

<sub>Instance Property</sub>

A number that identifies the source of the attribution.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceIdentifier: UInt8 { get }
```

## Discussion

This property contains an integer, between 0 and 255, that identifies the source of the attribution. For example, for an ad, `sourceIdentifier` might contain a campaign identifier so the advertiser can measure the effectiveness of different advertising campaigns.

This field corresponds to the `source_id` field of a web attribution.

## See Also

### Setting attribution details

- [destinationURL](destinationurl.md) — The destination URL to attribute.
- [purchaser](purchaser.md) — The entity that purchased the ad or content.
- [reportEndpoint](reportendpoint.md) — The URL that receives attribution data.
- [sourceDescription](sourcedescription.md) — A string describing the source tapped to launch the external link.
