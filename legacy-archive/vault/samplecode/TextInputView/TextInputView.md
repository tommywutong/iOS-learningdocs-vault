---
title: TextInputView
apple_id: DTS40008840
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-06-05'
source_url: https://developer.apple.com/library/archive/samplecode/TextInputView/Introduction/Intro.html
archived_at: '2026-07-18T03:26:38.448957Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# TextInputView

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-06-05 Updated for Mac OS X 10.7 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobugawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.7 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

A small application that demonstrates how a view can implement the NSTextInputClient protocol. The view acts as a very simple text field, accepting character input and scaling the text to match its height. When the user enters a newline, the text fades away, hence the name "FadingTextView".

As a proper adopter of NSTextInputClient, FadingTextView supports "marked text". This is how the text system represents characters that may still be modified by user input, such as the accent that appears when typing Option-E on the standard U.S. keyboard. The accent is considered "marked text" until another character is entered. (This is also used extensively in input for some other languages such as Japanese or Chinese.)

At a few points, FadingTextView needs to access its input context. This is accomplished by calling the standard NSView -inputContext method, which does not usually need to be overridden.

FadingTextView uses the Cocoa text system (NSTextStorage, NSLayoutManager, NSTextContainer) for efficient drawing of its text. Many of the NSTextInputClient required methods also deal with the position of characters; FadingTextView converts the given points from screen to local coordinates and lets its layout manager do the rest of the work.

Rather than redraw the text at every point during the fade, the text is drawn once to a cache image. This image is then composited more and more transparently over a white background.

The fade-out is accomplished using an NSTimer, which will run in both the default run loop mode and the event-tracking run loop mode. This is so that the fade-out will continue even during a live resize.

[Next](main.m.md)

