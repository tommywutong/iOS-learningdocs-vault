---
title: Game Controller Programming Guide
apple_id: TP40013276
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameController
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/ServicesDiscovery/Conceptual/GameControllerPG/ControllingInputontvOS/ControllingInputontvOS.html
archived_at: '2026-07-18T02:06:48.936923Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Game Controller Programming Guide](About%20Game%20Controllers.md)


[Next](Checklist%20for%20Adding%20Controllers.md)[Previous](Working%20with%20Controller%20Elements.md)

# Controlling Input on tvOS

Users can connect game controllers to Apple TV just as they do with iOS devices. When a game controller is connected to an Apple TV, the controller can also be used to navigate the user interface. Low-level controller inputs are automatically turned into higher-level events that are delivered through the responder chain. If your app relies solely on UIKit and focus interactions, you don’t need to do any work to support Game Controllers. Whether or not a user is using an Siri Remote or a game controller is transparently handled for you by tvOS.

There are a couple of significant changes to the Game Controller framework on Apple TV:

- A micro gamepad controller profile ([GCMicroGamepad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad)) specifically targets the capabilities of the Siri Remote.
- A view controller class ([GCEventViewController](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller)) can be used to control how controller and remote inputs are routed through your app.

A maximum of four game controllers (plus one Siri Remote) can be connected to an Apple TV at any given time. Your game designs should keep these limitations in mind.

The Siri Remote can act as a micro gamepad, and is great for games that require simple or motion based input. As with other controllers, it shows up in the Game Controller framework as a [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller) object. The remote supports both the [GCMotion](https://developer.apple.com/documentation/gamecontroller/gcmotion) and the [GCMicroGamepad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad) profiles. The micro gamepad profile is supported only by the Siri Remote; to support other game controllers, you must also implement the extended gamepad profile.

The controller has the following characteristics:

- The touchpad on the remote can be used as a D-pad. The D-pad provides analog input data.
- The remote can be used in either a portrait or landscape orientation. When you create your app, you decide whether the profile object flips the input data automatically when the user changes the remote orientation.
- The touchpad is available as a digital button (button A), by firmly pressing on the touchpad.
- The Play/Pause button on the remote is a digital button (button X).
- The Menu button on the remote is used to pause gameplay, calling the controller object’s pause handler.
- Although the remote supports motion data (and the `GCMotion` profile), the remote cannot determine the attitude or rotation of the remote. The corresponding properties always return constant values.

The default behavior in UIKIt on tvOS is to process all low-level controller inputs and deliver high-level events to the responder chain. Low-level game controller inputs are not available by default, because all of the events are processed by UIKit. When you want to read controller input directly, you need to turn off UIKit’s behavior. Controller input destination shows the two input paths.

__Figure 4-1__  Controller input destination

!

For example, a common design for many games is to have one view that displays a main menu of options, and a second view that presents gameplay. The main menu could be implemented using UIKit elements so that its behavior is consistent with focus behavior. When the gameplay view is presented, you would use the Game Controller framework to turn off the UIKit behavior controller input process in order to directly read the controller input.

If you plan to use the Game Controller framework to read low-level inputs, you need to use [GCEventViewController](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller) (or a subclass) to display your game content. By default, whenever the `GCEventViewController` object’s view or a subview is the first responder, then game controller input is captured by the view controller and delivered to your app through the Game Controller framework. Events are not delivered to UIKit. When a view that is not in the view controller’s hierarchy is the first responder, then events are processed normally by UIKit.

Once you have a `GCEventViewController`object in your responder chain, you can also use its [controllerUserInteractionEnabled](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller/1627773-controlleruserinteractionenabled) property to toggle where events are sent. For example, if your game mixes UIKit content on menu screens with Metal content as part of the game view, then when the game is paused, you would change the value of the [controllerUserInteractionEnabled](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller/1627773-controlleruserinteractionenabled) property to enable UIKit interaction. In this case, one of your menu items needs to be a button that resumes gameplay, because your controller’s pause handler will no longer be called. When this menu item is selected, you would switch the event handling back to game controllers and resume your game.

If for some reason you cannot use a `GCEventViewController` object to control how events are propagated, you can implement this behavior yourself in your game. To do this, override the [pressesBegan:withEvent:](https://developer.apple.com/documentation/uikit/uiresponder/1621134-pressesbegan) method (as well as the other event handlers for press events) in your view or view controller. If you want a particular event to be delivered to UIKit, call the super class’s implementation of the method. If you want it to only be processed by the game controller framework, do not call the superclass.

[Next](Checklist%20for%20Adding%20Controllers.md)[Previous](Working%20with%20Controller%20Elements.md)

