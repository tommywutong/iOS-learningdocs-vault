---
title: stopMonitoringSignificantLocationChanges()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/stopmonitoringsignificantlocationchanges()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoringsignificantlocationchanges()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/stopmonitoringsignificantlocationchanges%28%29.json'
content_hash: 'sha256:37d41151eb506e36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# stopMonitoringSignificantLocationChanges()

<sub>Instance Method</sub>

Stops the delivery of location events based on significant location changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func stopMonitoringSignificantLocationChanges()
```

## Discussion

Use this method to stop the delivery of location events that was started using the [- startMonitoringSignificantLocationChanges](<startmonitoringsignificantlocationchanges().md>) method. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the significant change location service

- [- startMonitoringSignificantLocationChanges](<startmonitoringsignificantlocationchanges().md>) — Starts the generation of updates based on significant location changes.
