---
title: Game Center Programming Guide
apple_id: TP40008304
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameCenter
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/GameKit_Guide/Users/Users.html
archived_at: '2026-07-15T08:18:48.739021Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Programming Guide](About%20Game%20Center.md)


[Next](Leaderboards%2C%20Achievements%2C%20and%20Challenges.md)[Previous](Displaying%20Game%20Center%20User%20Interface%20Elements.md)

# Working with Players in Game Center

Players are a critical part in any game that supports Game Center, because all Game Center features are related to the players. As a game developer, you need to understand some of the infrastructure that Game Center uses to support player accounts and how you implement it in your app. After reading this chapter, you will understand how to manage player information in your game. In particular, you’ll learn:

- How a game identifies different players on Game Center
- How a player logs themselves into Game Center and how your game knows whether a player is logged into a device it is running on
- How to retrieve details about particular players from Game Center
- How to implement support in your game so that a player can invite other players to become friends on Game Center

To take advantage of Game Center’s features, a user creates a Game Center account that identifies to identify themselves as a specific user. That user is known as a _player_ on Game Center. The Game Center service keeps track of critical account information for that player, such as who that player is, what games that player has played, what the player has accomplished in each game, and who that player’s friends are. Some of this information is directly available to your game; typically this is information specifically related to the game and general information about the player.

When a player wants to access Game Center on a particular device, the player signs in, or _authenticates_ on that device. A player authenticates their account by launching the Game Center app or by launching any game that implements Game Center support. In either case, the player is presented with an interface to provide their account name and password. Once authenticated, the player is associated with that device persistently until they explicitly sign out of Game Center in the Game Center app. Only one player is allowed to be authenticated on a device at a time; for a new player to be authenticated on the device, the existing authenticated player must sign out first.

Game Center is intended to be a social experience. Game Center allows a player to invite other players to be friends. When two players are friends, they can see each other’s status in the Game Center app, compare scores, and invite each other into matches more easily. Through Game Kit, your game can also access some information about the authenticated player’s friends or allow the player to invite players to become friends. For example, you can use this functionality to allow a player to send a friend invitation to a player they just met in a match played within your game.

Every player account is uniquely identified by a player identifier string contained within a GKPlayer object. The identifier string is created when the player’s account is first created and never changes, even if other information in the account changes. Thus, player identifiers are the only reliable way to track a particular player. For this reason, the Game Kit API uses player identifiers wherever a specific player needs to be identified. If Game Center needs to identify a specific player in your game, the Game Kit API returns that player’s identifier. Your game uses a player identifier to retrieve information from Game Center about that player.

In addition to using player identifiers in your interactions with Game Center, your game should also use the player identifier whenever it wants to store data locally about a specific player. For example, if your game stores data to track a player’s progress (such as on the device, on your own server, or on iCloud), use player identifiers to distinguish between multiple players playing on the same device. That way, if a different player signs into the device, you can immediately personalize the experience by showing content specific to that player.

When you design your game, you’ll find that your game is often aware of multiple players at the same time. For example, if you design a game using multiplayer networking, then you have information—and a player identifier—for each player in the match. However, on any particular device, one player always takes precedence over other players. The _local player_ is the player that is currently authenticated to play on that device. In Figure 3-1, two players are connected in a network match. On the left device, Bob is the local player and Mary is a remote player. On the right device, Mary is the local player and Bob is a remote player.

__Figure 3-1__  Local and remote players

!

Almost all classes in Game Kit that send data to or retrieve information from Game Center expect the device to have an authenticated local player. The work those classes do is always on behalf of the local player. For example, if your game reports scores to a leaderboard, it can only report a score earned by the local player. As such, before using any Game Center features, your game must first authenticate that there is a local player on the device. Game Kit returns an error to your game if it attempts to perform Game Center-related tasks that require an authenticated player when one isn’t available on the device.

When your game needs details for a particular player, it retrieves those details by making a query to Game Center using the player’s player identifier. Game Kit returns those details to your game in a [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer) object. Table 3-1 lists some of the more interesting properties on a player object.

__Table 3-1__  Important Player Object Properties

| Property | Description |
| [playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid) | A string that holds the player identifier string used to retrieve this player information. |
| [displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname) | A user-readable string you can display for this player in your own user interface. For example, in a network match, you might show the display names for each player in the match so that everyone knows who they are playing against. |

The `GKLocalPlayer` class is a special subclass of the [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer) class, and includes additional properties specific to the local player:

- The [authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated) property states whether the local player has been authencticated.
- The [underage](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515394-underage) property states whether this player is underage.

__Table 3-2__  Local Player Object Properties

| Property | Description |
| [authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated) | A Boolean value that states whether the local player has been authenticated and is logged into Game Center. If a player is not authenticated, certain Game Center capabilities are not available. |
| [underage](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515394-underage) | A Boolean value that states whether the local player is underage. Some Game Center features are disabled when the value of this property is `YES`; Game Center returns a [GKErrorUnderage](https://developer.apple.com/documentation/gamekit/gkerror/code/underage) error if you try to use those features. Your game can also use this property to decide whether it should disable some of its own features for an underage player. |

In addition to the display name for a given player, if the player has provided a photo, you can download that player’s photo to your game and use it in your game’s user interface.

Your game should start to authenticate the player as early as possible after launching, even before you present the user interface. Authentication is an asynchronous process and won’t slow down the loading of your title screen. Waiting until after the title screen is presented before authenticating the user only increases the delay until the player can play your game. The main reason you need to authenticate the player as early as possible is so that iOS can launch your game specifically to handle events that the player is interested in. For example, if your game supports turn-based matches, it might be launched because the player has already tapped a notification banner. Thus, you need to authenticate early so that your game can retrieve and process the Game Center event.

When your game authenticates a player, Game Kit first checks to see whether there is already an authenticated player on the device. Because a player stays authenticated until they explicitly sign out of Game Center, it is quite common that an authenticated player is already on the device. In this situation, a banner is briefly shown to let the player know that authentication succeeded, and then your game is immediately notified.

If there is not currently an authenticated player on the device, then an authentication dialog needs to be displayed so that the player can sign in with an existing account or create a new Game Center account. This is important, because it means that supporting authentication also means transparently supporting account creation.

To authenticate the local player, your game is handed a view controller to display at a time of your choosing. Typically, this means your game can cleanly pause its own animations and other features before displaying the view controller. This mechanism allows you to create a better user experience for the player.

To authenticate the local player, you create your own method that sets the authenticateHandler property. The method retrieves the [shared instance](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Singleton.html#//apple_ref/doc/uid/TP40008195-CH49) of the [GKLocalPlayer](https://developer.apple.com/documentation/gamekit/gklocalplayer) class and then sets that object’s [authenticateHandler](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515399-authenticatehandler) property to point to a [block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) that handles authentication events. Once you set an authentication handler, Game Kit automatically authenticates the player asynchronously, calling your authentication handler as necessary to complete the process. Each time your game moves from the background to the foreground, Game Kit automatically authenticates the local player again. See the [authenticateHandler](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515399-authenticatehandler) property for an example of how to create this method.

Always check the [authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated) property on the local player object to determine whether Game Kit was able to authenticate a local player. Do not rely on the error received by your game to determine whether an authenticated player is available on the device. Even when an error is returned to your game, Game Kit may have sufficient cached information to provide an authenticated player to your game. Also, it is not necessary for your game to display errors to the player when authentication fails; Game Kit already displays important errors to the player on your behalf. Most authentication errors are returned to your game primarily to assist you with debugging.

Once the player has been successfully authenticated, your game can read other properties on the local player object to determine the player’s display name and other attributes. You can also use other classes that access Game Center. In most cases, your game should immediately enable other code related to Game Center. For example, here are some common tasks that most games perform after successfully authenticating the local player:

- Read the [displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname) property to retrieve the local player’s name. Use this display name throughout your game when you want to refer to the player; do not prompt the player separately for their name.
- Add event handlers to receive events for Game Center features. For example, turn-based matches, real-time matches and challenges all require event handlers to process Game Center events. Because your game may have been launched specifically to receive a pending invitation; adding event handlers immediately after authenticating the player allows those events to be processed promptly.
- Retrieve the local player’s previous progress on achievements.
- Retrieve a list of player identifiers for the local player’s friends. This is a first step before loading more detailed information about those players.
- If your game stores its own custom information for a particular player (such as state variables indicating the player’s progress through your game), your completion handler might also load this data so that it can restore the player’s progress.

A game that supports both multitasking and Game Center must take additional steps when authenticating the local player. When your game is in the background, the status of the authenticated player may change, because the player may sign out or a new player may sign in. As such, you can never rely on the information staying the same when your game moves into the background,.

Here are some guidelines for authenticating the local player in a game that supports multitasking:

- Like other multitasking apps, your game should archive its state before moving into the background.
- As soon as your game moves to the background, the value of the local player object’s [authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated) property becomes and remains invalid until your game moves back to the foreground. You cannot read the value to determine if the player is still authenticated until Game Kit reauthenticates the player and calls your authentication handler. Your game must act as though there is not an authenticated player until your completion handler is called. Once your handler is called, value stored in the [authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated) property is valid again.
- If the value of the [authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated) property changed to `NO`, then there is no longer a local player authorized to access Game Center content. Your game must dispose of any Game Kit objects that were created using the previous local player.
- If the value of the [authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated) property is `YES`, then there is a local player authenticated on the device. However, a new player may have logged in. Your game should store the player identifier for the local player after it authenticates the player. Then, on future calls to your completion handler, compare the value of the local player object’s [playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid) property to the identifier stored by your game. If the identifier changed, then a new player has signed in. Your game should dispose of any objects associated with the previous player and then create or load the appropriate state for the new local player.

You may want to your game to reference the local player’s friends. For example, you might do this if you are implementing your own custom matchmaking or challenge interface and want to allow the player to pick and choose players from the friends list. Information about the local player’s friends is only loaded when you ask for it as this information can potentially be quite large and take awhile to send over the network. Use the [loadFriendPlayersWithCompletionHandler:](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515386-loadfriendplayers) method to retrieve information about the local player’s friends.

Retrieving details about the local player’s friends is a two-step process. First, your game loads the list of player identifiers for the local player’s friends. Then, as with any other player identifiers, your game calls Game Center to retrieve the details for those players.

Regardless of which Game Kit class returned player identifiers to your game, you retrieve detailed information about those players in the same way by calling the [loadPlayersForIdentifiers:withCompletionHandler:](https://developer.apple.com/documentation/gamekit/gkplayer/1520723-loadplayersforidentifiers) class method on the [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer) class. This Game Kit method takes two parameters. The first is an array of player identifiers for the players you are interested in. The second is a completion handler to be called after Game Kit retrieves the data from Game Center.

In addition to the information found in the player object, you can also attempt to load a photo for the player. Not all player objects have photos associated with them, so your code must be able to work without them. Use the [loadPhotoForSize:withCompletionHandler:](https://developer.apple.com/documentation/gamekit/gkplayer/1521176-loadphoto) method to import player photos. Note that there is not a property on the player object that stores the returned photo. You must write your own code to associate player photos with player objects.

The Game Center app allows players to send invitations to other players. Use the [GKFriendRequestComposeViewController](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller) class to allow a player to send friend requests. The friend request must be presented modally by a view controller that your game creates and can not be pushed onto a navigation controller. When the player dismisses the friend request, the delegate’s [friendRequestComposeViewControllerDidFinish:](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate/1437186-friendrequestcomposeviewcontroll) method is called.

[Next](Leaderboards%2C%20Achievements%2C%20and%20Challenges.md)[Previous](Displaying%20Game%20Center%20User%20Interface%20Elements.md)

