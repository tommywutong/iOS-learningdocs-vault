---
title: NSAdvertisingAttributionReportEndpoint
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 14.5+, iPadOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/nsadvertisingattributionreportendpoint
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/nsadvertisingattributionreportendpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nsadvertisingattributionreportendpoint.json'
content_hash: 'sha256:b83c3de632fd972f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# NSAdvertisingAttributionReportEndpoint

<sub>Property List Key</sub>

The URL where Private Click Measurement and SKAdNetwork send attribution information.

## Discussion

This key is a string that contains a valid URL containing your domain name. Provide a string in the format `“https://example.com”`, where you replace `example` with your domain name. Include this key in your app for the following two uses:

- To specify where the system sends event attribution data it receives from launched websites that support Private Click Measurement (PCM). PCM won’t work if your app doesn’t include this key.
- To specify where the system sends a copy of the winning install-validation postback to the advertised app’s developer, for apps that are advertised using the [SKAdNetwork](../../storekit/skadnetwork.md) API. Including this key is optional.

The system sends postbacks to a well-known URL it generates using the domain name you provide in the key. To receive the postbacks, configure your server to receive HTTPS POST messages at the following endpoints:

- To receive PCM event attribution data: `https://example.com/.well-known/private-click-measurement/report-attribution/`
- To receive SKAdNetwork install-validation postbacks: `https://example.com/.well-known/skadnetwork/report-attribution/`

Replace `example.com` with your domain name. The system uses only the registrable part of the domain name, and ignores any subdomains.

For more information about PCM and setting up a server to receive event attribution data, see [Introducing Private Click Measurement](https://webkit.org/blog/11529/introducing-private-click-measurement-pcm/). For more information about configuring an advertised app to enable its developer to receive postbacks, see [Configuring an advertised app](../../storekit/configuring-an-advertised-app.md) and [SKAdNetwork](../../storekit/skadnetwork.md).

> [!note] Note
> Mac apps built with Mac Catalyst don’t support PCM.

## See Also

### Network

- [NSAppTransportSecurity](nsapptransportsecurity.md) — A description of changes made to the default security for HTTP connections.
- [NSBonjourServices](nsbonjourservices.md) — Bonjour service types browsed by the app.
- [CKSharingSupported](cksharingsupported.md) — A Boolean value that indicates your app supports CloudKit Sharing.
