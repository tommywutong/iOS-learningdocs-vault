---
title: Data Formatting Guide for Core Foundation
apple_id: 10000176i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/dfCreatingCFDateFormatters.html
archived_at: '2026-07-15T07:22:17.161317Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Data Formatting Guide for Core Foundation](Introduction%20to%20Data%20Formatting%20Guide%20for%20Core%20Foundation.md)


[Next](Creating%20and%20Using%20CFNumberFormatter%20Objects.md)[Previous](Introduction%20to%20Data%20Formatting%20Guide%20for%20Core%20Foundation.md)

# Creating and Using CFDateFormatter Objects

Date formatters format the textual representation of date objects and convert textual representations of dates and times into date objects. You create date formatter objects by specifying a locale (typically the user's current locale) and a time style, you can also specify a custom format string.

You create a date formatter using the function `CFDateFormatterCreate`. You specify a locale for the format, and styles for the date and time parts of the format. You use `CFDateFormatterCreateStringWithDate` to convert a date to a textual representation.

CFDateFormatter defines several date and time format styles—short, medium, long, and full. It also defines a “none” style that you can use to suppress output of a component. The use of styles is illustrated in [Use Formatter Styles to Present Dates and Times With the User’s Preferences](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmzzfvjvomy). The date and time styles do not specify an exact format—they depend on the locale, the user preference settings, and the operating system version. If you want an exact format, use the `CFDateFormatterSetFormat` function to change the format strings, as shown in [Use Format Strings to Specify Custom Formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmzzfvjvomq).

The following code sample creates a date formatter that provides a full representation of a date using the `kCFDateFormatterLongStyle` style.

```
CFDateRef date = CFDateCreate(NULL, 123456);
CFLocaleRef currentLocale = CFLocaleCopyCurrent();

CFDateFormatterRef dateFormatter = CFDateFormatterCreate
        (NULL, currentLocale, kCFDateFormatterLongStyle, kCFDateFormatterLongStyle);

CFStringRef formattedString = CFDateFormatterCreateStringWithDate
        (NULL, dateFormatter, date);
CFShow(formattedString);

// Memory management
CFRelease(date);
CFRelease(currentLocale);
CFRelease(dateFormatter);
CFRelease(formattedString);

// Output (for en_US locale): January 2, 2001 2:17:36 AM PST
```

The following example shows the use of `kCFDateFormatterNoStyle` to suppress output of the time component.

```
CFDateRef date = CFDateCreate(NULL, 123456);
CFLocaleRef currentLocale = CFLocaleCopyCurrent();

CFDateFormatterRef dateFormatter = CFDateFormatterCreate
        (NULL, currentLocale, kCFDateFormatterShortStyle, kCFDateFormatterNoStyle);
CFStringRef formattedString = CFDateFormatterCreateStringWithDate
        (NULL, dateFormatter, date);
CFShow(formattedString);

// Memory management
CFRelease(date);
CFRelease(currentLocale);
CFRelease(dateFormatter);
CFRelease(formattedString);

// Output (for en_US locale): 1/2/01
```

The code sample shown in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmzzfvjvona) formats a date value using different styles as a comparison. For the purposes of illustration, the sample specifies a particular locale.

__Listing 1__  Comparing date format styles

```
CFDateRef date = CFDateCreate(NULL, 123456);
CFStringRef enUSLocaleIdentifier = CFSTR("en_US");
CFLocaleRef enUSLocale = CFLocaleCreate(NULL, enUSLocaleIdentifier);

// Create different date formatters
CFDateFormatterRef shortFormatter = CFDateFormatterCreate
        (NULL, enUSLocale, kCFDateFormatterShortStyle, kCFDateFormatterShortStyle);
CFDateFormatterRef mediumFormatter = CFDateFormatterCreate
        (NULL, enUSLocale, kCFDateFormatterMediumStyle, kCFDateFormatterMediumStyle);
CFDateFormatterRef longFormatter = CFDateFormatterCreate
        (NULL, enUSLocale, kCFDateFormatterLongStyle, kCFDateFormatterLongStyle);
CFDateFormatterRef fullFormatter = CFDateFormatterCreate
        (NULL, enUSLocale, kCFDateFormatterFullStyle, kCFDateFormatterFullStyle);

// Create formatted strings
CFStringRef shortString = CFDateFormatterCreateStringWithDate
        (NULL, shortFormatter, date);
CFStringRef mediumString = CFDateFormatterCreateStringWithDate
        (NULL, mediumFormatter, date);
CFStringRef longString = CFDateFormatterCreateStringWithDate
        (NULL, longFormatter, date);
CFStringRef fullString = CFDateFormatterCreateStringWithDate
        (NULL, fullFormatter, date);

fprintf(stdout, "Short formatted date = %s\n",
        CFStringGetCStringPtr(shortString, CFStringGetSystemEncoding()));
fprintf(stdout, "Medium date = %s\n",
        CFStringGetCStringPtr(mediumString, CFStringGetSystemEncoding()));
fprintf(stdout, "Long formatted date = %s\n",
        CFStringGetCStringPtr(longString, CFStringGetSystemEncoding()));
fprintf(stdout, "Full formatted date = %s\n\n",
        CFStringGetCStringPtr(fullString, CFStringGetSystemEncoding()));

// Memory management
CFRelease(date);
CFRelease(enUSLocale);
CFRelease(shortFormatter);
CFRelease(mediumFormatter);
CFRelease(longFormatter);
CFRelease(fullFormatter);
CFRelease(shortString);
CFRelease(mediumString);
CFRelease(longString);
CFRelease(fullString);

// Output
Short formatted date = 1/2/01 2:17 AM
Medium date = Jan 2, 2001 2:17:36 AM
Long formatted date = January 2, 2001 2:17:36 AM PST
Full formatted date = Tuesday, January 2, 2001 2:17:36 AM PST
```


Typically, you are encouraged to use the predefined styles that are localized by the system. There are, though, broadly speaking two situations in which you need to use custom formats:

1. For fixed format strings, like Internet dates.
2. For user-visible elements that don’t match any of the existing styles

To specify a custom fixed format for a date formatter, you use [setDateFormat:](https://developer.apple.com/documentation/foundation/dateformatter/1413514-dateformat). The format string uses the format patterns from the Unicode Technical Standard #35. The version of the standard varies with release of the operating system:

- OS X v10.9 and iOS 7 use [version tr35-31](http://www.unicode.org/reports/tr35/tr35-31/tr35-dates.html#Date_Format_Patterns).
- OS X v10.8 and iOS 6 use [version tr35-25](http://www.unicode.org/reports/tr35/tr35-25.html#Date_Format_Patterns).
- iOS 5 uses [version tr35-19](http://www.unicode.org/reports/tr35/tr35-19.html#Date_Format_Patterns).
- OS X v10.7 and iOS 4.3 use [version tr35-17](http://www.unicode.org/reports/tr35/tr35-17.html#Date_Format_Patterns).
- iOS 4.0, iOS 4.1, and iOS 4.2 use [version tr35-15](http://www.unicode.org/reports/tr35/tr35-15.html#Date_Format_Patterns).
- iOS 3.2 uses [version tr35-12](http://www.unicode.org/reports/tr35/tr35-12.html#Date_Format_Patterns).
- OS X v10.6, iOS 3.0, and iOS 3.1 use [version tr35-10](http://unicode.org/reports/tr35/tr35-10.html#Date_Format_Patterns).
- OS X v10.5 uses [version tr35-6](http://unicode.org/reports/tr35/tr35-6.html#Date_Format_Patterns).
- OS X v10.4 uses [version tr35-4](http://unicode.org/reports/tr35/tr35-4.html#Date_Format_Patterns).

The following example illustrates using a custom format string. (Note use of `yyyy` to format the year. A common mistake is to use `YYYY` which represents the week year, not the calendar year.)

```
CFLocaleRef currentLocale = CFLocaleCopyCurrent();
CFDateRef date = CFDateCreate(NULL, 123456);

CFDateFormatterRef customDateFormatter = CFDateFormatterCreate
        (NULL, currentLocale, kCFDateFormatterNoStyle, kCFDateFormatterNoStyle);
CFStringRef customDateFormat = CFSTR("yyyy-MM-dd*HH:mm");
CFDateFormatterSetFormat(customDateFormatter, customDateFormat);

CFStringRef customFormattedDateString = CFDateFormatterCreateStringWithDate
        (NULL, customDateFormatter, date);
CFShow(customFormattedDateString);

// Memory management
CFRelease(currentLocale);
CFRelease(date);
CFRelease(customDateFormatter);
CFRelease(customFormattedDateString);

// Output: 2001-01-02*02:17
```


To display a date that contains a specific set of elements, you use [CFDateFormatterCreateDateFormatFromTemplate](https://developer.apple.com/documentation/corefoundation/1396320-cfdateformattercreatedateformatf)]. The function generates a format string with the date components you want to use, but with the correct punctuation and order appropriate for the user (that is, customized for the user’s locale and preferences). You then use the format string to create a formatter.

To understand the need for this, consider a situation where you want to display the day name, day, and month. You cannot create this representation of a date using formatter styles (there is no style that omits the year). Neither, though, can you _easily and consistently_ create the representation correctly using format strings. Although at first glance it may seem straightforward, there’s a complication: a user from the United States would typically expect dates in the form, “Mon, Jan 3”, whereas a user from Great Britain would typically expect dates in the form “Mon 31 Jan”.

The following example illustrates the point:

```
CFStringRef dateComponents = CFSTR("yMMMMd");

CFLocaleRef usLocale = CFLocaleCreate(NULL, CFSTR("en_US"));
CFStringRef usDateFormatString =
    CFDateFormatterCreateDateFormatFromTemplate(NULL, dateComponents, 0, usLocale);
// Date format for English (United States): MMMM d, y

CFLocaleRef gbLocale = CFLocaleCreate(NULL, CFSTR("en_GB"));
CFStringRef gbDateFormatString =
    CFDateFormatterCreateDateFormatFromTemplate(NULL, dateComponents, 0, gbLocale);
// Date format for English (United Kingdom): d MMMM y
```

[Next](Creating%20and%20Using%20CFNumberFormatter%20Objects.md)[Previous](Introduction%20to%20Data%20Formatting%20Guide%20for%20Core%20Foundation.md)

