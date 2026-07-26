---
title: sr_sensorForDeletionRecordsFromSensor()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsstring/sr_sensorfordeletionrecordsfromsensor()
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/sr_sensorfordeletionrecordsfromsensor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/sr_sensorfordeletionrecordsfromsensor%28%29.json'
content_hash: 'sha256:2e5919ac856c10bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# sr_sensorForDeletionRecordsFromSensor()

<sub>Instance Method</sub>

> [!warning] Deprecated
> Use deletionRecords(matching request: SRFetchRequest) of SRReader\<Sensor\> class

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func sr_sensorForDeletionRecordsFromSensor() -> SRSensor?
```

## Return Value

May return nil if there is no deletion record available for this sensor

## Discussion

Returns a sensor stream that contains deletion records of the sensor

This sensor stream should only be used for fetching. All other operations will be ignored. Deletion records share the recording and authorization state with their parent sensor.
