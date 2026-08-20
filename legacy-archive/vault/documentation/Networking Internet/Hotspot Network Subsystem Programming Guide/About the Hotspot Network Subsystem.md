---
title: Hotspot Network Subsystem Programming Guide
apple_id: TP40016639
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/Hotspot_Network_Subsystem_Guide/Contents/Introduction.html
archived_at: '2026-07-15T08:18:49.635827Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Authentication%20State%20Machine.md)

# About the Hotspot Network Subsystem

The Hotspot Network Subsystem allows a Hotspot Helper application to participate in the process of classifying and authenticating to Wi-Fi hotspot networks. This programming guide is a companion to Apple’s _[NEHotspotHelper Class Reference](https://developer.apple.com/documentation/networkextension/nehotspothelper)_, which describes the Hotspot Helper API.

A Hotspot Helper application receives commands to be processed and provides a response to a command after it has been processed. In most instances, application command processing occurs while the application is running in the background.

The application receives commands to process as part of two main functions: authentication and scan list filtering. These functions and their recommended implementations are described in the following sections:

- [Authentication State Machine](Authentication%20State%20Machine.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzzfvbuqmrnknltc)
- [Scan List Filtering](Hotspot%20Network%20Scan%20List%20Filtering.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzzfvbuqmznknltc)
- [Hotspot Helper Command Handling Details](Hotspot%20Helper%20Command%20Handling%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzzfvbuqnbnknltc)
- [Important Guidelines](Important%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzzfvbuqnjnknltc)

[Next](Authentication%20State%20Machine.md)

