---
title: MKAnnotationCalloutInfoDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/mkannotationcalloutinfodidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mkannotationcalloutinfodidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/mkannotationcalloutinfodidchange.json'
content_hash: 'sha256:b446a61aee6bd937'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# MKAnnotationCalloutInfoDidChange

<sub>Type Property</sub>

A property to observe to determine when the title or subtitle information of an annotation object changes.

> [!warning] Deprecated
> Use KVO notifications instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let MKAnnotationCalloutInfoDidChange: NSNotification.Name
```

## Discussion

This notification supports legacy applications and is no longer necessary. MapKit tracks changes to the title and subtitle of an annotation using KVO notifications.
