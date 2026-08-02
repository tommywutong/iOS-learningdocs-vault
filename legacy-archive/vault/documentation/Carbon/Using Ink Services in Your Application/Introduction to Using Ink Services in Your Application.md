---
title: Using Ink Services in Your Application
apple_id: TP40000959
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2003-07-24'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/using_ink/ink_intro/ink_intro.html
archived_at: '2026-07-15T05:25:24.253205Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Ink%20Services%20Concepts.md)

# Introduction to Using Ink Services in Your Application

Ink supports text input using a stylus and a graphics tablet. When a user prints text with the stylus, Ink processes the text and flows the recognized text to the current insertion point, just as if the user had typed it on a keyboard. When users work with a graphics tablet, there’s no need to put down the stylus and return to the keyboard just to enter a title, caption, or filename. Users can also write keyboard equivalents with the stylus that enable them to open and close windows, and otherwise control an application without lifting the stylus from the tablet. Users can turn Ink handwriting recognition on or off, control where inking is permitted, and enable or disable recognition of predefined editing gestures.

When Ink was introduced in Mac OS X version 10.2, it provided automatic support for Ink input into applications. As long as the user enables Ink in System Preferences, an application receives Ink input as text without needing any modifications. As English text is written on a tablet, it is automatically recognized and entered as a stream of key down events into a document or text field.

With the introduction of the Ink Services application programming interface (API) in Mac OS X version 10.3, developers can further integrate Ink into their application and create novel solutions for Mac OS X. Some of the key features the new API provides are:

- The ability to programmatically enable or disable handwriting recognition
- Access to a list of alternate interpretations for Ink input
- Support for deferred recognition and recognition on demand
- Support for direct manipulation of text using gestures
- Access to Ink data at multiple levels (points and recognized text)

With the release of Mac OS X version 10.3, the Ink recognition engine supports English, French, and German. The language that is recognized depends on the user’s language setting in the Ink pane of System Preferences.

Any developer whose application receives text input should read this document to find out how the Ink Services API can benefit an application. The document is of most benefit to developers who have specific needs related to Ink input. Some specialized needs include the following situations:

- You want to implement a handwriting recognition solution for an input device. For example, you are a hardware vendor who wants to supply end-user software for your tablet or other piece of hardware.
- You need to provide a customized solution for recognizing the end of a phrase or word. For example, you want all input in a given window to be treated as a single phrase.
- You are writing a text editor and want to provide support for direct manipulation of text with Ink gestures.
- You want to implement a correction model. For example, you want to provide users with a list of alternate interpretations for a word.

The remainder of this document is organized into the following chapters:

- [Ink Services Concepts](Ink%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbtfvkfawcsivddcmbr), describes the Ink user interface, provides an overview of how Ink works in Mac OS X, and introduces the key concepts you need to understand the Ink Services API.
- [Ink Services Tasks](Ink%20Services%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbufvkfawcsivddcmbr), provides information on how to accomplish the most common programming tasks using the Ink Services API.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbvfvkfami), defines Ink terminology.

The ideal way to proceed through the document depends on your programming experience and the tasks you want Ink Services to perform. Because the Ink Services API is new to Mac OS X, all developers should first read [Ink Services Concepts](Ink%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbtfvkfawcsivddcmbr). If you need more than the automatic support provided by Ink Services, you should read the how-to sections in [Ink Services Tasks](Ink%20Services%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbufvkfawcsivddcmbr) that seem most appropriate to your application.

If you plan to use the Ink Services API in your application, you should read _Ink Services Reference_, as this document provides a complete reference to the Ink Services API.

[Next](Ink%20Services%20Concepts.md)

