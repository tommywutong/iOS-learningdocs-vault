---
title: intent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/intent
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/intent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/intent.json'
content_hash: 'sha256:ec4d65b847317a43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# intent

<sub>Instance Property</sub>

Metadata for populating your share extensions interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
var intent: INIntent? { get }
```

## Discussion

When the user selects an app from the list of suggested apps in iOS’s share sheet, this property contains metadata that you can use to populate your share extensions interface. The source for the metadata is the [INSendMessageIntent](../../intents/insendmessageintent.md) of your messaging app.

This property is `nil` if your app’s share extension wasn’t launched from the list of suggested apps.

> [!note] Note
> To learn more about adding a share extension to the list of suggested apps, read [Supporting suggestions in your app’s share extension](../supporting-suggestions-in-your-app-s-share-extension.md).
