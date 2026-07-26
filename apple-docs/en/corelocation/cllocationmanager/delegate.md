---
title: delegate
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/delegate
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/delegate.json'
content_hash: 'sha256:8c0cad033564d80a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# delegate

<sub>Instance Property</sub>

The delegate object to receive update events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any CLLocationManagerDelegate)? { get set }
```

## Discussion

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Receiving data from location services

- [CLLocationManagerDelegate](../cllocationmanagerdelegate.md) — The methods you use to receive events from an associated location-manager object.
