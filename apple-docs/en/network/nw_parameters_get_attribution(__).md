---
title: 'nw_parameters_get_attribution(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_get_attribution(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_get_attribution(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_get_attribution%28_%3A%29.json'
content_hash: 'sha256:50e7eb8e90218e35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_get_attribution(_:)

<sub>Function</sub>

Gets a flag that indicates whether the network request originates from the developer or the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_get_attribution(_ parameters: nw_parameters_t) -> nw_parameters_attribution_t
```

## Parameters

- `parameters` — The network parameters to read from.

## Return Value

An indication of whether the network request comes from the developer or from the user.

## See Also

### Traffic Attribution

- [Inspecting app activity data](inspecting-app-activity-data.md) — Verify that your app accesses only the user data and network resources that you expect it to access.
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md) — Control whether the App Privacy Report attributes network traffic to the app or to the user.
- [nw_parameters_set_attribution](<nw_parameters_set_attribution(____).md>) — Sets a flag that indicates whether the network request originates from the developer or the user.
- [nw_parameters_attribution_t](nw_parameters_attribution_t.md) — The entities that can make a network request.
