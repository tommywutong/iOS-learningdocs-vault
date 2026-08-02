---
title: Verifying App Accessibility on iOS
apple_id: TP40012619
resource_type: Guide
platform: iOS
topic: User Experience
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/technotes/TestingAccessibilityOfiOSApps/TestAccessibilityonYourDevicewithVoiceOver/TestAccessibilityonYourDevicewithVoiceOver.html
archived_at: '2026-07-27T06:57:08.751292Z'
---
> 导航：[总目录](../../README.md) · [technotes](../../_indexes/technotes.md) · [Verifying App Accessibility on iOS](About%20Accessibility%20Verification%20on%20iOS.md)



# Test Accessibility on Your Device with VoiceOver

It’s a good idea to test your app using VoiceOver, because you can experience the app in the same way that VoiceOver users will experience it. Using VoiceOver to run your app can expose problem areas—for example, confusing labels, unhelpful hints, and unreachable elements—that make your app less accessible.

_VoiceOver_ is a sophisticated technology that provides many powerful features to users with disabilities. Although you don’t need to become an expert VoiceOver user to test your app with it, you do need to know a handful of basic gestures. This chapter describes how to activate VoiceOver and use it to run your app.

## First Steps

Go to Settings > General > Accessibility > VoiceOver and tap the switch control to turn VoiceOver on, as shown in Figure 1-1. If you provide hints for any accessible elements in your app, check to make sure the Speak Hints switch is on (it is on by default). Before leaving VoiceOver settings, make sure the Speaking Rate slider is adjusted to an appropriate value.

__Figure 1-1__  Enable VoiceOver in Settings

（原归档配图获取待重试：`voiceover_settings.png`）

__Note:__ Alternatively, you can turn on VoiceOver using the triple-click Home button setting, as described in [Quickly Toggle VoiceOver by Triple-Clicking the Home Button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdmmjzfvbuqmznknltk).

After you’ve turned VoiceOver on, you’ll notice that many familiar gestures have different effects. For example, a single tap causes VoiceOver to speak the selected item and a double tap activates the selected item. When an element is selected, VoiceOver draws a black rounded rectangle around it, which is called the _VoiceOver cursor_. VoiceOver users are confident navigating the interface because the VoiceOver cursor prevents them from triggering something unintentionally.

A complete list of VoiceOver gestures are detailed in Table 1-1.

__Table 1-1__  VoiceOver gestures are different from standard gestures

| VoiceOver gesture | Action |
| __Drag over the screen__ | Select and speak each item as you touch it. |
| __One-finger tap__ | Speak the selected item. |
| __One-finger swipe right or left__ | Select the next or previous item. The order of elements is determined by their screen coordinates in a left-to-right, top-to-bottom fashion. To override this order, group accessible elements together with the [shouldGroupAccessibilityChildren](https://developer.apple.com/documentation/objectivec/nsobject/1615143-shouldgroupaccessibilitychildren) property. |
| __One-finger swipe up or down__ | This gesture performs different actions depending on the context:   - On an adjustable element, such as a slider, increment or decrement the value. Adjustable elements implement the [UIAccessibilityTraitAdjustable](https://developer.apple.com/documentation/uikit/uiaccessibilitytraitadjustable) trait. - In a text view, move the insertion point backwards or forwards. |
| __One-finger double tap__ | This gesture performs one of the following:   - Activate the selected item. - Toggle the selected switch. - Unlock the lock screen when the Unlock switch is selected. |
| __Split-tap__—Touch and hold an element, then tap anywhere on the screen with another finger. | Combine the selection and activation gesture into one. Once familiar, this gesture is quick to input, especially when typing. |
| __One-finger double press__—With one finger, perform a double tap. During the second tap, continue to hold your finger against the screen. | Drag an item. |
| __Two-finger tap__ | Pause reading. Two-finger tap again to resume reading. |
| __Two-finger double tap__—Also called a Magic Tap. | Start and stop the current action. For example, a Magic Tap starts or pauses the stopwatch in the Clock app, and answers or hangs up a call in the Phone app. Not all views implement the Magic Tap; you must opt in to achieve this functionality. See [Responding to Special VoiceOver Gestures](../../featuredarticles/View%20Controller%20Programming%20Guide%20for%20iOS/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmrnknltk) for more information. |
| __Two-finger scrub__—A Z-shaped gesture, also called an Escape. | Go back hierarchically. For example, an Escape traverses up, or pops, the navigation stack in a navigation controller. Not all views implement the Escape; you must opt in to achieve this functionality. See [Responding to Special VoiceOver Gestures](../../featuredarticles/View%20Controller%20Programming%20Guide%20for%20iOS/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmrnknltk) for more information. |
| __Two-finger swipe up__ | Read all accessible items from the top of the screen. |
| __Two-finger swipe down__ | Read all accessible items from the current position. |
| __Two-finger pinch open__ | Select text. |
| __Two-finger pinch close__ | Deselect text. |
| __Three-finger swipe up or down__ | Scroll a list or area of the screen. |
| __Three-finger swipe right or left__ | Navigate to the next or previous page. |
| __Three-finger double tap__—If zoom is enabled, this becomes a three-finger triple tap. | Toggle speech. VoiceOver sound icons, or audio feedback, still play if the device is not muted. |
| __Three-finger triple tap__—If zoom is enabled, this becomes a three-finger quadruple tap. | Toggle Screen Curtain. See [Emulate the VoiceOver Experience with the Screen Curtain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdmmjzfvbuqmznknltcmi). |
| __Four-finger tap at top or bottom of screen__ | Select the first or last accessible element on the screen. |

![tip icon](attachments/Resources/1282/Images/tips_2x.png)

__Tip:__ A great place to practice VoiceOver gestures is in the VoiceOver Practice area found in Settings > General > Accessibility > VoiceOver. VoiceOver needs to be enabled for the VoiceOver Practice button to appear.

While testing your app, ensure that interactive controls and important pieces of information can be accessed by the VoiceOver cursor. UI decoration is irrelevant to the VoiceOver user, and need not be accessible.

__Important:__ To avoid your interface from sounding robotic, make an effort to sculpt the prose of your accessibility descriptions. For guidelines on crafting accessibility labels and hints, see [Supply Accurate and Helpful Attribute Information](../../documentation/User%20Experience/Accessibility%20Programming%20Guide%20for%20iOS/Making%20Your%20iOS%20App%20Accessible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobvfvbuqmjqgiwvgvzu).

## VoiceOver Tips and Tricks

This section contains special VoiceOver shortcuts and gestures that can help you operate and master VoiceOver. With these tips, you can quickly change VoiceOver settings, jump to a certain element when many are presented onscreen, and use iOS from the perception of someone with a visual impairment.

### Quickly Toggle VoiceOver by Triple-Clicking the Home Button

You can toggle VoiceOver on and off quickly by setting it to the triple-click setting in Settings > General > Accessibility > Triple-Click, as shown in Figure 1-2. Then, by triple-clicking the Home button, you can toggle VoiceOver on or off. This is much quicker than navigating back to the Settings app every time you want to enable or disable VoiceOver, speeding up accessibility testing significantly while making it easy to disable VoiceOver when you’re not sure which gesture to use.

__Figure 1-2__  Set the triple-click Home button setting to VoiceOver

（原归档配图获取待重试：`tripleclick_2x.png`）

### Fine-Tune Speech Granularity with the VoiceOver Rotor

You can break down the speech of VoiceOver to a per-word and even per-character basis by using the VoiceOver rotor, as shown in Figure 1-3. Rotate two fingers in a clockwise or counter-clockwise motion, as if turning a dial, to cycle through rotor options. After an option is selected, swipe up or down with one finger to progress to the previous or next value as indicated by the rotor option.

__Figure 1-3__  Use the VoiceOver rotor to speak text word by word

（原归档配图获取待重试：`rotor_2x.png`）

You can also add options to the rotor in Settings > General > Accessibility > VoiceOver > Rotor. For example, you can add the Speech Rate option to dynamically adjust the speaking rate from anywhere in iOS by swiping up or down. Rotor options are contextually sensitive and may not appear in all environments.

### Scroll Faster with the Item Chooser

The Item Chooser can help you quickly select the element you’re looking for, particularly when there are a great number of elements in a view. With two fingers, triple-tap the screen to bring up the Item Chooser, as shown in Figure 1-4. Then, select the indexed list on the right and flick up or down to progress to the previous or next letter, respectively. This approach is useful for jumping to a particular point in a table view that doesn’t have an indexed list. The Item Chooser is also useful for searching items onscreen when there is no search field present, and for sorting an unordered list alphabetically. Dismiss the Item Chooser by performing the Escape command—a two-finger Z-shaped gesture.

__Figure 1-4__  The Item Chooser

（原归档配图获取待重试：`accessibility_item_chooser_2x.png`）

## Emulate the VoiceOver Experience with the Screen Curtain

To simulate the experience a visually impaired user might have with your app, you can run it with the VoiceOver _screen curtain_ in place. When you activate the screen curtain, VoiceOver turns off the device display so that no one can read. Testing with the display turned off obliges you to rely on the information VoiceOver speaks and removes the temptation to use your app as a sighted user would. To turn off the display while you use VoiceOver, triple-tap the screen with three fingers. To turn the display back on, perform the same gesture again.

__Note:__ If zoom is enabled, the screen curtain gesture becomes a three-finger quadruple tap.
