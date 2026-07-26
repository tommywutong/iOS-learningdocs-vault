---
title: nw_parameters_attribution_t
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_parameters_attribution_t
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_attribution_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_attribution_t.json'
content_hash: 'sha256:c04211c0e8d07608'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_attribution_t

<sub>Enumeration</sub>

The entities that can make a network request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum nw_parameters_attribution_t
```

## Overview

Use one of these values when setting the `attribution` parameter of a network request with the [nw_parameters_get_attribution](<nw_parameters_get_attribution(__).md>) method. If you don’t set a value, the system assumes [nw_parameters_attribution_developer](nw_parameters_attribution_t/developer.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Request Sources

- [nw_parameters_attribution_developer](nw_parameters_attribution_t/developer.md) — A developer-initiated network request.
- [nw_parameters_attribution_user](nw_parameters_attribution_t/user.md) — The user explicitly directs the app to make a network request.

### Initializers

- [init(rawValue:)](<nw_parameters_attribution_t/init(rawvalue_).md>)

## See Also

### Traffic Attribution

- [Inspecting app activity data](inspecting-app-activity-data.md) — Verify that your app accesses only the user data and network resources that you expect it to access.
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md) — Control whether the App Privacy Report attributes network traffic to the app or to the user.
- [nw_parameters_set_attribution](<nw_parameters_set_attribution(____).md>) — Sets a flag that indicates whether the network request originates from the developer or the user.
- [nw_parameters_get_attribution](<nw_parameters_get_attribution(__).md>) — Gets a flag that indicates whether the network request originates from the developer or the user.
