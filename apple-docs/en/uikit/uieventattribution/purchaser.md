---
title: purchaser
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieventattribution/purchaser
source_url: 'https://developer.apple.com/documentation/uikit/uieventattribution/purchaser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieventattribution/purchaser.json'
content_hash: 'sha256:a75980ec094e2937'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEventAttribution](../uieventattribution.md)

# purchaser

<sub>Instance Property</sub>

The entity that purchased the ad or content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var purchaser: String { get }
```

## Discussion

This property contains the name of the party that purchased the ad or other content. For example, for an in-app ad, this would contain the name of the company or individual that purchased the advertisement. The system may truncate this field if it’s longer than 100 characters.

## See Also

### Setting attribution details

- [destinationURL](destinationurl.md) — The destination URL to attribute.
- [reportEndpoint](reportendpoint.md) — The URL that receives attribution data.
- [sourceDescription](sourcedescription.md) — A string describing the source tapped to launch the external link.
- [sourceIdentifier](sourceidentifier.md) — A number that identifies the source of the attribution.
