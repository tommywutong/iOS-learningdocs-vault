---
title: Accessibility updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/accessibility
source_url: 'https://developer.apple.com/documentation/updates/accessibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/accessibility.json'
content_hash: 'sha256:fd3aef46d0f9672f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# Accessibility updates

<sub>Article</sub>

Learn about important changes to Accessibility.

## Overview

Browse notable changes in [Accessibility](../accessibility.md).

## June 2025

- Add [Accessibility Nutrition Labels](../accessibility.md#Add-Accessibility-Nutrition-Labels-to-your-product-page) to your App Store product page to indicate which accessibility features your app supports.
- Support Assistive Access in iOS and iPadOS scenes with [AssistiveAccess](../swiftui/assistiveaccess.md).
- Use [AXBrailleTranslator](../accessibility/axbrailletranslator.md) to translate print text to Braille and Braille to print text according to a given Braille table.
- Use [openSettings(for:)](<../accessibility/accessibilitysettings/opensettings(for_).md>) to open the Settings app to new sections of Accessibility settings, including [AccessibilitySettings.Feature.assistiveTouch](../accessibility/accessibilitysettings/feature/assistivetouch.md), [AccessibilitySettings.Feature.assistiveTouchDevices](../accessibility/accessibilitysettings/feature/assistivetouchdevices.md), and  [AccessibilitySettings.Feature.dwellControl](../accessibility/accessibilitysettings/feature/dwellcontrol.md).

## June 2024

### General

- Enhance music with tactile feedback for people who are deaf or hard of hearing by playing Apple-generated haptic tracks along with music tracks. Add the [MusicHapticsSupported](../bundleresources/information-property-list/musichapticssupported.md) `Info.plist` key to notify the system that your app supports the Music Haptics feature. Specify which song is playing using the [MPNowPlayingInfoPropertyInternationalStandardRecordingCode](../mediaplayer/mpnowplayinginfopropertyinternationalstandardrecordingcode.md). Music Haptics uses the International Standard Recording Code (ISRC) to choose the correct Music Haptics track to play at the same time. Observe and respond to the status of the haptic track playback using [MAMusicHapticsManager](../mediaaccessibility/mamusichapticsmanager.md).
- Open the Settings app to a specific section of Accessibility settings using [openSettings(for:)](<../accessibility/accessibilitysettings/opensettings(for_).md>).
- Support people’s preference to reduce the blinking animation of the text insertion indicator for custom cursor implementations. Check the value of the preference with [prefersNonBlinkingTextInsertionIndicator](../accessibility/accessibilitysettings/prefersnonblinkingtextinsertionindicator.md), and observe when people change that preference with [prefersNonBlinkingTextInsertionIndicatorDidChangeNotification](../accessibility/accessibilitysettings/prefersnonblinkingtextinsertionindicatordidchangenotification.md).
- Check if a device uses Assistive Access with [isAssistiveAccessEnabled](../accessibility/accessibilitysettings/isassistiveaccessenabled.md) if you need to remove workflows or UI elements that aren’t appropriate in the context of Assistive Access.

### SwiftUI

- Specify that your accessibility element behaves as a tab bar using the [isTabBar](../swiftui/accessibilitytraits/istabbar.md) accessibility trait with the [accessibilityAddTraits(_:)](<../swiftui/view/accessibilityaddtraits(__).md>) modifier. In UIKit, use [tabBar](../uikit/uiaccessibilitytraits/tabbar.md).
- Enhance how you structure accessibility labels by appending custom content using [accessibilityLabel(content:)](<../swiftui/view/accessibilitylabel(content_).md>).
- Generate a localized description of a color in a string interpolation by adding `accessibilityName:`, such as `"\(accessibilityName: myColor)"`. Pass that string to any accessibility modifier.

## June 2023

- Provide a great experience for your app in Assistive Access, an accessibility feature that tailors the iOS and iPadOS experience for people with cognitive disabilities. Adopt [UISupportsFullScreenInAssistiveAccess](../bundleresources/information-property-list/uisupportsfullscreeninassistiveaccess.md) to allow your app’s UI to expand into all the available space above the Back button in Assistive Access.
- Personalize your app with Personal Voice, a new feature that lets people record and recreate their voice directly on their iOS and macOS devices. Personal voices appear alongside system voices and are available for Live Speech, a type-to-speak feature that lets a person synthesize speech on the fly. Request access to synthesize speech with personal voices using a new request authorization API in [AVSpeechSynthesizer](../avfaudio/avspeechsynthesizer.md).
- Detect and mitigate sequences of flashing effects in your video content when the Dim Flashing Lights setting is on. If your app performs custom video drawing instead of using AVFoundation APIs, implement this behavior using [MAFlashingLightsProcessor](../mediaaccessibility/maflashinglightsprocessor.md).
- Pause animated images in your app when a person turns off the Animated Images setting on their device. Check the value of this setting using [accessibilityPlayAnimatedImages](../swiftui/environmentvalues/accessibilityplayanimatedimages.md).
- Send announcement, layout change, screen change, and page scroll accessibility notifications with greater ease in multiplatform apps using the new Swift type [AccessibilityNotification](../accessibility/accessibilitynotification.md). Make sure people receive the most important information first by specifying a default, low, or high priority for announcements.
- Enhance custom accessibility elements by specifying the combination of traits and behaviors that best characterizes the element. Add the new trait [isToggle](../swiftui/accessibilitytraits/istoggle.md) to controls that toggle on and off, and the new action [accessibilityZoomAction(_:)](<../swiftui/view/accessibilityzoomaction(__).md>) to content that can zoom in and out.
- Configure new direct touch options through [accessibilityDirectTouch(_:options:)](<../swiftui/view/accessibilitydirecttouch(__options_).md>) to provide the best experience for elements that support direct touch interactions in your app. Specify the [silentOnTouch](../swiftui/accessibilitydirecttouchoptions/silentontouch.md) option to ensure VoiceOver is silent when a person interacts with the direct touch area so your app can provide its own audio feedback. Specify the [requiresActivation](../swiftui/accessibilitydirecttouchoptions/requiresactivation.md) option to make the direct touch area require VoiceOver to activate the element before touch passthrough happens.
- Simplify how you maintain your UIKit accessibility code with block-based setters for accessibility attributes.
- Ensure robust testing of your app’s accessibility experience by performing accessibility audits using [XCUIApplication](../xctest/xcuiapplication.md).
- Assign automation elements to expose certain UI elements specifically for the purpose of automation without affecting the accessibility of those elements.

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
- [Background Tasks updates](backgroundtasks.md) — Learn about important changes in Background Tasks.
