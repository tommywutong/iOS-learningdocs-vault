---
title: NSLocalNetworkUsageDescription
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 14.0+, iPadOS 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/nslocalnetworkusagedescription
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/nslocalnetworkusagedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nslocalnetworkusagedescription.json'
content_hash: 'sha256:861bc400adb4c5fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# NSLocalNetworkUsageDescription

<sub>Property List Key</sub>

A message that tells people why the app is requesting access to the local network.

## Discussion

Any app that uses the local network, directly or indirectly, should include this description. This includes apps that use Bonjour and services implemented with Bonjour, as well as direct unicast or multicast connections to local hosts.

## See Also

### Networking

- [NSNearbyInteractionUsageDescription](nsnearbyinteractionusagedescription.md) — A request for user permission to begin an interaction session with nearby devices.
- [NSNearbyInteractionAllowOnceUsageDescription](nsnearbyinteractionallowonceusagedescription.md) — A one-time request for user permission to begin an interaction session with nearby devices. _(deprecated)_
