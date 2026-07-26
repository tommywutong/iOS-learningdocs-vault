---
title: Address book entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.personal-information.addressbook
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.personal-information.addressbook'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.personal-information.addressbook.json'
content_hash: 'sha256:ea5ba03f078a5774'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Address book entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.

## Discussion

To add this entitlement to your app, enable the App Sandbox capability in Xcode and then select Contacts, or enable the Hardened Runtime capability and then select Address Book.

## See Also

### Personal information

- [Location entitlement](com.apple.security.personal-information.location.md) — A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](com.apple.security.personal-information.calendars.md) — A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
- [Photos Library Entitlement](com.apple.security.personal-information.photos-library.md) — A Boolean value that indicates whether the app has read-write access to the user’s Photos library.
