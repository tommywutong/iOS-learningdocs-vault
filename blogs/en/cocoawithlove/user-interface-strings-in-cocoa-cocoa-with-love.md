---
title: 'User interface strings in Cocoa | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/04/user-interface-strings-in-cocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:297591de494727d7'
translated: false
---

> 原文：[User interface strings in Cocoa | Cocoa with Love](https://www.cocoawithlove.com/2011/04/user-interface-strings-in-cocoa.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I'll look at best practice for using and managing text strings in your user interface. This is a fairly simple topic but Cocoa has established "best practices" for handling user interface strings that new Cocoa developers should be aware of. Since it is inevitably related, I'll also look at the steps involved in localizing the strings in your applications but remember: you should follow good practice for string handling, even if you have no intention of ever translating your application.

## Introduction (the wrong way)

Putting a text string in your user interface is not a difficult thing to do on a technical level. In code, filling in text can be as simple as setting the `text` property of a `UILabel` to a literal string:

```objc
someUserInterfaceLabel.text = @"Text to display";
```

(This code is for an iOS `UILabel`. On Mac OS X, you would set the `stringValue` property of an `NSTextField` but otherwise the step is the same.)

While this will work, you should never set a user interface string this way.

## Setting labels with literal strings (the right way)

The most thorough way to put a literal string into your Cocoa application's user interface is:

```objc
someUserInterfaceLabel.text =
    NSLocalizedStringFromTable(
        @"Text to display",       // the native language string
        @"SomePageLabels",        // the category
        @"Label display string"); // a comment describing context
```

This is pretty verbose though. It is often okay to just use:

```objc
someUserInterfaceLabel.text = NSLocalizedString(@"Text to display", nil);
```

If you take no other steps, this will produce exact the same output as the "wrong way" example.

You should _always_ use the `NSLocalizedString`[...] macros for _every_ user interface string in your code.

But wait... this `NSLocalizedString`[...] stuff requires more typing and unless you take yet more additional steps, it won't have any functional difference? If I'm not planning to translate my program right now, aren't they a complete waste of time?

## Why NSLocalizedString is important, even if you don't intend to translate

Obviously, the `NSLocalizedString`[...] functions (and the less common `CFCopyLocalizedString`[...] variants) are functions that exist to enable localization (i.e. letting you translate your application into different languages).

Technically, they're not even functions — they're just macros that invoke the `-[NSBundle localizedStringForKey:value:table:]` method — but you should always use the macro and not the underlying method for reasons I'll discuss in the "Mechanics of Translation" section below.

However, even if you're not intending to ever localize your application, you should _always_ use `NSLocalizedString`.

There are a few reasons for this:

1. : The future is hard to predict: you never know if you'll want to translate in the future. Needing to go through your code and find rogue literal strings is time consuming and prone to mistakes. Instead, everything should always have

  from the beginning.
2. : It keeps the exact details of your model/presentation layer at least one level of indirection removed from your controller code. In some cases, you can simply change the .strings files for your program to update the user interface and not need to change code due to this separation.
3. : It clearly identifies text strings intended for user presentation as opposed to text strings used as keys for programming use only.
4. : with your user interface strings detached from your controller, you'll be less likely to try to read static strings back from the user interface (a very bad idea) or place programmer-targetted strings in the user-interface.

Get into the habit of using `NSLocalizedString`. It's really simple to do — even when you're hacking code together quickly, you should be able to use it.

The first two points in the previous list are self-explanatory but the second two merit further explanation.

### Separation of concerns

It is always helpful in programming to be able to glance at code and understand the intent. Consider the following piece of code in isolation:

```objc
[someDictionary setObject:@"value" forKey:SomeKeyNameString];
[someDictionary setObject:NSLocalizedString(@"value", nil) forKey:SomeOtherKeyNameString];
```

Without knowing what `someDictionary` is for or what the purpose of the `SomeKeyNameString` and `SomeOtherKeyNameString` values are, we know that the second string is intended for display in the user interface at some point whereas the first string is purely for tracking a value internally.

This clear labelling of intent is helpful as strings for user display have a very different role in a program compared to strings for internal use.

### Discourages other bad practices

If you treat `NSLocalizedString` in your mind as though its output is a black box, this can help you avoid poor controller design when managing user interface elements. It can act as a conceptual tool to encourage you to design things the right way, instead of a lazy way.

Your controller code should treat user interface strings as something that can be written but not read. Reading static strings back from the user interface is always bad (it ends up being a form of "[common or data coupling](http://en.wikipedia.org/wiki/Coupling_(computer_programming))" — a bad design practice).

In the "Separation of concerns" example above, you might consider that since the keys `SomeKeyNameString` and `SomeOtherKeyNameString` are defined in global variables in this example, that perhaps you'd want to define your localized strings in global variables. In most cases a global variable for a user string is actually a bad idea.

We define dictionary keys in global variables because more than one location in the program may need to use exact the same value or the exchange of information between the two points will fail. But with user interface strings, you should never have a second piece of code that requires the exact same value: you should never read back from the user interface or require user interface collusion. Generally, the only situation where the same string should appear multiple times is if the same user interface code is displaying it (i.e. you're drawing the same object) but in this case, the code is common and the string should only need to appear once in the code.

If you need to uniquely identify a label or the state of a text displaying item, testing the text it contains is the wrong way to do that. A far better way is to use the `tag` value of any `UIView`/`NSActionCell` and then map the `tag` value onto the object's role or function (`tag` is a pointer sized value so you can store a non-retained object reference here if needed, not just an integer). The `tag` property is not reserved for any other purpose; it is intended for the controller to track user interface items and their state.

## Mechanics of translation (when you're ready)

Eventually, you may actually have to translate your program. Let's look at the steps involved.

### Create your ".strings" files

The files you need to translate are the ".strings" files in your application. By default though, your project probably won't have any ".strings" files (except possibly an InfoPlist.strings file which is for translating your Info.plist file's strings).

The first step is to make sure you have a localized directory somewhere (probably in the Resources subdirectory of your project's folder). The localized directory should be named "en.lproj" if you're starting with English strings, otherwise you'll want to replace "en" with the appropriate ISO 639-1 or ISO 639-2 designators. If needed you can use the script and region identifiers too as described in [Apple's Language and Locale Designations](http://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPInternational/Articles/LanguageDesignations.html).

A note on folder names: it is common to see "English.lproj" used as the name for English localization instead of "en.lproj" — in fact, Xcode 3 still generates folders with this name if you Get Info on a file and select "Make file localizable". Apple have stated that these old, "full" names are deprecated from Mac OS X 10.4 onwards in favor of ISO 639-1 or ISO 639-2 designators. Don't use the old "English.proj" style names anymore and replace with "en.lproj" if it is autocreated (yes, you might need to update your Xcode paths if you change the folder name).

Now we can create ".strings" files automatically from all the `NSLocalizedString` references in your program. To do this, open a Terminal in your Project's root directory and run the following command:

```objc
find -E . -iregex '.*\.(m|h|mm)$' -print0 | xargs -0 genstrings -a -o Resources/en.lproj
```

This will process all .m, .h and .mm files in your directory hierarchy and create ".strings" files for them in the en.lproj directory (note, the en.lproj directory must already exist). This assumes that the localized resources directory you created is located at "Resources/en.proj", relative to your Project's root directory; obviously, you'll need to change this if your localized resources are elsewhere.

The ".strings" file will be filled with entries that look like this:

```objc
/* This comment provided comes from the last parameter of the NSLocalizedString macro. */
"Some UI string %@ to translate %@" = "Some UI string %1$@ to translate %2$@";
```

Your translator just needs to translate the right-hand side of the equality statement. Notice that placeholders in your strings are given ordinal positions (1 and 2 in this case) so that the translation can change the order of placeholders if necessary (obviously, if you use placeholders, you should include a comment that explains what they're going to be).

> generally, the whole process of creating new language variants is referred to as localization. In reality though, it comprises two steps:
> 
> 1. : where you decouple the program from the original locale
> 2. : where you add translations and behaviors for each new locale
> 
> By that terminology, the inclusion of
> 
> wrappers and the creation of ".strings" files is the "Internationalizing" phase.

### genstrings will only handle static NSLocalizedString and CFCopyLocalizedString strings

The only strings that will be automatically extracted are those wrapped in `NSLocalizedString`[...] and `CFCopyLocalizedString`[...] macros. Obviously, all your user interface text needs to be wrapped in these but also remember that the underlying `-[NSBundle localizedStringForKey:value:table:]` method will _not_ be automatically extracted.

Why would you ever use `-[NSBundle localizedStringForKey:value:table:]` directly then? The answer is for dynamically generated strings.

The genstrings command will raise an error if it detects anything other than a static string in the localization macros. This is appropriate because you don't want your translators translating variable names and function calls (they only need to translate the results of those calls).

The answer to why you would use `-[NSBundle localizedStringForKey:value:table:]` is then: the actual strings to be translated are located elsewhere in the code (or are in a ".strings" file that was not generated from code) and you are simply looking them up dynamically.

## Encoding problems

From Mac OS X 10.5 onwards, you can put any UTF-8 characters in your `NSLocalizedString` constants. Prior to this, they were required to be pure 7-bit ASCII with all Unicode escaped with \\\\Uxxxx style escaping or you could use MacRoman with the -macRoman command-line option to use MacRoman high-ASCII characters.

> : UTF-8 has been around since 1993 and Unicode 2.0 since 1996; if you have created any 8-bit character content since 1996 in anything other than UTF-8, then I hate you.
> 
> I weep to think of the years of programmer time that are still wasted attempting to support non-Unicode formats without characters getting garbled because people are still creating content using ancient encodings without useful identifiers to indicate what nonsense encoding they're using (or worse, people creating content that explicitly uses the wrong encoding for an encoding-specific text field).
> 
> MacRoman? Atrocious. Big-5? I hope you want to see garbage output. Windows Latin? You suck. If you're creating new content using anything other than UTF-8, UTF-16 or UTF-32 then you should be forced to serve prison time with whatever idiot monkey decided that UTF-16 should be allowed little-endian and big-endian variants instead of a single authoritative encoding.

The actual text files generated by genstrings are UTF-16 in whatever byte order your system happens to use. i.e. UTF-16BE on PowerPC and UTF-16LE on Intel Macs.

Grumble.

## Translating XIB files

Not all your strings will come from your code. The other common text location is in XIB files. XIB files can be a little bit trickier than strings in code due to two factors:

1. While you can extract the strings from a XIB file easily, you also have to merge them back in once the translation is complete — basically another step that can go wrong
2. The ".strings" file format extracted from XIB files is uglier and doesn't have easy room for comments to send to the translator

For these two reasons, I generally avoid putting text in XIB files if reasonably possible — it is normally easier to have text inserted at NIB load time by the code. Of course, menus, button labels and automator labels can't reasonably be moved into code so you're still likely to need a number of XIB files translated.

You extract the .strings from XIB files in a similar way to extracting the strings from code. However, first we must make all of our XIB files localizable (if they aren't already).

To localize your XIB files, select them all in the Xcode project Group Tree, Get Info on them and then from the first tab, select "Make file localizable".

Then, go to the localized directory where your files all ended up (if there's multiple, you'll need to do this for each one) and run the following in Terminal:

```objc
for file in *.xib; do
    ibtool --export-strings-file "$file".strings "$file"
done
```

This will generate all the ".strings" files for your XIB files.

Once the ".strings" files are localized, create a new ".lproj" directory with the appropriate language name for the new translations and put all the ".strings" files in it. Then open a Terminal in this new folder and run:

```objc
for file in *.xib.strings; do
    basename=`basename "$file" .strings`
    ibtool --strings-file "$file" --write "$basename" "../en.lproj/$basename"
done
```

This will merge all the ".xib.strings" files in the current directory with the XIB files from the en.lproj directory, creating the translated XIB files.

## Translating other resources

The same "Make file localizable" step that we used for the XIB files in the previous section can be applied to any resource file in your Xcode group tree so you can localize other resources in whatever way is apppropriate.

Here's a tip though: avoid localizing anything other than strings and XIB files by whatever means possible. Having non-strings files for translation will cause you nothing but pain and suffering.

In particular: **avoid localizing images**. Work as hard as you can to keep all text out of images (except in logos that don't require translation). You can perform quite sophisticated drawing and text handling in Cocoa code if needed and this will almost always be easier than localizing images.

I haven't really touched on non-string code localization topics in this post. There's date, time, numbers, error descriptions and other stuff — most of the time, the classes and APIs for these make it clear what you need to do. Just read [Apple's Internationalization documentation](http://developer.apple.com/library/mac/#documentation/MacOSX/Conceptual/BPInternational/BPInternational.html%23//apple_ref/doc/uid/10000171-SW1).

## Conclusion

Most programmers should already know the information in this post. Numerous other Mac programming blogs have discussed the topic:

- Call Me Fishmeal: Pimp My Code, Part 17: Lost in Translations.
- OS X & Cocoa Writings: Internationalizing Cocoa Applications, by Andrew C Stone
- Internationalizing Cocoa applications, mmalcolm Crawford

See how anciently old those second two links are? I'm not telling you new information. The advice remains the same: always, _ALWAYS_ use `NSLocalizedString` for your user interface strings.

Actual translation can happen later or not at all — my point is that your need for translation (or lack of need) should not determine whether you use `NSLocalizedString` as it is best practice in any case. Of course you can rest assured that translation will all work out if your code is already `NSLocalizedString`-compliant.
