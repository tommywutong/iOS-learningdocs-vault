---
title: How can I determine the order of the languages set by the user in the Language
  tab of the International preference pane?
apple_id: DTS10004123
resource_type: QA
platform: macOS
topic: User Experience
technology: Foundation
published: '2006-12-19'
source_url: https://developer.apple.com/library/archive/qa/qa1391/_index.html
archived_at: '2026-07-18T02:30:30.353654Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1391

# How can I determine the order of the languages set by the user in the Language tab of the International preference pane?

## Q:  How can I determine the order of the languages set by the user in the Language tab of the International preference pane?

A: How can I determine the order of the languages set by the user in the Language tab of the International preference pane?

As documented at [Internationalization Programming Topics: Getting the Current Language and Locale](https://developer.apple.com/documentation/MacOSX/Conceptual/BPInternational/Articles/ChoosingLocalizations.html), most developers do not need to deal with the order of the languages as the appropriate localization will be chosen by the system automatically, and for a finer control, developers can use the CFBundle localization-related APIs.

But there may be situations where you want to get the list of languages directly from the user preferences.

The documentation explains how to retrieve this list with a Cocoa example:

__Listing 1__  Retrieving the languages in Cocoa (short).

```
NSUserDefaults * defaults = [NSUserDefaults standardUserDefaults]; NSArray * languages = [defaults objectForKey:@"AppleLanguages"]; NSLog(@"%@\n", languages);
```

which would return the following printout:

__Listing 2__  Languages printout.

```
(en, fr, de, es, it, nl, sv, nb, ja, "zh-Hans", da, fi, pt, "zh-Hant", ko, hu)
```

It may be worthwhile to note that the code could also have been written as:

__Listing 3__  Retrieving the languages in Cocoa (expanded).

```
NSUserDefaults * defaults = [NSUserDefaults standardUserDefaults]; NSDictionary * globalDomain = [defaults persistentDomainForName:@"NSGlobalDomain"]; NSArray * languages = [globalDomain objectForKey:@"AppleLanguages"]; NSLog(@"%@\n", languages);
```

Since the AppleLanguages key is in the global domain of the user defaults.

Since you cannot count on the data to be in canonical form, it is imperative that you use the CFLocale APIs to convert the entries of the AppleLanguages dictionary in canonical forms.

If you are building your code for Mac OS X v10.4 and later, you can use the `CFLocaleCreateCanonicalLanguageIdentifierFromString` API.

If you are building your code for Mac OS X v10.3 (Panther) and later, you can use the `CFLocaleCreateCanonicalLocaleIdentifierFromString` API.

If you are building your code for Mac OS X v10.2 (Jaguar) or earlier, you will have to use your own table mapping non-canonical forms to canonical forms.

In Terminal, you could obtain the exact same printout with:

__Listing 4__  Retrieving the languages in Terminal (expanded).

```
defaults read NSGlobalDomain AppleLanguages
```

or

__Listing 5__  Retrieving the languages in Terminal (short).

```
defaults read -g AppleLanguages
```


To retrieve this order of languages in Carbon you use:

__Listing 6__  Retrieving the languages in Carbon.

```
CFArrayRef languages = CFPreferencesCopyValue(          CFSTR("AppleLanguages"),          kCFPreferencesAnyApplication,          kCFPreferencesCurrentUser,          kCFPreferencesAnyHost); CFShow(languages);
```

which would printout:

__Listing 7__  Carbon Languages printout.

```
<CFArray 0x30a5d0 [0xa07ba150]>{type = immutable, count = 16, values = (     0 : <CFString 0x309b10 [0xa07ba150]>{contents = "en"}     1 : <CFString 0x30a4c0 [0xa07ba150]>{contents = "fr"}     2 : <CFString 0x30a4d0 [0xa07ba150]>{contents = "de"}     3 : <CFString 0x30a4e0 [0xa07ba150]>{contents = "es"}     4 : <CFString 0x30a4f0 [0xa07ba150]>{contents = "it"}     5 : <CFString 0x30a500 [0xa07ba150]>{contents = "nl"}     6 : <CFString 0x30a510 [0xa07ba150]>{contents = "sv"}     7 : <CFString 0x30a520 [0xa07ba150]>{contents = "nb"}     8 : <CFString 0x30a530 [0xa07ba150]>{contents = "ja"}     9 : <CFString 0x30a540 [0xa07ba150]>{contents = "zh-Hans"}     10 : <CFString 0x30a560 [0xa07ba150]>{contents = "da"}     11 : <CFString 0x30a570 [0xa07ba150]>{contents = "fi"}     12 : <CFString 0x30a580 [0xa07ba150]>{contents = "pt"}     13 : <CFString 0x30a590 [0xa07ba150]>{contents = "zh-Hant"}     14 : <CFString 0x30a5b0 [0xa07ba150]>{contents = "ko"}     15 : <CFString 0x30a5c0 [0xa07ba150]>{contents = "hu"} )}
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-12-19 | New document that retrieving the order of the languages set by the International preference pane in Cocoa, Carbon, and Terminal. |

