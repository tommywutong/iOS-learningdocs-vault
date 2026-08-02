---
title: SearchField
apple_id: DTS10004112
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-06-25'
source_url: https://developer.apple.com/library/archive/samplecode/SearchField/Listings/README_md.html
archived_at: '2026-07-18T03:23:37.123985Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SearchField](SearchField.md)


[Next](LICENSE.txt.md)[Previous](MyWindowController.h.md)

# README.md

```objc
# SearchField

"SearchField" is a sample Cocoa application that shows how to use a special text control called "NSSearchField".  This is the control that is used in the popular Apple applications like Safari, iTunes, Mail, etc.


## Summary
An NSSearchField object implements a text field control that is optimized for performing text-based searches. The control provides a customized text field for entering search data, a search button, a cancel button, and a pop-up icon menu for listing recent search strings and custom search categories.

When the user types and then pauses, the NSSearchField's cell’s action message is sent to its target. You can then query the cell’s string value for the current text and search a list of keywords to match, then providing these words the control's drop down menu.  This sample shows you how to override the text-based searching by providing your own list of keywords.

With regards to the popup icon for show the recents menu listing recent search strings, this sample shows how to further customize this menu by building the menu completely from scratch.  You can do this using InterfaceBuilder, but the code gives you a better illustration.

## Keyword Searching
Basically we want to override the NSSearchField's type completion feature by providing our own list of keyword to match.  Therefore its up to us to call the control's "complete:" method at the right time.

Each time a character is typed, a lookup occurs every time "controlTextDidChange:" is called.  If you don't want the drop down list to show on each character typed, then you need to call "complete:" less frequently.  Each lookup forces the drop down list to update itself causing the menu to disappear and reappear again with the new matches.  So calling "complete:" from within the controlTextDidChange can flood the run loop by repeatedly generating "controlTextDidChange:" calls.  So we need to be a little smarter not to post "complete:" when it's not necessary.

Hence, by implementing -
- (NSArray*)control:(NSControl*)control textView:(NSTextView *)textView completions:(NSArray*)words forPartialWordRange:(NSRange)charRange indexOfSelectedItem:(int*)index;
you now have complete control on the contents on which text-based searching is based.


## Requirements

### Build

Xcode 6.0 or later; OS X 10.10 SDK or later

### Runtime

OS X 10.8 or later

Copyright (C) 2006-2015 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](MyWindowController.h.md)

