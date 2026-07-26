---
title: 'Method invocation formatting styles in Objective-C | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/11/method-invocation-formatting-styles-in.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:7a4d252dee4a00dd'
translated: false
---

> 原文：[Method invocation formatting styles in Objective-C | Cocoa with Love](https://www.cocoawithlove.com/2008/11/method-invocation-formatting-styles-in.html)　·　Cocoa with Love (Matt Gallagher)

While most traits of Objective-C follow consistent styles, method invocation formatting — arguably a defining characteristic of the language — does not. In this post, I'll look at a handful of approaches that different programmers use to format their method invocations and discuss their advantages and disadvantages.

## The problems with method invocations...

How should you format a method invocation when it is too long to fit on the line? Judging from the multitude of conventions that different programmers use, there is no clear answer.

There is no ambiguity about how to write a short, simple method invocation:

```objc
[myColor set];
```

But if a method is longer than the nominated screen width:

```objc
NSColor *myColor = [NSColor colorWithCalibratedRed:120.0/255.0 green:120.0/255.0 blue:120.0/255.0 alpha:1.0];
```

opinions begin to vary.

In addition to this consideration is how much should you inline? Cocoa strongly suggests that an allocation and initialization statement should always be a single line:

```objc
id myObject = [[MyClass alloc] init];
```

but how far should you continue to inline before decomposing the statement into separate statements? i.e.

```objc
// Completely inline...
NSColor *deviceColor = [[[NSColorPicker sharedColorPicker] color] colorUsingColorSpaceName:NSDeviceRGBColorSpace];

// Decomposed...
NSColor *cur = [[NSColorPicker sharedColorPicker] color];
NSColor *devColor = [cur colorUsingColorSpaceName:NSDeviceRGBColorSpace];
```

Here are a few different approaches...

## Style 1: Soft wrap and never decompose

The simplest approach to formatting Objective-C method invocations is the "do nothing" approach. This involves:

- Make your text editor wrap lines with an indent if they are wider than the page
- Never decompose statements if the sub-methods are only used once.

Using this approach, the `deviceColor` creation might look like this:

```objc
NSColor *deviceColor = [[[NSColorPicker sharedColorPicker] color]
    colorUsingColorSpaceName:NSDeviceRGBColorSpace];
```

This is the approach advocated by [Penny Arcade](http://www.penny-arcade.com/comic/2007/07/02/) [recurring character](http://www.penny-arcade.com/comic/2008/11/26/) Wil Shipley in his [Pimp My Code series](http://www.wilshipley.com/blog/2005/10/pimp-my-code-part-5-special-apple.html). It is also the approach that Apple have started using in some (but not all) of Xcode's project templates.

### Advantages

You, as the typer of code, never have to do anything. No fussing, no reformatting. You also never have to declare a variable that you only need once; just inline everything.

For Apple, providing code in a template, this approach also has the advantage that if users prefer wrapped code, it is faster for Xcode users to reformat this unwrapped style into a wrapped style of their choice than it is to reformat already wrapped code into a different style.

### Disadvantages

This approach can reduce clarity.

From [Pimp My Code Part 5: Special Apple Sample Code Edition...](http://www.wilshipley.com/blog/2005/10/pimp-my-code-part-5-special-apple.html):

```objc
    return [[NSSearchPathForDirectoriesInDomains(NSApplicationSupportDirectory,
        NSUserDomainMask, YES) objectAtIndex:0] 
        stringByAppendingPathComponent:[[NSProcessInfo processInfo]
        processName]];
```

A statement like this is not for everyone. Personally, when I'm starting to lose focus on the code after a few hours at the keyboard, I can't read this well. The visual hierarchy of the statement doesn't follow the structure it contains. A missing or redundant element could be hiding anywhere.

There is also a lack of interoperability with this approach. To anyone reading your code in a non-wrapping editor, the code is significantly less legible. For this reason code is sometimes formatted in the same way but hard-wrapped at 80 characters.

## Style 2: Left align all parameters at the same level

For the `myColor` creation statement that I showed earlier, left aligning all parameters would result in the following:

```objc
NSColor *myColor =
    [NSColor
        colorWithCalibratedRed:120.0/255.0
        green:120.0/255.0
        blue:120.0/255.0
        alpha:1.0];
```

### Advantages

Visual structure follows statement structure resulting in high readability. Highly effective for methods with long parameter lists. This approach is also sympathetic to common C and C++ code formatting styles.

Minor variations on this style are excellent for formatting structured inline data. i.e.

```objc
NSDictionary *myDictionary =
    [NSDictionary dictionaryWithObjectsAndKeys:
        [NSArray arrayWithObjects:
            [NSDictionary dictionaryWithObjectsAndKeys:
                @"value1", @"key1",
                @"value2", @"key2",
                @"value3", @"key3",
            nil],
        nil], @"keyForArray",
        @"topLevelValue1", @"topLevelKey1",
        @"topLevelValue2", @"topLevelKey2",
    nil];
```

### Disadvantages

Relative to soft-wrap in your text editor, this approach has a high code formatting and maintenance cost. There's a lot of tabs, returns and whitespace to type, delete and move.

Dogmatically applying this style to complexly structured statements can result in poor results. For example, the Pimp My Code sample rigourously formatted in this way:

```objc
    return
        [[NSSearchPathForDirectoriesInDomains(
                    NSApplicationSupportDirectory,
                    NSUserDomainMask,
                    YES)
                objectAtIndex:0] 
            stringByAppendingPathComponent:
                [[NSProcessInfo processInfo]
                    processName]];
```

## Style 3: Some left align, some decompose

A more balanced variation on the previous formatting, this approach makes the following changes:

- Decompose the self access/creation if it can't be performed on one line
- Only begin wrapping a sub-statement if it can't fit on its line
- Put the self component of the invocation on the same line as the assignment or return operator (optional)

The sample taken from Pimp My Code would now become:

```objc
    NSArray *searchPath = NSSearchPathForDirectoriesInDomains(
        NSApplicationSupportDirectory,
        NSUserDomainMask,
        YES);
    return [[searchPath objectAtIndex:0]
        stringByAppendingPathComponent:
            [[NSProcessInfo processInfo] processName]];
```

### Advantages

Handles compound statements better than dogmatic alignment of every single parameter yet retains much of the structural clarity. Decomposing self access, rather than wrapping it, makes the "subject" of the statement more clear.

### Disadvantages

Requires a few judgement calls to be made about when to decompose and when to begin wrapping a statement.

Can have the highest code-formatting maintenance requirements of the styles listed so far, since choosing to decompose or reintegrate elements is time-consuming.

## Style 4: Column alignment

This relates to various method invocation formatting styles which attempt to align columns of wrapped data within their lines, including alignment on the colon character:

```objc
      [object methodWithParam:theParam
                      another:theOtherValue
                    something:theSomethingValue
                         else:theElseValue];
```

From my perspective, I don't see people write this type of invocation much anymore, so it seems to me like an "old way of doing things". However the support is in Xcode to help you with this (Preferences-\>Indentation-\>Syntax Aware Indenting-\>":").

I've also seen the following style used:

```objc
    [someObject       instanceMethod:   parameter];
    [differentObject  otherMethod:      anotherParameter];
```

which is an attempt to tab-align every single component on the line.

### Advantages

If you are strongly particular about alignment, then maybe this is for you.

### Disadvantages

It is doubtful that the end-result in these cases justifies the effort to generate and maintain them. There is text editor support for some of these alignments but it still requires maintenance.

These approaches are also incompatible with any sub-statements that need to be wrapped and so require near-complete decomposition.

## Conclusion

If you look at my code, I clearly use something approximating "Style 3", with ad hoc variations depending on how I'm feeling. After years of working in offices with strict coding standards, it seems odd that I don't maintain greater attention to detail but there it is.

There are certainly times when I've considered changing my style to soft-wrapped. Reformatting code because you're changing a line or you decide it's unwieldy is annoying (although I doubt that it actually consumes as much time as it seems).

Soft-wrapped code also appears to be the direction that Apple are heading and they tend to drag a lot of Mac programmers along in their wake.

At this time, I don't find wrapped code to be a pleasing enough aesthetic, so I continue to endure the burden of formatting.
