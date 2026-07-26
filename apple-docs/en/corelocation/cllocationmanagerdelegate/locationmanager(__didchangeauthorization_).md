---
title: 'locationManager(_:didChangeAuthorization:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+（14.0 起废弃）, iPadOS 4.2+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.7+（11.0 起废弃）, tvOS 9.0+（14.0 起废弃）, watchOS 1.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidchangeauthorization%3A%29.json'
content_hash: 'sha256:b27b3d373dee4b05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didChangeAuthorization:)

<sub>Instance Method</sub>

Tells the delegate its authorization status when the app creates the location manager and when the authorization status changes.

> [!warning] Deprecated
> Use [- locationManagerDidChangeAuthorization:](<locationmanagerdidchangeauthorization(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus)
```

## Parameters

- `manager` — The location manager object reporting the event.

- `status` — The authorization status for the app.

## See Also

### Responding to authorization changes

- [- locationManagerDidChangeAuthorization:](<locationmanagerdidchangeauthorization(__).md>) — Tells the delegate when the app creates the location manager and when the authorization status changes.
