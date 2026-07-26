---
title: CTRadioAccessTechnologyDidChangeNotification
framework: Core Telephony
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（12.0 起废弃）, iPadOS 7.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coretelephony/ctradioaccesstechnologydidchangenotification
source_url: 'https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologydidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretelephony/ctradioaccesstechnologydidchangenotification.json'
content_hash: 'sha256:0a4eb5c21a93be45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Telephony](../coretelephony.md)

# CTRadioAccessTechnologyDidChangeNotification

<sub>Global Variable</sub>

The name of the notification indicating that the radio access technology changed for one of the services.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
extern NSString * const CTRadioAccessTechnologyDidChangeNotification;
```

## Discussion

The notification’s [object](../foundation/nsnotification/object.md) is an [NSString](../foundation/nsstring.md) that represents the service identifier of the service whose radio access technology has changed. Use this string as the key in [serviceCurrentRadioAccessTechnology](cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md) to get the value of the new radio access technology for the service.

## See Also

### Deprecated

- [currentRadioAccessTechnology](cttelephonynetworkinfo/currentradioaccesstechnology.md) — The current radio access technology registered with the device. _(deprecated)_
- [subscriberCellularProvider](cttelephonynetworkinfo/subscribercellularprovider.md) — Information about the user’s cellular service provider. _(deprecated)_
- [subscriberCellularProviderDidUpdateNotifier](cttelephonynetworkinfo/subscribercellularproviderdidupdatenotifier.md) — A block dispatched when the user’s cellular service provider information changes. _(deprecated)_
- [serviceSubscriberCellularProviders](cttelephonynetworkinfo/servicesubscribercellularproviders.md) — A dictionary that contains carrier information about each service. _(deprecated)_
- [serviceSubscriberCellularProvidersDidUpdateNotifier](cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier.md) — A block dispatched when there are updates to the user’s cellular provider information for any service. _(deprecated)_
- [CTServiceRadioAccessTechnologyDidChangeNotification](ctserviceradioaccesstechnologydidchangenotification.md)
