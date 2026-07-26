---
title: stopMonitoringVisits()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/stopmonitoringvisits()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoringvisits()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/stopmonitoringvisits%28%29.json'
content_hash: 'sha256:0f724ce2ad57dee7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# stopMonitoringVisits()

<sub>Instance Method</sub>

Stops the delivery of visit-related events.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func stopMonitoringVisits()
```

## Discussion

Calling this method disables the delivery of visit-related events for your app. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the visits location service

- [- startMonitoringVisits](<startmonitoringvisits().md>) — Starts the delivery of visit-related events.
