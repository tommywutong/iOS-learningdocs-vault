---
title: CTServiceRadioAccessTechnologyDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/ctserviceradioaccesstechnologydidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ctserviceradioaccesstechnologydidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/ctserviceradioaccesstechnologydidchange.json'
content_hash: 'sha256:6dcfd3b966325c4d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# CTServiceRadioAccessTechnologyDidChange

<sub>Type Property</sub>

A notification that posts when radio access technology changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let CTServiceRadioAccessTechnologyDidChange: NSNotification.Name
```

## Discussion

The notification’s `object` is a string that represents the identifier of the service with changes to its radio access technology.  Use this identifier as the key in [serviceCurrentRadioAccessTechnology](../../../coretelephony/cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md) to get the value of the new radio access technology for the service.

## See Also

### Core Telephony

- [CTRadioAccessTechnologyDidChange](ctradioaccesstechnologydidchange.md) — The name of the notification indicating that the radio access technology changed for one of the services. _(deprecated)_
