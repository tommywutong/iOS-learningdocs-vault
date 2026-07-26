---
title: AVAudioSession
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiosession
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiosession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiosession.json'
content_hash: 'sha256:c009adeccd4fdd49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioSession

<sub>Class</sub>

An object that communicates to the system how you intend to use audio in your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioSession
```

## Overview

An audio session acts as an intermediary between your app and the operating system — and, in turn, the underlying audio hardware. You use an audio session to communicate to the operating system the general nature of your app’s audio without detailing the specific behavior or required interactions with the audio hardware. You delegate the management of those details to the audio session, which ensures that the operating system can best manage the user’s audio experience.

All iOS, tvOS, and watchOS apps have a default audio session that comes preconfigured with the following behavior:

- It supports audio playback, but disallows audio recording.
- When the app plays audio, it silences any other background audio.
- In iOS, setting the Ring/Silent switch to silent mode silences any audio the app is playing.
- In iOS, locking a device silences the app’s audio.

Although the default audio session provides useful behavior, it generally doesn’t provide the audio behavior a media app needs. To change the default behavior, you configure your app’s audio session category.

There are six possible categories you can use, but [AVAudioSessionCategoryPlayback](avaudiosession/category-swift.struct/playback.md) is the one that playback apps most commonly use. This category indicates that audio playback is a central feature of your app. When you specify this category, your app’s audio continues with the Ring/Silent switch set to silent mode (iOS only). Using this category, you can also play background audio if you’re using the Audio, AirPlay, and Picture in Picture background mode. For more information, see `Enabling Background Audio`.

You use an [AVAudioSession](avaudiosession.md) object to configure your app’s audio session. This class is a singleton object used to set the audio session’s category, mode, and other configurations. You can interact with the audio session throughout your app’s life cycle, but it’s often useful to perform this configuration at app launch, as shown in the following example.

```swift
func configureAudioSession() {
    // Retrieve the shared audio session.
    let audioSession = AVAudioSession.sharedInstance()
    do {
        // Set the audio session category and mode.
        try audioSession.setCategory(.playback, mode: .moviePlayback)
    } catch {
        print("Failed to set the audio session configuration")
    }
}
```

The audio session uses this configuration when you activate the session using the [setActive:error:](avaudiosession/setactive_error_.md) or [- setActive:withOptions:error:](<avaudiosession/setactive(__options_).md>) method.

> [!note] Note
> You can activate the audio session at any time after setting its category, but it’s generally preferable to defer this call until your app begins audio playback. Deferring the call ensures that you won’t prematurely interrupt any other background audio that may be in progress.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the shared audio session

- [+ sharedInstance](<avaudiosession/sharedinstance().md>) — Returns the shared audio session instance.

### Configuring standard audio behaviors

- [- setCategory:mode:routeSharingPolicy:options:error:](<avaudiosession/setcategory(__mode_policy_options_).md>) — Sets the session category, mode, route-sharing policy, and options.
- [- setCategory:mode:options:error:](<avaudiosession/setcategory(__mode_options_).md>) — Sets the audio session’s category, mode, and options.
- [- setCategory:withOptions:error:](<avaudiosession/setcategory(__options_).md>) — Sets the audio session’s category with the specified options.
- [- setCategory:error:](<avaudiosession/setcategory(__).md>) — Sets the audio session’s category.
- [- setMode:error:](<avaudiosession/setmode(__).md>) — Sets the audio session’s mode.

### Configuring the spatial experience in visionOS

- [intendedSpatialExperience](avaudiosession/intendedspatialexperience-1bpnq.md) — The spatial audio experience your app intends to provide the user.
- [setIntendedSpatialExperience(_:)](<avaudiosession/setintendedspatialexperience(__).md>) — Sets the spatial audio experience your app intends to provide the user.
- [AVAudioSessionSpatialExperience](avaudiosessionspatialexperience-swift.protocol.md)
- [isNowPlayingCandidate](avaudiosession/isnowplayingcandidate.md) — A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.
- [- setIsNowPlayingCandidate:error:](<avaudiosession/setisnowplayingcandidate(__).md>) — Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.

### Activating the audio configuration

- [- setActive:withOptions:error:](<avaudiosession/setactive(__options_).md>) — Activates or deactivates your app’s audio session using the specified options.
- [- activateWithOptions:completionHandler:](<avaudiosession/activate(options_completionhandler_).md>) — Activates an audio session asynchronously.
- [- deactivateWithOptions:completionHandler:](<avaudiosession/deactivate(options_completionhandler_).md>) — Deactivates the audio session asynchronously. _(beta)_
- [AVAudioSessionActivationOptions](avaudiosessionactivationoptions.md) — Constants that describe the options to pass when activating the audio session.
- [AVAudioSessionDeactivationOptions](avaudiosessiondeactivationoptions.md) — Options for deactivating an AVAudioSession

### Observing activation lifecycle

- [AVAudioSessionDidBecomeActiveNotification](avaudiosession/didbecomeactivenotification.md) — Notification sent when the audio session becomes active. _(beta)_
- [AVAudioSessionDidBecomeInactiveNotification](avaudiosession/didbecomeinactivenotification.md) — Notification sent when the audio session becomes inactive. _(beta)_
- [AVAudioSessionResumptionRecommendationNotification](avaudiosession/resumptionrecommendationnotification.md) — Notification sent when the system provides a resumption recommendation. _(beta)_
- [AVAudioSessionDeactivationContextKey](avaudiosession/deactivationcontextkey.md) — Keys for [AVAudioSessionDidBecomeInactiveNotification](avaudiosession/didbecomeinactivenotification.md) Value is an [DeactivationContext](avaudiosession/deactivationcontext.md) object describing the deactivation. _(beta)_
- [AVAudioSessionResumptionContextKey](avaudiosession/resumptioncontextkey.md) — Keys for [AVAudioSessionResumptionRecommendationNotification](avaudiosession/resumptionrecommendationnotification.md) Value is an [ResumptionContext](avaudiosession/resumptioncontext.md) describing the resumption recommendation. _(beta)_
- [DidBecomeActiveMessage](avaudiosession/didbecomeactivemessage.md)
- [DidBecomeInactiveMessage](avaudiosession/didbecomeinactivemessage.md)
- [ResumptionRecommendationMessage](avaudiosession/resumptionrecommendationmessage.md)
- [DeactivationResult](avaudiosession/deactivationresult.md) — Type-safe representation of audio session deactivation results.
- [DeactivationContext](avaudiosession/deactivationcontext.md) — An object that describes why and how the audio session deactivated. _(beta)_
- [DeactivationSource](avaudiosession/deactivationsource.md) — The source of the audio session deactivation. _(beta)_
- [InterruptionContext](avaudiosession/interruptioncontext.md) — An object that provides context about an audio session interruption. _(beta)_
- [ResumptionContext](avaudiosession/resumptioncontext.md) — An object that provides context when resumption becomes available. _(beta)_
- [ResumptionRecommendation](avaudiosession/resumptionrecommendation.md) — The system’s recommendation on whether to resume playback. _(beta)_

### Inspecting the category configuration

- [category](avaudiosession/category-swift.property.md) — The current audio session category.
- [availableCategories](avaudiosession/availablecategories.md) — The audio session categories available on the current device.
- [Category](avaudiosession/category-swift.struct.md) — Audio session category identifiers.
- [categoryOptions](avaudiosession/categoryoptions-swift.property.md) — The set of options associated with the current audio session category.
- [CategoryOptions](avaudiosession/categoryoptions-swift.struct.md) — Constants that specify optional audio behaviors.
- [AVAudioSessionCategoryOptionFarFieldInput](avaudiosession/categoryoptions-swift.struct/farfieldinput.md) — This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [AVAudioSessionCategoryPlayAndRecord](avaudiosession/category-swift.struct/playandrecord.md), [AVAudioSessionCategoryRecord](avaudiosession/category-swift.struct/record.md), and `AVAudioSessionMultiRoute` with [AVAudioSessionModeDualRoute](avaudiosession/mode-swift.struct/dualroute.md).

### Inspecting mode configuration

- [mode](avaudiosession/mode-swift.property.md) — The current audio session’s mode.
- [availableModes](avaudiosession/availablemodes.md) — The audio session modes available on the device.
- [Mode](avaudiosession/mode-swift.struct.md) — Audio session mode identifiers.

### Inspecting rendering mode and capabilities

- [renderingMode](avaudiosession/renderingmode-swift.property.md) — The current audio session’s rendering mode.
- [RenderingMode](avaudiosession/renderingmode-swift.enum.md) — Audio session rendering mode identifiers.
- [AVAudioSessionRenderingModeChangeNotification](avaudiosession/renderingmodechangenotification.md) — A notification the system posts when the rendering mode changes.
- [supportedOutputChannelLayouts](avaudiosession/supportedoutputchannellayouts.md) — The array of channel layouts that the current route supports.
- [AVAudioSessionRenderingCapabilitiesChangeNotification](avaudiosession/renderingcapabilitieschangenotification.md) — A notification the system posts when the rendering capabilities change.

### Inspecting the route sharing policy

- [routeSharingPolicy](avaudiosession/routesharingpolicy-swift.property.md) — The active route-sharing policy.
- [RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.enum.md) — Cases that indicate the possible route-sharing policies for an audio session.

### Mixing with other audio

- [otherAudioPlaying](avaudiosession/isotheraudioplaying.md) — A Boolean value that indicates whether another app is playing audio.
- [secondaryAudioShouldBeSilencedHint](avaudiosession/secondaryaudioshouldbesilencedhint.md) — A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [AVAudioSessionSilenceSecondaryAudioHintNotification](avaudiosession/silencesecondaryaudiohintnotification.md) — A notification the system posts when the primary audio from other apps starts and stops.
- [allowHapticsAndSystemSoundsDuringRecording](avaudiosession/allowhapticsandsystemsoundsduringrecording.md) — A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [- setAllowHapticsAndSystemSoundsDuringRecording:error:](<avaudiosession/setallowhapticsandsystemsoundsduringrecording(__).md>) — Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.

### Managing audio routing

- [Audio routing](audio-routing.md) — Inspect and configure audio routes, ports, and data sources.

### Preparing for long-form video playback

- [- prepareRouteSelectionForPlaybackWithCompletionHandler:](<avaudiosession/preparerouteselectionforplayback(completionhandler_).md>) — Prepares the route selection for long-form video playback.
- [RouteSelection](avaudiosession/routeselection.md) — Constants used to define the active route selection.

### Handling interruptions

- [prefersNoInterruptionsFromSystemAlerts](avaudiosession/prefersnointerruptionsfromsystemalerts.md) — A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [- setPrefersNoInterruptionsFromSystemAlerts:error:](<avaudiosession/setprefersnointerruptionsfromsystemalerts(__).md>) — Sets the preference for not interrupting the audio session with system alerts.
- [prefersInterruptionOnRouteDisconnect](avaudiosession/prefersinterruptiononroutedisconnect.md) — A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [- setPrefersInterruptionOnRouteDisconnect:error:](<avaudiosession/setprefersinterruptiononroutedisconnect(__).md>) — Sets a preference to interrupt the audio session when the active route disconnects.
- [AVAudioSessionInterruptionNotification](avaudiosession/interruptionnotification.md) — A notification the system posts when an audio interruption occurs.

### Monitoring spatial capabilities

- [AVAudioSessionSpatialPlaybackCapabilitiesChangedNotification](avaudiosession/spatialplaybackcapabilitieschangednotification.md) — A notification the system posts when its spatial playback capabilities change.

### Inspecting the audio prompt style

- [promptStyle](avaudiosession/promptstyle-swift.property.md) — A hint to audio sessions that use voice prompt mode to alter the type of prompts they issue in response to other system audio, such as Siri and phone calls.
- [PromptStyle](avaudiosession/promptstyle-swift.enum.md) — Constants that indicate the prompt style to use.

### Enabling stereo recording

- [inputOrientation](avaudiosession/inputorientation.md) — An orientation value that dictates which directions represent left and right when capturing audio from a built-in microphone configured for stereo recording.
- [preferredInputOrientation](avaudiosession/preferredinputorientation.md) — The audio session’s preferred stereo input orientation.
- [- setPreferredInputOrientation:error:](<avaudiosession/setpreferredinputorientation(__).md>) — Sets the audio session’s preferred stereo input orientation.
- [StereoOrientation](avaudiosession/stereoorientation.md) — Constants that define the supported stereo orientations.

### Enabling adding audio to calls

- [isMicrophoneInjectionAvailable](avaudiosession/ismicrophoneinjectionavailable.md) — A Boolean value that indicates whether microphone injection is available.
- [preferredMicrophoneInjectionMode](avaudiosession/preferredmicrophoneinjectionmode.md) — The preferred mode of injecting audio into another app’s input stream.
- [- setPreferredMicrophoneInjectionMode:error:](<avaudiosession/setpreferredmicrophoneinjectionmode(__).md>) — Sets the preferred mode of injecting audio into another app’s input stream.
- [MicrophoneInjectionMode](avaudiosession/microphoneinjectionmode.md) — The modes of injecting audio into another app’s input stream.
- [AVAudioSessionMicrophoneInjectionCapabilitiesChangeNotification](avaudiosession/microphoneinjectioncapabilitieschangenotification.md) — A notification the system posts when its capability to inject audio into an input stream changes.

### Configuring echo cancellation

- [isEchoCancelledInputAvailable](avaudiosession/isechocancelledinputavailable.md) — A Boolean value that indicates whether the built-in microphone and speaker route supports echo cancellation.
- [isEchoCancelledInputEnabled](avaudiosession/isechocancelledinputenabled.md) — A Boolean value that indicates whether an echo-canceled input is in an enabled state.
- [- setPrefersEchoCancelledInput:error:](<avaudiosession/setprefersechocancelledinput(__).md>) — Sets a preference to enable echo-canceled input on supported hardware.
- [prefersEchoCancelledInput](avaudiosession/prefersechocancelledinput.md) — A Boolean value that indicates the audio session’s preference for using an echo-canceled input.

### Configuring audio muting

- [outputMuted](avaudiosession/isoutputmuted.md) — A Boolean value that indicates whether audio output is in a muted state.
- [- setOutputMuted:error:](<avaudiosession/setoutputmuted(__).md>) — Sets a Boolean value to inform the system to mute the session’s output audio. The default value is false (unmuted).
- [AVAudioSessionOutputMuteStateChangeNotification](avaudiosession/outputmutestatechangenotification.md) — Notification sent to registered listeners when session’s output mute state changes.
- [AVAudioSessionMuteStateKey](avaudiosession/mutestatekey.md) — Keys for [AVAudioSessionOutputMuteStateChangeNotification](avaudiosession/outputmutestatechangenotification.md) Value is `NSNumber` type with boolean value 0 for unmuted or value 1 for muted (samples zeroed out)
- [AVAudioSessionUserIntentToUnmuteOutputNotification](avaudiosession/userintenttounmuteoutputnotification.md) — Notification sent to registered listeners when the application’s output is muted and user hints to unmute.
- [AVAudioSessionUserIntentToUnmuteOutputNotification](avaudiosession/userintenttounmuteoutputnotification.md) — Notification sent to registered listeners when the application’s output is muted and user hints to unmute.
- [AVAudioSessionMuteStateKey](avaudiosession/mutestatekey.md) — Keys for [AVAudioSessionOutputMuteStateChangeNotification](avaudiosession/outputmutestatechangenotification.md) Value is `NSNumber` type with boolean value 0 for unmuted or value 1 for muted (samples zeroed out)

### Configuring device settings

- [Audio hardware](audio-hardware.md) — Inspect and configure audio device settings including input gain, sample rate, and channel counts.

### Setting the aggregated I/O preference

- [- setAggregatedIOPreference:error:](<avaudiosession/setaggregatediopreference(__).md>) — Sets the audio session’s aggregated I/O configuration preference.
- [IOType](avaudiosession/iotype.md) — Constant values used to specify the audio session’s aggregated I/O behavior.

### Handling a change of media services

- [AVAudioSessionMediaServicesWereResetNotification](avaudiosession/mediaserviceswereresetnotification.md) — A notification the system posts when the media server restarts.
- [AVAudioSessionMediaServicesWereLostNotification](avaudiosession/mediaserviceswerelostnotification.md) — A notification the system posts when it terminates the media server.

### Errors

- [AVAudioSession.ErrorCode](../coreaudiotypes/avaudiosession/errorcode.md) — Codes that describe error conditions that may occur when performing audio session operations.

### Deprecated

- [Deprecated Symbols](deprecated-symbols.md) — Review unsupported symbols and their replacements.

### Structures

- [BypassedSpatialExperience](avaudiosession/bypassedspatialexperience.md) — An experience that bypasses system-provided audio spatialization.
- [FixedSpatialExperience](avaudiosession/fixedspatialexperience.md) — An experience where the sound has a size dictated by its sound stage and is head-locked relative to the user.
- [HeadTrackedSpatialExperience](avaudiosession/headtrackedspatialexperience.md) — An experience where the sound a size dictated by its sound stage and location dictated by its anchoring strategy.

### Enumerations

- [AnchoringStrategy](avaudiosession/anchoringstrategy.md) — Constants that specify how to set the origin of audio in a head-tracked spatial experience.

## See Also

### System audio

- [Handling audio interruptions](handling-audio-interruptions.md) — Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](responding-to-audio-route-changes.md) — Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Routing audio to specific devices in multidevice sessions](routing-audio-to-specific-devices-in-multidevice-sessions.md) — Map audio channels to specific devices in multiroute sessions for recording and playback.
- [Adding synthesized speech to calls](adding-synthesized-speech-to-calls.md) — Provide a more accessible experience by adding your app’s audio to a call.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md) — Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [AVAudioApplication](avaudioapplication.md) — An object that manages one or more audio sessions that belong to an app.
- [AVAudioRoutingArbiter](avaudioroutingarbiter.md) — An object for configuring macOS apps to participate in AirPods Automatic Switching.
