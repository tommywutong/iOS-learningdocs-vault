---
title: AVSpeechSynthesizer
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avspeechsynthesizer
source_url: 'https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avspeechsynthesizer.json'
content_hash: 'sha256:3ba4500a3a0c3584'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVSpeechSynthesizer

<sub>Class</sub>

An object that produces synthesized speech from text utterances and enables monitoring or controlling of ongoing speech.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSpeechSynthesizer
```

## Overview

To speak some text, create an [AVSpeechUtterance](avspeechutterance.md) instance that contains the text and pass it to [- speakUtterance:](<avspeechsynthesizer/speak(__).md>) on a speech synthesizer instance. You can optionally also retrieve an [AVSpeechSynthesisVoice](avspeechsynthesisvoice.md) and set it on the utterance’s [voice](avspeechutterance/voice.md) property to have the speech synthesizer use that voice when speaking the utterance’s text.

The speech synthesizer maintains a queue of utterances that it speaks. If the synthesizer isn’t speaking, calling [- speakUtterance:](<avspeechsynthesizer/speak(__).md>) begins speaking that utterance either immediately or after pausing for its [preUtteranceDelay](avspeechutterance/preutterancedelay.md), if necessary. If the synthesizer is speaking, the synthesizer adds utterances to a queue and speaks them in the order it receives them.

After speech begins, you can use the synthesizer object to pause or stop speech. After pausing, you can resume the speech from its paused point or stop the speech entirely and remove all remaining utterances in the queue.

You can monitor the speech synthesizer by examining its [speaking](avspeechsynthesizer/isspeaking.md) and [paused](avspeechsynthesizer/ispaused.md) properties, or by setting a delegate that conforms to [AVSpeechSynthesizerDelegate](avspeechsynthesizerdelegate.md). The delegate receives significant events as they occur during speech synthesis.

An `AVSpeechSynthesizer` also controls the route where the speech plays. For more information, see Directing speech output.

> [!note] Note
> The system doesn’t automatically retain the speech synthesizer, so you need to manually retain it until speech concludes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Controlling speech

- [- speakUtterance:](<avspeechsynthesizer/speak(__).md>) — Adds the utterance you specify to the speech synthesizer’s queue.
- [- continueSpeaking](<avspeechsynthesizer/continuespeaking().md>) — Resumes speech from its paused point.
- [- pauseSpeakingAtBoundary:](<avspeechsynthesizer/pausespeaking(at_).md>) — Pauses speech at the boundary you specify.
- [- stopSpeakingAtBoundary:](<avspeechsynthesizer/stopspeaking(at_).md>) — Stops speech at the boundary you specify.
- [AVSpeechBoundary](avspeechboundary.md) — Specifies when to pause or stop speech.

### Inspecting a speech synthesizer

- [speaking](avspeechsynthesizer/isspeaking.md) — A Boolean value that indicates whether the speech synthesizer is speaking or is in a paused state and has utterances to speak.
- [paused](avspeechsynthesizer/ispaused.md) — A Boolean value that indicates whether a speech synthesizer is in a paused state.

### Managing the delegate

- [delegate](avspeechsynthesizer/delegate.md) — The delegate object for the speech synthesizer.
- [AVSpeechSynthesizerDelegate](avspeechsynthesizerdelegate.md) — A delegate protocol that contains optional methods you can implement to respond to events that occur during speech synthesis.

### Directing speech output

- [usesApplicationAudioSession](avspeechsynthesizer/usesapplicationaudiosession.md) — A Boolean value that specifies whether the app manages the audio session.
- [mixToTelephonyUplink](avspeechsynthesizer/mixtotelephonyuplink.md) — A Boolean value that specifies whether to send synthesized speech to an active call.
- [outputChannels](avspeechsynthesizer/outputchannels.md) — An array of audio session channels to route generated speech.
- [- writeUtterance:toBufferCallback:](<avspeechsynthesizer/write(__tobuffercallback_).md>) — Generates speech for the utterance and invokes the callback with the audio buffer.
- [BufferCallback](avspeechsynthesizer/buffercallback.md) — A type that defines a callback that receives a buffer of generated speech.
- [- writeUtterance:toBufferCallback:toMarkerCallback:](<avspeechsynthesizer/write(__tobuffercallback_tomarkercallback_).md>) — Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [MarkerCallback](avspeechsynthesizer/markercallback.md) — A type that defines a callback that receives speech markers.

### Enabling personal voices

- [personalVoiceAuthorizationStatus](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.type.property.md) — Your app’s authorization to use personal voices.
- [AVSpeechSynthesisAvailableVoicesDidChangeNotification](avspeechsynthesizer/availablevoicesdidchangenotification.md) — A notification that indicates a change in available voices for speech synthesis.
- [+ requestPersonalVoiceAuthorizationWithCompletionHandler:](<avspeechsynthesizer/requestpersonalvoiceauthorization(completionhandler_).md>) — Prompts the user to authorize your app to use personal voices.
- [PersonalVoiceAuthorizationStatus](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum.md) — An enumeration that models the personal voices authorization status.
