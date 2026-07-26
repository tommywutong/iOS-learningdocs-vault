---
title: annotation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/openurloptions/annotation
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/openurloptions/annotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/openurloptions/annotation.json'
content_hash: 'sha256:19abc17db2672609'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [OpenURLOptions](../openurloptions.md)

# annotation

<sub>Instance Property</sub>

A property-list object that contains the annotation data provided by a document interaction controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var annotation: Any? { get }
```

## Discussion

This property contains the data that the originating app placed in the [annotation](../../uidocumentinteractioncontroller/annotation.md) property of its [UIDocumentInteractionController](../../uidocumentinteractioncontroller.md). The root object is always an [NSDictionary](../../../foundation/nsdictionary.md) object. The contents of that dictionary may be any other property list types, including [NSDictionary](../../../foundation/nsdictionary.md), [NSArray](../../../foundation/nsarray.md), [NSData](../../../foundation/nsdata.md), [NSString](../../../foundation/nsstring.md), [NSNumber](../../../foundation/nsnumber.md), or [NSDate](../../../foundation/nsdate.md) objects.

## See Also

### Specifying the URL details

- [sourceApplication](sourceapplication.md) — The bundle ID of the app that originated the request.
- [eventAttribution](eventattribution.md) — An event attribution associated with the URL to open.
