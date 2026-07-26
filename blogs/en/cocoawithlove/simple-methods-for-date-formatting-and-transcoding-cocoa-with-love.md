---
title: 'Simple methods for date formatting and transcoding | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/05/simple-methods-for-date-formatting-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:1806b6a6852211da'
translated: false
---

> 原文：[Simple methods for date formatting and transcoding | Cocoa with Love](https://www.cocoawithlove.com/2009/05/simple-methods-for-date-formatting-and.html)　·　Cocoa with Love (Matt Gallagher)

There is no single-line method for converting between formatting date strings and date objects in Cocoa — the API opts for flexibility rather than simplicity. Unfortunately, this combines with documentation that omits, misdirects and occasionally misinforms, making NSDateFormatter one of the more confusing classes for new Cocoa programmers. In this post, I'll try to address some of the documentation issues and I'll present some methods that will turn NSDate into a formatted string or convert between date strings in a single method.

## Default, locale-based date formatting

Before I get into date formatting strings (which is the real purpose of this post) I will quickly show you how to get a string from an `NSDate`:

```objc
NSDate *date = [NSDate date];
NSDateFormatter *dateFormatter = [[[NSDateFormatter alloc] init] autorelease];
[dateFormatter setDateStyle:NSDateFormatterLongStyle];
NSString *dateString = [dateFormatter stringFromDate:date];
```

This code formats the string according to the user's preferences set in the International General Settings (iPhone) or System Preferences (Mac OS X).

Personally, I think this is verbose for such a common activity and normally use a category method on `NSDate` to reduce it:

```objc
@implementation NSDate (FormattedStrings)
- (NSString *)dateStringWithStyle:(NSDateFormatterStyle)style
{
    NSDateFormatter *dateFormatter = [[[NSDateFormatter alloc] init] autorelease];
    [dateFormatter setDateStyle:style];
    return [dateFormatter stringFromDate:self];
}
@end
```

This reduces the first code sample to:

```objc
 NSString *dateString = [[NSDate date] dateStringWithStyle:NSDateFormatterLongStyle];
```

If you need time strings instead of date strings, create a `timeStringWithStyle:` method by replacing the `setDateStyle:` invocation with `setTimeStyle:`.

I have read rants by other Objective-C programmers who hate seeing projects with hundreds of small categories for every little task.

Frankly, I've never understood the objection. In fact, I think lots of small categories used to choose the settings you prefer on top of common interfaces is essential for establishing consistent aesthetics for your program — your entire program will have the same style and you can easily update the aesthetic for the whole program by editing a single location.

An example would be to replace this `dateStringWithStyle:` method with a `dateStringWithProjectStyle` method that returns the appropriately configured string for use throughout your program. One of your projects might use `NSDateFormatterLongStyle` and the next might use a totally customized format (as I'll describe in the next sections) but you as a programmer can still invoke `dateStringWithProjectStyle` everywhere you need a string from an `NSDate`.

## Date formatting documentation issues

At its heart, `NSDateFormatter` is very simple to use and yet it repeatedly baffles new users. I don't think this is really the fault of the API as much as the history behind it and the effect that it has had on the documentation.

Despite `NSDateFormatterBehavior10_4` being the only date formatting you should ever use and the only style that _should_ exist in the documentation, Apple's documentation has the following quirks:

1. The actual syntax for `NSDateFormatterBehavior10_4` is never given in the documentation and you can easily miss the links to [Unicode Standard (tr35)](http://unicode.org/reports/tr35/tr35-4.html#Date_Format_Patterns) which describe it.
2. A majority of the pages in the date formatting documentation seem concerned with the old `NSDateFormatterBehavior10_0` style formatter behavior even though this is functionally deprecated.
3. The documentation for `defaultFormatterBehavior` claims `NSDateFormatterBehavior10_0` is the default style but it is actually `NSDateFormatterBehavior10_4` in Leopard and iPhoneSDK2.0.

Then, if you've been skimming through the documentation getting confused by the different styles, you may overlook one line at the top of the `NSDateFormatter` API reference page:

> **iPhone OS Note:** iPhone OS supports only the modern 10.4+ behavior. 10.0-style methods and format strings are not available on iPhone OS.

All that documentation in the iPhone SDK concerned with the old `NSDateFormatterBehavior10_0` style is completely meaningless — _you can't use `NSDateFormatterBehavior10_0` at all on the iPhone_.

Adding to the iPhone frustration, `NSDateFormatterBehavior10_0` will work in the simulator, causing headaches when code suddenly stops working on the device.

On Mac OS X, even though you can use `NSDateFormatterBehavior10_0`, it is deprecated for all practical purposes so you probably shouldn't. Annoyingly, since the documentation still claims `NSDateFormatterBehavior10_0` is the default, you should explicitly set the formatter behavior to `NSDateFormatterBehavior10_4` to remain safe — at least until the documented default is updated to formally match the actual default.

I don't mean to be cruel to Apple — documentation is difficult, time consuming and annoying — but I suspect these quirks in the documentation and behavior are responsible for a lot of confusion.

## Date formatting syntax

Setting a date formatting string looks like this:

```objc
NSDate *date = [NSDate date];
NSDateFormatter *dateFormatter = [[[NSDateFormatter alloc] init] autorelease];
[dateFormatter setFormatterBehavior:NSDateFormatterBehavior10_4];
[dateFormatter setDateFormat:@"dd MMM, yyyy"];
NSString *dateString = [dateFormatter stringFromDate:date];
```

This will create a string of the format "26 May, 2009". The arrangement of data in this string is determined by the format string passed to the `setDateFormat:` method.

A quick summary of the date formatting options useable in this format string:

| Character | Matches/Outputs | Multiples |
|---|---|---|
| y | Year | 1, 2 or 4 'y's will show the value, 2 digit zero-padded value or 4 digit zero-padded value respectively |
| M | Month | 1, 2, 3, 4 or 5 'M's will show the value, 2 digit zero-padded value, short name, long name or initial letter months |
| d | Day of Month | 1 or 2 'd's will show the value or 2 digit zero-padded value representation respectively. |
| E | Weekday | 1, 2, 3, 4 or 5 'e's will show the value weekday number, 2 digit zero-padded value weekday number, short name, long name or initial letter respectively. Weekday numbers starts on Sunday. Use lowercase 'e' for weekday numbers starting on Monday. |
| a | AM or PM | No repeat supported |
| h | Hour | 1 or 2 'h's will show the value or 2 digit zero-padded value representation respectively. Use uppercase for 24 hour time. |
| m | Minute | 1 or 2 'm's will show the value or 2 digit zero-padded value representation respectively. |
| s | Second | 1 or 2 's's will show the value or 2 digit zero-padded value representation respectively. |
| z | Timezone | 1, 2, 3 or 4 'z's will show short acronym, short name, long acronym, long name respectively. Use uppercase to show GMT offset instead of name — 1 or 2 digit zero-padded values shows GMT or RFC 822 respectively. |

Case is important — using the wrong case can cause parsing to fail. Use lowercase by default for all values except Month.

Alphabetic and numeric characters should be enclosed in single quotes (asterisk character) if you want them to pass through the parser as literal characters. A double asterisk will pass through as a single asterisk (self escaping). Most other punctuation and spaces will go through as normal except backslash which works like a normal C-string escape character to handle tabs, newlines and other special characters.

For the complete specification, including the more obscure options that I haven't bothered to list, see [Unicode Standard (tr35)](http://unicode.org/reports/tr35/tr35-4.html#Date_Format_Patterns).

## Date string transcoding

The date formatting options can also be used to parse strings. With parsing and output formatting, we can create a date string transcoder method in a category on `NSDateFormatter`:

```objc
+ (NSString *)dateStringFromString:(NSString *)sourceString
    sourceFormat:(NSString *)sourceFormat
    destinationFormat:(NSString *)destinationFormat
{
    NSDateFormatter *dateFormatter = [[[NSDateFormatter alloc] init] autorelease];
    [dateFormatter setFormatterBehavior:NSDateFormatterBehavior10_4];
    [dateFormatter setDateFormat:sourceFormat];
    NSDate *date = [dateFormatter dateFromString:sourceString];
    [dateFormatter setDateFormat:destinationFormat];
    return [dateFormatter stringFromDate:date];
}
```

We can use this method to convert one date string (for example "2007-08-11T19:30:00Z") into another ("7:30:00PM on August 11, 2007") in the following manner:

```objc
NSString *inputDateString = @"2007-08-11T19:30:00Z";
NSString *outputDateString = [NSDateFormatter
    dateStringFromString:inputDateString
    sourceFormat:@"yyyy-MM-dd'T'HH:mm:ss'Z'"
    destinationFormat:@"h:mm:ssa 'on' MMMM d, yyyy"];
```

## Calendar stuff

The `NSDateFormatter` class is just for parsing and formatting strings. You shouldn't use it to build dates from their components or to decompose dates into components. For that task, use `NSCalendar`. It's a little outside the scope of this post but since I know it will come up, here's how to set an `NSDate` to the 26th of May, 2009 using `NSCalendar`:

```objc
NSDateComponents *components = [[[NSDateComponents alloc] init] autorelease];
[components setDay:26];
[components setMonth:5];
[components setYear:2009];
NSCalendar *gregorian =
    [[[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar] autorelease];
NSDate *date = [gregorian dateFromComponents:components];
```

To get the components from a date, use:

```objc
unsigned unitFlags = NSYearCalendarUnit | NSMonthCalendarUnit |  NSDayCalendarUnit;
NSDate *date = [NSDate date];
NSCalendar *gregorian =
    [[[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar] autorelease];
NSDateComponents *components = [gregorian components:unitFlags fromDate:date];
```

## Conclusion

As I've said a few times now, the actual API for date formatting in Cocoa is simple. The only reason why I consider it a topic worthy of a post is that I still see at least one question a week on [StackOverflow](http://stackoverflow.com) and other forums asking why `NSDateFormatter` is failing in their code and the answer is normally because their code confuses the formatting behaviors, uses the wrong format specifiers or has otherwise misunderstood the required steps.

I hope what I've presented clears up these issues. Date formatting should be simple enough that you can write it once and never worry about it again.
