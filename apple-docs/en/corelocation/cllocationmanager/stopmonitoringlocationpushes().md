---
title: stopMonitoringLocationPushes()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/stopmonitoringlocationpushes()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoringlocationpushes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/stopmonitoringlocationpushes%28%29.json'
content_hash: 'sha256:57d71927d085af7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# stopMonitoringLocationPushes()

<sub>Instance Method</sub>

Stops monitoring for Apple Push Notification service (APNs) location pushes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func stopMonitoringLocationPushes()
```

## Discussion

Call this method to stop the device from monitoring for APNs location pushes. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Monitoring location push notifications

- [- startMonitoringLocationPushesWithCompletion:](<startmonitoringlocationpushes(completion_).md>) — Starts monitoring for the delivery of Apple Push Notification service (APNs) location pushes, and provides a device-specific token for sending pushes.
