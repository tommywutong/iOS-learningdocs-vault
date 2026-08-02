---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSTimestampFormatter.html
archived_at: '2026-07-15T08:13:56.617461Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSTimestampFormatter

> **__Inherits from:__**
> : java.text.Format : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

Instances of NSTimestampFormatter format NSTimestamps into their textual representations and convert textual representations of dates and times into NSTimestamps. You can express the representation of dates and times very flexibly: "Thu 22 Dec 1994" is just as acceptable as "12/22/94".

You can associate an date pattern with a WOString or WOTextField dynamic element. WebObjects uses an NSTimestampFormatter object to perform the appropriate conversions.

You can also create an NSTimestampFormatter with the constructor, provide a date pattern string, and use java.text.Format's [format](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3gn5zg2ylu) and [parseObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3qmfzhgzkpmjvgky3u) methods to convert between NSTimestamps and their textual representations:

> ```
> NSTimestampFormatter formatter = new NSTimestampFormatter("%m/%d/%y");
> String description = formatter.format(myNSTimestamp);
> ```

> ```
> NSTimestampFormatter formatter = new NSTimestampFormatter("%m/%d/%y");
> NSTimestamp myNSTimestamp = formatter.parseObject(myTimestampString);
> ```

Instances of NSTimestampFormatter are immutable.

## The Calendar Pattern

You must specify a pattern whenever you create a NSTimestampFormatter. This pattern is a string that contains specifiers that are very similar to those used in the standard C library function __strftime()__. When NSTimestampFormatter converts a date to a string, it uses this pattern.

The date conversion specifiers cover a range of date conventions:

|  |  |
| --- | --- |
| __Specifier__ | __Description__ |
| `%%` | a `'%'` character |
| `%a` | abbreviated weekday name |
| `%A` | full weekday name |
| `%b` | abbreviated month name |
| `%B` | full month name |
| `%c` | shorthand for "`%X %x`", the locale format for date and time |
| `%d` | day of the month as a decimal number (01-31) |
| `%e` | same as `%d` but does not print the leading 0 for days 1 through 9 |
| `%F` | milliseconds as a decimal number (000-999) |
| `%H` | hour based on a 24-hour clock as a decimal number (00-23) |
| `%I` | hour based on a 12-hour clock as a decimal number (01-12) |
| `%j` | day of the year as a decimal number (001-366) |
| `%m` | month as a decimal number (01-12) |
| `%M` | minute as a decimal number (00-59) |
| `%p` | AM/PM designation for the locale |
| `%S` | second as a decimal number (00-59) |
| `%w` | weekday as a decimal number (0-6), where Sunday is 0 |
| `%x` | date using the date representation for the locale |
| `%X` | time using the time representation for the locale |
| `%y` | year without century (00-99) |
| `%Y` | year with century (such as 1990) |
| `%Z` | time zone name (such as Pacific Daylight Time) |
| `%z` | time zone offset in hours and minutes from GMT (HHMM) |

Alternatively, you can specify the pattern using Sun's date pattern specifiers. See Sun's documentation for the java.text.SimpleDateFormat class for more information.

## Converting Date Strings Without Time Zones

When you convert a string without a time zone specification to an NSTimestamp, the formatter assumes the time zone is the default parse time zone (see the [defaultParseTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3emvtgc5lmorigc4ttmvkgs3lfljxw4zi) and [setDefaultParseTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3tmv2eizlgmf2wy5cqmfzhgzkunfwwkwtpnzsq) methods). An analogous time zone, called the default format time zone, is used when converting an NSTimestamp without a time zone to a string.

Sometimes you need to give the user a choice of time zones. For example, you might put the time zones in a pull-down list. In such cases, you can use the [parseObjectInUTC](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3qmfzhgzkpmjvgky3ujfxfkvcd) method to parse a date string for the UTC time zone. The following code shows how you can compute the offset from UTC for the particular time zone the user chooses and add it to the parsed timestamp:

> ```
> NSTimestamp date = (NSTimestamp)myFormatter.parseInUTC(myString);
> NSTimeZone tz = NSTimeZone.timeZoneWithName(myTimeZoneName);
> int offset = tz.secondsFromGMTForTimestamp(date);
> long milliseconds = date.getTime() - offset * 1000;
> NSTimestamp dateWithTimeZone = new NSTimestamp(milliseconds);
> ```

## Constructors

---

### NSTimestampFormatter

`public NSTimestampFormatter()`

Creates a NSTimestampFormatter with the default pattern (`%m/%d/%y`).

`public NSTimestampFormatter(String pattern)`

Creates an NSTimestampFormatter with the pattern string _pattern_. If _pattern_ is `null`, this constructor uses the default pattern (`%m/%d/%y`). See ["The Calendar Pattern" (page 300)](#apple-ijaueqsdi5dek) for more information on specifying the pattern string.

`public NSTimestampFormatter(String pattern, java.text.DateFormatSymbols formatSymbols)`

Creates an NSTimestampFormatter with the specified pattern using the specified date format symbols. If _pattern_ is `null`, this constructor uses the default pattern (`%m/%d/%y`) with the slashes replaced by the appropriate date symbol. See ["The Calendar Pattern" (page 300)](#apple-ijaueqsdi5dek) for more information on specifying the pattern string.

`public NSTimestampFormatter(String pattern, java.util.Locale locale)`

Creates an NSTimestampFormatter with the specified pattern using the date symbols for the specified locale. If _pattern_ is `null`, this constructor uses the default pattern (`%m/%d/%y`) with the slashes ("/") replaced by the appropriate date symbol. See ["The Calendar Pattern" (page 300)](#apple-ijaueqsdi5dek) for more information on specifying the pattern string.

---

## Instance Methods

---

### __defaultFormatTimeZone__

`public NSTimeZone defaultFormatTimeZone()`

Returns the default time zone the receiver uses for formatting (converting an [NSTimestamp](NSTimestamp.md#apple-indeerkkivfek) into a string). If the default format time zone is not `null`, the receiver uses the default format time zone when it performs the conversion. Otherwise the receiver uses the time zone of the NSTimestamp that it is converting. The default format time zone itself defaults to `null`.

__See Also:__ [defaultParseTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3emvtgc5lmorigc4ttmvkgs3lfljxw4zi)

---

### __defaultParseTimeZone__

`public synchronized NSTimeZone defaultParseTimeZone()`

Returns the default time zone the receiver uses for parsing (converting a string to an [NSTimestamp](NSTimestamp.md#apple-indeerkkivfek)). During the conversion, if the NSTimestamp has a time zone (its [timeZone](NSTimestamp.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporuw2zk2n5xgk) method returns something other than `null`), the receiver uses the NSTimestamp's time zone. Otherwise the receiver uses the default parse time zone. The default parse time zone itself defaults to the time zone specified by the `user.timezone` system property.

__See Also:__ [defaultFormatTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3emvtgc5lmordg64tnmf2fi2lnmvng63tf)

---

### format

`public StringBuffer format( Object object, StringBuffer toAppendTo, java.text.FieldPosition position)`

Formats _object_ to produce a string, appends the string to _toAppendTo_, and returns the resulting StringBuffer. The _position_ parameter specifies an alignment field to place the formatted object. When the method returns, this parameter contains the position of the alignment field. See Sun's java.text.Format documentation for more information.

---

### parseObjectInUTC

`public Object parseObjectInUTC( String source, java.text.ParsePosition status)`

Parses a string to produce an object using UTC as the time zone. This method ignores the time zone specified by the string and the value of the parse time zone. For parameter definitions, see Sun's java.text.Format documentation for the __parseObject__ method.

__See Also:__ [parseObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3qmfzhgzkpmjvgky3u)

---

### parseObject

`public Object parseObject( String source, java.text.ParsePosition status)`

Parses a string to produce an object. If the string does not specify a time zone, uses the default parse time zone. See Sun's java.text.Format documentation for more information.

__See Also:__ [setDefaultParseTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3tmv2eizlgmf2wy5cqmfzhgzkunfwwkwtpnzsq)

---

### __pattern__

`public String pattern()`

Returns the receiver's pattern. See ["The Calendar Pattern" (page 300)](#apple-ijaueqsdi5dek) for more information about the pattern.

---

### __setDefaultFormatTimeZone__

`public synchronized void setDefaultFormatTimeZone(NSTimeZone timeZone)`

Sets the default time zone the receiver uses for formatting (converting an [NSTimestamp](NSTimestamp.md#apple-indeerkkivfek) into a string) to _timeZone_.

__See Also:__ [setDefaultParseTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3tmv2eizlgmf2wy5cqmfzhgzkunfwwkwtpnzsq)

---

### __setDefaultParseTimeZone__

`public synchronized void setDefaultParseTimeZone(NSTimeZone timeZone)`

Sets the default time zone the receiver uses for parsing (converting a string to an [NSTimestamp](NSTimestamp.md#apple-indeerkkivfek)) to _timeZone_.

__See Also:__ [setDefaultFormatTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3tmv2eizlgmf2wy5cgn5zg2ylukruw2zk2n5xgk)

---

### __setPattern__

`public synchronized void setPattern(String pattern)`

Sets the receiver's pattern to _pattern_. See ["The Calendar Pattern" (page 300)](#apple-ijaueqsdi5dek) for more information about the pattern.

---

### __toString__

`public String toString()`

Returns a string representation of the receiver that includes the default format time zone, the default parse time zone, and the pattern.

__See Also:__ [defaultFormatTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3emvtgc5lmordg64tnmf2fi2lnmvng63tf), [defaultParseTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3emvtgc5lmorigc4ttmvkgs3lfljxw4zi), [pattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24cgn5zg2yluorsxel3qmf2hizlsny)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
