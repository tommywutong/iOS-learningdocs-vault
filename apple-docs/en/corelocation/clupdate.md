---
title: CLUpdate
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clupdate
source_url: 'https://developer.apple.com/documentation/corelocation/clupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clupdate.json'
content_hash: 'sha256:b56e00fbcdde631d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLUpdate

<sub>Class</sub>

An object that represents a location update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLUpdate : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Update properties

- [isStationary](clupdate/isstationary.md) — A Boolean value that indicates whether the device is stationary. _(deprecated)_
- [location](clupdate/location.md) — A person’s location, if available.

### Instance Properties

- [accuracyLimited](clupdate/accuracylimited.md)
- [authorizationDenied](clupdate/authorizationdenied.md)
- [authorizationDeniedGlobally](clupdate/authorizationdeniedglobally.md)
- [authorizationRequestInProgress](clupdate/authorizationrequestinprogress.md)
- [authorizationRestricted](clupdate/authorizationrestricted.md)
- [insufficientlyInUse](clupdate/insufficientlyinuse.md)
- [locationUnavailable](clupdate/locationunavailable.md)
- [serviceSessionRequired](clupdate/servicesessionrequired.md)
- [stationary](clupdate/stationary.md)

## See Also

### Monitoring

- [CLMonitor](clmonitor-6ynwz.md) — An object that monitors the conditions you add to it.
