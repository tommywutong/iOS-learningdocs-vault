---
title: Working with Date and Time in Cocoa (Part 2)
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-2/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:78d884cda2608bd3'
translated: false
---

> 原文：[Working with Date and Time in Cocoa (Part 2)](https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-2/)　·　Ole Begemann

# Working with Date and Time in Cocoa (Part 2)

In part 2 of my little series on date and time handling in Cocoa I am going to talk about date parsing and formatting. In other words: how to convert strings into date objects and vice versa. You should [read part 1 first](https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-1/) if you haven’t yet to get an overview of the classes used by Cocoa’s date and time system.

# NSDateFormatter

When working with date and time, two very common requirements are, (1) displaying dates in your UI, and (2) reading in date/time values from external sources like a web service or text file. Since humans are not very good at interpreting the second-based timestamps that `NSDate` uses to store dates internally, both of these tasks usually make it necessary to convert between `NSDate` and `NSString` or vice versa.

In the Foundation framework, the class to use for this task (in either direction) is [`NSDateFormatter`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSDateFormatter_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40003643). Let me show you how it works.

# 1. Turning Dates Into Strings

Let’s start with the easier (because less error-prone) of the two directions: turn an `NSDate` instance into a readable string. Usage of the `NSDateFormatter` class always involves three steps: (1) create the date formatter; (2) configure it; (3) send it a `stringFromDate:` message to get the result. Obviously, the configuration step is where the interesting stuff happens. We should differentiate between two separate use cases: do we want to create a human-readable output or do we need to create a string according to a specific format to be read by another API?

## Formatting for Humans: Let the User Decide

When displaying dates in your app’s UI, you should always take the user’s preferences into account. Fortunately, that is easy with `NSDateFormatter`. To simply convert an `NSDate` into an `NSString` use code like this:

```
NSDate *myDate = [NSDate date];
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
[dateFormatter setDateStyle:NSDateFormatterMediumStyle];
[dateFormatter setTimeStyle:NSDateFormatterMediumStyle];
NSString *myDateString = [dateFormatter stringFromDate:myDate];
NSLog(@"%@", myDateString);
```

With my current locale settings (German), the output looks like this: `22.11.2011 18:33:19`, but that’s just me. By default, `NSDateFormatter` observes the current user’s locale settings so other users might see results like `Nov 22, 2011 6:33:19 PM` or `2011-11-22 下午6:33:19` or even `२२-११-२०११ ६:३३:१९ अपराह्`, all for the same input and with the same code.

As a developer, you are not supposed to care about the actual output. Just use the `setDateStyle:` and `setTimeStyle:` methods to control how short or long the output should be. Possible values are `NSDateFormatterShortStyle`, `NSDateFormatterMediumStyle`, `NSDateFormatterLongStyle` and `NSDateFormatterFullStyle`; you can also use `NSDateFormatterNoStyle` to suppress the date or the time component in the resulting string.

The class method [`+localizedStringFromDate:dateStyle:timeStyle:`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSDateFormatter_Class/Reference/Reference.html#//apple_ref/doc/uid/20000447-SW52) provides a shorter way to achieve the same result as the code snippet above.

If you want to have more control over the output format, you can set a specific format using the `setDateFormat:` method. Note, though, that Apple specifically discourages that approach for human-readable dates since there is no date and time format that is accepted worldwide. `NSDateFormatter` understands the date format specifiers of the [Unicode spec for date formats](http://unicode.org/reports/tr35/tr35-10.html#Date_Format_Patterns). If you want to go this route, have a look at the [`+dateFormatFromTemplate:options:locale:`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSDateFormatter_Class/Reference/Reference.html#//apple_ref/doc/uid/20000447-SW53) class method. It lets you specify a string of date format specifiers that your output string should include and returns an appropriate date format string for the specified locale.

## Formatting for Machines: Controlled Environment Needed

It is a whole other matter if you need to create a date string according to the specification of a certain file format or API. In such a case, you usually have to follow a very strict spec to make sure the other party can read the string you are generating.[1](#fn:1)

It should be clear that we must use the `setDateFormat:` method here. But that is not enough. Remember from [part 1](https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-1/) that you can represent the same point in time very differently, depending on the calendar and time zone. By default, `NSDateFormatter` uses the user’s current calendar and time zone, which are possibly different from the requirements. Most file formats and web APIs use the western, Gregorian calendar, so we need to make sure that our date formatter uses it, too:

```
NSDate *myDate = [NSDate dateWithTimeIntervalSinceReferenceDate:343675999.713839];
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
NSCalendar *calendar = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
[dateFormatter setCalendar:calendar];
```

We must also make sure to set the date formatter’s _locale_ to a generic value so as not to run into conflict’s with the user’s locale settings, which can influence the naming of weekdays and months as well as the clocks 12/24 hour setting. The date formatter’s `setLocale:` method expects an instance of the [`NSLocale`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSLocale_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40003674) class. To create one, we need to specify a locale identifiers. These usually consist of a combination of a language and a country code, such as `@"en_US"`. For our needs, however, there exists the special locale identifier `@"en_US_POSIX"` that is [guaranteed to not change in the future](http://developer.apple.com/library/ios/#qa/qa1480/_index.html).

Note that a locale also includes a calendar setting so setting the calendar explicitly as we did above is no longer necessary (but does not hurt).

```
NSLocale *locale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US_POSIX"];
[dateFormatter setLocale:locale];
```

The date’s time zone can possibly be included in the formatted output string. But as I also mentioned in [part 1](https://oleb.net/blog/2011/11/working-with-date-and-time-in-cocoa-part-1/), time zone identifiers such as “+01:00”, “PST” or “CET” are notoriously ambiguous. In most cases, it’s best to stick with UTC:

```
NSTimeZone *timeZone = [NSTimeZone timeZoneForSecondsFromGMT:0];
[dateFormatter setTimeZone:timeZone];
```

Now, we are finally ready to set our date format and create the result string. For example, to format a date according to the common [RFC 3339](http://www.ietf.org/rfc/rfc3339.txt) ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) standard:

```
[dateFormatter setDateFormat:@"yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"];
NSString *myDateString = [dateFormatter stringFromDate:myDate];
// => 2011-11-22T17:33:19Z
```

Again, see the [Unicode standard mentioned above](http://unicode.org/reports/tr35/tr35-10.html#Date_Format_Patterns) for a list of possible format specifiers. Pay special attention to the year format specifier `@"yyyy"`. It is different than the capitalized `@YYYY`, which represents the year of the date’s week and not the year of the day. 99% of the time, you probably want to use @”yyyy”. I have seen this bug so many times in production code that it’s not funny anymore so make sure your unit tests catch it.[2](#fn:2)

Also note that I am using the literal character `'Z'` to represent the UTC time zone we set on the date formatter before. If you need to include the time zone in your format string, make sure to experiment with the possible time zone format specifiers (`z`, `Z`, `v`, `V`, each with 1-4 characters) and different time zones to really understand what you’re getting yourself into.[3](#fn:3) As I said, dealing with time zones is no fun, especially when it comes to ambiguous abbreviations or daylight savings time. It’s best to avoid if at all possible.

# 2. Turning Strings Into Dates

Let’s move on to the other side of `NSDateFormatter`: parsing a string representation of a date and/or time and converting it to an `NSDate` instance. Your main use case for this should be the parsing of dates you read in from a web service API or a text file.

## Parsing Machine-Generated Dates

In this case, you use the class much like in the reverse case that we just discussed:

1. .
2. locale and the UTC time zone.
3. Set the formatter’s date format string to the specified format.
4. .

For example, here is how to parse a date from an RSS feed entry of the form `Mon, 06 Sep 2009 16:45:00 -0900` as specified in [RFC 822](http://www.faqs.org/rfcs/rfc822.html):

```
NSString *myDateString = @"Mon, 06 Sep 2009 16:45:00 -0900";

NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
NSLocale *locale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US_POSIX"];
[dateFormatter setLocale:locale];
[dateFormatter setDateFormat:@"EEE, dd MMM yyyy HH:mm:ss Z"];

NSDate *myDate = [dateFormatter dateFromString:myDateString];
NSLog(@"%@", myDate);
// => 2009-09-07 01:45:00 +0000
```

Note how we did not set the date formatter’s time zone explicitly here. Instead, the `Z` character in the format string is now a format specifier for the time zone rather than the literal character it was in the example above. Also note that the output format of `NSLog()` shows date and time in UTC but it really represents the exact same point in time as the input string.

If a date formatter cannot parse the string, `dateFromString:` returns `nil`. Your code must be able to deal with this case gracefully.

## Parsing Free-Form Date Strings

What if you don’t know the exact format of the string, e.g. because you want to let the user enter a date and time in a free-form text field[4](#fn:4)? I am afraid that `NSDateFormatter` will probably not be a big help then. The class does have a `setLenient:` method that enables heuristics when parsing a string. However, even in lenient mode you are still required to specify an exact date format. In lenient mode, the formatter correctly parses a date string containing slashes (`@"03/11/2011 11:03:45"`) when the date format specifies blanks (`@"dd MMM yyyy HH:mm:ss"`) but that seems approximately to be the extent of what it can do.

For really lenient parsing with `NSDateFormatter`, you would probably have to try multiple formats and check for success after each attempt. The Unicode standard includes some [suggestions for lenient parsing](http://unicode.org/reports/tr35/tr35-10.html#Lenient_Parsing) if you want to go that route.

**Update November 23, 2011:** In most cases, you are probably better off providing the user a dedicated control for date and time entry that guarantees valid and unambiguous values, such as [`UIDatePicker`](http://developer.apple.com/library/ios/#documentation/uikit/reference/UIDatePicker_Class/Reference/UIDatePicker.html) or [`NSDatePicker`](http://developer.apple.com/library/mac/#documentation/Cocoa/Reference/ApplicationKit/Classes/NSDatePicker_Class/Reference/Reference.html).

### NSDataDetector to the Rescue!

A more promising approach might be the relatively new [`NSDataDetector`](http://developer.apple.com/library/ios/#documentation/Foundation/Reference/NSDataDetector_Class/Reference/Reference.html) class. Although not a classic member of the date and time handling classes in Cocoa, I want to mention it here for its ability to match, among other things, dates and times in free-form strings such as e-mail messages.

Because `NSDataDetector` is a special kind of regular expression, its API is completely different:

```
NSString *myDateString = @"24.11.2011 15:00";
NSError *error = nil;
NSDataDetector *detector = [NSDataDetector dataDetectorWithTypes:NSTextCheckingTypeDate error:&error];
NSArray *matches = [detector matchesInString:myDateString options:0 range:NSMakeRange(0, [myDateString length])];
for (NSTextCheckingResult *match in matches) {
    NSLog(@"Detected Date: %@", match.date);           // => 2011-11-24 14:00:00 +0000
    NSLog(@"Detected Time Zone: %@", match.timeZone);  // => (null)
    NSLog(@"Detected Duration: %f", match.duration);   // => 0.000000
}
```

In this case, the detection worked great[5](#fn:5), and the detector can also deal with relative strings such as `@"next Monday at 7 pm"` or `@"tomorrow at noon"`. `NSDataDetector` always seems to use the current locale and time zone to interpret dates in strings.

# Miscellaneous Findings

## Use Thread-Local Storage for NSDateFormatter

The `-[NSDateFormatter init]` method is quite expensive. If you need the same date formatter repeatedly, you should cache it, either in a static variable [as in this example in Apple’s Technical Q&A QA1480](http://developer.apple.com/library/ios/#qa/qa1480/_index.html) (see Listing 2) or, even better, by using [Thread-Local Storage](http://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/Multithreading/CreatingThreads/CreatingThreads.html#//apple_ref/doc/uid/10000057i-CH15-SW4) as explained by Alex Curylo in his article [Threadsafe Date Formatting](http://www.alexcurylo.com/blog/2011/07/05/threadsafe-date-formatting/).

## More Efficient Date Parsing

If you still encounter performance problems with `NSDateFormatter`, note this suggestion in the same [QA1480](http://developer.apple.com/library/ios/#qa/qa1480/_index.html):

> Finally, if you’re willing to look at solutions outside of the Cocoa space, it’s very easy and efficient to parse and generate fixed-format dates using the standard C library functions [`strptime_l`](http://developer.apple.com/library/mac/#documentation/darwin/reference/manpages/man3/strptime_l.3.html) and [`strftime_l`](http://developer.apple.com/library/mac/#documentation/darwin/reference/manpages/man3/strftime_l.3.html). Be aware that the C library also has the idea of a current locale. To guarantee a fixed date format, you should pass `NULL` to the `loc` parameter of these routines. This causes them to use the POSIX locale (also known as the C locale), which is equivalent to Cocoa’s “en_US_POSIX” locale.

For a data point, see Sam Soffes’s article how he [improved the performance of his date parsing code by a factor of more than 20×](http://samsoff.es/posts/how-to-drastically-improve-your-app-with-an-afternoon-and-instruments) by switching from `NSDateFormatter` to C-based date parsing.

## GMT != UTC

Cédric Luthi discovered a [seemingly weird `NSDateFormatter` behavior](https://twitter.com/0xced/status/137927496631988224) last weekend. See the following code:

```
NSString *dateString = @"0001-01-01 00:00:00 GMT";
NSDateFormatter *df = [[NSDateFormatter alloc] init];
[df setLocale:[[NSLocale alloc] initWithLocaleIdentifier:@"en_US_POSIX"]];
[df setDateFormat:@"yyyy-MM-dd HH:mm:ss zzz"];
NSDate *myDate = [df dateFromString: dateString];
NSLog(@"%@", myDate);
```

The result of the log statement: `0001-01-01 01:27:24 +0000`. Hm, 01:27:24? Where can such a weird result come from? It turns out the answer is the GMT time zone. Do the same with UTC as the time zone and the result is the expected `0001-01-01 00:00:00 +0000`. **Update November 23, 2011:** [Cédric notes on Twitter](https://twitter.com/0xced/status/139289644129984512) that Snow Leopard doesn’t seem to understand “UTC” and `@"0001-01-01 00:00:00 UTC"` returns a `nil` date. I find that very strange.

So it seems that when dealing with historical dates, UTC and GMT are not identical in Cocoa. Instead, the system seems to use past definitions of GMT that were valid at the date in question. When I investigated this further, I found out that only for dates later than 9 April, 1968, GMT and UTC are identical in Cocoa. So beware of the difference if your app deals with the past. Use UTC as your time zone if you want to interpret all dates in today’s time system.

1. Wouldn’t it be great if all web services used [Unix timestamps](https://en.wikipedia.org/wiki/Unix_timestamp) to represent dates? I could omit this entire section as the conversion from and to `NSDate` would be trivial. For some reason, however, most APIs use string-based dates, which at least have the advantage of being human-readable. [↩︎](#fnref:1)
2. For example, the year-of-week for 1 January 2005 is 2004 because that date belongs to the last calendar week of 2004 rather than the first calendar week of 2005. Use `NSDate *testDate = [NSDate dateWithTimeIntervalSinceReferenceDate:126273600.0]` in your unit test and assert that you get the correct result for both format strings `@"yyyy"` and `@"yyyy"`. [↩︎](#fnref:2)
3. By the way, [CodeRunner](http://krillapps.com/coderunner/), which I [reviewed recently here on the blog](https://oleb.net/blog/2011/10/coderunner/) is an awesome little app to experiment with date formatters. I used it constantly while writing this article. [↩︎](#fnref:3)
4. There are a number of apps that let you do just that, for example iCal in Lion, the great [Fantastical app](http://flexibits.com/fantastical) and Google Calendar. [↩︎](#fnref:4)
5. My time zone is one hour earlier than UTC, hence the time difference between input and output string. [↩︎](#fnref:5)
