---
title: MKAnnotationCalloutInfoDidChangeNotification
framework: MapKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkannotationcalloutinfodidchangenotification
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationcalloutinfodidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationcalloutinfodidchangenotification.json'
content_hash: 'sha256:6b0f1815e0ae00f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKAnnotationCalloutInfoDidChangeNotification

<sub>Global Variable</sub>

A property to observe to determine when the title or subtitle information of an annotation object changes.

> [!warning] Deprecated
> Use KVO notifications instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const MKAnnotationCalloutInfoDidChangeNotification;
```

## Discussion

This notification supports legacy applications and is no longer necessary. MapKit tracks changes to the title and subtitle of an annotation using KVO notifications.
