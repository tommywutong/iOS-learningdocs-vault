---
title: reportEndpoint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieventattribution/reportendpoint
source_url: 'https://developer.apple.com/documentation/uikit/uieventattribution/reportendpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieventattribution/reportendpoint.json'
content_hash: 'sha256:8ef9c265ca7337ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEventAttribution](../uieventattribution.md)

# reportEndpoint

<sub>Instance Property</sub>

The URL that receives attribution data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var reportEndpoint: URL? { get }
```

## Discussion

This read-only property contains the URL that recieves the event attribution data. Your app sets this value by reading it from its `Info.plist` using the [NSAdvertisingAttributionReportEndpoint](../../bundleresources/information-property-list/nsadvertisingattributionreportendpoint.md) key.

Specify the desired value in your Xcode project’s `Info.plist` file. Your app uses the value you set in all PCM attribution requests. You can’t change the value at runtime.

This field corresponds to the `source_site` field of a web attribution.

## See Also

### Setting attribution details

- [destinationURL](destinationurl.md) — The destination URL to attribute.
- [purchaser](purchaser.md) — The entity that purchased the ad or content.
- [sourceDescription](sourcedescription.md) — A string describing the source tapped to launch the external link.
- [sourceIdentifier](sourceidentifier.md) — A number that identifies the source of the attribution.
