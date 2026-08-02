---
title: Speech Programming Topics
apple_id: 10000178i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2003-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Speech/Speech.html
archived_at: '2026-07-15T07:19:18.629822Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Synthesizing%20Speech.md)

# Introduction to Speech

The Cocoa programmatic interface for speech enables an application to “pronounce” a string of text using a synthetic voice. In addition, an application can use this interface to “listen” for commands spoken by a user and act upon those commands. An application can combine both capabilities for a interactive user experience that enables the user to accomplish a multi-step task without depending on the keyboard or mouse. These capabilities not only benefit users of your application who have attention, vision, or other physical disabilities, but can be used by the application to convey or obtain critical information without forcing users to shift focus from what they’re doing.

The NSSpeechSynthesizer and NSSpeechRecognizer classes provide the Cocoa interface to the lower-level Carbon technologies of Speech Synthesis and Speech Recognition, respectively. If you require greater control of speech than permitted by the Cocoa classes, you may use the underlying Carbon frameworks instead.

Speech in Cocoa consists of two general procedures:

- [Synthesizing Speech](Synthesizing%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4dalkcifbekrchjfca) describes how to use an NSSpeechSynthesizer object to speak a string of text to users in a specific voice.
- [Recognizing Speech](Recognizing%20Speech.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4dclkcineuqrkcizea) describes how to use an NSSpeechRecognizer object to apprehend spoken commands which your application can then act upon.

[Next](Synthesizing%20Speech.md)

