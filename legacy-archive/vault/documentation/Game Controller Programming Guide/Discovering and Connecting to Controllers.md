---
title: Game Controller Programming Guide
apple_id: TP40013276
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameController
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/ServicesDiscovery/Conceptual/GameControllerPG/DiscoveringControllers/DiscoveringControllers.html
archived_at: '2026-07-18T02:06:49.551535Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Game Controller Programming Guide](About%20Game%20Controllers.md)


[Next](Working%20with%20Controller%20Elements.md)[Previous](Incorporating%20Controllers%20into%20Your%20Game.md)

# Discovering and Connecting to Controllers

In your game, a physical controller is represented by a [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller) object. When a controller is connected, an object is automatically created by the Game Controller framework. You then use this object to configure the controller and read its inputs.

In this chapter, you:

- Learn how to help a user discover an unpaired wireless controller
- Obtain [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller) objects for connected controllers
- Configure a connected controller

A wireless controller must be discovered before it can be connected to an iOS device, Apple TV, or Mac. The discovery process is triggered on both the controller and the device, and the two are allowed to connect to each other. After discovery is complete, the devices are paired and the controller is connected. A new controller is discovered only once. After that, if the device and the controller are both turned on simultaneously, they automatically find and connect to each other.

Normally, discovery occurs outside your game—that is, a player usually pairs the controller before launching your game. However, you can let a player discover new controllers from within your game.

The discovery process follows these steps:

1. To start discovering new controllers, call the [startWirelessControllerDiscoveryWithCompletionHandler:](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458879-startwirelesscontrollerdiscovery) class method, passing in a completion handler. New controllers are automatically discovered and paired with the device.
2. The discovery process eventually stops after some time has passed, but to end it early, you can call the [stopWirelessControllerDiscovery](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458854-stopwirelesscontrollerdiscovery) class method.
3. After the discovery process ends, the Game Controller framework calls your completion handler.

Here are some useful guidelines to consider when implementing support for discovery:

- __Design and display an appropriate interface to the user.__ There is no built-in user interface displayed when in discovery mode. The framework manages only the discovery process. You might provide a button in your user interface to start the process and change it to a cancel button while the discovery process is active.
- __Pause active gameplay until the discovery process completes.__The discovery process may take a long time to complete, and the player may be unable to interact with your game while pairing the controller.

After your app has finished launching, the operating system automatically creates a list of connected controllers. Call the [controllers](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458871-controllers) class method to retrieve an array of [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller) objects for all connected controllers. Next, use these objects to configure the controllers or read the controller’s inputs. If there are no connected controllers or you call this method while your app is launching, the array will be empty.

After the initial list of controllers is populated, the Game Controller framework posts notifications when a controller is connected ([GCControllerDidConnectNotification](https://developer.apple.com/documentation/gamecontroller/gccontrollerdidconnectnotification)) or disconnected ([GCControllerDidDisconnectNotification](https://developer.apple.com/documentation/gamecontroller/gccontrollerdiddisconnectnotification)). Your game should almost always register for both notifications to provide a proper user experience. The notification object’s [object](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) property holds the [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller) object for the controller whose status has just changed.

Because the number of controllers may vary, you need the appropriate behavior for your game. Here are some guidelines:

- If no controllers are connected, use your standard user interface to control your game.
- If a single controller is connected, _always_ use it.
- If multiple controllers are connected and one of them is a formfitting controller, make it the default controller. If all of the connected controllers are standalone, provide a way for players to select a controller.
- If multiple controllers are connected and your game supports multiple players, assign a controller to each player.

Typically, you want to maintain a strong reference to controller objects for connected controllers used by your game. Use these objects to perform controller-related tasks. For example, you often need to:

- Get information about the controller, such as whether or not it is a formfitting controller
- Configure a player index on the controller so that you can associate it with a specific player
- Assign a block to a controller object’s [controllerPausedHandler](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458852-controllerpausedhandler) property
- Read the controller object’s profile properties to obtain controller input; see Working with Controller Elements

Some of these tasks are introduced here. For specific details, see _[GCController Class Reference](https://developer.apple.com/documentation/gamecontroller/gccontroller)_.

A player index associates a controller with a specific player. Whenever your game uses a particular controller, you must set the [playerIndex](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458885-playerindex) property to reflect which player is using that controller. For example, in a game between two players, both using controllers, you would set one controller to [GCControllerPlayerIndex1](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index1) and the other to [GCControllerPlayerIndex2](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/gccontrollerplayerindex2). When you set the player index, it causes a matching LED on the controller to light up. Similarly, if your game stops using a particular controller, it should set the index to [GCControllerPlayerIndexUnset](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/indexunset). This value guarantees that the LEDs on the controller are not lit.

[Next](Working%20with%20Controller%20Elements.md)[Previous](Incorporating%20Controllers%20into%20Your%20Game.md)

