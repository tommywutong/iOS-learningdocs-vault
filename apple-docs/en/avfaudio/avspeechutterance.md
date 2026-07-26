---
title: AVSpeechUtterance
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avspeechutterance
source_url: 'https://developer.apple.com/documentation/avfaudio/avspeechutterance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avspeechutterance.json'
content_hash: 'sha256:593763169064176b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVSpeechUtterance

<sub>Class</sub>

An object that encapsulates the text for speech synthesis and parameters that affect the speech.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSpeechUtterance
```

## Overview

An `AVSpeechUtterance` is the basic unit of speech synthesis.

To synthesize speech, create an `AVSpeechUtterance` instance with text you want a speech synthesizer to speak. Optionally, change the [voice](avspeechutterance/voice.md), [pitchMultiplier](avspeechutterance/pitchmultiplier.md), [volume](avspeechutterance/volume.md), [rate](avspeechutterance/rate.md), [preUtteranceDelay](avspeechutterance/preutterancedelay.md), or [postUtteranceDelay](avspeechutterance/postutterancedelay.md) parameters for the utterance. Pass the utterance to an instance of [AVSpeechSynthesizer](avspeechsynthesizer.md) to begin speech, or enqueue the utterance to speak later if the synthesizer is already speaking.

Split a body of text into multiple utterances if you want to apply different speech parameters. For example, you can emphasize a sentence by increasing the pitch and decreasing the rate of that utterance relative to others, or you can introduce pauses between sentences by putting each into an utterance with a leading or trailing delay.

Set and use the [AVSpeechSynthesizerDelegate](avspeechsynthesizerdelegate.md) to receive notifications when the synthesizer starts or finishes speaking an utterance. Create an utterance for each meaningful unit in a body of text if you want to receive notifications as its speech progresses.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating an utterance

- [- initWithString:](<avspeechutterance/init(string_).md>) — Creates an utterance with the text string that you specify for the speech synthesizer to speak.
- [- initWithAttributedString:](<avspeechutterance/init(attributedstring_).md>) — Creates an utterance with the attributed text string that you specify for the speech synthesizer to speak.
- [AVSpeechSynthesisIPANotationAttribute](avspeechsynthesisipanotationattribute.md) — A string that contains International Phonetic Alphabet (IPA) symbols the speech synthesizer uses to control pronunciation of certain words or phrases.
- [- initWithSSMLRepresentation:](<avspeechutterance/init(ssmlrepresentation_)-8zam9.md>) — Creates a speech utterance with an Speech Synthesis Markup Language (SSML) string.

### Configuring an utterance

- [voice](avspeechutterance/voice.md) — The voice the speech synthesizer uses when speaking the utterance.
- [pitchMultiplier](avspeechutterance/pitchmultiplier.md) — The baseline pitch the speech synthesizer uses when speaking the utterance.
- [volume](avspeechutterance/volume.md) — The volume the speech synthesizer uses when speaking the utterance.
- [prefersAssistiveTechnologySettings](avspeechutterance/prefersassistivetechnologysettings.md) — A Boolean that specifies whether assistive technology settings take precedence over the property values of this utterance.

### Configuring utterance timing

- [rate](avspeechutterance/rate.md) — The rate the speech synthesizer uses when speaking the utterance.
- [AVSpeechUtteranceMinimumSpeechRate](avspeechutteranceminimumspeechrate.md) — The minimum rate the speech synthesizer uses when speaking an utterance.
- [AVSpeechUtteranceMaximumSpeechRate](avspeechutterancemaximumspeechrate.md) — The maximum rate the speech synthesizer uses when speaking an utterance.
- [AVSpeechUtteranceDefaultSpeechRate](avspeechutterancedefaultspeechrate.md) — The default rate the speech synthesizer uses when speaking an utterance.
- [preUtteranceDelay](avspeechutterance/preutterancedelay.md) — The amount of time the speech synthesizer pauses before speaking the utterance.
- [postUtteranceDelay](avspeechutterance/postutterancedelay.md) — The amount of time the speech synthesizer pauses after speaking an utterance before handling the next utterance in the queue.

### Inspecting utterance text

- [speechString](avspeechutterance/speechstring.md) — A string that contains the text for speech synthesis.
- [attributedSpeechString](avspeechutterance/attributedspeechstring.md) — An attributed string that contains the text for speech synthesis.

### Initializers

- [init(SSMLRepresentation:)](<avspeechutterance/init(ssmlrepresentation_)-2aunp.md>)
- [init(SSMLRepresentation:)](<avspeechutterance/init(ssmlrepresentation_)-7rl77.md>)
- [init(coder:)](<avspeechutterance/init(coder_).md>)

## See Also

### Spoken text attributes

- [AVSpeechSynthesisVoice](avspeechsynthesisvoice.md) — A distinct voice for use in speech synthesis.
