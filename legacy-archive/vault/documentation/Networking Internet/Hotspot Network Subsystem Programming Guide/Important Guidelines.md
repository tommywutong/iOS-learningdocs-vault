---
title: Hotspot Network Subsystem Programming Guide
apple_id: TP40016639
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/Hotspot_Network_Subsystem_Guide/Contents/ImportantGuidelines.html
archived_at: '2026-07-15T08:18:49.627135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Hotspot Network Subsystem Programming Guide](About%20the%20Hotspot%20Network%20Subsystem.md)


[Next](Document%20Revision%20History.md)[Previous](Hotspot%20Helper%20Command%20Handling%20Details.md)

# Important Guidelines

The Hotspot Helper application MUST adhere to the following guidelines.

When given the `Evaluate` command, do not blindly return `kHotspotHelperConfidenceHigh` without knowing that the network is one your app can handle.

The helper contributes to the overall user experience of connecting to Wi-Fi networks. Handling commands efficiently means that there is CPU left over for other processing to take place.

Respond to commands with low latency. The state machine relies on input from the helpers to make progress. The obvious exception to this is the `PresentUI` command, which relies on user input and is therefore not bounded in time.

The display name `kNEHotspotHelperOptionDisplayName` should be no longer than 15 characters. This restriction allows the user interface to more easily show multiple helpers that have claimed a given network.

When multiple helpers are installed, it’s possible that more than one helper is able to authenticate to the same Wi-Fi network. When such a Wi-Fi network is joined, there is no guarantee that a particular helper will perform the authentication. In most cases, it doesn’t matter which helper does the authentication, but in some cases cost or other factors make it desirable to select a particular helper.

To help resolve this issue, the helper application should provide configuration UI to disable the helper globally and/or by SSID. That way, the user can influence which helper performs the authentication.

[Next](Document%20Revision%20History.md)[Previous](Hotspot%20Helper%20Command%20Handling%20Details.md)

