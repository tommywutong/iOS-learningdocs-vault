---
title: nw_parameters_attribution_t.user
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_parameters_attribution_t/user
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_attribution_t/user'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_attribution_t/user.json'
content_hash: 'sha256:b085d373c3ca9690'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [nw_parameters_attribution_t](../nw_parameters_attribution_t.md)

# nw_parameters_attribution_t.user

<sub>Case</sub>

The user explicitly directs the app to make a network request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case user
```

## Discussion

Use this value for the `attribution` parameter of a call to the [nw_parameters_get_attribution](<../nw_parameters_get_attribution(__).md>) method when constructing a network request that satisfies a user request to access an explicit, unmodified URL. In all other cases, use the [nw_parameters_attribution_developer](developer.md) value instead.

## See Also

### Request Sources

- [nw_parameters_attribution_developer](developer.md) — A developer-initiated network request.
