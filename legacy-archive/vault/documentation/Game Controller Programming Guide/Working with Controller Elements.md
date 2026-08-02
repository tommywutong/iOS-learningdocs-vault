---
title: Game Controller Programming Guide
apple_id: TP40013276
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameController
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/ServicesDiscovery/Conceptual/GameControllerPG/ReadingControllerInputs/ReadingControllerInputs.html
archived_at: '2026-07-18T02:06:51.562748Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Game Controller Programming Guide](About%20Game%20Controllers.md)


[Next](Controlling%20Input%20on%20tvOS.md)[Previous](Discovering%20and%20Connecting%20to%20Controllers.md)

# Working with Controller Elements

After your game has discovered a controller, you need to map its controls to different actions within your game. The Game Controller framework makes it easy to map these controls, regardless of what kind of controller is connected. In this chapter, you will learn about:

- The role that profiles play in mapping physical control hardware to functions in your game
- Different strategies for using the controls on a controller

A _controller profile_ promises a specific, logical arrangement of controls, or _elements_. A game controller can support more than one profile. If a game controller supports a profile, this means that every control promised by the profile is present in the physical controller. When you implement your game, you choose which profiles to support and then read the appropriate elements on those profiles to receive input data. The Game Controller framework then maps the actual physical control data to the elements of the logical profile.

A controller profile is implemented as a class in the Game Controller framework. Table 3-1 lists the available profiles and the corresponding property on the `GCController` class.

__Table 3-1__  Game controller profiles

| Profile | Implementation class | GCController property |
| Extended Gamepad (extended control layout) | [GCExtendedGamepad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad) | [extendedGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458883-extendedgamepad) |
| Micro Gamepad (Siri Remote) | [GCMicroGamepad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad) | [microGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1627772-microgamepad) |

To determine whether a controller supports a profile, read the property that matches the profile on the controller’s `GCController` object. If the value is `nil`, the controller does not support that profile. Otherwise, the returned profile object is used to access the control elements.

You can read multiple profiles on the same controller simultaneously. If you do, be aware that the same hardware control may be mapped to logical elements in multiple profiles.

The different kinds of elements are represented by classes in the Game Controller framework. All controller elements are derived from the [GCControllerElement](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement) class, which implements common behaviors. Each profile class exposes one or more properties that represent the control values. Table 3-2 lists the available element types and the classes that implement them.

__Table 3-2__  Game controller element types

| Element type | Implementation class | Element value |
| Button | [GCControllerButtonInput](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput) | A floating point number between `0` and `1`. Alternatively, can be read as a Boolean value that states whether the button is pressed. |
| Axis | [GCControllerAxisInput](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput) | A floating point number between `-1` and `1`. |
| Directional pad (D-pad) | [GCControllerDirectionPad](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad) | Read as either two axes or four directional buttons. |

As the player manipulates the physical controller, the controller’s hardware inputs are sent to the Game Controller framework. Next, the hardware signals are normalized and a consistent value is computed for each physical control. Then, all elements in the profiles supported by the controller are updated to match the new values.

When designing your game, you can use one of the following strategies to read the profile’s input elements:

- In your game loop, poll the values of the elements you are interested in. Reading an input directly works best for elements, such as directional pads, which need to be read every frame. See [Reading an Element’s Values Directly](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenzwfvbuqmznknltcma).
- Register a block to be called when values change. You can choose to register a block for a single element or for all of the elements in the profile. Callbacks work best when you need to guarantee that a change is always detected. See [Registering to be Called When an Element Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenzwfvbuqmznknltcmi).
- Use snapshots to save the current control state. Because all of a profile’s controls are read simultaneously and saved to the snapshot, you can use this state at a later point in time.

Many games use a rendering loop to organize their game design. Each time through the loop, the game processes state changes, artificial intelligence, and player input. One common, simple strategy is to poll the elements you are interested in each time through the game loop.

Listing 3-1 shows a possible implementation of this concept. This method is intended to be called each time a frame is processed. For example, if your game is built with Sprite Kit, you might poll the element information from inside a scene’s [update:](https://developer.apple.com/documentation/spritekit/skscene/1519802-update) method. Listing 3-1 reads three elements on the extended gamepad profile. The thumbstick is used to control a spaceship’s thrust, and the two triggers are used to fire lasers or to launch missiles.

__Listing 3-1__  Polling the elements of a profile

```objc
- (void) readControlInputs
{
    GCExtendedGamepad *profile = self.myController.extendedGamepad;
    if (profile.rightTrigger.isPressed)
        [self fireLasers];
    if (profile.leftTrigger.isPressed)
        [self launchMissile];
    [self applyThrust: profile.leftThumbstick.yAxis.value];
}
```

In this example, the [pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed) property is used for the weapons, but the value property is used for the ship’s thrust. The weapons can only be in one of two states: firing or not firing. However, the ship’s thrust is calculated based on how far the player moves the thumbstick, so the [value](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500224-value) property must be used instead.

In some games, it is better to be called at the exact moment when an element changes. For example, you might want to ensure that a button press is always detected, even if the press occurs between frames. To implement this, you register a change handler. The Game Controller framework processes and updates profiles on the main thread. Whenever it updates an element’s value in the profile, any handlers for that element are called. A handler can be registered on the profile object or a specific element in the profile. When the handler is created on the profile object, it is called whenever any element on the profile changes. If multiple values on the profile change simultaneously, the handler is called once for each element that changed. If the handler is registered on an element, the handler is called whenever that element or any of that element’s children are updated.

Listing 3-2 implements a handler on the profile object. In this example, the code checks the two triggers to determine whether either was pressed.

__Listing 3-2__  Registering a value handler for a profile

```
GCExtendedGamepad *profile = self.myController.extendedGamepad;
profile.valueChangedHandler = ^(GCExtendedGamepad *gamepad, GCControllerElement *element)
    {
        if ((gamepad.rightTrigger == element) && gamepad.rightTrigger.isPressed)
            [self fireLasers];
        if ((gamepad.leftTrigger == element) && gamepad.leftTrigger.isPressed)
            [self launchMissile];
    };
```

Alternatively, this code could have been written with separate handlers for each button. Listing 3-3 shows how to implement separate handler elements for the left and right triggers.

__Listing 3-3__  Registering separate value handlers for profile elements

```
GCExtendedGamepad *profile = self.myController.extendedGamepad;
profile.rightTrigger.valueChangedHandler = ^(GCControllerButtonInput *button, float value, BOOL pressed)
    {
        if (pressed)
            [self fireLasers];
    };
profile.leftTrigger.valueChangedHandler = ^(GCControllerButtonInput *button, float value, BOOL pressed)
    {
        if (pressed)
            [self launchMissile];
    };
```


A _snapshot_ is a special kind of profile object that holds values for all of the elements in a profile at the moment when the snapshot was recorded. You can then read and use these control values at your leisure. Potential uses for a snapshot include:

- Reading the inputs in one thread and then transferring them to another thread for processing.
- Transmitting controller inputs over a network.
- Saving controller data to a file. You might do this to capture a gameplay session for an instant replay feature or for debugging purposes.

There is one snapshot class for each profile class. Each kind of snapshot is implemented as a subclass of the profile class that represents the profile being saved. To create a new snapshot, call the profile object’s [saveSnapshot](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497415-savesnapshot) method. Because the snapshot object is also a profile object, read its values as you would with the regular profile object. You can often use the same code you’ve already written to process controller inputs and use it on snapshots instead.

To flatten a snapshot into a binary file that you can send over a network or save to disk, you read the snapshot’s [snapshotData](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493928-snapshotdata) property. If you have previously saved a data object, you can read its data in one of two ways:

- Allocate a new snapshot object for the class used to create the binary data, and initialize it with the [initWithSnapshotData:](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493933-init) method.
- Assign the `NSData` object to an existing snapshot object’s `snapshotData` property. When you do this, all of the elements in the snapshot are updated, and any handlers assigned to the snapshot object are called.

Here are some guidelines for the button and thumbstick element types.

When reading a button element, you can either determine whether the button is pressed or measure how much pressure is applied to the button. If you care only whether the button is pressed, always use the [pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed) property. The Game Controller framework automatically uses a heuristic to determine whether the button is pressed. Use the [value](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522580-value) property only when you need to know the actual pressure being applied to the button. When measuring pressure, keep in mind that it takes a minimum amount of pressure before the button recognizes that pressure is being applied. This means that the first nonzero value returned by the button element may be larger than expected. After the button exceeds this threshold, it continues to measure nonzero values until it is completely released.

In the past, thumbstick controls on controllers have been problematic, requiring additional work in game code to compensate for the thumbstick’s dead zone or control values that exceeded the tolerances of the device. If you are porting code from another platform, you should disable this code when bringing your code to iOS or OS X. The Game Controller framework automatically performs these calculations for you.

[Next](Controlling%20Input%20on%20tvOS.md)[Previous](Discovering%20and%20Connecting%20to%20Controllers.md)

