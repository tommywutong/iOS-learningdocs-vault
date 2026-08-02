---
title: Verifying App Accessibility on iOS
apple_id: TP40012619
resource_type: Guide
platform: iOS
topic: User Experience
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/technotes/TestingAccessibilityOfiOSApps/TestingtheAccessibilityofiOSApps/TestingtheAccessibilityofiOSApps.html
archived_at: '2026-07-27T06:57:08.738995Z'
---
> 导航：[总目录](../../README.md) · [technotes](../../_indexes/technotes.md)



# About Accessibility Verification on iOS

By now, you’ve made your app [accessible](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Accessibility.html#//apple_ref/doc/uid/TP40008195-CH66). But how can you be sure? You can test the accessibility by interacting with your app using the same screen-reading technology as the visually impaired. In this way, you replicate the accessible experience. You may even think of accessibility enhancements when you experience accessibility for yourself. You’ve already done the work, now see for yourself what the experience is like.

Continue reading to learn how to verify that your accessibility enhancements work as intended.

## At a Glance

You can test for accessibility on a physical device and in iOS Simulator.

### Learn How to Use VoiceOver

iOS ships with a screen-reading technology called _VoiceOver_. VoiceOver changes the way taps and swipes are interpreted by the system in order to augment usability for those who cannot see. Because VoiceOver lets you control your device in ways you’re not used to, learning how to use it may seem daunting. But all it takes is the right gestures and a few usability tips.

__Relevant Chapter:__ [Test Accessibility on Your Device with VoiceOver](Test%20Accessibility%20on%20Your%20Device%20with%20VoiceOver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdmmjzfvbuqmznknltc)

### Learn How to Use Accessibility Inspector

A handy tool called Accessibility Inspector can help you debug a flawed accessibility implementation. Accessibility Inspector runs on your Mac inside iOS Simulator. After you enable the inspector, you can see the available information VoiceOver leverages.

__Relevant Chapter:__ [Debug Accessibility in iOS Simulator with the Accessibility Inspector](Debug%20Accessibility%20in%20iOS%20Simulator%20with%20the%20Accessibility%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdmmjzfvbuqnbnknltc)

## Prerequisites

This article assumes that you’ve already attempted to make your app accessible, as explained in the following documents:

- _[Accessibility Programming Guide for iOS](../../documentation/User%20Experience/Accessibility%20Programming%20Guide%20for%20iOS/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobv)_—Describes how custom views can enhance accessibility.
- [Supporting Accessibility](../../featuredarticles/View%20Controller%20Programming%20Guide%20for%20iOS/SupportingAccessibility.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmjs) in _[View Controller Programming Guide for iOS](../../featuredarticles/View%20Controller%20Programming%20Guide%20for%20iOS/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjx)_—Describes the view controller’s role of making an app accessible.

## See Also

_[HelloGoodbye: Using the Accessibility API to Widen Your User Base](../../samplecode/HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base/HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkojt)_—Download the sample code project to see an accessible implementation in action.
