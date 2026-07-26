---
title: AVSpeechSynthesisVoice
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avspeechsynthesisvoice
source_url: 'https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avspeechsynthesisvoice.json'
content_hash: 'sha256:74cde068b36738e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVSpeechSynthesisVoice

<sub>Class</sub>

A distinct voice for use in speech synthesis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSpeechSynthesisVoice
```

## Overview

The primary factors that distinguish a voice in speech synthesis are language, locale, and quality. Create an instance of `AVSpeechSynthesisVoice` to select a voice that’s appropriate for the text and the language, and set it as the value of the [voice](avspeechutterance/voice.md) property on an [AVSpeechUtterance](avspeechutterance.md) instance. The voice may optionally reflect a local variant of the language, such as Australian or South African English. For a complete list of supported languages, see [Languages Supported by VoiceOver](https://support.apple.com/en-us/HT206175).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Obtaining voices

- [+ voiceWithIdentifier:](<avspeechsynthesisvoice/init(identifier_).md>) — Retrieves a voice for the identifier you specify.
- [+ voiceWithLanguage:](<avspeechsynthesisvoice/init(language_).md>) — Retrieves a voice for the BCP 47 code language code you specify.
- [+ speechVoices](<avspeechsynthesisvoice/speechvoices().md>) — Retrieves all available voices on the device.
- [AVSpeechSynthesisVoiceIdentifierAlex](avspeechsynthesisvoiceidentifieralex.md) — The voice that the system identifies as Alex.

### Inspecting voices

- [identifier](avspeechsynthesisvoice/identifier.md) — The unique identifier of a voice.
- [name](avspeechsynthesisvoice/name.md) — The name of a voice.
- [quality](avspeechsynthesisvoice/quality.md) — The speech quality of a voice.
- [gender](avspeechsynthesisvoice/gender.md) — The gender for a voice.
- [voiceTraits](avspeechsynthesisvoice/voicetraits.md) — The traits of a voice.
- [audioFileSettings](avspeechsynthesisvoice/audiofilesettings.md) — A dictionary that contains audio file settings.
- [AVSpeechSynthesisVoiceQuality](avspeechsynthesisvoicequality.md) — The speech quality of a voice.
- [AVSpeechSynthesisVoiceGender](avspeechsynthesisvoicegender.md) — The gender for a voice.
- [Traits](avspeechsynthesisvoice/traits.md) — Traits that describe a voice.

### Working with language codes

- [+ currentLanguageCode](<avspeechsynthesisvoice/currentlanguagecode().md>) — Returns the language and locale code for the user’s current locale.
- [language](avspeechsynthesisvoice/language.md) — A BCP 47 code that contains the voice’s language and locale.

### Initializers

- [init(coder:)](<avspeechsynthesisvoice/init(coder_).md>)

## See Also

### Spoken text attributes

- [AVSpeechUtterance](avspeechutterance.md) — An object that encapsulates the text for speech synthesis and parameters that affect the speech.
