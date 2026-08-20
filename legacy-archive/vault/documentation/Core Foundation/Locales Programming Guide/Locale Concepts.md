---
title: Locales Programming Guide
apple_id: 10000181i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-06-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFLocales/Articles/CFLocaleConcepts.html
archived_at: '2026-07-15T07:22:27.690013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Locales Programming Guide](Introduction%20to%20Locales.md)


[Next](Working%20With%20Core%20Foundation%20Locales.md)[Previous](Introduction%20to%20Locales.md)

# Locale Concepts

Some computational tasks require information about the current user context to be able to process data—particularly when formatting output for presentation to the user or when interpreting input. A locale object provides a repository for that information. An operation that requires a locale object to perform its task is called _locale-sensitive_.

A locale is not a language; it’s a set of conventions for handling written language text and various units (for example, date and time formats, currency used, and the decimal separator).

Conceptually, a locale identifies a specific user community—a group of users who have similar cultural and linguistic expectations for human-computer interaction (and the kinds of data they process). A locale’s _identifier_ is a label for a given set of settings. For example, “en” (representing “English”) is an identifier for a linguistic (and to some extent cultural) locale that includes (among others) Australia, Great Britain, and the United States. There are also specific regional locales for Australian English, British English, U.S. English, and so on.

Practically, a locale is a set of default settings for a given identifier: A given locale object is simply a collection of settings. In Core Foundation, locales are represented by instances of CFLocaleRef. In Cocoa, with OS X version 10.4 and later, locales are represented by instances of NSLocale.

In OS X the locale preference need not be the same as the language preference—they are set independently. Users choose their locale in System Preferences > International, using the Region pop-up menu in the Formats pane. You can programmatically retrieve the array of language preferences from System Preferences using the key `AppleLanguages`. You retrieve the locale preference using the key `AppleLocale`.

Note that it is also possible for users to specify their own preferences, which override the system-defined defaults for the chosen locale (see [Interaction Between Locales and Preferences](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2daljrgy2dkmbt)).

When you display data to a user it should be formatted according to the conventions of the user’s native country, region, or culture. Conversely, when users enter data, they may do so according to their own customs or preferences. Locale objects are used to provide information required to localize the presentation or interpretation of data. This information can include decimal separators, date formats, and units of measurement, as well as language and region information.

For example, by convention in the United States “7/4/76” represents the Bicentennial of the Declaration of Independence. However, in Great Britain, it represents the “7th of April, 1976”; in Thailand using the Thai Traditional Calendar it might represent “April 7th, 2519”; and in France it represents “7 avril 1976”. To take a more subtle example, in the United States“12.125” represents the decimal number twelve and one eighth, whereas in Germany it represents twelve thousand one hundred and twenty-five.

A locale’s _identifier_ is based on the naming convention defined by the International Components for Unicode (ICU). See [http://icu.sourceforge.net/userguide/locale.html](http://icu.sourceforge.net/userguide/locale.html) for information on their convention. The identifier consists of up to three pieces of ordered information: a _language code_, a _region code_, and a _variant code_.

- The language code is based on the ISO 639-x/IETF [BCP 47](http://www.rfc-editor.org/rfc/bcp/bcp47.txt) standard. ISO 639-1 defines two-character codes, such as “en” and “fr”, for the world’s most commonly used languages. If a two-letter ISO 639-1 code is not available, then ISO 639-2 three-letter identifiers are accepted as well, for example “haw” for Hawaiian. For more details, see [http://www.loc.gov/standards/iso639-2/php/English_list.php](http://www.loc.gov/standards/iso639-2/php/English_list.php).
- The region code is defined by ISO 3166-1 (see, for example, [http://www.iso.org/iso/country_codes/iso_3166_code_lists/english_country_names_and_code_elements.htm](http://www.iso.org/iso/country_codes/iso_3166_code_lists/english_country_names_and_code_elements.htm)). The region code is given in capital letters and appended, after an underscore, after the language code, for example “en_US”, “en_GB”, and “fr_FR”.
- The variant code is arbitrary and may have any number of keywords (which may be application-specific), each separated by an underscore. Developers are discouraged from using variant codes, as the format may change in the future.

Table 1 provides further examples.

__Table 1__  Components of a locale: language, country and variant

| Locale ID | Language | Country | Variant | Definition |
| es_PE | es | PE |  | Spanish, Peru |
| es_ES | es | ES |  | Spanish, Spain |
| es_ES_PREEURO | es | ES | PREEURO | Spanish, Spain prior to Euro support |
| kl_GL | kl | GL |  | Kalaallisut, Greenland |

Locale names such as “English”, “French”, and “Japanese” are deprecated in OS X and are supported solely for backward compatibility. The Script Manager and all its concepts are deprecated. CFLocale never uses old-style Script Manager codes (except for one compatibility function, [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes](https://developer.apple.com/documentation/corefoundation/1543446-cflocalecreatecanonicallocaleide)).

Note that you should typically have no reason to use locale identifiers directly in your code.

Locales are arranged in a hierarchy. At the root is the system locale, which provides default values for all settings. Below the root hierarchy are language locales. These encapsulate settings for language groups, such as English, German and Chinese (using identifiers “en”, “de”, and “zh”). Normal locales specify a language in a particular region (for example “en_GB”, “de_AT”, and “zh_SG”).

When you look up a value in a locale, the receiver itself will be searched first for a value specific to that locale. If the value is not found in that locale, its parent is searched, and so on, up to the root locale.

It is common to think of locales as providing information which is shared by a community of users. Every individual, however, may have their own preferences. To interpret input data from the current user, or to format data to display to the current user, you should use the user’s locale. You access the logical “user” locale for the current user using `CFLocaleCopyCurrent` (see [Locale for the Current User](Working%20With%20Core%20Foundation%20Locales.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dcljrgyztknbr)). This returns a locale object which represents the settings for the current user’s chosen system locale overlaid with any custom settings the user has specified in System Preferences.

There are four separate settings in International Preferences that involve language. The first three are set in the Languages tab, and the last is set in the Formats tab.

1. Primary language: affects user interface, used for other places where a \*language\* (not locale) preference is operative (e.g., Safari)
2. Collation (sort) order. This is set by default to match the primary language, but it can be overridden by the user. It only affects collation (localized string comparison).
3. Text break. This is set by default to match the primary language, but it can be overridden by the user. It only affects text boundary analysis (words, lines, and so on).
4. Region (Locale). This is set in Setup Assistant to combine the primary language at install time and the country specified in Setup Assistant. It can be changed by the user. If it doesn't match the primary language, the user gets a warning in the Languages tab.

Note that _only the setting in the Formats tab affects CFLocale properties_. The primary language has no influence on CFLocale properties—it only affects the user interface, not regional settings.

If a user should be able to specify their own settings for an application, the application can store those in the Preferences system (using the appropriate key). If the user updates their preferences (internally or externally to the application), these changes must be propagated through the application by synchronizing preferences and re-fetching Locale objects (see [Lifetime of Locale Objects](Working%20With%20Core%20Foundation%20Locales.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dcljrgy2dqnbu)).

[Next](Working%20With%20Core%20Foundation%20Locales.md)[Previous](Introduction%20to%20Locales.md)

