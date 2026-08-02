---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/Foundation.html
archived_at: '2026-07-18T02:54:12.639746Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# Foundation Changes

## Foundation

FoundationErrors.hAdded [NSUbiquitousFileErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfileerrormaximum)Added [NSUbiquitousFileErrorMinimum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfileerrorminimum)Added [NSUbiquitousFileNotUploadedDueToQuotaError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfilenotuploadedduetoquotaerror)Added [NSUbiquitousFileUbiquityServerNotAvailable](https://developer.apple.com/documentation/foundation/nsubiquitousfileubiquityservernotavailable)Added [NSUbiquitousFileUnavailableError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsubiquitousfileunavailableerror)NSArray.hAdded [-[NSArray firstObject]](https://developer.apple.com/documentation/foundation/nsarray/1412852-firstobject)Added [-[NSArray init]](https://developer.apple.com/documentation/foundation/nsarray/1414315-init)Added [-[NSMutableArray init]](https://developer.apple.com/documentation/foundation/nsmutablearray/1407556-init)Modified [+[NSArray array]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/array)

|  | Declaration |
| --- | --- |
| From | + (id)array |
| To | + (instancetype)array |

Modified [+[NSArray arrayWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithArray:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithArray:(NSArray \*)array |
| To | + (instancetype)arrayWithArray:(NSArray \*)array |

Modified [+[NSArray arrayWithObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObject:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithObject:(id)anObject |
| To | + (instancetype)arrayWithObject:(id)anObject |

Modified [+[NSArray arrayWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObjects:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithObjects:(id)firstObj, ... |
| To | + (instancetype)arrayWithObjects:(id)firstObj, ... |

Modified [+[NSArray arrayWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | + (instancetype)arrayWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [-[NSArray initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithArray:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array |
| To | - (instancetype)initWithArray:(NSArray \*)array |

Modified [-[NSArray initWithArray:copyItems:]](https://developer.apple.com/documentation/foundation/nsarray/1408557-initwitharray)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array copyItems:(BOOL)flag |
| To | - (instancetype)initWithArray:(NSArray \*)array copyItems:(BOOL)flag |

Modified [-[NSArray initWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id)firstObj, ... |
| To | - (instancetype)initWithObjects:(id)firstObj, ... |

Modified [-[NSArray initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [+[NSMutableArray arrayWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSMutableArray/arrayWithCapacity:)

|  | Declaration |
| --- | --- |
| From | + (id)arrayWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)arrayWithCapacity:(NSUInteger)numItems |

Modified [-[NSMutableArray initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

NSCalendar.hAdded [-[NSCalendar AMSymbol]](https://developer.apple.com/documentation/foundation/nscalendar/1416226-amsymbol)Added [-[NSCalendar PMSymbol]](https://developer.apple.com/documentation/foundation/nscalendar/1416343-pmsymbol)Added [+[NSCalendar calendarWithIdentifier:]](https://developer.apple.com/documentation/foundation/nscalendar/1412400-calendarwithidentifier)Added [-[NSCalendar compareDate:toDate:toUnitGranularity:]](https://developer.apple.com/documentation/foundation/nscalendar/1415661-compare)Added [-[NSCalendar component:fromDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1416505-component)Added [-[NSCalendar components:fromDateComponents:toDateComponents:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1411297-components)Added [-[NSCalendar componentsInTimeZone:fromDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1413194-components)Added [-[NSCalendar date:matchesComponents:]](https://developer.apple.com/documentation/foundation/nscalendar/1407954-date)Added [-[NSCalendar dateByAddingUnit:value:toDate:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1407989-datebyaddingunit)Added [-[NSCalendar dateBySettingHour:minute:second:ofDate:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1407363-date)Added [-[NSCalendar dateBySettingUnit:value:ofDate:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1417915-datebysettingunit)Added [-[NSCalendar dateWithEra:year:month:day:hour:minute:second:nanosecond:]](https://developer.apple.com/documentation/foundation/nscalendar/1415254-date)Added [-[NSCalendar dateWithEra:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:]](https://developer.apple.com/documentation/foundation/nscalendar/1413628-datewithera)Added [-[NSCalendar enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nscalendar/1413938-enumeratedates)Added [-[NSCalendar eraSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1415038-erasymbols)Added [-[NSCalendar getEra:year:month:day:fromDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1418143-getera)Added [-[NSCalendar getEra:yearForWeekOfYear:weekOfYear:weekday:fromDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1410912-getera)Added [-[NSCalendar getHour:minute:second:nanosecond:fromDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1415012-gethour)Added [-[NSCalendar isDate:equalToDate:toUnitGranularity:]](https://developer.apple.com/documentation/foundation/nscalendar/1411431-isdate)Added [-[NSCalendar isDate:inSameDayAsDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1417649-isdate)Added [-[NSCalendar isDateInToday:]](https://developer.apple.com/documentation/foundation/nscalendar/1417149-isdateintoday)Added [-[NSCalendar isDateInTomorrow:]](https://developer.apple.com/documentation/foundation/nscalendar/1410279-isdateintomorrow)Added [-[NSCalendar isDateInWeekend:]](https://developer.apple.com/documentation/foundation/nscalendar/1412175-isdateinweekend)Added [-[NSCalendar isDateInYesterday:]](https://developer.apple.com/documentation/foundation/nscalendar/1409356-isdateinyesterday)Added [-[NSCalendar longEraSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1414285-longerasymbols)Added [-[NSCalendar monthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1414872-monthsymbols)Added [-[NSCalendar nextDateAfterDate:matchingComponents:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1416165-nextdateafterdate)Added [-[NSCalendar nextDateAfterDate:matchingHour:minute:second:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1416814-nextdateafterdate)Added [-[NSCalendar nextDateAfterDate:matchingUnit:value:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1417170-nextdateafterdate)Added [-[NSCalendar nextWeekendStartDate:interval:options:afterDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1409905-nextweekendstartdate)Added [-[NSCalendar quarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1411517-quartersymbols)Added [-[NSCalendar rangeOfWeekendStartDate:interval:containingDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1413286-rangeofweekendstartdate)Added [-[NSCalendar shortMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1408952-shortmonthsymbols)Added [-[NSCalendar shortQuarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1414864-shortquartersymbols)Added [-[NSCalendar shortStandaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1418180-shortstandalonemonthsymbols)Added [-[NSCalendar shortStandaloneQuarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1409823-shortstandalonequartersymbols)Added [-[NSCalendar shortStandaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1413871-shortstandaloneweekdaysymbols)Added [-[NSCalendar shortWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1407268-shortweekdaysymbols)Added [-[NSCalendar standaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1409598-standalonemonthsymbols)Added [-[NSCalendar standaloneQuarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1407159-standalonequartersymbols)Added [-[NSCalendar standaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1411219-standaloneweekdaysymbols)Added [-[NSCalendar startOfDayForDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1417161-startofdayfordate)Added [-[NSCalendar veryShortMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1412779-veryshortmonthsymbols)Added [-[NSCalendar veryShortStandaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1408035-veryshortstandalonemonthsymbols)Added [-[NSCalendar veryShortStandaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1418273-veryshortstandaloneweekdaysymbol)Added [-[NSCalendar veryShortWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1417207-veryshortweekdaysymbols)Added [-[NSCalendar weekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1412939-weekdaysymbols)Added -[NSDateComponents isValidDate]Added [-[NSDateComponents isValidDateInCalendar:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1412707-isvaliddate)Added [-[NSDateComponents nanosecond]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415730-nanosecond)Added [-[NSDateComponents setNanosecond:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415730-nanosecond)Added [-[NSDateComponents setValue:forComponent:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415961-setvalue)Added [-[NSDateComponents valueForComponent:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416763-value)Added [NSCalendarDayChangedNotification](https://developer.apple.com/documentation/foundation/nscalendardaychangednotification)Added [NSCalendarIdentifierBuddhist](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1414245-buddhist)Added [NSCalendarIdentifierChinese](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1407198-chinese)Added [NSCalendarIdentifierCoptic](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1410834-coptic)Added [NSCalendarIdentifierEthiopicAmeteAlem](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1409712-ethiopicametealem)Added [NSCalendarIdentifierEthiopicAmeteMihret](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1417448-ethiopicametemihret)Added [NSCalendarIdentifierGregorian](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1410488-gregorian)Added [NSCalendarIdentifierHebrew](https://developer.apple.com/documentation/foundation/nscalendaridentifierhebrew)Added [NSCalendarIdentifierISO8601](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1410413-iso8601)Added [NSCalendarIdentifierIndian](https://developer.apple.com/documentation/foundation/nscalendaridentifierindian)Added [NSCalendarIdentifierIslamic](https://developer.apple.com/documentation/foundation/nscalendaridentifierislamic)Added [NSCalendarIdentifierIslamicCivil](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1414615-islamiccivil)Added [NSCalendarIdentifierJapanese](https://developer.apple.com/documentation/foundation/nscalendaridentifierjapanese)Added [NSCalendarIdentifierPersian](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1415601-persian)Added [NSCalendarIdentifierRepublicOfChina](https://developer.apple.com/documentation/foundation/nscalendaridentifierrepublicofchina)Added [NSCalendarMatchFirst](https://developer.apple.com/documentation/foundation/nscalendar/options/1410281-matchfirst)Added [NSCalendarMatchLast](https://developer.apple.com/documentation/foundation/nscalendar/options/1412627-matchlast)Added [NSCalendarMatchNextTime](https://developer.apple.com/documentation/foundation/nscalendar/options/1411904-matchnexttime)Added [NSCalendarMatchNextTimePreservingSmallerUnits](https://developer.apple.com/documentation/foundation/nscalendaroptions/nscalendarmatchnexttimepreservingsmallerunits)Added [NSCalendarMatchPreviousTimePreservingSmallerUnits](https://developer.apple.com/documentation/foundation/nscalendaroptions/nscalendarmatchprevioustimepreservingsmallerunits)Added [NSCalendarMatchStrictly](https://developer.apple.com/documentation/foundation/nscalendar/options/1416455-matchstrictly)Added [NSCalendarOptions](https://developer.apple.com/documentation/foundation/nscalendaroptions)Added [NSCalendarSearchBackwards](https://developer.apple.com/documentation/foundation/nscalendar/options/1416053-searchbackwards)Added [NSCalendarUnitCalendar](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitcalendar)Added [NSCalendarUnitDay](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitday)Added [NSCalendarUnitEra](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitera)Added [NSCalendarUnitHour](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunithour)Added [NSCalendarUnitMinute](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitminute)Added [NSCalendarUnitMonth](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitmonth)Added [NSCalendarUnitNanosecond](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitnanosecond)Added [NSCalendarUnitQuarter](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitquarter)Added [NSCalendarUnitSecond](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitsecond)Added [NSCalendarUnitTimeZone](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunittimezone)Added [NSCalendarUnitWeekOfMonth](https://developer.apple.com/documentation/foundation/nscalendar/unit/1412656-weekofmonth)Added [NSCalendarUnitWeekOfYear](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411748-weekofyear)Added [NSCalendarUnitWeekday](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitweekday)Added [NSCalendarUnitWeekdayOrdinal](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunitweekdayordinal)Added [NSCalendarUnitYear](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunityear)Added [NSCalendarUnitYearForWeekOfYear](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarunityearforweekofyear)Added [NSCalendarWrapComponents](https://developer.apple.com/documentation/foundation/nscalendar/options/1408451-wrapcomponents)Added [NSDateComponentUndefined](https://developer.apple.com/documentation/foundation/nsdatecomponentundefined)Added #def NS_CALENDAR_DEPRECATEDAdded #def NS_CALENDAR_DEPRECATED_MACAdded #def NS_CALENDAR_ENUM_DEPRECATEDModified [-[NSCalendar components:fromDate:]](https://developer.apple.com/documentation/foundation/nscalendar/1414841-components)

|  | Declaration |
| --- | --- |
| From | - (NSDateComponents \*)components:(NSUInteger)unitFlags fromDate:(NSDate \*)date |
| To | - (NSDateComponents \*)components:(NSCalendarUnit)unitFlags fromDate:(NSDate \*)date |

Modified [-[NSCalendar components:fromDate:toDate:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1407925-components)

|  | Declaration |
| --- | --- |
| From | - (NSDateComponents \*)components:(NSUInteger)unitFlags fromDate:(NSDate \*)startingDate toDate:(NSDate \*)resultDate options:(NSUInteger)opts |
| To | - (NSDateComponents \*)components:(NSCalendarUnit)unitFlags fromDate:(NSDate \*)startingDate toDate:(NSDate \*)resultDate options:(NSCalendarOptions)opts |

Modified [-[NSCalendar dateByAddingComponents:toDate:options:]](https://developer.apple.com/documentation/foundation/nscalendar/1409577-date)

|  | Declaration |
| --- | --- |
| From | - (NSDate \*)dateByAddingComponents:(NSDateComponents \*)comps toDate:(NSDate \*)date options:(NSUInteger)opts |
| To | - (NSDate \*)dateByAddingComponents:(NSDateComponents \*)comps toDate:(NSDate \*)date options:(NSCalendarOptions)opts |

NSData.hAdded [-[NSData base64EncodedDataWithOptions:]](https://developer.apple.com/documentation/foundation/nsdata/1412739-base64encodeddatawithoptions)Added [-[NSData base64EncodedStringWithOptions:]](https://developer.apple.com/documentation/foundation/nsdata/1413546-base64encodedstringwithoptions)Added [-[NSData base64Encoding]](https://developer.apple.com/documentation/foundation/nsdata/1547242-base64encoding)Added [-[NSData enumerateByteRangesUsingBlock:]](https://developer.apple.com/documentation/foundation/nsdata/1408400-enumeratebyterangesusingblock)Added [-[NSData initWithBase64EncodedData:options:]](https://developer.apple.com/documentation/foundation/nsdata/1417833-init)Added [-[NSData initWithBase64EncodedString:options:]](https://developer.apple.com/documentation/foundation/nsdata/1410081-initwithbase64encodedstring)Added [-[NSData initWithBase64Encoding:]](https://developer.apple.com/documentation/foundation/nsdata/1547237-init)Added [-[NSData initWithBytesNoCopy:length:deallocator:]](https://developer.apple.com/documentation/foundation/nsdata/1417337-initwithbytesnocopy)Added NSData(NSDataBase64Encoding)Added [NSDataBase64DecodingIgnoreUnknownCharacters](https://developer.apple.com/documentation/foundation/nsdata/base64decodingoptions/1410087-ignoreunknowncharacters)Added [NSDataBase64DecodingOptions](https://developer.apple.com/documentation/foundation/nsdata/base64decodingoptions)Added [NSDataBase64Encoding64CharacterLineLength](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions/1407872-linelength64characters)Added [NSDataBase64Encoding76CharacterLineLength](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions/1413700-linelength76characters)Added [NSDataBase64EncodingEndLineWithCarriageReturn](https://developer.apple.com/documentation/foundation/nsdatabase64encodingoptions/nsdatabase64encodingendlinewithcarriagereturn)Added [NSDataBase64EncodingEndLineWithLineFeed](https://developer.apple.com/documentation/foundation/nsdatabase64encodingoptions/nsdatabase64encodingendlinewithlinefeed)Added [NSDataBase64EncodingOptions](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions)NSDate.hModified [+[NSDate date]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/date)

|  | Declaration |
| --- | --- |
| From | + (id)date |
| To | + (instancetype)date |

Modified [+[NSDate dateWithTimeInterval:sinceDate:]](https://developer.apple.com/documentation/foundation/nsdate/1591578-datewithtimeinterval)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeInterval:(NSTimeInterval)ti sinceDate:(NSDate \*)date |
| To | + (instancetype)dateWithTimeInterval:(NSTimeInterval)secsToBeAdded sinceDate:(NSDate \*)date |

Modified [+[NSDate dateWithTimeIntervalSince1970:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithTimeIntervalSince1970:)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeIntervalSince1970:(NSTimeInterval)secs |
| To | + (instancetype)dateWithTimeIntervalSince1970:(NSTimeInterval)secs |

Modified [+[NSDate dateWithTimeIntervalSinceNow:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithTimeIntervalSinceNow:)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeIntervalSinceNow:(NSTimeInterval)secs |
| To | + (instancetype)dateWithTimeIntervalSinceNow:(NSTimeInterval)secs |

Modified [+[NSDate dateWithTimeIntervalSinceReferenceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithTimeIntervalSinceReferenceDate:)

|  | Declaration |
| --- | --- |
| From | + (id)dateWithTimeIntervalSinceReferenceDate:(NSTimeInterval)secs |
| To | + (instancetype)dateWithTimeIntervalSinceReferenceDate:(NSTimeInterval)ti |

Modified [-[NSDate init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/init)

|  | Declaration |
| --- | --- |
| From | - (id)init |
| To | - (instancetype)init |

Modified [-[NSDate initWithTimeInterval:sinceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeInterval:sinceDate:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeInterval:(NSTimeInterval)secsToBeAdded sinceDate:(NSDate \*)anotherDate |
| To | - (instancetype)initWithTimeInterval:(NSTimeInterval)secsToBeAdded sinceDate:(NSDate \*)date |

Modified [-[NSDate initWithTimeIntervalSince1970:]](https://developer.apple.com/documentation/foundation/nsdate/1416453-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeIntervalSince1970:(NSTimeInterval)ti |
| To | - (instancetype)initWithTimeIntervalSince1970:(NSTimeInterval)secs |

Modified [-[NSDate initWithTimeIntervalSinceNow:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeIntervalSinceNow:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeIntervalSinceNow:(NSTimeInterval)secs |
| To | - (instancetype)initWithTimeIntervalSinceNow:(NSTimeInterval)secs |

Modified [-[NSDate initWithTimeIntervalSinceReferenceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeIntervalSinceReferenceDate:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithTimeIntervalSinceReferenceDate:(NSTimeInterval)secsToBeAdded |
| To | - (instancetype)initWithTimeIntervalSinceReferenceDate:(NSTimeInterval)ti |

NSDictionary.hAdded [-[NSDictionary init]](https://developer.apple.com/documentation/foundation/nsdictionary/1418147-init)Added [-[NSMutableDictionary init]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1410577-init)Modified [+[NSDictionary dictionary]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionary)

|  | Declaration |
| --- | --- |
| From | + (id)dictionary |
| To | + (instancetype)dictionary |

Modified [+[NSDictionary dictionaryWithDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithDictionary:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithDictionary:(NSDictionary \*)dict |
| To | + (instancetype)dictionaryWithDictionary:(NSDictionary \*)dict |

Modified [+[NSDictionary dictionaryWithObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObject:forKey:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObject:(id)object forKey:(id<NSCopying>)key |
| To | + (instancetype)dictionaryWithObject:(id)object forKey:(id<NSCopying>)key |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |
| To | + (instancetype)dictionaryWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |
| To | + (instancetype)dictionaryWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |

Modified [+[NSDictionary dictionaryWithObjectsAndKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjectsAndKeys:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjectsAndKeys:(id)firstObject, ... |
| To | + (instancetype)dictionaryWithObjectsAndKeys:(id)firstObject, ... |

Modified [-[NSDictionary initWithDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithDictionary:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithDictionary:(NSDictionary \*)otherDictionary |
| To | - (instancetype)initWithDictionary:(NSDictionary \*)otherDictionary |

Modified [-[NSDictionary initWithDictionary:copyItems:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithDictionary:copyItems:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithDictionary:(NSDictionary \*)otherDictionary copyItems:(BOOL)flag |
| To | - (instancetype)initWithDictionary:(NSDictionary \*)otherDictionary copyItems:(BOOL)flag |

Modified [-[NSDictionary initWithObjects:forKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |
| To | - (instancetype)initWithObjects:(NSArray \*)objects forKeys:(NSArray \*)keys |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt |

Modified [-[NSDictionary initWithObjectsAndKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjectsAndKeys:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjectsAndKeys:(id)firstObject, ... |
| To | - (instancetype)initWithObjectsAndKeys:(id)firstObject, ... |

Modified [+[NSMutableDictionary dictionaryWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSMutableDictionary/dictionaryWithCapacity:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)dictionaryWithCapacity:(NSUInteger)numItems |

Modified [-[NSMutableDictionary initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

NSExpression.hAdded [-[NSExpression allowEvaluation]](https://developer.apple.com/documentation/foundation/nsexpression/1409244-allowevaluation)Added [+[NSExpression expressionForAnyKey]](https://developer.apple.com/documentation/foundation/nsexpression/1410198-expressionforanykey)Added [NSAnyKeyExpressionType](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype/anykey)Modified [NSExpression](https://developer.apple.com/documentation/foundation/nsexpression)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSIndexPath.hAdded -[NSIndexPath init]Modified [+[NSIndexPath indexPathWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexpath/1521019-indexpathwithindex)

|  | Declaration |
| --- | --- |
| From | + (id)indexPathWithIndex:(NSUInteger)index |
| To | + (instancetype)indexPathWithIndex:(NSUInteger)index |

Modified [+[NSIndexPath indexPathWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1521015-indexpathwithindexes)

|  | Declaration |
| --- | --- |
| From | + (id)indexPathWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |
| To | + (instancetype)indexPathWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |

Modified [-[NSIndexPath initWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416855-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndex:(NSUInteger)index |
| To | - (instancetype)initWithIndex:(NSUInteger)index |

Modified [-[NSIndexPath initWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416906-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |
| To | - (instancetype)initWithIndexes:(const NSUInteger [])indexes length:(NSUInteger)length |

NSIndexSet.hModified [+[NSIndexSet indexSet]](https://developer.apple.com/documentation/foundation/nsindexset/1427281-indexset)

|  | Declaration |
| --- | --- |
| From | + (id)indexSet |
| To | + (instancetype)indexSet |

Modified [+[NSIndexSet indexSetWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexset/1427254-indexsetwithindex)

|  | Declaration |
| --- | --- |
| From | + (id)indexSetWithIndex:(NSUInteger)value |
| To | + (instancetype)indexSetWithIndex:(NSUInteger)value |

Modified [+[NSIndexSet indexSetWithIndexesInRange:]](https://developer.apple.com/documentation/foundation/nsindexset/1427274-indexsetwithindexesinrange)

|  | Declaration |
| --- | --- |
| From | + (id)indexSetWithIndexesInRange:(NSRange)range |
| To | + (instancetype)indexSetWithIndexesInRange:(NSRange)range |

Modified [-[NSIndexSet init]](https://developer.apple.com/documentation/foundation/nsindexset/1807255-init)

|  | Declaration |
| --- | --- |
| From | - (id)init |
| To | - (instancetype)init |

Modified [-[NSIndexSet initWithIndex:]](https://developer.apple.com/documentation/foundation/nsindexset/1416501-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndex:(NSUInteger)value |
| To | - (instancetype)initWithIndex:(NSUInteger)value |

Modified [-[NSIndexSet initWithIndexSet:]](https://developer.apple.com/documentation/foundation/nsindexset/1415602-initwithindexset)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexSet:(NSIndexSet \*)indexSet |
| To | - (instancetype)initWithIndexSet:(NSIndexSet \*)indexSet |

Modified [-[NSIndexSet initWithIndexesInRange:]](https://developer.apple.com/documentation/foundation/nsindexset/1414013-initwithindexesinrange)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexesInRange:(NSRange)range |
| To | - (instancetype)initWithIndexesInRange:(NSRange)range |

NSKeyedArchiver.hAdded [-[NSKeyedArchiver setRequiresSecureCoding:]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417084-requiressecurecoding)Added [-[NSKeyedUnarchiver setRequiresSecureCoding:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410824-requiressecurecoding)Added [NSKeyedArchiveRootObjectKey](https://developer.apple.com/documentation/foundation/nskeyedarchiverootobjectkey)NSLocale.hAdded -[NSLocale init]Added [+[NSLocale localeWithLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1488627-localewithlocaleidentifier)Modified [-[NSLocale initWithLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1414217-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithLocaleIdentifier:(NSString \*)string |
| To | - (instancetype)initWithLocaleIdentifier:(NSString \*)string |

NSMetadata.hAdded [-[NSMetadataItem initWithURL:]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1414919-init)Added [-[NSMetadataQuery enumerateResultsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1415856-enumerateresults)Added [-[NSMetadataQuery enumerateResultsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1415123-enumerateresults)Added [-[NSMetadataQuery operationQueue]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410953-operationqueue)Added [-[NSMetadataQuery searchItems]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411307-searchitems)Added [-[NSMetadataQuery setOperationQueue:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410953-operationqueue)Added [-[NSMetadataQuery setSearchItems:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411307-searchitems)Added [NSMetadataQueryIndexedLocalComputerScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryindexedlocalcomputerscope)Added [NSMetadataQueryIndexedNetworkScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryindexednetworkscope)Added [NSMetadataQueryUpdateAddedItemsKey](https://developer.apple.com/documentation/foundation/nsmetadataqueryupdateaddeditemskey)Added [NSMetadataQueryUpdateChangedItemsKey](https://developer.apple.com/documentation/foundation/nsmetadataqueryupdatechangeditemskey)Added [NSMetadataQueryUpdateRemovedItemsKey](https://developer.apple.com/documentation/foundation/nsmetadataqueryupdateremoveditemskey)Modified [NSMetadataItemDisplayNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdisplaynamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSContentChangeDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscontentchangedatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSCreationDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscreationdatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfsnamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSSizeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfssizekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemIsUbiquitousKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisubiquitouskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemPathKey](https://developer.apple.com/documentation/foundation/nsmetadataitempathkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemURLKey](https://developer.apple.com/documentation/foundation/nsmetadataitemurlkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemhasunresolvedconflictskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey)

|  | Header | Deprecation |
| --- | --- | --- |
| From | Foundation/NSMetadata.h | _none_ |
| To | Foundation/NSMetadataAttributes.h | OS X 10.9 |

Modified [NSMetadataUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentdownloadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

NSMetadataAttributes.hAdded [NSMetadataItemAcquisitionMakeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemacquisitionmakekey)Added [NSMetadataItemAcquisitionModelKey](https://developer.apple.com/documentation/foundation/nsmetadataitemacquisitionmodelkey)Added [NSMetadataItemAlbumKey](https://developer.apple.com/documentation/foundation/nsmetadataitemalbumkey)Added [NSMetadataItemAltitudeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaltitudekey)Added [NSMetadataItemApertureKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaperturekey)Added [NSMetadataItemAppleLoopDescriptorsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemappleloopdescriptorskey)Added [NSMetadataItemAppleLoopsKeyFilterTypeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemappleloopskeyfiltertypekey)Added [NSMetadataItemAppleLoopsLoopModeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemappleloopsloopmodekey)Added [NSMetadataItemAppleLoopsRootKeyKey](https://developer.apple.com/documentation/foundation/nsmetadataitemappleloopsrootkeykey)Added [NSMetadataItemApplicationCategoriesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemapplicationcategorieskey)Added [NSMetadataItemAttributeChangeDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemattributechangedatekey)Added [NSMetadataItemAudiencesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaudienceskey)Added [NSMetadataItemAudioBitRateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaudiobitratekey)Added [NSMetadataItemAudioChannelCountKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaudiochannelcountkey)Added [NSMetadataItemAudioEncodingApplicationKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaudioencodingapplicationkey)Added [NSMetadataItemAudioSampleRateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaudiosampleratekey)Added [NSMetadataItemAudioTrackNumberKey](https://developer.apple.com/documentation/foundation/nsmetadataitemaudiotracknumberkey)Added [NSMetadataItemAuthorAddressesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemauthoraddresseskey)Added [NSMetadataItemAuthorEmailAddressesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemauthoremailaddresseskey)Added [NSMetadataItemAuthorsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemauthorskey)Added [NSMetadataItemBitsPerSampleKey](https://developer.apple.com/documentation/foundation/nsmetadataitembitspersamplekey)Added [NSMetadataItemCFBundleIdentifierKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcfbundleidentifierkey)Added [NSMetadataItemCameraOwnerKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcameraownerkey)Added [NSMetadataItemCityKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcitykey)Added [NSMetadataItemCodecsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcodecskey)Added [NSMetadataItemColorSpaceKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcolorspacekey)Added [NSMetadataItemCommentKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcommentkey)Added [NSMetadataItemComposerKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcomposerkey)Added [NSMetadataItemContactKeywordsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcontactkeywordskey)Added [NSMetadataItemContentCreationDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcontentcreationdatekey)Added [NSMetadataItemContentModificationDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcontentmodificationdatekey)Added [NSMetadataItemContentTypeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcontenttypekey)Added [NSMetadataItemContentTypeTreeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcontenttypetreekey)Added [NSMetadataItemContributorsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcontributorskey)Added [NSMetadataItemCopyrightKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcopyrightkey)Added [NSMetadataItemCountryKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcountrykey)Added [NSMetadataItemCoverageKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcoveragekey)Added [NSMetadataItemCreatorKey](https://developer.apple.com/documentation/foundation/nsmetadataitemcreatorkey)Added [NSMetadataItemDateAddedKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdateaddedkey)Added [NSMetadataItemDeliveryTypeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdeliverytypekey)Added [NSMetadataItemDescriptionKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdescriptionkey)Added [NSMetadataItemDirectorKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdirectorkey)Added [NSMetadataItemDownloadedDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdownloadeddatekey)Added [NSMetadataItemDueDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemduedatekey)Added [NSMetadataItemDurationSecondsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdurationsecondskey)Added [NSMetadataItemEXIFGPSVersionKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexifgpsversionkey)Added [NSMetadataItemEXIFVersionKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexifversionkey)Added [NSMetadataItemEditorsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemeditorskey)Added [NSMetadataItemEmailAddressesKey](https://developer.apple.com/documentation/foundation/nsmetadataitememailaddresseskey)Added [NSMetadataItemEncodingApplicationsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemencodingapplicationskey)Added [NSMetadataItemExecutableArchitecturesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexecutablearchitectureskey)Added [NSMetadataItemExecutablePlatformKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexecutableplatformkey)Added [NSMetadataItemExposureModeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexposuremodekey)Added [NSMetadataItemExposureProgramKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexposureprogramkey)Added [NSMetadataItemExposureTimeSecondsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexposuretimesecondskey)Added [NSMetadataItemExposureTimeStringKey](https://developer.apple.com/documentation/foundation/nsmetadataitemexposuretimestringkey)Added [NSMetadataItemFNumberKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfnumberkey)Added [NSMetadataItemFinderCommentKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfindercommentkey)Added [NSMetadataItemFlashOnOffKey](https://developer.apple.com/documentation/foundation/nsmetadataitemflashonoffkey)Added [NSMetadataItemFocalLength35mmKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfocallength35mmkey)Added [NSMetadataItemFocalLengthKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfocallengthkey)Added [NSMetadataItemFontsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfontskey)Added [NSMetadataItemGPSAreaInformationKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsareainformationkey)Added [NSMetadataItemGPSDOPKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsdopkey)Added [NSMetadataItemGPSDateStampKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsdatestampkey)Added [NSMetadataItemGPSDestBearingKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsdestbearingkey)Added [NSMetadataItemGPSDestDistanceKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsdestdistancekey)Added [NSMetadataItemGPSDestLatitudeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsdestlatitudekey)Added [NSMetadataItemGPSDestLongitudeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsdestlongitudekey)Added [NSMetadataItemGPSDifferentalKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsdifferentalkey)Added [NSMetadataItemGPSMapDatumKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsmapdatumkey)Added [NSMetadataItemGPSMeasureModeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsmeasuremodekey)Added [NSMetadataItemGPSProcessingMethodKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsprocessingmethodkey)Added [NSMetadataItemGPSStatusKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpsstatuskey)Added [NSMetadataItemGPSTrackKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgpstrackkey)Added [NSMetadataItemGenreKey](https://developer.apple.com/documentation/foundation/nsmetadataitemgenrekey)Added [NSMetadataItemHasAlphaChannelKey](https://developer.apple.com/documentation/foundation/nsmetadataitemhasalphachannelkey)Added [NSMetadataItemHeadlineKey](https://developer.apple.com/documentation/foundation/nsmetadataitemheadlinekey)Added [NSMetadataItemISOSpeedKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisospeedkey)Added [NSMetadataItemIdentifierKey](https://developer.apple.com/documentation/foundation/nsmetadataitemidentifierkey)Added [NSMetadataItemImageDirectionKey](https://developer.apple.com/documentation/foundation/nsmetadataitemimagedirectionkey)Added [NSMetadataItemInformationKey](https://developer.apple.com/documentation/foundation/nsmetadataiteminformationkey)Added [NSMetadataItemInstantMessageAddressesKey](https://developer.apple.com/documentation/foundation/nsmetadataiteminstantmessageaddresseskey)Added [NSMetadataItemInstructionsKey](https://developer.apple.com/documentation/foundation/nsmetadataiteminstructionskey)Added [NSMetadataItemIsApplicationManagedKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisapplicationmanagedkey)Added [NSMetadataItemIsGeneralMIDISequenceKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisgeneralmidisequencekey)Added [NSMetadataItemIsLikelyJunkKey](https://developer.apple.com/documentation/foundation/nsmetadataitemislikelyjunkkey)Added [NSMetadataItemKeySignatureKey](https://developer.apple.com/documentation/foundation/nsmetadataitemkeysignaturekey)Added [NSMetadataItemKeywordsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemkeywordskey)Added [NSMetadataItemKindKey](https://developer.apple.com/documentation/foundation/nsmetadataitemkindkey)Added [NSMetadataItemLanguagesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemlanguageskey)Added [NSMetadataItemLastUsedDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemlastuseddatekey)Added [NSMetadataItemLatitudeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemlatitudekey)Added [NSMetadataItemLayerNamesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemlayernameskey)Added [NSMetadataItemLensModelKey](https://developer.apple.com/documentation/foundation/nsmetadataitemlensmodelkey)Added [NSMetadataItemLongitudeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemlongitudekey)Added [NSMetadataItemLyricistKey](https://developer.apple.com/documentation/foundation/nsmetadataitemlyricistkey)Added [NSMetadataItemMaxApertureKey](https://developer.apple.com/documentation/foundation/nsmetadataitemmaxaperturekey)Added [NSMetadataItemMediaTypesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemmediatypeskey)Added [NSMetadataItemMeteringModeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemmeteringmodekey)Added [NSMetadataItemMusicalGenreKey](https://developer.apple.com/documentation/foundation/nsmetadataitemmusicalgenrekey)Added [NSMetadataItemMusicalInstrumentCategoryKey](https://developer.apple.com/documentation/foundation/nsmetadataitemmusicalinstrumentcategorykey)Added [NSMetadataItemMusicalInstrumentNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemmusicalinstrumentnamekey)Added [NSMetadataItemNamedLocationKey](https://developer.apple.com/documentation/foundation/nsmetadataitemnamedlocationkey)Added [NSMetadataItemNumberOfPagesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemnumberofpageskey)Added [NSMetadataItemOrganizationsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemorganizationskey)Added [NSMetadataItemOrientationKey](https://developer.apple.com/documentation/foundation/nsmetadataitemorientationkey)Added [NSMetadataItemOriginalFormatKey](https://developer.apple.com/documentation/foundation/nsmetadataitemoriginalformatkey)Added [NSMetadataItemOriginalSourceKey](https://developer.apple.com/documentation/foundation/nsmetadataitemoriginalsourcekey)Added [NSMetadataItemPageHeightKey](https://developer.apple.com/documentation/foundation/nsmetadataitempageheightkey)Added [NSMetadataItemPageWidthKey](https://developer.apple.com/documentation/foundation/nsmetadataitempagewidthkey)Added [NSMetadataItemParticipantsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemparticipantskey)Added [NSMetadataItemPerformersKey](https://developer.apple.com/documentation/foundation/nsmetadataitemperformerskey)Added [NSMetadataItemPhoneNumbersKey](https://developer.apple.com/documentation/foundation/nsmetadataitemphonenumberskey)Added [NSMetadataItemPixelCountKey](https://developer.apple.com/documentation/foundation/nsmetadataitempixelcountkey)Added [NSMetadataItemPixelHeightKey](https://developer.apple.com/documentation/foundation/nsmetadataitempixelheightkey)Added [NSMetadataItemPixelWidthKey](https://developer.apple.com/documentation/foundation/nsmetadataitempixelwidthkey)Added [NSMetadataItemProducerKey](https://developer.apple.com/documentation/foundation/nsmetadataitemproducerkey)Added [NSMetadataItemProfileNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemprofilenamekey)Added [NSMetadataItemProjectsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemprojectskey)Added [NSMetadataItemPublishersKey](https://developer.apple.com/documentation/foundation/nsmetadataitempublisherskey)Added [NSMetadataItemRecipientAddressesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemrecipientaddresseskey)Added [NSMetadataItemRecipientEmailAddressesKey](https://developer.apple.com/documentation/foundation/nsmetadataitemrecipientemailaddresseskey)Added [NSMetadataItemRecipientsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemrecipientskey)Added [NSMetadataItemRecordingDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemrecordingdatekey)Added [NSMetadataItemRecordingYearKey](https://developer.apple.com/documentation/foundation/nsmetadataitemrecordingyearkey)Added [NSMetadataItemRedEyeOnOffKey](https://developer.apple.com/documentation/foundation/nsmetadataitemredeyeonoffkey)Added [NSMetadataItemResolutionHeightDPIKey](https://developer.apple.com/documentation/foundation/nsmetadataitemresolutionheightdpikey)Added [NSMetadataItemResolutionWidthDPIKey](https://developer.apple.com/documentation/foundation/nsmetadataitemresolutionwidthdpikey)Added [NSMetadataItemRightsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemrightskey)Added [NSMetadataItemSecurityMethodKey](https://developer.apple.com/documentation/foundation/nsmetadataitemsecuritymethodkey)Added [NSMetadataItemSpeedKey](https://developer.apple.com/documentation/foundation/nsmetadataitemspeedkey)Added [NSMetadataItemStarRatingKey](https://developer.apple.com/documentation/foundation/nsmetadataitemstarratingkey)Added [NSMetadataItemStateOrProvinceKey](https://developer.apple.com/documentation/foundation/nsmetadataitemstateorprovincekey)Added [NSMetadataItemStreamableKey](https://developer.apple.com/documentation/foundation/nsmetadataitemstreamablekey)Added [NSMetadataItemSubjectKey](https://developer.apple.com/documentation/foundation/nsmetadataitemsubjectkey)Added [NSMetadataItemTempoKey](https://developer.apple.com/documentation/foundation/nsmetadataitemtempokey)Added [NSMetadataItemTextContentKey](https://developer.apple.com/documentation/foundation/nsmetadataitemtextcontentkey)Added [NSMetadataItemThemeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemthemekey)Added [NSMetadataItemTimeSignatureKey](https://developer.apple.com/documentation/foundation/nsmetadataitemtimesignaturekey)Added [NSMetadataItemTimestampKey](https://developer.apple.com/documentation/foundation/nsmetadataitemtimestampkey)Added [NSMetadataItemTitleKey](https://developer.apple.com/documentation/foundation/nsmetadataitemtitlekey)Added [NSMetadataItemTotalBitRateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemtotalbitratekey)Added [NSMetadataItemVersionKey](https://developer.apple.com/documentation/foundation/nsmetadataitemversionkey)Added [NSMetadataItemVideoBitRateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemvideobitratekey)Added [NSMetadataItemWhereFromsKey](https://developer.apple.com/documentation/foundation/nsmetadataitemwherefromskey)Added [NSMetadataItemWhiteBalanceKey](https://developer.apple.com/documentation/foundation/nsmetadataitemwhitebalancekey)Added [NSMetadataUbiquitousItemDownloadingErrorKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingerrorkey)Added [NSMetadataUbiquitousItemDownloadingStatusCurrent](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatuscurrent)Added [NSMetadataUbiquitousItemDownloadingStatusDownloaded](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatusdownloaded)Added [NSMetadataUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatuskey)Added [NSMetadataUbiquitousItemDownloadingStatusNotDownloaded](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadingstatusnotdownloaded)Added [NSMetadataUbiquitousItemUploadingErrorKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemuploadingerrorkey)Modified [NSMetadataItemDisplayNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemdisplaynamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSContentChangeDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscontentchangedatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSCreationDateKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfscreationdatekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfsnamekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemFSSizeKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfssizekey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemIsUbiquitousKey](https://developer.apple.com/documentation/foundation/nsmetadataitemisubiquitouskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemPathKey](https://developer.apple.com/documentation/foundation/nsmetadataitempathkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataItemURLKey](https://developer.apple.com/documentation/foundation/nsmetadataitemurlkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemHasUnresolvedConflictsKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemhasunresolvedconflictskey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadedkey)

|  | Header | Deprecation |
| --- | --- | --- |
| From | Foundation/NSMetadata.h | _none_ |
| To | Foundation/NSMetadataAttributes.h | OS X 10.9 |

Modified [NSMetadataUbiquitousItemIsDownloadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisdownloadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemIsUploadingKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisuploadingkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentdownloadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

Modified [NSMetadataUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitempercentuploadedkey)

|  | Header |
| --- | --- |
| From | Foundation/NSMetadata.h |
| To | Foundation/NSMetadataAttributes.h |

NSNetServices.hRemoved [-[NSNetService addresses]](https://developer.apple.com/documentation/foundation/netservice/1408528-addresses)Removed [-[NSNetService delegate]](https://developer.apple.com/documentation/foundation/netservice/1410296-delegate)Removed [-[NSNetService domain]](https://developer.apple.com/documentation/foundation/nsnetservice/1414495-domain)Removed [-[NSNetService hostName]](https://developer.apple.com/documentation/foundation/nsnetservice/1413300-hostname)Removed [-[NSNetService name]](https://developer.apple.com/documentation/foundation/nsnetservice/1409022-name)Removed [-[NSNetService port]](https://developer.apple.com/documentation/foundation/nsnetservice/1409816-port)Removed [-[NSNetService setDelegate:]](https://developer.apple.com/documentation/foundation/netservice/1410296-delegate)Removed [-[NSNetService type]](https://developer.apple.com/documentation/foundation/nsnetservice/1416595-type)Removed [-[NSNetServiceBrowser delegate]](https://developer.apple.com/documentation/foundation/netservicebrowser/1409380-delegate)Removed [-[NSNetServiceBrowser setDelegate:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1409380-delegate)Added [NSNetService.addresses](https://developer.apple.com/documentation/foundation/netservice/1408528-addresses)Added [NSNetService.delegate](https://developer.apple.com/documentation/foundation/nsnetservice/1410296-delegate)Added [NSNetService.domain](https://developer.apple.com/documentation/foundation/nsnetservice/1414495-domain)Added [NSNetService.hostName](https://developer.apple.com/documentation/foundation/netservice/1413300-hostname)Added [NSNetService.name](https://developer.apple.com/documentation/foundation/nsnetservice/1409022-name)Added [NSNetService.port](https://developer.apple.com/documentation/foundation/netservice/1409816-port)Added [NSNetService.type](https://developer.apple.com/documentation/foundation/netservice/1416595-type)Added [NSNetServiceBrowser.delegate](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1409380-delegate)Added [-[NSNetServiceDelegate netService:didAcceptConnectionWithInputStream:outputStream:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1407489-netservice)Added [NSNetServiceListenForConnections](https://developer.apple.com/documentation/foundation/nsnetserviceoptions/nsnetservicelistenforconnections)Modified [-[NSNetService protocolSpecificInformation]](https://developer.apple.com/documentation/foundation/nsnetservice/1807237-protocolspecificinformation)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [-[NSNetService resolve]](https://developer.apple.com/documentation/foundation/nsnetservice/1506204-resolve)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [-[NSNetService setProtocolSpecificInformation:]](https://developer.apple.com/documentation/foundation/nsnetservice/1807240-setprotocolspecificinformation)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [-[NSNetServiceBrowser searchForAllDomains]](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1807244-searchforalldomains)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

NSNotification.hAdded [-[NSNotification init]](https://developer.apple.com/documentation/foundation/nsnotification/1412595-init)Added [-[NSNotification initWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1415764-init)Added -[NSNotificationCenter init]Modified [+[NSNotification notificationWithName:object:]](https://developer.apple.com/documentation/foundation/nsnotification/1417440-notificationwithname)

|  | Declaration |
| --- | --- |
| From | + (id)notificationWithName:(NSString \*)aName object:(id)anObject |
| To | + (instancetype)notificationWithName:(NSString \*)aName object:(id)anObject |

Modified [+[NSNotification notificationWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1574705-notificationwithname)

|  | Declaration |
| --- | --- |
| From | + (id)notificationWithName:(NSString \*)aName object:(id)anObject userInfo:(NSDictionary \*)aUserInfo |
| To | + (instancetype)notificationWithName:(NSString \*)aName object:(id)anObject userInfo:(NSDictionary \*)aUserInfo |

Modified [+[NSNotificationCenter defaultCenter]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/clm/NSNotificationCenter/defaultCenter)

|  | Declaration |
| --- | --- |
| From | + (id)defaultCenter |
| To | + (instancetype)defaultCenter |

NSObjCRuntime.hRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_2_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NARemoved #def AVAILABLE_MAC_OS_X_VERSION_NA_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NAAdded [#def NSFoundationVersionNumber10_8](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8)Added [#def NSFoundationVersionNumber10_8_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_1)Added [#def NSFoundationVersionNumber10_8_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_2)Added [#def NSFoundationVersionNumber10_8_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_3)Added [#def NSFoundationVersionNumber10_8_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_8_4)Added #def NS_CLASS_DEPRECATEDAdded #def NS_CLASS_DEPRECATED_IOSAdded #def NS_CLASS_DEPRECATED_MACModified #def NSINTEGER_DEFINED

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [#def NSIntegerMax](https://developer.apple.com/documentation/objectivec/nsintegermax)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [#def NSIntegerMin](https://developer.apple.com/documentation/objectivec/nsintegermin)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [NSUInteger](https://developer.apple.com/documentation/objectivec/nsuinteger)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

Modified [#def NSUIntegerMax](https://developer.apple.com/documentation/objectivec/nsuintegermax)

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

NSObject.hModified [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject alloc]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/alloc)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject allocWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/allocWithZone:)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | + (id)allocWithZone:(NSZone \*)zone |
| To | objc/NSObject.h | + (id)allocWithZone:(struct _NSZone \*)zone |

Modified [-[NSObject autorelease]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/autorelease)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject class]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/class)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject conformsToProtocol:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/conformsToProtocol:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject conformsToProtocol:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/conformsToProtocol:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject copy]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/copy)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject copyWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/copyWithZone:)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | + (id)copyWithZone:(NSZone \*)zone |
| To | objc/NSObject.h | + (id)copyWithZone:(struct _NSZone \*)zone |

Modified [-[NSObject dealloc]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/description)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/description)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject doesNotRecognizeSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/doesNotRecognizeSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject finalize]](https://developer.apple.com/documentation/objectivec/nsobject/1418513-finalize)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject forwardInvocation:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/forwardInvocation:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject forwardingTargetForSelector:]](https://developer.apple.com/documentation/objectivec/nsobject/1418855-forwardingtarget)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject hash]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/hash)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/init)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject initialize]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/initialize)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject instanceMethodForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instanceMethodForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject instanceMethodSignatureForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instanceMethodSignatureForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject instancesRespondToSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instancesRespondToSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isEqual:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isEqual:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isKindOfClass:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isKindOfClass:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isMemberOfClass:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isMemberOfClass:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject isProxy]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isProxy)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject isSubclassOfClass:]](https://developer.apple.com/documentation/objectivec/nsobject/1418669-issubclassofclass)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject load]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/load)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject methodForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/methodForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject methodSignatureForSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/methodSignatureForSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject mutableCopy]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/mutableCopy)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject mutableCopyWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/mutableCopyWithZone:)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | + (id)mutableCopyWithZone:(NSZone \*)zone |
| To | objc/NSObject.h | + (id)mutableCopyWithZone:(struct _NSZone \*)zone |

Modified [+[NSObject new]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/new)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject performSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/performSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject performSelector:withObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/performSelector:withObject:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject performSelector:withObject:withObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/performSelector:withObject:withObject:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject release]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject resolveClassMethod:]](https://developer.apple.com/documentation/objectivec/nsobject/1418889-resolveclassmethod)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject resolveInstanceMethod:]](https://developer.apple.com/documentation/objectivec/nsobject/1418500-resolveinstancemethod)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject respondsToSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/respondsToSelector:)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject retain]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retain)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject retainCount]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retainCount)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject self]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/self)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [+[NSObject superclass]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/superclass)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject superclass]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/superclass)

|  | Header |
| --- | --- |
| From | Foundation/NSObject.h |
| To | objc/NSObject.h |

Modified [-[NSObject zone]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/zone)

|  | Header | Declaration |
| --- | --- | --- |
| From | Foundation/NSObject.h | - (NSZone \*)zone |
| To | objc/NSObject.h | - (struct _NSZone \*)zone |

NSOrderedSet.hAdded [-[NSMutableOrderedSet init]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410545-init)Added [-[NSOrderedSet init]](https://developer.apple.com/documentation/foundation/nsorderedset/1417735-init)Modified [-[NSMutableOrderedSet initWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411583-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

Modified [+[NSMutableOrderedSet orderedSetWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1543283-orderedsetwithcapacity)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)orderedSetWithCapacity:(NSUInteger)numItems |

Modified [-[NSOrderedSet initWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408623-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array |
| To | - (instancetype)initWithArray:(NSArray \*)array |

Modified [-[NSOrderedSet initWithArray:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1418006-initwitharray)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithArray:(NSArray \*)set copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409272-initwitharray)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)set range:(NSRange)range copyItems:(BOOL)flag |
| To | - (instancetype)initWithArray:(NSArray \*)set range:(NSRange)range copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413883-initwithobject)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObject:(id)object |
| To | - (instancetype)initWithObject:(id)object |

Modified [-[NSOrderedSet initWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543287-initwithobjects)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id)firstObj, ... |
| To | - (instancetype)initWithObjects:(id)firstObj, ... |

Modified [-[NSOrderedSet initWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411910-initwithobjects)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [-[NSOrderedSet initWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1412402-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithOrderedSet:(NSOrderedSet \*)set |
| To | - (instancetype)initWithOrderedSet:(NSOrderedSet \*)set |

Modified [-[NSOrderedSet initWithOrderedSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411658-initwithorderedset)

|  | Declaration |
| --- | --- |
| From | - (id)initWithOrderedSet:(NSOrderedSet \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithOrderedSet:(NSOrderedSet \*)set copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417751-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |
| To | - (instancetype)initWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |

Modified [-[NSOrderedSet initWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1416344-initwithset)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set |
| To | - (instancetype)initWithSet:(NSSet \*)set |

Modified [-[NSOrderedSet initWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411246-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |

Modified [+[NSOrderedSet orderedSet]](https://developer.apple.com/documentation/foundation/nsorderedset/1543313-orderedset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSet |
| To | + (instancetype)orderedSet |

Modified [+[NSOrderedSet orderedSetWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543310-orderedsetwitharray)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithArray:(NSArray \*)array |
| To | + (instancetype)orderedSetWithArray:(NSArray \*)array |

Modified [+[NSOrderedSet orderedSetWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543321-orderedsetwitharray)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithArray:(NSArray \*)array range:(NSRange)range copyItems:(BOOL)flag |
| To | + (instancetype)orderedSetWithArray:(NSArray \*)array range:(NSRange)range copyItems:(BOOL)flag |

Modified [+[NSOrderedSet orderedSetWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543339-orderedsetwithobject)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithObject:(id)object |
| To | + (instancetype)orderedSetWithObject:(id)object |

Modified [+[NSOrderedSet orderedSetWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543312-orderedsetwithobjects)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithObjects:(id)firstObj, ... |
| To | + (instancetype)orderedSetWithObjects:(id)firstObj, ... |

Modified [+[NSOrderedSet orderedSetWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543334-init)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | + (instancetype)orderedSetWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [+[NSOrderedSet orderedSetWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543280-orderedsetwithorderedset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithOrderedSet:(NSOrderedSet \*)set |
| To | + (instancetype)orderedSetWithOrderedSet:(NSOrderedSet \*)set |

Modified [+[NSOrderedSet orderedSetWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543292-orderedsetwithorderedset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |
| To | + (instancetype)orderedSetWithOrderedSet:(NSOrderedSet \*)set range:(NSRange)range copyItems:(BOOL)flag |

Modified [+[NSOrderedSet orderedSetWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543298-orderedsetwithset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithSet:(NSSet \*)set |
| To | + (instancetype)orderedSetWithSet:(NSSet \*)set |

Modified [+[NSOrderedSet orderedSetWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543331-orderedsetwithset)

|  | Declaration |
| --- | --- |
| From | + (id)orderedSetWithSet:(NSSet \*)set copyItems:(BOOL)flag |
| To | + (instancetype)orderedSetWithSet:(NSSet \*)set copyItems:(BOOL)flag |

NSPredicate.hAdded [-[NSMutableOrderedSet filterUsingPredicate:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1408348-filterusingpredicate)Added [-[NSOrderedSet filteredOrderedSetUsingPredicate:]](https://developer.apple.com/documentation/foundation/nsorderedset/1415807-filtered)Added [-[NSPredicate allowEvaluation]](https://developer.apple.com/documentation/foundation/nspredicate/1416310-allowevaluation)Added [+[NSPredicate predicateFromMetadataQueryString:]](https://developer.apple.com/documentation/foundation/nspredicate/1417831-predicatefrommetadataquerystring)Added NSMutableOrderedSet(NSPredicateSupport)Added NSOrderedSet(NSPredicateSupport)Modified [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSProcessInfo.hAdded [-[NSProcessInfo beginActivityWithOptions:reason:]](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415995-beginactivitywithoptions)Added [-[NSProcessInfo endActivity:]](https://developer.apple.com/documentation/foundation/processinfo/1411321-endactivity)Added [-[NSProcessInfo performActivityWithOptions:reason:usingBlock:]](https://developer.apple.com/documentation/foundation/processinfo/1418048-performactivity)Added [NSActivityAutomaticTerminationDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityautomaticterminationdisabled)Added [NSActivityBackground](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivitybackground)Added [NSActivityIdleDisplaySleepDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityidledisplaysleepdisabled)Added [NSActivityIdleSystemSleepDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityidlesystemsleepdisabled)Added [NSActivityLatencyCritical](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/1415541-latencycritical)Added [NSActivityOptions](https://developer.apple.com/documentation/foundation/processinfo/activityoptions)Added [NSActivitySuddenTerminationDisabled](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivitysuddenterminationdisabled)Added [NSActivityUserInitiated](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivityuserinitiated)Added [NSActivityUserInitiatedAllowingIdleSystemSleep](https://developer.apple.com/documentation/foundation/processinfo/activityoptions/1414902-userinitiatedallowingidlesystems)Added NSProcessInfo()NSProgress.hAdded [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress)Added [+[NSProgress addSubscriberForFileURL:withPublishingHandler:]](https://developer.apple.com/documentation/foundation/progress/1418475-addsubscriber)Added [-[NSProgress becomeCurrentWithPendingUnitCount:]](https://developer.apple.com/documentation/foundation/progress/1410103-becomecurrent)Added [-[NSProgress cancel]](https://developer.apple.com/documentation/foundation/nsprogress/1413832-cancel)Added [NSProgress.cancellable](https://developer.apple.com/documentation/foundation/nsprogress/1409348-cancellable)Added [NSProgress.cancellationHandler](https://developer.apple.com/documentation/foundation/nsprogress/1408913-cancellationhandler)Added [NSProgress.cancelled](https://developer.apple.com/documentation/foundation/progress/1414454-iscancelled)Added [NSProgress.completedUnitCount](https://developer.apple.com/documentation/foundation/nsprogress/1407934-completedunitcount)Added [+[NSProgress currentProgress]](https://developer.apple.com/documentation/foundation/nsprogress/1412499-currentprogress)Added [NSProgress.fractionCompleted](https://developer.apple.com/documentation/foundation/nsprogress/1408579-fractioncompleted)Added [NSProgress.indeterminate](https://developer.apple.com/documentation/foundation/progress/1412871-isindeterminate)Added [-[NSProgress initWithParent:userInfo:]](https://developer.apple.com/documentation/foundation/progress/1409133-init)Added [NSProgress.kind](https://developer.apple.com/documentation/foundation/progress/1416139-kind)Added [NSProgress.localizedAdditionalDescription](https://developer.apple.com/documentation/foundation/nsprogress/1412455-localizedadditionaldescription)Added [NSProgress.localizedDescription](https://developer.apple.com/documentation/foundation/nsprogress/1417251-localizeddescription)Added [NSProgress.old](https://developer.apple.com/documentation/foundation/progress/1407931-isold)Added [NSProgress.pausable](https://developer.apple.com/documentation/foundation/progress/1417421-ispausable)Added [-[NSProgress pause]](https://developer.apple.com/documentation/foundation/nsprogress/1412377-pause)Added [NSProgress.paused](https://developer.apple.com/documentation/foundation/progress/1415495-ispaused)Added [NSProgress.pausingHandler](https://developer.apple.com/documentation/foundation/nsprogress/1412873-pausinghandler)Added [+[NSProgress progressWithTotalUnitCount:]](https://developer.apple.com/documentation/foundation/nsprogress/1415509-progresswithtotalunitcount)Added [-[NSProgress publish]](https://developer.apple.com/documentation/foundation/progress/1416782-publish)Added [+[NSProgress removeSubscriber:]](https://developer.apple.com/documentation/foundation/progress/1410457-removesubscriber)Added [-[NSProgress resignCurrent]](https://developer.apple.com/documentation/foundation/nsprogress/1407180-resigncurrent)Added [-[NSProgress setUserInfoObject:forKey:]](https://developer.apple.com/documentation/foundation/nsprogress/1407537-setuserinfoobject)Added [NSProgress.totalUnitCount](https://developer.apple.com/documentation/foundation/nsprogress/1410940-totalunitcount)Added [-[NSProgress unpublish]](https://developer.apple.com/documentation/foundation/nsprogress/1413268-unpublish)Added [-[NSProgress userInfo]](https://developer.apple.com/documentation/foundation/progress/1413314-userinfo)Added [NSProgressEstimatedTimeRemainingKey](https://developer.apple.com/documentation/foundation/progressuserinfokey/1407371-estimatedtimeremainingkey)Added [NSProgressFileAnimationImageKey](https://developer.apple.com/documentation/foundation/nsprogressfileanimationimagekey)Added [NSProgressFileAnimationImageOriginalRectKey](https://developer.apple.com/documentation/foundation/nsprogressfileanimationimageoriginalrectkey)Added [NSProgressFileCompletedCountKey](https://developer.apple.com/documentation/foundation/nsprogressfilecompletedcountkey)Added [NSProgressFileIconKey](https://developer.apple.com/documentation/foundation/nsprogressfileiconkey)Added [NSProgressFileOperationKindCopying](https://developer.apple.com/documentation/foundation/progress/fileoperationkind/1415785-copying)Added [NSProgressFileOperationKindDecompressingAfterDownloading](https://developer.apple.com/documentation/foundation/progress/fileoperationkind/1410985-decompressingafterdownloading)Added [NSProgressFileOperationKindDownloading](https://developer.apple.com/documentation/foundation/nsprogressfileoperationkinddownloading)Added [NSProgressFileOperationKindKey](https://developer.apple.com/documentation/foundation/progressuserinfokey/1408097-fileoperationkindkey)Added [NSProgressFileOperationKindReceiving](https://developer.apple.com/documentation/foundation/nsprogressfileoperationkindreceiving)Added [NSProgressFileTotalCountKey](https://developer.apple.com/documentation/foundation/nsprogressfiletotalcountkey)Added [NSProgressFileURLKey](https://developer.apple.com/documentation/foundation/progressuserinfokey/1408815-fileurlkey)Added [NSProgressKindFile](https://developer.apple.com/documentation/foundation/progresskind/1409141-file)Added [NSProgressPublishingHandler](https://developer.apple.com/documentation/foundation/nsprogresspublishinghandler)Added [NSProgressThroughputKey](https://developer.apple.com/documentation/foundation/nsprogressthroughputkey)Added [NSProgressUnpublishingHandler](https://developer.apple.com/documentation/foundation/progress/unpublishinghandler)NSScanner.hAdded [-[NSScanner scanUnsignedLongLong:]](https://developer.apple.com/documentation/foundation/scanner/1408559-scanunsignedlonglong)Modified [-[NSScanner scanCharactersFromSet:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanCharactersFromSet:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)value |
| To | - (BOOL)scanCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)result |

Modified [-[NSScanner scanDouble:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanDouble:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanDouble:(double \*)value |
| To | - (BOOL)scanDouble:(double \*)result |

Modified [-[NSScanner scanFloat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanFloat:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanFloat:(float \*)value |
| To | - (BOOL)scanFloat:(float \*)result |

Modified [-[NSScanner scanHexInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanHexInt:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanHexInt:(unsigned int \*)value |
| To | - (BOOL)scanHexInt:(unsigned int \*)result |

Modified [-[NSScanner scanInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanInt:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanInt:(int \*)value |
| To | - (BOOL)scanInt:(int \*)result |

Modified [-[NSScanner scanInteger:]](https://developer.apple.com/documentation/foundation/nsscanner/1411082-scaninteger)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanInteger:(NSInteger \*)value |
| To | - (BOOL)scanInteger:(NSInteger \*)result |

Modified [-[NSScanner scanLongLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanLongLong:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanLongLong:(long long \*)value |
| To | - (BOOL)scanLongLong:(long long \*)result |

Modified [-[NSScanner scanString:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanString:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanString:(NSString \*)string intoString:(NSString \*\*)value |
| To | - (BOOL)scanString:(NSString \*)string intoString:(NSString \*\*)result |

Modified [-[NSScanner scanUpToCharactersFromSet:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanUpToCharactersFromSet:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanUpToCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)value |
| To | - (BOOL)scanUpToCharactersFromSet:(NSCharacterSet \*)set intoString:(NSString \*\*)result |

Modified [-[NSScanner scanUpToString:intoString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanUpToString:intoString:)

|  | Declaration |
| --- | --- |
| From | - (BOOL)scanUpToString:(NSString \*)string intoString:(NSString \*\*)value |
| To | - (BOOL)scanUpToString:(NSString \*)string intoString:(NSString \*\*)result |

NSSet.hAdded [-[NSMutableSet init]](https://developer.apple.com/documentation/foundation/nsmutableset/1414518-init)Added [-[NSSet init]](https://developer.apple.com/documentation/foundation/nsset/1409698-init)Modified [-[NSMutableSet initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCapacity:(NSUInteger)numItems |
| To | - (instancetype)initWithCapacity:(NSUInteger)numItems |

Modified [+[NSMutableSet setWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSMutableSet/setWithCapacity:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithCapacity:(NSUInteger)numItems |
| To | + (instancetype)setWithCapacity:(NSUInteger)numItems |

Modified [-[NSSet initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithArray:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithArray:(NSArray \*)array |
| To | - (instancetype)initWithArray:(NSArray \*)array |

Modified [-[NSSet initWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(id)firstObj, ... |
| To | - (instancetype)initWithObjects:(id)firstObj, ... |

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [-[NSSet initWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set |
| To | - (instancetype)initWithSet:(NSSet \*)set |

Modified [-[NSSet initWithSet:copyItems:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:copyItems:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |
| To | - (instancetype)initWithSet:(NSSet \*)set copyItems:(BOOL)flag |

Modified [+[NSSet set]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/set)

|  | Declaration |
| --- | --- |
| From | + (id)set |
| To | + (instancetype)set |

Modified [+[NSSet setWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithArray:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithArray:(NSArray \*)array |
| To | + (instancetype)setWithArray:(NSArray \*)array |

Modified [+[NSSet setWithObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObject:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObject:(id)object |
| To | + (instancetype)setWithObject:(id)object |

Modified [+[NSSet setWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObjects:(id)firstObj, ... |
| To | + (instancetype)setWithObjects:(id)firstObj, ... |

Modified [+[NSSet setWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObjects:(const id [])objects count:(NSUInteger)cnt |
| To | + (instancetype)setWithObjects:(const id [])objects count:(NSUInteger)cnt |

Modified [+[NSSet setWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithSet:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithSet:(NSSet \*)set |
| To | + (instancetype)setWithSet:(NSSet \*)set |

NSSortDescriptor.hAdded [-[NSMutableOrderedSet sortUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410023-sort)Added [-[NSOrderedSet sortedArrayUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409953-sortedarray)Added [-[NSSortDescriptor allowEvaluation]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1412371-allowevaluation)Added NSMutableOrderedSet(NSKeyValueSorting)Added NSOrderedSet(NSKeyValueSorting)Modified [NSSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSString.hModified [-[NSString init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/init)

|  | Declaration |
| --- | --- |
| From | - (id)init |
| To | - (instancetype)init |

Modified [-[NSString initWithBytes:length:encoding:]](https://developer.apple.com/documentation/foundation/nsstring/1407339-initwithbytes)

|  | Declaration |
| --- | --- |
| From | - (id)initWithBytes:(const void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding |
| To | - (instancetype)initWithBytes:(const void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding |

Modified [-[NSString initWithBytesNoCopy:length:encoding:freeWhenDone:]](https://developer.apple.com/documentation/foundation/nsstring/1413830-initwithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | - (id)initWithBytesNoCopy:(void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding freeWhenDone:(BOOL)freeBuffer |
| To | - (instancetype)initWithBytesNoCopy:(void \*)bytes length:(NSUInteger)len encoding:(NSStringEncoding)encoding freeWhenDone:(BOOL)freeBuffer |

Modified [-[NSString initWithCString:encoding:]](https://developer.apple.com/documentation/foundation/nsstring/1411950-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCString:(const char \*)nullTerminatedCString encoding:(NSStringEncoding)encoding |
| To | - (instancetype)initWithCString:(const char \*)nullTerminatedCString encoding:(NSStringEncoding)encoding |

Modified [-[NSString initWithCharacters:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithCharacters:length:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCharacters:(const unichar \*)characters length:(NSUInteger)length |
| To | - (instancetype)initWithCharacters:(const unichar \*)characters length:(NSUInteger)length |

Modified [-[NSString initWithCharactersNoCopy:length:freeWhenDone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithCharactersNoCopy:length:freeWhenDone:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithCharactersNoCopy:(unichar \*)characters length:(NSUInteger)length freeWhenDone:(BOOL)freeBuffer |
| To | - (instancetype)initWithCharactersNoCopy:(unichar \*)characters length:(NSUInteger)length freeWhenDone:(BOOL)freeBuffer |

Modified [-[NSString initWithContentsOfFile:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1412610-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [-[NSString initWithContentsOfFile:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1418227-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [-[NSString initWithContentsOfURL:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1414463-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [-[NSString initWithContentsOfURL:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1414472-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | - (instancetype)initWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [-[NSString initWithData:encoding:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithData:encoding:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithData:(NSData \*)data encoding:(NSStringEncoding)encoding |
| To | - (instancetype)initWithData:(NSData \*)data encoding:(NSStringEncoding)encoding |

Modified [-[NSString initWithFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format, ... |
| To | - (instancetype)initWithFormat:(NSString \*)format, ... |

Modified [-[NSString initWithFormat:arguments:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:arguments:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format arguments:(va_list)argList |
| To | - (instancetype)initWithFormat:(NSString \*)format arguments:(va_list)argList |

Modified [-[NSString initWithFormat:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:locale:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format locale:(id)locale, ... |
| To | - (instancetype)initWithFormat:(NSString \*)format locale:(id)locale, ... |

Modified [-[NSString initWithFormat:locale:arguments:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:locale:arguments:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithFormat:(NSString \*)format locale:(id)locale arguments:(va_list)argList |
| To | - (instancetype)initWithFormat:(NSString \*)format locale:(id)locale arguments:(va_list)argList |

Modified [-[NSString initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithString:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithString:(NSString \*)aString |
| To | - (instancetype)initWithString:(NSString \*)aString |

Modified [-[NSString initWithUTF8String:]](https://developer.apple.com/documentation/foundation/nsstring/1412128-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithUTF8String:(const char \*)nullTerminatedCString |
| To | - (instancetype)initWithUTF8String:(const char \*)nullTerminatedCString |

Modified [+[NSString localizedStringWithFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/localizedStringWithFormat:)

|  | Declaration |
| --- | --- |
| From | + (id)localizedStringWithFormat:(NSString \*)format, ... |
| To | + (instancetype)localizedStringWithFormat:(NSString \*)format, ... |

Modified [+[NSString string]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/string)

|  | Declaration |
| --- | --- |
| From | + (id)string |
| To | + (instancetype)string |

Modified [+[NSString stringWithCString:encoding:]](https://developer.apple.com/documentation/foundation/nsstring/1497310-stringwithcstring)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithCString:(const char \*)cString encoding:(NSStringEncoding)enc |
| To | + (instancetype)stringWithCString:(const char \*)cString encoding:(NSStringEncoding)enc |

Modified [+[NSString stringWithCharacters:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithCharacters:length:)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithCharacters:(const unichar \*)characters length:(NSUInteger)length |
| To | + (instancetype)stringWithCharacters:(const unichar \*)characters length:(NSUInteger)length |

Modified [+[NSString stringWithContentsOfFile:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497327-stringwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfFile:(NSString \*)path encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithContentsOfFile:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497254-stringwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfFile:(NSString \*)path usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithContentsOfURL:encoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497360-stringwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfURL:(NSURL \*)url encoding:(NSStringEncoding)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithContentsOfURL:usedEncoding:error:]](https://developer.apple.com/documentation/foundation/nsstring/1497408-stringwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |
| To | + (instancetype)stringWithContentsOfURL:(NSURL \*)url usedEncoding:(NSStringEncoding \*)enc error:(NSError \*\*)error |

Modified [+[NSString stringWithFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithFormat:)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithFormat:(NSString \*)format, ... |
| To | + (instancetype)stringWithFormat:(NSString \*)format, ... |

Modified [+[NSString stringWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithString:)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithString:(NSString \*)string |
| To | + (instancetype)stringWithString:(NSString \*)string |

Modified [+[NSString stringWithUTF8String:]](https://developer.apple.com/documentation/foundation/nsstring/1497379-stringwithutf8string)

|  | Declaration |
| --- | --- |
| From | + (id)stringWithUTF8String:(const char \*)nullTerminatedCString |
| To | + (instancetype)stringWithUTF8String:(const char \*)nullTerminatedCString |

NSTextCheckingResult.hAdded [NSTextCheckingResult.alternativeStrings](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415454-alternativestrings)Added [+[NSTextCheckingResult correctionCheckingResultWithRange:replacementString:alternativeStrings:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1416640-correctioncheckingresult)NSTimer.hAdded [-[NSTimer setTolerance:]](https://developer.apple.com/documentation/foundation/nstimer/1415085-tolerance)Added [-[NSTimer tolerance]](https://developer.apple.com/documentation/foundation/nstimer/1415085-tolerance)NSURL.hAdded [+[NSCharacterSet URLFragmentAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1412537-urlfragmentallowed)Added [+[NSCharacterSet URLHostAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416426-urlhostallowedcharacterset)Added [+[NSCharacterSet URLPasswordAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1417313-urlpasswordallowed)Added [+[NSCharacterSet URLPathAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416804-urlpathallowed)Added [+[NSCharacterSet URLQueryAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416698-urlqueryallowed)Added [+[NSCharacterSet URLUserAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1411851-urluserallowedcharacterset)Added [-[NSString stringByAddingPercentEncodingWithAllowedCharacters:]](https://developer.apple.com/documentation/foundation/nsstring/1411946-stringbyaddingpercentencodingwit)Added [-[NSString stringByRemovingPercentEncoding]](https://developer.apple.com/documentation/foundation/nsstring/1409569-removingpercentencoding)Added [-[NSURL fileSystemRepresentation]](https://developer.apple.com/documentation/foundation/nsurl/1412925-filesystemrepresentation)Added [+[NSURL fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1411492-fileurlwithfilesystemrepresentat)Added [-[NSURL getFileSystemRepresentation:maxLength:]](https://developer.apple.com/documentation/foundation/nsurl/1415117-getfilesystemrepresentation)Added [-[NSURL initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1411210-init)Added [-[NSURL removeAllCachedResourceValues]](https://developer.apple.com/documentation/foundation/nsurl/1417078-removeallcachedresourcevalues)Added [-[NSURL removeCachedResourceValueForKey:]](https://developer.apple.com/documentation/foundation/nsurl/1410758-removecachedresourcevalue)Added [-[NSURL setTemporaryResourceValue:forKey:]](https://developer.apple.com/documentation/foundation/nsurl/1411094-settemporaryresourcevalue)Added [NSURLComponents](https://developer.apple.com/documentation/foundation/nsurlcomponents)Added [-[NSURLComponents URL]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1413469-url)Added [-[NSURLComponents URLRelativeToURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1408378-url)Added [+[NSURLComponents componentsWithString:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1572054-componentswithstring)Added [+[NSURLComponents componentsWithURL:resolvingAgainstBaseURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1572050-componentswithurl)Added [NSURLComponents.fragment](https://developer.apple.com/documentation/foundation/nsurlcomponents/1417638-fragment)Added [NSURLComponents.host](https://developer.apple.com/documentation/foundation/nsurlcomponents/1411178-host)Added [-[NSURLComponents init]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1414141-init)Added [-[NSURLComponents initWithString:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410784-initwithstring)Added [-[NSURLComponents initWithURL:resolvingAgainstBaseURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1416476-init)Added [NSURLComponents.password](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415604-password)Added [NSURLComponents.path](https://developer.apple.com/documentation/foundation/nsurlcomponents/1409650-path)Added [NSURLComponents.percentEncodedFragment](https://developer.apple.com/documentation/foundation/nsurlcomponents/1418392-percentencodedfragment)Added [NSURLComponents.percentEncodedHost](https://developer.apple.com/documentation/foundation/nsurlcomponents/1418231-percentencodedhost)Added [NSURLComponents.percentEncodedPassword](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410319-percentencodedpassword)Added [NSURLComponents.percentEncodedPath](https://developer.apple.com/documentation/foundation/nsurlcomponents/1408161-percentencodedpath)Added [NSURLComponents.percentEncodedQuery](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410395-percentencodedquery)Added [NSURLComponents.percentEncodedUser](https://developer.apple.com/documentation/foundation/nsurlcomponents/1417767-percentencodeduser)Added [NSURLComponents.port](https://developer.apple.com/documentation/foundation/nsurlcomponents/1413451-port)Added [NSURLComponents.query](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415452-query)Added [NSURLComponents.scheme](https://developer.apple.com/documentation/foundation/nsurlcomponents/1407517-scheme)Added [NSURLComponents.user](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415026-user)Added NSCharacterSet(NSURLUtilities)Added [NSURLTagNamesKey](https://developer.apple.com/documentation/foundation/nsurltagnameskey)Added [NSURLUbiquitousItemDownloadingErrorKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415978-ubiquitousitemdownloadingerrorke)Added [NSURLUbiquitousItemDownloadingStatusCurrent](https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus/1412385-current)Added [NSURLUbiquitousItemDownloadingStatusDownloaded](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadingstatusdownloaded)Added [NSURLUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadingstatuskey)Added [NSURLUbiquitousItemDownloadingStatusNotDownloaded](https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus/1416947-notdownloaded)Added [NSURLUbiquitousItemUploadingErrorKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1417266-ubiquitousitemuploadingerrorkey)Modified [NSURLBookmarkCreationPreferFileIDResolution](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationpreferfileidresolution)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [NSURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1572053-ubiquitousitemisdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSURLAuthenticationChallenge.hModified [NSURLAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSSecureCoding |

NSURLConnection.hModified [+[NSURLConnection sendAsynchronousRequest:queue:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1418125-sendasynchronousrequest)

|  | Declaration |
| --- | --- |
| From | + (void)sendAsynchronousRequest:(NSURLRequest \*)request queue:(NSOperationQueue \*)queue completionHandler:(void (^)(NSURLResponse \*, NSData \*, NSError \*))handler |
| To | + (void)sendAsynchronousRequest:(NSURLRequest \*)request queue:(NSOperationQueue \*)queue completionHandler:(void (^)(NSURLResponse \*response, NSData \*data, NSError \*connectionError))handler |

NSURLCredential.hAdded [NSURLCredentialPersistenceSynchronizable](https://developer.apple.com/documentation/foundation/urlcredential/persistence/synchronizable)Modified [NSURLCredential](https://developer.apple.com/documentation/foundation/urlcredential)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURLCredentialStorage.hAdded [-[NSURLCredentialStorage removeCredential:forProtectionSpace:options:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1407695-remove)Added [NSURLCredentialStorageRemoveSynchronizableCredentials](https://developer.apple.com/documentation/foundation/nsurlcredentialstorageremovesynchronizablecredentials)NSURLProtectionSpace.hModified [NSURLProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlprotectionspace)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURLRequest.hAdded [+[NSURLRequest supportsSecureCoding]](https://developer.apple.com/documentation/foundation/nsurlrequest/1416510-supportssecurecoding)Modified [NSURLRequest](https://developer.apple.com/documentation/foundation/nsurlrequest)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

NSURLResponse.hModified [NSURLResponse](https://developer.apple.com/documentation/foundation/nsurlresponse)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURLSession.hAdded [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession)Added [NSURLSession.configuration](https://developer.apple.com/documentation/foundation/nsurlsession/1411477-configuration)Added -[NSURLSession dataTaskWithHTTPGetRequest:]Added -[NSURLSession dataTaskWithHTTPGetRequest:completionHandler:]Added [-[NSURLSession dataTaskWithRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410592-datataskwithrequest)Added [-[NSURLSession dataTaskWithRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1407613-datataskwithrequest)Added [-[NSURLSession dataTaskWithURL:]](https://developer.apple.com/documentation/foundation/urlsession/1411554-datatask)Added [-[NSURLSession dataTaskWithURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410330-datataskwithurl)Added [NSURLSession.delegate](https://developer.apple.com/documentation/foundation/nsurlsession/1411530-delegate)Added [NSURLSession.delegateQueue](https://developer.apple.com/documentation/foundation/nsurlsession/1411571-delegatequeue)Added [-[NSURLSession downloadTaskWithRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411481-downloadtaskwithrequest)Added [-[NSURLSession downloadTaskWithRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411511-downloadtaskwithrequest)Added [-[NSURLSession downloadTaskWithResumeData:]](https://developer.apple.com/documentation/foundation/urlsession/1409226-downloadtask)Added [-[NSURLSession downloadTaskWithResumeData:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411598-downloadtaskwithresumedata)Added [-[NSURLSession downloadTaskWithURL:]](https://developer.apple.com/documentation/foundation/urlsession/1411482-downloadtask)Added [-[NSURLSession downloadTaskWithURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411608-downloadtaskwithurl)Added [-[NSURLSession finishTasksAndInvalidate]](https://developer.apple.com/documentation/foundation/urlsession/1407428-finishtasksandinvalidate)Added [-[NSURLSession flushWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411622-flush)Added [-[NSURLSession getTasksWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411578-gettaskswithcompletionhandler)Added [-[NSURLSession invalidateAndCancel]](https://developer.apple.com/documentation/foundation/urlsession/1411538-invalidateandcancel)Added [-[NSURLSession resetWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411479-reset)Added [NSURLSession.sessionDescription](https://developer.apple.com/documentation/foundation/urlsession/1408277-sessiondescription)Added [+[NSURLSession sessionWithConfiguration:]](https://developer.apple.com/documentation/foundation/urlsession/1411474-init)Added [+[NSURLSession sessionWithConfiguration:delegate:delegateQueue:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411597-sessionwithconfiguration)Added [+[NSURLSession sharedSession]](https://developer.apple.com/documentation/foundation/urlsession/1409000-shared)Added [-[NSURLSession uploadTaskWithRequest:fromData:]](https://developer.apple.com/documentation/foundation/nsurlsession/1409763-uploadtaskwithrequest)Added [-[NSURLSession uploadTaskWithRequest:fromData:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411518-uploadtask)Added [-[NSURLSession uploadTaskWithRequest:fromFile:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411550-uploadtaskwithrequest)Added [-[NSURLSession uploadTaskWithRequest:fromFile:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411638-uploadtaskwithrequest)Added [-[NSURLSession uploadTaskWithStreamedRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410934-uploadtaskwithstreamedrequest)Added [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration)Added [NSURLSessionConfiguration.HTTPAdditionalHeaders](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411532-httpadditionalheaders)Added [NSURLSessionConfiguration.HTTPCookieAcceptPolicy](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1408933-httpcookieacceptpolicy)Added [NSURLSessionConfiguration.HTTPCookieStorage](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411599-httpcookiestorage)Added [NSURLSessionConfiguration.HTTPMaximumConnectionsPerHost](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1407597-httpmaximumconnectionsperhost)Added [NSURLSessionConfiguration.HTTPShouldSetCookies](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411589-httpshouldsetcookies)Added [NSURLSessionConfiguration.HTTPShouldUsePipelining](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411657-httpshouldusepipelining)Added [NSURLSessionConfiguration.TLSMaximumSupportedProtocol](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1409076-tlsmaximumsupportedprotocol)Added [NSURLSessionConfiguration.TLSMinimumSupportedProtocol](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411526-tlsminimumsupportedprotocol)Added [NSURLSessionConfiguration.URLCache](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410148-urlcache)Added [NSURLSessionConfiguration.URLCredentialStorage](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410947-urlcredentialstorage)Added [NSURLSessionConfiguration.allowsCellularAccess](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1409406-allowscellularaccess)Added [+[NSURLSessionConfiguration backgroundSessionConfiguration:]](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411521-backgroundsessionconfiguration)Added [NSURLSessionConfiguration.connectionProxyDictionary](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411499-connectionproxydictionary)Added [+[NSURLSessionConfiguration defaultSessionConfiguration]](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411560-defaultsessionconfiguration)Added [+[NSURLSessionConfiguration ephemeralSessionConfiguration]](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410529-ephemeral)Added [NSURLSessionConfiguration.identifier](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408987-identifier)Added [NSURLSessionConfiguration.networkServiceType](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411606-networkservicetype)Added [NSURLSessionConfiguration.protocolClasses](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411050-protocolclasses)Added [NSURLSessionConfiguration.requestCachePolicy](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411655-requestcachepolicy)Added [NSURLSessionConfiguration.timeoutIntervalForRequest](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1408259-timeoutintervalforrequest)Added [NSURLSessionConfiguration.timeoutIntervalForResource](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408153-timeoutintervalforresource)Added [NSURLSessionDataDelegate](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate)Added [-[NSURLSessionDataDelegate URLSession:dataTask:didBecomeDownloadTask:]](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1409936-urlsession)Added [-[NSURLSessionDataDelegate URLSession:dataTask:didReceiveData:]](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411528-urlsession)Added [-[NSURLSessionDataDelegate URLSession:dataTask:didReceiveResponse:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1410027-urlsession)Added [-[NSURLSessionDataDelegate URLSession:dataTask:willCacheResponse:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1411612-urlsession)Added [NSURLSessionDataTask](https://developer.apple.com/documentation/foundation/urlsessiondatatask)Added [NSURLSessionDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate)Added [-[NSURLSessionDelegate URLSession:didBecomeInvalidWithError:]](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1407776-urlsession)Added [-[NSURLSessionDelegate URLSession:didReceiveChallenge:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1409308-urlsession)Added [NSURLSessionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate)Added [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didFinishDownloadingToURL:]](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/1411575-urlsession)Added [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/1408142-urlsession)Added [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:]](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1409408-urlsession)Added [NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask)Added [-[NSURLSessionDownloadTask cancelByProducingResumeData:]](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask/1411634-cancelbyproducingresumedata)Added [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask)Added [-[NSURLSessionTask cancel]](https://developer.apple.com/documentation/foundation/urlsessiontask/1411591-cancel)Added [NSURLSessionTask.countOfBytesExpectedToReceive](https://developer.apple.com/documentation/foundation/urlsessiontask/1410663-countofbytesexpectedtoreceive)Added [NSURLSessionTask.countOfBytesExpectedToSend](https://developer.apple.com/documentation/foundation/urlsessiontask/1411534-countofbytesexpectedtosend)Added [NSURLSessionTask.countOfBytesReceived](https://developer.apple.com/documentation/foundation/urlsessiontask/1411581-countofbytesreceived)Added [NSURLSessionTask.countOfBytesSent](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1410444-countofbytessent)Added [NSURLSessionTask.currentRequest](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411649-currentrequest)Added [NSURLSessionTask.error](https://developer.apple.com/documentation/foundation/urlsessiontask/1408145-error)Added [NSURLSessionTask.originalRequest](https://developer.apple.com/documentation/foundation/urlsessiontask/1411572-originalrequest)Added [NSURLSessionTask.response](https://developer.apple.com/documentation/foundation/urlsessiontask/1410586-response)Added [-[NSURLSessionTask resume]](https://developer.apple.com/documentation/foundation/urlsessiontask/1411121-resume)Added [NSURLSessionTask.state](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1409888-state)Added [-[NSURLSessionTask suspend]](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411565-suspend)Added [NSURLSessionTask.taskDescription](https://developer.apple.com/documentation/foundation/urlsessiontask/1409798-taskdescription)Added [NSURLSessionTask.taskIdentifier](https://developer.apple.com/documentation/foundation/urlsessiontask/1411231-taskidentifier)Added [NSURLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate)Added [-[NSURLSessionTaskDelegate URLSession:task:didCompleteWithError:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411610-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:didReceiveChallenge:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411595-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1408299-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:needNewBodyStream:]](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1410001-urlsession)Added [-[NSURLSessionTaskDelegate URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1411626-urlsession)Added [NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/nsurlsessionuploadtask)Added NSURLSession(NSURLSessionAsynchronousConvenience)Added NSURLSession(NSURLSessionDeprecated)Added [NSURLSessionAuthChallengeCancelAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengecancelauthenticationchallenge)Added [NSURLSessionAuthChallengeDisposition](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition)Added [NSURLSessionAuthChallengePerformDefaultHandling](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/performdefaulthandling)Added [NSURLSessionAuthChallengeRejectProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengerejectprotectionspace)Added [NSURLSessionAuthChallengeUseCredential](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/usecredential)Added [NSURLSessionDownloadTaskResumeData](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtaskresumedata)Added [NSURLSessionResponseAllow](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponseallow)Added [NSURLSessionResponseBecomeDownload](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsebecomedownload)Added [NSURLSessionResponseCancel](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsecancel)Added [NSURLSessionResponseDisposition](https://developer.apple.com/documentation/foundation/urlsession/responsedisposition)Added [NSURLSessionTaskState](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate)Added [NSURLSessionTaskStateCanceling](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate/nsurlsessiontaskstatecanceling)Added [NSURLSessionTaskStateCompleted](https://developer.apple.com/documentation/foundation/urlsessiontask/state/completed)Added [NSURLSessionTaskStateRunning](https://developer.apple.com/documentation/foundation/urlsessiontask/state/running)Added [NSURLSessionTaskStateSuspended](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate/nsurlsessiontaskstatesuspended)Added [NSURLSessionTransferSizeUnknown](https://developer.apple.com/documentation/foundation/nsurlsessiontransfersizeunknown)NSUserDefaults.hAdded [-[NSUserDefaults initWithSuiteName:]](https://developer.apple.com/documentation/foundation/userdefaults/1409957-init)Modified [-[NSUserDefaults initWithUser:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/initWithUser:)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [-[NSUserDefaults persistentDomainNames]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/persistentDomainNames)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

NSUserNotification.hAdded [NSUserNotification.contentImage](https://developer.apple.com/documentation/foundation/nsusernotification/1414856-contentimage)Added [NSUserNotification.hasReplyButton](https://developer.apple.com/documentation/foundation/nsusernotification/1413216-hasreplybutton)Added [NSUserNotification.identifier](https://developer.apple.com/documentation/foundation/nsusernotification/1416410-identifier)Added [NSUserNotification.response](https://developer.apple.com/documentation/foundation/nsusernotification/1416115-response)Added [NSUserNotification.responsePlaceholder](https://developer.apple.com/documentation/foundation/nsusernotification/1410983-responseplaceholder)Added [NSUserNotificationActivationTypeReplied](https://developer.apple.com/documentation/foundation/nsusernotification/activationtype/replied)NSXMLNodeOptions.hAdded [NSXMLNodeNeverEscapeContents](https://developer.apple.com/documentation/foundation/xmlnode/options/1412887-nodeneverescapecontents)Added [NSXMLNodePromoteSignificantWhitespace](https://developer.apple.com/documentation/foundation/xmlnode/options/1415246-nodepromotesignificantwhitespace)NSXPCConnection.hModified [-[NSXPCConnection remoteObjectProxyWithErrorHandler:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1407905-remoteobjectproxywitherrorhandle)

|  | Declaration |
| --- | --- |
| From | - (id)remoteObjectProxyWithErrorHandler:(void (^)(NSError \*))handler |
| To | - (id)remoteObjectProxyWithErrorHandler:(void (^)(NSError \*error))handler |

Modified [-[NSXPCProxyCreating remoteObjectProxyWithErrorHandler:]](https://developer.apple.com/documentation/foundation/nsxpcproxycreating/1415611-remoteobjectproxywitherrorhandle)

|  | Declaration |
| --- | --- |
| From | - (id)remoteObjectProxyWithErrorHandler:(void (^)(NSError \*))handler |
| To | - (id)remoteObjectProxyWithErrorHandler:(void (^)(NSError \*error))handler |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
