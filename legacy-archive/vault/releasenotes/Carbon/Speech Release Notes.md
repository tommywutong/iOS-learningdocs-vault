---
title: Speech Release Notes
apple_id: TP40001043
resource_type: Release Note
platform: macOS
topic: User Experience
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-Speech/index.html
archived_at: '2026-07-18T02:50:22.434711Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Speech Release Notes

This release note provides the latest information about speech technologies for OS X v10.5 (Leopard).

### Speech Synthesis

The Speech Synthesis framework API has been enhanced in Leopard to include support for Core Foundation data types. Also new for Leopard is Alex, an English-speaking voice that leverages advanced Apple technology to deliver natural intonation even at very fast speaking rates. In fact, the synthesizer improvements that make the Alex voice possible can be heard in all of Apple's voices, resulting in more natural intonation and rhythm, and more accurate pronunciations.

### Support for Core Foundation Data Types

New Speech Synthesis routines allow developers to use `CFStringRef` types and other Core Foundation data types when interacting with speech channels. Developers no longer need to convert Core Foundation string objects into a buffer of bytes before speaking text, which makes it much easier to speak non-English languages such as Japanese. In addition, speech channel attributes can now be represented as Core Foundation data types, and external dictionaries can be stored as property list files. You'll find an example of using these new routines in `/Developer/Examples/Speech/Synthesis/SpeechSynthesisExample`.

### Enhanced Synthesizer Plug-in Support

Developers of synthesizer plug-ins will want to revise their synthesizers to support receiving `CFStringRef` types and other Core Foundation data types from the Speech Synthesis framework. This means that the synthesizer will receive the original `CFStringRef` from the client application without conversion, making it easier to support languages that depend on Unicode. And, to better support VoiceOver, synthesizer developers will want to add information to their voice bundles so VoiceOver will know which characters can be individually spoken. For an example of creating a synthesizer plug-in, look in `/Developer/Examples/Speech/Synthesis/SynthesizerAndVoiceExample`.

### Alex

The Alex voice is designed to minimize the need to customize the spoken text by supplying intonational instructions (embedded commands). However, if you find that you still need to provide some customization, be aware that there are subtle differences between Alex and the other Apple voices. From a developer's perspective, the most important difference is the response of the synthesizer to embedded commands that control intonation, such as `pbas`, `pmod`, and `emph`. In Apple's prior synthesizer these commands are faithfully followed by the voices. In the case of Alex, however, these specifications are treated as "guidelines" or "hints". The synthesizer uses these hints to inform its decision-making process, but might not follow them exactly in all cases.

In order to attain the advancements you hear in Alex, the on-disk size of the Alex voice bundle is significantly larger than other Apple voices, resulting in longer delays when first speaking. If minimizing this delay is important, consider preloading the voice by speaking the desired text to a file, such as `/dev/null`, sufficiently ahead of the time you'll need to speak it to the user.
