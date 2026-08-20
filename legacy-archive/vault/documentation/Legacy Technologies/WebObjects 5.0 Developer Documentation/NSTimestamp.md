---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSTimestamp.html
archived_at: '2026-07-15T08:13:56.592032Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSTimestamp

> **__Inherits from:__**
> : java.sql.Timestamp : java.util.Date : Object

> **__Implements:__**
> : NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSTimestamp objects represent a particular instance in time. NSTimestamp is a subclass of java.sql.Timestamp, itself a subclass of java.util.Date. Unlike the NSGregorianDate class in previous versions of the Foundation framework, NSTimestamp does not support calendar functions. Refer to the table below to determine which classes to use to perform date operations in WebObjects.

|  |  |
| --- | --- |
| __Class__ | __Description__ |
| NSTimestamp | Represents an instance in time |
| java.util.GregorianCalendar | Represents a calendar date |
| NSTimeZone | Represents a time zone |
| NSTimestampFormatter | Converts NSTimestamps to strings and vice versa. |

See the Sun's documentation for the java.util.GregorianCalendar class for more information about using calendars in Java.

## Common Date Operations

For the following code segments, you need to import `java.util.*` to access Java's date API.

To break up a NSTimestamp into its component year, month, day, hour, etc., you can convert it into a java.util.GregorianCalendar and invoke its __get__ method on the individual fields:

> ```
> NSTimestamp myNSTimestamp = new NSTimestamp();
> GregorianCalendar myCalendar = new GregorianCalendar();
> myCalendar.setTime(myNSTimestamp);
> int year = myCalendar.get(GregorianCalendar.YEAR);
> int dayOfMonth = myCalendar.get(GregorianCalendar.DAY_OF_MONTH);
> ```

To create an NSTimestamp based on its components, use the following code:

> ```
> NSTimeZone tz = NSTimeZone.timeZoneWithName("America/Los_Angeles", true);
> NSTimestamp myNSTimestamp = new NSTimestamp(year, month, day, hour, minute, seconds, tz);
>
> ```

To add an offset in Gregorian units to an NSTimestamp, use the following code:

> ```
> NSTimestamp myNSTimestamp = new NSTimestamp();
> myNSTimestamp.timestampByAddingGregorianUnits(year, month, day, hour, minute, seconds);
> ```

To create an NSTimestamp representing the current time, use the no-argument constructor:

> ```
> NSTimestamp currentTime = new NSTimestamp();
> ```

The Enterprise Objects Framework expects dates to be represented as NSTimestamp objects. To convert a java.util.Date to an NSTimestamp use:

> ```
> NSTimestamp myNSTimestamp = new NSTimestamp(myJavaUtilDate);
> ```

Since NSTimestamp is a subclass of java.util.Date, you don't need to convert an NSTimestamp into a java.util.Date.

## Constants

---

NSTimestamp provides the following constants.

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| DistantFuture | NSTimestamp | An NSTimestamp that represents a date in the distant future (in terms of centuries). |
| DistantPast | NSTimestamp | An NSTimestamp that represents a date in the distant future (in terms of centuries). |

## Interfaces Implemented

---

> : NSCoding
>
> : [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmnwgc43tizxxeq3pmrsxe): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsxg5dbnvyc6zdfmnxwizkpmjvgky3u): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmvxgg33emvlws5diinxwizls)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpjzjvi2lnmvzxiylnoa)
>
> **Instance methods**
>
> : [compare](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmnxw24dbojsq): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporxvg5dsnfxgo)
>
> **Deprecated methods**
>
> : [currentTimeIntervalSinceReferenceDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsxg5dbnvyc6y3vojzgk3tukruw2zkjnz2gk4twmfwfg2lomnsvezlgmvzgk3tdmvcgc5df): [dayOfCommonEra](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmrqxst3ginxw23lpnzcxeyi): [dayOfMonth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmrqxst3gjvxw45di): [dayOfWeek](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmrqxst3gk5swk2y): [dayOfYear](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmrqxst3glfswc4q): [distantFuture](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsxg5dbnvyc6zdjon2gc3tuiz2xi5lsmu): [distantPast](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsxg5dbnvyc6zdjon2gc3tukbqxg5a): [earlierTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpmvqxe3djmvzfi2lnmvzxiylnoa): [gregorianUnitsSinceTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpm5zgkz3pojuwc3svnzuxi42tnfxggzkunfwwk43umfwxa): [hourOfDay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpnbxxk4spmzcgc6i): [laterTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpnrqxizlskruw2zltorqw24a): [microsecondOfSecond](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpnvuwg4tponswg33omrhwmu3fmnxw4za): [millisecondsToTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsxg5dbnvyc63ljnrwgs43fmnxw4zdtkrxvi2lnmvew45dfoj3gc3a): [minuteOfHour](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpnvuw45lumvhwmsdpovza): [monthOfYear](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bpnvxw45dij5tfszlboi): [secondOfMinute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponswg33omrhwmtljnz2xizi): [timeIntervalSinceNow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporuw2zkjnz2gk4twmfwfg2lomnsu433x): [timeIntervalSinceReferenceDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporuw2zkjnz2gk4twmfwfg2lomnsvezlgmvzgk3tdmvcgc5df): [timeIntervalSinceTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporuw2zkjnz2gk4twmfwfg2lomnsvi2lnmvzxiylnoa): [timeIntervalToMilliseconds](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsxg5dbnvyc65djnvsus3tumvzhmylmkrxu22lmnruxgzldn5xgi4y): [setDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxirdborsq): [setHours](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxisdpovzhg): [setMinutes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxitljnz2xizlt): [setMonth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxitlpnz2gq): [setNanos](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxittbnzxxg): [setSeconds](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxiu3fmnxw4zdt): [setTime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxivdjnvsq): [setYear](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bponsxiwlfmfza): [timestampByAddingGregorianUnits](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporuw2zltorqw24ccpfawizdjnztuo4tfm5xxe2lbnzkw42luom): [timestampByAddingTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporuw2zltorqw24ccpfawizdjnztvi2lnmvew45dfoj3gc3a): [timeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bporuw2zk2n5xgk): [yearOfCommonEra](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zltorqw24bppfswc4spmzbw63lnn5xek4tb)

## Constructors

---

### NSTimestamp

`public NSTimestamp()`

Creates an NSTimestamp representing the current time, accurate to the millisecond.

`public NSTimestamp(java.sql.Timestamp date)`

Creates an NSTimestamp object representing the same instant in time as _date_.

`public NSTimestamp(java.util.Date date)`

Creates an NSTimestamp object representing the same instant in time as _date_.

`public NSTimestamp(long milliseconds)`

Creates an NSTimestamp object representing the specified number of milliseconds since January 1, 1970, 00:00:00 GMT.

`public NSTimestamp( long milliseconds, java.util.TimeZone timezone)`

Creates an NSTimestamp object representing the specified number of milliseconds since January 1, 1970, 00:00:00 in the specified time zone.

`public NSTimestamp( long milliseconds, int nanoseconds)`

Creates an NSTimestamp object representing the specified number of milliseconds since January 1, 1970, 00:00:00 GMT and sets the number of nanoseconds to _nanoseconds_.

`public NSTimestamp( long milliseconds, int nanoseconds, java.util.TimeZone timezone)`

Creates an NSTimestamp object representing the specified number of milliseconds and nanoseconds since January 1, 1970, 00:00:00 in the specified time zone.

`public NSTimestamp( long milliseconds, NSTimestamp timestamp)`

Creates an NSTimestamp object representing the specified number of milliseconds after the time specified by _timestamp_.

`public NSTimestamp( int year, int month, int day, int hours, int minutes, int seconds, java.util.TimeZone timezone)`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Common Date Operations" (page 284)](#apple-ijbeoq2giffeg) for information on how to create a NSTimestamp based on its components.

Creates an NSTimestamp object representing the specified year, month, day, hours, minutes, and seconds in the specified time zone.

---

## Static Methods

---

### __currentTimeIntervalSinceReferenceDate__

`public static long currentTimeIntervalSinceReferenceDate()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the number of milliseconds between the system's absolute reference date (the first instant of 1 January 1970, GMT) and the current date and time.

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates a NSTimestamp from data in coder.

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq)

---

### __distantFuture__

`public static NSTimestamp distantFuture()`

Deprecated in the Java Foundation framework. Don't use this method. Use the constant [DistantFuture](#apple-ijbeoskfi5cei) instead.

Creates and returns an NSTimestamp that represents a date many centuries in the future. You can pass this value where an NSTimestamp is required to have the date argument essentially ignored. For example, the NSLock method __tryLock(NSTimeStamp)__ returns `false` if the receiver fails to acquire the lock before the specified date. You can use the object returned by __distantFuture__ as the date argument to wait indefinitely to acquire the lock.

---

### __distantPast__

`public static NSTimestamp distantPast()`

Deprecated in the Java Foundation framework. Don't use this method. Use the constant [DistantPast](#apple-ijbeosccjjduc) instead.

Creates and returns an NSTimestamp that represents a date many centuries in the past. You can use this object in your code as a control date, a guaranteed temporal boundary.

---

### __millisecondsToTimeInterval__

`public static long millisecondsToTimeInterval(long milliseconds)`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the time interval in seconds corresponding to the specified time represented in milliseconds. Any fractional part of a second is truncated.

---

### __timeIntervalToMilliseconds__

`public static long timeIntervalToMilliseconds(long timeInterval)`

Deprecated in the Java Foundation framework. Don't use this method.

Returns a time interval in milliseconds corresponding to the specified time interval represented in seconds.

---

## Instance Methods

---

### classForCoder

`public Class classForCoder()`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) in the interface specification for NSCoding.

---

### compare

`public int compare(NSTimestamp timestamp)`

Returns an integer indicating whether the receiver is before, after, or the same as _timestamp_. If the receiver is before _timestamp_, this method returns NSComparator.OrderedAscending. If the receiver is after _timestamp_, this method returns NSComparator.OrderedDescending. If the dates match, this method returns NSComparator.OrderedSame.

---

### dayOfCommonEra

`public int dayOfCommonEra()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the number of days since the beginning of the Common Era. The base year of the Common Era is 1 C.E. (which is the same as 1 A.D.).

---

### dayOfMonth

`public int dayOfMonth()`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

Returns a number that indicates the day of the month (1 through 31) of the receiver.

---

### dayOfWeek

`public int dayOfWeek()`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

Returns a number that indicates the day of the week (0 through 6) of the receiver; 0 indicates Sunday.

---

### dayOfYear

`public int dayOfYear()`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

Returns a number that indicates the day of the year (1 through 366) of the receiver.

---

### __earlierTimestamp__

`public NSTimestamp earlierTimestamp(NSTimestamp timestamp)`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the receiver or _timestamp_, whichever is earlier.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the interface specification for NSCoding.

---

### gregorianUnitsSinceTimestamp

`public void gregorianUnitsSinceTimestamp( NSTimestamp.IntRef years, NSTimestamp.IntRef months, NSTimestamp.IntRef days, NSTimestamp.IntRef hours, NSTimestamp.IntRef minutes, NSTimestamp.IntRef seconds, NSTimestamp timestamp)`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

Computes the time difference in calendar units between the receiver and _timestamp_ and returns it in _years_, _months_, _days_, _hours_, _minutes_, and _seconds_. NSTimestamp.IntRef is a local class that contains a single element: the integer __value__.

You can choose any representation you wish for the time difference by passing `null` for the arguments you want to ignore. For example, the following code fragment computes the difference in months, days, and years between two dates:

> ```
> NSTimestamp momsBDay =
>     new NSTimestamp(1936, 1, 8, 7, 30, 0, java.util.TimeZone.getTimeZone("EST"));
> NSTimestamp dateOfBirth =
>     new NSTimestamp(1965, 12, 7, 17, 25, 0, new NSTimeZone("EST"));
>
> NSTimestamp.IntRef years = new NSTimestamp.IntRef();
> NSTimestamp.IntRef months = new NSTimestamp.IntRef();
> NSTimestamp.IntRef days = new NSTimestamp.IntRef();
>
> dateOfBirth.gregorianUnitsSinceTimestamp(momsBDay, years, months, days,
>     null, null, null)
> ```

This message returns 29 years, 10 months, and 29 days. If you want to express the years in terms of months, you pass `null` for the years argument:

> ```
> dateOfBirth.gregorianUnitsSinceTimestamp(momsBDay, null, months, days,      null, null, null);
> ```

This message returns 358 months and 29 days.

---

### hourOfDay

`public int hourOfDay()`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

Returns the hour value (0 through 23) of the receiver. On Daylight Savings "fall back" days, a value of 1 is returned for two consecutive hours, but with a different time zone (the first in daylight savings time and the second in standard time).

---

### __laterTimestamp__

`public NSTimestamp laterTimestamp(NSTimestamp timestamp)`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the receiver or _timestamp_, whichever is later.

---

### microsecondOfSecond

`public int microsecondOfSecond()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the microseconds value (0 through 999,999) of the receiver.

---

### minuteOfHour

`public int minuteOfHour()`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

Returns the minutes value (0 through 59) of the receiver.

---

### monthOfYear

`public int monthOfYear()`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative. Note that java.util.Calendar represents months as integers from 0 to 11.

Returns a number that indicates the month of the year (1 through 12) of the receiver.

---

### secondOfMinute

`public int secondOfMinute()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the seconds value (0 through 59) of the receiver. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

---

### setDate

`public void setDate(int date)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### setHours

`public void setHours(int hours)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### setMinutes

`public void setMinutes(int minutes)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### setMonth

`public void setMonth(int month)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### setNanos

`public void setNanos(int nanoseconds)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### setSeconds

`public void setSeconds(int seconds)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### setTime

`public void setTime(long milliseconds)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### setYear

`public void setYear(int year)`

Deprecated in the Java Foundation framework. Don't use this method. NSTimestamp objects are immutable.

---

### __timeIntervalSinceNow__

`public long timeIntervalSinceNow()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the number of milliseconds between the receiver's time and the current system time. This value is negative if the receiver's time is earlier than the current system time.

---

### __timeIntervalSinceReferenceDate__

`public long timeIntervalSinceReferenceDate()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the number of milliseconds between the receiver's time and the reference date (January 1, 1970, 00:00 GMT). This value is negative if the receiver's time is earlier than the reference date.

---

### __timeIntervalSinceTimestamp__

`public long timeIntervalSinceTimestamp(NSTimestamp time)`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the number of milliseconds between the receiver's time and _time_. This value is negative if the receiver's time is earlier than _time_.

---

### timestampByAddingGregorianUnits

`public NSTimestamp timestampByAddingGregorianUnits( int year, int month, int day, int hour, int minute, int second)`

Deprecated in the Java Foundation framework. Don't use this method.

Returns an NSTimestamp that is updated with the _year_, _month_, _day_, _hour_, _minute_, and _second_ offsets specified as arguments. The offsets can be positive (future) or negative (past). This method preserves "clock time" across changes in Daylight Savings Time zones and leap years. For example, adding one month to an NSTimestamp with a time of 12 noon correctly maintains time at 12 noon.

The following code fragment shows an NSTimestamp created with a date a week later than an existing NSTimestamp.

> ```
> NSTimestamp now = new NSTimestamp();
> NSTimestamp nextWeek =
>     now.timestampByAddingGregorianUnits(0, 0, 7, 0, 0, 0);
> ```

---

### timestampByAddingTimeInterval

`public NSTimestamp timestampByAddingTimeInterval(long timeInterval)`

Deprecated in the Java Foundation framework. Don't use this method.

Returns an NSTimestamp with the specified time interval in milliseconds added to the receiver's time.

---

### timeZone

`public java.util.TimeZone timeZone()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns the time zone object associated with the receiver. You can explicitly set the time zone to an java.util.TimeZone object using a constructor that takes an java.util.TimeZone object as an argument. If you do not specify a time zone for an object at initialization time, NSTimestamp uses the default time zone for the locale.

---

### toString

`public String toString()`

Returns a string representation of the receiver in the form: "YYYY/MM/DD HH:MM:SS TimeZone".

---

### yearOfCommonEra

`public int yearOfCommonEra()`

Deprecated in the Java Foundation framework. Don't use this method. See the ["Class Description" (page 283)](#apple-infeiq2ii5duk) for [NSTimestamp](#apple-indeerkkivfek) for an alternative.

Returns a number that indicates the year, including the century, of the receiver (for example, 1995). The base year of the Common Era is 1 C.E. (which is the same as 1 A.D).

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
