---
title: GameKit updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/gamekit
source_url: 'https://developer.apple.com/documentation/updates/gamekit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/gamekit.json'
content_hash: 'sha256:56d0a5b921668f86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# GameKit updates

<sub>Article</sub>

Learn about important changes to GameKit.

## Overview

Browse notable changes in [GameKit](../gamekit.md).

## June 2025

- Use a GameKit Configuration file in Xcode to configure Game Activities and Challenges.
- Test leaderboard score submissions by receiving system notifications when they happen. On iOS, open Settings \> Developer, then turn on Notify About Score Submissions.
- Use [GKGameActivity](../gamekit/gkgameactivity.md) to present players with ways to engage each other in your game.
- Configure challenges in Xcode or App Store Connect and use  [GKChallengeDefinition](../gamekit/gkchallengedefinition.md) to retrieve the metadata you define.

## June 2024

### Dashboard

- Create a [GKGameCenterViewController](../gamekit/gkgamecenterviewcontroller.md) object using the [init(leaderboardSetID:)](<../gamekit/gkgamecenterviewcontroller/init(leaderboardsetid_).md>) initializer to display a set of leaderboards in the dashboard.
- Use the [init(player:)](<../gamekit/gkgamecenterviewcontroller/init(player_).md>) initializer to display a player’s profile in the dashboard.

### Voice chat

- Use SharePlay to allow voice chat in your real-time games instead of [GKVoiceChat](../gamekit/gkvoicechat.md) which is deprecated. When you present a [GKMatchmakerViewController](../gamekit/gkmatchmakerviewcontroller.md) object, it automatically shows a SharePlay button on iOS. To implement a custom SharePlay experience, see [GKMatchmaker](../gamekit/gkmatchmaker.md#4110693).

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
