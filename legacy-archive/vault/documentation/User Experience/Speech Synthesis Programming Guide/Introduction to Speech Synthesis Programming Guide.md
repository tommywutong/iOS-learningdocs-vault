---
title: Speech Synthesis Programming Guide
apple_id: TP40004365
resource_type: Guide
platform: macOS
topic: User Experience
technology: ApplicationServices
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-18T02:12:49.798106Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Speech%20Synthesis%20in%20OS%20X.md)

# Introduction to Speech Synthesis Programming Guide

Speech synthesis, also called text-to-speech, is the generation of synthetic speech. An application or other process sends text to a speech synthesizer, which creates a spoken version that can be output through the audio hardware or saved to a file.

This document covers speech synthesis support in OS X. It provides an overview of speech components and the speech synthesis process, and it describes how to incorporate and manipulate synthesized speech in your application.

You should read this document to learn about speech synthesis in OS X and about how you can customize your application’s spoken output. If you’re unfamiliar with the concepts of synthesized speech, be sure to read [Speech Synthesis in OS X](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltm) for an overview of how speech fits into the operating system and of the speech generation process. Carbon, Cocoa, and AppleScript provide APIs to produce spoken output. Be sure to read the API overviews in [Designing and Implementing an Application That Speaks](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnbnknlte) to find out which programming language provides the features you need.

Speech Synthesis Programming Guide contains the following chapters and appendixes:

- [Speech Synthesis in OS X](Speech%20Synthesis%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmznknltm) provides an overview of the speech generation process and its components, and describes ways you can use and customize spoken output in your application.
- [Designing and Implementing an Application That Speaks](Designing%20and%20Implementing%20an%20Application%20That%20Speaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnbnknlte) describes some design strategies and guidelines for providing spoken output in your application. It also outlines the speech synthesis APIs available in Cocoa, Carbon, and AppleScript, and provides some sample code.
- [Techniques for Customizing Synthesized Speech](Techniques%20for%20Customizing%20Synthesized%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnjnknltg) details several methods for customizing your application’s spoken output, and describes a handful of ways to improve synthesized speech.
- [Syntax of Embedded Speech Commands](Syntax%20of%20Embedded%20Speech%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnznknltc) describes the formal syntax of embedded speech commands.
- [Phonemes](Phonemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqojnknltc) lists the North American English phoneme symbols the MacinTalk synthesizer recognizes.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqnrnknltc) contains definitions of speech-related terms used in this document. Every term you see displayed in bold font, such as _speech synthesizer_, appears in the Glossary.
- [Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgnrvfvbuqmrnknltc) lists the changes made to this document.

In addition to this document, the [Reference Library > User Experience > Speech Technologies](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000437-TP30000576) contains several other resources to help you take advantage of synthesized speech in your application.

- _[Speech Synthesis Manager Reference](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)_ describes the Carbon speech synthesis API.
- _[NSSpeechSynthesizer Class Reference](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer)_ describes the Cocoa speech synthesis API.
- _[Speech Programming Topics](../../Cocoa/Speech%20Programming%20Topics/Introduction%20to%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tq2i)_ briefly describes some of the tasks you can accomplish using the Cocoa speech synthesis API.
- _[CocoaSpeechSynthesisExample](../../../samplecode/CocoaSpeechSynthesisExample/CocoaSpeechSynthesisExample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcmbyhe)_ is a sample Cocoa application that uses the Carbon speech synthesis API.
- The speech developers mailing list ([speech-dev](http://lists.apple.com/mailman/listinfo/speech-dev)) is an excellent place to discuss issues related to speech synthesis and recognition.
[Next](Speech%20Synthesis%20in%20OS%20X.md)

