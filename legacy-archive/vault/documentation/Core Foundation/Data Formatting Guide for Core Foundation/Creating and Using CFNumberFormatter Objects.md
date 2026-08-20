---
title: Data Formatting Guide for Core Foundation
apple_id: 10000176i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/dfCreatingCFNumberFormatters.html
archived_at: '2026-07-15T07:22:17.174439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Data Formatting Guide for Core Foundation](Introduction%20to%20Data%20Formatting%20Guide%20for%20Core%20Foundation.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20and%20Using%20CFDateFormatter%20Objects.md)

# Creating and Using CFNumberFormatter Objects

Number formatters format the textual representation of number objects and convert textual representations of numeric values into number objects. The representation encompasses integers, floats, and doubles; floats and doubles can be formatted to a specified decimal position. You create number formatter objects by specifying a number style, you can also specify a custom format string.

To create a CFNumberFormatter, you must specify a locale and a formatter style as illustrated in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge4tolktk4yq), or a format string, as shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge4tolktk4za). Format styles do not specify an exact format—they depend on the locale, user preference settings, and operating system version. If you want to specify an exact format, use the `CFNumberFormatterSetFormat` function to set the format string, and the `CFNumberFormatterSetProperty` function to change specific properties such as separators, the "Not a number" symbol, and the padding character.

__Listing 1__  Code sample showing how to create a number formatter using a formatter style

```
float aFloat = 1234.567;
int fractionDigits = 2;
CFLocaleRef currentLocale = CFLocaleCopyCurrent();

CFNumberFormatterRef numberFormatter = CFNumberFormatterCreate
        (NULL, currentLocale, kCFNumberFormatterDecimalStyle);
CFNumberRef maxFractionDigits = CFNumberCreate
        (NULL, kCFNumberIntType, &fractionDigits);
CFNumberFormatterSetProperty
        (numberFormatter, kCFNumberFormatterMaxFractionDigits, maxFractionDigits);
CFStringRef formattedNumberString = CFNumberFormatterCreateStringWithValue
        (NULL, numberFormatter, kCFNumberFloatType, &aFloat);

CFShow(formattedNumberString);

// Memory management
CFRelease(currentLocale);
CFRelease(numberFormatter);
CFRelease(maxFractionDigits);
CFRelease(formattedNumberString);

// Output (for en_US_POSIX locale): 1234.57
```


__Listing 2__  Code sample showing how to create a number formatter using a formatter string

```
float aFloat = 1234.567;
CFStringRef frLocaleIdentifier = CFSTR("fr_FR");
CFLocaleRef frLocale = CFLocaleCreate(NULL, frLocaleIdentifier);

CFNumberFormatterRef numberFormatter = CFNumberFormatterCreate
        (NULL, frLocale, kCFNumberFormatterNoStyle);
CFStringRef formatString = CFSTR("#.##");
CFNumberFormatterSetFormat(numberFormatter, formatString);
CFStringRef formattedNumberString = CFNumberFormatterCreateStringWithValue
        (NULL, numberFormatter, kCFNumberFloatType, &aFloat);

CFShow(formattedNumberString);

// Memory management
CFRelease(frLocale);
CFRelease(numberFormatter);
CFRelease(formattedNumberString);

// Output (for fr_FR locale -- note "," decimal separator): 1234,57
```

The following code fragment creates a number formatter that formats numbers as percentages using the `kCFNumberFormatterPercentStyle` number style. In this example, the `CFNumberFormatterCreateStringWithNumber` function converts the numeric value of `0.2` to a textual representation of `"20%"`.

```
// Creating a number formatter
float percent = 0.20;
CFNumberFormatterRef numberFormatter = CFNumberFormatterCreate
        (NULL, currentLocale, kCFNumberFormatterPercentStyle);
CFNumberRef number = CFNumberCreate(NULL, kCFNumberFloatType, &percent);
CFStringRef numberString = CFNumberFormatterCreateStringWithNumber
        (NULL, numberFormatter, number);
```


CFNumberFormatter defines several format styles. You set a formatter's style when you create the formatter. The code sample shown in [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnbsfvjvomq) formats a numeric value using decimal, percentage, currency, and scientific notation styles. (The output format depends on user preference, so may vary in your application.)

__Listing 3__  Comparing number format styles

```
float n = 1.20;
CFNumberRef value = CFNumberCreate(NULL, kCFNumberFloatType, &n);
CFLocaleRef currentLocale = CFLocaleCopyCurrent();

// Create different number formatters
CFNumberFormatterRef decimalFormatter = CFNumberFormatterCreate
        (NULL, currentLocale, kCFNumberFormatterDecimalStyle);
CFNumberFormatterRef currencyFormatter = CFNumberFormatterCreate
        (NULL, currentLocale, kCFNumberFormatterCurrencyStyle);
CFNumberFormatterRef percentFormatter = CFNumberFormatterCreate
        (NULL, currentLocale, kCFNumberFormatterPercentStyle);
CFNumberFormatterRef scientificFormatter = CFNumberFormatterCreate
        (NULL, currentLocale, kCFNumberFormatterScientificStyle);

// Create formatted strings
CFStringRef decimalString = CFNumberFormatterCreateStringWithNumber
        (NULL, decimalFormatter, value);
CFStringRef currencyString = CFNumberFormatterCreateStringWithNumber
        (NULL, currencyFormatter, value);
CFStringRef percentString = CFNumberFormatterCreateStringWithNumber
        (NULL, percentFormatter, value);
CFStringRef scientificString = CFNumberFormatterCreateStringWithNumber
        (NULL, scientificFormatter, value);

// Print formatted strings to stdout
fprintf(stdout, "Decimal formatted number = %s\n",
        CFStringGetCStringPtr(decimalString, CFStringGetSystemEncoding()));
fprintf(stdout, "Currency number = %s\n",
        CFStringGetCStringPtr(currencyString, CFStringGetSystemEncoding()));
fprintf(stdout, "Percent formatted number = %s\n",
        CFStringGetCStringPtr(percentString, CFStringGetSystemEncoding()));
fprintf(stdout, "Scientific formatted number = %s\n",
        CFStringGetCStringPtr(scientificString, CFStringGetSystemEncoding()));

// Memory management
CFRelease(currentLocale);
CFRelease(decimalFormatter);
CFRelease(currencyFormatter);
CFRelease(percentFormatter);
CFRelease(scientificFormatter);
CFRelease(decimalString);
CFRelease(currencyString);
CFRelease(percentString);
CFRelease(scientificString);

// Output (for en_US_POSIX locale)
Decimal formatted number = 1.2
Currency number = $1.20
Percent formatted number = 120%
Scientific formatted number = 1.20000004768372E0
```


Typically, you are encouraged to use the predefined styles that are localized by the system. If you want, however, you can change properties of number formatters using the `CFNumberFormatterSetProperty` function—see [CFNumberFormatterRef](https://developer.apple.com/documentation/corefoundation/cfnumberformatter) for a complete list of the properties that can be changed using this function. For example, you can set the decimal separator to a comma, as shown in the following code fragment.

```
CFNumberFormatterRef decimalFormatter = CFNumberFormatterCreate
        (NULL, currentLocale, kCFNumberFormatterDecimalStyle);
CFNumberFormatterSetProperty(decimalFormatter,
        kCFNumberFormatterDecimalSeparator, CFSTR(","));
```

Using the formatter `decimalFormatter` above, you can convert a numeric value of `1.2` to a textual representation of `1,2`.

If you want to specify an exact format, use the `CFNumberFormatterSetFormat` function to set the format string. The format string uses the format patterns from the Unicode Technical Standard #35. The version of the standard varies with release of the operating system:

- OS X v10.9 and iOS 7 use [version tr35-31](http://www.unicode.org/reports/tr35/tr35-31/tr35-dates.html#Number_Format_Patterns).
- OS X v10.8 and iOS 6 use [version tr35-25](http://www.unicode.org/reports/tr35/tr35-25.html#Number_Format_Patterns).
- iOS 5 uses [version tr35-19](http://www.unicode.org/reports/tr35/tr35-19.html#Number_Format_Patterns).
- OS X v10.7 and iOS 4.3 use [version tr35-17](http://www.unicode.org/reports/tr35/tr35-17.html#Number_Format_Patterns).
- iOS 4.0, iOS 4.1, and iOS 4.2 use [version tr35-15](http://www.unicode.org/reports/tr35/tr35-15.html#Number_Format_Patterns).
- iOS 3.2 uses [version tr35-12](http://www.unicode.org/reports/tr35/tr35-12.html#Number_Format_Patterns).
- OS X v10.6, iOS 3.0, and iOS 3.1 use [version tr35-10](http://unicode.org/reports/tr35/tr35-10.html#Number_Format_Patterns).
- OS X v10.5 uses [version tr35-6](http://unicode.org/reports/tr35/tr35-6.html#Number_Format_Patterns).
- OS X v10.4 uses [version tr35-4](http://unicode.org/reports/tr35/tr35-4.html#Number_Format_Patterns).

For example, specifying the format string as `"$#,##0.00"` yields text representations such as `"$156.30"`.

The code sample shown in [Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnbsfvjvomy) formats different numeric values using `"$#,##0.00"` as the format string for currency values.

__Listing 4__  Using number format strings

```
CFLocaleRef currentLocale = CFLocaleCopyCurrent();
CFNumberFormatterRef customCurrencyFormatter = CFNumberFormatterCreate
    (NULL, currentLocale, kCFNumberFormatterCurrencyStyle);
CFNumberFormatterSetFormat(customCurrencyFormatter, CFSTR("$#,##0.00"));

float n1 = 6.3;
CFNumberRef number1 = CFNumberCreate(NULL, kCFNumberFloatType, &n1);
float n2 = 156.3;
CFNumberRef number2 = CFNumberCreate(NULL, kCFNumberFloatType, &n2);
float n3 = 1156.372;
CFNumberRef number3 = CFNumberCreate(NULL, kCFNumberFloatType, &n3);

CFStringRef string1 = CFNumberFormatterCreateStringWithNumber
        (NULL, customCurrencyFormatter, number1);
CFStringRef string2 = CFNumberFormatterCreateStringWithNumber
        (NULL, customCurrencyFormatter, number2);
CFStringRef string3 = CFNumberFormatterCreateStringWithNumber
        (NULL, customCurrencyFormatter, number3);

fprintf(stdout, "Format of %f = %s\n",
        n1, CFStringGetCStringPtr(string1, CFStringGetSystemEncoding()));
fprintf(stdout, "Format of %f = %s\n",
        n2, CFStringGetCStringPtr(string2, CFStringGetSystemEncoding()));
fprintf(stdout, "Format of %f = %s\n\n",
        n3, CFStringGetCStringPtr(string3, CFStringGetSystemEncoding()));

// Memory management
CFRelease(currentLocale);
CFRelease(customCurrencyFormatter);
CFRelease(number1);
CFRelease(number2);
CFRelease(number3);
CFRelease(string1);
CFRelease(string2);
CFRelease(string3);

// Output (for en_US_POSIX locale)
Format of 6.300000 = $6.30
Format of 156.300003 = $156.30
Format of 1156.371948 = $1,156.37
```

[Next](Document%20Revision%20History.md)[Previous](Creating%20and%20Using%20CFDateFormatter%20Objects.md)

