---
title: Game Center Programming Guide
apple_id: TP40008304
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameCenter
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/GameKit_Guide/CreatingaHostedMatch/CreatingaHostedMatch.html
archived_at: '2026-07-15T08:18:38.219388Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Programming Guide](About%20Game%20Center.md)


[Next](Turn-Based%20Matches.md)[Previous](Real-Time%20Matches.md)

# Hosted Matches

Hosted matches allow your game to use Game Center’s matchmaking service to find players, but use your own server to connect the players to each other. Hosted matches require you to implement your own custom low-level networking code, because Game Center’s servers are not involved in the match play at all. However, hosted games offer larger match sizes and the ability to add your own server into every match.

The code you write for hosted matchmaking is similar to the code you write for real-time matches. Before you attempt to create a game that uses hosted matches, you should already be familiar with real-time matchmaking. The critical difference between the two models is that hosted matchmaking returns player identifiers instead of a completed match object. Your game then connects that player to your own server. Your server must match that player’s network address to the player identifier and, similar to a match, perform routing when one device in the match needs to communicate with others.

Table 8-1 lists the most common methods for real-time matchmaking and the corresponding methods or implementation details for hosted matchmaking.

__Table 8-1__  Methods to implement hosted matchmaking

| Real-time matchmaking | Hosted matchmaking |
| Your view controller delegate implements the [matchmakerViewController:didFindMatch:](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492416-matchmakerviewcontroller) method to receive the match. | Your delegate implements the [matchmakerViewController:hostedPlayerDidAccept:](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492412-matchmakerviewcontroller) method to receive a notification that a player has accepted an invitation to join the match. |
| Your programmatic matchmaking code calls [findMatchForRequest:withCompletionHandler:](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520777-findmatch) to create a new match. | Your programmatic code calls [findPlayersForHostedRequest:withCompletionHandler:](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520973-findplayersforhostedrequest) to find a set of new players for a match. |
| Your programmatic code calls [addPlayersToMatch:matchRequest:completionHandler:](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520561-addplayerstomatch) to add players to a match. | Your programmatic code calls [findPlayersForHostedRequest:withCompletionHandler:](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520973-findplayersforhostedrequest) to find a set of new players for a match. Because you implement your own match architecture, you need to decide when you make this call whether or not you are adding the players to an existing hosted match. |
| Your game receives an invitation. | The [GKInvite](https://developer.apple.com/documentation/gamekit/gkinvite) object’s [hosted](https://developer.apple.com/documentation/gamekit/gkinvite/1520458-hosted) property tells you whether the match is a hosted match. Typically, this matters only if your game implements both hosted and nonhosted matches. |

By default, when you perform the matchmaking process, Game Kit returns an instance of the [GKMatch](https://developer.apple.com/documentation/gamekit/gkmatch) object on each device connected to the match. Each device then uses its match object to communicate with other participants. For most games, this default behavior is exactly what you want. The `GKMatch` class abstracts the underlying network topology so that your game can simply focus on sending data to other participants without you having to worry about how the data is transmitted.

However, some games may want to support more players than the maximum number of supported players on Game Center, or may want their own server to arbitrate the match. In these cases, you can still use matchmaking to find players for a _hosted match_. A hosted match does not use `GKMatch` objects. Instead, each copy of your game receives the player identifiers for all of the players in the match. Your game then takes additional steps to connect the players to your server.

Creating a hosted match requires your game to implement all of the low-level networking required for your game. In particular, you must do all of the following in your game:

- Design and implement your own networking code to connect each device to your server.
- Design and implement your own networking protocol to inform other devices of the state of any participant in the match.
- Design and implement your own server implementation to map player identifiers to the specific device connected to your server. Thus, your server becomes responsible for routing network data between players.
- If your game uses Game Kit’s standard matchmaking user interface, you must make sure each device informs Game Kit after it connects to your server. This information allows Game Kit to update its user interface.

Create and configure a new match request and then initializes a new [GKMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller) object using the match request. The presenting view controller makes itself the matchmaking view controller’s delegate and then presents the matchmaking interface over itself. The player interacts with the matchmaking screen until the match is ready to start or an error occurs.

When the view controller is hosted, your delegate implements the [matchmakerViewController:hostedPlayerDidAccept:](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492412-matchmakerviewcontroller) method to process the new player. Your delegate needs to behave differently depending on which device your game is running on:

- When called on the player’s device, the device needs to connect to your own server. When successfully connected, call the [setHostedPlayer:connected:](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492418-sethostedplayer) method to tell the view controller that the player has connected to the match.
- When called on another player’s device, your game needs to determine that it can talk to the new player’s device through your server. Once it knows it can send messages to the other client, call the [setHostedPlayer:connected:](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492418-sethostedplayer) method to update the user interface.

After all invitees have accepted your app’s match request, you send the information about the players to the server, and then send a start-game message to all of the invitees. When invitees receive the start-game message, they must manually close the view controller for their app.

[Next](Turn-Based%20Matches.md)[Previous](Real-Time%20Matches.md)

