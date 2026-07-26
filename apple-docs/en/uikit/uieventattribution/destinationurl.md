---
title: destinationURL
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieventattribution/destinationurl
source_url: 'https://developer.apple.com/documentation/uikit/uieventattribution/destinationurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieventattribution/destinationurl.json'
content_hash: 'sha256:2de6cb4b9aefa22c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEventAttribution](../uieventattribution.md)

# destinationURL

<sub>Instance Property</sub>

The destination URL to attribute.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var destinationURL: URL { get }
```

## Discussion

This property contains the URL associated with the event; for example, the `destinationURL` for an advertisement contains the external link opened when the user taps the ad.

This field corresponds to the `attributed_on_site` field of a web attribution.

## See Also

### Setting attribution details

- [purchaser](purchaser.md) — The entity that purchased the ad or content.
- [reportEndpoint](reportendpoint.md) — The URL that receives attribution data.
- [sourceDescription](sourcedescription.md) — A string describing the source tapped to launch the external link.
- [sourceIdentifier](sourceidentifier.md) — A number that identifies the source of the attribution.
