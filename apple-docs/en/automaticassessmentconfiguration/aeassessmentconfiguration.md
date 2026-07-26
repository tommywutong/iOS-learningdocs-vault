---
title: AEAssessmentConfiguration
framework: Automatic Assessment Configuration
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 14.0+, macOS 10.15.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/automaticassessmentconfiguration/aeassessmentconfiguration
source_url: 'https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automaticassessmentconfiguration/aeassessmentconfiguration.json'
content_hash: 'sha256:ea94ed9dc8ed13cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Automatic Assessment Configuration](../automaticassessmentconfiguration.md)

# AEAssessmentConfiguration

<sub>Class</sub>

Configuration information for an assessment session.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AEAssessmentConfiguration
```

## Overview

Create a configuration instance and pass it to the [- initWithConfiguration:](<aeassessmentsession/init(configuration_).md>) initializer of an [AEAssessmentSession](aeassessmentsession.md) instance to create a new assessment session. Before using the configuration, indicate which exceptions you want to allow for the assessment session’s restrictions by setting values on the configuration instance. For example, you can set values to allow dictation and certain aspects of autocorrect:

**Swift**

```swift
let config = AEAssessmentConfiguration()

#if os(iOS) // These exceptions available only on iOS and iPadOS.
config.allowsDictation = true
config.autocorrectMode = [.punctuation, .spelling]
#endif

let session = AEAssessmentSession(configuration: config)
```

**Objective-C**

```objc
AEAssessmentConfiguration *config = [AEAssessmentConfiguration new];

#if TARGET_OS_IPHONE || TARGET_IPHONE_SIMULATOR // These exceptions available only on iOS and iPadOS.
config.allowsDictation = YES;
config.autocorrectMode = AEAutocorrectModePunctuation | AEAutocorrectModeSpelling;
#endif

AEAssessmentSession *session = [[AEAssessmentSession alloc] initWithConfiguration:config];
```

While you provide a configuration instance when creating a session on iOS, iPadOS, and macOS, specific exceptions apply only to certain platforms. In particular, on macOS, you can selectively make specific apps besides your own available during an assessment — for example, to allow users to access a calculator or a dictionary. All other exceptions apply only to iOS and iPadOS.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Allowing access to other apps

- [- setConfiguration:forApplication:](<aeassessmentconfiguration/setconfiguration(__for_).md>) — Adds an app to the list of apps available during an assessment.
- [configurationsByApplication](aeassessmentconfiguration/configurationsbyapplication.md) — The collection of apps available during an assessment, along with their associated configurations.
- [- removeApplication:](<aeassessmentconfiguration/remove(__).md>) — Removes the availability of a previously allowed app.
- [mainParticipantConfiguration](aeassessmentconfiguration/mainparticipantconfiguration.md) — The app-specific configuration for the app that invokes the assessment.
- [AEAssessmentApplication](aeassessmentapplication.md) — A representation of an app that users can access during an assessment.
- [AEAssessmentParticipantConfiguration](aeassessmentparticipantconfiguration.md) — Configuration information for an app that’s available during an assessment.

### Allowing accessibility

- [allowsAccessibilitySpeech](aeassessmentconfiguration/allowsaccessibilityspeech.md) — A Boolean value that indicates whether to allow the speech-related accessibility features during an assessment. _(deprecated)_
- [allowsDictation](aeassessmentconfiguration/allowsdictation.md) — A Boolean value that indicates whether to allow the use of dictation during an assessment.

### Allowing typing assistance

- [allowsContinuousPathKeyboard](aeassessmentconfiguration/allowscontinuouspathkeyboard.md) — A Boolean value that indicates whether to allow Slide to Type to operate during an assessment.
- [allowsKeyboardShortcuts](aeassessmentconfiguration/allowskeyboardshortcuts.md) — A Boolean value that indicates whether to allow keyboard shortcuts during an assessment.
- [allowsPredictiveKeyboard](aeassessmentconfiguration/allowspredictivekeyboard.md) — A Boolean value that indicates whether to enable the predictive keyboard during an assessment.
- [allowsPasswordAutoFill](aeassessmentconfiguration/allowspasswordautofill.md) — A Boolean value that indicates whether to allow password autofill during an assessment.

### Allowing corrections

- [allowsSpellCheck](aeassessmentconfiguration/allowsspellcheck.md) — A Boolean value that indicates whether to allow spell check during an assessment.
- [autocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.property.md) — A Boolean value that indicates whether to allow Autocorrect during an assessment.
- [AutocorrectMode](aeassessmentconfiguration/autocorrectmode-swift.struct.md) — The set of autocorrect features that you can enable during an assessment.

### Allowing handoff

- [allowsActivityContinuation](aeassessmentconfiguration/allowsactivitycontinuation.md) — A Boolean value that indicates whether to allow Handoff during an assessment.

### Instance Properties

- [allowLockdownMode](aeassessmentconfiguration/allowlockdownmode.md) — A Boolean value that indicates whether the assessment allows Lockdown Mode to be active. _(beta)_
- [allowOnlyParticipantsToRun](aeassessmentconfiguration/allowonlyparticipantstorun.md) — A Boolean value that indicates whether only participant applications are allowed to run during an assessment. _(beta)_
- [allowPrivateRelay](aeassessmentconfiguration/allowprivaterelay.md) — A Boolean value that indicates whether the assessment allows iCloud Private Relay to be active. _(beta)_
- [allowedAppleMenuItems](aeassessmentconfiguration/allowedapplemenuitems.md) — The set of allowed Apple menu items during an assessment. _(beta)_
- [allowedDirectoriesAndFiles](aeassessmentconfiguration/alloweddirectoriesandfiles.md) — The set of allowed directories and files that participants can access during an assessment. _(beta)_
- [allowedMenuBarItems](aeassessmentconfiguration/allowedmenubaritems.md) — The set of menu bar items that should remain visible during an assessment. _(beta)_
- [allowsAccessibilityAlternativeInputMethods](aeassessmentconfiguration/allowsaccessibilityalternativeinputmethods.md) — A Boolean value that indicates whether to allow alternative input methods for accessibility features during an assessment. _(beta)_
- [allowsAccessibilityBackgroundSounds](aeassessmentconfiguration/allowsaccessibilitybackgroundsounds.md) — A Boolean value that indicates whether to allow Background Sounds during an assessment. _(beta)_
- [allowsAccessibilityFullKeyboardAccess](aeassessmentconfiguration/allowsaccessibilityfullkeyboardaccess.md) — A Boolean value that indicates whether to allow Full Keyboard Access during an assessment. _(beta)_
- [allowsAccessibilityHoverText](aeassessmentconfiguration/allowsaccessibilityhovertext.md) — A Boolean value that indicates whether to allow Hover Text during an assessment. _(beta)_
- [allowsAccessibilityKeyboard](aeassessmentconfiguration/allowsaccessibilitykeyboard.md) — A Boolean value that indicates whether to allow the Accessibility Keyboard during an assessment.
- [allowsAccessibilityLiveCaptions](aeassessmentconfiguration/allowsaccessibilitylivecaptions.md) — A Boolean value that indicates whether to allow Live Captions during an assessment.
- [allowsAccessibilityLiveSpeech](aeassessmentconfiguration/allowsaccessibilitylivespeech.md) — A Boolean value that indicates whether to allow Live Speech during an assessment. _(beta)_
- [allowsAccessibilityReader](aeassessmentconfiguration/allowsaccessibilityreader.md) — A Boolean value that indicates whether to allow the Accessibility Reader during an assessment.
- [allowsAccessibilitySpokenContent](aeassessmentconfiguration/allowsaccessibilityspokencontent.md) — A Boolean value that indicates whether to allow Spoken Content during an assessment. _(beta)_
- [allowsAccessibilitySwitchControl](aeassessmentconfiguration/allowsaccessibilityswitchcontrol.md) — A Boolean value that indicates whether to allow Switch Control during an assessment. _(beta)_
- [allowsAccessibilityTypingFeedback](aeassessmentconfiguration/allowsaccessibilitytypingfeedback.md) — A Boolean value that indicates whether to allow accessibility typing feedback during an assessment.
- [allowsAccessibilityVoiceControl](aeassessmentconfiguration/allowsaccessibilityvoicecontrol.md) — A Boolean value that indicates whether to allow Voice Control during an assessment. _(beta)_
- [allowsAccessibilityVoiceOver](aeassessmentconfiguration/allowsaccessibilityvoiceover.md) — A Boolean value that indicates whether to allow VoiceOver during an assessment. _(beta)_
- [allowsAccessibilityZoom](aeassessmentconfiguration/allowsaccessibilityzoom.md) — A Boolean value that indicates whether to allow Zoom during an assessment. _(beta)_
- [allowsAutoFill](aeassessmentconfiguration/allowsautofill.md) — A Boolean value that indicates whether to allow autofill during an assessment. _(beta)_
- [allowsDock](aeassessmentconfiguration/allowsdock.md) — A Boolean value that indicates whether to allow the Dock during an assessment. _(beta)_
- [allowsEmojiKeyboard](aeassessmentconfiguration/allowsemojikeyboard.md) — A Boolean value that indicates whether to allow the emoji keyboard during an assessment.
- [allowsMenuBar](aeassessmentconfiguration/allowsmenubar.md) — A Boolean value that indicates whether to allow the menu bar during an assessment. _(beta)_
- [allowsScreenshots](aeassessmentconfiguration/allowsscreenshots.md) — A Boolean value that indicates whether to allow screenshots copied to the clipboard during an assessment.
- [allowsStructuralInput](aeassessmentconfiguration/allowsstructuralinput.md) — A Boolean value that indicates whether to allow Chinese and Japanese structural input during an assessment. _(beta)_
- [allowsUserScriptExecution](aeassessmentconfiguration/allowsuserscriptexecution.md) — A Boolean value that indicates whether to allow user script execution during an assessment. _(beta)_
- [requiresManagedDevice](aeassessmentconfiguration/requiresmanageddevice.md) — A Boolean value that indicates whether the device must be managed to start an assessment. _(beta)_
- [requiresSIP](aeassessmentconfiguration/requiressip.md) — A Boolean value that indicates whether System Integrity Protection (SIP) must be enabled to start an assessment. _(beta)_
- [requiresSingleUser](aeassessmentconfiguration/requiressingleuser.md) — A Boolean value that indicates whether only a single user account must be logged in to start an assessment. _(beta)_
- [requiresUserAccountType](aeassessmentconfiguration/requiresuseraccounttype.md) — Specifies the type of user account required to start an assessment. _(beta)_

## See Also

### Sessions

- [Preparing an educational assessment app for distribution](preparing-an-educational-assessment-app-for-distribution.md) — Ensure your app maintains academic integrity by reviewing assessment practices and managing system capabilities.
- [Build an Educational Assessment App](build-an-educational-assessment-app.md) — Ensure the academic integrity of your assessment app by using Automatic Assessment Configuration.
- [AEAssessmentSession](aeassessmentsession.md) — A session that your app uses to protect an assessment.
