---
title: XPC updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/updates/xpc
source_url: 'https://developer.apple.com/documentation/updates/xpc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/xpc.json'
content_hash: 'sha256:1c3a2d26e864568a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# XPC updates

<sub>Article</sub>

Learn about important changes to XPC.

## Overview

Browse notable changes in [XPC](https://developer.apple.com/documentation/xpc).

## March 2024

### Security

- Test whether the peer executable that communicates with your app over an XPC connection has an expected entitlement by calling [xpc_connection_set_peer_entitlement_exists_requirement(_:_:)](<../xpc/xpc_connection_set_peer_entitlement_exists_requirement(____).md>), and whether it has a specific value for an entitlement by calling [xpc_connection_set_peer_entitlement_matches_value_requirement(_:_:_:)](<../xpc/xpc_connection_set_peer_entitlement_matches_value_requirement(______).md>).
- Test whether the peer executable that communicates with your app over an XPC connection is an Apple platform binary with a given signing identifier by calling [xpc_connection_set_peer_platform_identity_requirement(_:_:)](<../xpc/xpc_connection_set_peer_platform_identity_requirement(____).md>).
- Test whether your Apple Developer team signed the peer executable that communicates with your app over an XPC connection by calling [xpc_connection_set_peer_team_identity_requirement(_:_:)](<../xpc/xpc_connection_set_peer_team_identity_requirement(____).md>).
- Test whether the peer executable that communicates with your app over an XPC connection satisfies a lightweight code requirement by calling [xpc_connection_set_peer_lightweight_code_requirement(_:_:)](<../xpc/xpc_connection_set_peer_lightweight_code_requirement(____).md>).

## June 2023

- Create XPC services using native Swift syntax. Use [XPCListener](../xpc/xpclistener.md) to create an XPC server that listens for messages from other processes. Use [XPCSession](../xpc/xpcsession.md) to create clients that connect to servers and exchange messages.
- For C and Objective-C projects, use the corresponding [xpc_listener_t](../xpc/xpc_listener_t.md) and [xpc_session_t](../xpc/xpc_session_t-10if0.md) APIs.
- In Xcode, use the updated XPC services target template to choose whether you want to use the high-level [NSXPCConnection](../foundation/nsxpcconnection.md) or the low-level `libXPC` APIs.

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
