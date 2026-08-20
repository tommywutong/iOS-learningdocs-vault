---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSTimeZone.html
archived_at: '2026-07-15T08:13:56.568908Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

# NSTimeZone

> **__Inherits from:__**
> : java.util.TimeZone : Object

> **__Implements:__**
> : Cloneable: Serializable: NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSTimeZone defines the behavior of time zone objects. Time zone objects represent geopolitical regions. Consequently, these objects have names for these regions. Time zone objects also represent a temporal offset, either plus or minus, from Greenwich Mean Time (GMT) and an abbreviation (such as "PST").

NSTimeZone provides several constructors to get time zone objects. The class also permits you to set the default time zone within your application ( [setDefaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxgzluirswmylvnr2fi2lnmvng63tf)). You can access this default time zone at any time with the [defaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwizlgmf2wy5cunfwwkwtpnzsq) static method, and with the [localTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwy33dmfwfi2lnmvng63tf) static method, you can get a relative time zone object that decodes itself to become the default time zone for any locale in which it finds itself.

Because NSTimeZone is a subclass of java.util.TimeZone, you can also use the java.util.TimeZone API with NSTimeZones.

__WARNING__ NSTimeZone is only intended to be used with NSTimestamp and NSTimestampFormatter. It produces incorrect results when used with Java's date-related classes.

Some NSTimestamp methods return date objects that are automatically bound to time zone objects. These date objects use the functionality of NSTimeZone to adjust dates for the proper locale. Unless you specify otherwise, objects returned from NSTimestamp are bound to the default time zone for the current locale.

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3dnrxw4zi)
>
> :
>
> : java.io.Serializable:
>
> : NSCoding
>
> : [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwizldn5sgkt3cnjswg5a): [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3dnrqxg42gn5zeg33emvza): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3fnzrw6zdfk5uxi2cdn5sgk4q)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl2oknkgs3lfljxw4zi)
>
> **Getting the default time zone**
>
> : [localTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwy33dmfwfi2lnmvng63tf): [defaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwizlgmf2wy5cunfwwkwtpnzsq): [setDefaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxgzluirswmylvnr2fi2lnmvng63tf): [resetSystemTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxezltmv2fg6ltorsw2vdjnvsvu33omu)
>
> **Getting time zone information**
>
> : [abbreviationDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwcytcojsxm2lboruw63senfrxi2lpnzqxe6i): [knownTimeZoneNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxww3tpo5xfi2lnmvng63tfjzqw2zlt)
>
> **Getting information about a specific time zone**
>
> : [abbreviation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3bmjrhezlwnfqxi2lpny): [abbreviationForTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3bmjrhezlwnfqxi2lpnzdg64sunfwwk43umfwxa): [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3omfwwk): [secondsFromGMT](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3tmvrw63teondhe33ni5gvi): [secondsFromGMTForTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3tmvrw63teondhe33ni5gvirtpojkgs3lfon2gc3lq): [isDaylightSavingTime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3joncgc6lmnftwq5ctmf3gs3thkruw2zi): [isDaylightSavingTimeForTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3joncgc6lmnftwq5ctmf3gs3thkruw2zkgn5zfi2lnmvzxiylnoa): [data](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3emf2gc)
>
> **Comparing time zones**
>
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3fof2wc3dt): [isEqualToTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3joncxc5lbnrkg6vdjnvsvu33omu)
>
> **Instance methods inherited from java.util.TimeZone**
>
> : [getAvailableIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwozluif3gc2lmmfrgyzkjirzq): [getDefault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwozluirswmylvnr2a): [getDisplayName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3hmv2ei2ltobwgc6komfwwk): [getID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3hmv2esra): [getOffset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3hmv2e6ztgonsxi): [getRawOffset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3hmv2feylxj5tgm43foq): [hasSameRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3imfzvgylnmvjhk3dfom): [inDaylightTime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3jnzcgc6lmnftwq5cunfwwk): [setDefault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxgzluirswmylvnr2a): [setID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3tmv2esra): [setRawOffset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3tmv2feylxj5tgm43foq): [useDaylightTime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3vonsuiylznruwo2dukruw2zi)

## Constructors

---

### NSTimeZone

`public NSTimeZone()`

This constructor is used internally to implement the java.io.Serializable and java.io.Externalizable interfaces and should be considered private. Use the static factory methods to create time zones.

`protected NSTimeZone( String aTimeZoneName, NSData data)`

This constructor is used internally by NSTimeZone and should be considered private. Use the static factory methods to create time zones.

---

## Static Methods

---

### abbreviationDictionary

`public static NSDictionary abbreviationDictionary()`

Returns a dictionary holding the mappings of time zone abbreviations to time zone names.

More than one time zone may have the same abbreviation. For example, US/Pacific and Canada/Pacific both use the abbreviation "PST." In these cases __abbreviationDictionary__ chooses a single name to map the abbreviation to.

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates and returns an NSTimeZone from the data in _coder._

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq) Interface Description

---

### defaultTimeZone

`public static synchronized NSTimeZone defaultTimeZone()`

Returns the default time zone set for your application. If no default time zone has been set, this method invokes [systemTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxg6ltorsw2vdjnvsvu33omu) and returns the system time zone.

__See Also:__ [localTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwy33dmfwfi2lnmvng63tf), [setDefaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxgzluirswmylvnr2fi2lnmvng63tf), [systemTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxg6ltorsw2vdjnvsvu33omu)

---

### getAvailableIDs

`public static String[] getAvailableIDs()`

See the method description for __getAvailableIDs__ in the java.util.TimeZone class specification.

---

### getDefault

`public static java.util.TimeZone getDefault()`

See the method description for __getDefault__ in the java.util.TimeZone class specification.

---

### knownTimeZoneNames

`public static NSArray knownTimeZoneNames()`

Returns an array of strings listing the names of all the time zones known to the system.

---

### localTimeZone

`public static NSTimeZone localTimeZone()`

Returns an object that forwards all messages to the default time zone for your application. This behavior is particularly useful for NSTimestamp objects that are archived or sent as Distributed Objects and may be interpreted in different locales.

__See Also:__ [defaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwizlgmf2wy5cunfwwkwtpnzsq), [setDefaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxgzluirswmylvnr2fi2lnmvng63tf)

---

### resetSystemTimeZone

`public static synchronized void resetSystemTimeZone()`

Clears the previously determined system time zone, if any. Subsequent calls to [systemTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxg6ltorsw2vdjnvsvu33omu) will attempt to redetermine the system time zone.

---

### setDefault

`public static synchronized void setDefault(java.util.TimeZone zone)`

See the method description for __setDefault__ in the java.util.TimeZone class specification.

---

### setDefaultTimeZone

`public static synchronized void setDefaultTimeZone(NSTimeZone aTimeZone)`

Sets the time zone appropriate for your application. There can be only one default time zone, so by setting a new default time zone, you lose the previous one.

__See Also:__ [defaultTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwizlgmf2wy5cunfwwkwtpnzsq), [localTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxwy33dmfwfi2lnmvng63tf)

---

### systemTimeZone

`public static synchronized NSTimeZone systemTimeZone()`

Returns the time zone currently used by the system. If it can't figure out the current time zone, returns the GMT time zone.

---

### timeZoneForSecondsFromGMT

`public static synchronized NSTimeZone timeZoneForSecondsFromGMT(int seconds)`

Returns a time zone object with _seconds_ offset from Greenwich Mean Time. The name of the new time zone is GMT +/- the offset, in hours and minutes. Time zones created with this never have daylight savings and the offset is constant no matter the date; the name and abbreviation do NOT follow the POSIX convention of minutes-west.

__See Also:__ [timeZoneWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxi2lnmvng63tfk5uxi2comfwwk)

---

### timeZoneWithName

`public static synchronized NSTimeZone timeZoneWithName( String aTimeZoneName, boolean trybbreviation)`

Returns the time zone object identified by the name _aTimeZoneName_. If _tryAbbreviation_ is `false`, this method searches the time zone information directory for matching names. If _tryAbbreviation_ is `true`, this method attempts to resolve the abbreviation to a name using the abbreviation dictionary. Returns `null` if there is no match on the name.

__See Also:__ [timeZoneForSecondsFromGMT](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxi2lnmvng63tfizxxeu3fmnxw4zdtizzg63khjvka), [knownTimeZoneNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxww3tpo5xfi2lnmvng63tfjzqw2zlt)

---

### timeZoneWithNameAndData

`public static synchronized NSTimeZone timeZoneWithNameAndData( String aTimeZoneName, NSData data)`

Returns the time zone with the name _aTimeZoneName_ whose data has been initialized using the contents of _data_. You should not call this method directly-use [timeZoneWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgvdjnvsvu33omuxxi2lnmvng63tfk5uxi2comfwwk) instead.

---

## Instance Methods

---

### abbreviation

`public String abbreviation()`

Returns the abbreviation for the time zone, such as "EDT" (Eastern Daylight Time). Invokes [abbreviationForTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3bmjrhezlwnfqxi2lpnzdg64sunfwwk43umfwxa) with the current date as the argument.

---

### abbreviationForTimestamp

`public String abbreviationForTimestamp(NSTimestamp aTimestamp)`

Returns the abbreviation for the time zone object at the date specified by _aTimestamp_. Note that the abbreviation may be different at different dates. For example, during Daylight Savings Time the US/Eastern time zone has an abbreviation of "EDT." At other times, its abbreviation is "EST."

---

### classForCoder

`public Class classForCoder()`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq).

__See Also:__ [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) (NSCoding)

---

### clone

`public Object clone()`

Simply returns the receiver. Since NSArrays are immutable, there's no need to make an actual clone.

---

### data

`public NSData data()`

Returns the data that stores the information used by the time zone. This data should be treated as an opaque object.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description for [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the NSCoding interface specification.

---

### equals

`public boolean equals(Object anObject)`

Returns `true` if _anObject_ is an NSTimeZone and its contents are equal to the receiver's or `false` otherwise. If you know that _anObject_ is an NSTimestamp, use the more efficient method [isEqualToTimeZone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3joncxc5lbnrkg6vdjnvsvu33omu) instead.

---

### getDisplayName

`public String getDisplayName( boolean daylight, int style, java.util.Locale locale)`

Returns the name of the equivalent java.util.SimpleTimeZone if one exists. Otherwise returns the receiver's geopolitical region name.

---

### getID

`public String getID()`

Returns the receiver's geopolitical region name.

---

### getOffset

`public int getOffset( int era, int year, int month, int day, int dayOfWeek, int milliseconds)`

See the method description for __getOffset__ in the java.util.TimeZone class specification.

---

### getRawOffset

`public int getRawOffset()`

See the method description for __getRawOffset__ in the java.util.TimeZone class specification. For NSTimeZones, this method always returns 0.

---

### hashCode

`public synchronized int hashCode()`

See the method description for __hashCode__ in the Object class specification.

---

### hasSameRules

`public boolean hasSameRules(java.util.TimeZone other)`

Returns `true` if _other_ is the same as the receiver (as determined by [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3fof2wc3dt).).

---

### inDaylightTime

`public boolean inDaylightTime(java.util.Date date)`

See the method description for __inDaylightTime__ in the java.util.TimeZone class specification.

---

### isDaylightSavingTime

`public boolean isDaylightSavingTime()`

Returns `true` if the time zone is currently using Daylight Savings Time. This method invokes [isDaylightSavingTimeForTimestamp](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkruw2zk2n5xgkl3joncgc6lmnftwq5ctmf3gs3thkruw2zkgn5zfi2lnmvzxiylnoa) with the current date as the argument.

---

### isDaylightSavingTimeForTimestamp

`public boolean isDaylightSavingTimeForTimestamp(NSTimestamp aTimestamp)`

Returns `true` if the time zone uses Daylight Savings Time at the date specified by _aTimestamp_.

---

### isEqualToTimeZone

`public boolean isEqualToTimeZone(NSTimeZone aTimeZone)`

Returns `true` if _aTimeZone_ and the receiving time zone have the same name and data.

---

### name

`public String name()`

Returns the geopolitical region name that identifies the time zone.

---

### readExternal

`public void readExternal(java.io.ObjectInput input) throws java.io.IOException,ClassNotFoundException`

Description forthcoming.

---

### readResolve

`public Object readResolve() throws java.io.ObjectStreamException`

Conformance to java.io.Serializable.

---

### secondsFromGMT

`public int secondsFromGMT()`

Returns the current difference in seconds between the time zone and Greenwich Mean Time.

---

### secondsFromGMTForTimestamp

`public int secondsFromGMTForTimestamp(NSTimestamp aTimestamp)`

Returns the difference in seconds between the time zone and Greenwich Mean Time at the date specified by _aTimestamp_. This may be different from the current difference if the time zone changes its offset from GMT at different points in the year-for example, the U.S. time zones change with daylight savings time.

---

### setID

`public void setID(String ID)`

Throws an IllegalStateException because NSTimeZones are immutable.

---

### setRawOffset

`public void setRawOffset(int offsetMillis)`

Throws an IllegalStateException because NSTimeZones are immutable.

---

### toString

`public String toString()`

Returns a string representation of the receiver that indicates the receiver's name, the receiver's current offset from GMT, and whether the receiver is currently using Daylight Savings Time.

---

### useDaylightTime

`public boolean useDaylightTime()`

See the method description for __useDaylightTime__ in the java.util.TimeZone class specification.

---

### writeExternal

`public void writeExternal( java.io.ObjectOutput output) throws java.io.IOException`

Description forthcoming.

---

## Notifications

---

### SystemTimeZoneDidChangeNotification

`public static final String SystemTimeZoneDidChangeNotification;`

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
