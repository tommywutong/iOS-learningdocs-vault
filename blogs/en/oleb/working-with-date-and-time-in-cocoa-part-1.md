---
title: Working with Date and Time in Cocoa (Part 1)
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-1/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9d75b7c905e706f4'
translated: false
---

> 原文：[Working with Date and Time in Cocoa (Part 1)](https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-1/)　·　Ole Begemann

# Working with Date and Time in Cocoa (Part 1)

One of the most common problems I see newbies to Objective-C and Cocoa struggle with on [Stack Overflow](http://stackoverflow.com) is how to deal correctly with dates and times. Cocoa’s approach to date and time handling may indeed seem overly complex at first glance: where other languages’ standard libraries seem to get by with just one or two classes to cover this field, the Foundation framework employs a staggering array of separate classes: [`NSDate`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSDate_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40003641), [`NSDateComponents`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSDateComponents_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40003642), [`NSDateFormatter`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSDateFormatter_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40003643), [`NSCalendar`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSCalendar_Class/Reference/NSCalendar.html#//apple_ref/doc/uid/TP40003626), [`NSTimeZone`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSTimeZone_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40003748). These classes deal directly with date and time and you should be familiar with all of them. In addition, you should also understand the role of the [`NSLocale`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSLocale_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40003674) class.

Let’s have a look at those classes one by one. As you will see, the Cocoa approach to date and time handling is not only quite easy to understand but also extremely flexible.

# NSDate

`NSDate` is the central class of the date/time handling in Foundation, and at the same time the simplest imaginable. `NSDate` is nothing more than a wrapper around a single number: the number of seconds since 1 January, 2001, at 00:00 (midnight), [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)^[1](#fn:1). For values representing numbers of seconds, the framework uses a custom type, `NSTimeInterval`, which is currently defined as a 64-bit floating point value. According to the documentation, this is enough to yield an impressive [sub-millisecond precision over a range of 10,000 years](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_DataTypes/Reference/reference.html#//apple_ref/doc/uid/20000018-SW69).

## Represents an Absolute Point in Time

An `NSDate` object always represents an absolute point in time.^[2](#fn:2) This insight has two important consequences:

1. _There is no way to represent a certain date without including a specific time._ For instance, to say that a particular `NSDate` instance represents _17 November 2011_ makes no sense; you always have to include the particular time and time zone, such as _17 November 2011 00:00:00 +00:00_ (or any other time of your choice).

  If your app needs to store dates with less-than-second precision in order to represent entire days, months or years, you should either not use your own custom class for this or, better, define a rule how your app deals with the _unused_ components of the date (e.g., set the time components of the date to _00:00:00 +00:00_).

  If you are sloppy and store dates with arbitrary time components, you will run into problems later when you want to compare or group multiple dates.
2. _`NSDate` has no concept of time zones._ When it is midnight in London (_17 November 2011 00:00:00 +00:00_), it is only 6 pm on the day before in New York (_16 November 2011 18:00:00 -06:00_). Both dates represent the _same point in time_ and are thus _absolutely equal_ as far as `NSDate` is concerned.

  The implication of this is that you cannot store the time zone of a date and time in an `NSDate` object. If your app needs this information, you will have to store it in a different field. But more often than not, you will find that the time zone is actually not a field that should be stored with a date. Rather, it is a _runtime_ preference of the person that is currently using your app, and your app should probably display most dates in the user’s current time zone.

## How To Create An `NSDate` That Represents A Specific Date?

The easiest way to create an `NSDate` object is `[NSDate date];`. This will return an instance that represents the current moment and is often useful in code when it comes to storing creation or modification dates of records or to measure certain time intervals in your app.

The more generic task of creating an instance that represents a specific date and time turns out to be not so straightforward. There is the `+dateWithTimeIntervalSinceReferenceDate:` class method, but it requires you to know the interval in seconds between your desired date and the reference date (1 January 2001 00:00:00 +00:00). Turns out most people don’t count dates that way. That’s where the other classes come in.

# NSCalendar

Most people reading this will probably only ever use the same single calendar with its 12 months named January, February and so on, seven-day weeks, counting the years from the reputed birth of Jesus. It is easy to forget that (1) the current “western” [Gregorian Calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) has only been introduced in 1582 and (2) there are many more calendars in practical use around the world today. The Foundation framework can currently handle [ten different calendars](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSLocale_Class/Reference/Reference.html#//apple_ref/doc/uid/TP30001224-SW41)^[3](#fn:3).

It should be clear that, to specify a date unambiguously, we need to specify the calendar we use. For instance, while today’s date falls into the year 2011 in the familiar Gregorian calendar, the current year is 2554 and 5772 in the [Buddhist](https://en.wikipedia.org/wiki/Buddhist_calendar) and [Hebrew](https://en.wikipedia.org/wiki/Hebrew_calendar) calendars, respectively.

In Cocoa, a calendar is represented by the `NSCalendar` class. To create an instance of a specific calendar, pass one of the valid [calendar identifiers](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSLocale_Class/Reference/Reference.html#//apple_ref/doc/uid/TP30001224-SW41) to the initializer:

```
NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
NSCalendar *buddhist = [[NSCalendar alloc] initWithCalendarIdentifier:NSBuddhistCalendar];
NSCalendar *hebrew = [[NSCalendar alloc] initWithCalendarIdentifier:NSHebrewCalendar];
```

There are also two class methods, `+currentCalendar` and `+autoupdatingCurrentCalendar` that return the current user’s preferred calendar. Note that the object returned by the latter method automatically adapts to changes in System Preferences.

The rest of the class is pretty straightforward. You can query the calendar for its configuration, i.e., things like the number of days that are in a month or which day is considered the first day of the week. Have a look at the [documentation](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSCalendar_Class/Reference/NSCalendar.html#//apple_ref/doc/uid/TP40003626) to get a feel for what is possible. There are also methods to split a date into its calendrical components or do the reverse but we are not quite ready to do that yet.

# NSTimeZone

Any time specification is not precise enough without also indicating the time zone. I have already discussed that we need a way to reference time zones separately from `NSDate` and the `NSTimeZone` class does just that. There are several methods to create a time zone instance, the most straightforward being `+timeZoneForSecondsFromGMT:`.

Note, though, that the numeric offset from GMT is in many cases not enough to identify a specific time zone due to different daylight saving rules around the world. It is safer to specify a time zone by name using the `+timeZoneWithName:` method. Valid names are of the form `@"Europe/Berlin"`.^[4](#fn:4)

Another method, `+timeZoneWithAbbreviation:` should be handled with care. It is supposed to create time zones from common abbreviations such as “PST” or “CEST”. The problem is that these abbreviations are not always unique – different countries might use the same abbreviation for different time zones or different abbreviations for the same time zone. You should avoid this ambiguity if possible.

**Update November 22, 2011:** In addition, the rules which time zone abbreviation is understood under a specific locale setting can change. As Cédric Luthi found out, [Apple made a change in iOS 5](http://www.openradar.me/9944011) that causes the abbreviations “CET” and “CEST” (Central European (Summer) Time, very commonly used in Europe) to be no longer recognized if the user’s current locale setting is _en_US_. These abbreviations do still work with the _en_GB_ locale, however. Another reason to avoid them completely if you ask me.

Last but not least, use the `+systemTimeZone` method to get a reference to the user’s current time zone.

# NSDateComponents

We have almost everything we need now to manipulate dates in our code. Our fourth class, `NSDateComponents`, represents kind of the same information as `NSDate`: a single point in time. Unlike the latter, however, an `NSDateComponents` instance lets you access and manipulate every single calendrical component of that absolute point^[5](#fn:5), from the year down to the second and including such things as era, calendar, time zone and weekday.

## Constructing Dates

Knowing this, let’s construct a date that represents the beginning of Steve Jobs’s Macworld 2007 keynote when he first introduced the iPhone:

```
NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
NSTimeZone *pacificTime = [NSTimeZone timeZoneWithName:@"America/Los_Angeles"];

NSDateComponents *dateComps = [[NSDateComponents alloc] init];
[dateComps setCalendar:gregorian];
[dateComps setYear:2007];
[dateComps setMonth:1];
[dateComps setDay:9];
[dateComps setTimeZone:pacificTime];
[dateComps setHour:9]; // keynote started at 9:00 am
[dateComps setMinute:0]; // default value, can be omitted
[dateComps setSecond:0]; // default value, can be omitted

NSDate *dateOfKeynote = [dateComps date];
NSLog(@"Date of Keynote: %@", dateOfKeynote);
```

The output:

```
Date of Keynote: 2007-01-09 17:00:00 +0000
```

Hm, 17:00:00? But remember that `NSDate` does not care about time zones. When printing an `NSDate` with `NSLog()`, the system always uses UTC, which is 8 hours ahead of San Francisco (or 7 hours during daylight savings time). So the resulting date is indeed correct.

**Update November 28, 2011:** Thanks to Shan for [pointing out on Twitter](https://twitter.com/lakesidelatte/status/139682491207389184) that the code snippet above won’t work on OS X 10.6 or iOS 3.x because the `setCalendar:` and `setTimeZone:` methods are quite recent additions to `NSDateComponents`. To stay compatible with the older OSs, create your `NSDateComponents` instance just as above (without setting a calendar and time zone) and use the `dateFromComponents:` method of `NSCalendar`:

```
...
[gregorian setTimeZone:pacificTime];
NSDate *dateOfKeynote = [gregorian dateFromComponents:dateComps];
NSLog(@"Date of Keynote: %@", dateOfKeynote);
```

You see, it’s just as easy.

Now that we have an `NSDateComponents` instance, you would perhaps expect that you can get more information out of it. For example, let’s try to find out what day of the week the keynote was:

```
NSInteger weekday = [dateComps weekday]; // => -1 == NSUndefinedDateComponent
```

The documentation explains this:

> An instance of `NSDateComponents` is not responsible for answering questions about a date beyond the information with which it was initialized. For example, if you initialize one with May 6, 2004, its weekday is `NSUndefinedDateComponent`, not Thursday. To get the correct day of the week, you must create a suitable instance of `NSCalendar`, create an `NSDate` object using `dateFromComponents:` and then use `components:fromDate:` to retrieve the weekday.

Let’s try that:

```
NSDate *dateOfKeynote = [dateComps date]; // or: [gregorian dateFromComponents:dateComps]
NSDateComponents *weekdayComponents = [gregorian components:NSWeekdayCalendarUnit fromDate:dateOfKeynote];
NSInteger weekday = [weekdayComponents weekday]; // => 3 == Tuesday
```

Note how we can specify in the `-[NSCalendar components:fromDate:]` method which date components we are interested in (using a bit mask). Some of the components can be expensive so it makes sense to only ask for the information you really need.

## Date Calculations

The combination of `NSDateComponents` and `NSCalendar` is also the way to go for fancy date calculations. Say I want to create a date that goes back in time by exactly a month, a day and an hour from the current moment (using the current user’s calendar):

```
NSDate *now = [NSDate date];
NSDateComponents *comps = [[NSDateComponents alloc] init];
[comps setMonth:-1];
[comps setDay:-1];
[comps setHour:-1];
NSCalendar *calendar = [NSCalendar currentCalendar];
NSDate *newDate = [calendar dateByAddingComponents:comps toDate:now options:0];
```

`NSDateComponents` is an incredibly flexible und useful class. In combination with `NSCalendar`, you can probably do all the date calculations you ever thought of.

# Continued in Part 2: Date Parsing and Formatting

The classes I presented above give you a complete toolkit to work with date and time in your code. Two things are still missing, though: how to parse dates that come into your app as strings and how to output properly formatted dates as strings? Both of these tasks are handled by the `NSDateFormatter` class, which [I discuss in part 2 of this little series](https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-2/).

1. Or [GMT](https://en.wikipedia.org/wiki/Greenwich_Mean_Time), which is arguably the same, at least for our purposes. [↩︎](#fnref:1)
2. Yes, that means the date and time system does not deal with [relativity](https://en.wikipedia.org/wiki/Special_relativity). Cocoa is deeply rooted in [Newtonian physics](https://en.wikipedia.org/wiki/Absolute_time_and_space). **Update November 23, 2011:** We also pretend that [leap seconds](https://en.wikipedia.org/wiki/Leap_second) do not exist. [↩︎](#fnref:2)
3. With some limitations regarding the Chinese calendars. See the description of [valid calendar identifiers in the documentation](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSLocale_Class/Reference/Reference.html#//apple_ref/doc/uid/TP30001224-SW41). [↩︎](#fnref:3)
4. Apple uses the well-known [tz database](https://en.wikipedia.org/wiki/Tz_database). Log the result of `+knownTimeZoneNames` to get a list of all valid names. [↩︎](#fnref:4)
5. Implied in this is that `NSDateComponents` objects are mutable whereas `NSDate` instances are immutable. [↩︎](#fnref:5)
