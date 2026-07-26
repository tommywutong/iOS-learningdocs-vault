---
title: CTRadioAccessTechnologyDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+（12.0 起废弃）, iPadOS 7.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange.json'
content_hash: 'sha256:037b8407c8b989a4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# CTRadioAccessTechnologyDidChange

<sub>Type Property</sub>

The name of the notification indicating that the radio access technology changed for one of the services.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let CTRadioAccessTechnologyDidChange: NSNotification.Name
```

## Discussion

The notification’s [object](../object.md) is an [NSString](../../nsstring.md) that represents the service identifier of the service whose radio access technology has changed. Use this string as the key in [serviceCurrentRadioAccessTechnology](../../../coretelephony/cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md) to get the value of the new radio access technology for the service.

## See Also

### Core Telephony

- [CTServiceRadioAccessTechnologyDidChange](ctserviceradioaccesstechnologydidchange.md) — A notification that posts when radio access technology changes.
