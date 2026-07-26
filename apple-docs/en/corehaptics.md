---
title: Core Haptics
framework: Core Haptics
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corehaptics
source_url: 'https://developer.apple.com/documentation/corehaptics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corehaptics.json'
content_hash: 'sha256:ebba842b656d9bf9'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Core Haptics

<sub>Framework</sub>

Compose and play haptic patterns to customize your iOS app’s haptic feedback.

## Overview

Core Haptics lets you add customized haptic and audio feedback to your app. Use haptics to engage users physically, with tactile and audio feedback that gets attention and reinforces actions. Some system-provided interface elements—like pickers, switches, and sliders—automatically provide haptic feedback as users interact with them. With Core Haptics, you extend this functionality by composing and combining haptics beyond the default patterns.

Your app can play custom haptic patterns crafted from basic building blocks called haptic events ([CHHapticEvent](corehaptics/chhapticevent.md)). Events can be transient, like the feedback you get from toggling a switch, or continuous, like the vibration or sound from a ringtone. You can use transient and continuous patterns independently, or build your pattern from precise combinations of the two. Another type of haptic event allows you to play customized audio content as part of your pattern.

## Topics

### Essentials

- [Preparing your app to play haptics](corehaptics/preparing-your-app-to-play-haptics.md) — Set up your app to play haptics.
- [Playing a single-tap haptic pattern](corehaptics/playing-a-single-tap-haptic-pattern.md) — Create and play a transient haptic pattern from a dictionary literal inline.
- [CHHapticEngine](corehaptics/chhapticengine.md) — An object that represents the connection to the haptic server.
- [CHHapticPattern](corehaptics/chhapticpattern.md) — An object representing a haptic waveform.
- [CHHapticPatternPlayer](corehaptics/chhapticpatternplayer.md) — A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.
- [CHHapticAdvancedPatternPlayer](corehaptics/chhapticadvancedpatternplayer.md) — A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.

### Programmatic haptics

- [Delivering Rich App Experiences with Haptics](corehaptics/delivering-rich-app-experiences-with-haptics.md) — Enhance your app’s experience by incorporating haptic and sound feedback into key interactive moments.
- [Playing Collision-Based Haptic Patterns](corehaptics/playing-collision-based-haptic-patterns.md) — Play a custom haptic pattern whose strength depends on an object’s collision speed.
- [Updating Continuous and Transient Haptic Parameters in Real Time](corehaptics/updating-continuous-and-transient-haptic-parameters-in-real-time.md) — Generate continuous and transient haptic patterns in response to user touch.
- [CHHapticEvent](corehaptics/chhapticevent.md) — An object that describes a single haptic or audio event.
- [CHHapticEventParameter](corehaptics/chhapticeventparameter.md) — A static parameter value that represents a single property of the haptic pattern.
- [CHHapticDynamicParameter](corehaptics/chhapticdynamicparameter.md) — A value that you send to a haptic pattern player to alter a property value during playback.
- [CHHapticParameterCurve](corehaptics/chhapticparametercurve.md) — A curve that you send to a haptic pattern player to alter a property value gradually during playback.

### File-based haptics

- [Playing a Custom Haptic Pattern from a File](corehaptics/playing-a-custom-haptic-pattern-from-a-file.md) — Sample predesigned Apple Haptic Audio Pattern files, and learn how to play your own.
- [Representing haptic patterns in AHAP files](corehaptics/representing-haptic-patterns-in-ahap-files.md) — Understand the Apple Haptic and Audio Pattern (AHAP) file format.

### Game controller haptics

- [Playing Haptics on Game Controllers](corehaptics/playing-haptics-on-game-controllers.md) — Add haptic feedback to supported game controllers by using Core Haptics.

### Haptic errors

- [CoreHapticsErrorDomain](corehaptics/corehapticserrordomain.md) — A string representation of the haptic error domain.
- [CHHapticError](corehaptics/chhapticerror.md) — A structure that represents a framework error.
- [Code](corehaptics/chhapticerror/code.md) — Error codes for framework operations.

### Variables

- [CHHapticAudioResourceKeyLoopEnabled](corehaptics/chhapticaudioresourcekeyloopenabled.md) — A key for a Boolean value that indicates whether to loop audio playback.
- [CHHapticAudioResourceKeyUseVolumeEnvelope](corehaptics/chhapticaudioresourcekeyusevolumeenvelope.md) — A key for a Boolean value that indicates whether audio file playback fades in and out using an envelope.

### Type Aliases

- [CHHapticAudioResourceKey](corehaptics/chhapticaudioresourcekey.md) — A type alias for a key that identifies the playback behavior of an audio resource.
