---
title: Game Center Programming Guide
apple_id: TP40008304
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameCenter
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/GameKit_Guide/SavedGames/SavedGames.html
archived_at: '2026-07-15T08:18:48.730260Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Programming Guide](About%20Game%20Center.md)


[Next](Matchmaking%20Overview.md)[Previous](Leaderboards%2C%20Achievements%2C%20and%20Challenges.md)

# Saving A Game

Saving and sharing game data between iOS devices can be difficult. Current iCloud strategies do not provide developers with a good solution to saving game data between devices. Whether requiring developers to implement several different APIs or limiting the amount of information they can save, current iCloud strategies do not provide developers with a viable solution. To provide saved game data between devices, developers need to create their own solutions, either using their own servers or using a secondary service, such as Facebook. Using the new saved game methods found in [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame), [GKLocalPlayer](https://developer.apple.com/documentation/gamekit/gklocalplayer), and [GKSavedGameListener](https://developer.apple.com/documentation/gamekit/gksavedgamelistener) classes, developers can easily save game data to iCloud.

Currently, the saved game API is best used for single-player games or a pass-and-play game on a single device. Only the local player is required to save the game and any device can be used to retrieve the saved game information. Turn-based games already have a saved state as the turn is passed from one player to another and real-time games require all players to be present any time the game is played and only a single player can save the game.

When implementing saved games in your app, you must keep the following information in mind:

- The player must have an iCloud account to save games
- No specific limit on the amount of data that can be saved
- Game won’t be saved if there is no room in the player’s iCloud account
- The app controls how and what data is saved
- Saved games are tied to the iCloud account, not the Game Center account

Table 5-1 shows the common properties used by a [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame) object.

__Table 5-1__  Common saved game properties

| Property | Description |
| [deviceName](https://developer.apple.com/documentation/gamekit/gksavedgame/1520629-devicename) | The name of the device that created the saved game file. |
| [modificationDate](https://developer.apple.com/documentation/gamekit/gksavedgame/1520829-modificationdate) | The date the saved game file was last modified. |
| [name](https://developer.apple.com/documentation/gamekit/gksavedgame/1520819-name) | The name of the saved game file. |

Saving games using the saved game APIs requires the user to have an iCloud account. Using iCloud provides users with a way to save a game from any device that has an Internet connection. Along with providing the ability to save games from anywhere, iCloud provides users with the ability to save large data files. The size of a saved game file is limited to the amount of space in the users iCloud account. However, you should always strive to minimize the amount of data being saved. This prevents the user from running out of space and decreases the amount of time required to fetch or save a game file.

Today’s games are played on multiple devices depending on where the user happens to be. Whether they are at home playing on their iMac, sitting in front of a television with their iPad, or on a bus with their iPhone, a player wants to continue playing a game from the last place they left off and not have to worry about which device they were playing on. Including the ability to save and retrieve saved games greatly increases the playability of your game.

It is up to you to decide how and when users can save a game. If you want your player’s to consider each action before performing that action, then you might want to only allow a single saved game file. However, if you don’t mind your players going back and trying different actions, then allow the player to name and create several different saved game files. In either case, it is up to you to create a save game mechanism for your app.

After the player creates a new saved game file, use the [saveGameData:withName:completionHandler:](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520527-savegamedata) method to save the game data to iCloud. If there is already a saved game object with the same name, the new saved game data overwrites the old saved game data. Otherwise a new [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame) object is created and saved.

Players want to continue to play games they have saved, whether they saved the game on their current device or another device. To retrieve the list of games the player has saved from a device, your app calls the [fetchSavedGamesWithCompletionHandler:](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521086-fetchsavedgameswithcompletionhan) method to retrieve the list of games for the player. This method returns a list of [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame) objects that contains the identifying information for each saved game. Before presenting the list of saved games to the player, you must ensure that none of the saved games have the same name. If more than one saved game has the same name, you must resolve the name conflict before you present the list of saved games to the player.

After you have resolved any conflicts, present the list of saved games to the player, if applicable. The player then selects the saved game file they wish to continue playing. Call the [loadDataWithCompletionHandler:](https://developer.apple.com/documentation/gamekit/gksavedgame/1520754-loaddatawithcompletionhandler) method to retrieve the data associated with the [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame) object chosen by the player.

With users having multiple devices, it is not unusual for a player to be playing the same game on different devices at the same time. Because of this, it is possible to have multiple saved games with the same name and from different devices. It is up to your app to find any conflicting games and fix the conflict.

After determining that there is a conflict between saved games, you need to create an array containing only the [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame) objects for the conflicting games. You then send the array to the [resolveConflictingSavedGames:withData:completionHandler:](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521116-resolveconflictingsavedgames) method. This method resolves any saved game conflicts and modifies the array so that it does not contain any saved game conflicts.

[Next](Matchmaking%20Overview.md)[Previous](Leaderboards%2C%20Achievements%2C%20and%20Challenges.md)

