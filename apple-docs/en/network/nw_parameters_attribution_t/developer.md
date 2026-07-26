---
title: nw_parameters_attribution_t.developer
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_parameters_attribution_t/developer
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_attribution_t/developer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_attribution_t/developer.json'
content_hash: 'sha256:d3754cedafb1de59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [nw_parameters_attribution_t](../nw_parameters_attribution_t.md)

# nw_parameters_attribution_t.developer

<sub>Case</sub>

A developer-initiated network request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case developer
```

## Discussion

Use this value for the `attribution` parameter of a call to the [nw_parameters_get_attribution](<../nw_parameters_get_attribution(__).md>) method when creating a network request for any purpose other than when the user explicitly accesses a link. This includes requests that your app makes to get user data. This is the default value.

For cases where the user enters a URL, like in the navigation bar of a web browser, or taps or clicks a URL to load the content it represents, use the [nw_parameters_attribution_user](user.md) value instead.

## See Also

### Request Sources

- [nw_parameters_attribution_user](user.md) — The user explicitly directs the app to make a network request.
