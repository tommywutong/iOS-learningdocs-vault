---
title: Game Controller Programming Guide
apple_id: TP40013276
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: GameController
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/ServicesDiscovery/Conceptual/GameControllerPG/Appendix/Appendix.html
archived_at: '2026-07-18T02:06:48.594049Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Game Controller Programming Guide](About%20Game%20Controllers.md)


[Next](Document%20Revision%20History.md)[Previous](Controlling%20Input%20on%20tvOS.md)

# Checklist for Adding Controllers

This appendix summarizes the critical issues described in this document by providing two checklists, one for iOS and one for Mac.

|  |  |
| --- | --- |
| ../Art/checkbox_unchecked_2x.png | Your game must not require a game controller. |
| ../Art/checkbox_unchecked_2x.png | Your game must be playable using a standalone controller, without access to the device. |
| ../Art/checkbox_unchecked_2x.png | Your game must support the pause notification. It should toggle between pausing and resuming your game. |
| ../Art/checkbox_unchecked_2x.png | Your game must disable the screen idle timer if the touchscreen is not used in your gameplay. See the [idleTimerDisabled](https://developer.apple.com/documentation/uikit/uiapplication/1623070-idletimerdisabled) property for more information. |
| ../Art/checkbox_unchecked_2x.png | When the iOS device is placed inside a formfitting controller, your game must run only in landscape mode. |
| ../Art/checkbox_unchecked_2x.png | Your game must hide any virtual controls while it is being controlled from a controller. |
| ../Art/checkbox_unchecked_2x.png | After a controller is connected, set the player index to a reasonable value. |

|  |  |
| --- | --- |
| ../Art/checkbox_unchecked_2x.png | Provide a user interface that explains which control elements are used by your game. Use the standard names for control elements. |
| ../Art/checkbox_unchecked_2x.png | Respond appropriately when a controller is connected or disconnected. |
| ../Art/checkbox_unchecked_2x.png | Make a control layout that is easy for players to understand and operate. |
| ../Art/checkbox_unchecked_2x.png | Remove any code from your app that compensates for thumbstick dead zones. |
| ../Art/checkbox_unchecked_2x.png | When using button elements, use the [pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed) property to determine whether a button is pressed. Use the [value](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522580-value) analog property only if your gameplay relies on the pressure applied to the button. |

|  |  |
| --- | --- |
| ../Art/checkbox_unchecked_2x.png | Your game must support the Siri Remote or an MFi Game Controller. (It may support both.) |
| ../Art/checkbox_unchecked_2x.png | Your game must support the pause notification. It should toggle between pausing and resuming your game. When your gameplay is inactive, you should ignore inputs in the Game Controller framework so that this button is processed appropriately by UIKit. |
| ../Art/checkbox_unchecked_2x.png | Your game must disable the screen idle timer if a controller’s input is being used directly. See the [idleTimerDisabled](https://developer.apple.com/documentation/uikit/uiapplication/1623070-idletimerdisabled) property for more information. |

|  |  |
| --- | --- |
| ../Art/checkbox_unchecked_2x.png | Provide a user interface that explains which control elements are used by your game. Use the standard names for control elements. |
| ../Art/checkbox_unchecked_2x.png | After a controller is connected, set the player index to a reasonable value. |
| ../Art/checkbox_unchecked_2x.png | Respond appropriately when a controller is connected or disconnected. |
| ../Art/checkbox_unchecked_2x.png | Make a control layout that is easy for players to understand and operate. |
| ../Art/checkbox_unchecked_2x.png | Remove any code from your app that compensates for thumbstick dead zones. |
| ../Art/checkbox_unchecked_2x.png | When using button elements, use the [pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed) property to determine whether a button is pressed. Use the [value](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522580-value) analog property only if your gameplay relies on the pressure applied to the button. |

|  |  |
| --- | --- |
| ../Art/checkbox_unchecked_2x.png | Your game must not require a game controller. |
| ../Art/checkbox_unchecked_2x.png | Your game must be playable using a standalone controller, without access to the Mac. |
| ../Art/checkbox_unchecked_2x.png | Your game must support the pause notification. It should toggle between pausing and resuming your game. |
| ../Art/checkbox_unchecked_2x.png | After a controller is connected, set the player index to a reasonable value. |

|  |  |
| --- | --- |
| ../Art/checkbox_unchecked_2x.png | Provide a user interface that explains which control elements are used by your game. Use the standard names for control elements. |
| ../Art/checkbox_unchecked_2x.png | Respond appropriately when a controller is connected or disconnected. |
| ../Art/checkbox_unchecked_2x.png | Make a control layout that is easy for players to understand and operate. |
| ../Art/checkbox_unchecked_2x.png | Remove any code from your app that compensates for thumbstick dead zones. |
| ../Art/checkbox_unchecked_2x.png | When using button elements, use the [pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed) property to determine whether a button is pressed. Use the [value](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522580-value) analog property only if your gameplay relies on the pressure applied to the button. |

[Next](Document%20Revision%20History.md)[Previous](Controlling%20Input%20on%20tvOS.md)

