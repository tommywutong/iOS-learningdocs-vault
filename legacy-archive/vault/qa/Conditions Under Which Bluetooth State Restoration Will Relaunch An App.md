---
title: Conditions Under Which Bluetooth State Restoration Will Relaunch An App
apple_id: DTS40017678
resource_type: QA
platform: iOS
topic: null
technology: CoreBluetooth
published: '2017-09-08'
source_url: https://developer.apple.com/library/archive/qa/qa1962/_index.html
archived_at: '2026-07-18T02:38:00.788787Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1962

# Conditions Under Which Bluetooth State Restoration Will Relaunch An App

## Q:  What are the conditions that iOS 11 Bluetooth State Restoration will relaunch my app?

A: Bluetooth State Restoration will relaunch your app in the background for pending Core Bluetooth requests.

With iOS 11, Bluetooth State Restoration will relaunch your app under more circumstances than before. There are, though, certain conditions where the system will not relaunch your app regardless of pending requests.

Because of system state and user actions, it is possible that your app may not be restored in response to a Bluetooth event. Therefore it is important to educate your users so that they understand how their actions effect your app.

Well designed apps will be resilient under such conditions.

__Table 1__  Conditions for Bluetooth State Restoration to relaunch your app

| App/Device state | Will the app will be relaunched | Notes | iOS 10 behavior |
| App suspended in memory | N/A | App will be activated without needing a relaunch | Same |
| App removed from memory | YES |  | YES |
| App crashed | YES |  | YES |
| App Force Quit by the user | NO |  | NO |
| Bluetooth power toggled | NO | Users may toggle Bluetooth power either through Settings, or via Airplane mode | NO |
| Airplane Mode toggled | YES (only if Bluetooth power is not toggled with Airplane Mode) | Users may configure the Airplane Mode switch to not toggle Bluetooth power | NO |
| Device restarted | YES (see notes) | If the device requires a passcode to unlock, apps will not be relaunched until the device is unlocked for the first time after a restart | NO |

Also, it is important to keep in mind that the app will be relaunched and restored __if and only if__ it is pending on a specific Bluetooth event or action (like scanning, connecting, or a subscribed notification characteristic), and this event has occurred.

For more information on Bluetooth State Preservation and Restoration refer to [State Preservation and Restoration](https://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothBackgroundProcessingForIOSApps/PerformingTasksWhileYourAppIsInTheBackground.html#//apple_ref/doc/uid/TP40013257-CH7-SW10) in [Core Bluetooth Programming Guide](https://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257-CH1-SW1)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-09-08 | New document that lists the conditions under which Bluetooth State Restoration will relaunch your app |

