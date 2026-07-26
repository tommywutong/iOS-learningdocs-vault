---
title: appEntityIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, macOS 15.2+, tvOS 18.2+, visionOS 2.2+, watchOS 11.2+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/appentityidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/appentityidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/appentityidentifier.json'
content_hash: 'sha256:faa25b7bdd0e8418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# appEntityIdentifier

<sub>Instance Property</sub>

The identifier of an app entity that you associate with the user activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var appEntityIdentifier: EntityIdentifier? { get set }
```

## Discussion

By associating an app entity with a user activity, you make the entity available to Siri and Apple Intelligence. To clear the association with the app entity, set `appEntityIdentifier` to `nil`.

For more information, refer to doc://com.apple.documentation/documentation/appintents/Making-onscreen-content-available-to-siri-and-apple-intelligence and [App Intents](../../appintents.md).

## See Also

### Specifying app identifiers

- [targetContentIdentifier](targetcontentidentifier.md) — A string that identifies the user activity’s content.
- [externalMediaContentIdentifier](externalmediacontentidentifier.md) — A unique identifier from the app’s media content catalog for the currently displayed media item.
