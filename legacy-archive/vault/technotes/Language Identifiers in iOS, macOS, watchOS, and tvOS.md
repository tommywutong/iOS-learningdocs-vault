---
title: Language Identifiers in iOS, macOS, watchOS, and tvOS
apple_id: DTS40016588
resource_type: Technical Note
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: Foundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/technotes/tn2418/_index.html
archived_at: '2026-07-26T19:54:15.047211Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2418

# Language Identifiers in iOS, macOS, watchOS, and tvOS

Language identifiers have changed in iOS 9, macOS Sierra, watchOS 3, and tvOS 10. This document describes what has changed and provides guidance for best practices to adapt to these changes.

[Language Identifiers in iOS, macOS, watchOS, and tvOS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjyhawugsbrfvgectshkvauork7jfcektsujfdesrksknpusts7jfhvgx27jvaugt2tl5pvoqkuinee6u27l5au4rc7krle6uy)[Matching Language Identifiers and Loading Localized Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjyhawugsbrfvgucvcdjbeu4r27jrau4r2vifdukx2jircu4vcjizeukustl5au4rc7jrhucrcjjzdv6tcpinauysk2ivcf6usfknhvkusdivjq)[For More Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjyhawugsbrfvde6us7jvhverk7jfhemt2sjvaviskpjy)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnjyhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Language Identifiers in iOS, macOS, watchOS, and tvOS

With iOS 9, the results returned by `Locale.preferredLanguages()` can differ from previous releases. In iOS 8 and earlier, only certain language, script, and region combinations were returned by this API. However, in iOS 9, more combinations of language, script, and region are permitted. This change is also applied to macOS Sierra, watchOS 3, and tvOS 10.

For example, when a user has configured their iOS device with language set to English and region set to India, `Locale.preferredLanguages()` will now return `[ "en-IN" ]`, instead of `[ "en" ]`. This allows for smarter language fallbacks; for this user, if an app doesn’t support `en-IN` as a localization, but does support `en-GB`, the fallback mechanism will select `en-GB` instead of `en`.

These implicit fallbacks are not always obvious from the language identifier; they are driven by locale data used by `Bundle`’s resource-loading mechanism. Trying to handle language identifiers manually, or performing string comparisons on them, will lead to problems. Instead, rely on `Bundle` APIs when loading resources or matching language identifiers to an available set of languages.

[Back to Top](#)

## Matching Language Identifiers and Loading Localized Resources

Resources loaded using `NSLocalizedString`, or directly using `localizedStringForKey` or other `Bundle` resource-loading methods, will automatically follow appropriate fallback logic.

If you need to load resources manually, such as from a custom or server-side source, note that you should still rely on `Bundle` for language matching to get consistent results. For example, if you have a set of available languages and you would like to know the best language to use from that set given the user’s preferences, you can use the logic described in Listing 1.

__Listing 1__  Preferred language lookup

```
let availableLanguages = [ "en", "en-GB", "en-US", "fr", "fr-CH", "de", "de-CH" ]
let bestMatchedLanguage = Bundle.preferredLocalizations(from: availableLanguages).first
```

In this example, if the user’s most preferred language was "`en-IN`" (Indian English), then `bestMatchedLanguage` would be "`en-GB`" (British English).

See Listing 2 for another example that demonstrates how Bundle handles non-trivial language fallbacks.

__Listing 2__  Additional lookup example

```
let availableLanguages = [ "en", "en-GB", "en-US", "zh-Hans", "zh-Hant" ]
let bestMatchedLanguage = Bundle.preferredLocalizations(from: availableLanguages).first
```

Here, if the user’s most preferred language was "`zh-HK`" (Traditional Chinese – Hong Kong), then `bestMatchedLanguage` would be "`zh-Hant`" (Traditional Chinese).

Note that `Bundle.preferredLocalizations(from:)` will restrict the results to localizations supported by `Bundle.mainBundle()`, or the return value of `Bundle.mainBundle().localizations()`. If you would like to match against a different set of language identifiers, use `Bundle.preferredLocalizations(from:forPreferences:)` which does not rely on `mainBundle`’s localizations and instead solely relies on the two arguments passed in.

[Back to Top](#)

## For More Information

For additional information about internationalization and localization, please see the [Internationalization and Localization Guide](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-08-16 | Updated to reflect the changes in the latest iOS, macOS, watchOS, and tvOS, and the changes in Swift 3 as well. |
| 2015-09-24 | Formatting updates. |
| 2015-09-18 | New document that describes the changes having to do with language identifiers in iOS, macOS, watchOS, and tvOS, and best practices for adapting. |

