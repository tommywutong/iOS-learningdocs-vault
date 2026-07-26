---
title: 'locationManager(_:didVisit:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didvisit:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didvisit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidvisit%3A%29.json'
content_hash: 'sha256:15dfc1a2f3565665'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didVisit:)

<sub>Instance Method</sub>

Tells the delegate that a new visit-related event was received.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didVisit visit: CLVisit)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `visit` — The visit object that contains the information about the event.

## Discussion

The location manager calls this method whenever it has new visit event to report to your app.
