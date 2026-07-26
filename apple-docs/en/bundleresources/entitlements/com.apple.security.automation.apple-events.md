---
title: Apple Events Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.automation.apple-events
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.automation.apple-events'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.automation.apple-events.json'
content_hash: 'sha256:f27cbdfe3d0fd51d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Apple Events Entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether the app may prompt the user for permission to send Apple events to other apps.

## Discussion

Your app doesn’t need the Apple Events entitlement if it only sends Apple events to itself or to other processes signed with the same team ID.

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Resource Access, select Apple Events.
