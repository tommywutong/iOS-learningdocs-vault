---
title: 'locationManager(_:monitoringDidFailFor:withError:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.8+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Amonitoringdidfailfor%3Awitherror%3A%29.json'
content_hash: 'sha256:47b6a3b6bfe01d51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:monitoringDidFailFor:withError:)

<sub>Instance Method</sub>

Tells the delegate that a region monitoring error occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, monitoringDidFailFor region: CLRegion?, withError error: any Error)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `region` — The region for which the error occurred.

- `error` — An error object containing the error code that indicates why region monitoring failed.

## Discussion

If an error occurs while trying to monitor a given region, the location manager sends this message to its delegate. Region monitoring might fail because the region itself cannot be monitored or because there was a more general failure in configuring the region monitoring service.

Although implementation of this method is optional, it is recommended that you implement it if you use region monitoring in your application.

## See Also

### Related Documentation

- [- locationManager:didFailWithError:](<locationmanager(__didfailwitherror_).md>) — Tells the delegate that the location manager was unable to retrieve a location value.
