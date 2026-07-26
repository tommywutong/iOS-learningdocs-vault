---
title: GKPlayerAuthenticationDidChangeNotificationName
framework: GameKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamekit/gkplayerauthenticationdidchangenotificationname
source_url: 'https://developer.apple.com/documentation/gamekit/gkplayerauthenticationdidchangenotificationname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamekit/gkplayerauthenticationdidchangenotificationname.json'
content_hash: 'sha256:2300c229b31904f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [GameKit](../gamekit.md)

# GKPlayerAuthenticationDidChangeNotificationName

<sub>Global Variable</sub>

A notification that posts after GameKit initializes the local player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSNotificationName GKPlayerAuthenticationDidChangeNotificationName;
```

## Discussion

The object property for this notification is a `GKLocalPlayer` object. Passing `nil` provides standard Notification Center behavior, which is to receive the notification for any object.

## See Also

### Players

- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md) — Give players the ability to connect and interact with friends in your game.
- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md) — Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [Protecting the player’s privacy using scoped identifiers](protecting-the-player-s-privacy-using-scoped-identifiers.md) — Use the scoped identifiers that GameKit provides you as player IDs when transmitting or saving player data.
- [GKLocalPlayer](gklocalplayer.md) — The local player who signs in to Game Center on the device running the game.
- [GKPlayer](gkplayer.md) — A remote player who the local player running your game can invite and communicate with through Game Center.
- [GKBasePlayer](gkbaseplayer.md) — A class that provides common data and methods for the different player objects.
- [GKLocalPlayerListener](gklocalplayerlistener.md) — A protocol that handles events for Game Center players.
- [GKPlayerDidChangeNotificationName](gkplayerdidchangenotificationname.md) — A notification that posts when a player object’s data changes.
