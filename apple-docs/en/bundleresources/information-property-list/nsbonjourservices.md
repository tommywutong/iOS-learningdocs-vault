---
title: NSBonjourServices
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 14.0+, iPadOS 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/nsbonjourservices
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/nsbonjourservices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nsbonjourservices.json'
content_hash: 'sha256:cc03e538a42e0718'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# NSBonjourServices

<sub>Property List Key</sub>

Bonjour service types browsed by the app.

## Discussion

The value associated with this key is an array of strings that represent Bonjour service types. Include all service types that your app expects to use. Bonjour service type strings look like `_ipp._tcp`, and `_myservice._udp`, where the first substring identifies the application protocol and the second identifies the transport protocol.

## See Also

### Network

- [NSAdvertisingAttributionReportEndpoint](nsadvertisingattributionreportendpoint.md) — The URL where Private Click Measurement and SKAdNetwork send attribution information.
- [NSAppTransportSecurity](nsapptransportsecurity.md) — A description of changes made to the default security for HTTP connections.
- [CKSharingSupported](cksharingsupported.md) — A Boolean value that indicates your app supports CloudKit Sharing.
