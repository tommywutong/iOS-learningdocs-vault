---
title: Game Center Programming Guide
apple_id: TP40008304
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameCenter
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/GameKit_Guide/DisplayingGameCenterUserInterfaceElements/DisplayingGameCenterUserInterfaceElements.html
archived_at: '2026-07-15T08:18:38.230928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Game Center Programming Guide](About%20Game%20Center.md)


[Next](Working%20with%20Players%20in%20Game%20Center.md)[Previous](Developing%20a%20Game%20Center-Aware%20Game.md)

# Displaying Game Center User Interface Elements

Game Center provides two distinct types of user interface elements for you to use in your game. The first type is intended to be displayed modally by your game, covering your own game’s user interface and temporarily interrupting the normal flow of your game. Typically these user interface screens allow a player to interact with content loaded from Game Center or to perform Game Center tasks. When the player finishes interacting with one of these screens of content, your game shows the next appropriate screen, either by returning to one of your game screens or by advancing to another screenful of content.

In iOS, a fullscreen user interface is packaged as a view controller, and follows the standard conventions of view controllers on the system. One of your game’s view controllers is expected to present these view controllers when needed, and later respond when the view controller is dismissed. On OS X, a special class provided by Game Kit provides a similar infrastructure so that your game can present the user interface.

The second type of user interface element is a banner that is displayed for a short time to the player. Afterwards, the banner automatically disappears from the screen. While players can interact with some banners, usually banners are simply used to display a message to the player. Game Center displays many banners on behalf of your game, but you can also present your own banners to the player if your game has information you need to display.

The convention used by Game Kit is for one of your view controllers to present the Game Kit view controller. Your view controller acts as a delegate to the view controller it presents so that the view controller can be informed when the player is finished looking at the presented screen. The Game Center view controller displays many different pieces of Game Center content, so most games should offer a button that brings the player to this screen, even if the game also shows Game Center content using a custom user interface. To present a Game Kit view controller you create a new instance of a [GKGameCenterViewController](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller), set its delegate and display the desired information.

In most cases, your game would pause gameplay or other real-time behavior when displaying one of these standard user interface classes. When the view controller is later dismissed, it can resume these activities.

In OS X, view controllers do not play the same role as they do in iOS. In many cases, some other object responsible for your user interface displays the Game Center control. It does this through the use of the [GKDialogController](https://developer.apple.com/documentation/gamekit/gkdialogcontroller) class. This class presents the user interface in a window provided by your game.

You create and populate your Game Center view controller in the same way as in iOS. However, after creating the Game Center view controller, you then create a GKDialogController instance. The Game Center view controller is associated with the GKDialogController using the [presentViewController:](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1520909-present) method.

Creating a banner in your game is accomplished using the [GKNotificationBanner](https://developer.apple.com/documentation/gamekit/gknotificationbanner) class. You create a title and message for the banner and send this information to [showBannerWithTitle:message:completionHandler:](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515370-showbannerwithtitle). If you want to change the amount of time that the banner is displayed, use the [showBannerWithTitle:message:duration:completionHandler:](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515368-showbannerwithtitle) method.

[Next](Working%20with%20Players%20in%20Game%20Center.md)[Previous](Developing%20a%20Game%20Center-Aware%20Game.md)

