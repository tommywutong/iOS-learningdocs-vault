---
title: The Minus Sign
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/02/minus-sign/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:457a9a8128dd294c'
translated: false
---

> 原文：[The Minus Sign](https://oleb.net/blog/2015/02/minus-sign/)　·　Ole Begemann

# The Minus Sign

## Don’t use a hyphen when you need a minus sign.

[Typographically correct punctuation](http://mislav.uniqpath.com/2012/01/special-chars/) is mostly about quotation marks, apostrophes, and dashes. But one thing that especially bugs me is when people use a standard [hyphen](https://en.wikipedia.org/wiki/Hyphen) (as in -5) where they should use a [minus sign](https://en.wikipedia.org/wiki/Plus_and_minus_signs#Minus_sign) (−5).

The hyphen key on your keyboard is actually called [hyphen-minus](https://en.wikipedia.org/wiki/Hyphen-minus) because in ASCII it was also used as the minus sign and for dashes. This character is still present in Unicode for compatibility reasons (its character code is U+002D), but Unicode also encodes the hyphen (‐, U+2010) and minus sign (−, U+2212) separately.

In all good-quality typefaces the minus sign is specifically designed to work well with digits. It has the same width as the plus sign and is also vertically aligned with the center of digits. It is because of this last point that the [en dash](https://en.wikipedia.org/wiki/Dash#En_dash)—though similar in width to the minus sign—is often a poor replacement.

# Using the Minus Sign With NSNumberFormatter

The default behavior of [`NSNumberFormatter`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSNumberFormatter_Class/index.html) is to use the hyphen-minus to format negative numbers. Considering that the class can be used not just for output formatting but also for parsing strings, this default makes sense. Almost every data interchange format (think JSON) uses the hyphen-minus to represent a minus sign.

But if you need to format negative numbers for display in your app, your text will look much more professional if you use the real minus sign. Fortunately, this is easy. All you need to do is create a string with the correct minus sign character and assign it to your number formatter’s `minusSign` property. In Swift:

```
let x = -5
let formatter = NSNumberFormatter()
formatter.minusSign = "\u{2212}" // U+2212 MINUS SIGN
let s = formatter.stringFromNumber(x)
```

In Objective-C, the escape sequence for the minus sign looks like this:

```
...
formatter.minusSign = @"\u2212"; // U+2212 MINUS SIGN
...
```

The difference is significant:

![Hyphen-minus vs. minus sign](https://oleb.net/media/hyphen-minus-vs-minus-sign.png)

<sub>Hyphen-minus vs. minus sign.</sub>
