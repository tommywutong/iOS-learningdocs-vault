---
title: Keyboard Adventures
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2012/04/Keyboard-Adventures/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:03ca322516095c3a'
translated: false
---

> 原文：[Keyboard Adventures](https://belkadan.com/blog/2012/04/Keyboard-Adventures/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« ["Little Big Details"](https://belkadan.com/blog/2011/08/Little-Big-Details/)

[Git Tricks](https://belkadan.com/blog/2012/10/Git-Tricks/) »

« [rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=mac-os-x)

[quasiquarantine](https://belkadan.com/blog/2019/12/Quasiquarantine/?tag=mac-os-x) »

## [Keyboard Adventures](#)

The best utility for making custom keyboard layouts on Mac OS X has long been [Ukelele](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ukelele) (sic). Sure, Apple came up with an [XML format](https://developer.apple.com/library/mac/technotes/tn2056) for keyboard layouts, but when you want a variant of an existing keyboard, it’s a lot easier to just _copy the existing keyboard_ in Ukelele and modify the keys you want to change.

A few years ago I took a class on Phonetics and Phonology, and found myself needing to type in [IPA](http://en.wikipedia.org/wiki/International_Phonetic_Alphabet) quite often. So I fired up Ukelele and made a copy of the standard Dvorak keyboard and got to work. I didn’t change any of the regular keys, but I added a number of IPA characters for when you hold Option, and turned my numpad into an approximation of the human vowel space.

![My keyboard layout when the option key is down](https://belkadan.com/blog/2012/04/Keyboard-Adventures/dvorak-ipa.png) ![](https://belkadan.com/blog/2012/04/Keyboard-Adventures/dvorak.png)

_(mouse over if you’ve forgotten what regular Dvorak looks like)_

What are all those orange keys? Those are _[dead keys](http://en.wikipedia.org/wiki/Dead_key),_ usually used to make accented characters and co-opted by me for typing characters linguistically similar to the first one.[1](#fn:example) Ukelele can handle these as well.

To use your custom keyboard, just save the `keylayout` file from Ukelele in a “Keyboard Layouts” folder inside your Library folder. You can even give your keyboard an icon for the menu bar switcher by putting a 16x16 icon file in the folder, as long as it’s in ICNS format and has the same name as the layout file.

All that was good enough for me until Mac OS X Lion came around.

### Press and Hold

When Lion came out, there was a new feature, clearly inspired by iOS: the ability to hold a key for a bit and get a [popover](https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/AppleHIGuidelines/Windows/Windows.html#//apple_ref/doc/uid/20000961-SW4) of variants. This generated quite a bit of outcry from a number of people who apparently need to type repeated letters a lot. I, on the other hand, think it’s a pretty cool feature.

![Variations on "e", in TextEdit](https://belkadan.com/blog/2012/04/Keyboard-Adventures/press-and-hold.png)

It’d be really nice to have configurable press-and-hold options in the same way that we have configurable keyboard layouts with configurable dead keys, right? Having taken a year of Mandarin Chinese, it might be useful if, say, the first four variants of “e” corresponded to the four tones in Mandarin. But there’s nowhere in the `keylayout` spec that includes this feature.

Fortunately, [someone’s already solved this problem](http://apple.stackexchange.com/a/44928). For maybe 95% of the world, Lri’s solution is good enough: it works, and it’s fairly extensible. There was just one problem: my custom Dvorak IPA keyboard layout wasn’t getting the press-and-hold popover at all.

### The Text Input System

The OS X text input system is a complicated beast, but then again text input is pretty complicated in and of itself. Keyboard layouts are well and good for many alphabetic languages, but for something like Japanese or Chinese you need a bit more power. For this, there are programs called _[input methods](https://developer.apple.com/library/mac/#releasenotes/Cocoa/RN-InputMethodKit/_index.html),_ which handle, say, the translation from Latin characters to Chinese ones with the corresponding Mandarin pronunciation.[2](#fn:palettes)

The press-and-hold feature is implemented as an input method that listens for held-down key events. Unlike the Japanese or Chinese input methods, the press-and-hold feature is not exclusive, and does not appear in the input menu. Other than that, though, the text input system treats it like any other input method, and in theory you could write my own input method that did exactly the same thing. (More on this later…)

Underneath the nice interface for writing input methods is the [Text Input Source Services](https://developer.apple.com/library/mac/#documentation/TextFonts/Reference/TextInputSourcesReference/Reference/reference.html) layer. This is a CoreFoundation-compatible C API for the text input system — essentially a programmatic interface to the input menu. That means it has to handle both the complex input methods like Japanese and the humble keyboard layouts for QWERTY, Dvorak, and my “Dvorak IPA”.

In order to bring the `keylayout` files in line with the way OS X plugins are structured, and more importantly to make them localizable, there’s a second way to provide keyboard layouts to the text input system: bundles containing `keylayout` files. This is also described [alongside the XML format](https://developer.apple.com/library/mac/technotes/tn2056), and shows a pretty standard bundle layout. The main benefit is being able to provide a `strings` file for the localized keyboard names, but there’s also the added effects of having the icon and the keyboard layout in a single package, and being able to distribute multiple keyboard layouts together if you want.

None of that was going to solve my problem, though. It wasn’t until I looked in the actual header file for the Text Input Source Services that I discovered there was more to writing keyboard layouts, or for that matter input methods, than existed in Apple’s online documentation. Specifically:

> For Leopard, there are two new keys for use in plists to provide information that supports the Text Input Sources functions above (these keys will be ignored in earlier systems):
> 
> `"TISInputSourceID"` - a key to specify the InputSourceID, a reverse-DNS-style string meant to uniquely identify any input source. If this key is not specified, the Text Input Sources functions will attempt to construct an InputSourceID from other information.
> 
> `"TISIntendedLanguage"` - a key to specify the primary language which the input source is intended to input. If there is none - as with the Unicode Hex Input key layout, for example - this key need not be specified. The language is indicated by a string in in the format described by [BCP 47](http://en.wikipedia.org/wiki/IETF_language_tag) (the successor to RFC 3066).

> In the Info.plist file, the value for the `CFBundleIdentifier` key must be a string that includes `".keyboardlayout."`; typically this might be something like `"com.companyname.keyboardlayout.MyKeyboardLayouts"`. (Before Leopard, it was required to be a string that began `"com.apple.keyboardlayout"`, even for keyboard layouts not supplied by Apple).

> A dictionary of properties for each key layout in the bundle should be provided using a key of the form `"KLInfo_`_keylayoutname_`"` (even if _keylayoutname_ includes spaces or punctuation). This dictionary is where to specify the keys `"TISInputSourceID"` and `"TISIntendedLanguage"` and their associated values.
> 
> `"TISInputSourceID"` note: For keyboard layouts this should typically be something like `"com.companyname.keylayout.`_keylayoutname_``”`. If this key is not specified, an InputSourceID will be constructed by combining _bundleID_ + `“.keylayout.”` + _keylayoutname_.
> 
> If the keyboard layouts in the above example were intended to input Azerbaijani in Latin script, then the Info.plist entries could be:
> 
> ```
> <key>KLInfo_MyLayoutOne</key>
> <dict>
>   <key>TISInputSourceID</key>
>   <string>com.companyname.keylayout.MyLayoutOne</string>
>   <key>TISIntendedLanguage</key>
>   <string>az-Latn</string>
> </dict>
> <key>KLInfo_MyLayoutTwo</key>
> <dict>
>   <key>TISInputSourceID</key>
>   <string>com.companyname.keylayout.MyLayoutTwo</string>
>   <key>TISIntendedLanguage</key>
>   <string>az-Latn</string>
> </dict>
> ```

_Cocoa programmers will probably be smirking at the Text Input Source Services’ abuse of Info.plist: it’s not that this information shouldn’t be here, but that it shouldn’t use *prefixed* keys. The usual way to do this is an array of dictionaries with a `"name"` key of some kind. Also, the keyboard names are localized in InfoPlist.strings, which is supposed to only be for data in Info.plist._

There is more information on how input methods use these keys, but the main point is that this information isn’t available _anywhere_ online. And though Ukelele now has an option to save in bundle format, it doesn’t have a way to set the magic language key — which, it turns out, is the key to getting the press-and-hold feature to work with custom keyboard layouts. By manually editing the Info.plist file and specifying that my keyboard had an intended language of `"en"`, then logging out and back in, I got exactly what I wanted: press-and-hold accents in Dvorak IPA mode.

I’m planning to send an e-mail to the developer of Ukelele to add this feature, and I’ve filed [rdar](rdar://problem/11327265)://[11327265](http://openradar.appspot.com/11327265) with Apple about the lack of documentation here. Meanwhile, I’ve copied the relevant parts of the headers here in the hopes that it’ll show up on [search engine] next time someone has this problem.

### Custom Press and Hold

So, this ought to be enough, right? I managed to get the accents popover to show up for my custom keyboard layout, and I know how to change the set of variants. If I was just interested in that, I’d be done, right?

…Except I don’t really like messing with system files, especially not ones in the /System folder that you’re really not supposed to touch. Because system apps and plugins are [signed](http://en.wikipedia.org/wiki/Code_signing) now, modifying resources inside PressAndHold.app could disable the feature altogether. (Clearly it doesn’t right now, but that could change.) On a more practical note, any system update that touches PressAndHold.app could overwrite your changes, which is at least a bit annoying.

I said before that it’s possible to write your own input method that does everything PressAndHold.app does. But…

That comes from the developer of [SIMBL](http://www.culater.net/software/SIMBL/SIMBL.php), a program specifically designed for injecting code into existing OS X applications. While this can be a HUGE security risk, it’s also what allows me to build a plugin like [Keystone](http://belkadan.com/keystone/) that runs inside Safari. In this case, I decided to make a plugin that ran inside PressAndHold.app. In a fit of grandeur I called it MagicPressAndHold.

The actual implementation of that plug-in wasn’t so hard. Using the [`class-dump`](http://www.codethecode.com/projects/class-dump/) utility (and, uh, breaking Apple’s Terms of Service a bit), I found that there’s a single method that serves as the entry point for accented character suggestions: `-accentsStringForString:language:`. So I just had to inject my own implementation of that method to gain control over the set of variant characters.

The above uses explicit \<code\>\</code\> tags so that the text inside is still valid for abbreviations. Yay for Kramdown.

I ran into a slight snag because PressAndHold.app doesn’t run like a normal Mac OS X application. Instead, it’s launched by the text input system as necessary and doesn’t show up in NSWorkspace’s usual “application launched” notifications. That means SIMBL doesn’t get a chance to look at it. Manually sending SIMBL’s “please load me” AppleEvent to PressAndHold.app did the trick.

```
tell application "PressAndHold" to inject SIMBL into Snow Leopard
```

And it worked!

![The variants for "i" match the four tones of Mandarin Chinese.](https://belkadan.com/blog/2012/04/Keyboard-Adventures/magic-press-and-hold.png)

Of course, this isn’t so useful yet. There’s no preferences UI, and it isn’t automatically loaded. But it’s a working proof-of-concept, and the code is [available on GitHub](https://github.com/belkadan/MagicPressAndHold).

### Postscript: Chronology

The progression from “custom keyboard layout” to “hacking into a system plugin for the text input system” may have seemed pretty overwhelming already, but the true story is even less of a straight line. In truth, I first heard about the press-and-hold feature when everyone started complaining about it. Like I said, when I first upgraded to Lion myself, I thought it was pretty cool.

Then I spent months never using it, and not just because I was on a custom keyboard layout. I just forgot about it.

A few days ago I came across it again on someone’s blog, made it to the [StackOverflow post](http://apple.stackexchange.com/a/44928) I mentioned already, and found about about PressAndHold.app. What was different about my custom keyboard layout from Apple’s? Unfortunately, Apple’s keyboard layouts aren’t stored in a user-readable format anymore, so I couldn’t do much more than check the output of Ukelele. I tried saying my keyboard layout was a Roman keyboard instead of Unicode, but that had no effect. I tried using a bundle instead of just the `keylayout` file, but _that_ had no effect. So I started hacking into PressAndHold.app to try to figure out what was going on.

(That was fun. Pro tip: don’t attach a text-based debugger to a text input method — you lose all ability to type after a few seconds. Not sure why the delay.)

I started hacking together MagicPressAndHold, taking my usual approach of simply logging arguments and return values in the methods I wanted to edit. In this case, that was `-accentsStringForString:language:`…and I noticed that my Dvorak IPA keyboard layout had no language (an empty string). What was up with that?

I sort of took it for granted at first that `keylayout` files can’t have associated languages, since there’s nothing in the XML file that indicates a language. So my first pass was to [assume the system language](https://github.com/belkadan/MagicPressAndHold/commit/6ef2d2d2680068e79d3443d06f46795cd4c5401e) if there isn’t one associated with the keyboard, and _that worked._

Why continue? Well, it was an accident. I started looking ahead to how I could have the variant characters be different depending on which keyboard was active. And the way you find out which keyboard is active is by using the Text Input Source Services.

And _that’s_ where the “secret” language keys are documented. So after getting MagicPressAndHold in a working state, I backtracked to my keyboard layout bundle, trying a number of experiments in the configuration. What I didn’t realize is that most of them don’t take effect unless you log out and back in again, but the simplest thing—a `TISIntendedLanguage` of `"en"`—did work in the end.

And MagicPressAndHold? Well, without a good way to inject itself into PressAndHold (which quits after not being used for a while, and launches again on demand), it’s probably going to remain an experiment, and I don’t plan to do any serious work on it.

1. For example, typing Option-R gives me retroflex variants of /t/, /d/, and /s/. [↩︎](#fnref:example)
2. There are actually _two_ other kinds of input to the Cocoa text system: “ink” inputs, which allow you to, say, _draw_ a Chinese character instead of typing its Romanization, and “palette” inputs, which include the Keyboard Viewer and Character Picker palettes. You can create these too, but that’s beyond the scope of this post. [↩︎](#fnref:palettes)

This entry was posted on [April](https://belkadan.com/blog/2012/04) 26, [2012](https://belkadan.com/blog/2012) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Text](https://belkadan.com/blog/tags/text)
