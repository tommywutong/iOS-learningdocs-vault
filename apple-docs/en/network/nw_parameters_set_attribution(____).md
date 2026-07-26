---
title: 'nw_parameters_set_attribution(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_set_attribution(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_set_attribution(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_set_attribution%28_%3A_%3A%29.json'
content_hash: 'sha256:1d9c65ea46f08e37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_set_attribution(_:_:)

<sub>Function</sub>

Sets a flag that indicates whether the network request originates from the developer or the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_set_attribution(_ parameters: nw_parameters_t, _ attribution: nw_parameters_attribution_t)
```

## Parameters

- `parameters` — The network parameters to update.

- `attribution` — An indication of whether the network request comes from the developer or from the user.

## Discussion

If you don’t set this flag, the system assumes a value of [nw_parameters_attribution_developer](nw_parameters_attribution_t/developer.md). Use this default value for any network request that your app makes that isn’t explicitly from the user. This includes requests that you make to your own server, even when you load user data. It also includes links that the user selects, but that you modify in any way — including by adding HTTP headers — before loading the content.

Set this value to [nw_parameters_attribution_user](nw_parameters_attribution_t/user.md) only for requests that the user explicitly makes, like when the user enters a URL or taps or clicks a URL that they can read, and only if your app loads and displays the data without altering the request.

## See Also

### Traffic Attribution

- [Inspecting app activity data](inspecting-app-activity-data.md) — Verify that your app accesses only the user data and network resources that you expect it to access.
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md) — Control whether the App Privacy Report attributes network traffic to the app or to the user.
- [nw_parameters_get_attribution](<nw_parameters_get_attribution(__).md>) — Gets a flag that indicates whether the network request originates from the developer or the user.
- [nw_parameters_attribution_t](nw_parameters_attribution_t.md) — The entities that can make a network request.
