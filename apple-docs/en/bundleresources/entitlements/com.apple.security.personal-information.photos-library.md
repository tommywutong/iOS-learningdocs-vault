---
title: Photos Library Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.personal-information.photos-library
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.personal-information.photos-library'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.personal-information.photos-library.json'
content_hash: 'sha256:d879befaf3083b7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Photos Library Entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether the app has read-write access to the user’s Photos library.

## Discussion

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode. Then, under Resource Access, select Photos Library.

## See Also

### Personal information

- [Address book entitlement](com.apple.security.personal-information.addressbook.md) — A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Location entitlement](com.apple.security.personal-information.location.md) — A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](com.apple.security.personal-information.calendars.md) — A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
