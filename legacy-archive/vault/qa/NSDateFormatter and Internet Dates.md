---
title: NSDateFormatter and Internet Dates
apple_id: DTS40009878
resource_type: QA
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-08-14'
source_url: https://developer.apple.com/library/archive/qa/qa1480/_index.html
archived_at: '2026-07-18T02:31:22.946853Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1480

# NSDateFormatter and Internet Dates

## Q:  I'm using NSDateFormatter to parse an Internet-style date, but this fails for some users in some regions. I've set a specific date format string; shouldn't that force NSDateFormatter to work independently of the user's region settings?

A: No. While setting a date format string will appear to work for most users, it's not the right solution to this problem. There are many places where format strings behave in unexpected ways. For example:

- A user can change their calendar (using System Preferences > Language & Region > Calendar on OS X, or Settings > General > International > Calendar on iOS). In that case NSDateFormatter will treat the numbers in the string you parse as if they were in the user's chosen calendar. For example, if the user selects the Buddhist calendar, parsing the year "2010" will yield an NSDate in 1467, because the year 2010 on the Buddhist calendar was the year 1467 on the (Gregorian) calendar that we use day-to-day.
- On iOS, the user can override the default AM/PM versus 24-hour time setting (via Settings > General > Date & Time > 24-Hour Time), which causes NSDateFormatter to rewrite the format string you set, which can cause your time parsing to fail.

To solve this problem properly, you have to understand that NSDateFormatter has two common roles:

- generating and parsing user-visible dates
- generating and parsing fixed-format dates, such as the RFC 3339-style dates used by many Internet protocols

If you're working with user-visible dates, you should avoid setting a fixed date format string because it's very hard to predict how your format string will be expressed in all possible user configurations. Rather, you should limit yourself to setting date and time styles (via `-[NSDateFormatter setDateStyle:]` and `-[NSDateFormatter setTimeStyle:]`) or generate your date format string from a template (using `+[NSDateFormatter dateFormatFromTemplate:options:locale:]`).

On the other hand, if you're working with fixed-format dates, you should first set the locale of the date formatter to something appropriate for your fixed format. In most cases the best locale to choose is "en_US_POSIX", a locale that's specifically designed to yield US English results regardless of both user and system preferences. "en_US_POSIX" is also invariant in time (if the US, at some point in the future, changes the way it formats dates, "en_US" will change to reflect the new behaviour, but "en_US_POSIX" will not), and between machines ("en_US_POSIX" works the same on iOS as it does on OS X, and as it it does on other platforms).

Once you've set "en_US_POSIX" as the locale of the date formatter, you can then set the date format string and the date formatter will behave consistently for all users.

Listing 1 shows how to use NSDateFormatter for both of the roles described above. First it creates a "en_US_POSIX" date formatter to parse the incoming [RFC 3339](http://www.ietf.org/rfc/rfc3339.txt) date string, using a fixed date format string and UTC as the time zone. Next, it creates a standard date formatter for rendering the date as a string to display to the user.

__Listing 1__  Parsing an RFC 3339 date-time

```objc
- (NSString *)userVisibleDateTimeStringForRFC3339DateTimeString:(NSString *)rfc3339DateTimeString
    // Returns a user-visible date time string that corresponds to the
    // specified RFC 3339 date time string. Note that this does not handle
    // all possible RFC 3339 date time strings, just one of the most common
    // styles.
{
    NSString *          userVisibleDateTimeString;
    NSDateFormatter *   rfc3339DateFormatter;
    NSLocale *          enUSPOSIXLocale;
    NSDate *            date;
    NSDateFormatter *   userVisibleDateFormatter;

    userVisibleDateTimeString = nil;

    // Convert the RFC 3339 date time string to an NSDate.

    rfc3339DateFormatter = [[[NSDateFormatter alloc] init] autorelease];

    enUSPOSIXLocale = [NSLocale localeWithLocaleIdentifier:@"en_US_POSIX"];

    [rfc3339DateFormatter setLocale:enUSPOSIXLocale];
    [rfc3339DateFormatter setDateFormat:@"yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"];
    [rfc3339DateFormatter setTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];

    date = [rfc3339DateFormatter dateFromString:rfc3339DateTimeString];
    if (date != nil) {

        // Convert the NSDate to a user-visible date string.

        userVisibleDateFormatter = [[[NSDateFormatter alloc] init] autorelease];

        [userVisibleDateFormatter setDateStyle:NSDateFormatterShortStyle];
        [userVisibleDateFormatter setTimeStyle:NSDateFormatterShortStyle];

        userVisibleDateTimeString = [userVisibleDateFormatter stringFromDate:date];
    }
    return userVisibleDateTimeString;
}
```

The code in Listing 1 is correct, but it's not as efficient as it could be. Specifically, it creates a date formatter, uses it once, and then throws it away. A better approach is the one shown in Listing 2. This holds on to its date formatters for subsequent reuse.

__Listing 2__  Parsing an RFC 3339 date-time more efficiently

```objc
static NSDateFormatter *    sUserVisibleDateFormatter;

- (NSString *)userVisibleDateTimeStringForRFC3339DateTimeString2:(NSString *)rfc3339DateTimeString
    // Returns a user-visible date time string that corresponds to the
    // specified RFC 3339 date time string. Note that this does not handle
    // all possible RFC 3339 date time strings, just one of the most common
    // styles.
{
    static NSDateFormatter *    sRFC3339DateFormatter;
    NSString *                  userVisibleDateTimeString;
    NSDate *                    date;

    // If the date formatters aren't already set up, do that now and cache them
    // for subsequence reuse.

    if (sRFC3339DateFormatter == nil) {
        NSLocale *                  enUSPOSIXLocale;

        sRFC3339DateFormatter = [[NSDateFormatter alloc] init];

        enUSPOSIXLocale = [NSLocale localeWithLocaleIdentifier:@"en_US_POSIX"];

        [sRFC3339DateFormatter setLocale:enUSPOSIXLocale];
        [sRFC3339DateFormatter setDateFormat:@"yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"];
        [sRFC3339DateFormatter setTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
    }

    if (sUserVisibleDateFormatter == nil) {
        sUserVisibleDateFormatter = [[NSDateFormatter alloc] init];

        [sUserVisibleDateFormatter setDateStyle:NSDateFormatterShortStyle];
        [sUserVisibleDateFormatter setTimeStyle:NSDateFormatterShortStyle];
    }

    // Convert the RFC 3339 date time string to an NSDate.
    // Then convert the NSDate to a user-visible date string.

    userVisibleDateTimeString = nil;

    date = [sRFC3339DateFormatter dateFromString:rfc3339DateTimeString];
    if (date != nil) {
        userVisibleDateTimeString = [sUserVisibleDateFormatter stringFromDate:date];
    }
    return userVisibleDateTimeString;
}
```

If you cache date formatters, or any other objects that depend on the user's current locale, you should subscribe to the `NSCurrentLocaleDidChangeNotification` notification and update your cached objects when the current locale changes. The code in Listing 2 defines `sUserVisibleDateFormatter` outside of the method so that other code, not shown, can update it as necessary. In contrast, `sRFC3339DateFormatter` is defined inside the method because, by design, it is not dependent on the user's locale settings.

Finally, if you're willing to look at solutions outside of the Cocoa space, it's very easy and efficient to parse and generate fixed-format dates using the standard C library functions `strptime_l` and `strftime_l`. Be aware that the C library also has the idea of a current locale. To guarantee a fixed date format, you should pass `NULL` to the `loc` parameter of these routines. This causes them to use the POSIX locale (also known as the C locale), which is equivalent to Cocoa's "en_US_POSIX" locale.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-14 | Removed a reference to a bug in +autoupdatingCurrentLocale (r. 7792724) that was fixed in iOS 4 (r. 15794178). Added a reference to date formatter templates. Made minor editorial changes. |
| 2010-04-29 | RFC 3339 dates are always in UTC, so set the time zone on the RFC 3339 date formatter to UTC. |
| 2010-03-31 | New document that explains how to use NSDateFormatter with fixed-format dates, like those in various Internet protocols. |

