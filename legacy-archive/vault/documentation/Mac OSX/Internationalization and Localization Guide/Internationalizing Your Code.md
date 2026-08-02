---
title: Internationalization and Localization Guide
apple_id: 10000171i
resource_type: Guide
platform: iOS|Xcode Developer Tools|macOS
topic: User Experience
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/InternationalizingYourCode/InternationalizingYourCode.html
archived_at: '2026-07-15T08:15:51.859973Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Internationalization and Localization Guide](About%20Internationalization%20and%20Localization.md)


[Next](Formatting%20Data%20Using%20the%20Locale%20Settings.md)[Previous](Internationalizing%20the%20User%20Interface.md)

# Internationalizing Your Code

In addition to internationalizing your user interface, write code that handles text in multiple languages. First store international text in strings files similar to the strings files used by base internationalization in [Internationalizing the User Interface](Internationalizing%20the%20User%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedglktk4zq). Also use language and locale-sensitive APIs for enumerating, searching, and sorting text in your code. Use standard text views for displaying and parsing text input as well. Let these APIs handle the complexity of different writing and input systems for you.

All user-facing text supplied by your app programmatically needs to be localized—that is, user-facing text that is not contained in `.storyboard` or `.xib` files, such as error messages, needs to be translated into the current language before it’s presented to the user. iOS and OS X provide a mechanism to retrieve localized text from strings files at runtime. In your code, replace strings containing user-facing text with the return value of an `NSLocalizedString` macro. When you export localizations, Xcode searches your code for the macros and includes the strings files in the exported localization file for translation. When you import localizations, Xcode adds the strings files, used by your code, to your Xcode project.

For example, instead of using the `@"26.22 miles"` string in your code, use:

```
NSLocalizedString(@"RunningDistance", @"distance for a marathon")
```

where `@"RunningDistance"` is the key for text that is retrieved from a localized strings file. The `@"distance for a marathon"` parameter is a comment about the key-value pair stored in the strings file as a hint to localizers. If you want different behavior, use one of the other `NSLocalizedString` macros that take more parameters, described in _Foundation Functions Reference_.

You don’t need to store all your key-value pairs in the same strings files. You can use other `NSLocalizedString` macros to create separate strings files and optionally, store them in different bundles. For more information on `NSLocalizedString` macros, read [String Resources](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6) in _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

To retrieve a localized string from a strings file, rather than adding it to a strings file, use the [localizedStringForKey:value:table:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/localizedStringForKey:value:table:) method in the [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) class. When the strings file corresponding to the specified table is not in your project, the `NSLocalizedString` macros and the [localizedStringForKey:value:table:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/localizedStringForKey:value:table:) method return the value parameter as the localized string.

Later, when you import localizations, as described in [Importing Localizations](Localizing%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk42a), the localized strings files are added to your project. (Alternatively, you can generate the development language strings files from `NSLocalizedString` macros directly, as described in [Creating Strings Files for User-Facing Text in Your Code](Managing%20Strings%20Files%20Yourself.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedcojnknltc).)

If your strings contain plurals of nouns or units of measurement, read [Handling Noun Plurals and Units of Measurement](Localizing%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk4yta) for how to extend this mechanism for languages that have different plural rules.

For all user-facing text, use string objects—instances of [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString), [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString), and their subclasses—that support Unicode. Unicode is a standard for encoding characters from all the world’s writing systems. String objects encapsulate a Unicode string encoded in UTF-16 format. What the user sees as a character may be represented and encoded as multiple characters in a Unicode string. Therefore, use string methods that manipulate composed character sequences, not individual characters in a string. Use the appropriate string APIs for iteration, searching, and sorting too. Use standard views and controls that display Unicode string objects correctly.

For comprehensive documentation on string objects, read _[String Programming Guide](../../Cocoa/String%20Programming%20Guide/Introduction%20to%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztk2i)_.

The [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) class handles the complexity of character encoding for you by allowing you to access character clusters or ranges. Use the [rangeOfComposedCharacterSequenceAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfComposedCharacterSequenceAtIndex:) and [rangeOfComposedCharacterSequencesForRange:](https://developer.apple.com/documentation/foundation/nsstring/1410993-rangeofcomposedcharactersequence) methods to ensure that you don’t split user characters in a string and break the text. These methods return a range within a string that represents the user character.

For example, Table 3-1 shows the numeric representation of user characters in UTF-16 and UTF-32 encoding. Note that the user characters have different lengths no matter what encoding format you use.

__Table 3-1__  Unicode Encoding of User Characters

| User Character | UTF-16 | UTF-32 |
| ../Art/chinese_string_table.svg | D85E DFFD | 27BFD |
| ../Art/korean_string_table.svg | 1100 1161 11A8 | 01100 01161 011A8 |

Enumerate strings by composed character sequence, word, sentence, or paragraph, not individual characters in a string. To enumerate a string by composed character sequence, use the [enumerateSubstringsInRange:options:usingBlock:](https://developer.apple.com/documentation/foundation/nsstring/1416774-enumeratesubstringsinrange) method and pass [NSStringEnumerationByComposedCharacterSequences](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1407290-bycomposedcharactersequences) as the options parameter. To enumerate a string by word (skipping over punctuation), pass [NSStringEnumerationByWords](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1407663-bywords) as the options parameter.

For example, if you pass [NSStringEnumerationByComposedCharacterSequences](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1407290-bycomposedcharactersequences) to the [enumerateSubstringsInRange:options:usingBlock:](https://developer.apple.com/documentation/foundation/nsstring/1416774-enumeratesubstringsinrange) method, it returns the user characters, as in the composed character sequences:

- ![../Art/chinese_string_table.svg](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Art/chinese_string_table.svg)
- ![../Art/korean_string_table.svg](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Art/korean_string_table.svg)

If the string is

- ![../Art/enumerating_strings.svg](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Art/enumerating_strings.svg)

and you pass [NSStringEnumerationByWords](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1407663-bywords) as the options parameter, the following words are returned:

- ![../Art/enumerating_word_1.svg](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Art/enumerating_word_1.svg)
- ![../Art/enumerating_word_2.svg](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Art/enumerating_word_2.svg)
- ![../Art/enumerating_word_3.svg](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Art/enumerating_word_3.svg)
- ![../Art/enumerating_word_4.svg](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Art/enumerating_word_4.svg)

Notice that spaces and punctuation are not included in the words.

To search the contents of a string or verify the presence of a string within a string using locale-sensitive comparison algorithms, use the [rangeOfString:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1417348-range) method, passing the current locale as the locale parameter. The constants you can combine and pass as the options parameter are:

**[NSCaseInsensitiveSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSCaseInsensitiveSearch)**
: Case-insensitive search. For example, `‘B’` is the same as `‘b’`.

**[NSDiacriticInsensitiveSearch](https://developer.apple.com/documentation/foundation/nsstring/compareoptions/1412313-diacriticinsensitive)**
: Ignores diacritic marks. For example, `‘ö’` is equal to `‘o’`.

**[NSBackwardsSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSBackwardsSearch)**
: Search backwards. (The default is forwards.)

**[NSAnchoredSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSAnchoredSearch)**
: Search at the starting point.

For example, if you are searching for user text in a string, pass the [NSCaseInsensitiveSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSCaseInsensitiveSearch) and [NSDiacriticInsensitiveSearch](https://developer.apple.com/documentation/foundation/nsstring/compareoptions/1412313-diacriticinsensitive) constants as the options parameter to the [rangeOfString:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1417348-range) method. Typically, searching text is a case and diacritic insensitive operation, but sorting text is case and diacritic sensitive.

For text you display to users, use locale-sensitive APIs for sorting and comparing strings. Different languages and regions have different sort order standards. For example, in French the diacritics are significant, and in English they are not. In some languages multiple letters are combined and affect the sort order.

To use the locale-sensitive comparison algorithms, use the [localizedStandardCompare:](https://developer.apple.com/documentation/foundation/nsstring/1409742-localizedstandardcompare) method which produces the same results as the Finder.

If you don’t want the same results as the Finder, use the [compare:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1414561-compare) method, passing the current locale as the locale parameter, or the [localizedCompare:](https://developer.apple.com/documentation/foundation/nsstring/1416999-localizedcompare) method.

Don’t use the [localizedCaseInsensitiveCompare:](https://developer.apple.com/documentation/foundation/nsstring/1417333-localizedcaseinsensitivecompare) method for sorting.

Use standard views and controls that handle the complexity of Unicode text layout and display for you. Characters in a string do not directly correspond to text rendered on the screen. What appears on the screen is a sequence of glyphs. A glyph is the smallest displayable unit in a font. A glyph may represent one character, more than one character, or part of a character. The mapping of characters to glyphs is not simple—it can be many-to-many. In addition, the order and position of glyphs in a line is complex. The standard views and controls even lay out bidirectional text properly for you—for example, the order of characters in a string containing an English word followed by a Hebrew word is not the same order used to lay out the text in a view, as described in [Handling Bidirectional Text](Supporting%20Right-to-Left%20Languages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedcnznknlti).

If you need to write custom display code, use the appropriate low-level text APIs. To learn about the text classes for iOS, read _[Text Programming Guide for iOS](../../Strings%20Text%20Fonts/Text%20Programming%20Guide%20for%20iOS/About%20Text%20Handling%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbs)_ and for Mac, read _[Text Layout Programming Guide](../../Cocoa/Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_.

The user might enter text in any language and format. iOS and OS X can recognize the language the user is typing and provide the appropriate keyboard options. If you are parsing text as the user enters it, keep in mind that there’s a many-to-many mapping from keyboard characters to language characters.

For some languages, the user doesn’t enter text one character at a time. That is, keys the user presses on a keyboard don’t necessarily correspond to characters in the language. In French, the user adds an accent at the insertion point by choosing it from a pop-up menu. In Japanese and Chinese languages, the user enters phonetic representations and selects a candidate from the candidate list to confirm the marked text. In both cases, preliminary text is inserted first and then converted to final text when the user confirms it.

To determine if the user confirmed marked text, send [markedTextRange](https://developer.apple.com/documentation/uikit/uitextinput/1614489-markedtextrange) to a text view. If this method returns an empty string, the user confirmed some entered text.

To get the language that the user is currently typing, use the [textInputMode](https://developer.apple.com/documentation/uikit/uiresponder/1621133-textinputmode) property in the [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) class, as in:

```
NSString *languageID = [[[UIApplication sharedApplication] textInputMode] primaryLanguage];
```

The returned string is a language ID, as described in [Language and Locale IDs](Language%20and%20Locale%20IDs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedcnjnknltc), that identifies a written language or dialect.

To get the set of languages that the user enables:

```
NSArray *languages = [[[UIApplication sharedApplication] textInputMode] activeInputModes];
```

where the returned array contains instances of the [UITextInputMode](https://developer.apple.com/documentation/uikit/uitextinputmode) class.

Worldwide, the format of personal names, mailing addresses, and phone numbers varies considerably. Personal names have many different formats including different ordering of the components. For example, in Asian countries, the family name is followed by the given name with no spaces between. The format of mailing addresses depends on the country. Phone numbers have different amounts of digits and punctuation between them. To handle varying input formats in your text views, use Interface Builder to add data detectors to your text views. A data detector identifies addresses and phone numbers in many different international formats and optionally turns them into links.

To detect this type of data in strings programmatically, read _[NSDataDetector Class Reference](https://developer.apple.com/documentation/foundation/nsdatadetector)_.

To get the language that the app is using from the main application bundle, use the [preferredLocalizations](https://developer.apple.com/documentation/foundation/nsbundle/1413220-preferredlocalizations) method in the [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) class:

```
NSString *languageID = [[NSBundle mainBundle] preferredLocalizations].firstObject;
```

[Next](Formatting%20Data%20Using%20the%20Locale%20Settings.md)[Previous](Internationalizing%20the%20User%20Interface.md)

