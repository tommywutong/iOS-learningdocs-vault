---
title: Locales Programming Guide
apple_id: 10000181i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-06-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFLocales/Articles/CFLocaleWorking.html
archived_at: '2026-07-15T07:22:28.198273Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Locales Programming Guide](Introduction%20to%20Locales.md)


[Next](Document%20Revision%20History.md)[Previous](Locale%20Concepts.md)

# Working With Core Foundation Locales

In Core Foundation, locales are represented by instances of CFLocale. You generally use the locale object for the current user, rather than for a specific locale, and typically in conjunction with other objects, usually formatters. Locale objects are currently immutable. It is important to understand the interaction between locales and the Preferences system.

Typically you want to format or interpret information for the current user. You generally therefore use the user’s locale, which you access with `CFLocaleCopyCurrent` (see [Locale for the Current User](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dcljrgyztknbr)). Sometimes, however, you may need to display information formatted for a particular locale, independently of the user’s preference.

You can create a locale object for a specific locale with `CFLocaleCreate` by supplying the suitable identifier (see [Locale Naming Conventions](Locale%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2daljrgy2dinbw)).

```
CFStringRef localeIdent = CFSTR("fr_FR");
CFLocaleRef localeRef = CFLocaleCreate(kCFAllocatorDefault, localeIdent);
```

To ensure that you have the appropriate representation for a locale’s identifier, you should use `CFLocaleCreateCanonicalLocaleIdentifierFromString` to create the canonical form—this function is especially useful for dealing with legacy information.

```
CFStringRef localeIdent = CFSTR("French");
CFStringRef stringRef =
    CFLocaleCreateCanonicalLocaleIdentifierFromString(kCFAllocatorDefault,
    localeIdent);
CFLocaleRef localeRef = CFLocaleCreate(kCFAllocatorDefault, stringRef);
```

There is no guarantee that information exists for the locale you specify. The following example creates a valid locale object (for the Thai language, country US). OS X does not, however, provide specific data for this locale, so it will fall back first to “th” (Thai language), then to the root locale (see [Locale Hierarchies](Locale%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2daljrgy2dqnzx)).

```
CFStringRef localeIdent = CFSTR("th_US");
CFLocaleRef localeRef = CFLocaleCreate(kCFAllocatorDefault, localeIdent);
```

The system default settings are available from the root locale using [CFLocaleGetSystem](https://developer.apple.com/documentation/corefoundation/1543257-cflocalegetsystem). This function provides default values for all settings for all locales (see [Locale Hierarchies](Locale%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2daljrgy2dqnzx)).

Although a locale specifies defaults for a given language or region, individual users may specify their own settings, which override those for their chosen locale. OS X provides locale objects that represent the settings for the current user’s chosen system locale overlaid with any custom settings the user has specified. You access the logical user locale for the current user using [CFLocaleCopyCurrent](https://developer.apple.com/documentation/corefoundation/1542508-cflocalecopycurrent).

Even though settings for a user’s locale may differ from those of the system defaults, the identifier for the two may be the same. For example, a user may choose British English as their language preference but specify custom date and time formatters. The following code sample illustrates a case where even though the formatters for the user and system locales are different, the locales’ identifiers are the same.

```
systemLocaleRef = CFLocaleCreate(kCFAllocatorDefault, CFSTR("en_GB"));
// created "default" localeRef for "en_GB"
dateFormatter = CFDateFormatterCreate(kCFAllocatorDefault, systemLocaleRef, kCFDateFormatterLongStyle, kCFDateFormatterMediumStyle);
CFShow(CFDateFormatterGetFormat(dateFormatter));
// output "d MMMM yyyy HH:mm:ss"
userLocaleRef = CFLocaleCopyCurrent();
CFShow(CFLocaleGetIdentifier(userLocaleRef));
// output "en_GB"
dateFormatter = CFDateFormatterCreate
    (kCFAllocatorDefault, userLocaleRef, kCFDateFormatterLongStyle, kCFDateFormatterMediumStyle);
CFShow(CFDateFormatterGetFormat(dateFormatter));
// output “MMM’ ‘d’, ‘yyy h’:’mm’:’ss’ ‘a”
```

If you create a locale object for a given region, you get the defaults for that region even if the users has chosen that region as his or her default and provided his or her own preferences.

Locale objects represent snapshots of settings at a particular time. For system default locale settings, values may change with different releases of the operating system. For a user’s locale, users may at any point change their language preference, modify their preferred date format, or alter their measurement units.

Locale objects are currently immutable; in future versions of the operating system this may not be true. You should ensure that when you require an immutable locale object, you make an immutable copy of an existing locale object to use for as long as necessary.

The object you get back from `CFLocaleCopyCurrent` does not change when the user changes their Preferences settings. Moreover, the object itself may be cached by the runtime system, so successive calls of `CFLocaleCopyCurrent` may return the same object, even if a user has changed preference settings. If you want to ensure that your locale settings are consistent with user preferences, you must synchronize preferences and get a new locale object with `CFLocaleCopyCurrent`.

How often an application should synchronize preferences and refetch a locale object depends on the granularity of the operation in which it’s used and on how responsive you want your application to be to changes in its environment. For example, a graphical application that displays rulers on screen should update the ruler units as often as is appropriate. In a long-running report, however, it may be appropriate to cache the locale at the beginning of the procedure and use that throughout to ensure that the date format is consistent.

You typically use locales in conjunction with other objects such as formatters, as shown in the following example.

```
userLocaleRef = CFLocaleCopyCurrent();
CFNumberFormatterRef numberFormatter =
    CFNumberFormatterCreate(kCFAllocatorDefault, userLocaleRef, kCFNumberFormatterDecimalStyle);
```

You can also retrieve information such as decimal separators, date formats and units of measurement from a locale object:

```
userLocaleRef = CFLocaleCopyCurrent();
stringRef = CFLocaleGetValue(userlocaleRef, kCFLocaleDecimalSeparator);
```

To retrieve information such as the array of names of the days of the week, you can use a formatter:

```
CFLocaleRef locale = CFLocaleCopyCurrent();
CFDateFormatterRef formatter =
    CFDateFormatterCreate (NULL, locale, kCFDateFormatterMediumStyle, kCFDateFormatterMediumStyle);
CFArrayRef weekdaySymbols =
    CFDateFormatterCopyProperty (formatter, kCFDateFormatterWeekdaySymbols);
```

[Next](Document%20Revision%20History.md)[Previous](Locale%20Concepts.md)

