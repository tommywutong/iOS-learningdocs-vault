---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Foundation.html
archived_at: '2026-07-18T02:50:38.819096Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Foundation Changes for Objective-C

### Foundation

#### FoundationErrors.h

Added [NSCloudSharingConflictError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscloudsharingconflicterror)Added [NSCloudSharingErrorMaximum](https://developer.apple.com/documentation/foundation/nscloudsharingerrormaximum)Added [NSCloudSharingErrorMinimum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscloudsharingerrorminimum)Added [NSCloudSharingNetworkFailureError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscloudsharingnetworkfailureerror)Added [NSCloudSharingNoPermissionError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscloudsharingnopermissionerror)Added [NSCloudSharingOtherError](https://developer.apple.com/documentation/foundation/nscloudsharingothererror)Added [NSCloudSharingQuotaExceededError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscloudsharingquotaexceedederror)Added [NSCloudSharingTooManyParticipantsError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscloudsharingtoomanyparticipantserror)

#### NSArray.h

Modified [-[NSArray initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype)initWithObjects:(ObjectType  _Nonnull const [])objects count:(NSUInteger)cnt ``` |

#### NSBundle.h

Added [NSBundle.allBundles](https://developer.apple.com/documentation/foundation/nsbundle/1413705-allbundles)Added [NSBundle.allFrameworks](https://developer.apple.com/documentation/foundation/nsbundle/1408056-allframeworks)Added [NSBundle.mainBundle](https://developer.apple.com/documentation/foundation/nsbundle/1410786-mainbundle)

#### NSCalendar.h

Added [NSCalendar.autoupdatingCurrentCalendar](https://developer.apple.com/documentation/foundation/nscalendar/1413771-autoupdatingcurrent)Added [NSCalendar.currentCalendar](https://developer.apple.com/documentation/foundation/nscalendar/1408501-current)Added [NSCalendarIdentifier](https://developer.apple.com/documentation/foundation/nscalendaridentifier)Modified [NSCalendar.calendarIdentifier](https://developer.apple.com/documentation/foundation/nscalendar/1408268-calendaridentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *calendarIdentifier ``` |
| To | ``` @property(readonly, copy) NSCalendarIdentifier calendarIdentifier ``` |

Modified [+[NSCalendar calendarWithIdentifier:]](https://developer.apple.com/documentation/foundation/nscalendar/1412400-calendarwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (NSCalendar *)calendarWithIdentifier:(NSString *)calendarIdentifierConstant ``` |
| To | ``` + (NSCalendar *)calendarWithIdentifier:(NSCalendarIdentifier)calendarIdentifierConstant ``` |

Modified [-[NSCalendar initWithCalendarIdentifier:]](https://developer.apple.com/documentation/foundation/nscalendar/1415991-initwithcalendaridentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCalendarIdentifier:(NSString *)ident ``` |
| To | ``` - (id)initWithCalendarIdentifier:(NSCalendarIdentifier)ident ``` |

#### NSCharacterSet.h

Added [NSCharacterSet.alphanumericCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1407466-alphanumericcharacterset)Added [NSCharacterSet.capitalizedLetterCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1414409-capitalizedlettercharacterset)Added [NSCharacterSet.controlCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416371-controlcharacters)Added [NSCharacterSet.decimalDigitCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1408239-decimaldigits)Added [NSCharacterSet.decomposableCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416868-decomposables)Added [NSCharacterSet.illegalCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416321-illegalcharacterset)Added [NSCharacterSet.letterCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1408569-lettercharacterset)Added [NSCharacterSet.lowercaseLetterCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1417123-lowercaseletters)Added [NSCharacterSet.newlineCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416730-newlinecharacterset)Added [NSCharacterSet.nonBaseCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1407836-nonbasecharacters)Added [NSCharacterSet.punctuationCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1411415-punctuationcharacterset)Added [NSCharacterSet.symbolCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1410965-symbols)Added [NSCharacterSet.uppercaseLetterCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1417569-uppercaselettercharacterset)Added [NSCharacterSet.whitespaceAndNewlineCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1413732-whitespacesandnewlines)Added [NSCharacterSet.whitespaceCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416393-whitespacecharacterset)Modified [NSCharacterSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/cl/NSCharacterSet)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSMutableCharacterSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/cl/NSMutableCharacterSet)

|  | Protocols |
| --- | --- |
| From | NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

#### NSCoder.h

Added [NSCoder.decodingFailurePolicy](https://developer.apple.com/documentation/foundation/nscoder/1642984-decodingfailurepolicy)Added [NSCoder.error](https://developer.apple.com/documentation/foundation/nscoder/1643263-error)Added [NSDecodingFailurePolicy](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy)Added [NSDecodingFailurePolicyRaiseException](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy/raiseexception)Added [NSDecodingFailurePolicySetErrorAndReturn](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy/seterrorandreturn)

#### NSDate.h

Added [NSDate.distantFuture](https://developer.apple.com/documentation/foundation/nsdate/1415385-distantfuture)Added [NSDate.distantPast](https://developer.apple.com/documentation/foundation/nsdate/1418197-distantpast)

#### NSDateComponentsFormatter.h

Added [NSDateComponentsFormatterUnitsStyleBrief](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle/brief)

#### NSDateFormatter.h

Added [NSDateFormatter.defaultFormatterBehavior](https://developer.apple.com/documentation/foundation/nsdateformatter/1409266-defaultformatterbehavior)Modified +[NSDateFormatter setDefaultFormatterBehavior:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setDefaultFormatterBehavior:(NSDateFormatterBehavior)behavior ``` |
| To | ``` + (void)setDefaultFormatterBehavior:(NSDateFormatterBehavior)defaultFormatterBehavior ``` |

#### NSDateInterval.h (Added)

Added [NSDateInterval](https://developer.apple.com/documentation/foundation/nsdateinterval)Added [-[NSDateInterval compare:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641636-compare)Added [-[NSDateInterval containsDate:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641647-contains)Added [NSDateInterval.duration](https://developer.apple.com/documentation/foundation/nsdateinterval/1641643-duration)Added [NSDateInterval.endDate](https://developer.apple.com/documentation/foundation/nsdateinterval/1641651-enddate)Added [-[NSDateInterval init]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641637-init)Added [-[NSDateInterval initWithCoder:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641642-init)Added [-[NSDateInterval initWithStartDate:duration:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641653-initwithstartdate)Added [-[NSDateInterval initWithStartDate:endDate:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641639-init)Added [-[NSDateInterval intersectionWithDateInterval:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641645-intersection)Added [-[NSDateInterval intersectsDateInterval:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641654-intersects)Added [-[NSDateInterval isEqualToDateInterval:]](https://developer.apple.com/documentation/foundation/nsdateinterval/1641650-isequal)Added [NSDateInterval.startDate](https://developer.apple.com/documentation/foundation/nsdateinterval/1641656-startdate)

#### NSDateIntervalFormatter.h

Added [-[NSDateIntervalFormatter stringFromDateInterval:]](https://developer.apple.com/documentation/foundation/dateintervalformatter/1642848-string)

#### NSDecimalNumber.h

Added [NSDecimalNumber.defaultBehavior](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1418084-defaultbehavior)Added [NSDecimalNumber.maximumDecimalNumber](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1415841-maximum)Added [NSDecimalNumber.minimumDecimalNumber](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1413371-minimumdecimalnumber)Added [NSDecimalNumber.notANumber](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1413389-notanumber)Added [NSDecimalNumber.one](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1415711-one)Added [NSDecimalNumber.zero](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1413127-zero)Modified [+[NSDecimalNumber setDefaultBehavior:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/clm/NSDecimalNumber/setDefaultBehavior:)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setDefaultBehavior:(id<NSDecimalNumberBehaviors>)behavior ``` |
| To | ``` + (void)setDefaultBehavior:(id<NSDecimalNumberBehaviors>)defaultBehavior ``` |

#### NSDictionary.h

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const ObjectType  _Nonnull [])objects forKeys:(const id<NSCopying>  _Nonnull [])keys count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype)initWithObjects:(ObjectType  _Nonnull const [])objects forKeys:(id<NSCopying>  _Nonnull const [])keys count:(NSUInteger)cnt ``` |

#### NSDistributedNotificationCenter.h

Added [NSDistributedNotificationCenterType](https://developer.apple.com/documentation/foundation/distributednotificationcenter/centertype)Modified [-[NSDistributedNotificationCenter addObserver:selector:name:object:]](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter/1414151-addobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObserver:(id)observer selector:(SEL)aSelector name:(NSString *)aName object:(NSString *)anObject ``` |
| To | ``` - (void)addObserver:(id)observer selector:(SEL)aSelector name:(NSNotificationName)aName object:(NSString *)anObject ``` |

Modified [-[NSDistributedNotificationCenter addObserver:selector:name:object:suspensionBehavior:]](https://developer.apple.com/documentation/foundation/distributednotificationcenter/1414136-addobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObserver:(id)observer selector:(SEL)selector name:(NSString *)name object:(NSString *)object suspensionBehavior:(NSNotificationSuspensionBehavior)suspensionBehavior ``` |
| To | ``` - (void)addObserver:(id)observer selector:(SEL)selector name:(NSNotificationName)name object:(NSString *)object suspensionBehavior:(NSNotificationSuspensionBehavior)suspensionBehavior ``` |

Modified [+[NSDistributedNotificationCenter notificationCenterForType:]](https://developer.apple.com/documentation/foundation/distributednotificationcenter/1415403-fortype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDistributedNotificationCenter *)notificationCenterForType:(NSString *)notificationCenterType ``` |
| To | ``` + (NSDistributedNotificationCenter *)notificationCenterForType:(NSDistributedNotificationCenterType)notificationCenterType ``` |

Modified [-[NSDistributedNotificationCenter postNotificationName:object:]](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter/1410991-postnotificationname)

|  | Declaration |
| --- | --- |
| From | ``` - (void)postNotificationName:(NSString *)aName object:(NSString *)anObject ``` |
| To | ``` - (void)postNotificationName:(NSNotificationName)aName object:(NSString *)anObject ``` |

Modified [-[NSDistributedNotificationCenter postNotificationName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter/1416995-postnotificationname)

|  | Declaration |
| --- | --- |
| From | ``` - (void)postNotificationName:(NSString *)aName object:(NSString *)anObject userInfo:(NSDictionary *)aUserInfo ``` |
| To | ``` - (void)postNotificationName:(NSNotificationName)aName object:(NSString *)anObject userInfo:(NSDictionary *)aUserInfo ``` |

Modified [-[NSDistributedNotificationCenter postNotificationName:object:userInfo:deliverImmediately:]](https://developer.apple.com/documentation/foundation/distributednotificationcenter/1418360-postnotificationname)

|  | Declaration |
| --- | --- |
| From | ``` - (void)postNotificationName:(NSString *)name object:(NSString *)object userInfo:(NSDictionary *)userInfo deliverImmediately:(BOOL)deliverImmediately ``` |
| To | ``` - (void)postNotificationName:(NSNotificationName)name object:(NSString *)object userInfo:(NSDictionary *)userInfo deliverImmediately:(BOOL)deliverImmediately ``` |

Modified [-[NSDistributedNotificationCenter postNotificationName:object:userInfo:options:]](https://developer.apple.com/documentation/foundation/distributednotificationcenter/1417581-postnotificationname)

|  | Declaration |
| --- | --- |
| From | ``` - (void)postNotificationName:(NSString *)name object:(NSString *)object userInfo:(NSDictionary *)userInfo options:(NSDistributedNotificationOptions)options ``` |
| To | ``` - (void)postNotificationName:(NSNotificationName)name object:(NSString *)object userInfo:(NSDictionary *)userInfo options:(NSDistributedNotificationOptions)options ``` |

Modified [-[NSDistributedNotificationCenter removeObserver:name:object:]](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter/1416236-removeobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObserver:(id)observer name:(NSString *)aName object:(NSString *)anObject ``` |
| To | ``` - (void)removeObserver:(id)observer name:(NSNotificationName)aName object:(NSString *)anObject ``` |

#### NSError.h

Added [NSErrorDomain](https://developer.apple.com/documentation/foundation/nserrordomain)Modified [NSError.domain](https://developer.apple.com/documentation/foundation/nserror/1413924-domain)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *domain ``` |
| To | ``` @property(readonly, copy) NSErrorDomain domain ``` |

Modified [+[NSError errorWithDomain:code:userInfo:]](https://developer.apple.com/documentation/foundation/nserror/1522782-errorwithdomain)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)errorWithDomain:(NSString *)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` |
| To | ``` + (instancetype)errorWithDomain:(NSErrorDomain)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` |

Modified [-[NSError initWithDomain:code:userInfo:]](https://developer.apple.com/documentation/foundation/nserror/1417063-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDomain:(NSString *)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` |
| To | ``` - (instancetype)initWithDomain:(NSErrorDomain)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` |

Modified [+[NSError setUserInfoValueProviderForDomain:provider:]](https://developer.apple.com/documentation/foundation/nserror/1408064-setuserinfovalueproviderfordomai)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setUserInfoValueProviderForDomain:(NSString *)errorDomain provider:(id  _Nullable (^)(NSError *err, NSString *userInfoKey))provider ``` |
| To | ``` + (void)setUserInfoValueProviderForDomain:(NSErrorDomain)errorDomain provider:(id  _Nullable (^)(NSError *err, NSString *userInfoKey))provider ``` |

Modified [+[NSError userInfoValueProviderForDomain:]](https://developer.apple.com/documentation/foundation/nserror/1413427-userinfovalueprovider)

|  | Declaration |
| --- | --- |
| From | ``` + (id  _Nullable (^)(NSError * _Nonnull, NSString * _Nonnull))userInfoValueProviderForDomain:(NSString *)errorDomain ``` |
| To | ``` + (id  _Nullable (^)(NSError * _Nonnull, NSString * _Nonnull))userInfoValueProviderForDomain:(NSErrorDomain)errorDomain ``` |

#### NSException.h

Added [NSAssertionHandler.currentHandler](https://developer.apple.com/documentation/foundation/nsassertionhandler/1417391-currenthandler)Modified [+[NSException exceptionWithName:reason:userInfo:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/clm/NSException/exceptionWithName:reason:userInfo:)

|  | Declaration |
| --- | --- |
| From | ``` + (NSException *)exceptionWithName:(NSString *)name reason:(NSString *)reason userInfo:(NSDictionary *)userInfo ``` |
| To | ``` + (NSException *)exceptionWithName:(NSExceptionName)name reason:(NSString *)reason userInfo:(NSDictionary *)userInfo ``` |

Modified [-[NSException initWithName:reason:userInfo:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/initWithName:reason:userInfo:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)aName reason:(NSString *)aReason userInfo:(NSDictionary *)aUserInfo ``` |
| To | ``` - (instancetype)initWithName:(NSExceptionName)aName reason:(NSString *)aReason userInfo:(NSDictionary *)aUserInfo ``` |

Modified [NSException.name](https://developer.apple.com/documentation/foundation/nsexception/1410925-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *name ``` |
| To | ``` @property(readonly, copy) NSExceptionName name ``` |

Modified [+[NSException raise:format:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/clm/NSException/raise:format:)

|  | Declaration |
| --- | --- |
| From | ``` + (void)raise:(NSString *)name format:(NSString *)format, ... ``` |
| To | ``` + (void)raise:(NSExceptionName)name format:(NSString *)format, ... ``` |

Modified [+[NSException raise:format:arguments:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/clm/NSException/raise:format:arguments:)

|  | Declaration |
| --- | --- |
| From | ``` + (void)raise:(NSString *)name format:(NSString *)format arguments:(va_list)argList ``` |
| To | ``` + (void)raise:(NSExceptionName)name format:(NSString *)format arguments:(va_list)argList ``` |

#### NSFileCoordinator.h

Added [NSFileCoordinator.filePresenters](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1407685-filepresenters)

#### NSFileHandle.h

Added [NSFileHandle.fileHandleWithNullDevice](https://developer.apple.com/documentation/foundation/filehandle/1413881-nulldevice)Added [NSFileHandle.fileHandleWithStandardError](https://developer.apple.com/documentation/foundation/nsfilehandle/1411001-filehandlewithstandarderror)Added [NSFileHandle.fileHandleWithStandardInput](https://developer.apple.com/documentation/foundation/nsfilehandle/1413686-filehandlewithstandardinput)Added [NSFileHandle.fileHandleWithStandardOutput](https://developer.apple.com/documentation/foundation/nsfilehandle/1416965-filehandlewithstandardoutput)Modified [-[NSFileHandle acceptConnectionInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/filehandle/1412997-acceptconnectioninbackgroundandn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)acceptConnectionInBackgroundAndNotifyForModes:(NSArray<NSString *> *)modes ``` |
| To | ``` - (void)acceptConnectionInBackgroundAndNotifyForModes:(NSArray<NSRunLoopMode> *)modes ``` |

Modified [-[NSFileHandle readInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1416294-readinbackgroundandnotifyformode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)readInBackgroundAndNotifyForModes:(NSArray<NSString *> *)modes ``` |
| To | ``` - (void)readInBackgroundAndNotifyForModes:(NSArray<NSRunLoopMode> *)modes ``` |

Modified [-[NSFileHandle readToEndOfFileInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1417321-readtoendoffileinbackgroundandno)

|  | Declaration |
| --- | --- |
| From | ``` - (void)readToEndOfFileInBackgroundAndNotifyForModes:(NSArray<NSString *> *)modes ``` |
| To | ``` - (void)readToEndOfFileInBackgroundAndNotifyForModes:(NSArray<NSRunLoopMode> *)modes ``` |

Modified [-[NSFileHandle waitForDataInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/filehandle/1414643-waitfordatainbackgroundandnotify)

|  | Declaration |
| --- | --- |
| From | ``` - (void)waitForDataInBackgroundAndNotifyForModes:(NSArray<NSString *> *)modes ``` |
| To | ``` - (void)waitForDataInBackgroundAndNotifyForModes:(NSArray<NSRunLoopMode> *)modes ``` |

#### NSFileManager.h

Added [NSFileManager.defaultManager](https://developer.apple.com/documentation/foundation/filemanager/1409234-default)Added [NSFileManager.homeDirectoryForCurrentUser](https://developer.apple.com/documentation/foundation/filemanager/1642807-homedirectoryforcurrentuser)Added [-[NSFileManager homeDirectoryForUser:]](https://developer.apple.com/documentation/foundation/filemanager/1642853-homedirectory)Added [NSFileManager.temporaryDirectory](https://developer.apple.com/documentation/foundation/filemanager/1642996-temporarydirectory)Added [NSFileAttributeKey](https://developer.apple.com/documentation/foundation/nsfileattributekey)Added [NSFileAttributeType](https://developer.apple.com/documentation/foundation/fileattributetype)Added NSFileManager(NSUserInformation)Added [NSFileProtectionType](https://developer.apple.com/documentation/foundation/nsfileprotectiontype)Modified [NSDirectoryEnumerator.directoryAttributes](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1411357-directoryattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary<NSString *,id> *directoryAttributes ``` |
| To | ``` @property(readonly, copy) NSDictionary<NSFileAttributeKey, id> *directoryAttributes ``` |

Modified [NSDirectoryEnumerator.fileAttributes](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1413284-fileattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary<NSString *,id> *fileAttributes ``` |
| To | ``` @property(readonly, copy) NSDictionary<NSFileAttributeKey, id> *fileAttributes ``` |

Modified [-[NSFileManager attributesOfFileSystemForPath:error:]](https://developer.apple.com/documentation/foundation/filemanager/1411896-attributesoffilesystem)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary<NSString *,id> *)attributesOfFileSystemForPath:(NSString *)path error:(NSError * _Nullable *)error ``` |
| To | ``` - (NSDictionary<NSFileAttributeKey,id> *)attributesOfFileSystemForPath:(NSString *)path error:(NSError * _Nullable *)error ``` |

Modified [-[NSFileManager attributesOfItemAtPath:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1410452-attributesofitematpath)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary<NSString *,id> *)attributesOfItemAtPath:(NSString *)path error:(NSError * _Nullable *)error ``` |
| To | ``` - (NSDictionary<NSFileAttributeKey,id> *)attributesOfItemAtPath:(NSString *)path error:(NSError * _Nullable *)error ``` |

Modified [-[NSFileManager contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1413768-contentsofdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<NSURL *> *)contentsOfDirectoryAtURL:(NSURL *)url includingPropertiesForKeys:(NSArray<NSString *> *)keys options:(NSDirectoryEnumerationOptions)mask error:(NSError * _Nullable *)error ``` |
| To | ``` - (NSArray<NSURL *> *)contentsOfDirectoryAtURL:(NSURL *)url includingPropertiesForKeys:(NSArray<NSURLResourceKey> *)keys options:(NSDirectoryEnumerationOptions)mask error:(NSError * _Nullable *)error ``` |

Modified [-[NSFileManager enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1409571-enumeratoraturl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDirectoryEnumerator<NSURL *> *)enumeratorAtURL:(NSURL *)url includingPropertiesForKeys:(NSArray<NSString *> *)keys options:(NSDirectoryEnumerationOptions)mask errorHandler:(BOOL (^)(NSURL *url, NSError *error))handler ``` |
| To | ``` - (NSDirectoryEnumerator<NSURL *> *)enumeratorAtURL:(NSURL *)url includingPropertiesForKeys:(NSArray<NSURLResourceKey> *)keys options:(NSDirectoryEnumerationOptions)mask errorHandler:(BOOL (^)(NSURL *url, NSError *error))handler ``` |

Modified [-[NSFileManager mountedVolumeURLsIncludingResourceValuesForKeys:options:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1409626-mountedvolumeurlsincludingresour)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray<NSURL *> *)mountedVolumeURLsIncludingResourceValuesForKeys:(NSArray<NSString *> *)propertyKeys options:(NSVolumeEnumerationOptions)options ``` |
| To | ``` - (NSArray<NSURL *> *)mountedVolumeURLsIncludingResourceValuesForKeys:(NSArray<NSURLResourceKey> *)propertyKeys options:(NSVolumeEnumerationOptions)options ``` |

Modified [-[NSFileManager setAttributes:ofItemAtPath:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1413667-setattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setAttributes:(NSDictionary<NSString *,id> *)attributes ofItemAtPath:(NSString *)path error:(NSError * _Nullable *)error ``` |
| To | ``` - (BOOL)setAttributes:(NSDictionary<NSFileAttributeKey,id> *)attributes ofItemAtPath:(NSString *)path error:(NSError * _Nullable *)error ``` |

#### NSHTTPCookie.h

Added [NSHTTPCookiePropertyKey](https://developer.apple.com/documentation/foundation/httpcookiepropertykey)Modified [+[NSHTTPCookie cookieWithProperties:]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392967-cookiewithproperties)

|  | Declaration |
| --- | --- |
| From | ``` + (NSHTTPCookie *)cookieWithProperties:(NSDictionary<NSString *,id> *)properties ``` |
| To | ``` + (NSHTTPCookie *)cookieWithProperties:(NSDictionary<NSHTTPCookiePropertyKey,id> *)properties ``` |

Modified [-[NSHTTPCookie initWithProperties:]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392975-initwithproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithProperties:(NSDictionary<NSString *,id> *)properties ``` |
| To | ``` - (instancetype)initWithProperties:(NSDictionary<NSHTTPCookiePropertyKey,id> *)properties ``` |

Modified [NSHTTPCookie.properties](https://developer.apple.com/documentation/foundation/nshttpcookie/1393017-properties)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary<NSString *,id> *properties ``` |
| To | ``` @property(readonly, copy) NSDictionary<NSHTTPCookiePropertyKey, id> *properties ``` |

#### NSHTTPCookieStorage.h

Added [NSHTTPCookieStorage.sharedHTTPCookieStorage](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1416095-sharedhttpcookiestorage)

#### NSISO8601DateFormatter.h (Added)

Added [NSISO8601DateFormatter](https://developer.apple.com/documentation/foundation/nsiso8601dateformatter)Added [-[NSISO8601DateFormatter dateFromString:]](https://developer.apple.com/documentation/foundation/nsiso8601dateformatter/1643127-datefromstring)Added [NSISO8601DateFormatter.formatOptions](https://developer.apple.com/documentation/foundation/nsiso8601dateformatter/1643324-formatoptions)Added [-[NSISO8601DateFormatter init]](https://developer.apple.com/documentation/foundation/iso8601dateformatter/1643114-init)Added [-[NSISO8601DateFormatter stringFromDate:]](https://developer.apple.com/documentation/foundation/iso8601dateformatter/1643076-string)Added [+[NSISO8601DateFormatter stringFromDate:timeZone:formatOptions:]](https://developer.apple.com/documentation/foundation/iso8601dateformatter/1642834-string)Added [NSISO8601DateFormatter.timeZone](https://developer.apple.com/documentation/foundation/nsiso8601dateformatter/1643185-timezone)Added [NSISO8601DateFormatOptions](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions)Added [NSISO8601DateFormatWithColonSeparatorInTime](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithcolonseparatorintime)Added [NSISO8601DateFormatWithColonSeparatorInTimeZone](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithcolonseparatorintimezone)Added [NSISO8601DateFormatWithDashSeparatorInDate](https://developer.apple.com/documentation/foundation/iso8601dateformatter/options/1642784-withdashseparatorindate)Added [NSISO8601DateFormatWithDay](https://developer.apple.com/documentation/foundation/iso8601dateformatter/options/1643108-withday)Added [NSISO8601DateFormatWithFullDate](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithfulldate)Added [NSISO8601DateFormatWithFullTime](https://developer.apple.com/documentation/foundation/iso8601dateformatter/options/1642935-withfulltime)Added [NSISO8601DateFormatWithInternetDateTime](https://developer.apple.com/documentation/foundation/iso8601dateformatter/options/1643217-withinternetdatetime)Added [NSISO8601DateFormatWithMonth](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithmonth)Added [NSISO8601DateFormatWithSpaceBetweenDateAndTime](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithspacebetweendateandtime)Added [NSISO8601DateFormatWithTime](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithtime)Added [NSISO8601DateFormatWithTimeZone](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithtimezone)Added [NSISO8601DateFormatWithWeekOfYear](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithweekofyear)Added [NSISO8601DateFormatWithYear](https://developer.apple.com/documentation/foundation/nsiso8601dateformatoptions/nsiso8601dateformatwithyear)

#### NSKeyedArchiver.h

Added [NSKeyedArchiver.encodedData](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1643042-encodeddata)Added [-[NSKeyedArchiver init]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1642790-init)Added [NSKeyedUnarchiver.decodingFailurePolicy](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1643164-decodingfailurepolicy)

#### NSKeyValueCoding.h

Added [NSObject.accessInstanceVariablesDirectly](https://developer.apple.com/documentation/objectivec/nsobject/1415307-accessinstancevariablesdirectly)Added [NSKeyValueOperator](https://developer.apple.com/documentation/foundation/nskeyvalueoperator)

#### NSKeyValueObserving.h

Added [NSKeyValueChangeKey](https://developer.apple.com/documentation/foundation/nskeyvaluechangekey)Modified [-[NSObject observeValueForKeyPath:ofObject:change:context:]](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath)

|  | Declaration |
| --- | --- |
| From | ``` - (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary<NSString *,id> *)change context:(void *)context ``` |
| To | ``` - (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary<NSKeyValueChangeKey,id> *)change context:(void *)context ``` |

#### NSLocale.h

Added [NSLocale.alternateQuotationBeginDelimiter](https://developer.apple.com/documentation/foundation/nslocale/1643238-alternatequotationbegindelimiter)Added [NSLocale.alternateQuotationEndDelimiter](https://developer.apple.com/documentation/foundation/nslocale/1642885-alternatequotationenddelimiter)Added [NSLocale.autoupdatingCurrentLocale](https://developer.apple.com/documentation/foundation/nslocale/1414388-autoupdatingcurrentlocale)Added [NSLocale.availableLocaleIdentifiers](https://developer.apple.com/documentation/foundation/nslocale/1410448-availablelocaleidentifiers)Added [NSLocale.calendarIdentifier](https://developer.apple.com/documentation/foundation/nslocale/2242779-calendaridentifier)Added [NSLocale.collationIdentifier](https://developer.apple.com/documentation/foundation/nslocale/1643092-collationidentifier)Added [NSLocale.collatorIdentifier](https://developer.apple.com/documentation/foundation/nslocale/1643195-collatoridentifier)Added [NSLocale.commonISOCurrencyCodes](https://developer.apple.com/documentation/foundation/nslocale/1407272-commonisocurrencycodes)Added [NSLocale.countryCode](https://developer.apple.com/documentation/foundation/nslocale/1643060-countrycode)Added [NSLocale.currencyCode](https://developer.apple.com/documentation/foundation/nslocale/1642836-currencycode)Added [NSLocale.currencySymbol](https://developer.apple.com/documentation/foundation/nslocale/1642814-currencysymbol)Added [NSLocale.currentLocale](https://developer.apple.com/documentation/foundation/nslocale/1409990-currentlocale)Added [NSLocale.decimalSeparator](https://developer.apple.com/documentation/foundation/nslocale/1643064-decimalseparator)Added [NSLocale.exemplarCharacterSet](https://developer.apple.com/documentation/foundation/nslocale/1643019-exemplarcharacterset)Added [NSLocale.groupingSeparator](https://developer.apple.com/documentation/foundation/nslocale/1643096-groupingseparator)Added [NSLocale.ISOCountryCodes](https://developer.apple.com/documentation/foundation/nslocale/1413869-isocountrycodes)Added [NSLocale.ISOCurrencyCodes](https://developer.apple.com/documentation/foundation/nslocale/1417834-isocurrencycodes)Added [NSLocale.ISOLanguageCodes](https://developer.apple.com/documentation/foundation/nslocale/1418015-isolanguagecodes)Added [NSLocale.languageCode](https://developer.apple.com/documentation/foundation/nslocale/1643026-languagecode)Added [-[NSLocale localizedStringForCalendarIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/2242780-localizedstringforcalendaridenti)Added [-[NSLocale localizedStringForCollationIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1642875-localizedstring)Added [-[NSLocale localizedStringForCollatorIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1643004-localizedstring)Added [-[NSLocale localizedStringForCountryCode:]](https://developer.apple.com/documentation/foundation/nslocale/1642920-localizedstring)Added [-[NSLocale localizedStringForCurrencyCode:]](https://developer.apple.com/documentation/foundation/nslocale/1643179-localizedstring)Added [-[NSLocale localizedStringForLanguageCode:]](https://developer.apple.com/documentation/foundation/nslocale/1643226-localizedstringforlanguagecode)Added [-[NSLocale localizedStringForLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1642864-localizedstringforlocaleidentifi)Added [-[NSLocale localizedStringForScriptCode:]](https://developer.apple.com/documentation/foundation/nslocale/1643126-localizedstring)Added [-[NSLocale localizedStringForVariantCode:]](https://developer.apple.com/documentation/foundation/nslocale/1643264-localizedstring)Added [NSLocale.preferredLanguages](https://developer.apple.com/documentation/foundation/nslocale/1415614-preferredlanguages)Added [NSLocale.quotationBeginDelimiter](https://developer.apple.com/documentation/foundation/nslocale/1643155-quotationbegindelimiter)Added [NSLocale.quotationEndDelimiter](https://developer.apple.com/documentation/foundation/nslocale/1643162-quotationenddelimiter)Added [NSLocale.scriptCode](https://developer.apple.com/documentation/foundation/nslocale/1643213-scriptcode)Added [NSLocale.systemLocale](https://developer.apple.com/documentation/foundation/nslocale/1407691-system)Added [NSLocale.usesMetricSystem](https://developer.apple.com/documentation/foundation/nslocale/1643225-usesmetricsystem)Added [NSLocale.variantCode](https://developer.apple.com/documentation/foundation/nslocale/1643152-variantcode)Added [NSLocaleKey](https://developer.apple.com/documentation/foundation/nslocale/key)Modified [-[NSLocale displayNameForKey:value:]](https://developer.apple.com/documentation/foundation/nslocale/1415931-displayname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)displayNameForKey:(id)key value:(id)value ``` |
| To | ``` - (NSString *)displayNameForKey:(NSLocaleKey)key value:(id)value ``` |

Modified [-[NSLocale objectForKey:]](https://developer.apple.com/documentation/foundation/nslocale/1418430-objectforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKey:(id)key ``` |
| To | ``` - (id)objectForKey:(NSLocaleKey)key ``` |

#### NSMeasurement.h (Added)

Added [NSMeasurement](https://developer.apple.com/documentation/foundation/nsmeasurement)Added [-[NSMeasurement canBeConvertedToUnit:]](https://developer.apple.com/documentation/foundation/nsmeasurement/1690850-canbeconverted)Added [NSMeasurement.doubleValue](https://developer.apple.com/documentation/foundation/nsmeasurement/1643124-doublevalue)Added [-[NSMeasurement initWithDoubleValue:unit:]](https://developer.apple.com/documentation/foundation/nsmeasurement/1643012-initwithdoublevalue)Added [-[NSMeasurement measurementByAddingMeasurement:]](https://developer.apple.com/documentation/foundation/nsmeasurement/1643170-measurementbyaddingmeasurement)Added [-[NSMeasurement measurementByConvertingToUnit:]](https://developer.apple.com/documentation/foundation/nsmeasurement/1642900-measurementbyconvertingtounit)Added [-[NSMeasurement measurementBySubtractingMeasurement:]](https://developer.apple.com/documentation/foundation/nsmeasurement/1642872-measurementbysubtractingmeasurem)Added [NSMeasurement.unit](https://developer.apple.com/documentation/foundation/nsmeasurement/1642831-unit)

#### NSMeasurementFormatter.h (Added)

Added [NSMeasurementFormatter](https://developer.apple.com/documentation/foundation/nsmeasurementformatter)Added [NSMeasurementFormatter.locale](https://developer.apple.com/documentation/foundation/measurementformatter/1642061-locale)Added [NSMeasurementFormatter.numberFormatter](https://developer.apple.com/documentation/foundation/measurementformatter/1642056-numberformatter)Added [-[NSMeasurementFormatter stringFromMeasurement:]](https://developer.apple.com/documentation/foundation/measurementformatter/1642057-string)Added [-[NSMeasurementFormatter stringFromUnit:]](https://developer.apple.com/documentation/foundation/measurementformatter/1642059-string)Added [NSMeasurementFormatter.unitOptions](https://developer.apple.com/documentation/foundation/measurementformatter/1642066-unitoptions)Added [NSMeasurementFormatter.unitStyle](https://developer.apple.com/documentation/foundation/measurementformatter/1642067-unitstyle)Added [NSMeasurementFormatterUnitOptions](https://developer.apple.com/documentation/foundation/measurementformatter/unitoptions)Added [NSMeasurementFormatterUnitOptionsNaturalScale](https://developer.apple.com/documentation/foundation/measurementformatter/unitoptions/1642065-naturalscale)Added [NSMeasurementFormatterUnitOptionsProvidedUnit](https://developer.apple.com/documentation/foundation/measurementformatter/unitoptions/1642063-providedunit)Added [NSMeasurementFormatterUnitOptionsTemperatureWithoutUnit](https://developer.apple.com/documentation/foundation/nsmeasurementformatterunitoptions/nsmeasurementformatterunitoptionstemperaturewithoutunit)

#### NSNetServices.h

Modified [-[NSNetService removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/netservice/1414621-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)removeFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSNetService scheduleInRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsnetservice/1417221-scheduleinrunloop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSNetServiceBrowser removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1411566-removefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)removeFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSNetServiceBrowser scheduleInRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1409776-scheduleinrunloop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

#### NSNotification.h

Added [NSNotificationCenter.defaultCenter](https://developer.apple.com/documentation/foundation/nsnotificationcenter/1414169-defaultcenter)Added [NSNotificationName](https://developer.apple.com/documentation/foundation/nsnotification/name)Modified [-[NSNotification initWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1415764-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name object:(id)object userInfo:(NSDictionary *)userInfo ``` |
| To | ``` - (instancetype)initWithName:(NSNotificationName)name object:(id)object userInfo:(NSDictionary *)userInfo ``` |

Modified [NSNotification.name](https://developer.apple.com/documentation/foundation/nsnotification/1416472-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *name ``` |
| To | ``` @property(readonly, copy) NSNotificationName name ``` |

Modified [+[NSNotification notificationWithName:object:]](https://developer.apple.com/documentation/foundation/nsnotification/1417440-notificationwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)notificationWithName:(NSString *)aName object:(id)anObject ``` |
| To | ``` + (instancetype)notificationWithName:(NSNotificationName)aName object:(id)anObject ``` |

Modified [+[NSNotification notificationWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1574705-notificationwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)notificationWithName:(NSString *)aName object:(id)anObject userInfo:(NSDictionary *)aUserInfo ``` |
| To | ``` + (instancetype)notificationWithName:(NSNotificationName)aName object:(id)anObject userInfo:(NSDictionary *)aUserInfo ``` |

Modified [-[NSNotificationCenter addObserver:selector:name:object:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/addObserver:selector:name:object:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObserver:(id)observer selector:(SEL)aSelector name:(NSString *)aName object:(id)anObject ``` |
| To | ``` - (void)addObserver:(id)observer selector:(SEL)aSelector name:(NSNotificationName)aName object:(id)anObject ``` |

Modified [-[NSNotificationCenter addObserverForName:object:queue:usingBlock:]](https://developer.apple.com/documentation/foundation/nsnotificationcenter/1411723-addobserverforname)

|  | Declaration |
| --- | --- |
| From | ``` - (id<NSObject>)addObserverForName:(NSString *)name object:(id)obj queue:(NSOperationQueue *)queue usingBlock:(void (^)(NSNotification *note))block ``` |
| To | ``` - (id<NSObject>)addObserverForName:(NSNotificationName)name object:(id)obj queue:(NSOperationQueue *)queue usingBlock:(void (^)(NSNotification *note))block ``` |

Modified [-[NSNotificationCenter postNotificationName:object:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/postNotificationName:object:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)postNotificationName:(NSString *)aName object:(id)anObject ``` |
| To | ``` - (void)postNotificationName:(NSNotificationName)aName object:(id)anObject ``` |

Modified [-[NSNotificationCenter postNotificationName:object:userInfo:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/postNotificationName:object:userInfo:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)postNotificationName:(NSString *)aName object:(id)anObject userInfo:(NSDictionary *)aUserInfo ``` |
| To | ``` - (void)postNotificationName:(NSNotificationName)aName object:(id)anObject userInfo:(NSDictionary *)aUserInfo ``` |

Modified [-[NSNotificationCenter removeObserver:name:object:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/removeObserver:name:object:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObserver:(id)observer name:(NSString *)aName object:(id)anObject ``` |
| To | ``` - (void)removeObserver:(id)observer name:(NSNotificationName)aName object:(id)anObject ``` |

#### NSNotificationQueue.h

Added [NSNotificationQueue.defaultQueue](https://developer.apple.com/documentation/foundation/nsnotificationqueue/1412392-defaultqueue)Modified [-[NSNotificationQueue enqueueNotification:postingStyle:coalesceMask:forModes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/instm/NSNotificationQueue/enqueueNotification:postingStyle:coalesceMask:forModes:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enqueueNotification:(NSNotification *)notification postingStyle:(NSPostingStyle)postingStyle coalesceMask:(NSNotificationCoalescing)coalesceMask forModes:(NSArray<NSString *> *)modes ``` |
| To | ``` - (void)enqueueNotification:(NSNotification *)notification postingStyle:(NSPostingStyle)postingStyle coalesceMask:(NSNotificationCoalescing)coalesceMask forModes:(NSArray<NSRunLoopMode> *)modes ``` |

#### NSObjCRuntime.h

Added #def FOUNDATION_SWIFT_SDK_EPOCH_AT_LEASTAdded #def FOUNDATION_SWIFT_SDK_EPOCH_LESS_THANAdded #def NS_DEPRECATED_WITH_REPLACEMENT_MACAdded #def NS_EXTENSIBLE_STRING_ENUMAdded #def NS_NO_TAIL_CALLAdded #def NS_NOESCAPEAdded #def NS_STRING_ENUMAdded [NSExceptionName](https://developer.apple.com/documentation/foundation/nsexceptionname)Added [#def NSFoundationVersionNumber10_10_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_4)Added [#def NSFoundationVersionNumber10_10_5](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_5)Added [#def NSFoundationVersionNumber10_10_Max](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_max)Added [#def NSFoundationVersionNumber10_11](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_11)Added [#def NSFoundationVersionNumber10_11_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_11_1)Added [#def NSFoundationVersionNumber10_11_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_11_2)Added [#def NSFoundationVersionNumber10_11_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_11_3)Added [#def NSFoundationVersionNumber10_11_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_11_4)Added [#def NSFoundationVersionNumber10_11_Max](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_11_max)Added [NSRunLoopMode](https://developer.apple.com/documentation/foundation/nsrunloopmode)

#### NSObject.h

Added [NSSecureCoding.supportsSecureCoding](https://developer.apple.com/documentation/foundation/nssecurecoding/1855946-supportssecurecoding)

#### NSOperation.h

Added [NSOperationQueue.currentQueue](https://developer.apple.com/documentation/foundation/nsoperationqueue/1413097-currentqueue)Added [NSOperationQueue.mainQueue](https://developer.apple.com/documentation/foundation/nsoperationqueue/1409193-mainqueue)

#### NSOrderedSet.h

Modified [-[NSOrderedSet initWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411910-initwithobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype)initWithObjects:(ObjectType  _Nonnull const [])objects count:(NSUInteger)cnt ``` |

#### NSPersonNameComponentsFormatter.h

Added [-[NSPersonNameComponentsFormatter personNameComponentsFromString:]](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter/1642979-personnamecomponentsfromstring)

#### NSPointerFunctions.h

Modified [NSPointerFunctions.usesStrongWriteBarrier](https://developer.apple.com/documentation/foundation/nspointerfunctions/1410762-usesstrongwritebarrier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NSPointerFunctions.usesWeakReadAndWriteBarriers](https://developer.apple.com/documentation/foundation/nspointerfunctions/1411097-usesweakreadandwritebarriers)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### NSPort.h

Modified [-[NSMachPort removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsmachport/1399555-removefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeFromRunLoop:(NSRunLoop *)runLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)removeFromRunLoop:(NSRunLoop *)runLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSMachPort scheduleInRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsmachport/1399523-scheduleinrunloop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleInRunLoop:(NSRunLoop *)runLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)scheduleInRunLoop:(NSRunLoop *)runLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSPort addConnection:toRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsport/1399553-addconnection)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addConnection:(NSConnection *)conn toRunLoop:(NSRunLoop *)runLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)addConnection:(NSConnection *)conn toRunLoop:(NSRunLoop *)runLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSPort removeConnection:fromRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsport/1399501-removeconnection)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeConnection:(NSConnection *)conn fromRunLoop:(NSRunLoop *)runLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)removeConnection:(NSConnection *)conn fromRunLoop:(NSRunLoop *)runLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSPort removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsport/1399525-removefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeFromRunLoop:(NSRunLoop *)runLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)removeFromRunLoop:(NSRunLoop *)runLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSPort scheduleInRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/port/1399517-schedule)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleInRunLoop:(NSRunLoop *)runLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)scheduleInRunLoop:(NSRunLoop *)runLoop forMode:(NSRunLoopMode)mode ``` |

#### NSProcessInfo.h

Added [NSProcessInfo.fullUserName](https://developer.apple.com/documentation/foundation/processinfo/1643199-fullusername)Added [NSProcessInfo.processInfo](https://developer.apple.com/documentation/foundation/nsprocessinfo/1408734-processinfo)Added [NSProcessInfo.userName](https://developer.apple.com/documentation/foundation/nsprocessinfo/1643193-username)Added NSProcessInfo(NSUserInformation)

#### NSProgress.h

Added [NSProgressFileOperationKind](https://developer.apple.com/documentation/foundation/nsprogressfileoperationkind)Added [NSProgressKind](https://developer.apple.com/documentation/foundation/nsprogresskind)Added [NSProgressUserInfoKey](https://developer.apple.com/documentation/foundation/nsprogressuserinfokey)Modified [NSProgress.kind](https://developer.apple.com/documentation/foundation/progress/1416139-kind)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *kind ``` |
| To | ``` @property(copy) NSProgressKind kind ``` |

Modified [-[NSProgress setUserInfoObject:forKey:]](https://developer.apple.com/documentation/foundation/nsprogress/1407537-setuserinfoobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setUserInfoObject:(id)objectOrNil forKey:(NSString *)key ``` |
| To | ``` - (void)setUserInfoObject:(id)objectOrNil forKey:(NSProgressUserInfoKey)key ``` |

Modified [NSProgress.userInfo](https://developer.apple.com/documentation/foundation/nsprogress/1413314-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *userInfo ``` |
| To | ``` @property(readonly, copy) NSDictionary<NSProgressUserInfoKey, id> *userInfo ``` |

#### NSRunLoop.h

Added [NSRunLoop.currentRunLoop](https://developer.apple.com/documentation/foundation/nsrunloop/1412291-currentrunloop)Added [NSRunLoop.mainRunLoop](https://developer.apple.com/documentation/foundation/runloop/1418388-main)Added [-[NSRunLoop performBlock:]](https://developer.apple.com/documentation/foundation/runloop/2091881-perform)Added [-[NSRunLoop performInModes:block:]](https://developer.apple.com/documentation/foundation/nsrunloop/2091880-performinmodes)Modified [-[NSObject performSelector:withObject:afterDelay:inModes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/performSelector:withObject:afterDelay:inModes:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performSelector:(SEL)aSelector withObject:(id)anArgument afterDelay:(NSTimeInterval)delay inModes:(NSArray<NSString *> *)modes ``` |
| To | ``` - (void)performSelector:(SEL)aSelector withObject:(id)anArgument afterDelay:(NSTimeInterval)delay inModes:(NSArray<NSRunLoopMode> *)modes ``` |

Modified [-[NSRunLoop acceptInputForMode:beforeDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/acceptInputForMode:beforeDate:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)acceptInputForMode:(NSString *)mode beforeDate:(NSDate *)limitDate ``` |
| To | ``` - (void)acceptInputForMode:(NSRunLoopMode)mode beforeDate:(NSDate *)limitDate ``` |

Modified [-[NSRunLoop addPort:forMode:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/addPort:forMode:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addPort:(NSPort *)aPort forMode:(NSString *)mode ``` |
| To | ``` - (void)addPort:(NSPort *)aPort forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSRunLoop addTimer:forMode:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/addTimer:forMode:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addTimer:(NSTimer *)timer forMode:(NSString *)mode ``` |
| To | ``` - (void)addTimer:(NSTimer *)timer forMode:(NSRunLoopMode)mode ``` |

Modified [NSRunLoop.currentMode](https://developer.apple.com/documentation/foundation/nsrunloop/1412652-currentmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *currentMode ``` |
| To | ``` @property(readonly, copy) NSRunLoopMode currentMode ``` |

Modified [-[NSRunLoop limitDateForMode:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/limitDateForMode:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDate *)limitDateForMode:(NSString *)mode ``` |
| To | ``` - (NSDate *)limitDateForMode:(NSRunLoopMode)mode ``` |

Modified [-[NSRunLoop performSelector:target:argument:order:modes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/performSelector:target:argument:order:modes:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performSelector:(SEL)aSelector target:(id)target argument:(id)arg order:(NSUInteger)order modes:(NSArray<NSString *> *)modes ``` |
| To | ``` - (void)performSelector:(SEL)aSelector target:(id)target argument:(id)arg order:(NSUInteger)order modes:(NSArray<NSRunLoopMode> *)modes ``` |

Modified [-[NSRunLoop removePort:forMode:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/removePort:forMode:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removePort:(NSPort *)aPort forMode:(NSString *)mode ``` |
| To | ``` - (void)removePort:(NSPort *)aPort forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSRunLoop runMode:beforeDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/runMode:beforeDate:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)runMode:(NSString *)mode beforeDate:(NSDate *)limitDate ``` |
| To | ``` - (BOOL)runMode:(NSRunLoopMode)mode beforeDate:(NSDate *)limitDate ``` |

#### NSSet.h

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype)initWithObjects:(ObjectType  _Nonnull const [])objects count:(NSUInteger)cnt ``` |

#### NSStream.h

Added [NSStreamNetworkServiceTypeCallSignaling](https://developer.apple.com/documentation/foundation/streamnetworkservicetypevalue/2142917-callsignaling)Added [NSStreamNetworkServiceTypeValue](https://developer.apple.com/documentation/foundation/streamnetworkservicetypevalue)Added [NSStreamPropertyKey](https://developer.apple.com/documentation/foundation/nsstreampropertykey)Added [NSStreamSocketSecurityLevel](https://developer.apple.com/documentation/foundation/streamsocketsecuritylevel)Added [NSStreamSOCKSProxyConfiguration](https://developer.apple.com/documentation/foundation/nsstreamsocksproxyconfiguration)Added [NSStreamSOCKSProxyVersion](https://developer.apple.com/documentation/foundation/streamsocksproxyversion)Modified [-[NSStream propertyForKey:]](https://developer.apple.com/documentation/foundation/stream/1410226-property)

|  | Declaration |
| --- | --- |
| From | ``` - (id)propertyForKey:(NSString *)key ``` |
| To | ``` - (id)propertyForKey:(NSStreamPropertyKey)key ``` |

Modified [-[NSStream removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/stream/1411285-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)removeFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSStream scheduleInRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsstream/1417370-scheduleinrunloop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSStream setProperty:forKey:]](https://developer.apple.com/documentation/foundation/nsstream/1412045-setproperty)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setProperty:(id)property forKey:(NSString *)key ``` |
| To | ``` - (BOOL)setProperty:(id)property forKey:(NSStreamPropertyKey)key ``` |

#### NSString.h

Added [NSString.availableStringEncodings](https://developer.apple.com/documentation/foundation/nsstring/1417579-availablestringencodings)Added [NSString.defaultCStringEncoding](https://developer.apple.com/documentation/foundation/nsstring/1410091-defaultcstringencoding)Added [NSStringEncodingDetectionOptionsKey](https://developer.apple.com/documentation/foundation/nsstringencodingdetectionoptionskey)Added [NSStringTransform](https://developer.apple.com/documentation/foundation/stringtransform)Modified [-[NSString compare:options:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:options:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSComparisonResult)compare:(NSString *)string options:(NSStringCompareOptions)mask range:(NSRange)compareRange ``` |
| To | ``` - (NSComparisonResult)compare:(NSString *)string options:(NSStringCompareOptions)mask range:(NSRange)rangeOfReceiverToCompare ``` |

Modified [-[NSString compare:options:range:locale:]](https://developer.apple.com/documentation/foundation/nsstring/1414561-compare)

|  | Declaration |
| --- | --- |
| From | ``` - (NSComparisonResult)compare:(NSString *)string options:(NSStringCompareOptions)mask range:(NSRange)compareRange locale:(id)locale ``` |
| To | ``` - (NSComparisonResult)compare:(NSString *)string options:(NSStringCompareOptions)mask range:(NSRange)rangeOfReceiverToCompare locale:(id)locale ``` |

Modified [-[NSString rangeOfCharacterFromSet:options:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:options:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet *)searchSet options:(NSStringCompareOptions)mask range:(NSRange)searchRange ``` |
| To | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet *)searchSet options:(NSStringCompareOptions)mask range:(NSRange)rangeOfReceiverToSearch ``` |

Modified [-[NSString rangeOfString:options:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfString:(NSString *)searchString options:(NSStringCompareOptions)mask range:(NSRange)searchRange ``` |
| To | ``` - (NSRange)rangeOfString:(NSString *)searchString options:(NSStringCompareOptions)mask range:(NSRange)rangeOfReceiverToSearch ``` |

Modified [-[NSString rangeOfString:options:range:locale:]](https://developer.apple.com/documentation/foundation/nsstring/1417348-range)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfString:(NSString *)searchString options:(NSStringCompareOptions)mask range:(NSRange)searchRange locale:(NSLocale *)locale ``` |
| To | ``` - (NSRange)rangeOfString:(NSString *)searchString options:(NSStringCompareOptions)mask range:(NSRange)rangeOfReceiverToSearch locale:(NSLocale *)locale ``` |

Modified [-[NSString stringByApplyingTransform:reverse:]](https://developer.apple.com/documentation/foundation/nsstring/1407787-applyingtransform)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)stringByApplyingTransform:(NSString *)transform reverse:(BOOL)reverse ``` |
| To | ``` - (NSString *)stringByApplyingTransform:(NSStringTransform)transform reverse:(BOOL)reverse ``` |

Modified [+[NSString stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:]](https://developer.apple.com/documentation/foundation/nsstring/1413576-stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` + (NSStringEncoding)stringEncodingForData:(NSData *)data encodingOptions:(NSDictionary<NSString *,id> *)opts convertedString:(NSString * _Nullable *)string usedLossyConversion:(BOOL *)usedLossyConversion ``` |
| To | ``` + (NSStringEncoding)stringEncodingForData:(NSData *)data encodingOptions:(NSDictionary<NSStringEncodingDetectionOptionsKey,id> *)opts convertedString:(NSString * _Nullable *)string usedLossyConversion:(BOOL *)usedLossyConversion ``` |

#### NSTextCheckingResult.h

Modified [+[NSTextCheckingResult grammarCheckingResultWithRange:details:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407190-grammarcheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` + (NSTextCheckingResult *)grammarCheckingResultWithRange:(NSRange)range details:(NSArray<NSString *> *)details ``` |
| To | ``` + (NSTextCheckingResult *)grammarCheckingResultWithRange:(NSRange)range details:(NSArray<NSDictionary<NSString *,id> *> *)details ``` |

Modified [NSTextCheckingResult.grammarDetails](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1408959-grammardetails)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray<NSString *> *grammarDetails ``` |
| To | ``` @property(readonly, copy) NSArray<NSDictionary<NSString *,id> *> *grammarDetails ``` |

#### NSThread.h

Added [NSThread.callStackReturnAddresses](https://developer.apple.com/documentation/foundation/thread/1409565-callstackreturnaddresses)Added [NSThread.callStackSymbols](https://developer.apple.com/documentation/foundation/thread/1414836-callstacksymbols)Added [NSThread.currentThread](https://developer.apple.com/documentation/foundation/thread/1410679-current)Added [+[NSThread detachNewThreadWithBlock:]](https://developer.apple.com/documentation/foundation/nsthread/2088563-detachnewthreadwithblock)Added [-[NSThread initWithBlock:]](https://developer.apple.com/documentation/foundation/nsthread/2088561-initwithblock)Added [NSThread.mainThread](https://developer.apple.com/documentation/foundation/thread/1414782-main)

#### NSTimer.h

Added [-[NSTimer initWithFireDate:interval:repeats:block:]](https://developer.apple.com/documentation/foundation/nstimer/2091887-initwithfiredate)Added [+[NSTimer scheduledTimerWithTimeInterval:repeats:block:]](https://developer.apple.com/documentation/foundation/nstimer/2091889-scheduledtimerwithtimeinterval)Added [+[NSTimer timerWithTimeInterval:repeats:block:]](https://developer.apple.com/documentation/foundation/timer/2091888-init)

#### NSTimeZone.h

Added [NSTimeZone.abbreviationDictionary](https://developer.apple.com/documentation/foundation/nstimezone/1387258-abbreviationdictionary)Added [NSTimeZone.defaultTimeZone](https://developer.apple.com/documentation/foundation/nstimezone/1387244-defaulttimezone)Added [NSTimeZone.knownTimeZoneNames](https://developer.apple.com/documentation/foundation/nstimezone/1387223-knowntimezonenames)Added [NSTimeZone.localTimeZone](https://developer.apple.com/documentation/foundation/nstimezone/1387209-local)Added [NSTimeZone.systemTimeZone](https://developer.apple.com/documentation/foundation/nstimezone/1387231-systemtimezone)Added [NSTimeZone.timeZoneDataVersion](https://developer.apple.com/documentation/foundation/nstimezone/1387187-timezonedataversion)Modified +[NSTimeZone setAbbreviationDictionary:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setAbbreviationDictionary:(NSDictionary<NSString *,NSString *> *)dict ``` |
| To | ``` + (void)setAbbreviationDictionary:(NSDictionary<NSString *,NSString *> *)abbreviationDictionary ``` |

Modified [+[NSTimeZone setDefaultTimeZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/setDefaultTimeZone:)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setDefaultTimeZone:(NSTimeZone *)aTimeZone ``` |
| To | ``` + (void)setDefaultTimeZone:(NSTimeZone *)defaultTimeZone ``` |

#### NSUndoManager.h

Modified [NSUndoManager.runLoopModes](https://developer.apple.com/documentation/foundation/nsundomanager/1409504-runloopmodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray<NSString *> *runLoopModes ``` |
| To | ``` @property(copy) NSArray<NSRunLoopMode> *runLoopModes ``` |

#### NSUnit.h (Added)

Added [NSDimension](https://developer.apple.com/documentation/foundation/nsdimension)Added [+[NSDimension baseUnit]](https://developer.apple.com/documentation/foundation/dimension/1690740-baseunit)Added [NSDimension.converter](https://developer.apple.com/documentation/foundation/dimension/1823516-converter)Added [-[NSDimension initWithSymbol:converter:]](https://developer.apple.com/documentation/foundation/nsdimension/1823633-initwithsymbol)Added [NSUnit](https://developer.apple.com/documentation/foundation/nsunit)Added [-[NSUnit initWithSymbol:]](https://developer.apple.com/documentation/foundation/nsunit/1690760-initwithsymbol)Added [NSUnit.symbol](https://developer.apple.com/documentation/foundation/nsunit/1642700-symbol)Added [NSUnitAcceleration](https://developer.apple.com/documentation/foundation/unitacceleration)Added [+[NSUnitAcceleration gravity]](https://developer.apple.com/documentation/foundation/unitacceleration/1690681-gravity)Added [NSUnitAcceleration.gravity](https://developer.apple.com/documentation/foundation/nsunitacceleration/1690681-gravity)Added [+[NSUnitAcceleration metersPerSecondSquared]](https://developer.apple.com/documentation/foundation/nsunitacceleration/1856015-meterspersecondsquared)Added [NSUnitAcceleration.metersPerSecondSquared](https://developer.apple.com/documentation/foundation/unitacceleration/1856015-meterspersecondsquared)Added [NSUnitAngle](https://developer.apple.com/documentation/foundation/unitangle)Added [+[NSUnitAngle arcMinutes]](https://developer.apple.com/documentation/foundation/nsunitangle/1856069-arcminutes)Added [NSUnitAngle.arcMinutes](https://developer.apple.com/documentation/foundation/nsunitangle/1856069-arcminutes)Added [+[NSUnitAngle arcSeconds]](https://developer.apple.com/documentation/foundation/unitangle/1856114-arcseconds)Added [NSUnitAngle.arcSeconds](https://developer.apple.com/documentation/foundation/nsunitangle/1856114-arcseconds)Added [+[NSUnitAngle degrees]](https://developer.apple.com/documentation/foundation/nsunitangle/1856083-degrees)Added [NSUnitAngle.degrees](https://developer.apple.com/documentation/foundation/nsunitangle/1856083-degrees)Added [+[NSUnitAngle gradians]](https://developer.apple.com/documentation/foundation/nsunitangle/1855988-gradians)Added [NSUnitAngle.gradians](https://developer.apple.com/documentation/foundation/nsunitangle/1855988-gradians)Added [+[NSUnitAngle radians]](https://developer.apple.com/documentation/foundation/unitangle/1856062-radians)Added [NSUnitAngle.radians](https://developer.apple.com/documentation/foundation/nsunitangle/1856062-radians)Added [+[NSUnitAngle revolutions]](https://developer.apple.com/documentation/foundation/nsunitangle/1855992-revolutions)Added [NSUnitAngle.revolutions](https://developer.apple.com/documentation/foundation/nsunitangle/1855992-revolutions)Added [NSUnitArea](https://developer.apple.com/documentation/foundation/unitarea)Added [+[NSUnitArea acres]](https://developer.apple.com/documentation/foundation/unitarea/1856099-acres)Added [NSUnitArea.acres](https://developer.apple.com/documentation/foundation/nsunitarea/1856099-acres)Added [+[NSUnitArea ares]](https://developer.apple.com/documentation/foundation/unitarea/1856064-ares)Added [NSUnitArea.ares](https://developer.apple.com/documentation/foundation/unitarea/1856064-ares)Added [+[NSUnitArea hectares]](https://developer.apple.com/documentation/foundation/unitarea/1856066-hectares)Added [NSUnitArea.hectares](https://developer.apple.com/documentation/foundation/nsunitarea/1856066-hectares)Added [+[NSUnitArea squareCentimeters]](https://developer.apple.com/documentation/foundation/nsunitarea/1856030-squarecentimeters)Added [NSUnitArea.squareCentimeters](https://developer.apple.com/documentation/foundation/nsunitarea/1856030-squarecentimeters)Added [+[NSUnitArea squareFeet]](https://developer.apple.com/documentation/foundation/nsunitarea/1856014-squarefeet)Added [NSUnitArea.squareFeet](https://developer.apple.com/documentation/foundation/unitarea/1856014-squarefeet)Added [+[NSUnitArea squareInches]](https://developer.apple.com/documentation/foundation/unitarea/1856067-squareinches)Added [NSUnitArea.squareInches](https://developer.apple.com/documentation/foundation/nsunitarea/1856067-squareinches)Added [+[NSUnitArea squareKilometers]](https://developer.apple.com/documentation/foundation/nsunitarea/1856053-squarekilometers)Added [NSUnitArea.squareKilometers](https://developer.apple.com/documentation/foundation/nsunitarea/1856053-squarekilometers)Added [+[NSUnitArea squareMegameters]](https://developer.apple.com/documentation/foundation/nsunitarea/1856008-squaremegameters)Added [NSUnitArea.squareMegameters](https://developer.apple.com/documentation/foundation/nsunitarea/1856008-squaremegameters)Added [+[NSUnitArea squareMeters]](https://developer.apple.com/documentation/foundation/nsunitarea/1855985-squaremeters)Added [NSUnitArea.squareMeters](https://developer.apple.com/documentation/foundation/nsunitarea/1855985-squaremeters)Added [+[NSUnitArea squareMicrometers]](https://developer.apple.com/documentation/foundation/nsunitarea/1856041-squaremicrometers)Added [NSUnitArea.squareMicrometers](https://developer.apple.com/documentation/foundation/nsunitarea/1856041-squaremicrometers)Added [+[NSUnitArea squareMiles]](https://developer.apple.com/documentation/foundation/unitarea/1856097-squaremiles)Added [NSUnitArea.squareMiles](https://developer.apple.com/documentation/foundation/unitarea/1856097-squaremiles)Added [+[NSUnitArea squareMillimeters]](https://developer.apple.com/documentation/foundation/unitarea/1856039-squaremillimeters)Added [NSUnitArea.squareMillimeters](https://developer.apple.com/documentation/foundation/nsunitarea/1856039-squaremillimeters)Added [+[NSUnitArea squareNanometers]](https://developer.apple.com/documentation/foundation/unitarea/1856072-squarenanometers)Added [NSUnitArea.squareNanometers](https://developer.apple.com/documentation/foundation/unitarea/1856072-squarenanometers)Added [+[NSUnitArea squareYards]](https://developer.apple.com/documentation/foundation/nsunitarea/1856070-squareyards)Added [NSUnitArea.squareYards](https://developer.apple.com/documentation/foundation/nsunitarea/1856070-squareyards)Added [NSUnitConcentrationMass](https://developer.apple.com/documentation/foundation/nsunitconcentrationmass)Added [+[NSUnitConcentrationMass gramsPerLiter]](https://developer.apple.com/documentation/foundation/unitconcentrationmass/1856019-gramsperliter)Added [NSUnitConcentrationMass.gramsPerLiter](https://developer.apple.com/documentation/foundation/nsunitconcentrationmass/1856019-gramsperliter)Added [+[NSUnitConcentrationMass milligramsPerDeciliter]](https://developer.apple.com/documentation/foundation/nsunitconcentrationmass/1856024-milligramsperdeciliter)Added [NSUnitConcentrationMass.milligramsPerDeciliter](https://developer.apple.com/documentation/foundation/nsunitconcentrationmass/1856024-milligramsperdeciliter)Added [+[NSUnitConcentrationMass millimolesPerLiterWithGramsPerMole:]](https://developer.apple.com/documentation/foundation/nsunitconcentrationmass/1855799-millimolesperliterwithgramspermo)Added [NSUnitConverter](https://developer.apple.com/documentation/foundation/nsunitconverter)Added [-[NSUnitConverter baseUnitValueFromValue:]](https://developer.apple.com/documentation/foundation/nsunitconverter/1823668-baseunitvaluefromvalue)Added [-[NSUnitConverter valueFromBaseUnitValue:]](https://developer.apple.com/documentation/foundation/unitconverter/1823657-value)Added [NSUnitConverterLinear](https://developer.apple.com/documentation/foundation/nsunitconverterlinear)Added [NSUnitConverterLinear.coefficient](https://developer.apple.com/documentation/foundation/nsunitconverterlinear/1823683-coefficient)Added [NSUnitConverterLinear.constant](https://developer.apple.com/documentation/foundation/unitconverterlinear/1823598-constant)Added [-[NSUnitConverterLinear initWithCoefficient:]](https://developer.apple.com/documentation/foundation/nsunitconverterlinear/1823611-initwithcoefficient)Added [-[NSUnitConverterLinear initWithCoefficient:constant:]](https://developer.apple.com/documentation/foundation/nsunitconverterlinear/1823577-initwithcoefficient)Added [NSUnitDispersion](https://developer.apple.com/documentation/foundation/nsunitdispersion)Added [+[NSUnitDispersion partsPerMillion]](https://developer.apple.com/documentation/foundation/unitdispersion/1690700-partspermillion)Added [NSUnitDispersion.partsPerMillion](https://developer.apple.com/documentation/foundation/unitdispersion/1690700-partspermillion)Added [NSUnitDuration](https://developer.apple.com/documentation/foundation/unitduration)Added [+[NSUnitDuration hours]](https://developer.apple.com/documentation/foundation/nsunitduration/1855994-hours)Added [NSUnitDuration.hours](https://developer.apple.com/documentation/foundation/nsunitduration/1855994-hours)Added [+[NSUnitDuration minutes]](https://developer.apple.com/documentation/foundation/nsunitduration/1856088-minutes)Added [NSUnitDuration.minutes](https://developer.apple.com/documentation/foundation/nsunitduration/1856088-minutes)Added [+[NSUnitDuration seconds]](https://developer.apple.com/documentation/foundation/nsunitduration/1856005-seconds)Added [NSUnitDuration.seconds](https://developer.apple.com/documentation/foundation/nsunitduration/1856005-seconds)Added [NSUnitElectricCharge](https://developer.apple.com/documentation/foundation/unitelectriccharge)Added [+[NSUnitElectricCharge ampereHours]](https://developer.apple.com/documentation/foundation/nsunitelectriccharge/1856117-amperehours)Added [NSUnitElectricCharge.ampereHours](https://developer.apple.com/documentation/foundation/unitelectriccharge/1856117-amperehours)Added [+[NSUnitElectricCharge coulombs]](https://developer.apple.com/documentation/foundation/nsunitelectriccharge/1856032-coulombs)Added [NSUnitElectricCharge.coulombs](https://developer.apple.com/documentation/foundation/unitelectriccharge/1856032-coulombs)Added [+[NSUnitElectricCharge kiloampereHours]](https://developer.apple.com/documentation/foundation/unitelectriccharge/1856045-kiloamperehours)Added [NSUnitElectricCharge.kiloampereHours](https://developer.apple.com/documentation/foundation/nsunitelectriccharge/1856045-kiloamperehours)Added [+[NSUnitElectricCharge megaampereHours]](https://developer.apple.com/documentation/foundation/unitelectriccharge/1856020-megaamperehours)Added [NSUnitElectricCharge.megaampereHours](https://developer.apple.com/documentation/foundation/nsunitelectriccharge/1856020-megaamperehours)Added [+[NSUnitElectricCharge microampereHours]](https://developer.apple.com/documentation/foundation/unitelectriccharge/1856006-microamperehours)Added [NSUnitElectricCharge.microampereHours](https://developer.apple.com/documentation/foundation/unitelectriccharge/1856006-microamperehours)Added [+[NSUnitElectricCharge milliampereHours]](https://developer.apple.com/documentation/foundation/nsunitelectriccharge/1856102-milliamperehours)Added [NSUnitElectricCharge.milliampereHours](https://developer.apple.com/documentation/foundation/unitelectriccharge/1856102-milliamperehours)Added [NSUnitElectricCurrent](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent)Added [+[NSUnitElectricCurrent amperes]](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1855973-amperes)Added [NSUnitElectricCurrent.amperes](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1855973-amperes)Added [+[NSUnitElectricCurrent kiloamperes]](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1856001-kiloamperes)Added [NSUnitElectricCurrent.kiloamperes](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1856001-kiloamperes)Added [+[NSUnitElectricCurrent megaamperes]](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1855980-megaamperes)Added [NSUnitElectricCurrent.megaamperes](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1855980-megaamperes)Added [+[NSUnitElectricCurrent microamperes]](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1856047-microamperes)Added [NSUnitElectricCurrent.microamperes](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1856047-microamperes)Added [+[NSUnitElectricCurrent milliamperes]](https://developer.apple.com/documentation/foundation/unitelectriccurrent/1856058-milliamperes)Added [NSUnitElectricCurrent.milliamperes](https://developer.apple.com/documentation/foundation/nsunitelectriccurrent/1856058-milliamperes)Added [NSUnitElectricPotentialDifference](https://developer.apple.com/documentation/foundation/nsunitelectricpotentialdifference)Added [+[NSUnitElectricPotentialDifference kilovolts]](https://developer.apple.com/documentation/foundation/nsunitelectricpotentialdifference/1856086-kilovolts)Added [NSUnitElectricPotentialDifference.kilovolts](https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference/1856086-kilovolts)Added [+[NSUnitElectricPotentialDifference megavolts]](https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference/1855975-megavolts)Added [NSUnitElectricPotentialDifference.megavolts](https://developer.apple.com/documentation/foundation/nsunitelectricpotentialdifference/1855975-megavolts)Added [+[NSUnitElectricPotentialDifference microvolts]](https://developer.apple.com/documentation/foundation/nsunitelectricpotentialdifference/1856022-microvolts)Added [NSUnitElectricPotentialDifference.microvolts](https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference/1856022-microvolts)Added [+[NSUnitElectricPotentialDifference millivolts]](https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference/1856094-millivolts)Added [NSUnitElectricPotentialDifference.millivolts](https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference/1856094-millivolts)Added [+[NSUnitElectricPotentialDifference volts]](https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference/1856095-volts)Added [NSUnitElectricPotentialDifference.volts](https://developer.apple.com/documentation/foundation/nsunitelectricpotentialdifference/1856095-volts)Added [NSUnitElectricResistance](https://developer.apple.com/documentation/foundation/nsunitelectricresistance)Added [+[NSUnitElectricResistance kiloohms]](https://developer.apple.com/documentation/foundation/unitelectricresistance/1855981-kiloohms)Added [NSUnitElectricResistance.kiloohms](https://developer.apple.com/documentation/foundation/nsunitelectricresistance/1855981-kiloohms)Added [+[NSUnitElectricResistance megaohms]](https://developer.apple.com/documentation/foundation/nsunitelectricresistance/1856009-megaohms)Added [NSUnitElectricResistance.megaohms](https://developer.apple.com/documentation/foundation/nsunitelectricresistance/1856009-megaohms)Added [+[NSUnitElectricResistance microohms]](https://developer.apple.com/documentation/foundation/nsunitelectricresistance/1856031-microohms)Added [NSUnitElectricResistance.microohms](https://developer.apple.com/documentation/foundation/unitelectricresistance/1856031-microohms)Added [+[NSUnitElectricResistance milliohms]](https://developer.apple.com/documentation/foundation/unitelectricresistance/1856049-milliohms)Added [NSUnitElectricResistance.milliohms](https://developer.apple.com/documentation/foundation/nsunitelectricresistance/1856049-milliohms)Added [+[NSUnitElectricResistance ohms]](https://developer.apple.com/documentation/foundation/nsunitelectricresistance/1856110-ohms)Added [NSUnitElectricResistance.ohms](https://developer.apple.com/documentation/foundation/nsunitelectricresistance/1856110-ohms)Added [NSUnitEnergy](https://developer.apple.com/documentation/foundation/unitenergy)Added [+[NSUnitEnergy calories]](https://developer.apple.com/documentation/foundation/unitenergy/1855990-calories)Added [NSUnitEnergy.calories](https://developer.apple.com/documentation/foundation/nsunitenergy/1855990-calories)Added [+[NSUnitEnergy joules]](https://developer.apple.com/documentation/foundation/nsunitenergy/1855987-joules)Added [NSUnitEnergy.joules](https://developer.apple.com/documentation/foundation/unitenergy/1855987-joules)Added [+[NSUnitEnergy kilocalories]](https://developer.apple.com/documentation/foundation/nsunitenergy/1856028-kilocalories)Added [NSUnitEnergy.kilocalories](https://developer.apple.com/documentation/foundation/unitenergy/1856028-kilocalories)Added [+[NSUnitEnergy kilojoules]](https://developer.apple.com/documentation/foundation/nsunitenergy/1856113-kilojoules)Added [NSUnitEnergy.kilojoules](https://developer.apple.com/documentation/foundation/unitenergy/1856113-kilojoules)Added [+[NSUnitEnergy kilowattHours]](https://developer.apple.com/documentation/foundation/nsunitenergy/1856092-kilowatthours)Added [NSUnitEnergy.kilowattHours](https://developer.apple.com/documentation/foundation/nsunitenergy/1856092-kilowatthours)Added [NSUnitFrequency](https://developer.apple.com/documentation/foundation/unitfrequency)Added [+[NSUnitFrequency gigahertz]](https://developer.apple.com/documentation/foundation/unitfrequency/1690667-gigahertz)Added [NSUnitFrequency.gigahertz](https://developer.apple.com/documentation/foundation/unitfrequency/1690667-gigahertz)Added [+[NSUnitFrequency hertz]](https://developer.apple.com/documentation/foundation/unitfrequency/1690670-hertz)Added [NSUnitFrequency.hertz](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690670-hertz)Added [+[NSUnitFrequency kilohertz]](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690767-kilohertz)Added [NSUnitFrequency.kilohertz](https://developer.apple.com/documentation/foundation/unitfrequency/1690767-kilohertz)Added [+[NSUnitFrequency megahertz]](https://developer.apple.com/documentation/foundation/unitfrequency/1690707-megahertz)Added [NSUnitFrequency.megahertz](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690707-megahertz)Added [+[NSUnitFrequency microhertz]](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690838-microhertz)Added [NSUnitFrequency.microhertz](https://developer.apple.com/documentation/foundation/unitfrequency/1690838-microhertz)Added [+[NSUnitFrequency millihertz]](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690882-millihertz)Added [NSUnitFrequency.millihertz](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690882-millihertz)Added [+[NSUnitFrequency nanohertz]](https://developer.apple.com/documentation/foundation/unitfrequency/1690663-nanohertz)Added [NSUnitFrequency.nanohertz](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690663-nanohertz)Added [+[NSUnitFrequency terahertz]](https://developer.apple.com/documentation/foundation/unitfrequency/1690717-terahertz)Added [NSUnitFrequency.terahertz](https://developer.apple.com/documentation/foundation/nsunitfrequency/1690717-terahertz)Added [NSUnitFuelEfficiency](https://developer.apple.com/documentation/foundation/nsunitfuelefficiency)Added [+[NSUnitFuelEfficiency litersPer100Kilometers]](https://developer.apple.com/documentation/foundation/nsunitfuelefficiency/1856054-litersper100kilometers)Added [NSUnitFuelEfficiency.litersPer100Kilometers](https://developer.apple.com/documentation/foundation/unitfuelefficiency/1856054-litersper100kilometers)Added [+[NSUnitFuelEfficiency milesPerGallon]](https://developer.apple.com/documentation/foundation/nsunitfuelefficiency/1856085-milespergallon)Added [NSUnitFuelEfficiency.milesPerGallon](https://developer.apple.com/documentation/foundation/nsunitfuelefficiency/1856085-milespergallon)Added [+[NSUnitFuelEfficiency milesPerImperialGallon]](https://developer.apple.com/documentation/foundation/unitfuelefficiency/1856089-milesperimperialgallon)Added [NSUnitFuelEfficiency.milesPerImperialGallon](https://developer.apple.com/documentation/foundation/nsunitfuelefficiency/1856089-milesperimperialgallon)Added [NSUnitIlluminance](https://developer.apple.com/documentation/foundation/nsunitilluminance)Added [+[NSUnitIlluminance lux]](https://developer.apple.com/documentation/foundation/nsunitilluminance/1823716-lux)Added [NSUnitIlluminance.lux](https://developer.apple.com/documentation/foundation/unitilluminance/1823716-lux)Added [NSUnitLength](https://developer.apple.com/documentation/foundation/unitlength)Added [+[NSUnitLength astronomicalUnits]](https://developer.apple.com/documentation/foundation/unitlength/1856087-astronomicalunits)Added [NSUnitLength.astronomicalUnits](https://developer.apple.com/documentation/foundation/nsunitlength/1856087-astronomicalunits)Added [+[NSUnitLength centimeters]](https://developer.apple.com/documentation/foundation/nsunitlength/1856082-centimeters)Added [NSUnitLength.centimeters](https://developer.apple.com/documentation/foundation/nsunitlength/1856082-centimeters)Added [+[NSUnitLength decameters]](https://developer.apple.com/documentation/foundation/nsunitlength/1856042-decameters)Added [NSUnitLength.decameters](https://developer.apple.com/documentation/foundation/unitlength/1856042-decameters)Added [+[NSUnitLength decimeters]](https://developer.apple.com/documentation/foundation/nsunitlength/1856007-decimeters)Added [NSUnitLength.decimeters](https://developer.apple.com/documentation/foundation/nsunitlength/1856007-decimeters)Added [+[NSUnitLength fathoms]](https://developer.apple.com/documentation/foundation/unitlength/1856090-fathoms)Added [NSUnitLength.fathoms](https://developer.apple.com/documentation/foundation/unitlength/1856090-fathoms)Added [+[NSUnitLength feet]](https://developer.apple.com/documentation/foundation/nsunitlength/1855972-feet)Added [NSUnitLength.feet](https://developer.apple.com/documentation/foundation/nsunitlength/1855972-feet)Added [+[NSUnitLength furlongs]](https://developer.apple.com/documentation/foundation/nsunitlength/1856065-furlongs)Added [NSUnitLength.furlongs](https://developer.apple.com/documentation/foundation/nsunitlength/1856065-furlongs)Added [+[NSUnitLength hectometers]](https://developer.apple.com/documentation/foundation/nsunitlength/1855970-hectometers)Added [NSUnitLength.hectometers](https://developer.apple.com/documentation/foundation/nsunitlength/1855970-hectometers)Added [+[NSUnitLength inches]](https://developer.apple.com/documentation/foundation/unitlength/1856018-inches)Added [NSUnitLength.inches](https://developer.apple.com/documentation/foundation/unitlength/1856018-inches)Added [+[NSUnitLength kilometers]](https://developer.apple.com/documentation/foundation/nsunitlength/1856106-kilometers)Added [NSUnitLength.kilometers](https://developer.apple.com/documentation/foundation/unitlength/1856106-kilometers)Added [+[NSUnitLength lightyears]](https://developer.apple.com/documentation/foundation/unitlength/1855974-lightyears)Added [NSUnitLength.lightyears](https://developer.apple.com/documentation/foundation/nsunitlength/1855974-lightyears)Added [+[NSUnitLength megameters]](https://developer.apple.com/documentation/foundation/nsunitlength/1856036-megameters)Added [NSUnitLength.megameters](https://developer.apple.com/documentation/foundation/unitlength/1856036-megameters)Added [+[NSUnitLength meters]](https://developer.apple.com/documentation/foundation/nsunitlength/1855995-meters)Added [NSUnitLength.meters](https://developer.apple.com/documentation/foundation/nsunitlength/1855995-meters)Added [+[NSUnitLength micrometers]](https://developer.apple.com/documentation/foundation/unitlength/1855998-micrometers)Added [NSUnitLength.micrometers](https://developer.apple.com/documentation/foundation/unitlength/1855998-micrometers)Added [+[NSUnitLength miles]](https://developer.apple.com/documentation/foundation/nsunitlength/1856016-miles)Added [NSUnitLength.miles](https://developer.apple.com/documentation/foundation/nsunitlength/1856016-miles)Added [+[NSUnitLength millimeters]](https://developer.apple.com/documentation/foundation/unitlength/1856046-millimeters)Added [NSUnitLength.millimeters](https://developer.apple.com/documentation/foundation/unitlength/1856046-millimeters)Added [+[NSUnitLength nanometers]](https://developer.apple.com/documentation/foundation/nsunitlength/1856004-nanometers)Added [NSUnitLength.nanometers](https://developer.apple.com/documentation/foundation/unitlength/1856004-nanometers)Added [+[NSUnitLength nauticalMiles]](https://developer.apple.com/documentation/foundation/nsunitlength/1855986-nauticalmiles)Added [NSUnitLength.nauticalMiles](https://developer.apple.com/documentation/foundation/unitlength/1855986-nauticalmiles)Added [+[NSUnitLength parsecs]](https://developer.apple.com/documentation/foundation/nsunitlength/1856021-parsecs)Added [NSUnitLength.parsecs](https://developer.apple.com/documentation/foundation/unitlength/1856021-parsecs)Added [+[NSUnitLength picometers]](https://developer.apple.com/documentation/foundation/unitlength/1856012-picometers)Added [NSUnitLength.picometers](https://developer.apple.com/documentation/foundation/nsunitlength/1856012-picometers)Added [+[NSUnitLength scandinavianMiles]](https://developer.apple.com/documentation/foundation/unitlength/1856061-scandinavianmiles)Added [NSUnitLength.scandinavianMiles](https://developer.apple.com/documentation/foundation/unitlength/1856061-scandinavianmiles)Added [+[NSUnitLength yards]](https://developer.apple.com/documentation/foundation/nsunitlength/1855993-yards)Added [NSUnitLength.yards](https://developer.apple.com/documentation/foundation/nsunitlength/1855993-yards)Added [NSUnitMass](https://developer.apple.com/documentation/foundation/nsunitmass)Added [+[NSUnitMass carats]](https://developer.apple.com/documentation/foundation/unitmass/1856037-carats)Added [NSUnitMass.carats](https://developer.apple.com/documentation/foundation/unitmass/1856037-carats)Added [+[NSUnitMass centigrams]](https://developer.apple.com/documentation/foundation/nsunitmass/1856116-centigrams)Added [NSUnitMass.centigrams](https://developer.apple.com/documentation/foundation/unitmass/1856116-centigrams)Added [+[NSUnitMass decigrams]](https://developer.apple.com/documentation/foundation/nsunitmass/1856063-decigrams)Added [NSUnitMass.decigrams](https://developer.apple.com/documentation/foundation/unitmass/1856063-decigrams)Added [+[NSUnitMass grams]](https://developer.apple.com/documentation/foundation/unitmass/1855976-grams)Added [NSUnitMass.grams](https://developer.apple.com/documentation/foundation/unitmass/1855976-grams)Added [+[NSUnitMass kilograms]](https://developer.apple.com/documentation/foundation/nsunitmass/1855996-kilograms)Added [NSUnitMass.kilograms](https://developer.apple.com/documentation/foundation/unitmass/1855996-kilograms)Added [+[NSUnitMass metricTons]](https://developer.apple.com/documentation/foundation/nsunitmass/1856076-metrictons)Added [NSUnitMass.metricTons](https://developer.apple.com/documentation/foundation/nsunitmass/1856076-metrictons)Added [+[NSUnitMass micrograms]](https://developer.apple.com/documentation/foundation/nsunitmass/1856010-micrograms)Added [NSUnitMass.micrograms](https://developer.apple.com/documentation/foundation/nsunitmass/1856010-micrograms)Added [+[NSUnitMass milligrams]](https://developer.apple.com/documentation/foundation/nsunitmass/1856060-milligrams)Added [NSUnitMass.milligrams](https://developer.apple.com/documentation/foundation/unitmass/1856060-milligrams)Added [+[NSUnitMass nanograms]](https://developer.apple.com/documentation/foundation/unitmass/1856078-nanograms)Added [NSUnitMass.nanograms](https://developer.apple.com/documentation/foundation/nsunitmass/1856078-nanograms)Added [+[NSUnitMass ounces]](https://developer.apple.com/documentation/foundation/unitmass/1856056-ounces)Added [NSUnitMass.ounces](https://developer.apple.com/documentation/foundation/unitmass/1856056-ounces)Added [+[NSUnitMass ouncesTroy]](https://developer.apple.com/documentation/foundation/unitmass/1856003-ouncestroy)Added [NSUnitMass.ouncesTroy](https://developer.apple.com/documentation/foundation/unitmass/1856003-ouncestroy)Added [+[NSUnitMass picograms]](https://developer.apple.com/documentation/foundation/unitmass/1856035-picograms)Added [NSUnitMass.picograms](https://developer.apple.com/documentation/foundation/unitmass/1856035-picograms)Added [+[NSUnitMass poundsMass]](https://developer.apple.com/documentation/foundation/nsunitmass/1856023-poundsmass)Added [NSUnitMass.poundsMass](https://developer.apple.com/documentation/foundation/unitmass/1856023-pounds)Added [+[NSUnitMass shortTons]](https://developer.apple.com/documentation/foundation/nsunitmass/1856081-shorttons)Added [NSUnitMass.shortTons](https://developer.apple.com/documentation/foundation/unitmass/1856081-shorttons)Added [+[NSUnitMass slugs]](https://developer.apple.com/documentation/foundation/unitmass/1856027-slugs)Added [NSUnitMass.slugs](https://developer.apple.com/documentation/foundation/nsunitmass/1856027-slugs)Added [+[NSUnitMass stones]](https://developer.apple.com/documentation/foundation/unitmass/1856033-stones)Added [NSUnitMass.stones](https://developer.apple.com/documentation/foundation/nsunitmass/1856033-stones)Added [NSUnitPower](https://developer.apple.com/documentation/foundation/unitpower)Added [+[NSUnitPower femtowatts]](https://developer.apple.com/documentation/foundation/nsunitpower/1856043-femtowatts)Added [NSUnitPower.femtowatts](https://developer.apple.com/documentation/foundation/unitpower/1856043-femtowatts)Added [+[NSUnitPower gigawatts]](https://developer.apple.com/documentation/foundation/unitpower/1856108-gigawatts)Added [NSUnitPower.gigawatts](https://developer.apple.com/documentation/foundation/nsunitpower/1856108-gigawatts)Added [+[NSUnitPower horsepower]](https://developer.apple.com/documentation/foundation/unitpower/1690871-horsepower)Added [NSUnitPower.horsepower](https://developer.apple.com/documentation/foundation/unitpower/1690871-horsepower)Added [+[NSUnitPower kilowatts]](https://developer.apple.com/documentation/foundation/nsunitpower/1856084-kilowatts)Added [NSUnitPower.kilowatts](https://developer.apple.com/documentation/foundation/nsunitpower/1856084-kilowatts)Added [+[NSUnitPower megawatts]](https://developer.apple.com/documentation/foundation/nsunitpower/1856073-megawatts)Added [NSUnitPower.megawatts](https://developer.apple.com/documentation/foundation/nsunitpower/1856073-megawatts)Added [+[NSUnitPower microwatts]](https://developer.apple.com/documentation/foundation/unitpower/1856051-microwatts)Added [NSUnitPower.microwatts](https://developer.apple.com/documentation/foundation/unitpower/1856051-microwatts)Added [+[NSUnitPower milliwatts]](https://developer.apple.com/documentation/foundation/nsunitpower/1855984-milliwatts)Added [NSUnitPower.milliwatts](https://developer.apple.com/documentation/foundation/nsunitpower/1855984-milliwatts)Added [+[NSUnitPower nanowatts]](https://developer.apple.com/documentation/foundation/unitpower/1855999-nanowatts)Added [NSUnitPower.nanowatts](https://developer.apple.com/documentation/foundation/nsunitpower/1855999-nanowatts)Added [+[NSUnitPower picowatts]](https://developer.apple.com/documentation/foundation/unitpower/1856104-picowatts)Added [NSUnitPower.picowatts](https://developer.apple.com/documentation/foundation/unitpower/1856104-picowatts)Added [+[NSUnitPower terawatts]](https://developer.apple.com/documentation/foundation/nsunitpower/1856100-terawatts)Added [NSUnitPower.terawatts](https://developer.apple.com/documentation/foundation/unitpower/1856100-terawatts)Added [+[NSUnitPower watts]](https://developer.apple.com/documentation/foundation/unitpower/1856075-watts)Added [NSUnitPower.watts](https://developer.apple.com/documentation/foundation/nsunitpower/1856075-watts)Added [NSUnitPressure](https://developer.apple.com/documentation/foundation/nsunitpressure)Added [+[NSUnitPressure bars]](https://developer.apple.com/documentation/foundation/nsunitpressure/1856109-bars)Added [NSUnitPressure.bars](https://developer.apple.com/documentation/foundation/nsunitpressure/1856109-bars)Added [+[NSUnitPressure gigapascals]](https://developer.apple.com/documentation/foundation/nsunitpressure/1855983-gigapascals)Added [NSUnitPressure.gigapascals](https://developer.apple.com/documentation/foundation/unitpressure/1855983-gigapascals)Added [+[NSUnitPressure hectopascals]](https://developer.apple.com/documentation/foundation/unitpressure/1856111-hectopascals)Added [NSUnitPressure.hectopascals](https://developer.apple.com/documentation/foundation/unitpressure/1856111-hectopascals)Added [+[NSUnitPressure inchesOfMercury]](https://developer.apple.com/documentation/foundation/nsunitpressure/1856074-inchesofmercury)Added [NSUnitPressure.inchesOfMercury](https://developer.apple.com/documentation/foundation/unitpressure/1856074-inchesofmercury)Added [+[NSUnitPressure kilopascals]](https://developer.apple.com/documentation/foundation/unitpressure/1856057-kilopascals)Added [NSUnitPressure.kilopascals](https://developer.apple.com/documentation/foundation/unitpressure/1856057-kilopascals)Added [+[NSUnitPressure megapascals]](https://developer.apple.com/documentation/foundation/nsunitpressure/1856115-megapascals)Added [NSUnitPressure.megapascals](https://developer.apple.com/documentation/foundation/nsunitpressure/1856115-megapascals)Added [+[NSUnitPressure millibars]](https://developer.apple.com/documentation/foundation/nsunitpressure/1856093-millibars)Added [NSUnitPressure.millibars](https://developer.apple.com/documentation/foundation/unitpressure/1856093-millibars)Added [+[NSUnitPressure millimetersOfMercury]](https://developer.apple.com/documentation/foundation/unitpressure/1856052-millimetersofmercury)Added [NSUnitPressure.millimetersOfMercury](https://developer.apple.com/documentation/foundation/unitpressure/1856052-millimetersofmercury)Added [+[NSUnitPressure newtonsPerMetersSquared]](https://developer.apple.com/documentation/foundation/unitpressure/1856096-newtonspermeterssquared)Added [NSUnitPressure.newtonsPerMetersSquared](https://developer.apple.com/documentation/foundation/unitpressure/1856096-newtonspermeterssquared)Added [+[NSUnitPressure poundsForcePerSquareInch]](https://developer.apple.com/documentation/foundation/nsunitpressure/1856077-poundsforcepersquareinch)Added [NSUnitPressure.poundsForcePerSquareInch](https://developer.apple.com/documentation/foundation/nsunitpressure/1856077-poundsforcepersquareinch)Added [NSUnitSpeed](https://developer.apple.com/documentation/foundation/nsunitspeed)Added [+[NSUnitSpeed kilometersPerHour]](https://developer.apple.com/documentation/foundation/nsunitspeed/1856044-kilometersperhour)Added [NSUnitSpeed.kilometersPerHour](https://developer.apple.com/documentation/foundation/nsunitspeed/1856044-kilometersperhour)Added [+[NSUnitSpeed knots]](https://developer.apple.com/documentation/foundation/nsunitspeed/1856050-knots)Added [NSUnitSpeed.knots](https://developer.apple.com/documentation/foundation/nsunitspeed/1856050-knots)Added [+[NSUnitSpeed metersPerSecond]](https://developer.apple.com/documentation/foundation/nsunitspeed/1856079-meterspersecond)Added [NSUnitSpeed.metersPerSecond](https://developer.apple.com/documentation/foundation/nsunitspeed/1856079-meterspersecond)Added [+[NSUnitSpeed milesPerHour]](https://developer.apple.com/documentation/foundation/nsunitspeed/1856098-milesperhour)Added [NSUnitSpeed.milesPerHour](https://developer.apple.com/documentation/foundation/nsunitspeed/1856098-milesperhour)Added [NSUnitTemperature](https://developer.apple.com/documentation/foundation/unittemperature)Added [+[NSUnitTemperature celsius]](https://developer.apple.com/documentation/foundation/nsunittemperature/1690835-celsius)Added [NSUnitTemperature.celsius](https://developer.apple.com/documentation/foundation/unittemperature/1690835-celsius)Added [+[NSUnitTemperature fahrenheit]](https://developer.apple.com/documentation/foundation/nsunittemperature/1690842-fahrenheit)Added [NSUnitTemperature.fahrenheit](https://developer.apple.com/documentation/foundation/unittemperature/1690842-fahrenheit)Added [+[NSUnitTemperature kelvin]](https://developer.apple.com/documentation/foundation/unittemperature/1690766-kelvin)Added [NSUnitTemperature.kelvin](https://developer.apple.com/documentation/foundation/nsunittemperature/1690766-kelvin)Added [NSUnitVolume](https://developer.apple.com/documentation/foundation/nsunitvolume)Added [+[NSUnitVolume acreFeet]](https://developer.apple.com/documentation/foundation/nsunitvolume/1855978-acrefeet)Added [NSUnitVolume.acreFeet](https://developer.apple.com/documentation/foundation/nsunitvolume/1855978-acrefeet)Added [+[NSUnitVolume bushels]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856025-bushels)Added [NSUnitVolume.bushels](https://developer.apple.com/documentation/foundation/nsunitvolume/1856025-bushels)Added [+[NSUnitVolume centiliters]](https://developer.apple.com/documentation/foundation/unitvolume/1856040-centiliters)Added [NSUnitVolume.centiliters](https://developer.apple.com/documentation/foundation/unitvolume/1856040-centiliters)Added [+[NSUnitVolume cubicCentimeters]](https://developer.apple.com/documentation/foundation/unitvolume/1856112-cubiccentimeters)Added [NSUnitVolume.cubicCentimeters](https://developer.apple.com/documentation/foundation/nsunitvolume/1856112-cubiccentimeters)Added [+[NSUnitVolume cubicDecimeters]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856048-cubicdecimeters)Added [NSUnitVolume.cubicDecimeters](https://developer.apple.com/documentation/foundation/nsunitvolume/1856048-cubicdecimeters)Added [+[NSUnitVolume cubicFeet]](https://developer.apple.com/documentation/foundation/unitvolume/1856017-cubicfeet)Added [NSUnitVolume.cubicFeet](https://developer.apple.com/documentation/foundation/unitvolume/1856017-cubicfeet)Added [+[NSUnitVolume cubicInches]](https://developer.apple.com/documentation/foundation/unitvolume/1856026-cubicinches)Added [NSUnitVolume.cubicInches](https://developer.apple.com/documentation/foundation/unitvolume/1856026-cubicinches)Added [+[NSUnitVolume cubicKilometers]](https://developer.apple.com/documentation/foundation/unitvolume/1856034-cubickilometers)Added [NSUnitVolume.cubicKilometers](https://developer.apple.com/documentation/foundation/nsunitvolume/1856034-cubickilometers)Added [+[NSUnitVolume cubicMeters]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856029-cubicmeters)Added [NSUnitVolume.cubicMeters](https://developer.apple.com/documentation/foundation/nsunitvolume/1856029-cubicmeters)Added [+[NSUnitVolume cubicMiles]](https://developer.apple.com/documentation/foundation/unitvolume/1856002-cubicmiles)Added [NSUnitVolume.cubicMiles](https://developer.apple.com/documentation/foundation/unitvolume/1856002-cubicmiles)Added [+[NSUnitVolume cubicMillimeters]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856013-cubicmillimeters)Added [NSUnitVolume.cubicMillimeters](https://developer.apple.com/documentation/foundation/unitvolume/1856013-cubicmillimeters)Added [+[NSUnitVolume cubicYards]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856107-cubicyards)Added [NSUnitVolume.cubicYards](https://developer.apple.com/documentation/foundation/unitvolume/1856107-cubicyards)Added [+[NSUnitVolume cups]](https://developer.apple.com/documentation/foundation/unitvolume/1855982-cups)Added [NSUnitVolume.cups](https://developer.apple.com/documentation/foundation/unitvolume/1855982-cups)Added [+[NSUnitVolume deciliters]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856091-deciliters)Added [NSUnitVolume.deciliters](https://developer.apple.com/documentation/foundation/nsunitvolume/1856091-deciliters)Added [+[NSUnitVolume fluidOunces]](https://developer.apple.com/documentation/foundation/unitvolume/1856038-fluidounces)Added [NSUnitVolume.fluidOunces](https://developer.apple.com/documentation/foundation/nsunitvolume/1856038-fluidounces)Added [+[NSUnitVolume gallons]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856105-gallons)Added [NSUnitVolume.gallons](https://developer.apple.com/documentation/foundation/nsunitvolume/1856105-gallons)Added [+[NSUnitVolume imperialFluidOunces]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856101-imperialfluidounces)Added [NSUnitVolume.imperialFluidOunces](https://developer.apple.com/documentation/foundation/unitvolume/1856101-imperialfluidounces)Added [+[NSUnitVolume imperialGallons]](https://developer.apple.com/documentation/foundation/nsunitvolume/1855997-imperialgallons)Added [NSUnitVolume.imperialGallons](https://developer.apple.com/documentation/foundation/unitvolume/1855997-imperialgallons)Added [+[NSUnitVolume imperialPints]](https://developer.apple.com/documentation/foundation/nsunitvolume/1855979-imperialpints)Added [NSUnitVolume.imperialPints](https://developer.apple.com/documentation/foundation/nsunitvolume/1855979-imperialpints)Added [+[NSUnitVolume imperialQuarts]](https://developer.apple.com/documentation/foundation/unitvolume/1855971-imperialquarts)Added [NSUnitVolume.imperialQuarts](https://developer.apple.com/documentation/foundation/unitvolume/1855971-imperialquarts)Added [+[NSUnitVolume imperialTablespoons]](https://developer.apple.com/documentation/foundation/unitvolume/1855989-imperialtablespoons)Added [NSUnitVolume.imperialTablespoons](https://developer.apple.com/documentation/foundation/unitvolume/1855989-imperialtablespoons)Added [+[NSUnitVolume imperialTeaspoons]](https://developer.apple.com/documentation/foundation/unitvolume/1856103-imperialteaspoons)Added [NSUnitVolume.imperialTeaspoons](https://developer.apple.com/documentation/foundation/unitvolume/1856103-imperialteaspoons)Added [+[NSUnitVolume kiloliters]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856068-kiloliters)Added [NSUnitVolume.kiloliters](https://developer.apple.com/documentation/foundation/nsunitvolume/1856068-kiloliters)Added [+[NSUnitVolume liters]](https://developer.apple.com/documentation/foundation/unitvolume/1856011-liters)Added [NSUnitVolume.liters](https://developer.apple.com/documentation/foundation/nsunitvolume/1856011-liters)Added [+[NSUnitVolume megaliters]](https://developer.apple.com/documentation/foundation/unitvolume/1856080-megaliters)Added [NSUnitVolume.megaliters](https://developer.apple.com/documentation/foundation/unitvolume/1856080-megaliters)Added [+[NSUnitVolume metricCups]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856000-metriccups)Added [NSUnitVolume.metricCups](https://developer.apple.com/documentation/foundation/unitvolume/1856000-metriccups)Added [+[NSUnitVolume milliliters]](https://developer.apple.com/documentation/foundation/nsunitvolume/1856071-milliliters)Added [NSUnitVolume.milliliters](https://developer.apple.com/documentation/foundation/nsunitvolume/1856071-milliliters)Added [+[NSUnitVolume pints]](https://developer.apple.com/documentation/foundation/unitvolume/1856059-pints)Added [NSUnitVolume.pints](https://developer.apple.com/documentation/foundation/nsunitvolume/1856059-pints)Added [+[NSUnitVolume quarts]](https://developer.apple.com/documentation/foundation/unitvolume/1856055-quarts)Added [NSUnitVolume.quarts](https://developer.apple.com/documentation/foundation/unitvolume/1856055-quarts)Added [+[NSUnitVolume tablespoons]](https://developer.apple.com/documentation/foundation/nsunitvolume/1855991-tablespoons)Added [NSUnitVolume.tablespoons](https://developer.apple.com/documentation/foundation/unitvolume/1855991-tablespoons)Added [+[NSUnitVolume teaspoons]](https://developer.apple.com/documentation/foundation/unitvolume/1855977-teaspoons)Added [NSUnitVolume.teaspoons](https://developer.apple.com/documentation/foundation/nsunitvolume/1855977-teaspoons)

#### NSURL.h

Added [NSCharacterSet.URLFragmentAllowedCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1412537-urlfragmentallowedcharacterset)Added [NSCharacterSet.URLHostAllowedCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416426-urlhostallowedcharacterset)Added [NSCharacterSet.URLPasswordAllowedCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1417313-urlpasswordallowedcharacterset)Added [NSCharacterSet.URLPathAllowedCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416804-urlpathallowedcharacterset)Added [NSCharacterSet.URLQueryAllowedCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1416698-urlqueryallowed)Added [NSCharacterSet.URLUserAllowedCharacterSet](https://developer.apple.com/documentation/foundation/nscharacterset/1411851-urluserallowedcharacterset)Added [NSURLCanonicalPathKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1642902-canonicalpathkey)Added [NSURLFileProtectionType](https://developer.apple.com/documentation/foundation/nsurlfileprotectiontype)Added [NSURLFileResourceType](https://developer.apple.com/documentation/foundation/urlfileresourcetype)Added [NSURLResourceKey](https://developer.apple.com/documentation/foundation/urlresourcekey)Added [NSURLThumbnailDictionaryItem](https://developer.apple.com/documentation/foundation/nsurlthumbnaildictionaryitem)Added [NSURLUbiquitousItemDownloadingStatus](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadingstatus)Added [NSURLVolumeIsEncryptedKey](https://developer.apple.com/documentation/foundation/nsurlvolumeisencryptedkey)Added [NSURLVolumeIsRootFileSystemKey](https://developer.apple.com/documentation/foundation/nsurlvolumeisrootfilesystemkey)Added [NSURLVolumeSupportsCompressionKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1643318-volumesupportscompressionkey)Added [NSURLVolumeSupportsExclusiveRenamingKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1643180-volumesupportsexclusiverenamingk)Added [NSURLVolumeSupportsFileCloningKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1642798-volumesupportsfilecloningkey)Added [NSURLVolumeSupportsSwapRenamingKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1643040-volumesupportsswaprenamingkey)Modified [-[NSURL bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:]](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)bookmarkDataWithOptions:(NSURLBookmarkCreationOptions)options includingResourceValuesForKeys:(NSArray<NSString *> *)keys relativeToURL:(NSURL *)relativeURL error:(NSError * _Nullable *)error ``` |
| To | ``` - (NSData *)bookmarkDataWithOptions:(NSURLBookmarkCreationOptions)options includingResourceValuesForKeys:(NSArray<NSURLResourceKey> *)keys relativeToURL:(NSURL *)relativeURL error:(NSError * _Nullable *)error ``` |

Modified [-[NSURL getPromisedItemResourceValue:forKey:error:]](https://developer.apple.com/documentation/foundation/nsurl/1414238-getpromiseditemresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getPromisedItemResourceValue:(id  _Nullable *)value forKey:(NSString *)key error:(NSError * _Nullable *)error ``` |
| To | ``` - (BOOL)getPromisedItemResourceValue:(id  _Nullable *)value forKey:(NSURLResourceKey)key error:(NSError * _Nullable *)error ``` |

Modified [-[NSURL getResourceValue:forKey:error:]](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getResourceValue:(out id  _Nullable *)value forKey:(NSString *)key error:(out NSError * _Nullable *)error ``` |
| To | ``` - (BOOL)getResourceValue:(out id  _Nullable *)value forKey:(NSURLResourceKey)key error:(out NSError * _Nullable *)error ``` |

Modified [-[NSURL promisedItemResourceValuesForKeys:error:]](https://developer.apple.com/documentation/foundation/nsurl/1407746-promiseditemresourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary<NSString *,id> *)promisedItemResourceValuesForKeys:(NSArray<NSString *> *)keys error:(NSError * _Nullable *)error ``` |
| To | ``` - (NSDictionary<NSURLResourceKey,id> *)promisedItemResourceValuesForKeys:(NSArray<NSURLResourceKey> *)keys error:(NSError * _Nullable *)error ``` |

Modified [-[NSURL removeCachedResourceValueForKey:]](https://developer.apple.com/documentation/foundation/nsurl/1410758-removecachedresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeCachedResourceValueForKey:(NSString *)key ``` |
| To | ``` - (void)removeCachedResourceValueForKey:(NSURLResourceKey)key ``` |

Modified [-[NSURL resourceValuesForKeys:error:]](https://developer.apple.com/documentation/foundation/nsurl/1417657-resourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary<NSString *,id> *)resourceValuesForKeys:(NSArray<NSString *> *)keys error:(NSError * _Nullable *)error ``` |
| To | ``` - (NSDictionary<NSURLResourceKey,id> *)resourceValuesForKeys:(NSArray<NSURLResourceKey> *)keys error:(NSError * _Nullable *)error ``` |

Modified [+[NSURL resourceValuesForKeys:fromBookmarkData:]](https://developer.apple.com/documentation/foundation/nsurl/1418097-resourcevaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary<NSString *,id> *)resourceValuesForKeys:(NSArray<NSString *> *)keys fromBookmarkData:(NSData *)bookmarkData ``` |
| To | ``` + (NSDictionary<NSURLResourceKey,id> *)resourceValuesForKeys:(NSArray<NSURLResourceKey> *)keys fromBookmarkData:(NSData *)bookmarkData ``` |

Modified [-[NSURL setResourceValue:forKey:error:]](https://developer.apple.com/documentation/foundation/nsurl/1413819-setresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setResourceValue:(id)value forKey:(NSString *)key error:(NSError * _Nullable *)error ``` |
| To | ``` - (BOOL)setResourceValue:(id)value forKey:(NSURLResourceKey)key error:(NSError * _Nullable *)error ``` |

Modified [-[NSURL setResourceValues:error:]](https://developer.apple.com/documentation/foundation/nsurl/1408208-setresourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setResourceValues:(NSDictionary<NSString *,id> *)keyedValues error:(NSError * _Nullable *)error ``` |
| To | ``` - (BOOL)setResourceValues:(NSDictionary<NSURLResourceKey,id> *)keyedValues error:(NSError * _Nullable *)error ``` |

Modified [-[NSURL setTemporaryResourceValue:forKey:]](https://developer.apple.com/documentation/foundation/nsurl/1411094-settemporaryresourcevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTemporaryResourceValue:(id)value forKey:(NSString *)key ``` |
| To | ``` - (void)setTemporaryResourceValue:(id)value forKey:(NSURLResourceKey)key ``` |

#### NSURLCache.h

Added [NSURLCache.sharedURLCache](https://developer.apple.com/documentation/foundation/nsurlcache/1413377-sharedurlcache)Modified +[NSURLCache setSharedURLCache:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setSharedURLCache:(NSURLCache *)cache ``` |
| To | ``` + (void)setSharedURLCache:(NSURLCache *)sharedURLCache ``` |

#### NSURLConnection.h

Modified [-[NSURLConnection scheduleInRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1417485-schedule)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)scheduleInRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

Modified [-[NSURLConnection unscheduleFromRunLoop:forMode:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1409722-unschedule)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unscheduleFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSString *)mode ``` |
| To | ``` - (void)unscheduleFromRunLoop:(NSRunLoop *)aRunLoop forMode:(NSRunLoopMode)mode ``` |

#### NSURLCredentialStorage.h

Added [NSURLCredentialStorage.sharedCredentialStorage](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1412355-shared)

#### NSURLRequest.h

Added [NSURLRequest.supportsSecureCoding](https://developer.apple.com/documentation/foundation/nsurlrequest/1416510-supportssecurecoding)Added [NSURLNetworkServiceTypeCallSignaling](https://developer.apple.com/documentation/foundation/nsurlrequestnetworkservicetype/nsurlnetworkservicetypecallsignaling)

#### NSURLSession.h

Added [NSURLSession.sharedSession](https://developer.apple.com/documentation/foundation/urlsession/1409000-shared)Added [NSURLSessionConfiguration.defaultSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411560-defaultsessionconfiguration)Added [NSURLSessionConfiguration.ephemeralSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1410529-ephemeralsessionconfiguration)Added [-[NSURLSessionTaskDelegate URLSession:task:didFinishCollectingMetrics:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1643148-urlsession)Added [NSURLSessionTaskMetrics](https://developer.apple.com/documentation/foundation/nsurlsessiontaskmetrics)Added [-[NSURLSessionTaskMetrics init]](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/1643240-init)Added [NSURLSessionTaskMetrics.redirectCount](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/1643136-redirectcount)Added [NSURLSessionTaskMetrics.taskInterval](https://developer.apple.com/documentation/foundation/nsurlsessiontaskmetrics/1643169-taskinterval)Added [NSURLSessionTaskMetrics.transactionMetrics](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/1642789-transactionmetrics)Added [NSURLSessionTaskTransactionMetrics](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics)Added [NSURLSessionTaskTransactionMetrics.connectEndDate](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1643239-connectenddate)Added [NSURLSessionTaskTransactionMetrics.connectStartDate](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1642815-connectstartdate)Added [NSURLSessionTaskTransactionMetrics.domainLookupEndDate](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1643173-domainlookupenddate)Added [NSURLSessionTaskTransactionMetrics.domainLookupStartDate](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1642859-domainlookupstartdate)Added [NSURLSessionTaskTransactionMetrics.fetchStartDate](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1643009-fetchstartdate)Added [-[NSURLSessionTaskTransactionMetrics init]](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1642954-init)Added [NSURLSessionTaskTransactionMetrics.networkProtocolName](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1643141-networkprotocolname)Added [NSURLSessionTaskTransactionMetrics.proxyConnection](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1642917-isproxyconnection)Added [NSURLSessionTaskTransactionMetrics.request](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1643144-request)Added [NSURLSessionTaskTransactionMetrics.requestEndDate](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1643056-requestenddate)Added [NSURLSessionTaskTransactionMetrics.requestStartDate](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1642906-requeststartdate)Added [NSURLSessionTaskTransactionMetrics.resourceFetchType](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1642919-resourcefetchtype)Added [NSURLSessionTaskTransactionMetrics.response](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1643172-response)Added [NSURLSessionTaskTransactionMetrics.responseEndDate](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1643300-responseenddate)Added [NSURLSessionTaskTransactionMetrics.responseStartDate](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1642966-responsestartdate)Added [NSURLSessionTaskTransactionMetrics.reusedConnection](https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/1643233-reusedconnection)Added [NSURLSessionTaskTransactionMetrics.secureConnectionEndDate](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1643255-secureconnectionenddate)Added [NSURLSessionTaskTransactionMetrics.secureConnectionStartDate](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/1643219-secureconnectionstartdate)Added [NSURLSessionTaskMetricsResourceFetchType](https://developer.apple.com/documentation/foundation/nsurlsessiontaskmetricsresourcefetchtype)Added [NSURLSessionTaskMetricsResourceFetchTypeLocalCache](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype/localcache)Added [NSURLSessionTaskMetricsResourceFetchTypeNetworkLoad](https://developer.apple.com/documentation/foundation/nsurlsessiontaskmetricsresourcefetchtype/nsurlsessiontaskmetricsresourcefetchtypenetworkload)Added [NSURLSessionTaskMetricsResourceFetchTypeServerPush](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype/serverpush)Added [NSURLSessionTaskMetricsResourceFetchTypeUnknown](https://developer.apple.com/documentation/foundation/nsurlsessiontaskmetricsresourcefetchtype/nsurlsessiontaskmetricsresourcefetchtypeunknown)

#### NSUserActivity.h

Modified [-[NSUserActivity init]](https://developer.apple.com/documentation/foundation/nsuseractivity/1409240-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[NSUserActivity initWithActivityType:]](https://developer.apple.com/documentation/foundation/nsuseractivity/1410714-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSUserDefaults.h

Added [NSUserDefaults.standardUserDefaults](https://developer.apple.com/documentation/foundation/userdefaults/1416603-standard)

#### NSUserNotification.h

Added [NSUserNotificationCenter.defaultUserNotificationCenter](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1416403-defaultusernotificationcenter)

#### NSValueTransformer.h

Added [NSValueTransformerName](https://developer.apple.com/documentation/foundation/nsvaluetransformername)Modified [+[NSValueTransformer setValueTransformer:forName:]](https://developer.apple.com/documentation/foundation/valuetransformer/1402018-setvaluetransformer)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setValueTransformer:(NSValueTransformer *)transformer forName:(NSString *)name ``` |
| To | ``` + (void)setValueTransformer:(NSValueTransformer *)transformer forName:(NSValueTransformerName)name ``` |

Modified [+[NSValueTransformer valueTransformerForName:]](https://developer.apple.com/documentation/foundation/valuetransformer/1402010-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValueTransformer *)valueTransformerForName:(NSString *)name ``` |
| To | ``` + (NSValueTransformer *)valueTransformerForName:(NSValueTransformerName)name ``` |

Modified [+[NSValueTransformer valueTransformerNames]](https://developer.apple.com/documentation/foundation/valuetransformer/1402012-valuetransformernames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray<NSString *> *)valueTransformerNames ``` |
| To | ``` + (NSArray<NSValueTransformerName> *)valueTransformerNames ``` |

#### NSXMLDTDNode.h

Modified [-[NSXMLDTDNode initWithKind:options:]](https://developer.apple.com/documentation/foundation/xmldtdnode/1408553-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind options:(NSUInteger)options ``` |
| To | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind options:(NSXMLNodeOptions)options ``` |

#### NSXMLElement.h

Modified [-[NSXMLElement initWithKind:options:]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388323-initwithkind)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind options:(NSUInteger)options ``` |
| To | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind options:(NSXMLNodeOptions)options ``` |

#### NSXMLNode.h

Modified [-[NSXMLNode initWithKind:options:]](https://developer.apple.com/documentation/foundation/xmlnode/1409747-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind options:(NSUInteger)options ``` |
| To | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind options:(NSXMLNodeOptions)options ``` |

#### NSXMLNodeOptions.h

Added [NSXMLNodeOptions](https://developer.apple.com/documentation/foundation/xmlnode/options)

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
