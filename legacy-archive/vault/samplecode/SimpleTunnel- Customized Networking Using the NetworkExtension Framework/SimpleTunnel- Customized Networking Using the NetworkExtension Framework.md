---
title: 'SimpleTunnel: Customized Networking Using the NetworkExtension Framework'
apple_id: TP40016140
resource_type: Sample Code
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleTunnel/Introduction/Intro.html
archived_at: '2026-07-18T03:24:22.682591Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](tunnelserver-main.swift.md)

# SimpleTunnel: Customized Networking Using the NetworkExtension Framework

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2016-10-04 Updated to Swift 3 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbqfvjgk5tjonuw63sinfzxi33spewui33oorggs3tlivwgk3lfnz2esrc7ge) |
| __Build Requirements:__ | Xcode 8.0, iOS 9.0 SDK, OS X 10.11 SDK |
| __Runtime Requirements:__ | iOS 9.0, OS X 10.11 |

The Network Extension framework exposes APIs that give you the ability to customize the networking features of iOS and OS X. This sample project demonstrates how to:

- Use the NEPacketTunnelProvider class to implement a custom VPN tunneling protocol.
- Use the NETunnelProviderManager class to create and manage VPN configurations that use the custom VPN tunneling protocol.
- Use the NEAppProxyProvider class to implement a custom transparent network proxy protocol.
- Use the NEAppProxyProviderManager class to manage VPN configurations that use the transparent network proxy protocol.
- Use the NEFilterControlProvider and NEFilterDataProvider classes to implement a custom on-device content filtering service.
- Use the NEFilterManager class to configure the custom filtering service.

[Next](tunnelserver-main.swift.md)

