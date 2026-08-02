---
title: Locales Programming Guide
apple_id: 10000181i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-06-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFLocales/CFLocales.html
archived_at: '2026-07-15T07:22:28.207970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Locale%20Concepts.md)

# Introduction to Locales

Locales
encapsulate information about linguistic, cultural, and technological
conventions and standards. Examples of information encapsulated
by a locale include the symbol used for the decimal separator in
numbers and the way dates are formatted. Locales are typically used
to provide, format, and interpret information about and according
to the user’s customs and preferences. They are frequently used
in conjunction with formatters (see _[Data Formatting Guide for Core Foundation](../Data%20Formatting%20Guide%20for%20Core%20Foundation/Introduction%20to%20Data%20Formatting%20Guide%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tm2i)_).
Although you can use many locales, you usually use the one associated
with the current user.

The operating system supplies data for dozens of different
locales, regardless of which languages are installed.

The following articles explain what locales are, how they
work, and common tasks you might perform with them:

- [Locale Concepts](Locale%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dalkdjjbeiqsiinba) describes
  what locales are, why they are useful, and how they are identified.
  It also introduces the relationship between locales and user preferences.
- [Working With Core Foundation Locales](Working%20With%20Core%20Foundation%20Locales.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dclkdjjbeiqsiinba) explains
  how to create locale objects in Core Foundation, how to get the
  current user’s locale, and how to use locale objects in conjunction
  with other objects. It also introduces aspects of the lifetime of
  a locale object.

[Next](Locale%20Concepts.md)

