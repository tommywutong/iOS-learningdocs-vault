---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/Foundation.html
archived_at: '2026-07-15T07:34:45.523550Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Foundation Changes

## Foundation

FoundationErrors.hAdded [NSPropertyListWriteInvalidError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nspropertylistwriteinvaliderror)Added [NSUserActivityConnectionUnavailableError](https://developer.apple.com/documentation/foundation/nsuseractivityconnectionunavailableerror)Added [NSUserActivityErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsuseractivityerrormaximum)Added [NSUserActivityErrorMinimum](https://developer.apple.com/documentation/foundation/nsuseractivityerrorminimum)Added [NSUserActivityHandoffFailedError](https://developer.apple.com/documentation/foundation/nsuseractivityhandofffailederror)Added [NSUserActivityHandoffUserInfoTooLargeError](https://developer.apple.com/documentation/foundation/nsuseractivityhandoffuserinfotoolargeerror)Added [NSUserActivityRemoteApplicationTimedOutError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsuseractivityremoteapplicationtimedouterror)NSAffineTransform.hRemoved [-[NSAffineTransform setTransformStruct:]](https://developer.apple.com/documentation/foundation/nsaffinetransform/1414485-transformstruct)Removed [-[NSAffineTransform transformStruct]](https://developer.apple.com/documentation/foundation/nsaffinetransform/1414485-transformstruct)Added [-[NSAffineTransform init]](https://developer.apple.com/documentation/foundation/nsaffinetransform/1411498-init)Added [NSAffineTransform.transformStruct](https://developer.apple.com/documentation/foundation/nsaffinetransform/1414485-transformstruct)Modified [-[NSAffineTransform initWithTransform:]](https://developer.apple.com/documentation/foundation/nsaffinetransform/1413399-initwithtransform)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTransform:(NSAffineTransform *)transform ``` |
| To | ``` - (instancetype)initWithTransform:(NSAffineTransform *)transform ``` |

NSAppleEventDescriptor.hRemoved [-[NSAppleEventDescriptor aeDesc]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1413715-aedesc)Removed [-[NSAppleEventDescriptor booleanValue]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1412412-booleanvalue)Removed [-[NSAppleEventDescriptor data]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1413486-data)Removed [-[NSAppleEventDescriptor descriptorType]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1408495-descriptortype)Removed [-[NSAppleEventDescriptor enumCodeValue]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1408039-enumcodevalue)Removed [-[NSAppleEventDescriptor eventClass]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1410955-eventclass)Removed [-[NSAppleEventDescriptor eventID]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1413356-eventid)Removed [-[NSAppleEventDescriptor int32Value]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1407270-int32value)Removed [-[NSAppleEventDescriptor numberOfItems]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1416786-numberofitems)Removed [-[NSAppleEventDescriptor returnID]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1415786-returnid)Removed [-[NSAppleEventDescriptor stringValue]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1407584-stringvalue)Removed [-[NSAppleEventDescriptor transactionID]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1408981-transactionid)Removed [-[NSAppleEventDescriptor typeCodeValue]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1409662-typecodevalue)Added [NSAppleEventDescriptor.aeDesc](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1413715-aedesc)Added [NSAppleEventDescriptor.booleanValue](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1412412-booleanvalue)Added [NSAppleEventDescriptor.data](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1413486-data)Added [NSAppleEventDescriptor.descriptorType](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1408495-descriptortype)Added [NSAppleEventDescriptor.enumCodeValue](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1408039-enumcodevalue)Added [NSAppleEventDescriptor.eventClass](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1410955-eventclass)Added [NSAppleEventDescriptor.eventID](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1413356-eventid)Added [NSAppleEventDescriptor.int32Value](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1407270-int32value)Added [NSAppleEventDescriptor.numberOfItems](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1416786-numberofitems)Added [NSAppleEventDescriptor.returnID](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1415786-returnid)Added [NSAppleEventDescriptor.stringValue](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1407584-stringvalue)Added [NSAppleEventDescriptor.transactionID](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1408981-transactionid)Added [NSAppleEventDescriptor.typeCodeValue](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1409662-typecodevalue)Modified [-[NSAppleEventDescriptor initListDescriptor]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1416351-initlistdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initListDescriptor ``` |
| To | ``` - (instancetype)initListDescriptor ``` |

Modified [-[NSAppleEventDescriptor initRecordDescriptor]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1416093-initrecorddescriptor)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initRecordDescriptor ``` |
| To | ``` - (instancetype)initRecordDescriptor ``` |

Modified [-[NSAppleEventDescriptor initWithAEDescNoCopy:]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1415233-initwithaedescnocopy)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithAEDescNoCopy:(const AEDesc *)aeDesc ``` | -- |
| To | ``` - (instancetype)initWithAEDescNoCopy:(const AEDesc *)aeDesc ``` | yes |

Modified [-[NSAppleEventDescriptor initWithDescriptorType:bytes:length:]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1417137-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDescriptorType:(DescType)descriptorType bytes:(const void *)bytes length:(NSUInteger)byteCount ``` |
| To | ``` - (instancetype)initWithDescriptorType:(DescType)descriptorType bytes:(const void *)bytes length:(NSUInteger)byteCount ``` |

Modified [-[NSAppleEventDescriptor initWithDescriptorType:data:]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1417129-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDescriptorType:(DescType)descriptorType data:(NSData *)data ``` |
| To | ``` - (instancetype)initWithDescriptorType:(DescType)descriptorType data:(NSData *)data ``` |

Modified [-[NSAppleEventDescriptor initWithEventClass:eventID:targetDescriptor:returnID:transactionID:]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1414999-initwitheventclass)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithEventClass:(AEEventClass)eventClass eventID:(AEEventID)eventID targetDescriptor:(NSAppleEventDescriptor *)targetDescriptor returnID:(AEReturnID)returnID transactionID:(AETransactionID)transactionID ``` |
| To | ``` - (instancetype)initWithEventClass:(AEEventClass)eventClass eventID:(AEEventID)eventID targetDescriptor:(NSAppleEventDescriptor *)targetDescriptor returnID:(AEReturnID)returnID transactionID:(AETransactionID)transactionID ``` |

NSAppleEventManager.hRemoved [-[NSAppleEventManager currentAppleEvent]](https://developer.apple.com/documentation/foundation/nsappleeventmanager/1414690-currentappleevent)Removed [-[NSAppleEventManager currentReplyAppleEvent]](https://developer.apple.com/documentation/foundation/nsappleeventmanager/1413207-currentreplyappleevent)Added [NSAppleEventManager.currentAppleEvent](https://developer.apple.com/documentation/foundation/nsappleeventmanager/1414690-currentappleevent)Added [NSAppleEventManager.currentReplyAppleEvent](https://developer.apple.com/documentation/foundation/nsappleeventmanager/1413207-currentreplyappleevent)NSAppleScript.hRemoved [-[NSAppleScript isCompiled]](https://developer.apple.com/documentation/foundation/nsapplescript/1410407-compiled)Removed [-[NSAppleScript source]](https://developer.apple.com/documentation/foundation/nsapplescript/1408453-source)Added [NSAppleScript.compiled](https://developer.apple.com/documentation/foundation/nsapplescript/1410407-iscompiled)Added [NSAppleScript.source](https://developer.apple.com/documentation/foundation/nsapplescript/1408453-source)Modified [-[NSAppleScript initWithContentsOfURL:error:]](https://developer.apple.com/documentation/foundation/nsapplescript/1412508-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url error:(NSDictionary **)errorInfo ``` | -- |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url error:(NSDictionary **)errorInfo ``` | yes |

Modified [-[NSAppleScript initWithSource:]](https://developer.apple.com/documentation/foundation/nsapplescript/1414313-initwithsource)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithSource:(NSString *)source ``` | -- |
| To | ``` - (instancetype)initWithSource:(NSString *)source ``` | yes |

NSArchiver.hRemoved [-[NSArchiver archiverData]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArchiver/Description.html#//apple_ref/occ/instm/NSArchiver/archiverData)Removed [-[NSObject classForArchiver]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/classForArchiver)Removed [-[NSUnarchiver isAtEnd]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUnarchiver/Description.html#//apple_ref/occ/instm/NSUnarchiver/isAtEnd)Removed [-[NSUnarchiver systemVersion]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUnarchiver/Description.html#//apple_ref/occ/instm/NSUnarchiver/systemVersion)Added [NSArchiver.archiverData](https://developer.apple.com/documentation/foundation/nsarchiver/1414268-archiverdata)Added [NSObject.classForArchiver](https://developer.apple.com/documentation/objectivec/nsobject/1411359-classforarchiver)Added [NSUnarchiver.atEnd](https://developer.apple.com/documentation/foundation/nsunarchiver/1407375-atend)Added [NSUnarchiver.systemVersion](https://developer.apple.com/documentation/foundation/nsunarchiver/1411208-systemversion)Modified [-[NSArchiver initForWritingWithMutableData:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArchiver/Description.html#//apple_ref/occ/instm/NSArchiver/initForWritingWithMutableData:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initForWritingWithMutableData:(NSMutableData *)mdata ``` | -- |
| To | ``` - (instancetype)initForWritingWithMutableData:(NSMutableData *)mdata ``` | yes |

Modified [-[NSUnarchiver initForReadingWithData:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUnarchiver/Description.html#//apple_ref/occ/instm/NSUnarchiver/initForReadingWithData:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initForReadingWithData:(NSData *)data ``` | -- |
| To | ``` - (instancetype)initForReadingWithData:(NSData *)data ``` | yes |

NSArray.hRemoved [-[NSArray count]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/count)Removed [-[NSArray description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/description)Removed [-[NSArray firstObject]](https://developer.apple.com/documentation/foundation/nsarray/1412852-firstobject)Removed [-[NSArray lastObject]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/lastObject)Removed [-[NSArray sortedArrayHint]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayHint)Added [NSArray.count](https://developer.apple.com/documentation/foundation/nsarray/1409982-count)Added [NSArray.description](https://developer.apple.com/documentation/foundation/nsarray/1413042-description)Added [NSArray.firstObject](https://developer.apple.com/documentation/foundation/nsarray/1412852-firstobject)Added [-[NSArray initWithCoder:]](https://developer.apple.com/documentation/foundation/nsarray/1407810-init)Added [NSArray.lastObject](https://developer.apple.com/documentation/foundation/nsarray/1408316-lastobject)Added [NSArray.sortedArrayHint](https://developer.apple.com/documentation/foundation/nsarray/1413063-sortedarrayhint)Added [+[NSMutableArray arrayWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1460079-arraywithcontentsoffile)Added [+[NSMutableArray arrayWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1460070-arraywithcontentsofurl)Added [-[NSMutableArray initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1409527-init)Added [-[NSMutableArray initWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1414670-initwithcontentsoffile)Added [-[NSMutableArray initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1411688-initwithcontentsofurl)Modified [+[NSArray arrayWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)arrayWithContentsOfFile:(NSString *)path ``` |
| To | ``` + (NSArray *)arrayWithContentsOfFile:(NSString *)path ``` |

Modified [+[NSArray arrayWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsarray/1460060-arraywithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)arrayWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (NSArray *)arrayWithContentsOfURL:(NSURL *)url ``` |

Modified [-[NSArray init]](https://developer.apple.com/documentation/foundation/nsarray/1414315-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSArray initWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (NSArray *)initWithContentsOfFile:(NSString *)path ``` |

Modified [-[NSArray initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsarray/1410518-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (NSArray *)initWithContentsOfURL:(NSURL *)url ``` |

Modified [-[NSArray initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:count:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableArray init]](https://developer.apple.com/documentation/foundation/nsmutablearray/1407556-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableArray initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/initWithCapacity:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSAttributedString.hRemoved [-[NSAttributedString length]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/length)Removed [-[NSAttributedString string]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/string)Removed [-[NSMutableAttributedString mutableString]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/mutableString)Added [NSAttributedString.length](https://developer.apple.com/documentation/foundation/nsattributedstring/1418432-length)Added [NSAttributedString.string](https://developer.apple.com/documentation/foundation/nsattributedstring/1412616-string)Added [NSMutableAttributedString.mutableString](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1416955-mutablestring)Modified [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [-[NSAttributedString initWithAttributedString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/initWithAttributedString:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAttributedString:(NSAttributedString *)attrStr ``` |
| To | ``` - (instancetype)initWithAttributedString:(NSAttributedString *)attrStr ``` |

Modified [-[NSAttributedString initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/initWithString:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithString:(NSString *)str ``` |
| To | ``` - (instancetype)initWithString:(NSString *)str ``` |

Modified [-[NSAttributedString initWithString:attributes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/initWithString:attributes:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithString:(NSString *)str attributes:(NSDictionary *)attrs ``` |
| To | ``` - (instancetype)initWithString:(NSString *)str attributes:(NSDictionary *)attrs ``` |

NSBackgroundActivityScheduler.h (Added)Added [NSBackgroundActivityScheduler](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler)Added [NSBackgroundActivityScheduler.identifier](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1412285-identifier)Added [-[NSBackgroundActivityScheduler initWithIdentifier:]](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1407482-init)Added [NSBackgroundActivityScheduler.interval](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1408819-interval)Added [-[NSBackgroundActivityScheduler invalidate]](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1408878-invalidate)Added [NSBackgroundActivityScheduler.qualityOfService](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1412688-qualityofservice)Added [NSBackgroundActivityScheduler.repeats](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1409853-repeats)Added [-[NSBackgroundActivityScheduler scheduleWithBlock:]](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1412813-schedulewithblock)Added [-[NSBackgroundActivityScheduler shouldDefer]](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1412167-shoulddefer)Added [NSBackgroundActivityScheduler.tolerance](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1408138-tolerance)Added [NSBackgroundActivityCompletionHandler](https://developer.apple.com/documentation/foundation/nsbackgroundactivitycompletionhandler)Added [NSBackgroundActivityResult](https://developer.apple.com/documentation/foundation/nsbackgroundactivityresult)Added [NSBackgroundActivityResultDeferred](https://developer.apple.com/documentation/foundation/nsbackgroundactivityresult/nsbackgroundactivityresultdeferred)Added [NSBackgroundActivityResultFinished](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/result/finished)NSBundle.hRemoved [-[NSBundle appStoreReceiptURL]](https://developer.apple.com/documentation/foundation/nsbundle/1407276-appstorereceipturl)Removed [-[NSBundle builtInPlugInsPath]](https://developer.apple.com/documentation/foundation/nsbundle/1408900-builtinpluginspath)Removed [-[NSBundle builtInPlugInsURL]](https://developer.apple.com/documentation/foundation/nsbundle/1409603-builtinpluginsurl)Removed [-[NSBundle bundleIdentifier]](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier)Removed [-[NSBundle bundlePath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/bundlePath)Removed [-[NSBundle bundleURL]](https://developer.apple.com/documentation/foundation/bundle/1415654-bundleurl)Removed [-[NSBundle developmentLocalization]](https://developer.apple.com/documentation/foundation/nsbundle/1417526-developmentlocalization)Removed [-[NSBundle executableArchitectures]](https://developer.apple.com/documentation/foundation/bundle/1415499-executablearchitectures)Removed [-[NSBundle executablePath]](https://developer.apple.com/documentation/foundation/bundle/1409078-executablepath)Removed [-[NSBundle executableURL]](https://developer.apple.com/documentation/foundation/bundle/1410470-executableurl)Removed [-[NSBundle infoDictionary]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/infoDictionary)Removed -[NSBundle isLoaded]Removed [-[NSBundle localizations]](https://developer.apple.com/documentation/foundation/bundle/1417415-localizations)Removed [-[NSBundle localizedInfoDictionary]](https://developer.apple.com/documentation/foundation/bundle/1407645-localizedinfodictionary)Removed [-[NSBundle preferredLocalizations]](https://developer.apple.com/documentation/foundation/nsbundle/1413220-preferredlocalizations)Removed [-[NSBundle principalClass]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/principalClass)Removed [-[NSBundle privateFrameworksPath]](https://developer.apple.com/documentation/foundation/bundle/1415562-privateframeworkspath)Removed [-[NSBundle privateFrameworksURL]](https://developer.apple.com/documentation/foundation/bundle/1417617-privateframeworksurl)Removed [-[NSBundle resourcePath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/resourcePath)Removed [-[NSBundle resourceURL]](https://developer.apple.com/documentation/foundation/bundle/1414821-resourceurl)Removed [-[NSBundle sharedFrameworksPath]](https://developer.apple.com/documentation/foundation/bundle/1417226-sharedframeworkspath)Removed [-[NSBundle sharedFrameworksURL]](https://developer.apple.com/documentation/foundation/nsbundle/1411774-sharedframeworksurl)Removed [-[NSBundle sharedSupportPath]](https://developer.apple.com/documentation/foundation/nsbundle/1411609-sharedsupportpath)Removed [-[NSBundle sharedSupportURL]](https://developer.apple.com/documentation/foundation/bundle/1416823-sharedsupporturl)Added [NSBundle.appStoreReceiptURL](https://developer.apple.com/documentation/foundation/bundle/1407276-appstorereceipturl)Added [NSBundle.builtInPlugInsPath](https://developer.apple.com/documentation/foundation/bundle/1408900-builtinpluginspath)Added [NSBundle.builtInPlugInsURL](https://developer.apple.com/documentation/foundation/nsbundle/1409603-builtinpluginsurl)Added [NSBundle.bundleIdentifier](https://developer.apple.com/documentation/foundation/bundle/1418023-bundleidentifier)Added [NSBundle.bundlePath](https://developer.apple.com/documentation/foundation/nsbundle/1407973-bundlepath)Added [NSBundle.bundleURL](https://developer.apple.com/documentation/foundation/bundle/1415654-bundleurl)Added [NSBundle.developmentLocalization](https://developer.apple.com/documentation/foundation/bundle/1417526-developmentlocalization)Added [NSBundle.executableArchitectures](https://developer.apple.com/documentation/foundation/nsbundle/1415499-executablearchitectures)Added [NSBundle.executablePath](https://developer.apple.com/documentation/foundation/nsbundle/1409078-executablepath)Added [NSBundle.executableURL](https://developer.apple.com/documentation/foundation/nsbundle/1410470-executableurl)Added [NSBundle.infoDictionary](https://developer.apple.com/documentation/foundation/nsbundle/1413477-infodictionary)Added [NSBundle.loaded](https://developer.apple.com/documentation/foundation/bundle/1413594-isloaded)Added [NSBundle.localizations](https://developer.apple.com/documentation/foundation/nsbundle/1417415-localizations)Added [NSBundle.localizedInfoDictionary](https://developer.apple.com/documentation/foundation/nsbundle/1407645-localizedinfodictionary)Added [NSBundle.preferredLocalizations](https://developer.apple.com/documentation/foundation/bundle/1413220-preferredlocalizations)Added [NSBundle.principalClass](https://developer.apple.com/documentation/foundation/bundle/1409048-principalclass)Added [NSBundle.privateFrameworksPath](https://developer.apple.com/documentation/foundation/nsbundle/1415562-privateframeworkspath)Added [NSBundle.privateFrameworksURL](https://developer.apple.com/documentation/foundation/bundle/1417617-privateframeworksurl)Added [NSBundle.resourcePath](https://developer.apple.com/documentation/foundation/nsbundle/1417723-resourcepath)Added [NSBundle.resourceURL](https://developer.apple.com/documentation/foundation/nsbundle/1414821-resourceurl)Added [NSBundle.sharedFrameworksPath](https://developer.apple.com/documentation/foundation/bundle/1417226-sharedframeworkspath)Added [NSBundle.sharedFrameworksURL](https://developer.apple.com/documentation/foundation/bundle/1411774-sharedframeworksurl)Added [NSBundle.sharedSupportPath](https://developer.apple.com/documentation/foundation/bundle/1411609-sharedsupportpath)Added [NSBundle.sharedSupportURL](https://developer.apple.com/documentation/foundation/bundle/1416823-sharedsupporturl)Modified [+[NSBundle bundleWithPath:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/bundleWithPath:)

|  | Declaration |
| --- | --- |
| From | ``` + (NSBundle *)bundleWithPath:(NSString *)path ``` |
| To | ``` + (instancetype)bundleWithPath:(NSString *)path ``` |

Modified [+[NSBundle bundleWithURL:]](https://developer.apple.com/documentation/foundation/nsbundle/1494992-bundlewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (NSBundle *)bundleWithURL:(NSURL *)url ``` |
| To | ``` + (instancetype)bundleWithURL:(NSURL *)url ``` |

Modified [-[NSBundle initWithPath:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/initWithPath:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithPath:(NSString *)path ``` | -- |
| To | ``` - (instancetype)initWithPath:(NSString *)path ``` | yes |

Modified [-[NSBundle initWithURL:]](https://developer.apple.com/documentation/foundation/nsbundle/1409352-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url ``` |

NSByteCountFormatter.hAdded [NSByteCountFormatter.formattingContext](https://developer.apple.com/documentation/foundation/bytecountformatter/1412185-formattingcontext)NSCache.hRemoved [-[NSCache countLimit]](https://developer.apple.com/documentation/foundation/nscache/1416355-countlimit)Removed [-[NSCache delegate]](https://developer.apple.com/documentation/foundation/nscache/1413061-delegate)Removed [-[NSCache evictsObjectsWithDiscardedContent]](https://developer.apple.com/documentation/foundation/nscache/1408469-evictsobjectswithdiscardedconten)Removed [-[NSCache name]](https://developer.apple.com/documentation/foundation/nscache/1409941-name)Removed [-[NSCache setCountLimit:]](https://developer.apple.com/documentation/foundation/nscache/1416355-countlimit)Removed [-[NSCache setDelegate:]](https://developer.apple.com/documentation/foundation/nscache/1413061-delegate)Removed [-[NSCache setEvictsObjectsWithDiscardedContent:]](https://developer.apple.com/documentation/foundation/nscache/1408469-evictsobjectswithdiscardedconten)Removed [-[NSCache setName:]](https://developer.apple.com/documentation/foundation/nscache/1409941-name)Removed [-[NSCache setTotalCostLimit:]](https://developer.apple.com/documentation/foundation/nscache/1407672-totalcostlimit)Removed [-[NSCache totalCostLimit]](https://developer.apple.com/documentation/foundation/nscache/1407672-totalcostlimit)Added [NSCache.countLimit](https://developer.apple.com/documentation/foundation/nscache/1416355-countlimit)Added [NSCache.delegate](https://developer.apple.com/documentation/foundation/nscache/1413061-delegate)Added [NSCache.evictsObjectsWithDiscardedContent](https://developer.apple.com/documentation/foundation/nscache/1408469-evictsobjectswithdiscardedconten)Added [NSCache.name](https://developer.apple.com/documentation/foundation/nscache/1409941-name)Added [NSCache.totalCostLimit](https://developer.apple.com/documentation/foundation/nscache/1407672-totalcostlimit)Modified [-[NSCacheDelegate cache:willEvictObject:]](https://developer.apple.com/documentation/foundation/nscachedelegate/1416107-cache)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSCalendar.hRemoved [-[NSCalendar AMSymbol]](https://developer.apple.com/documentation/foundation/nscalendar/1416226-amsymbol)Removed [-[NSCalendar PMSymbol]](https://developer.apple.com/documentation/foundation/nscalendar/1416343-pmsymbol)Removed [-[NSCalendar calendarIdentifier]](https://developer.apple.com/documentation/foundation/nscalendar/1408268-calendaridentifier)Removed [-[NSCalendar eraSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1415038-erasymbols)Removed [-[NSCalendar firstWeekday]](https://developer.apple.com/documentation/foundation/nscalendar/1408310-firstweekday)Removed [-[NSCalendar locale]](https://developer.apple.com/documentation/foundation/nscalendar/1418111-locale)Removed [-[NSCalendar longEraSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1414285-longerasymbols)Removed [-[NSCalendar minimumDaysInFirstWeek]](https://developer.apple.com/documentation/foundation/nscalendar/1410186-minimumdaysinfirstweek)Removed [-[NSCalendar monthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1414872-monthsymbols)Removed [-[NSCalendar quarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1411517-quartersymbols)Removed [-[NSCalendar setFirstWeekday:]](https://developer.apple.com/documentation/foundation/nscalendar/1408310-firstweekday)Removed [-[NSCalendar setLocale:]](https://developer.apple.com/documentation/foundation/nscalendar/1418111-locale)Removed [-[NSCalendar setMinimumDaysInFirstWeek:]](https://developer.apple.com/documentation/foundation/nscalendar/1410186-minimumdaysinfirstweek)Removed [-[NSCalendar setTimeZone:]](https://developer.apple.com/documentation/foundation/nscalendar/1409969-timezone)Removed [-[NSCalendar shortMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1408952-shortmonthsymbols)Removed [-[NSCalendar shortQuarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1414864-shortquartersymbols)Removed [-[NSCalendar shortStandaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1418180-shortstandalonemonthsymbols)Removed [-[NSCalendar shortStandaloneQuarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1409823-shortstandalonequartersymbols)Removed [-[NSCalendar shortStandaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1413871-shortstandaloneweekdaysymbols)Removed [-[NSCalendar shortWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1407268-shortweekdaysymbols)Removed [-[NSCalendar standaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1409598-standalonemonthsymbols)Removed [-[NSCalendar standaloneQuarterSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1407159-standalonequartersymbols)Removed [-[NSCalendar standaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1411219-standaloneweekdaysymbols)Removed [-[NSCalendar timeZone]](https://developer.apple.com/documentation/foundation/nscalendar/1409969-timezone)Removed [-[NSCalendar veryShortMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1412779-veryshortmonthsymbols)Removed [-[NSCalendar veryShortStandaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1408035-veryshortstandalonemonthsymbols)Removed [-[NSCalendar veryShortStandaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1418273-veryshortstandaloneweekdaysymbol)Removed [-[NSCalendar veryShortWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1417207-veryshortweekdaysymbols)Removed [-[NSCalendar weekdaySymbols]](https://developer.apple.com/documentation/foundation/nscalendar/1412939-weekdaysymbols)Removed [-[NSDateComponents calendar]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415799-calendar)Removed [-[NSDateComponents date]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1412861-date)Removed [-[NSDateComponents day]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415267-day)Removed [-[NSDateComponents era]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416364-era)Removed [-[NSDateComponents hour]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1411355-hour)Removed [-[NSDateComponents isLeapMonth]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408836-isleapmonth)Removed -[NSDateComponents isValidDate]Removed [-[NSDateComponents minute]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1409443-minute)Removed [-[NSDateComponents month]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408724-month)Removed [-[NSDateComponents nanosecond]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415730-nanosecond)Removed [-[NSDateComponents quarter]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416503-quarter)Removed [-[NSDateComponents second]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1414045-second)Removed [-[NSDateComponents setCalendar:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415799-calendar)Removed [-[NSDateComponents setDay:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415267-day)Removed [-[NSDateComponents setEra:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416364-era)Removed [-[NSDateComponents setHour:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1411355-hour)Removed [-[NSDateComponents setLeapMonth:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408836-leapmonth)Removed [-[NSDateComponents setMinute:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1409443-minute)Removed [-[NSDateComponents setMonth:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408724-month)Removed [-[NSDateComponents setNanosecond:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415730-nanosecond)Removed [-[NSDateComponents setQuarter:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416503-quarter)Removed [-[NSDateComponents setSecond:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1414045-second)Removed [-[NSDateComponents setTimeZone:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408233-timezone)Removed [-[NSDateComponents setWeekOfMonth:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413168-weekofmonth)Removed [-[NSDateComponents setWeekOfYear:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416908-weekofyear)Removed [-[NSDateComponents setWeekday:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1410442-weekday)Removed [-[NSDateComponents setWeekdayOrdinal:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1409476-weekdayordinal)Removed [-[NSDateComponents setYear:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1412462-year)Removed [-[NSDateComponents setYearForWeekOfYear:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413809-yearforweekofyear)Removed [-[NSDateComponents timeZone]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408233-timezone)Removed [-[NSDateComponents weekOfMonth]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413168-weekofmonth)Removed [-[NSDateComponents weekOfYear]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416908-weekofyear)Removed [-[NSDateComponents weekday]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1410442-weekday)Removed [-[NSDateComponents weekdayOrdinal]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1409476-weekdayordinal)Removed [-[NSDateComponents year]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1412462-year)Removed [-[NSDateComponents yearForWeekOfYear]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413809-yearforweekofyear)Added [NSCalendar.AMSymbol](https://developer.apple.com/documentation/foundation/nscalendar/1416226-amsymbol)Added [NSCalendar.PMSymbol](https://developer.apple.com/documentation/foundation/nscalendar/1416343-pmsymbol)Added [NSCalendar.calendarIdentifier](https://developer.apple.com/documentation/foundation/nscalendar/1408268-calendaridentifier)Added [NSCalendar.eraSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1415038-erasymbols)Added [NSCalendar.firstWeekday](https://developer.apple.com/documentation/foundation/nscalendar/1408310-firstweekday)Added [NSCalendar.locale](https://developer.apple.com/documentation/foundation/nscalendar/1418111-locale)Added [NSCalendar.longEraSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414285-longerasymbols)Added [NSCalendar.minimumDaysInFirstWeek](https://developer.apple.com/documentation/foundation/nscalendar/1410186-minimumdaysinfirstweek)Added [NSCalendar.monthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414872-monthsymbols)Added [NSCalendar.quarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1411517-quartersymbols)Added [NSCalendar.shortMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1408952-shortmonthsymbols)Added [NSCalendar.shortQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414864-shortquartersymbols)Added [NSCalendar.shortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1418180-shortstandalonemonthsymbols)Added [NSCalendar.shortStandaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1409823-shortstandalonequartersymbols)Added [NSCalendar.shortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1413871-shortstandaloneweekdaysymbols)Added [NSCalendar.shortWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1407268-shortweekdaysymbols)Added [NSCalendar.standaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1409598-standalonemonthsymbols)Added [NSCalendar.standaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1407159-standalonequartersymbols)Added [NSCalendar.standaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1411219-standaloneweekdaysymbols)Added [NSCalendar.timeZone](https://developer.apple.com/documentation/foundation/nscalendar/1409969-timezone)Added [NSCalendar.veryShortMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1412779-veryshortmonthsymbols)Added [NSCalendar.veryShortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1408035-veryshortstandalonemonthsymbols)Added [NSCalendar.veryShortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1418273-veryshortstandaloneweekdaysymbol)Added [NSCalendar.veryShortWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1417207-veryshortweekdaysymbols)Added [NSCalendar.weekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1412939-weekdaysymbols)Added [NSDateComponents.calendar](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415799-calendar)Added [NSDateComponents.date](https://developer.apple.com/documentation/foundation/nsdatecomponents/1412861-date)Added [NSDateComponents.day](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415267-day)Added [NSDateComponents.era](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416364-era)Added [NSDateComponents.hour](https://developer.apple.com/documentation/foundation/nsdatecomponents/1411355-hour)Added [NSDateComponents.leapMonth](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408836-isleapmonth)Added [NSDateComponents.minute](https://developer.apple.com/documentation/foundation/nsdatecomponents/1409443-minute)Added [NSDateComponents.month](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408724-month)Added [NSDateComponents.nanosecond](https://developer.apple.com/documentation/foundation/nsdatecomponents/1415730-nanosecond)Added [NSDateComponents.quarter](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416503-quarter)Added [NSDateComponents.second](https://developer.apple.com/documentation/foundation/nsdatecomponents/1414045-second)Added [NSDateComponents.timeZone](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408233-timezone)Added [NSDateComponents.validDate](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408788-validdate)Added [NSDateComponents.weekOfMonth](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413168-weekofmonth)Added [NSDateComponents.weekOfYear](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416908-weekofyear)Added [NSDateComponents.weekday](https://developer.apple.com/documentation/foundation/nsdatecomponents/1410442-weekday)Added [NSDateComponents.weekdayOrdinal](https://developer.apple.com/documentation/foundation/nsdatecomponents/1409476-weekdayordinal)Added [NSDateComponents.year](https://developer.apple.com/documentation/foundation/nsdatecomponents/1412462-year)Added [NSDateComponents.yearForWeekOfYear](https://developer.apple.com/documentation/foundation/nsdatecomponents/1413809-yearforweekofyear)Added [NSCalendarIdentifierIslamicTabular](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1414754-islamictabular)Added [NSCalendarIdentifierIslamicUmmAlQura](https://developer.apple.com/documentation/foundation/nscalendaridentifierislamicummalqura)Modified [+[NSCalendar autoupdatingCurrentCalendar]](https://developer.apple.com/documentation/foundation/nscalendar/1413771-autoupdatingcurrent)

|  | Declaration |
| --- | --- |
| From | ``` + (id)autoupdatingCurrentCalendar ``` |
| To | ``` + (NSCalendar *)autoupdatingCurrentCalendar ``` |

Modified [+[NSCalendar calendarWithIdentifier:]](https://developer.apple.com/documentation/foundation/nscalendar/1412400-calendarwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (id)calendarWithIdentifier:(NSString *)calendarIdentifierConstant ``` |
| To | ``` + (NSCalendar *)calendarWithIdentifier:(NSString *)calendarIdentifierConstant ``` |

Modified [+[NSCalendar currentCalendar]](https://developer.apple.com/documentation/foundation/nscalendar/1408501-current)

|  | Declaration |
| --- | --- |
| From | ``` + (id)currentCalendar ``` |
| To | ``` + (NSCalendar *)currentCalendar ``` |

Modified [-[NSCalendar initWithCalendarIdentifier:]](https://developer.apple.com/documentation/foundation/nscalendar/1415991-initwithcalendaridentifier)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDateComponents setWeek:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1430337-setweek)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [-[NSDateComponents week]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1430328-week)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [NSCalendarCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nscalendarcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSDayCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1409435-nsdaycalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSEraCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1409052-nseracalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSHourCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411272-nshourcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSMinuteCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1413292-nsminutecalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSMonthCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1408613-nsmonthcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSQuarterCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1414015-nsquartercalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSSecondCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nssecondcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSTimeZoneCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nstimezonecalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSUndefinedDateComponent](https://developer.apple.com/documentation/foundation/nsundefineddatecomponent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWeekCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1411024-nsweekcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWeekOfMonthCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekofmonthcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWeekOfYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekofyearcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWeekdayCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekdaycalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWeekdayOrdinalCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendarunit/nsweekdayordinalcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWrapCalendarComponents](https://developer.apple.com/documentation/foundation/1430373-nswrapcalendarcomponents/nswrapcalendarcomponents)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1415822-nsyearcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSYearForWeekOfYearCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1408285-nsyearforweekofyearcalendarunit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSCalendarDate.hModified [NSCalendarDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/cl/NSCalendarDate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSCalendarDate calendarDate]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/clm/NSCalendarDate/calendarDate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate calendarFormat]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/calendarFormat)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate dateByAddingYears:months:days:hours:minutes:seconds:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/dateByAddingYears:months:days:hours:minutes:seconds:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSCalendarDate dateWithString:calendarFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/clm/NSCalendarDate/dateWithString:calendarFormat:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSCalendarDate dateWithString:calendarFormat:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/clm/NSCalendarDate/dateWithString:calendarFormat:locale:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSCalendarDate dateWithYear:month:day:hour:minute:second:timeZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/clm/NSCalendarDate/dateWithYear:month:day:hour:minute:second:timeZone:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate dayOfCommonEra]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/dayOfCommonEra)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate dayOfMonth]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/dayOfMonth)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate dayOfWeek]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/dayOfWeek)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate dayOfYear]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/dayOfYear)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate descriptionWithCalendarFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/descriptionWithCalendarFormat:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate descriptionWithCalendarFormat:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/descriptionWithCalendarFormat:locale:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate descriptionWithLocale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/descriptionWithLocale:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate hourOfDay]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/hourOfDay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/initWithString:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate initWithString:calendarFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/initWithString:calendarFormat:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate initWithString:calendarFormat:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/initWithString:calendarFormat:locale:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate initWithYear:month:day:hour:minute:second:timeZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/initWithYear:month:day:hour:minute:second:timeZone:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate minuteOfHour]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/minuteOfHour)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate monthOfYear]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/monthOfYear)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate secondOfMinute]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/secondOfMinute)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate setCalendarFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/setCalendarFormat:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate setTimeZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/setTimeZone:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate timeZone]](https://developer.apple.com/documentation/foundation/nscalendardate/1564277-timezone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate yearOfCommonEra]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/yearOfCommonEra)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSCalendarDate years:months:days:hours:minutes:seconds:sinceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/years:months:days:hours:minutes:seconds:sinceDate:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSDate dateWithCalendarFormat:timeZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/dateWithCalendarFormat:timeZone:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSDate dateWithNaturalLanguageString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithNaturalLanguageString:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSDate dateWithNaturalLanguageString:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithNaturalLanguageString:locale:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSDate dateWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/dateWithString:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSDate descriptionWithCalendarFormat:timeZone:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/descriptionWithCalendarFormat:timeZone:locale:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSDate initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithString:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSCharacterSet.hRemoved [-[NSCharacterSet bitmapRepresentation]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/instm/NSCharacterSet/bitmapRepresentation)Removed [-[NSCharacterSet invertedSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/instm/NSCharacterSet/invertedSet)Added [NSCharacterSet.bitmapRepresentation](https://developer.apple.com/documentation/foundation/nscharacterset/1417719-bitmaprepresentation)Added [-[NSCharacterSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nscharacterset/1408497-initwithcoder)Added [NSCharacterSet.invertedSet](https://developer.apple.com/documentation/foundation/nscharacterset/1414025-inverted)Added [+[NSMutableCharacterSet alphanumericCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1417591-alphanumericcharacterset)Added [+[NSMutableCharacterSet capitalizedLetterCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1417049-capitalizedlettercharacterset)Added [+[NSMutableCharacterSet characterSetWithBitmapRepresentation:]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1415715-charactersetwithbitmaprepresenta)Added [+[NSMutableCharacterSet characterSetWithCharactersInString:]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1415362-init)Added [+[NSMutableCharacterSet characterSetWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1414233-charactersetwithcontentsoffile)Added [+[NSMutableCharacterSet characterSetWithRange:]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1410070-init)Added [+[NSMutableCharacterSet controlCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1414334-controlcharacterset)Added [+[NSMutableCharacterSet decimalDigitCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1415296-decimaldigit)Added [+[NSMutableCharacterSet decomposableCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1413503-decomposable)Added [+[NSMutableCharacterSet illegalCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1413024-illegal)Added [+[NSMutableCharacterSet letterCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1407361-lettercharacterset)Added [+[NSMutableCharacterSet lowercaseLetterCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1411410-lowercaselettercharacterset)Added [+[NSMutableCharacterSet newlineCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1409923-newline)Added [+[NSMutableCharacterSet nonBaseCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1409262-nonbase)Added [+[NSMutableCharacterSet punctuationCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1417626-punctuation)Added [+[NSMutableCharacterSet symbolCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1408001-symbolcharacterset)Added [+[NSMutableCharacterSet uppercaseLetterCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1418201-uppercaselettercharacterset)Added [+[NSMutableCharacterSet whitespaceAndNewlineCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1412583-whitespaceandnewline)Added [+[NSMutableCharacterSet whitespaceCharacterSet]](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/1414972-whitespacecharacterset)Modified [+[NSCharacterSet alphanumericCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/alphanumericCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)alphanumericCharacterSet ``` |
| To | ``` + (NSCharacterSet *)alphanumericCharacterSet ``` |

Modified [+[NSCharacterSet capitalizedLetterCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1414409-capitalizedlettercharacterset)

|  | Declaration |
| --- | --- |
| From | ``` + (id)capitalizedLetterCharacterSet ``` |
| To | ``` + (NSCharacterSet *)capitalizedLetterCharacterSet ``` |

Modified [+[NSCharacterSet characterSetWithBitmapRepresentation:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/characterSetWithBitmapRepresentation:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)characterSetWithBitmapRepresentation:(NSData *)data ``` |
| To | ``` + (NSCharacterSet *)characterSetWithBitmapRepresentation:(NSData *)data ``` |

Modified [+[NSCharacterSet characterSetWithCharactersInString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/characterSetWithCharactersInString:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)characterSetWithCharactersInString:(NSString *)aString ``` |
| To | ``` + (NSCharacterSet *)characterSetWithCharactersInString:(NSString *)aString ``` |

Modified [+[NSCharacterSet characterSetWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/characterSetWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)characterSetWithContentsOfFile:(NSString *)fName ``` |
| To | ``` + (NSCharacterSet *)characterSetWithContentsOfFile:(NSString *)fName ``` |

Modified [+[NSCharacterSet characterSetWithRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/characterSetWithRange:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)characterSetWithRange:(NSRange)aRange ``` |
| To | ``` + (NSCharacterSet *)characterSetWithRange:(NSRange)aRange ``` |

Modified [+[NSCharacterSet controlCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/controlCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)controlCharacterSet ``` |
| To | ``` + (NSCharacterSet *)controlCharacterSet ``` |

Modified [+[NSCharacterSet decimalDigitCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/decimalDigitCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)decimalDigitCharacterSet ``` |
| To | ``` + (NSCharacterSet *)decimalDigitCharacterSet ``` |

Modified [+[NSCharacterSet decomposableCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/decomposableCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)decomposableCharacterSet ``` |
| To | ``` + (NSCharacterSet *)decomposableCharacterSet ``` |

Modified [+[NSCharacterSet illegalCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/illegalCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)illegalCharacterSet ``` |
| To | ``` + (NSCharacterSet *)illegalCharacterSet ``` |

Modified [+[NSCharacterSet letterCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/letterCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)letterCharacterSet ``` |
| To | ``` + (NSCharacterSet *)letterCharacterSet ``` |

Modified [+[NSCharacterSet lowercaseLetterCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/lowercaseLetterCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)lowercaseLetterCharacterSet ``` |
| To | ``` + (NSCharacterSet *)lowercaseLetterCharacterSet ``` |

Modified [+[NSCharacterSet newlineCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416730-newlinecharacterset)

|  | Declaration |
| --- | --- |
| From | ``` + (id)newlineCharacterSet ``` |
| To | ``` + (NSCharacterSet *)newlineCharacterSet ``` |

Modified [+[NSCharacterSet nonBaseCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/nonBaseCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)nonBaseCharacterSet ``` |
| To | ``` + (NSCharacterSet *)nonBaseCharacterSet ``` |

Modified [+[NSCharacterSet punctuationCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/punctuationCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)punctuationCharacterSet ``` |
| To | ``` + (NSCharacterSet *)punctuationCharacterSet ``` |

Modified [+[NSCharacterSet symbolCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1410965-symbolcharacterset)

|  | Declaration |
| --- | --- |
| From | ``` + (id)symbolCharacterSet ``` |
| To | ``` + (NSCharacterSet *)symbolCharacterSet ``` |

Modified [+[NSCharacterSet uppercaseLetterCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/uppercaseLetterCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)uppercaseLetterCharacterSet ``` |
| To | ``` + (NSCharacterSet *)uppercaseLetterCharacterSet ``` |

Modified [+[NSCharacterSet whitespaceAndNewlineCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/whitespaceAndNewlineCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)whitespaceAndNewlineCharacterSet ``` |
| To | ``` + (NSCharacterSet *)whitespaceAndNewlineCharacterSet ``` |

Modified [+[NSCharacterSet whitespaceCharacterSet]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/clm/NSCharacterSet/whitespaceCharacterSet)

|  | Declaration |
| --- | --- |
| From | ``` + (id)whitespaceCharacterSet ``` |
| To | ``` + (NSCharacterSet *)whitespaceCharacterSet ``` |

NSClassDescription.hRemoved [-[NSClassDescription attributeKeys]](https://developer.apple.com/documentation/foundation/nsclassdescription/1415001-attributekeys)Removed [-[NSClassDescription toManyRelationshipKeys]](https://developer.apple.com/documentation/foundation/nsclassdescription/1408530-tomanyrelationshipkeys)Removed [-[NSClassDescription toOneRelationshipKeys]](https://developer.apple.com/documentation/foundation/nsclassdescription/1411937-toonerelationshipkeys)Removed [-[NSObject attributeKeys]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/attributeKeys)Removed [-[NSObject classDescription]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/classDescription)Removed [-[NSObject toManyRelationshipKeys]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/toManyRelationshipKeys)Removed [-[NSObject toOneRelationshipKeys]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/toOneRelationshipKeys)Added [NSClassDescription.attributeKeys](https://developer.apple.com/documentation/foundation/nsclassdescription/1415001-attributekeys)Added [NSClassDescription.toManyRelationshipKeys](https://developer.apple.com/documentation/foundation/nsclassdescription/1408530-tomanyrelationshipkeys)Added [NSClassDescription.toOneRelationshipKeys](https://developer.apple.com/documentation/foundation/nsclassdescription/1411937-toonerelationshipkeys)Added [NSObject.attributeKeys](https://developer.apple.com/documentation/objectivec/nsobject/1415656-attributekeys)Added [NSObject.classDescription](https://developer.apple.com/documentation/objectivec/nsobject/1411858-classdescription)Added [NSObject.toManyRelationshipKeys](https://developer.apple.com/documentation/objectivec/nsobject/1415662-tomanyrelationshipkeys)Added [NSObject.toOneRelationshipKeys](https://developer.apple.com/documentation/objectivec/nsobject/1414814-toonerelationshipkeys)NSCoder.hRemoved [-[NSCoder allowedClasses]](https://developer.apple.com/documentation/foundation/nscoder/1412486-allowedclasses)Removed [-[NSCoder allowsKeyedCoding]](https://developer.apple.com/documentation/foundation/nscoder/1417541-allowskeyedcoding)Removed [-[NSCoder requiresSecureCoding]](https://developer.apple.com/documentation/foundation/nscoder/1409845-requiressecurecoding)Removed [-[NSCoder systemVersion]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCoder/Description.html#//apple_ref/occ/instm/NSCoder/systemVersion)Added [NSCoder.allowedClasses](https://developer.apple.com/documentation/foundation/nscoder/1412486-allowedclasses)Added [NSCoder.allowsKeyedCoding](https://developer.apple.com/documentation/foundation/nscoder/1417541-allowskeyedcoding)Added [NSCoder.requiresSecureCoding](https://developer.apple.com/documentation/foundation/nscoder/1409845-requiressecurecoding)Added [NSCoder.systemVersion](https://developer.apple.com/documentation/foundation/nscoder/1413205-systemversion)NSComparisonPredicate.hRemoved [-[NSComparisonPredicate comparisonPredicateModifier]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1416376-comparisonpredicatemodifier)Removed [-[NSComparisonPredicate customSelector]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1413661-customselector)Removed [-[NSComparisonPredicate leftExpression]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1412552-leftexpression)Removed [-[NSComparisonPredicate options]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1414069-options)Removed [-[NSComparisonPredicate predicateOperatorType]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1418327-predicateoperatortype)Removed [-[NSComparisonPredicate rightExpression]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1409469-rightexpression)Added [NSComparisonPredicate.comparisonPredicateModifier](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1416376-comparisonpredicatemodifier)Added [NSComparisonPredicate.customSelector](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1413661-customselector)Added [NSComparisonPredicate.leftExpression](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1412552-leftexpression)Added [NSComparisonPredicate.options](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1414069-options)Added [NSComparisonPredicate.predicateOperatorType](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1418327-predicateoperatortype)Added [NSComparisonPredicate.rightExpression](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1409469-rightexpression)Modified [-[NSComparisonPredicate initWithLeftExpression:rightExpression:customSelector:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1409054-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs customSelector:(SEL)selector ``` |
| To | ``` - (instancetype)initWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs customSelector:(SEL)selector ``` |

Modified [-[NSComparisonPredicate initWithLeftExpression:rightExpression:modifier:type:options:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1413523-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSComparisonPredicateOptions)options ``` |
| To | ``` - (instancetype)initWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSComparisonPredicateOptions)options ``` |

Modified [+[NSComparisonPredicate predicateWithLeftExpression:rightExpression:customSelector:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1568141-predicatewithleftexpression)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)predicateWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs customSelector:(SEL)selector ``` |
| To | ``` + (NSComparisonPredicate *)predicateWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs customSelector:(SEL)selector ``` |

Modified [+[NSComparisonPredicate predicateWithLeftExpression:rightExpression:modifier:type:options:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1568140-predicatewithleftexpression)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)predicateWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSComparisonPredicateOptions)options ``` |
| To | ``` + (NSComparisonPredicate *)predicateWithLeftExpression:(NSExpression *)lhs rightExpression:(NSExpression *)rhs modifier:(NSComparisonPredicateModifier)modifier type:(NSPredicateOperatorType)type options:(NSComparisonPredicateOptions)options ``` |

NSCompoundPredicate.hRemoved [-[NSCompoundPredicate compoundPredicateType]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1412973-compoundpredicatetype)Removed [-[NSCompoundPredicate subpredicates]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1410273-subpredicates)Added [NSCompoundPredicate.compoundPredicateType](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1412973-compoundpredicatetype)Added [NSCompoundPredicate.subpredicates](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1410273-subpredicates)Modified [+[NSCompoundPredicate andPredicateWithSubpredicates:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1407855-andpredicatewithsubpredicates)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)andPredicateWithSubpredicates:(NSArray *)subpredicates ``` |
| To | ``` + (NSCompoundPredicate *)andPredicateWithSubpredicates:(NSArray *)subpredicates ``` |

Modified [-[NSCompoundPredicate initWithType:subpredicates:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1407744-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(NSCompoundPredicateType)type subpredicates:(NSArray *)subpredicates ``` |
| To | ``` - (instancetype)initWithType:(NSCompoundPredicateType)type subpredicates:(NSArray *)subpredicates ``` |

Modified [+[NSCompoundPredicate notPredicateWithSubpredicate:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1409462-notpredicatewithsubpredicate)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)notPredicateWithSubpredicate:(NSPredicate *)predicate ``` |
| To | ``` + (NSCompoundPredicate *)notPredicateWithSubpredicate:(NSPredicate *)predicate ``` |

Modified [+[NSCompoundPredicate orPredicateWithSubpredicates:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1417873-orpredicatewithsubpredicates)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)orPredicateWithSubpredicates:(NSArray *)subpredicates ``` |
| To | ``` + (NSCompoundPredicate *)orPredicateWithSubpredicates:(NSArray *)subpredicates ``` |

NSConnection.hRemoved [-[NSConnection delegate]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/delegate)Removed [-[NSConnection independentConversationQueueing]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/independentConversationQueueing)Removed [-[NSConnection isValid]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/isValid)Removed [-[NSConnection localObjects]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/localObjects)Removed [-[NSConnection multipleThreadsEnabled]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/multipleThreadsEnabled)Removed [-[NSConnection receivePort]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/receivePort)Removed [-[NSConnection remoteObjects]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/remoteObjects)Removed [-[NSConnection replyTimeout]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/replyTimeout)Removed [-[NSConnection requestModes]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/requestModes)Removed [-[NSConnection requestTimeout]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/requestTimeout)Removed [-[NSConnection rootObject]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/rootObject)Removed [-[NSConnection rootProxy]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/rootProxy)Removed [-[NSConnection sendPort]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/sendPort)Removed [-[NSConnection setDelegate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/setDelegate:)Removed [-[NSConnection setIndependentConversationQueueing:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/setIndependentConversationQueueing:)Removed [-[NSConnection setReplyTimeout:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/setReplyTimeout:)Removed [-[NSConnection setRequestTimeout:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/setRequestTimeout:)Removed [-[NSConnection setRootObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/setRootObject:)Removed [-[NSConnection statistics]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/statistics)Removed [-[NSDistantObjectRequest connection]](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/1806828-connection)Removed [-[NSDistantObjectRequest conversation]](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/1806830-conversation)Removed [-[NSDistantObjectRequest invocation]](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/1806832-invocation)Added [NSConnection.delegate](https://developer.apple.com/documentation/foundation/nsconnection/1478077-delegate)Added [NSConnection.independentConversationQueueing](https://developer.apple.com/documentation/foundation/nsconnection/1478038-independentconversationqueueing)Added [NSConnection.localObjects](https://developer.apple.com/documentation/foundation/nsconnection/1478043-localobjects)Added [NSConnection.multipleThreadsEnabled](https://developer.apple.com/documentation/foundation/nsconnection/1478100-multiplethreadsenabled)Added [NSConnection.receivePort](https://developer.apple.com/documentation/foundation/nsconnection/1478096-receiveport)Added [NSConnection.remoteObjects](https://developer.apple.com/documentation/foundation/nsconnection/1478047-remoteobjects)Added [NSConnection.replyTimeout](https://developer.apple.com/documentation/foundation/nsconnection/1478053-replytimeout)Added [NSConnection.requestModes](https://developer.apple.com/documentation/foundation/nsconnection/1478091-requestmodes)Added [NSConnection.requestTimeout](https://developer.apple.com/documentation/foundation/nsconnection/1478010-requesttimeout)Added [NSConnection.rootObject](https://developer.apple.com/documentation/foundation/nsconnection/1478012-rootobject)Added [NSConnection.rootProxy](https://developer.apple.com/documentation/foundation/nsconnection/1478065-rootproxy)Added [NSConnection.sendPort](https://developer.apple.com/documentation/foundation/nsconnection/1478071-sendport)Added [NSConnection.statistics](https://developer.apple.com/documentation/foundation/nsconnection/1478112-statistics)Added [NSConnection.valid](https://developer.apple.com/documentation/foundation/nsconnection/1478063-valid)Added [NSDistantObjectRequest.connection](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/1478073-connection)Added [NSDistantObjectRequest.conversation](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/1478098-conversation)Added [NSDistantObjectRequest.invocation](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/1478018-invocation)Modified [+[NSConnection connectionWithReceivePort:sendPort:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/clm/NSConnection/connectionWithReceivePort:sendPort:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)connectionWithReceivePort:(NSPort *)receivePort sendPort:(NSPort *)sendPort ``` |
| To | ``` + (instancetype)connectionWithReceivePort:(NSPort *)receivePort sendPort:(NSPort *)sendPort ``` |

Modified [+[NSConnection connectionWithRegisteredName:host:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/clm/NSConnection/connectionWithRegisteredName:host:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)connectionWithRegisteredName:(NSString *)name host:(NSString *)hostName ``` |
| To | ``` + (instancetype)connectionWithRegisteredName:(NSString *)name host:(NSString *)hostName ``` |

Modified [+[NSConnection connectionWithRegisteredName:host:usingNameServer:]](https://developer.apple.com/documentation/foundation/nsconnection/1478087-connectionwithregisteredname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)connectionWithRegisteredName:(NSString *)name host:(NSString *)hostName usingNameServer:(NSPortNameServer *)server ``` |
| To | ``` + (instancetype)connectionWithRegisteredName:(NSString *)name host:(NSString *)hostName usingNameServer:(NSPortNameServer *)server ``` |

Modified [-[NSConnection initWithReceivePort:sendPort:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/instm/NSConnection/initWithReceivePort:sendPort:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithReceivePort:(NSPort *)receivePort sendPort:(NSPort *)sendPort ``` |
| To | ``` - (instancetype)initWithReceivePort:(NSPort *)receivePort sendPort:(NSPort *)sendPort ``` |

Modified [+[NSConnection serviceConnectionWithName:rootObject:]](https://developer.apple.com/documentation/foundation/nsconnection/1478059-serviceconnectionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)serviceConnectionWithName:(NSString *)name rootObject:(id)root ``` |
| To | ``` + (instancetype)serviceConnectionWithName:(NSString *)name rootObject:(id)root ``` |

Modified [+[NSConnection serviceConnectionWithName:rootObject:usingNameServer:]](https://developer.apple.com/documentation/foundation/nsconnection/1478013-serviceconnectionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)serviceConnectionWithName:(NSString *)name rootObject:(id)root usingNameServer:(NSPortNameServer *)server ``` |
| To | ``` + (instancetype)serviceConnectionWithName:(NSString *)name rootObject:(id)root usingNameServer:(NSPortNameServer *)server ``` |

Modified [-[NSConnectionDelegate authenticateComponents:withData:]](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/1478108-authenticatecomponents)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSConnectionDelegate authenticationDataForComponents:]](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/1478039-authenticationdataforcomponents)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSConnectionDelegate connection:handleRequest:]](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/1478016-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSConnectionDelegate connection:shouldMakeNewConnection:]](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/1478045-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSConnectionDelegate createConversationForConnection:]](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/1478106-createconversationforconnection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSConnectionDelegate makeNewConnection:sender:]](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/1478057-makenewconnection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSData.hRemoved [-[NSData bytes]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/bytes)Removed [-[NSData description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/description)Removed [-[NSData length]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/length)Removed [-[NSMutableData mutableBytes]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/mutableBytes)Removed [-[NSMutableData setLength:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/setLength:)Added [NSData.bytes](https://developer.apple.com/documentation/foundation/nsdata/1410616-bytes)Added [NSData.description](https://developer.apple.com/documentation/foundation/nsdata/1412579-description)Added [NSData.length](https://developer.apple.com/documentation/foundation/nsdata/1416769-length)Added [NSMutableData.length](https://developer.apple.com/documentation/foundation/nsmutabledata/1413333-length)Added [NSMutableData.mutableBytes](https://developer.apple.com/documentation/foundation/nsmutabledata/1410770-mutablebytes)Modified [+[NSData data]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/data)

|  | Declaration |
| --- | --- |
| From | ``` + (id)data ``` |
| To | ``` + (instancetype)data ``` |

Modified [+[NSData dataWithBytes:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithBytes:length:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithBytes:(const void *)bytes length:(NSUInteger)length ``` |
| To | ``` + (instancetype)dataWithBytes:(const void *)bytes length:(NSUInteger)length ``` |

Modified [+[NSData dataWithBytesNoCopy:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithBytesNoCopy:length:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithBytesNoCopy:(void *)bytes length:(NSUInteger)length ``` |
| To | ``` + (instancetype)dataWithBytesNoCopy:(void *)bytes length:(NSUInteger)length ``` |

Modified [+[NSData dataWithBytesNoCopy:length:freeWhenDone:]](https://developer.apple.com/documentation/foundation/nsdata/1547240-datawithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithBytesNoCopy:(void *)bytes length:(NSUInteger)length freeWhenDone:(BOOL)b ``` |
| To | ``` + (instancetype)dataWithBytesNoCopy:(void *)bytes length:(NSUInteger)length freeWhenDone:(BOOL)b ``` |

Modified [+[NSData dataWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithContentsOfFile:(NSString *)path ``` |
| To | ``` + (instancetype)dataWithContentsOfFile:(NSString *)path ``` |

Modified [+[NSData dataWithContentsOfFile:options:error:]](https://developer.apple.com/documentation/foundation/nsdata/1547244-datawithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithContentsOfFile:(NSString *)path options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |
| To | ``` + (instancetype)dataWithContentsOfFile:(NSString *)path options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |

Modified [+[NSData dataWithContentsOfMappedFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithContentsOfMappedFile:)

|  | Deprecation |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.10 |

Modified [+[NSData dataWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsdata/1547245-datawithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (instancetype)dataWithContentsOfURL:(NSURL *)url ``` |

Modified [+[NSData dataWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/foundation/nsdata/1547238-datawithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithContentsOfURL:(NSURL *)url options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |
| To | ``` + (instancetype)dataWithContentsOfURL:(NSURL *)url options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |

Modified [+[NSData dataWithData:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithData:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithData:(NSData *)data ``` |
| To | ``` + (instancetype)dataWithData:(NSData *)data ``` |

Modified [-[NSData getBytes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/getBytes:)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSData initWithBase64EncodedData:options:]](https://developer.apple.com/documentation/foundation/nsdata/1417833-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBase64EncodedData:(NSData *)base64Data options:(NSDataBase64DecodingOptions)options ``` |
| To | ``` - (instancetype)initWithBase64EncodedData:(NSData *)base64Data options:(NSDataBase64DecodingOptions)options ``` |

Modified [-[NSData initWithBase64EncodedString:options:]](https://developer.apple.com/documentation/foundation/nsdata/1410081-initwithbase64encodedstring)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBase64EncodedString:(NSString *)base64String options:(NSDataBase64DecodingOptions)options ``` |
| To | ``` - (instancetype)initWithBase64EncodedString:(NSString *)base64String options:(NSDataBase64DecodingOptions)options ``` |

Modified [-[NSData initWithBytes:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/initWithBytes:length:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBytes:(const void *)bytes length:(NSUInteger)length ``` |
| To | ``` - (instancetype)initWithBytes:(const void *)bytes length:(NSUInteger)length ``` |

Modified [-[NSData initWithBytesNoCopy:length:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/initWithBytesNoCopy:length:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBytesNoCopy:(void *)bytes length:(NSUInteger)length ``` |
| To | ``` - (instancetype)initWithBytesNoCopy:(void *)bytes length:(NSUInteger)length ``` |

Modified [-[NSData initWithBytesNoCopy:length:deallocator:]](https://developer.apple.com/documentation/foundation/nsdata/1417337-initwithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBytesNoCopy:(void *)bytes length:(NSUInteger)length deallocator:(void (^)(void *bytes, NSUInteger length))deallocator ``` |
| To | ``` - (instancetype)initWithBytesNoCopy:(void *)bytes length:(NSUInteger)length deallocator:(void (^)(void *bytes, NSUInteger length))deallocator ``` |

Modified [-[NSData initWithBytesNoCopy:length:freeWhenDone:]](https://developer.apple.com/documentation/foundation/nsdata/1416020-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBytesNoCopy:(void *)bytes length:(NSUInteger)length freeWhenDone:(BOOL)b ``` |
| To | ``` - (instancetype)initWithBytesNoCopy:(void *)bytes length:(NSUInteger)length freeWhenDone:(BOOL)b ``` |

Modified [-[NSData initWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/initWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (instancetype)initWithContentsOfFile:(NSString *)path ``` |

Modified [-[NSData initWithContentsOfFile:options:error:]](https://developer.apple.com/documentation/foundation/nsdata/1411145-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfFile:(NSString *)path options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |
| To | ``` - (instancetype)initWithContentsOfFile:(NSString *)path options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |

Modified [-[NSData initWithContentsOfMappedFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/initWithContentsOfMappedFile:)

|  | Deprecation |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.10 |

Modified [-[NSData initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsdata/1413892-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |

Modified [-[NSData initWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/foundation/nsdata/1407864-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url options:(NSDataReadingOptions)readOptionsMask error:(NSError **)errorPtr ``` |

Modified [-[NSData initWithData:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/initWithData:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [+[NSMutableData dataWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSMutableData/dataWithCapacity:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithCapacity:(NSUInteger)aNumItems ``` |
| To | ``` + (instancetype)dataWithCapacity:(NSUInteger)aNumItems ``` |

Modified [+[NSMutableData dataWithLength:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSMutableData/dataWithLength:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dataWithLength:(NSUInteger)length ``` |
| To | ``` + (instancetype)dataWithLength:(NSUInteger)length ``` |

Modified [-[NSMutableData initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCapacity:(NSUInteger)capacity ``` |
| To | ``` - (instancetype)initWithCapacity:(NSUInteger)capacity ``` |

Modified [-[NSMutableData initWithLength:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/initWithLength:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLength:(NSUInteger)length ``` |
| To | ``` - (instancetype)initWithLength:(NSUInteger)length ``` |

NSDate.hRemoved [-[NSDate description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/description)Removed [-[NSDate timeIntervalSince1970]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/timeIntervalSince1970)Removed [-[NSDate timeIntervalSinceNow]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/timeIntervalSinceNow)Removed [-[NSDate timeIntervalSinceReferenceDate]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/timeIntervalSinceReferenceDate)Added [NSDate.description](https://developer.apple.com/documentation/foundation/nsdate/1409767-description)Added [-[NSDate initWithCoder:]](https://developer.apple.com/documentation/foundation/nsdate/1412602-initwithcoder)Added [NSDate.timeIntervalSince1970](https://developer.apple.com/documentation/foundation/nsdate/1407504-timeintervalsince1970)Added [NSDate.timeIntervalSinceNow](https://developer.apple.com/documentation/foundation/nsdate/1407937-timeintervalsincenow)Added [NSDate.timeIntervalSinceReferenceDate](https://developer.apple.com/documentation/foundation/nsdate/1417376-timeintervalsincereferencedate)Modified [-[NSDate dateByAddingTimeInterval:]](https://developer.apple.com/documentation/foundation/nsdate/1408823-addingtimeinterval)

|  | Declaration |
| --- | --- |
| From | ``` - (id)dateByAddingTimeInterval:(NSTimeInterval)ti ``` |
| To | ``` - (instancetype)dateByAddingTimeInterval:(NSTimeInterval)ti ``` |

Modified [-[NSDate init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDate initWithTimeIntervalSinceReferenceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeIntervalSinceReferenceDate:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDateComponentsFormatter.h (Added)Added [NSDateComponentsFormatter](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter)Added [NSDateComponentsFormatter.allowedUnits](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1410216-allowedunits)Added [NSDateComponentsFormatter.allowsFractionalUnits](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1413084-allowsfractionalunits)Added [NSDateComponentsFormatter.calendar](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1407359-calendar)Added [NSDateComponentsFormatter.collapsesLargestUnit](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1410812-collapseslargestunit)Added [NSDateComponentsFormatter.formattingContext](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter/1414198-formattingcontext)Added [-[NSDateComponentsFormatter getObjectValue:forString:errorDescription:]](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1412149-getobjectvalue)Added [NSDateComponentsFormatter.includesApproximationPhrase](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter/1416387-includesapproximationphrase)Added [NSDateComponentsFormatter.includesTimeRemainingPhrase](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter/1416416-includestimeremainingphrase)Added [+[NSDateComponentsFormatter localizedStringFromDateComponents:unitsStyle:]](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1411422-localizedstring)Added [NSDateComponentsFormatter.maximumUnitCount](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter/1416214-maximumunitcount)Added [-[NSDateComponentsFormatter stringForObjectValue:]](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1417219-string)Added [-[NSDateComponentsFormatter stringFromDate:toDate:]](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter/1415967-stringfromdate)Added [-[NSDateComponentsFormatter stringFromDateComponents:]](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter/1407641-stringfromdatecomponents)Added [-[NSDateComponentsFormatter stringFromTimeInterval:]](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1409040-string)Added [NSDateComponentsFormatter.unitsStyle](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatter/1413441-unitsstyle)Added [NSDateComponentsFormatter.zeroFormattingBehavior](https://developer.apple.com/documentation/foundation/datecomponentsformatter/1413749-zeroformattingbehavior)Added [NSDateComponentsFormatterUnitsStyle](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle)Added [NSDateComponentsFormatterUnitsStyleAbbreviated](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterunitsstyle/nsdatecomponentsformatterunitsstyleabbreviated)Added [NSDateComponentsFormatterUnitsStyleFull](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterunitsstyle/nsdatecomponentsformatterunitsstylefull)Added [NSDateComponentsFormatterUnitsStylePositional](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterunitsstyle/nsdatecomponentsformatterunitsstylepositional)Added [NSDateComponentsFormatterUnitsStyleShort](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterunitsstyle/nsdatecomponentsformatterunitsstyleshort)Added [NSDateComponentsFormatterUnitsStyleSpellOut](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterunitsstyle/nsdatecomponentsformatterunitsstylespellout)Added [NSDateComponentsFormatterZeroFormattingBehavior](https://developer.apple.com/documentation/foundation/datecomponentsformatter/zeroformattingbehavior)Added [NSDateComponentsFormatterZeroFormattingBehaviorDefault](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterzeroformattingbehavior/nsdatecomponentsformatterzeroformattingbehaviordefault)Added [NSDateComponentsFormatterZeroFormattingBehaviorDropAll](https://developer.apple.com/documentation/foundation/datecomponentsformatter/zeroformattingbehavior/1409787-dropall)Added [NSDateComponentsFormatterZeroFormattingBehaviorDropLeading](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterzeroformattingbehavior/nsdatecomponentsformatterzeroformattingbehaviordropleading)Added [NSDateComponentsFormatterZeroFormattingBehaviorDropMiddle](https://developer.apple.com/documentation/foundation/datecomponentsformatter/zeroformattingbehavior/1412863-dropmiddle)Added [NSDateComponentsFormatterZeroFormattingBehaviorDropTrailing](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterzeroformattingbehavior/nsdatecomponentsformatterzeroformattingbehaviordroptrailing)Added [NSDateComponentsFormatterZeroFormattingBehaviorNone](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterzeroformattingbehavior/nsdatecomponentsformatterzeroformattingbehaviornone)Added [NSDateComponentsFormatterZeroFormattingBehaviorPad](https://developer.apple.com/documentation/foundation/nsdatecomponentsformatterzeroformattingbehavior/nsdatecomponentsformatterzeroformattingbehaviorpad)NSDateFormatter.hRemoved [-[NSDateFormatter AMSymbol]](https://developer.apple.com/documentation/foundation/dateformatter/1409506-amsymbol)Removed [-[NSDateFormatter PMSymbol]](https://developer.apple.com/documentation/foundation/nsdateformatter/1412367-pmsymbol)Removed [-[NSDateFormatter calendar]](https://developer.apple.com/documentation/foundation/nsdateformatter/1413675-calendar)Removed [-[NSDateFormatter dateFormat]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateFormatter/Description.html#//apple_ref/occ/instm/NSDateFormatter/dateFormat)Removed [-[NSDateFormatter dateStyle]](https://developer.apple.com/documentation/foundation/nsdateformatter/1415411-datestyle)Removed [-[NSDateFormatter defaultDate]](https://developer.apple.com/documentation/foundation/nsdateformatter/1408312-defaultdate)Removed [-[NSDateFormatter doesRelativeDateFormatting]](https://developer.apple.com/documentation/foundation/nsdateformatter/1415848-doesrelativedateformatting)Removed [-[NSDateFormatter eraSymbols]](https://developer.apple.com/documentation/foundation/dateformatter/1418282-erasymbols)Removed [-[NSDateFormatter formatterBehavior]](https://developer.apple.com/documentation/foundation/dateformatter/1409720-formatterbehavior)Removed [-[NSDateFormatter generatesCalendarDates]](https://developer.apple.com/documentation/foundation/dateformatter/1411107-generatescalendardates)Removed [-[NSDateFormatter gregorianStartDate]](https://developer.apple.com/documentation/foundation/nsdateformatter/1416389-gregorianstartdate)Removed [-[NSDateFormatter isLenient]](https://developer.apple.com/documentation/foundation/nsdateformatter/1411441-lenient)Removed [-[NSDateFormatter locale]](https://developer.apple.com/documentation/foundation/nsdateformatter/1411973-locale)Removed [-[NSDateFormatter longEraSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1418081-longerasymbols)Removed [-[NSDateFormatter monthSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1412049-monthsymbols)Removed [-[NSDateFormatter quarterSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1417587-quartersymbols)Removed [-[NSDateFormatter setAMSymbol:]](https://developer.apple.com/documentation/foundation/dateformatter/1409506-amsymbol)Removed [-[NSDateFormatter setCalendar:]](https://developer.apple.com/documentation/foundation/dateformatter/1413675-calendar)Removed [-[NSDateFormatter setDateFormat:]](https://developer.apple.com/documentation/foundation/dateformatter/1413514-dateformat)Removed [-[NSDateFormatter setDateStyle:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1415411-datestyle)Removed [-[NSDateFormatter setDefaultDate:]](https://developer.apple.com/documentation/foundation/dateformatter/1408312-defaultdate)Removed [-[NSDateFormatter setDoesRelativeDateFormatting:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1415848-doesrelativedateformatting)Removed [-[NSDateFormatter setEraSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1418282-erasymbols)Removed [-[NSDateFormatter setFormatterBehavior:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1409720-formatterbehavior)Removed [-[NSDateFormatter setGeneratesCalendarDates:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1411107-generatescalendardates)Removed [-[NSDateFormatter setGregorianStartDate:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1416389-gregorianstartdate)Removed [-[NSDateFormatter setLenient:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1411441-lenient)Removed [-[NSDateFormatter setLocale:]](https://developer.apple.com/documentation/foundation/dateformatter/1411973-locale)Removed [-[NSDateFormatter setLongEraSymbols:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1418081-longerasymbols)Removed [-[NSDateFormatter setMonthSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1412049-monthsymbols)Removed [-[NSDateFormatter setPMSymbol:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1412367-pmsymbol)Removed [-[NSDateFormatter setQuarterSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1417587-quartersymbols)Removed [-[NSDateFormatter setShortMonthSymbols:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1409209-shortmonthsymbols)Removed [-[NSDateFormatter setShortQuarterSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1409851-shortquartersymbols)Removed [-[NSDateFormatter setShortStandaloneMonthSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1414771-shortstandalonemonthsymbols)Removed [-[NSDateFormatter setShortStandaloneQuarterSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1416421-shortstandalonequartersymbols)Removed [-[NSDateFormatter setShortStandaloneWeekdaySymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1409119-shortstandaloneweekdaysymbols)Removed [-[NSDateFormatter setShortWeekdaySymbols:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1416121-shortweekdaysymbols)Removed [-[NSDateFormatter setStandaloneMonthSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1416227-standalonemonthsymbols)Removed [-[NSDateFormatter setStandaloneQuarterSymbols:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1411487-standalonequartersymbols)Removed [-[NSDateFormatter setStandaloneWeekdaySymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1413618-standaloneweekdaysymbols)Removed [-[NSDateFormatter setTimeStyle:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1413467-timestyle)Removed [-[NSDateFormatter setTimeZone:]](https://developer.apple.com/documentation/foundation/dateformatter/1411406-timezone)Removed [-[NSDateFormatter setTwoDigitStartDate:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1417203-twodigitstartdate)Removed [-[NSDateFormatter setVeryShortMonthSymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1413632-veryshortmonthsymbols)Removed [-[NSDateFormatter setVeryShortStandaloneMonthSymbols:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1413322-veryshortstandalonemonthsymbols)Removed [-[NSDateFormatter setVeryShortStandaloneWeekdaySymbols:]](https://developer.apple.com/documentation/foundation/dateformatter/1418238-veryshortstandaloneweekdaysymbol)Removed [-[NSDateFormatter setVeryShortWeekdaySymbols:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1415109-veryshortweekdaysymbols)Removed [-[NSDateFormatter setWeekdaySymbols:]](https://developer.apple.com/documentation/foundation/nsdateformatter/1412405-weekdaysymbols)Removed [-[NSDateFormatter shortMonthSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1409209-shortmonthsymbols)Removed [-[NSDateFormatter shortQuarterSymbols]](https://developer.apple.com/documentation/foundation/dateformatter/1409851-shortquartersymbols)Removed [-[NSDateFormatter shortStandaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1414771-shortstandalonemonthsymbols)Removed [-[NSDateFormatter shortStandaloneQuarterSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1416421-shortstandalonequartersymbols)Removed [-[NSDateFormatter shortStandaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/dateformatter/1409119-shortstandaloneweekdaysymbols)Removed [-[NSDateFormatter shortWeekdaySymbols]](https://developer.apple.com/documentation/foundation/dateformatter/1416121-shortweekdaysymbols)Removed [-[NSDateFormatter standaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1416227-standalonemonthsymbols)Removed [-[NSDateFormatter standaloneQuarterSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1411487-standalonequartersymbols)Removed [-[NSDateFormatter standaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/dateformatter/1413618-standaloneweekdaysymbols)Removed [-[NSDateFormatter timeStyle]](https://developer.apple.com/documentation/foundation/nsdateformatter/1413467-timestyle)Removed [-[NSDateFormatter timeZone]](https://developer.apple.com/documentation/foundation/nsdateformatter/1411406-timezone)Removed [-[NSDateFormatter twoDigitStartDate]](https://developer.apple.com/documentation/foundation/dateformatter/1417203-twodigitstartdate)Removed [-[NSDateFormatter veryShortMonthSymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1413632-veryshortmonthsymbols)Removed [-[NSDateFormatter veryShortStandaloneMonthSymbols]](https://developer.apple.com/documentation/foundation/dateformatter/1413322-veryshortstandalonemonthsymbols)Removed [-[NSDateFormatter veryShortStandaloneWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1418238-veryshortstandaloneweekdaysymbol)Removed [-[NSDateFormatter veryShortWeekdaySymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1415109-veryshortweekdaysymbols)Removed [-[NSDateFormatter weekdaySymbols]](https://developer.apple.com/documentation/foundation/nsdateformatter/1412405-weekdaysymbols)Added [NSDateFormatter.AMSymbol](https://developer.apple.com/documentation/foundation/dateformatter/1409506-amsymbol)Added [NSDateFormatter.PMSymbol](https://developer.apple.com/documentation/foundation/nsdateformatter/1412367-pmsymbol)Added [NSDateFormatter.calendar](https://developer.apple.com/documentation/foundation/dateformatter/1413675-calendar)Added [NSDateFormatter.dateFormat](https://developer.apple.com/documentation/foundation/nsdateformatter/1413514-dateformat)Added [NSDateFormatter.dateStyle](https://developer.apple.com/documentation/foundation/dateformatter/1415411-datestyle)Added [NSDateFormatter.defaultDate](https://developer.apple.com/documentation/foundation/dateformatter/1408312-defaultdate)Added [NSDateFormatter.doesRelativeDateFormatting](https://developer.apple.com/documentation/foundation/dateformatter/1415848-doesrelativedateformatting)Added [NSDateFormatter.eraSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1418282-erasymbols)Added [NSDateFormatter.formatterBehavior](https://developer.apple.com/documentation/foundation/dateformatter/1409720-formatterbehavior)Added [NSDateFormatter.formattingContext](https://developer.apple.com/documentation/foundation/dateformatter/1408066-formattingcontext)Added [NSDateFormatter.generatesCalendarDates](https://developer.apple.com/documentation/foundation/nsdateformatter/1411107-generatescalendardates)Added [NSDateFormatter.gregorianStartDate](https://developer.apple.com/documentation/foundation/dateformatter/1416389-gregorianstartdate)Added [NSDateFormatter.lenient](https://developer.apple.com/documentation/foundation/dateformatter/1411441-islenient)Added [NSDateFormatter.locale](https://developer.apple.com/documentation/foundation/nsdateformatter/1411973-locale)Added [NSDateFormatter.longEraSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1418081-longerasymbols)Added [NSDateFormatter.monthSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1412049-monthsymbols)Added [NSDateFormatter.quarterSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1417587-quartersymbols)Added [-[NSDateFormatter setLocalizedDateFormatFromTemplate:]](https://developer.apple.com/documentation/foundation/dateformatter/1417087-setlocalizeddateformatfromtempla)Added [NSDateFormatter.shortMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1409209-shortmonthsymbols)Added [NSDateFormatter.shortQuarterSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1409851-shortquartersymbols)Added [NSDateFormatter.shortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1414771-shortstandalonemonthsymbols)Added [NSDateFormatter.shortStandaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1416421-shortstandalonequartersymbols)Added [NSDateFormatter.shortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1409119-shortstandaloneweekdaysymbols)Added [NSDateFormatter.shortWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1416121-shortweekdaysymbols)Added [NSDateFormatter.standaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1416227-standalonemonthsymbols)Added [NSDateFormatter.standaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1411487-standalonequartersymbols)Added [NSDateFormatter.standaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1413618-standaloneweekdaysymbols)Added [NSDateFormatter.timeStyle](https://developer.apple.com/documentation/foundation/nsdateformatter/1413467-timestyle)Added [NSDateFormatter.timeZone](https://developer.apple.com/documentation/foundation/dateformatter/1411406-timezone)Added [NSDateFormatter.twoDigitStartDate](https://developer.apple.com/documentation/foundation/dateformatter/1417203-twodigitstartdate)Added [NSDateFormatter.veryShortMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1413632-veryshortmonthsymbols)Added [NSDateFormatter.veryShortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1413322-veryshortstandalonemonthsymbols)Added [NSDateFormatter.veryShortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1418238-veryshortstandaloneweekdaysymbol)Added [NSDateFormatter.veryShortWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1415109-veryshortweekdaysymbols)Added [NSDateFormatter.weekdaySymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1412405-weekdaysymbols)Modified [-[NSDateFormatter allowsNaturalLanguage]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateFormatter/Description.html#//apple_ref/occ/instm/NSDateFormatter/allowsNaturalLanguage)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [-[NSDateFormatter initWithDateFormat:allowNaturalLanguage:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateFormatter/Description.html#//apple_ref/occ/instm/NSDateFormatter/initWithDateFormat:allowNaturalLanguage:)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

NSDateIntervalFormatter.h (Added)Added [NSDateIntervalFormatter](https://developer.apple.com/documentation/foundation/dateintervalformatter)Added [NSDateIntervalFormatter.calendar](https://developer.apple.com/documentation/foundation/dateintervalformatter/1417984-calendar)Added [NSDateIntervalFormatter.dateStyle](https://developer.apple.com/documentation/foundation/nsdateintervalformatter/1409519-datestyle)Added [NSDateIntervalFormatter.dateTemplate](https://developer.apple.com/documentation/foundation/dateintervalformatter/1407373-datetemplate)Added [NSDateIntervalFormatter.locale](https://developer.apple.com/documentation/foundation/nsdateintervalformatter/1409992-locale)Added [-[NSDateIntervalFormatter stringFromDate:toDate:]](https://developer.apple.com/documentation/foundation/dateintervalformatter/1418368-string)Added [NSDateIntervalFormatter.timeStyle](https://developer.apple.com/documentation/foundation/dateintervalformatter/1415655-timestyle)Added [NSDateIntervalFormatter.timeZone](https://developer.apple.com/documentation/foundation/dateintervalformatter/1410228-timezone)Added [NSDateIntervalFormatterFullStyle](https://developer.apple.com/documentation/foundation/dateintervalformatter/style/full)Added [NSDateIntervalFormatterLongStyle](https://developer.apple.com/documentation/foundation/nsdateintervalformatterstyle/nsdateintervalformatterlongstyle)Added [NSDateIntervalFormatterMediumStyle](https://developer.apple.com/documentation/foundation/dateintervalformatter/style/medium)Added [NSDateIntervalFormatterNoStyle](https://developer.apple.com/documentation/foundation/nsdateintervalformatterstyle/nsdateintervalformatternostyle)Added [NSDateIntervalFormatterShortStyle](https://developer.apple.com/documentation/foundation/dateintervalformatter/style/short)Added [NSDateIntervalFormatterStyle](https://developer.apple.com/documentation/foundation/nsdateintervalformatterstyle)NSDecimalNumber.hRemoved [-[NSDecimalNumber decimalValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/decimalValue)Removed [-[NSDecimalNumber doubleValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/doubleValue)Removed [-[NSDecimalNumber objCType]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/objCType)Removed [-[NSNumber decimalValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/decimalValue)Added [NSDecimalNumber.decimalValue](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1409664-decimalvalue)Added [NSDecimalNumber.doubleValue](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1407569-doublevalue)Added [NSDecimalNumber.objCType](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1409042-objctype)Added [NSNumber.decimalValue](https://developer.apple.com/documentation/foundation/nsnumber/1407409-decimalvalue)Modified [-[NSDecimalNumber initWithDecimal:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/initWithDecimal:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithDecimal:(NSDecimal)dcm ``` | -- |
| To | ``` - (instancetype)initWithDecimal:(NSDecimal)dcm ``` | yes |

Modified [-[NSDecimalNumber initWithMantissa:exponent:isNegative:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/initWithMantissa:exponent:isNegative:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMantissa:(unsigned long long)mantissa exponent:(short)exponent isNegative:(BOOL)flag ``` |
| To | ``` - (instancetype)initWithMantissa:(unsigned long long)mantissa exponent:(short)exponent isNegative:(BOOL)flag ``` |

Modified [-[NSDecimalNumber initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/initWithString:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithString:(NSString *)numberValue ``` |
| To | ``` - (instancetype)initWithString:(NSString *)numberValue ``` |

Modified [-[NSDecimalNumber initWithString:locale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/initWithString:locale:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithString:(NSString *)numberValue locale:(id)locale ``` |
| To | ``` - (instancetype)initWithString:(NSString *)numberValue locale:(id)locale ``` |

Modified [+[NSDecimalNumberHandler decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumberHandler/Description.html#//apple_ref/occ/clm/NSDecimalNumberHandler/decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)decimalNumberHandlerWithRoundingMode:(NSRoundingMode)roundingMode scale:(short)scale raiseOnExactness:(BOOL)exact raiseOnOverflow:(BOOL)overflow raiseOnUnderflow:(BOOL)underflow raiseOnDivideByZero:(BOOL)divideByZero ``` |
| To | ``` + (instancetype)decimalNumberHandlerWithRoundingMode:(NSRoundingMode)roundingMode scale:(short)scale raiseOnExactness:(BOOL)exact raiseOnOverflow:(BOOL)overflow raiseOnUnderflow:(BOOL)underflow raiseOnDivideByZero:(BOOL)divideByZero ``` |

Modified [+[NSDecimalNumberHandler defaultDecimalNumberHandler]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumberHandler/Description.html#//apple_ref/occ/clm/NSDecimalNumberHandler/defaultDecimalNumberHandler)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultDecimalNumberHandler ``` |
| To | ``` + (NSDecimalNumberHandler *)defaultDecimalNumberHandler ``` |

Modified [-[NSDecimalNumberHandler initWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumberHandler/Description.html#//apple_ref/occ/instm/NSDecimalNumberHandler/initWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithRoundingMode:(NSRoundingMode)roundingMode scale:(short)scale raiseOnExactness:(BOOL)exact raiseOnOverflow:(BOOL)overflow raiseOnUnderflow:(BOOL)underflow raiseOnDivideByZero:(BOOL)divideByZero ``` | -- |
| To | ``` - (instancetype)initWithRoundingMode:(NSRoundingMode)roundingMode scale:(short)scale raiseOnExactness:(BOOL)exact raiseOnOverflow:(BOOL)overflow raiseOnUnderflow:(BOOL)underflow raiseOnDivideByZero:(BOOL)divideByZero ``` | yes |

NSDictionary.hRemoved [-[NSDictionary allKeys]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/allKeys)Removed [-[NSDictionary allValues]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/allValues)Removed [-[NSDictionary count]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/count)Removed [-[NSDictionary description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/description)Removed [-[NSDictionary descriptionInStringsFileFormat]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/descriptionInStringsFileFormat)Added [NSDictionary.allKeys](https://developer.apple.com/documentation/foundation/nsdictionary/1409150-allkeys)Added [NSDictionary.allValues](https://developer.apple.com/documentation/foundation/nsdictionary/1408915-allvalues)Added [NSDictionary.count](https://developer.apple.com/documentation/foundation/nsdictionary/1409628-count)Added [NSDictionary.description](https://developer.apple.com/documentation/foundation/nsdictionary/1410799-description)Added [NSDictionary.descriptionInStringsFileFormat](https://developer.apple.com/documentation/foundation/nsdictionary/1413282-descriptioninstringsfileformat)Added [-[NSDictionary initWithCoder:]](https://developer.apple.com/documentation/foundation/nsdictionary/1417987-init)Added [+[NSMutableDictionary dictionaryWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1574188-dictionarywithcontentsoffile)Added [+[NSMutableDictionary dictionaryWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1574182-dictionarywithcontentsofurl)Added [-[NSMutableDictionary initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1418255-initwithcoder)Added [-[NSMutableDictionary initWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1407593-initwithcontentsoffile)Added [-[NSMutableDictionary initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1410409-initwithcontentsofurl)Modified [+[NSDictionary dictionaryWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dictionaryWithContentsOfFile:(NSString *)path ``` |
| To | ``` + (NSDictionary *)dictionaryWithContentsOfFile:(NSString *)path ``` |

Modified [+[NSDictionary dictionaryWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsdictionary/1574185-dictionarywithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dictionaryWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (NSDictionary *)dictionaryWithContentsOfURL:(NSURL *)url ``` |

Modified [-[NSDictionary init]](https://developer.apple.com/documentation/foundation/nsdictionary/1418147-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDictionary initWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (NSDictionary *)initWithContentsOfFile:(NSString *)path ``` |

Modified [-[NSDictionary initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsdictionary/1416069-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (NSDictionary *)initWithContentsOfURL:(NSURL *)url ``` |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [+[NSMutableDictionary dictionaryWithSharedKeySet:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1412658-dictionarywithsharedkeyset)

|  | Declaration |
| --- | --- |
| From | ``` + (id)dictionaryWithSharedKeySet:(id)keyset ``` |
| To | ``` + (NSMutableDictionary *)dictionaryWithSharedKeySet:(id)keyset ``` |

Modified [-[NSMutableDictionary init]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1410577-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableDictionary initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/initWithCapacity:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDistantObject.hRemoved [-[NSDistantObject connectionForProxy]](https://developer.apple.com/documentation/foundation/nsdistantobject/1806839-connectionforproxy)Added [NSDistantObject.connectionForProxy](https://developer.apple.com/documentation/foundation/nsdistantobject/1442598-connectionforproxy)Added [-[NSDistantObject initWithCoder:]](https://developer.apple.com/documentation/foundation/nsdistantobject/1442605-initwithcoder)Modified [-[NSDistantObject initWithLocal:connection:]](https://developer.apple.com/documentation/foundation/nsdistantobject/1442603-initwithlocal)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLocal:(id)target connection:(NSConnection *)connection ``` |
| To | ``` - (instancetype)initWithLocal:(id)target connection:(NSConnection *)connection ``` |

Modified [-[NSDistantObject initWithTarget:connection:]](https://developer.apple.com/documentation/foundation/nsdistantobject/1442597-initwithtarget)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTarget:(id)target connection:(NSConnection *)connection ``` |
| To | ``` - (instancetype)initWithTarget:(id)target connection:(NSConnection *)connection ``` |

Modified [+[NSDistantObject proxyWithLocal:connection:]](https://developer.apple.com/documentation/foundation/nsdistantobject/1442601-proxywithlocal)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDistantObject *)proxyWithLocal:(id)target connection:(NSConnection *)connection ``` |
| To | ``` + (id)proxyWithLocal:(id)target connection:(NSConnection *)connection ``` |

Modified [+[NSDistantObject proxyWithTarget:connection:]](https://developer.apple.com/documentation/foundation/nsdistantobject/1442599-proxywithtarget)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDistantObject *)proxyWithTarget:(id)target connection:(NSConnection *)connection ``` |
| To | ``` + (id)proxyWithTarget:(id)target connection:(NSConnection *)connection ``` |

NSDistributedLock.hRemoved [-[NSDistributedLock lockDate]](https://developer.apple.com/documentation/foundation/nsdistributedlock/1413773-lockdate)Added [NSDistributedLock.lockDate](https://developer.apple.com/documentation/foundation/nsdistributedlock/1413773-lockdate)Modified [-[NSDistributedLock initWithPath:]](https://developer.apple.com/documentation/foundation/nsdistributedlock/1410387-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithPath:(NSString *)path ``` | -- |
| To | ``` - (instancetype)initWithPath:(NSString *)path ``` | yes |

NSDistributedNotificationCenter.hRemoved [-[NSDistributedNotificationCenter setSuspended:]](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter/1407301-suspended)Removed [-[NSDistributedNotificationCenter suspended]](https://developer.apple.com/documentation/foundation/distributednotificationcenter/1407301-suspended)Added [NSDistributedNotificationCenter.suspended](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter/1407301-suspended)Modified [+[NSDistributedNotificationCenter defaultCenter]](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter/1412063-defaultcenter)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultCenter ``` |
| To | ``` + (NSDistributedNotificationCenter *)defaultCenter ``` |

NSEnergyFormatter.h (Added)Added [NSEnergyFormatter](https://developer.apple.com/documentation/foundation/energyformatter)Added [NSEnergyFormatter.forFoodEnergyUse](https://developer.apple.com/documentation/foundation/nsenergyformatter/1410338-forfoodenergyuse)Added [-[NSEnergyFormatter getObjectValue:forString:errorDescription:]](https://developer.apple.com/documentation/foundation/energyformatter/1414825-getobjectvalue)Added [NSEnergyFormatter.numberFormatter](https://developer.apple.com/documentation/foundation/energyformatter/1412614-numberformatter)Added [-[NSEnergyFormatter stringFromJoules:]](https://developer.apple.com/documentation/foundation/energyformatter/1409502-string)Added [-[NSEnergyFormatter stringFromValue:unit:]](https://developer.apple.com/documentation/foundation/energyformatter/1411983-string)Added [-[NSEnergyFormatter unitStringFromJoules:usedUnit:]](https://developer.apple.com/documentation/foundation/nsenergyformatter/1408656-unitstringfromjoules)Added [-[NSEnergyFormatter unitStringFromValue:unit:]](https://developer.apple.com/documentation/foundation/nsenergyformatter/1411180-unitstringfromvalue)Added [NSEnergyFormatter.unitStyle](https://developer.apple.com/documentation/foundation/nsenergyformatter/1414075-unitstyle)Added [NSEnergyFormatterUnit](https://developer.apple.com/documentation/foundation/nsenergyformatterunit)Added [NSEnergyFormatterUnitCalorie](https://developer.apple.com/documentation/foundation/energyformatter/unit/calorie)Added [NSEnergyFormatterUnitJoule](https://developer.apple.com/documentation/foundation/nsenergyformatterunit/nsenergyformatterunitjoule)Added [NSEnergyFormatterUnitKilocalorie](https://developer.apple.com/documentation/foundation/nsenergyformatterunit/nsenergyformatterunitkilocalorie)Added [NSEnergyFormatterUnitKilojoule](https://developer.apple.com/documentation/foundation/nsenergyformatterunit/nsenergyformatterunitkilojoule)NSEnumerator.hRemoved [-[NSEnumerator allObjects]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSEnumerator/Description.html#//apple_ref/occ/instm/NSEnumerator/allObjects)Added [NSEnumerator.allObjects](https://developer.apple.com/documentation/foundation/nsenumerator/1417755-allobjects)NSError.hRemoved [-[NSError code]](https://developer.apple.com/documentation/foundation/nserror/1409165-code)Removed [-[NSError domain]](https://developer.apple.com/documentation/foundation/nserror/1413924-domain)Removed [-[NSError helpAnchor]](https://developer.apple.com/documentation/foundation/nserror/1414718-helpanchor)Removed [-[NSError localizedDescription]](https://developer.apple.com/documentation/foundation/nserror/1414418-localizeddescription)Removed [-[NSError localizedFailureReason]](https://developer.apple.com/documentation/foundation/nserror/1412752-localizedfailurereason)Removed [-[NSError localizedRecoveryOptions]](https://developer.apple.com/documentation/foundation/nserror/1415950-localizedrecoveryoptions)Removed [-[NSError localizedRecoverySuggestion]](https://developer.apple.com/documentation/foundation/nserror/1407500-localizedrecoverysuggestion)Removed [-[NSError recoveryAttempter]](https://developer.apple.com/documentation/foundation/nserror/1408864-recoveryattempter)Removed [-[NSError userInfo]](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo)Added [NSError.code](https://developer.apple.com/documentation/foundation/nserror/1409165-code)Added [NSError.domain](https://developer.apple.com/documentation/foundation/nserror/1413924-domain)Added [NSError.helpAnchor](https://developer.apple.com/documentation/foundation/nserror/1414718-helpanchor)Added [NSError.localizedDescription](https://developer.apple.com/documentation/foundation/nserror/1414418-localizeddescription)Added [NSError.localizedFailureReason](https://developer.apple.com/documentation/foundation/nserror/1412752-localizedfailurereason)Added [NSError.localizedRecoveryOptions](https://developer.apple.com/documentation/foundation/nserror/1415950-localizedrecoveryoptions)Added [NSError.localizedRecoverySuggestion](https://developer.apple.com/documentation/foundation/nserror/1407500-localizedrecoverysuggestion)Added [NSError.recoveryAttempter](https://developer.apple.com/documentation/foundation/nserror/1408864-recoveryattempter)Added [NSError.userInfo](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo)Modified [+[NSError errorWithDomain:code:userInfo:]](https://developer.apple.com/documentation/foundation/nserror/1522782-errorwithdomain)

|  | Declaration |
| --- | --- |
| From | ``` + (id)errorWithDomain:(NSString *)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` |
| To | ``` + (instancetype)errorWithDomain:(NSString *)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` |

Modified [-[NSError initWithDomain:code:userInfo:]](https://developer.apple.com/documentation/foundation/nserror/1417063-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithDomain:(NSString *)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` | -- |
| To | ``` - (instancetype)initWithDomain:(NSString *)domain code:(NSInteger)code userInfo:(NSDictionary *)dict ``` | yes |

NSException.hRemoved [-[NSException callStackReturnAddresses]](https://developer.apple.com/documentation/foundation/nsexception/1412165-callstackreturnaddresses)Removed [-[NSException callStackSymbols]](https://developer.apple.com/documentation/foundation/nsexception/1416845-callstacksymbols)Removed [-[NSException name]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/name)Removed [-[NSException reason]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/reason)Removed [-[NSException userInfo]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/userInfo)Added [NSException.callStackReturnAddresses](https://developer.apple.com/documentation/foundation/nsexception/1412165-callstackreturnaddresses)Added [NSException.callStackSymbols](https://developer.apple.com/documentation/foundation/nsexception/1416845-callstacksymbols)Added [NSException.name](https://developer.apple.com/documentation/foundation/nsexception/1410925-name)Added [NSException.reason](https://developer.apple.com/documentation/foundation/nsexception/1415537-reason)Added [NSException.userInfo](https://developer.apple.com/documentation/foundation/nsexception/1418149-userinfo)Modified [-[NSException initWithName:reason:userInfo:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/initWithName:reason:userInfo:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithName:(NSString *)aName reason:(NSString *)aReason userInfo:(NSDictionary *)aUserInfo ``` | -- |
| To | ``` - (instancetype)initWithName:(NSString *)aName reason:(NSString *)aReason userInfo:(NSDictionary *)aUserInfo ``` | yes |

NSExpression.hRemoved [-[NSExpression arguments]](https://developer.apple.com/documentation/foundation/nsexpression/1411559-arguments)Removed [-[NSExpression collection]](https://developer.apple.com/documentation/foundation/nsexpression/1415684-collection)Removed [-[NSExpression constantValue]](https://developer.apple.com/documentation/foundation/nsexpression/1418093-constantvalue)Removed [-[NSExpression expressionBlock]](https://developer.apple.com/documentation/foundation/nsexpression/1409139-expressionblock)Removed [-[NSExpression expressionType]](https://developer.apple.com/documentation/foundation/nsexpression/1416975-expressiontype)Removed [-[NSExpression function]](https://developer.apple.com/documentation/foundation/nsexpression/1416200-function)Removed [-[NSExpression keyPath]](https://developer.apple.com/documentation/foundation/nsexpression/1416071-keypath)Removed [-[NSExpression leftExpression]](https://developer.apple.com/documentation/foundation/nsexpression/1415792-leftexpression)Removed [-[NSExpression operand]](https://developer.apple.com/documentation/foundation/nsexpression/1413698-operand)Removed [-[NSExpression predicate]](https://developer.apple.com/documentation/foundation/nsexpression/1407531-predicate)Removed [-[NSExpression rightExpression]](https://developer.apple.com/documentation/foundation/nsexpression/1416583-rightexpression)Removed [-[NSExpression variable]](https://developer.apple.com/documentation/foundation/nsexpression/1413759-variable)Added [NSExpression.arguments](https://developer.apple.com/documentation/foundation/nsexpression/1411559-arguments)Added [NSExpression.collection](https://developer.apple.com/documentation/foundation/nsexpression/1415684-collection)Added [NSExpression.constantValue](https://developer.apple.com/documentation/foundation/nsexpression/1418093-constantvalue)Added [NSExpression.expressionBlock](https://developer.apple.com/documentation/foundation/nsexpression/1409139-expressionblock)Added [NSExpression.expressionType](https://developer.apple.com/documentation/foundation/nsexpression/1416975-expressiontype)Added [NSExpression.function](https://developer.apple.com/documentation/foundation/nsexpression/1416200-function)Added [NSExpression.keyPath](https://developer.apple.com/documentation/foundation/nsexpression/1416071-keypath)Added [NSExpression.leftExpression](https://developer.apple.com/documentation/foundation/nsexpression/1415792-left)Added [NSExpression.operand](https://developer.apple.com/documentation/foundation/nsexpression/1413698-operand)Added [NSExpression.predicate](https://developer.apple.com/documentation/foundation/nsexpression/1407531-predicate)Added [NSExpression.rightExpression](https://developer.apple.com/documentation/foundation/nsexpression/1416583-rightexpression)Added [NSExpression.variable](https://developer.apple.com/documentation/foundation/nsexpression/1413759-variable)Modified [-[NSExpression initWithExpressionType:]](https://developer.apple.com/documentation/foundation/nsexpression/1418351-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithExpressionType:(NSExpressionType)type ``` |
| To | ``` - (instancetype)initWithExpressionType:(NSExpressionType)type ``` |

NSExtensionContext.h (Added)Added [NSExtensionContext](https://developer.apple.com/documentation/foundation/nsextensioncontext)Added [-[NSExtensionContext cancelRequestWithError:]](https://developer.apple.com/documentation/foundation/nsextensioncontext/1412773-cancelrequestwitherror)Added [-[NSExtensionContext completeRequestReturningItems:completionHandler:]](https://developer.apple.com/documentation/foundation/nsextensioncontext/1411301-completerequest)Added [NSExtensionContext.inputItems](https://developer.apple.com/documentation/foundation/nsextensioncontext/1414827-inputitems)Added [-[NSExtensionContext openURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsextensioncontext/1416791-open)Added [NSExtensionItemsAndErrorsKey](https://developer.apple.com/documentation/foundation/nsextensionitemsanderrorskey)NSExtensionItem.h (Added)Added [NSExtensionItem](https://developer.apple.com/documentation/foundation/nsextensionitem)Added [NSExtensionItem.attachments](https://developer.apple.com/documentation/foundation/nsextensionitem/1416690-attachments)Added [NSExtensionItem.attributedContentText](https://developer.apple.com/documentation/foundation/nsextensionitem/1408297-attributedcontenttext)Added [NSExtensionItem.attributedTitle](https://developer.apple.com/documentation/foundation/nsextensionitem/1416592-attributedtitle)Added [NSExtensionItem.userInfo](https://developer.apple.com/documentation/foundation/nsextensionitem/1414953-userinfo)Added [NSExtensionItemAttachmentsKey](https://developer.apple.com/documentation/foundation/nsextensionitemattachmentskey)Added [NSExtensionItemAttributedContentTextKey](https://developer.apple.com/documentation/foundation/nsextensionitemattributedcontenttextkey)Added [NSExtensionItemAttributedTitleKey](https://developer.apple.com/documentation/foundation/nsextensionitemattributedtitlekey)NSExtensionRequestHandling.h (Added)Added [NSExtensionRequestHandling](https://developer.apple.com/documentation/foundation/nsextensionrequesthandling)Added [-[NSExtensionRequestHandling beginRequestWithExtensionContext:]](https://developer.apple.com/documentation/foundation/nsextensionrequesthandling/1413395-beginrequestwithextensioncontext)NSFileCoordinator.hAdded [NSFileAccessIntent](https://developer.apple.com/documentation/foundation/nsfileaccessintent)Added [NSFileAccessIntent.URL](https://developer.apple.com/documentation/foundation/nsfileaccessintent/1411459-url)Added [+[NSFileAccessIntent readingIntentWithURL:options:]](https://developer.apple.com/documentation/foundation/nsfileaccessintent/1417829-readingintent)Added [+[NSFileAccessIntent writingIntentWithURL:options:]](https://developer.apple.com/documentation/foundation/nsfileaccessintent/1413014-writingintent)Added [-[NSFileCoordinator coordinateAccessWithIntents:queue:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1411533-coordinate)Added [NSFileCoordinator.purposeIdentifier](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1411868-purposeidentifier)Added [NSFileCoordinatorReadingForUploading](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/1407589-foruploading)Added [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/1411727-immediatelyavailablemetadataonly)Added [NSFileCoordinatorWritingContentIndependentMetadataOnly](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/1410365-contentindependentmetadataonly)Modified [-[NSFileCoordinator initWithFilePresenter:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1416795-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFilePresenter:(id<NSFilePresenter>)filePresenterOrNil ``` | -- |
| To | ``` - (instancetype)initWithFilePresenter:(id<NSFilePresenter>)filePresenterOrNil ``` | yes |

NSFileHandle.hRemoved [-[NSFileHandle availableData]](https://developer.apple.com/documentation/foundation/filehandle/1411463-availabledata)Removed [-[NSFileHandle fileDescriptor]](https://developer.apple.com/documentation/foundation/filehandle/1410326-filedescriptor)Removed [-[NSFileHandle offsetInFile]](https://developer.apple.com/documentation/foundation/filehandle/1408461-offsetinfile)Removed [-[NSPipe fileHandleForReading]](https://developer.apple.com/documentation/foundation/nspipe/1414352-filehandleforreading)Removed [-[NSPipe fileHandleForWriting]](https://developer.apple.com/documentation/foundation/nspipe/1412889-filehandleforwriting)Removed [-[NSPipe init]](https://developer.apple.com/documentation/foundation/nspipe/1807207-init)Added [NSFileHandle.availableData](https://developer.apple.com/documentation/foundation/filehandle/1411463-availabledata)Added [NSFileHandle.fileDescriptor](https://developer.apple.com/documentation/foundation/nsfilehandle/1410326-filedescriptor)Added [-[NSFileHandle initWithCoder:]](https://developer.apple.com/documentation/foundation/filehandle/1411174-init)Added [NSFileHandle.offsetInFile](https://developer.apple.com/documentation/foundation/filehandle/1408461-offsetinfile)Added [NSPipe.fileHandleForReading](https://developer.apple.com/documentation/foundation/pipe/1414352-filehandleforreading)Added [NSPipe.fileHandleForWriting](https://developer.apple.com/documentation/foundation/pipe/1412889-filehandleforwriting)Modified [+[NSFileHandle fileHandleForReadingAtPath:]](https://developer.apple.com/documentation/foundation/filehandle/1411250-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleForReadingAtPath:(NSString *)path ``` |
| To | ``` + (instancetype)fileHandleForReadingAtPath:(NSString *)path ``` |

Modified [+[NSFileHandle fileHandleForReadingFromURL:error:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1408422-filehandleforreadingfromurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleForReadingFromURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` + (instancetype)fileHandleForReadingFromURL:(NSURL *)url error:(NSError **)error ``` |

Modified [+[NSFileHandle fileHandleForUpdatingAtPath:]](https://developer.apple.com/documentation/foundation/filehandle/1411131-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleForUpdatingAtPath:(NSString *)path ``` |
| To | ``` + (instancetype)fileHandleForUpdatingAtPath:(NSString *)path ``` |

Modified [+[NSFileHandle fileHandleForUpdatingURL:error:]](https://developer.apple.com/documentation/foundation/filehandle/1417026-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleForUpdatingURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` + (instancetype)fileHandleForUpdatingURL:(NSURL *)url error:(NSError **)error ``` |

Modified [+[NSFileHandle fileHandleForWritingAtPath:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1414405-filehandleforwritingatpath)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleForWritingAtPath:(NSString *)path ``` |
| To | ``` + (instancetype)fileHandleForWritingAtPath:(NSString *)path ``` |

Modified [+[NSFileHandle fileHandleForWritingToURL:error:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1416892-filehandleforwritingtourl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleForWritingToURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` + (instancetype)fileHandleForWritingToURL:(NSURL *)url error:(NSError **)error ``` |

Modified [+[NSFileHandle fileHandleWithNullDevice]](https://developer.apple.com/documentation/foundation/nsfilehandle/1413881-filehandlewithnulldevice)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleWithNullDevice ``` |
| To | ``` + (NSFileHandle *)fileHandleWithNullDevice ``` |

Modified [+[NSFileHandle fileHandleWithStandardError]](https://developer.apple.com/documentation/foundation/filehandle/1411001-standarderror)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleWithStandardError ``` |
| To | ``` + (NSFileHandle *)fileHandleWithStandardError ``` |

Modified [+[NSFileHandle fileHandleWithStandardInput]](https://developer.apple.com/documentation/foundation/nsfilehandle/1413686-filehandlewithstandardinput)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleWithStandardInput ``` |
| To | ``` + (NSFileHandle *)fileHandleWithStandardInput ``` |

Modified [+[NSFileHandle fileHandleWithStandardOutput]](https://developer.apple.com/documentation/foundation/nsfilehandle/1416965-filehandlewithstandardoutput)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileHandleWithStandardOutput ``` |
| To | ``` + (NSFileHandle *)fileHandleWithStandardOutput ``` |

Modified [-[NSFileHandle initWithFileDescriptor:]](https://developer.apple.com/documentation/foundation/filehandle/1409825-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFileDescriptor:(int)fd ``` |
| To | ``` - (instancetype)initWithFileDescriptor:(int)fd ``` |

Modified [-[NSFileHandle initWithFileDescriptor:closeOnDealloc:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1408522-initwithfiledescriptor)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFileDescriptor:(int)fd closeOnDealloc:(BOOL)closeopt ``` | -- |
| To | ``` - (instancetype)initWithFileDescriptor:(int)fd closeOnDealloc:(BOOL)closeopt ``` | yes |

Modified [+[NSPipe pipe]](https://developer.apple.com/documentation/foundation/nspipe/1580418-pipe)

|  | Declaration |
| --- | --- |
| From | ``` + (id)pipe ``` |
| To | ``` + (NSPipe *)pipe ``` |

NSFileManager.hRemoved [-[NSDirectoryEnumerator directoryAttributes]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDirectoryEnumerator/Description.html#//apple_ref/occ/instm/NSDirectoryEnumerator/directoryAttributes)Removed [-[NSDirectoryEnumerator fileAttributes]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDirectoryEnumerator/Description.html#//apple_ref/occ/instm/NSDirectoryEnumerator/fileAttributes)Removed [-[NSDirectoryEnumerator level]](https://developer.apple.com/documentation/foundation/nsdirectoryenumerator/1408465-level)Removed [-[NSFileManager currentDirectoryPath]](https://developer.apple.com/documentation/foundation/nsfilemanager/1410766-currentdirectorypath)Removed [-[NSFileManager delegate]](https://developer.apple.com/documentation/foundation/filemanager/1415163-delegate)Removed [-[NSFileManager setDelegate:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1415163-delegate)Removed [-[NSFileManager ubiquityIdentityToken]](https://developer.apple.com/documentation/foundation/nsfilemanager/1408036-ubiquityidentitytoken)Added [NSDirectoryEnumerator.directoryAttributes](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1411357-directoryattributes)Added [NSDirectoryEnumerator.fileAttributes](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1413284-fileattributes)Added [NSDirectoryEnumerator.level](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1408465-level)Added [NSFileManager.currentDirectoryPath](https://developer.apple.com/documentation/foundation/nsfilemanager/1410766-currentdirectorypath)Added [NSFileManager.delegate](https://developer.apple.com/documentation/foundation/filemanager/1415163-delegate)Added [-[NSFileManager getRelationship:ofDirectory:inDomain:toItemAtURL:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1411439-getrelationship)Added [-[NSFileManager getRelationship:ofDirectoryAtURL:toItemAtURL:error:]](https://developer.apple.com/documentation/foundation/filemanager/1407229-getrelationship)Added [NSFileManager.ubiquityIdentityToken](https://developer.apple.com/documentation/foundation/filemanager/1408036-ubiquityidentitytoken)Added [NSURLRelationship](https://developer.apple.com/documentation/foundation/nsurlrelationship)Added [NSURLRelationshipContains](https://developer.apple.com/documentation/foundation/nsurlrelationship/nsurlrelationshipcontains)Added [NSURLRelationshipOther](https://developer.apple.com/documentation/foundation/nsurlrelationship/nsurlrelationshipother)Added [NSURLRelationshipSame](https://developer.apple.com/documentation/foundation/filemanager/urlrelationship/same)Modified [-[NSFileManagerDelegate fileManager:shouldCopyItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1414922-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldCopyItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1417936-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldLinkItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1414699-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldLinkItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1417589-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldMoveItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1407734-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldMoveItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1411878-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1410189-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1410788-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1415627-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1408003-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:movingItemAtPath:toPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1412865-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:movingItemAtURL:toURL:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1411289-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:removingItemAtPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1409791-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldProceedAfterError:removingItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1408660-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldRemoveItemAtPath:]](https://developer.apple.com/documentation/foundation/filemanagerdelegate/1412994-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileManagerDelegate fileManager:shouldRemoveItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1411918-filemanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSFilePresenter.hModified [-[NSFilePresenter accommodatePresentedItemDeletionWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414732-accommodatepresenteditemdeletion)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter accommodatePresentedSubitemDeletionAtURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415657-accommodatepresentedsubitemdelet)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedItemDidChange]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1416103-presenteditemdidchange)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedItemDidGainVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415018-presenteditemdidgainversion)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedItemDidLoseVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1417258-presenteditemdidlose)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedItemDidMoveToURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1417861-presenteditemdidmove)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedItemDidResolveConflictVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1418445-presenteditemdidresolveconflictv)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSFilePresenter.presentedItemOperationQueue](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415250-presenteditemoperationqueue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSOperationQueue *presentedItemOperationQueue ``` |
| To | ``` @property(readonly, retain) NSOperationQueue *presentedItemOperationQueue ``` |

Modified [NSFilePresenter.presentedItemURL](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414861-presenteditemurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *presentedItemURL ``` |
| To | ``` @property(readonly, copy) NSURL *presentedItemURL ``` |

Modified [-[NSFilePresenter presentedSubitemAtURL:didGainVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415472-presentedsubitematurl)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedSubitemAtURL:didLoseVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413957-presentedsubitem)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedSubitemAtURL:didMoveToURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1409465-presentedsubitematurl)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedSubitemAtURL:didResolveConflictVersion:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1416913-presentedsubitematurl)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedSubitemDidAppearAtURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1408642-presentedsubitemdidappear)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter presentedSubitemDidChangeAtURL:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1411135-presentedsubitemdidchangeaturl)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [NSFilePresenter.primaryPresentedItemURL](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415415-primarypresenteditemurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *primaryPresentedItemURL ``` |
| To | ``` @property(readonly, copy) NSURL *primaryPresentedItemURL ``` |

Modified [-[NSFilePresenter relinquishPresentedItemToReader:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1410743-relinquishpresenteditemtoreader)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter relinquishPresentedItemToWriter:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413688-relinquishpresenteditemtowriter)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFilePresenter savePresentedItemChangesWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414407-savepresenteditemchangeswithcomp)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSFileVersion.hAdded [+[NSFileVersion getNonlocalVersionsOfItemAtURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsfileversion/1416051-getnonlocalversionsofitematurl)Added [NSFileVersion.hasLocalContents](https://developer.apple.com/documentation/foundation/nsfileversion/1412014-haslocalcontents)Added [NSFileVersion.hasThumbnail](https://developer.apple.com/documentation/foundation/nsfileversion/1409471-hasthumbnail)Modified [NSFileVersion.URL](https://developer.apple.com/documentation/foundation/nsfileversion/1418131-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *URL ``` |
| To | ``` @property(readonly, copy) NSURL *URL ``` |

Modified [NSFileVersion.localizedName](https://developer.apple.com/documentation/foundation/nsfileversion/1413855-localizedname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *localizedName ``` |
| To | ``` @property(readonly, copy) NSString *localizedName ``` |

Modified [NSFileVersion.localizedNameOfSavingComputer](https://developer.apple.com/documentation/foundation/nsfileversion/1408866-localizednameofsavingcomputer)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *localizedNameOfSavingComputer ``` |
| To | ``` @property(readonly, copy) NSString *localizedNameOfSavingComputer ``` |

Modified [NSFileVersion.modificationDate](https://developer.apple.com/documentation/foundation/nsfileversion/1411506-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *modificationDate ``` |
| To | ``` @property(readonly, copy) NSDate *modificationDate ``` |

Modified [NSFileVersion.persistentIdentifier](https://developer.apple.com/documentation/foundation/nsfileversion/1407948-persistentidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) id<NSCoding> persistentIdentifier ``` |
| To | ``` @property(readonly, retain) id<NSCoding> persistentIdentifier ``` |

NSFileWrapper.hRemoved [-[NSFileWrapper fileAttributes]](https://developer.apple.com/documentation/foundation/filewrapper/1412745-fileattributes)Removed [-[NSFileWrapper fileWrappers]](https://developer.apple.com/documentation/foundation/filewrapper/1409437-filewrappers)Removed [-[NSFileWrapper filename]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1416684-filename)Removed [-[NSFileWrapper isDirectory]](https://developer.apple.com/documentation/foundation/filewrapper/1409030-isdirectory)Removed [-[NSFileWrapper isRegularFile]](https://developer.apple.com/documentation/foundation/filewrapper/1415680-isregularfile)Removed [-[NSFileWrapper isSymbolicLink]](https://developer.apple.com/documentation/foundation/filewrapper/1408125-issymboliclink)Removed [-[NSFileWrapper preferredFilename]](https://developer.apple.com/documentation/foundation/filewrapper/1409368-preferredfilename)Removed [-[NSFileWrapper regularFileContents]](https://developer.apple.com/documentation/foundation/filewrapper/1410178-regularfilecontents)Removed [-[NSFileWrapper serializedRepresentation]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412119-serializedrepresentation)Removed [-[NSFileWrapper setFileAttributes:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412745-fileattributes)Removed [-[NSFileWrapper setFilename:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1416684-filename)Removed [-[NSFileWrapper setPreferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1409368-preferredfilename)Removed [-[NSFileWrapper symbolicLinkDestinationURL]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408364-symboliclinkdestinationurl)Added [NSFileWrapper.directory](https://developer.apple.com/documentation/foundation/nsfilewrapper/1409030-directory)Added [NSFileWrapper.fileAttributes](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412745-fileattributes)Added [NSFileWrapper.fileWrappers](https://developer.apple.com/documentation/foundation/filewrapper/1409437-filewrappers)Added [NSFileWrapper.filename](https://developer.apple.com/documentation/foundation/nsfilewrapper/1416684-filename)Added [-[NSFileWrapper initWithCoder:]](https://developer.apple.com/documentation/foundation/filewrapper/1416358-init)Added [NSFileWrapper.preferredFilename](https://developer.apple.com/documentation/foundation/filewrapper/1409368-preferredfilename)Added [NSFileWrapper.regularFile](https://developer.apple.com/documentation/foundation/filewrapper/1415680-isregularfile)Added [NSFileWrapper.regularFileContents](https://developer.apple.com/documentation/foundation/nsfilewrapper/1410178-regularfilecontents)Added [NSFileWrapper.serializedRepresentation](https://developer.apple.com/documentation/foundation/filewrapper/1412119-serializedrepresentation)Added [NSFileWrapper.symbolicLink](https://developer.apple.com/documentation/foundation/filewrapper/1408125-issymboliclink)Added [NSFileWrapper.symbolicLinkDestinationURL](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408364-symboliclinkdestinationurl)Modified [-[NSFileWrapper addFileWithPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1417211-addfile)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSFileWrapper addSymbolicLinkWithDestination:preferredFilename:]](https://developer.apple.com/documentation/foundation/filewrapper/1414604-addsymboliclink)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSFileWrapper initDirectoryWithFileWrappers:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415121-initdirectorywithfilewrappers)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initDirectoryWithFileWrappers:(NSDictionary *)childrenByPreferredName ``` | -- |
| To | ``` - (instancetype)initDirectoryWithFileWrappers:(NSDictionary *)childrenByPreferredName ``` | yes |

Modified [-[NSFileWrapper initRegularFileWithContents:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1409508-initregularfilewithcontents)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initRegularFileWithContents:(NSData *)contents ``` | -- |
| To | ``` - (instancetype)initRegularFileWithContents:(NSData *)contents ``` | yes |

Modified [-[NSFileWrapper initSymbolicLinkWithDestination:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1411268-initsymboliclinkwithdestination)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSFileWrapper initSymbolicLinkWithDestinationURL:]](https://developer.apple.com/documentation/foundation/filewrapper/1415098-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initSymbolicLinkWithDestinationURL:(NSURL *)url ``` | -- |
| To | ``` - (instancetype)initSymbolicLinkWithDestinationURL:(NSURL *)url ``` | yes |

Modified [-[NSFileWrapper initWithPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1408388-initwithpath)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSFileWrapper initWithSerializedRepresentation:]](https://developer.apple.com/documentation/foundation/filewrapper/1407515-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithSerializedRepresentation:(NSData *)serializeRepresentation ``` | -- |
| To | ``` - (instancetype)initWithSerializedRepresentation:(NSData *)serializeRepresentation ``` | yes |

Modified [-[NSFileWrapper initWithURL:options:error:]](https://developer.apple.com/documentation/foundation/filewrapper/1415658-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url options:(NSFileWrapperReadingOptions)options error:(NSError **)outError ``` | -- |
| To | ``` - (instancetype)initWithURL:(NSURL *)url options:(NSFileWrapperReadingOptions)options error:(NSError **)outError ``` | yes |

Modified [-[NSFileWrapper needsToBeUpdatedFromPath:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1407738-needstobeupdatedfrompath)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSFileWrapper symbolicLinkDestination]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1418302-symboliclinkdestination)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSFileWrapper updateFromPath:]](https://developer.apple.com/documentation/foundation/filewrapper/1416300-update)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

Modified [-[NSFileWrapper writeToFile:atomically:updateFilenames:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415079-writetofile)

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10 |

NSFormatter.hAdded [NSFormattingContext](https://developer.apple.com/documentation/foundation/formatter/context)Added [NSFormattingContextBeginningOfSentence](https://developer.apple.com/documentation/foundation/formatter/context/beginningofsentence)Added [NSFormattingContextDynamic](https://developer.apple.com/documentation/foundation/nsformattingcontext/nsformattingcontextdynamic)Added [NSFormattingContextListItem](https://developer.apple.com/documentation/foundation/formatter/context/listitem)Added [NSFormattingContextMiddleOfSentence](https://developer.apple.com/documentation/foundation/formatter/context/middleofsentence)Added [NSFormattingContextStandalone](https://developer.apple.com/documentation/foundation/nsformattingcontext/nsformattingcontextstandalone)Added [NSFormattingContextUnknown](https://developer.apple.com/documentation/foundation/formatter/context/unknown)Added [NSFormattingUnitStyle](https://developer.apple.com/documentation/foundation/nsformattingunitstyle)Added [NSFormattingUnitStyleLong](https://developer.apple.com/documentation/foundation/nsformattingunitstyle/nsformattingunitstylelong)Added [NSFormattingUnitStyleMedium](https://developer.apple.com/documentation/foundation/nsformattingunitstyle/nsformattingunitstylemedium)Added [NSFormattingUnitStyleShort](https://developer.apple.com/documentation/foundation/formatter/unitstyle/short)NSGarbageCollector.hModified [NSGarbageCollector](https://developer.apple.com/documentation/foundation/nsgarbagecollector)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSGeometry.hRemoved [-[NSValue pointValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/pointValue)Removed [-[NSValue rectValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/rectValue)Removed [-[NSValue sizeValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/sizeValue)Added [NSValue.edgeInsetsValue](https://developer.apple.com/documentation/foundation/nsvalue/1391123-edgeinsetsvalue)Added [NSValue.pointValue](https://developer.apple.com/documentation/foundation/nsvalue/1391255-pointvalue)Added [NSValue.rectValue](https://developer.apple.com/documentation/foundation/nsvalue/1391171-rectvalue)Added [NSValue.sizeValue](https://developer.apple.com/documentation/foundation/nsvalue/1391301-sizevalue)Added [+[NSValue valueWithEdgeInsets:]](https://developer.apple.com/documentation/foundation/nsvalue/1391181-init)Added #def NSEDGEINSETS_DEFINEDAdded [NSEdgeInsetsEqual()](https://developer.apple.com/documentation/foundation/1391230-nsedgeinsetsequal)Added [NSEdgeInsetsZero](https://developer.apple.com/documentation/foundation/nsedgeinsetszero)Modified [NSEdgeInsets](https://developer.apple.com/documentation/foundation/nsedgeinsets)

|  | Header |
| --- | --- |
| From | AppKit/NSLayoutConstraint.h |
| To | Foundation/NSGeometry.h |

Modified [NSEdgeInsetsMake()](https://developer.apple.com/documentation/foundation/1391130-nsedgeinsetsmake)

|  | Header |
| --- | --- |
| From | AppKit/NSLayoutConstraint.h |
| To | Foundation/NSGeometry.h |

NSHTTPCookie.hRemoved [-[NSHTTPCookie comment]](https://developer.apple.com/documentation/foundation/httpcookie/1392997-comment)Removed [-[NSHTTPCookie commentURL]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392987-commenturl)Removed [-[NSHTTPCookie domain]](https://developer.apple.com/documentation/foundation/httpcookie/1393015-domain)Removed [-[NSHTTPCookie expiresDate]](https://developer.apple.com/documentation/foundation/nshttpcookie/1393019-expiresdate)Removed [-[NSHTTPCookie isHTTPOnly]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392969-httponly)Removed [-[NSHTTPCookie isSecure]](https://developer.apple.com/documentation/foundation/httpcookie/1393025-issecure)Removed [-[NSHTTPCookie isSessionOnly]](https://developer.apple.com/documentation/foundation/httpcookie/1392991-issessiononly)Removed [-[NSHTTPCookie name]](https://developer.apple.com/documentation/foundation/httpcookie/1393013-name)Removed [-[NSHTTPCookie path]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392981-path)Removed [-[NSHTTPCookie portList]](https://developer.apple.com/documentation/foundation/httpcookie/1393027-portlist)Removed [-[NSHTTPCookie properties]](https://developer.apple.com/documentation/foundation/nshttpcookie/1393017-properties)Removed [-[NSHTTPCookie value]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392995-value)Removed [-[NSHTTPCookie version]](https://developer.apple.com/documentation/foundation/httpcookie/1392993-version)Added [NSHTTPCookie.HTTPOnly](https://developer.apple.com/documentation/foundation/httpcookie/1392969-ishttponly)Added [NSHTTPCookie.comment](https://developer.apple.com/documentation/foundation/nshttpcookie/1392997-comment)Added [NSHTTPCookie.commentURL](https://developer.apple.com/documentation/foundation/httpcookie/1392987-commenturl)Added [NSHTTPCookie.domain](https://developer.apple.com/documentation/foundation/nshttpcookie/1393015-domain)Added [NSHTTPCookie.expiresDate](https://developer.apple.com/documentation/foundation/nshttpcookie/1393019-expiresdate)Added [NSHTTPCookie.name](https://developer.apple.com/documentation/foundation/nshttpcookie/1393013-name)Added [NSHTTPCookie.path](https://developer.apple.com/documentation/foundation/httpcookie/1392981-path)Added [NSHTTPCookie.portList](https://developer.apple.com/documentation/foundation/httpcookie/1393027-portlist)Added [NSHTTPCookie.properties](https://developer.apple.com/documentation/foundation/nshttpcookie/1393017-properties)Added [NSHTTPCookie.secure](https://developer.apple.com/documentation/foundation/nshttpcookie/1393025-secure)Added [NSHTTPCookie.sessionOnly](https://developer.apple.com/documentation/foundation/httpcookie/1392991-issessiononly)Added [NSHTTPCookie.value](https://developer.apple.com/documentation/foundation/httpcookie/1392995-value)Added [NSHTTPCookie.version](https://developer.apple.com/documentation/foundation/nshttpcookie/1392993-version)Modified [+[NSHTTPCookie cookieWithProperties:]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392967-cookiewithproperties)

|  | Declaration |
| --- | --- |
| From | ``` + (id)cookieWithProperties:(NSDictionary *)properties ``` |
| To | ``` + (NSHTTPCookie *)cookieWithProperties:(NSDictionary *)properties ``` |

Modified [-[NSHTTPCookie initWithProperties:]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392975-initwithproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProperties:(NSDictionary *)properties ``` |
| To | ``` - (instancetype)initWithProperties:(NSDictionary *)properties ``` |

NSHTTPCookieStorage.hRemoved [-[NSHTTPCookieStorage cookieAcceptPolicy]](https://developer.apple.com/documentation/foundation/httpcookiestorage/1410415-cookieacceptpolicy)Removed [-[NSHTTPCookieStorage cookies]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1418390-cookies)Removed [-[NSHTTPCookieStorage setCookieAcceptPolicy:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1410415-cookieacceptpolicy)Added [NSHTTPCookieStorage.cookieAcceptPolicy](https://developer.apple.com/documentation/foundation/httpcookiestorage/1410415-cookieacceptpolicy)Added [NSHTTPCookieStorage.cookies](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1418390-cookies)Added [-[NSHTTPCookieStorage getCookiesForTask:completionHandler:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1408517-getcookiesfortask)Added [-[NSHTTPCookieStorage removeCookiesSinceDate:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1407256-removecookiessincedate)Added [-[NSHTTPCookieStorage storeCookies:forTask:]](https://developer.apple.com/documentation/foundation/httpcookiestorage/1415381-storecookies)Added NSHTTPCookieStorage(NSURLSessionTaskAdditions)NSHashTable.hRemoved [-[NSHashTable allObjects]](https://developer.apple.com/documentation/foundation/nshashtable/1410223-allobjects)Removed [-[NSHashTable anyObject]](https://developer.apple.com/documentation/foundation/nshashtable/1410639-anyobject)Removed [-[NSHashTable count]](https://developer.apple.com/documentation/foundation/nshashtable/1413142-count)Removed [-[NSHashTable pointerFunctions]](https://developer.apple.com/documentation/foundation/nshashtable/1417398-pointerfunctions)Removed [-[NSHashTable setRepresentation]](https://developer.apple.com/documentation/foundation/nshashtable/1414641-setrepresentation)Added [NSHashTable.allObjects](https://developer.apple.com/documentation/foundation/nshashtable/1410223-allobjects)Added [NSHashTable.anyObject](https://developer.apple.com/documentation/foundation/nshashtable/1410639-anyobject)Added [NSHashTable.count](https://developer.apple.com/documentation/foundation/nshashtable/1413142-count)Added [NSHashTable.pointerFunctions](https://developer.apple.com/documentation/foundation/nshashtable/1417398-pointerfunctions)Added [NSHashTable.setRepresentation](https://developer.apple.com/documentation/foundation/nshashtable/1414641-setrepresentation)Modified [+[NSHashTable hashTableWithOptions:]](https://developer.apple.com/documentation/foundation/nshashtable/1415284-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)hashTableWithOptions:(NSPointerFunctionsOptions)options ``` |
| To | ``` + (NSHashTable *)hashTableWithOptions:(NSPointerFunctionsOptions)options ``` |

Modified [-[NSHashTable initWithOptions:capacity:]](https://developer.apple.com/documentation/foundation/nshashtable/1411066-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithOptions:(NSPointerFunctionsOptions)options capacity:(NSUInteger)initialCapacity ``` | -- |
| To | ``` - (instancetype)initWithOptions:(NSPointerFunctionsOptions)options capacity:(NSUInteger)initialCapacity ``` | yes |

Modified [-[NSHashTable initWithPointerFunctions:capacity:]](https://developer.apple.com/documentation/foundation/nshashtable/1416331-initwithpointerfunctions)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithPointerFunctions:(NSPointerFunctions *)functions capacity:(NSUInteger)initialCapacity ``` | -- |
| To | ``` - (instancetype)initWithPointerFunctions:(NSPointerFunctions *)functions capacity:(NSUInteger)initialCapacity ``` | yes |

Modified [+[NSHashTable weakObjectsHashTable]](https://developer.apple.com/documentation/foundation/nshashtable/1412241-weakobjectshashtable)

|  | Declaration |
| --- | --- |
| From | ``` + (id)weakObjectsHashTable ``` |
| To | ``` + (NSHashTable *)weakObjectsHashTable ``` |

NSHost.hRemoved [-[NSHost address]](https://developer.apple.com/documentation/foundation/host/1412418-address)Removed [-[NSHost addresses]](https://developer.apple.com/documentation/foundation/nshost/1417599-addresses)Removed [-[NSHost localizedName]](https://developer.apple.com/documentation/foundation/nshost/1409624-localizedname)Removed [-[NSHost name]](https://developer.apple.com/documentation/foundation/nshost/1416949-name)Removed [-[NSHost names]](https://developer.apple.com/documentation/foundation/nshost/1416026-names)Added [NSHost.address](https://developer.apple.com/documentation/foundation/nshost/1412418-address)Added [NSHost.addresses](https://developer.apple.com/documentation/foundation/nshost/1417599-addresses)Added [NSHost.localizedName](https://developer.apple.com/documentation/foundation/host/1409624-localizedname)Added [NSHost.name](https://developer.apple.com/documentation/foundation/host/1416949-name)Added [NSHost.names](https://developer.apple.com/documentation/foundation/host/1416026-names)Modified [+[NSHost currentHost]](https://developer.apple.com/documentation/foundation/nshost/1408946-currenthost)

|  | Declaration |
| --- | --- |
| From | ``` + (NSHost *)currentHost ``` |
| To | ``` + (instancetype)currentHost ``` |

Modified [+[NSHost hostWithAddress:]](https://developer.apple.com/documentation/foundation/host/1416437-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSHost *)hostWithAddress:(NSString *)address ``` |
| To | ``` + (instancetype)hostWithAddress:(NSString *)address ``` |

Modified [+[NSHost hostWithName:]](https://developer.apple.com/documentation/foundation/nshost/1409654-hostwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (NSHost *)hostWithName:(NSString *)name ``` |
| To | ``` + (instancetype)hostWithName:(NSString *)name ``` |

NSIndexPath.hRemoved -[NSIndexPath init]Removed [-[NSIndexPath length]](https://developer.apple.com/documentation/foundation/nsindexpath/1412001-length)Added [NSIndexPath.length](https://developer.apple.com/documentation/foundation/nsindexpath/1412001-length)Modified [NSIndexPath](https://developer.apple.com/documentation/foundation/nsindexpath)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [-[NSIndexPath initWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416906-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSIndexSet.hRemoved [-[NSIndexSet count]](https://developer.apple.com/documentation/foundation/nsindexset/1409648-count)Removed [-[NSIndexSet firstIndex]](https://developer.apple.com/documentation/foundation/nsindexset/1410814-firstindex)Removed [-[NSIndexSet init]](https://developer.apple.com/documentation/foundation/nsindexset/1807255-init)Removed [-[NSIndexSet lastIndex]](https://developer.apple.com/documentation/foundation/nsindexset/1415020-lastindex)Added [NSIndexSet.count](https://developer.apple.com/documentation/foundation/nsindexset/1409648-count)Added [NSIndexSet.firstIndex](https://developer.apple.com/documentation/foundation/nsindexset/1410814-firstindex)Added [NSIndexSet.lastIndex](https://developer.apple.com/documentation/foundation/nsindexset/1415020-lastindex)Modified [NSIndexSet](https://developer.apple.com/documentation/foundation/nsindexset)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [-[NSIndexSet initWithIndexSet:]](https://developer.apple.com/documentation/foundation/nsindexset/1415602-initwithindexset)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSIndexSet initWithIndexesInRange:]](https://developer.apple.com/documentation/foundation/nsindexset/1414013-initwithindexesinrange)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSInvocation.hRemoved [-[NSInvocation argumentsRetained]](https://developer.apple.com/documentation/foundation/nsinvocation/1437842-argumentsretained)Removed [-[NSInvocation methodSignature]](https://developer.apple.com/documentation/foundation/nsinvocation/1437846-methodsignature)Removed [-[NSInvocation selector]](https://developer.apple.com/documentation/foundation/nsinvocation/1437836-selector)Removed [-[NSInvocation setSelector:]](https://developer.apple.com/documentation/foundation/nsinvocation/1437836-selector)Removed [-[NSInvocation setTarget:]](https://developer.apple.com/documentation/foundation/nsinvocation/1437852-target)Removed [-[NSInvocation target]](https://developer.apple.com/documentation/foundation/nsinvocation/1437852-target)Added [NSInvocation.argumentsRetained](https://developer.apple.com/documentation/foundation/nsinvocation/1437842-argumentsretained)Added [NSInvocation.methodSignature](https://developer.apple.com/documentation/foundation/nsinvocation/1437846-methodsignature)Added [NSInvocation.selector](https://developer.apple.com/documentation/foundation/nsinvocation/1437836-selector)Added [NSInvocation.target](https://developer.apple.com/documentation/foundation/nsinvocation/1437852-target)NSItemProvider.h (Added)Added [NSItemProvider](https://developer.apple.com/documentation/foundation/nsitemprovider)Added [-[NSItemProvider hasItemConformingToTypeIdentifier:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1403921-hasitemconformingtotypeidentifie)Added [-[NSItemProvider initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1403911-init)Added [-[NSItemProvider initWithItem:typeIdentifier:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1403933-initwithitem)Added [-[NSItemProvider loadItemForTypeIdentifier:options:completionHandler:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1403900-loaditemfortypeidentifier)Added [-[NSItemProvider loadPreviewImageWithOptions:completionHandler:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1403925-loadpreviewimagewithoptions)Added [NSItemProvider.previewImageHandler](https://developer.apple.com/documentation/foundation/nsitemprovider/1403904-previewimagehandler)Added [-[NSItemProvider registerItemForTypeIdentifier:loadHandler:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1403917-registeritem)Added [NSItemProvider.registeredTypeIdentifiers](https://developer.apple.com/documentation/foundation/nsitemprovider/1403923-registeredtypeidentifiers)Added [NSExtensionJavaScriptPreprocessingResultsKey](https://developer.apple.com/documentation/foundation/nsextensionjavascriptpreprocessingresultskey)Added NSItemProvider(NSPreviewSupport)Added [NSItemProviderCompletionHandler](https://developer.apple.com/documentation/foundation/nsitemprovidercompletionhandler)Added [NSItemProviderErrorCode](https://developer.apple.com/documentation/foundation/nsitemprovidererrorcode)Added [NSItemProviderErrorDomain](https://developer.apple.com/documentation/foundation/nsitemprovidererrordomain)Added [NSItemProviderItemUnavailableError](https://developer.apple.com/documentation/foundation/nsitemprovider/errorcode/itemunavailableerror)Added [NSItemProviderLoadHandler](https://developer.apple.com/documentation/foundation/nsitemproviderloadhandler)Added [NSItemProviderPreferredImageSizeKey](https://developer.apple.com/documentation/foundation/nsitemproviderpreferredimagesizekey)Added [NSItemProviderUnexpectedValueClassError](https://developer.apple.com/documentation/foundation/nsitemprovider/errorcode/unexpectedvalueclasserror)Added [NSItemProviderUnknownError](https://developer.apple.com/documentation/foundation/nsitemprovidererrorcode/nsitemproviderunknownerror)NSKeyValueObserving.hRemoved [-[NSObject observationInfo]](https://developer.apple.com/documentation/objectivec/nsobject/1414009-observationinfo)Removed [-[NSObject setObservationInfo:]](https://developer.apple.com/documentation/objectivec/nsobject/1414009-observationinfo)Added [NSObject.observationInfo](https://developer.apple.com/documentation/objectivec/nsobject/1414009-observationinfo)NSKeyedArchiver.hRemoved [-[NSKeyedArchiver delegate]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1412809-delegate)Removed [-[NSKeyedArchiver outputFormat]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417520-outputformat)Removed [-[NSKeyedArchiver setDelegate:]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1412809-delegate)Removed [-[NSKeyedArchiver setOutputFormat:]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417520-outputformat)Removed [-[NSKeyedUnarchiver delegate]](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1415688-delegate)Removed [-[NSKeyedUnarchiver setDelegate:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1415688-delegate)Removed [-[NSObject classForKeyedArchiver]](https://developer.apple.com/documentation/objectivec/nsobject/1410512-classforkeyedarchiver)Added [NSKeyedArchiver.delegate](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1412809-delegate)Added [NSKeyedArchiver.outputFormat](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417520-outputformat)Added [NSKeyedUnarchiver.delegate](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1415688-delegate)Added [NSObject.classForKeyedArchiver](https://developer.apple.com/documentation/objectivec/nsobject/1410512-classforkeyedarchiver)Modified [-[NSKeyedArchiver initForWritingWithMutableData:]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1409579-initforwritingwithmutabledata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initForWritingWithMutableData:(NSMutableData *)data ``` |
| To | ``` - (instancetype)initForWritingWithMutableData:(NSMutableData *)data ``` |

Modified [-[NSKeyedArchiverDelegate archiver:didEncodeObject:]](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/1416193-archiver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedArchiverDelegate archiver:willEncodeObject:]](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/1409228-archiver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedArchiverDelegate archiver:willReplaceObject:withObject:]](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/1409389-archiver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedArchiverDelegate archiverDidFinish:]](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/1412480-archiverdidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedArchiverDelegate archiverWillFinish:]](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate/1411119-archiverwillfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedUnarchiver initForReadingWithData:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410862-initforreadingwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initForReadingWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initForReadingWithData:(NSData *)data ``` |

Modified [-[NSKeyedUnarchiverDelegate unarchiver:cannotDecodeObjectOfClassName:originalClasses:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/1409948-unarchiver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedUnarchiverDelegate unarchiver:didDecodeObject:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/1414187-unarchiver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedUnarchiverDelegate unarchiver:willReplaceObject:withObject:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/1413012-unarchiver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedUnarchiverDelegate unarchiverDidFinish:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/1418067-unarchiverdidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSKeyedUnarchiverDelegate unarchiverWillFinish:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/1415305-unarchiverwillfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSLengthFormatter.h (Added)Added [NSLengthFormatter](https://developer.apple.com/documentation/foundation/lengthformatter)Added [NSLengthFormatter.forPersonHeightUse](https://developer.apple.com/documentation/foundation/nslengthformatter/1416517-forpersonheightuse)Added [-[NSLengthFormatter getObjectValue:forString:errorDescription:]](https://developer.apple.com/documentation/foundation/lengthformatter/1413280-getobjectvalue)Added [NSLengthFormatter.numberFormatter](https://developer.apple.com/documentation/foundation/lengthformatter/1417778-numberformatter)Added [-[NSLengthFormatter stringFromMeters:]](https://developer.apple.com/documentation/foundation/lengthformatter/1416111-string)Added [-[NSLengthFormatter stringFromValue:unit:]](https://developer.apple.com/documentation/foundation/lengthformatter/1418018-string)Added [-[NSLengthFormatter unitStringFromMeters:usedUnit:]](https://developer.apple.com/documentation/foundation/lengthformatter/1407661-unitstring)Added [-[NSLengthFormatter unitStringFromValue:unit:]](https://developer.apple.com/documentation/foundation/lengthformatter/1416076-unitstring)Added [NSLengthFormatter.unitStyle](https://developer.apple.com/documentation/foundation/lengthformatter/1409965-unitstyle)Added [NSLengthFormatterUnit](https://developer.apple.com/documentation/foundation/lengthformatter/unit)Added [NSLengthFormatterUnitCentimeter](https://developer.apple.com/documentation/foundation/lengthformatter/unit/centimeter)Added [NSLengthFormatterUnitFoot](https://developer.apple.com/documentation/foundation/nslengthformatterunit/nslengthformatterunitfoot)Added [NSLengthFormatterUnitInch](https://developer.apple.com/documentation/foundation/nslengthformatterunit/nslengthformatterunitinch)Added [NSLengthFormatterUnitKilometer](https://developer.apple.com/documentation/foundation/nslengthformatterunit/nslengthformatterunitkilometer)Added [NSLengthFormatterUnitMeter](https://developer.apple.com/documentation/foundation/lengthformatter/unit/meter)Added [NSLengthFormatterUnitMile](https://developer.apple.com/documentation/foundation/lengthformatter/unit/mile)Added [NSLengthFormatterUnitMillimeter](https://developer.apple.com/documentation/foundation/nslengthformatterunit/nslengthformatterunitmillimeter)Added [NSLengthFormatterUnitYard](https://developer.apple.com/documentation/foundation/lengthformatter/unit/yard)NSLinguisticTagger.hRemoved [-[NSLinguisticTagger setString:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1407750-string)Removed [-[NSLinguisticTagger string]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1407750-string)Removed [-[NSLinguisticTagger tagSchemes]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1409018-tagschemes)Added [NSLinguisticTagger.string](https://developer.apple.com/documentation/foundation/nslinguistictagger/1407750-string)Added [NSLinguisticTagger.tagSchemes](https://developer.apple.com/documentation/foundation/nslinguistictagger/1409018-tagschemes)Modified [-[NSLinguisticTagger initWithTagSchemes:options:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1414576-initwithtagschemes)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithTagSchemes:(NSArray *)tagSchemes options:(NSUInteger)opts ``` | -- |
| To | ``` - (instancetype)initWithTagSchemes:(NSArray *)tagSchemes options:(NSUInteger)opts ``` | yes |

NSLocale.hRemoved -[NSLocale init]Removed [-[NSLocale localeIdentifier]](https://developer.apple.com/documentation/foundation/nslocale/1416263-localeidentifier)Added [-[NSLocale initWithCoder:]](https://developer.apple.com/documentation/foundation/nslocale/1415424-init)Added [NSLocale.localeIdentifier](https://developer.apple.com/documentation/foundation/nslocale/1416263-localeidentifier)Modified [+[NSLocale autoupdatingCurrentLocale]](https://developer.apple.com/documentation/foundation/nslocale/1414388-autoupdatingcurrent)

|  | Declaration |
| --- | --- |
| From | ``` + (id)autoupdatingCurrentLocale ``` |
| To | ``` + (NSLocale *)autoupdatingCurrentLocale ``` |

Modified [+[NSLocale currentLocale]](https://developer.apple.com/documentation/foundation/nslocale/1409990-currentlocale)

|  | Declaration |
| --- | --- |
| From | ``` + (id)currentLocale ``` |
| To | ``` + (NSLocale *)currentLocale ``` |

Modified [-[NSLocale initWithLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1414217-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [+[NSLocale systemLocale]](https://developer.apple.com/documentation/foundation/nslocale/1407691-system)

|  | Declaration |
| --- | --- |
| From | ``` + (id)systemLocale ``` |
| To | ``` + (NSLocale *)systemLocale ``` |

Modified [NSBuddhistCalendar](https://developer.apple.com/documentation/foundation/nsbuddhistcalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSChineseCalendar](https://developer.apple.com/documentation/foundation/nschinesecalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSGregorianCalendar](https://developer.apple.com/documentation/foundation/nsgregoriancalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSHebrewCalendar](https://developer.apple.com/documentation/foundation/nshebrewcalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSISO8601Calendar](https://developer.apple.com/documentation/foundation/nsiso8601calendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSIndianCalendar](https://developer.apple.com/documentation/foundation/nsindiancalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSIslamicCalendar](https://developer.apple.com/documentation/foundation/nsislamiccalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSIslamicCivilCalendar](https://developer.apple.com/documentation/foundation/nsislamiccivilcalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSJapaneseCalendar](https://developer.apple.com/documentation/foundation/nsjapanesecalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSPersianCalendar](https://developer.apple.com/documentation/foundation/nspersiancalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSRepublicOfChinaCalendar](https://developer.apple.com/documentation/foundation/nsrepublicofchinacalendar)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSLock.hRemoved [-[NSCondition name]](https://developer.apple.com/documentation/foundation/nscondition/1408091-name)Removed [-[NSCondition setName:]](https://developer.apple.com/documentation/foundation/nscondition/1408091-name)Removed [-[NSConditionLock condition]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/instm/NSConditionLock/condition)Removed [-[NSConditionLock name]](https://developer.apple.com/documentation/foundation/nsconditionlock/1411294-name)Removed [-[NSConditionLock setName:]](https://developer.apple.com/documentation/foundation/nsconditionlock/1411294-name)Removed [-[NSLock name]](https://developer.apple.com/documentation/foundation/nslock/1412568-name)Removed [-[NSLock setName:]](https://developer.apple.com/documentation/foundation/nslock/1412568-name)Removed [-[NSRecursiveLock name]](https://developer.apple.com/documentation/foundation/nsrecursivelock/1416232-name)Removed [-[NSRecursiveLock setName:]](https://developer.apple.com/documentation/foundation/nsrecursivelock/1416232-name)Added [NSCondition.name](https://developer.apple.com/documentation/foundation/nscondition/1408091-name)Added [NSConditionLock.condition](https://developer.apple.com/documentation/foundation/nsconditionlock/1408807-condition)Added [NSConditionLock.name](https://developer.apple.com/documentation/foundation/nsconditionlock/1411294-name)Added [NSLock.name](https://developer.apple.com/documentation/foundation/nslock/1412568-name)Added [NSRecursiveLock.name](https://developer.apple.com/documentation/foundation/nsrecursivelock/1416232-name)Modified [-[NSConditionLock initWithCondition:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/instm/NSConditionLock/initWithCondition:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithCondition:(NSInteger)condition ``` | -- |
| To | ``` - (instancetype)initWithCondition:(NSInteger)condition ``` | yes |

NSMapTable.hRemoved [-[NSMapTable count]](https://developer.apple.com/documentation/foundation/nsmaptable/1391360-count)Removed [-[NSMapTable keyPointerFunctions]](https://developer.apple.com/documentation/foundation/nsmaptable/1391412-keypointerfunctions)Removed [-[NSMapTable valuePointerFunctions]](https://developer.apple.com/documentation/foundation/nsmaptable/1391467-valuepointerfunctions)Added [NSMapTable.count](https://developer.apple.com/documentation/foundation/nsmaptable/1391360-count)Added [NSMapTable.keyPointerFunctions](https://developer.apple.com/documentation/foundation/nsmaptable/1391412-keypointerfunctions)Added [NSMapTable.valuePointerFunctions](https://developer.apple.com/documentation/foundation/nsmaptable/1391467-valuepointerfunctions)Modified [-[NSMapTable initWithKeyOptions:valueOptions:capacity:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391382-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithKeyOptions:(NSPointerFunctionsOptions)keyOptions valueOptions:(NSPointerFunctionsOptions)valueOptions capacity:(NSUInteger)initialCapacity ``` | -- |
| To | ``` - (instancetype)initWithKeyOptions:(NSPointerFunctionsOptions)keyOptions valueOptions:(NSPointerFunctionsOptions)valueOptions capacity:(NSUInteger)initialCapacity ``` | yes |

Modified [-[NSMapTable initWithKeyPointerFunctions:valuePointerFunctions:capacity:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391429-initwithkeypointerfunctions)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithKeyPointerFunctions:(NSPointerFunctions *)keyFunctions valuePointerFunctions:(NSPointerFunctions *)valueFunctions capacity:(NSUInteger)initialCapacity ``` | -- |
| To | ``` - (instancetype)initWithKeyPointerFunctions:(NSPointerFunctions *)keyFunctions valuePointerFunctions:(NSPointerFunctions *)valueFunctions capacity:(NSUInteger)initialCapacity ``` | yes |

Modified [+[NSMapTable mapTableWithKeyOptions:valueOptions:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391414-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)mapTableWithKeyOptions:(NSPointerFunctionsOptions)keyOptions valueOptions:(NSPointerFunctionsOptions)valueOptions ``` |
| To | ``` + (NSMapTable *)mapTableWithKeyOptions:(NSPointerFunctionsOptions)keyOptions valueOptions:(NSPointerFunctionsOptions)valueOptions ``` |

Modified [+[NSMapTable strongToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391440-strongtostrongobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (id)strongToStrongObjectsMapTable ``` |
| To | ``` + (NSMapTable *)strongToStrongObjectsMapTable ``` |

Modified [+[NSMapTable strongToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391366-strongtoweakobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (id)strongToWeakObjectsMapTable ``` |
| To | ``` + (NSMapTable *)strongToWeakObjectsMapTable ``` |

Modified [+[NSMapTable weakToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391346-weaktostrongobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (id)weakToStrongObjectsMapTable ``` |
| To | ``` + (NSMapTable *)weakToStrongObjectsMapTable ``` |

Modified [+[NSMapTable weakToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391430-weaktoweakobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (id)weakToWeakObjectsMapTable ``` |
| To | ``` + (NSMapTable *)weakToWeakObjectsMapTable ``` |

NSMassFormatter.h (Added)Added [NSMassFormatter](https://developer.apple.com/documentation/foundation/massformatter)Added [NSMassFormatter.forPersonMassUse](https://developer.apple.com/documentation/foundation/massformatter/1407306-isforpersonmassuse)Added [-[NSMassFormatter getObjectValue:forString:errorDescription:]](https://developer.apple.com/documentation/foundation/nsmassformatter/1417304-getobjectvalue)Added [NSMassFormatter.numberFormatter](https://developer.apple.com/documentation/foundation/nsmassformatter/1418462-numberformatter)Added [-[NSMassFormatter stringFromKilograms:]](https://developer.apple.com/documentation/foundation/nsmassformatter/1414324-stringfromkilograms)Added [-[NSMassFormatter stringFromValue:unit:]](https://developer.apple.com/documentation/foundation/massformatter/1409002-string)Added [-[NSMassFormatter unitStringFromKilograms:usedUnit:]](https://developer.apple.com/documentation/foundation/nsmassformatter/1408475-unitstringfromkilograms)Added [-[NSMassFormatter unitStringFromValue:unit:]](https://developer.apple.com/documentation/foundation/massformatter/1415491-unitstring)Added [NSMassFormatter.unitStyle](https://developer.apple.com/documentation/foundation/massformatter/1411215-unitstyle)Added [NSMassFormatterUnit](https://developer.apple.com/documentation/foundation/massformatter/unit)Added [NSMassFormatterUnitGram](https://developer.apple.com/documentation/foundation/massformatter/unit/gram)Added [NSMassFormatterUnitKilogram](https://developer.apple.com/documentation/foundation/massformatter/unit/kilogram)Added [NSMassFormatterUnitOunce](https://developer.apple.com/documentation/foundation/massformatter/unit/ounce)Added [NSMassFormatterUnitPound](https://developer.apple.com/documentation/foundation/nsmassformatterunit/nsmassformatterunitpound)Added [NSMassFormatterUnitStone](https://developer.apple.com/documentation/foundation/massformatter/unit/stone)NSMetadata.hRemoved [-[NSMetadataItem attributes]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1418347-attributes)Removed [-[NSMetadataQuery delegate]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1413181-delegate)Removed [-[NSMetadataQuery groupedResults]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416579-groupedresults)Removed [-[NSMetadataQuery groupingAttributes]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1409191-groupingattributes)Removed -[NSMetadataQuery init]Removed [-[NSMetadataQuery isGathering]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407539-isgathering)Removed [-[NSMetadataQuery isStarted]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416780-isstarted)Removed [-[NSMetadataQuery isStopped]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411941-stopped)Removed [-[NSMetadataQuery notificationBatchingInterval]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411884-notificationbatchinginterval)Removed [-[NSMetadataQuery operationQueue]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410953-operationqueue)Removed [-[NSMetadataQuery predicate]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411478-predicate)Removed [-[NSMetadataQuery resultCount]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418315-resultcount)Removed [-[NSMetadataQuery results]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1408872-results)Removed [-[NSMetadataQuery searchItems]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411307-searchitems)Removed [-[NSMetadataQuery searchScopes]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1412155-searchscopes)Removed [-[NSMetadataQuery setDelegate:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1413181-delegate)Removed [-[NSMetadataQuery setGroupingAttributes:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1409191-groupingattributes)Removed [-[NSMetadataQuery setNotificationBatchingInterval:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411884-notificationbatchinginterval)Removed [-[NSMetadataQuery setOperationQueue:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410953-operationqueue)Removed [-[NSMetadataQuery setPredicate:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411478-predicate)Removed [-[NSMetadataQuery setSearchItems:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411307-searchitems)Removed [-[NSMetadataQuery setSearchScopes:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1412155-searchscopes)Removed [-[NSMetadataQuery setSortDescriptors:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors)Removed [-[NSMetadataQuery setValueListAttributes:]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407767-valuelistattributes)Removed [-[NSMetadataQuery sortDescriptors]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors)Removed [-[NSMetadataQuery valueListAttributes]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407767-valuelistattributes)Removed [-[NSMetadataQuery valueLists]](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418401-valuelists)Removed [-[NSMetadataQueryAttributeValueTuple attribute]](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1415060-attribute)Removed [-[NSMetadataQueryAttributeValueTuple count]](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1414426-count)Removed [-[NSMetadataQueryAttributeValueTuple value]](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1417894-value)Removed [-[NSMetadataQueryResultGroup attribute]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1411276-attribute)Removed [-[NSMetadataQueryResultGroup resultCount]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1414790-resultcount)Removed [-[NSMetadataQueryResultGroup results]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1410191-results)Removed [-[NSMetadataQueryResultGroup subgroups]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1409929-subgroups)Removed [-[NSMetadataQueryResultGroup value]](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1417674-value)Added [NSMetadataItem.attributes](https://developer.apple.com/documentation/foundation/nsmetadataitem/1418347-attributes)Added [NSMetadataQuery.delegate](https://developer.apple.com/documentation/foundation/nsmetadataquery/1413181-delegate)Added [NSMetadataQuery.gathering](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407539-gathering)Added [NSMetadataQuery.groupedResults](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416579-groupedresults)Added [NSMetadataQuery.groupingAttributes](https://developer.apple.com/documentation/foundation/nsmetadataquery/1409191-groupingattributes)Added [NSMetadataQuery.notificationBatchingInterval](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411884-notificationbatchinginterval)Added [NSMetadataQuery.operationQueue](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410953-operationqueue)Added [NSMetadataQuery.predicate](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411478-predicate)Added [NSMetadataQuery.resultCount](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418315-resultcount)Added [NSMetadataQuery.results](https://developer.apple.com/documentation/foundation/nsmetadataquery/1408872-results)Added [NSMetadataQuery.searchItems](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411307-searchitems)Added [NSMetadataQuery.searchScopes](https://developer.apple.com/documentation/foundation/nsmetadataquery/1412155-searchscopes)Added [NSMetadataQuery.sortDescriptors](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors)Added [NSMetadataQuery.started](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416780-started)Added [NSMetadataQuery.stopped](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411941-isstopped)Added [NSMetadataQuery.valueListAttributes](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407767-valuelistattributes)Added [NSMetadataQuery.valueLists](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418401-valuelists)Added [NSMetadataQueryAttributeValueTuple.attribute](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1415060-attribute)Added [NSMetadataQueryAttributeValueTuple.count](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1414426-count)Added [NSMetadataQueryAttributeValueTuple.value](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple/1417894-value)Added [NSMetadataQueryResultGroup.attribute](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1411276-attribute)Added [NSMetadataQueryResultGroup.resultCount](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1414790-resultcount)Added [NSMetadataQueryResultGroup.results](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1410191-results)Added [NSMetadataQueryResultGroup.subgroups](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1409929-subgroups)Added [NSMetadataQueryResultGroup.value](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1417674-value)Added [NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryaccessibleubiquitousexternaldocumentsscope)Modified [-[NSMetadataItem initWithURL:]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1414919-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url ``` | -- |
| To | ``` - (instancetype)initWithURL:(NSURL *)url ``` | yes |

Modified [-[NSMetadataQueryDelegate metadataQuery:replacementObjectForResultObject:]](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/1407317-metadataquery)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMetadataQueryDelegate metadataQuery:replacementValueForAttribute:value:]](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/1414215-metadataquery)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSMetadataAttributes.hAdded [NSMetadataUbiquitousItemContainerDisplayNameKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemcontainerdisplaynamekey)Added [NSMetadataUbiquitousItemDownloadRequestedKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemdownloadrequestedkey)Added [NSMetadataUbiquitousItemIsExternalDocumentKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemisexternaldocumentkey)Added [NSMetadataUbiquitousItemURLInLocalContainerKey](https://developer.apple.com/documentation/foundation/nsmetadataubiquitousitemurlinlocalcontainerkey)NSMethodSignature.hRemoved [-[NSMethodSignature frameLength]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSMethodSignature/Description.html#//apple_ref/occ/instm/NSMethodSignature/frameLength)Removed [-[NSMethodSignature methodReturnLength]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSMethodSignature/Description.html#//apple_ref/occ/instm/NSMethodSignature/methodReturnLength)Removed [-[NSMethodSignature methodReturnType]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSMethodSignature/Description.html#//apple_ref/occ/instm/NSMethodSignature/methodReturnType)Removed [-[NSMethodSignature numberOfArguments]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSMethodSignature/Description.html#//apple_ref/occ/instm/NSMethodSignature/numberOfArguments)Added [NSMethodSignature.frameLength](https://developer.apple.com/documentation/foundation/nsmethodsignature/1519658-framelength)Added [NSMethodSignature.methodReturnLength](https://developer.apple.com/documentation/foundation/nsmethodsignature/1519666-methodreturnlength)Added [NSMethodSignature.methodReturnType](https://developer.apple.com/documentation/foundation/nsmethodsignature/1519667-methodreturntype)Added [NSMethodSignature.numberOfArguments](https://developer.apple.com/documentation/foundation/nsmethodsignature/1519662-numberofarguments)NSNetServices.hAdded [NSNetService.includesPeerToPeer](https://developer.apple.com/documentation/foundation/netservice/1414086-includespeertopeer)Added [NSNetServiceBrowser.includesPeerToPeer](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1413106-includespeertopeer)Modified [-[NSNetService initWithDomain:type:name:]](https://developer.apple.com/documentation/foundation/nsnetservice/1417615-initwithdomain)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDomain:(NSString *)domain type:(NSString *)type name:(NSString *)name ``` |
| To | ``` - (instancetype)initWithDomain:(NSString *)domain type:(NSString *)type name:(NSString *)name ``` |

Modified [-[NSNetService initWithDomain:type:name:port:]](https://developer.apple.com/documentation/foundation/nsnetservice/1413364-initwithdomain)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDomain:(NSString *)domain type:(NSString *)type name:(NSString *)name port:(int)port ``` |
| To | ``` - (instancetype)initWithDomain:(NSString *)domain type:(NSString *)type name:(NSString *)name port:(int)port ``` |

Modified [-[NSNetServiceBrowser init]](https://developer.apple.com/documentation/foundation/netservicebrowser/1412947-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didFindDomain:moreComing:]](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/1407204-netservicebrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didFindService:moreComing:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1417979-netservicebrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didNotSearch:]](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/1410567-netservicebrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didRemoveDomain:moreComing:]](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/1412712-netservicebrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didRemoveService:moreComing:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1412917-netservicebrowser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowserDidStopSearch:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1418341-netservicebrowserdidstopsearch)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowserWillSearch:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1408173-netservicebrowserwillsearch)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netService:didAcceptConnectionWithInputStream:outputStream:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1407489-netservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netService:didNotPublish:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1417101-netservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netService:didNotResolve:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1414161-netservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netService:didUpdateTXTRecordData:]](https://developer.apple.com/documentation/foundation/netservicedelegate/1413199-netservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netServiceDidPublish:]](https://developer.apple.com/documentation/foundation/netservicedelegate/1416802-netservicedidpublish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netServiceDidResolveAddress:]](https://developer.apple.com/documentation/foundation/netservicedelegate/1408457-netservicedidresolveaddress)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netServiceDidStop:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1409726-netservicedidstop)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netServiceWillPublish:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1414277-netservicewillpublish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceDelegate netServiceWillResolve:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1416022-netservicewillresolve)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSNotification.hRemoved [-[NSNotification name]](https://developer.apple.com/documentation/foundation/nsnotification/1416472-name)Removed [-[NSNotification object]](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object)Removed [-[NSNotification userInfo]](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo)Removed -[NSNotificationCenter init]Added [-[NSNotification initWithCoder:]](https://developer.apple.com/documentation/foundation/nsnotification/1412464-init)Added [NSNotification.name](https://developer.apple.com/documentation/foundation/nsnotification/1416472-name)Added [NSNotification.object](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object)Added [NSNotification.userInfo](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo)Modified [-[NSNotification init]](https://developer.apple.com/documentation/foundation/nsnotification/1412595-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSNotification initWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1415764-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNotificationCenter addObserverForName:object:queue:usingBlock:]](https://developer.apple.com/documentation/foundation/nsnotificationcenter/1411723-addobserverforname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)addObserverForName:(NSString *)name object:(id)obj queue:(NSOperationQueue *)queue usingBlock:(void (^)(NSNotification *note))block ``` |
| To | ``` - (id<NSObject>)addObserverForName:(NSString *)name object:(id)obj queue:(NSOperationQueue *)queue usingBlock:(void (^)(NSNotification *note))block ``` |

Modified [+[NSNotificationCenter defaultCenter]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/clm/NSNotificationCenter/defaultCenter)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)defaultCenter ``` |
| To | ``` + (NSNotificationCenter *)defaultCenter ``` |

NSNotificationQueue.hModified [+[NSNotificationQueue defaultQueue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/clm/NSNotificationQueue/defaultQueue)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultQueue ``` |
| To | ``` + (NSNotificationQueue *)defaultQueue ``` |

Modified [-[NSNotificationQueue initWithNotificationCenter:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/instm/NSNotificationQueue/initWithNotificationCenter:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithNotificationCenter:(NSNotificationCenter *)notificationCenter ``` | -- |
| To | ``` - (instancetype)initWithNotificationCenter:(NSNotificationCenter *)notificationCenter ``` | yes |

NSNumberFormatter.hRemoved [-[NSNumberFormatter allowsFloats]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/allowsFloats)Removed [-[NSNumberFormatter alwaysShowsDecimalSeparator]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408550-alwaysshowsdecimalseparator)Removed [-[NSNumberFormatter attributedStringForNil]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/attributedStringForNil)Removed [-[NSNumberFormatter attributedStringForNotANumber]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/attributedStringForNotANumber)Removed [-[NSNumberFormatter attributedStringForZero]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/attributedStringForZero)Removed [-[NSNumberFormatter currencyCode]](https://developer.apple.com/documentation/foundation/numberformatter/1410463-currencycode)Removed [-[NSNumberFormatter currencyDecimalSeparator]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407247-currencydecimalseparator)Removed [-[NSNumberFormatter currencyGroupingSeparator]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416213-currencygroupingseparator)Removed [-[NSNumberFormatter currencySymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1414668-currencysymbol)Removed [-[NSNumberFormatter decimalSeparator]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/decimalSeparator)Removed [-[NSNumberFormatter exponentSymbol]](https://developer.apple.com/documentation/foundation/numberformatter/1417223-exponentsymbol)Removed [-[NSNumberFormatter format]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/format)Removed [-[NSNumberFormatter formatWidth]](https://developer.apple.com/documentation/foundation/numberformatter/1411919-formatwidth)Removed [-[NSNumberFormatter formatterBehavior]](https://developer.apple.com/documentation/foundation/numberformatter/1417642-formatterbehavior)Removed [-[NSNumberFormatter generatesDecimalNumbers]](https://developer.apple.com/documentation/foundation/numberformatter/1410503-generatesdecimalnumbers)Removed [-[NSNumberFormatter groupingSeparator]](https://developer.apple.com/documentation/foundation/numberformatter/1412157-groupingseparator)Removed [-[NSNumberFormatter groupingSize]](https://developer.apple.com/documentation/foundation/numberformatter/1416167-groupingsize)Removed [-[NSNumberFormatter hasThousandSeparators]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/hasThousandSeparators)Removed [-[NSNumberFormatter internationalCurrencySymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412755-internationalcurrencysymbol)Removed [-[NSNumberFormatter isLenient]](https://developer.apple.com/documentation/foundation/numberformatter/1416953-islenient)Removed [-[NSNumberFormatter isPartialStringValidationEnabled]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412244-partialstringvalidationenabled)Removed [-[NSNumberFormatter locale]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416967-locale)Removed [-[NSNumberFormatter localizesFormat]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/localizesFormat)Removed [-[NSNumberFormatter maximum]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/maximum)Removed [-[NSNumberFormatter maximumFractionDigits]](https://developer.apple.com/documentation/foundation/numberformatter/1415364-maximumfractiondigits)Removed [-[NSNumberFormatter maximumIntegerDigits]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407284-maximumintegerdigits)Removed [-[NSNumberFormatter maximumSignificantDigits]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412008-maximumsignificantdigits)Removed [-[NSNumberFormatter minimum]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/minimum)Removed [-[NSNumberFormatter minimumFractionDigits]](https://developer.apple.com/documentation/foundation/numberformatter/1410459-minimumfractiondigits)Removed [-[NSNumberFormatter minimumIntegerDigits]](https://developer.apple.com/documentation/foundation/numberformatter/1410052-minimumintegerdigits)Removed [-[NSNumberFormatter minimumSignificantDigits]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410174-minimumsignificantdigits)Removed [-[NSNumberFormatter minusSign]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1409416-minussign)Removed [-[NSNumberFormatter multiplier]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408601-multiplier)Removed [-[NSNumberFormatter negativeFormat]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/negativeFormat)Removed [-[NSNumberFormatter negativeInfinitySymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417968-negativeinfinitysymbol)Removed [-[NSNumberFormatter negativePrefix]](https://developer.apple.com/documentation/foundation/numberformatter/1408096-negativeprefix)Removed [-[NSNumberFormatter negativeSuffix]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1413927-negativesuffix)Removed [-[NSNumberFormatter nilSymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412699-nilsymbol)Removed [-[NSNumberFormatter notANumberSymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416993-notanumbersymbol)Removed [-[NSNumberFormatter numberStyle]](https://developer.apple.com/documentation/foundation/numberformatter/1416915-numberstyle)Removed [-[NSNumberFormatter paddingCharacter]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1413690-paddingcharacter)Removed [-[NSNumberFormatter paddingPosition]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1411127-paddingposition)Removed [-[NSNumberFormatter perMillSymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412399-permillsymbol)Removed [-[NSNumberFormatter percentSymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407789-percentsymbol)Removed [-[NSNumberFormatter plusSign]](https://developer.apple.com/documentation/foundation/numberformatter/1416423-plussign)Removed [-[NSNumberFormatter positiveFormat]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/positiveFormat)Removed [-[NSNumberFormatter positiveInfinitySymbol]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412976-positiveinfinitysymbol)Removed [-[NSNumberFormatter positivePrefix]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1414204-positiveprefix)Removed [-[NSNumberFormatter positiveSuffix]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415071-positivesuffix)Removed [-[NSNumberFormatter roundingBehavior]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/roundingBehavior)Removed [-[NSNumberFormatter roundingIncrement]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412561-roundingincrement)Removed [-[NSNumberFormatter roundingMode]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1411156-roundingmode)Removed [-[NSNumberFormatter secondaryGroupingSize]](https://developer.apple.com/documentation/foundation/numberformatter/1413348-secondarygroupingsize)Removed [-[NSNumberFormatter setAllowsFloats:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setAllowsFloats:)Removed [-[NSNumberFormatter setAlwaysShowsDecimalSeparator:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408550-alwaysshowsdecimalseparator)Removed [-[NSNumberFormatter setAttributedStringForNil:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setAttributedStringForNil:)Removed [-[NSNumberFormatter setAttributedStringForNotANumber:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setAttributedStringForNotANumber:)Removed [-[NSNumberFormatter setAttributedStringForZero:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setAttributedStringForZero:)Removed [-[NSNumberFormatter setCurrencyCode:]](https://developer.apple.com/documentation/foundation/numberformatter/1410463-currencycode)Removed [-[NSNumberFormatter setCurrencyDecimalSeparator:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407247-currencydecimalseparator)Removed [-[NSNumberFormatter setCurrencyGroupingSeparator:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416213-currencygroupingseparator)Removed [-[NSNumberFormatter setCurrencySymbol:]](https://developer.apple.com/documentation/foundation/numberformatter/1414668-currencysymbol)Removed [-[NSNumberFormatter setDecimalSeparator:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setDecimalSeparator:)Removed [-[NSNumberFormatter setExponentSymbol:]](https://developer.apple.com/documentation/foundation/numberformatter/1417223-exponentsymbol)Removed [-[NSNumberFormatter setFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setFormat:)Removed [-[NSNumberFormatter setFormatWidth:]](https://developer.apple.com/documentation/foundation/numberformatter/1411919-formatwidth)Removed [-[NSNumberFormatter setFormatterBehavior:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417642-formatterbehavior)Removed [-[NSNumberFormatter setGeneratesDecimalNumbers:]](https://developer.apple.com/documentation/foundation/numberformatter/1410503-generatesdecimalnumbers)Removed [-[NSNumberFormatter setGroupingSeparator:]](https://developer.apple.com/documentation/foundation/numberformatter/1412157-groupingseparator)Removed [-[NSNumberFormatter setGroupingSize:]](https://developer.apple.com/documentation/foundation/numberformatter/1416167-groupingsize)Removed [-[NSNumberFormatter setHasThousandSeparators:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setHasThousandSeparators:)Removed [-[NSNumberFormatter setInternationalCurrencySymbol:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412755-internationalcurrencysymbol)Removed [-[NSNumberFormatter setLenient:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416953-lenient)Removed [-[NSNumberFormatter setLocale:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416967-locale)Removed [-[NSNumberFormatter setLocalizesFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setLocalizesFormat:)Removed [-[NSNumberFormatter setMaximum:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setMaximum:)Removed [-[NSNumberFormatter setMaximumFractionDigits:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415364-maximumfractiondigits)Removed [-[NSNumberFormatter setMaximumIntegerDigits:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407284-maximumintegerdigits)Removed [-[NSNumberFormatter setMaximumSignificantDigits:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412008-maximumsignificantdigits)Removed [-[NSNumberFormatter setMinimum:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setMinimum:)Removed [-[NSNumberFormatter setMinimumFractionDigits:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410459-minimumfractiondigits)Removed [-[NSNumberFormatter setMinimumIntegerDigits:]](https://developer.apple.com/documentation/foundation/numberformatter/1410052-minimumintegerdigits)Removed [-[NSNumberFormatter setMinimumSignificantDigits:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410174-minimumsignificantdigits)Removed [-[NSNumberFormatter setMinusSign:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1409416-minussign)Removed [-[NSNumberFormatter setMultiplier:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408601-multiplier)Removed [-[NSNumberFormatter setNegativeFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setNegativeFormat:)Removed [-[NSNumberFormatter setNegativeInfinitySymbol:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417968-negativeinfinitysymbol)Removed [-[NSNumberFormatter setNegativePrefix:]](https://developer.apple.com/documentation/foundation/numberformatter/1408096-negativeprefix)Removed [-[NSNumberFormatter setNegativeSuffix:]](https://developer.apple.com/documentation/foundation/numberformatter/1413927-negativesuffix)Removed [-[NSNumberFormatter setNilSymbol:]](https://developer.apple.com/documentation/foundation/numberformatter/1412699-nilsymbol)Removed [-[NSNumberFormatter setNotANumberSymbol:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416993-notanumbersymbol)Removed [-[NSNumberFormatter setNumberStyle:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416915-numberstyle)Removed [-[NSNumberFormatter setPaddingCharacter:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1413690-paddingcharacter)Removed [-[NSNumberFormatter setPaddingPosition:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1411127-paddingposition)Removed [-[NSNumberFormatter setPartialStringValidationEnabled:]](https://developer.apple.com/documentation/foundation/numberformatter/1412244-ispartialstringvalidationenabled)Removed [-[NSNumberFormatter setPerMillSymbol:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412399-permillsymbol)Removed [-[NSNumberFormatter setPercentSymbol:]](https://developer.apple.com/documentation/foundation/numberformatter/1407789-percentsymbol)Removed [-[NSNumberFormatter setPlusSign:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416423-plussign)Removed [-[NSNumberFormatter setPositiveFormat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setPositiveFormat:)Removed [-[NSNumberFormatter setPositiveInfinitySymbol:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412976-positiveinfinitysymbol)Removed [-[NSNumberFormatter setPositivePrefix:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1414204-positiveprefix)Removed [-[NSNumberFormatter setPositiveSuffix:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415071-positivesuffix)Removed [-[NSNumberFormatter setRoundingBehavior:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setRoundingBehavior:)Removed [-[NSNumberFormatter setRoundingIncrement:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412561-roundingincrement)Removed [-[NSNumberFormatter setRoundingMode:]](https://developer.apple.com/documentation/foundation/numberformatter/1411156-roundingmode)Removed [-[NSNumberFormatter setSecondaryGroupingSize:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1413348-secondarygroupingsize)Removed [-[NSNumberFormatter setTextAttributesForNegativeInfinity:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410417-textattributesfornegativeinfinit)Removed [-[NSNumberFormatter setTextAttributesForNegativeValues:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setTextAttributesForNegativeValues:)Removed [-[NSNumberFormatter setTextAttributesForNil:]](https://developer.apple.com/documentation/foundation/numberformatter/1408943-textattributesfornil)Removed [-[NSNumberFormatter setTextAttributesForNotANumber:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410959-textattributesfornotanumber)Removed [-[NSNumberFormatter setTextAttributesForPositiveInfinity:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408176-textattributesforpositiveinfinit)Removed [-[NSNumberFormatter setTextAttributesForPositiveValues:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setTextAttributesForPositiveValues:)Removed [-[NSNumberFormatter setTextAttributesForZero:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415971-textattributesforzero)Removed [-[NSNumberFormatter setThousandSeparator:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setThousandSeparator:)Removed [-[NSNumberFormatter setUsesGroupingSeparator:]](https://developer.apple.com/documentation/foundation/numberformatter/1409880-usesgroupingseparator)Removed [-[NSNumberFormatter setUsesSignificantDigits:]](https://developer.apple.com/documentation/foundation/numberformatter/1417793-usessignificantdigits)Removed [-[NSNumberFormatter setZeroSymbol:]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410405-zerosymbol)Removed [-[NSNumberFormatter textAttributesForNegativeInfinity]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410417-textattributesfornegativeinfinit)Removed [-[NSNumberFormatter textAttributesForNegativeValues]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/textAttributesForNegativeValues)Removed [-[NSNumberFormatter textAttributesForNil]](https://developer.apple.com/documentation/foundation/numberformatter/1408943-textattributesfornil)Removed [-[NSNumberFormatter textAttributesForNotANumber]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410959-textattributesfornotanumber)Removed [-[NSNumberFormatter textAttributesForPositiveInfinity]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408176-textattributesforpositiveinfinit)Removed [-[NSNumberFormatter textAttributesForPositiveValues]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/textAttributesForPositiveValues)Removed [-[NSNumberFormatter textAttributesForZero]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415971-textattributesforzero)Removed [-[NSNumberFormatter thousandSeparator]](https://developer.apple.com/documentation/foundation/numberformatter/1412771-thousandseparator)Removed [-[NSNumberFormatter usesGroupingSeparator]](https://developer.apple.com/documentation/foundation/numberformatter/1409880-usesgroupingseparator)Removed [-[NSNumberFormatter usesSignificantDigits]](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417793-usessignificantdigits)Removed [-[NSNumberFormatter zeroSymbol]](https://developer.apple.com/documentation/foundation/numberformatter/1410405-zerosymbol)Added [NSNumberFormatter.allowsFloats](https://developer.apple.com/documentation/foundation/numberformatter/1416119-allowsfloats)Added [NSNumberFormatter.alwaysShowsDecimalSeparator](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408550-alwaysshowsdecimalseparator)Added [NSNumberFormatter.attributedStringForNil](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416184-attributedstringfornil)Added [NSNumberFormatter.attributedStringForNotANumber](https://developer.apple.com/documentation/foundation/numberformatter/1416819-attributedstringfornotanumber)Added [NSNumberFormatter.attributedStringForZero](https://developer.apple.com/documentation/foundation/numberformatter/1415516-attributedstringforzero)Added [NSNumberFormatter.currencyCode](https://developer.apple.com/documentation/foundation/numberformatter/1410463-currencycode)Added [NSNumberFormatter.currencyDecimalSeparator](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407247-currencydecimalseparator)Added [NSNumberFormatter.currencyGroupingSeparator](https://developer.apple.com/documentation/foundation/numberformatter/1416213-currencygroupingseparator)Added [NSNumberFormatter.currencySymbol](https://developer.apple.com/documentation/foundation/nsnumberformatter/1414668-currencysymbol)Added [NSNumberFormatter.decimalSeparator](https://developer.apple.com/documentation/foundation/numberformatter/1408029-decimalseparator)Added [NSNumberFormatter.exponentSymbol](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417223-exponentsymbol)Added [NSNumberFormatter.format](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410565-format)Added [NSNumberFormatter.formatWidth](https://developer.apple.com/documentation/foundation/nsnumberformatter/1411919-formatwidth)Added [NSNumberFormatter.formatterBehavior](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417642-formatterbehavior)Added [NSNumberFormatter.formattingContext](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408543-formattingcontext)Added [NSNumberFormatter.generatesDecimalNumbers](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410503-generatesdecimalnumbers)Added [NSNumberFormatter.groupingSeparator](https://developer.apple.com/documentation/foundation/numberformatter/1412157-groupingseparator)Added [NSNumberFormatter.groupingSize](https://developer.apple.com/documentation/foundation/numberformatter/1416167-groupingsize)Added [NSNumberFormatter.hasThousandSeparators](https://developer.apple.com/documentation/foundation/numberformatter/1416451-hasthousandseparators)Added [NSNumberFormatter.internationalCurrencySymbol](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412755-internationalcurrencysymbol)Added [NSNumberFormatter.lenient](https://developer.apple.com/documentation/foundation/numberformatter/1416953-islenient)Added [NSNumberFormatter.locale](https://developer.apple.com/documentation/foundation/numberformatter/1416967-locale)Added [NSNumberFormatter.localizesFormat](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408133-localizesformat)Added [NSNumberFormatter.maximum](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417787-maximum)Added [NSNumberFormatter.maximumFractionDigits](https://developer.apple.com/documentation/foundation/numberformatter/1415364-maximumfractiondigits)Added [NSNumberFormatter.maximumIntegerDigits](https://developer.apple.com/documentation/foundation/nsnumberformatter/1407284-maximumintegerdigits)Added [NSNumberFormatter.maximumSignificantDigits](https://developer.apple.com/documentation/foundation/numberformatter/1412008-maximumsignificantdigits)Added [NSNumberFormatter.minimum](https://developer.apple.com/documentation/foundation/numberformatter/1417228-minimum)Added [NSNumberFormatter.minimumFractionDigits](https://developer.apple.com/documentation/foundation/numberformatter/1410459-minimumfractiondigits)Added [NSNumberFormatter.minimumIntegerDigits](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410052-minimumintegerdigits)Added [NSNumberFormatter.minimumSignificantDigits](https://developer.apple.com/documentation/foundation/numberformatter/1410174-minimumsignificantdigits)Added [NSNumberFormatter.minusSign](https://developer.apple.com/documentation/foundation/nsnumberformatter/1409416-minussign)Added [NSNumberFormatter.multiplier](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408601-multiplier)Added [NSNumberFormatter.negativeFormat](https://developer.apple.com/documentation/foundation/numberformatter/1414039-negativeformat)Added [NSNumberFormatter.negativeInfinitySymbol](https://developer.apple.com/documentation/foundation/numberformatter/1417968-negativeinfinitysymbol)Added [NSNumberFormatter.negativePrefix](https://developer.apple.com/documentation/foundation/numberformatter/1408096-negativeprefix)Added [NSNumberFormatter.negativeSuffix](https://developer.apple.com/documentation/foundation/nsnumberformatter/1413927-negativesuffix)Added [NSNumberFormatter.nilSymbol](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412699-nilsymbol)Added [NSNumberFormatter.notANumberSymbol](https://developer.apple.com/documentation/foundation/numberformatter/1416993-notanumbersymbol)Added [NSNumberFormatter.numberStyle](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416915-numberstyle)Added [NSNumberFormatter.paddingCharacter](https://developer.apple.com/documentation/foundation/numberformatter/1413690-paddingcharacter)Added [NSNumberFormatter.paddingPosition](https://developer.apple.com/documentation/foundation/nsnumberformatter/1411127-paddingposition)Added [NSNumberFormatter.partialStringValidationEnabled](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412244-partialstringvalidationenabled)Added [NSNumberFormatter.perMillSymbol](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412399-permillsymbol)Added [NSNumberFormatter.percentSymbol](https://developer.apple.com/documentation/foundation/numberformatter/1407789-percentsymbol)Added [NSNumberFormatter.plusSign](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416423-plussign)Added [NSNumberFormatter.positiveFormat](https://developer.apple.com/documentation/foundation/numberformatter/1410737-positiveformat)Added [NSNumberFormatter.positiveInfinitySymbol](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412976-positiveinfinitysymbol)Added [NSNumberFormatter.positivePrefix](https://developer.apple.com/documentation/foundation/numberformatter/1414204-positiveprefix)Added [NSNumberFormatter.positiveSuffix](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415071-positivesuffix)Added [NSNumberFormatter.roundingBehavior](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415880-roundingbehavior)Added [NSNumberFormatter.roundingIncrement](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412561-roundingincrement)Added [NSNumberFormatter.roundingMode](https://developer.apple.com/documentation/foundation/numberformatter/1411156-roundingmode)Added [NSNumberFormatter.secondaryGroupingSize](https://developer.apple.com/documentation/foundation/numberformatter/1413348-secondarygroupingsize)Added [NSNumberFormatter.textAttributesForNegativeInfinity](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410417-textattributesfornegativeinfinit)Added [NSNumberFormatter.textAttributesForNegativeValues](https://developer.apple.com/documentation/foundation/nsnumberformatter/1414530-textattributesfornegativevalues)Added [NSNumberFormatter.textAttributesForNil](https://developer.apple.com/documentation/foundation/numberformatter/1408943-textattributesfornil)Added [NSNumberFormatter.textAttributesForNotANumber](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410959-textattributesfornotanumber)Added [NSNumberFormatter.textAttributesForPositiveInfinity](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408176-textattributesforpositiveinfinit)Added [NSNumberFormatter.textAttributesForPositiveValues](https://developer.apple.com/documentation/foundation/nsnumberformatter/1409563-textattributesforpositivevalues)Added [NSNumberFormatter.textAttributesForZero](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415971-textattributesforzero)Added [NSNumberFormatter.thousandSeparator](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412771-thousandseparator)Added [NSNumberFormatter.usesGroupingSeparator](https://developer.apple.com/documentation/foundation/numberformatter/1409880-usesgroupingseparator)Added [NSNumberFormatter.usesSignificantDigits](https://developer.apple.com/documentation/foundation/nsnumberformatter/1417793-usessignificantdigits)Added [NSNumberFormatter.zeroSymbol](https://developer.apple.com/documentation/foundation/numberformatter/1410405-zerosymbol)NSObjCRuntime.hAdded [#def NSFoundationVersionNumber10_9](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_9)Added [#def NSFoundationVersionNumber10_9_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_9_1)Added [#def NSFoundationVersionNumber10_9_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_9_2)Added [NSQualityOfService](https://developer.apple.com/documentation/foundation/nsqualityofservice)Added [NSQualityOfServiceBackground](https://developer.apple.com/documentation/foundation/qualityofservice/background)Added [NSQualityOfServiceDefault](https://developer.apple.com/documentation/foundation/qualityofservice/default)Added [NSQualityOfServiceUserInitiated](https://developer.apple.com/documentation/foundation/nsqualityofservice/nsqualityofserviceuserinitiated)Added [NSQualityOfServiceUserInteractive](https://developer.apple.com/documentation/foundation/nsqualityofservice/nsqualityofserviceuserinteractive)Added [NSQualityOfServiceUtility](https://developer.apple.com/documentation/foundation/nsqualityofservice/nsqualityofserviceutility)Added #def NS_DESIGNATED_INITIALIZERAdded #def NS_EXTENSION_UNAVAILABLEAdded #def NS_EXTENSION_UNAVAILABLE_IOSAdded #def NS_EXTENSION_UNAVAILABLE_MACAdded #def NS_PROTOCOL_REQUIRES_EXPLICIT_IMPLEMENTATIONNSObject.hRemoved [-[NSObject autoContentAccessingProxy]](https://developer.apple.com/documentation/objectivec/nsobject/1409224-autocontentaccessingproxy)Removed [-[NSObject classForCoder]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/classForCoder)Added [NSObject.autoContentAccessingProxy](https://developer.apple.com/documentation/objectivec/nsobject/1409224-autocontentaccessingproxy)Added [NSObject.classForCoder](https://developer.apple.com/documentation/objectivec/nsobject/1411876-classforcoder)NSObjectScripting.hRemoved [-[NSObject scriptingProperties]](https://developer.apple.com/documentation/objectivec/nsobject/1417254-scriptingproperties)Removed [-[NSObject setScriptingProperties:]](https://developer.apple.com/documentation/objectivec/nsobject/1417254-scriptingproperties)Added [NSObject.scriptingProperties](https://developer.apple.com/documentation/objectivec/nsobject/1417254-scriptingproperties)NSOperation.hRemoved [-[NSBlockOperation executionBlocks]](https://developer.apple.com/documentation/foundation/nsblockoperation/1416555-executionblocks)Removed [-[NSInvocationOperation invocation]](https://developer.apple.com/documentation/foundation/nsinvocationoperation/1543655-invocation)Removed [-[NSInvocationOperation result]](https://developer.apple.com/documentation/foundation/nsinvocationoperation/1543615-result)Removed [-[NSOperation completionBlock]](https://developer.apple.com/documentation/foundation/nsoperation/1408085-completionblock)Removed [-[NSOperation dependencies]](https://developer.apple.com/documentation/foundation/nsoperation/1416668-dependencies)Removed [-[NSOperation init]](https://developer.apple.com/documentation/foundation/nsoperation/1808546-init)Removed [-[NSOperation isCancelled]](https://developer.apple.com/documentation/foundation/operation/1408418-iscancelled)Removed [-[NSOperation isConcurrent]](https://developer.apple.com/documentation/foundation/nsoperation/1411089-concurrent)Removed [-[NSOperation isExecuting]](https://developer.apple.com/documentation/foundation/operation/1415621-isexecuting)Removed [-[NSOperation isFinished]](https://developer.apple.com/documentation/foundation/operation/1413540-isfinished)Removed [-[NSOperation isReady]](https://developer.apple.com/documentation/foundation/nsoperation/1412992-ready)Removed [-[NSOperation queuePriority]](https://developer.apple.com/documentation/foundation/nsoperation/1411204-queuepriority)Removed [-[NSOperation setCompletionBlock:]](https://developer.apple.com/documentation/foundation/nsoperation/1408085-completionblock)Removed [-[NSOperation setQueuePriority:]](https://developer.apple.com/documentation/foundation/operation/1411204-queuepriority)Removed [-[NSOperation setThreadPriority:]](https://developer.apple.com/documentation/foundation/operation/1409020-threadpriority)Removed [-[NSOperation threadPriority]](https://developer.apple.com/documentation/foundation/operation/1409020-threadpriority)Removed [-[NSOperationQueue isSuspended]](https://developer.apple.com/documentation/foundation/nsoperationqueue/1415909-suspended)Removed [-[NSOperationQueue maxConcurrentOperationCount]](https://developer.apple.com/documentation/foundation/nsoperationqueue/1414982-maxconcurrentoperationcount)Removed [-[NSOperationQueue name]](https://developer.apple.com/documentation/foundation/operationqueue/1418063-name)Removed [-[NSOperationQueue operationCount]](https://developer.apple.com/documentation/foundation/nsoperationqueue/1415115-operationcount)Removed [-[NSOperationQueue operations]](https://developer.apple.com/documentation/foundation/nsoperationqueue/1415168-operations)Removed [-[NSOperationQueue setMaxConcurrentOperationCount:]](https://developer.apple.com/documentation/foundation/nsoperationqueue/1414982-maxconcurrentoperationcount)Removed [-[NSOperationQueue setName:]](https://developer.apple.com/documentation/foundation/operationqueue/1418063-name)Removed [-[NSOperationQueue setSuspended:]](https://developer.apple.com/documentation/foundation/nsoperationqueue/1415909-suspended)Added [NSBlockOperation.executionBlocks](https://developer.apple.com/documentation/foundation/nsblockoperation/1416555-executionblocks)Added [NSInvocationOperation.invocation](https://developer.apple.com/documentation/foundation/nsinvocationoperation/1543655-invocation)Added [NSInvocationOperation.result](https://developer.apple.com/documentation/foundation/nsinvocationoperation/1543615-result)Added [NSOperation.asynchronous](https://developer.apple.com/documentation/foundation/nsoperation/1408275-asynchronous)Added [NSOperation.cancelled](https://developer.apple.com/documentation/foundation/operation/1408418-iscancelled)Added [NSOperation.completionBlock](https://developer.apple.com/documentation/foundation/operation/1408085-completionblock)Added [NSOperation.concurrent](https://developer.apple.com/documentation/foundation/operation/1411089-isconcurrent)Added [NSOperation.dependencies](https://developer.apple.com/documentation/foundation/operation/1416668-dependencies)Added [NSOperation.executing](https://developer.apple.com/documentation/foundation/operation/1415621-isexecuting)Added [NSOperation.finished](https://developer.apple.com/documentation/foundation/nsoperation/1413540-finished)Added [NSOperation.name](https://developer.apple.com/documentation/foundation/operation/1416089-name)Added [NSOperation.qualityOfService](https://developer.apple.com/documentation/foundation/operation/1413553-qualityofservice)Added [NSOperation.queuePriority](https://developer.apple.com/documentation/foundation/operation/1411204-queuepriority)Added [NSOperation.ready](https://developer.apple.com/documentation/foundation/nsoperation/1412992-ready)Added [NSOperation.threadPriority](https://developer.apple.com/documentation/foundation/operation/1409020-threadpriority)Added [NSOperationQueue.maxConcurrentOperationCount](https://developer.apple.com/documentation/foundation/operationqueue/1414982-maxconcurrentoperationcount)Added [NSOperationQueue.name](https://developer.apple.com/documentation/foundation/operationqueue/1418063-name)Added [NSOperationQueue.operationCount](https://developer.apple.com/documentation/foundation/nsoperationqueue/1415115-operationcount)Added [NSOperationQueue.operations](https://developer.apple.com/documentation/foundation/operationqueue/1415168-operations)Added [NSOperationQueue.qualityOfService](https://developer.apple.com/documentation/foundation/operationqueue/1417919-qualityofservice)Added [NSOperationQueue.suspended](https://developer.apple.com/documentation/foundation/nsoperationqueue/1415909-suspended)Added [NSOperationQueue.underlyingQueue](https://developer.apple.com/documentation/foundation/operationqueue/1415344-underlyingqueue)Added #def NSOperationQualityOfServiceAdded #def NSOperationQualityOfServiceBackgroundAdded #def NSOperationQualityOfServiceUserInitiatedAdded #def NSOperationQualityOfServiceUserInteractiveAdded #def NSOperationQualityOfServiceUtilityModified [+[NSBlockOperation blockOperationWithBlock:]](https://developer.apple.com/documentation/foundation/nsblockoperation/1412757-blockoperationwithblock)

|  | Declaration |
| --- | --- |
| From | ``` + (id)blockOperationWithBlock:(void (^)(void))block ``` |
| To | ``` + (instancetype)blockOperationWithBlock:(void (^)(void))block ``` |

Modified [-[NSInvocationOperation initWithInvocation:]](https://developer.apple.com/documentation/foundation/nsinvocationoperation/1543647-initwithinvocation)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithInvocation:(NSInvocation *)inv ``` | -- |
| To | ``` - (instancetype)initWithInvocation:(NSInvocation *)inv ``` | yes |

Modified [-[NSInvocationOperation initWithTarget:selector:object:]](https://developer.apple.com/documentation/foundation/nsinvocationoperation/1543653-initwithtarget)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTarget:(id)target selector:(SEL)sel object:(id)arg ``` |
| To | ``` - (instancetype)initWithTarget:(id)target selector:(SEL)sel object:(id)arg ``` |

Modified [+[NSOperationQueue currentQueue]](https://developer.apple.com/documentation/foundation/nsoperationqueue/1413097-currentqueue)

|  | Declaration |
| --- | --- |
| From | ``` + (id)currentQueue ``` |
| To | ``` + (NSOperationQueue *)currentQueue ``` |

Modified [+[NSOperationQueue mainQueue]](https://developer.apple.com/documentation/foundation/operationqueue/1409193-main)

|  | Declaration |
| --- | --- |
| From | ``` + (id)mainQueue ``` |
| To | ``` + (NSOperationQueue *)mainQueue ``` |

NSOrderedSet.hRemoved [-[NSOrderedSet array]](https://developer.apple.com/documentation/foundation/nsorderedset/1411531-array)Removed [-[NSOrderedSet count]](https://developer.apple.com/documentation/foundation/nsorderedset/1410106-count)Removed [-[NSOrderedSet description]](https://developer.apple.com/documentation/foundation/nsorderedset/1415872-description)Removed [-[NSOrderedSet firstObject]](https://developer.apple.com/documentation/foundation/nsorderedset/1409765-firstobject)Removed [-[NSOrderedSet lastObject]](https://developer.apple.com/documentation/foundation/nsorderedset/1409143-lastobject)Removed [-[NSOrderedSet reversedOrderedSet]](https://developer.apple.com/documentation/foundation/nsorderedset/1411022-reversedorderedset)Removed [-[NSOrderedSet set]](https://developer.apple.com/documentation/foundation/nsorderedset/1413944-set)Added [-[NSMutableOrderedSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1413074-init)Added [NSOrderedSet.array](https://developer.apple.com/documentation/foundation/nsorderedset/1411531-array)Added [NSOrderedSet.count](https://developer.apple.com/documentation/foundation/nsorderedset/1410106-count)Added [NSOrderedSet.description](https://developer.apple.com/documentation/foundation/nsorderedset/1415872-description)Added [NSOrderedSet.firstObject](https://developer.apple.com/documentation/foundation/nsorderedset/1409765-firstobject)Added [-[NSOrderedSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417543-init)Added [NSOrderedSet.lastObject](https://developer.apple.com/documentation/foundation/nsorderedset/1409143-lastobject)Added [NSOrderedSet.reversedOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset/1411022-reversedorderedset)Added [NSOrderedSet.set](https://developer.apple.com/documentation/foundation/nsorderedset/1413944-set)Modified [-[NSMutableOrderedSet init]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410545-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableOrderedSet initWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411583-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOrderedSet init]](https://developer.apple.com/documentation/foundation/nsorderedset/1417735-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOrderedSet initWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411910-initwithobjects)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSOrthography.hAdded [-[NSOrthography initWithCoder:]](https://developer.apple.com/documentation/foundation/nsorthography/1408410-init)Modified [NSOrthography.allLanguages](https://developer.apple.com/documentation/foundation/nsorthography/1416205-alllanguages)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *allLanguages ``` |
| To | ``` @property(readonly, copy) NSArray *allLanguages ``` |

Modified [NSOrthography.allScripts](https://developer.apple.com/documentation/foundation/nsorthography/1410722-allscripts)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *allScripts ``` |
| To | ``` @property(readonly, copy) NSArray *allScripts ``` |

Modified [NSOrthography.dominantLanguage](https://developer.apple.com/documentation/foundation/nsorthography/1415229-dominantlanguage)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *dominantLanguage ``` |
| To | ``` @property(readonly, copy) NSString *dominantLanguage ``` |

Modified [NSOrthography.dominantScript](https://developer.apple.com/documentation/foundation/nsorthography/1407965-dominantscript)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *dominantScript ``` |
| To | ``` @property(readonly, copy) NSString *dominantScript ``` |

Modified [-[NSOrthography initWithDominantScript:languageMap:]](https://developer.apple.com/documentation/foundation/nsorthography/1408708-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithDominantScript:(NSString *)script languageMap:(NSDictionary *)map ``` | -- |
| To | ``` - (instancetype)initWithDominantScript:(NSString *)script languageMap:(NSDictionary *)map ``` | yes |

Modified [NSOrthography.languageMap](https://developer.apple.com/documentation/foundation/nsorthography/1409533-languagemap)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *languageMap ``` |
| To | ``` @property(readonly, copy) NSDictionary *languageMap ``` |

Modified [+[NSOrthography orthographyWithDominantScript:languageMap:]](https://developer.apple.com/documentation/foundation/nsorthography/1585529-orthographywithdominantscript)

|  | Declaration |
| --- | --- |
| From | ``` + (id)orthographyWithDominantScript:(NSString *)script languageMap:(NSDictionary *)map ``` |
| To | ``` + (instancetype)orthographyWithDominantScript:(NSString *)script languageMap:(NSDictionary *)map ``` |

NSPathUtilities.hRemoved [-[NSString fileSystemRepresentation]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/fileSystemRepresentation)Removed [-[NSString isAbsolutePath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/isAbsolutePath)Removed [-[NSString lastPathComponent]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/lastPathComponent)Removed [-[NSString pathComponents]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/pathComponents)Removed [-[NSString pathExtension]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/pathExtension)Removed [-[NSString stringByAbbreviatingWithTildeInPath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByAbbreviatingWithTildeInPath)Removed [-[NSString stringByDeletingLastPathComponent]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByDeletingLastPathComponent)Removed [-[NSString stringByDeletingPathExtension]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByDeletingPathExtension)Removed [-[NSString stringByExpandingTildeInPath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByExpandingTildeInPath)Removed [-[NSString stringByResolvingSymlinksInPath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByResolvingSymlinksInPath)Removed [-[NSString stringByStandardizingPath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByStandardizingPath)Added [NSString.absolutePath](https://developer.apple.com/documentation/foundation/nsstring/1409068-isabsolutepath)Added [NSString.fileSystemRepresentation](https://developer.apple.com/documentation/foundation/nsstring/1414559-filesystemrepresentation)Added [NSString.lastPathComponent](https://developer.apple.com/documentation/foundation/nsstring/1416528-lastpathcomponent)Added [NSString.pathComponents](https://developer.apple.com/documentation/foundation/nsstring/1414489-pathcomponents)Added [NSString.pathExtension](https://developer.apple.com/documentation/foundation/nsstring/1407801-pathextension)Added [NSString.stringByAbbreviatingWithTildeInPath](https://developer.apple.com/documentation/foundation/nsstring/1407943-stringbyabbreviatingwithtildeinp)Added [NSString.stringByDeletingLastPathComponent](https://developer.apple.com/documentation/foundation/nsstring/1411141-stringbydeletinglastpathcomponen)Added [NSString.stringByDeletingPathExtension](https://developer.apple.com/documentation/foundation/nsstring/1418214-stringbydeletingpathextension)Added [NSString.stringByExpandingTildeInPath](https://developer.apple.com/documentation/foundation/nsstring/1407716-stringbyexpandingtildeinpath)Added [NSString.stringByResolvingSymlinksInPath](https://developer.apple.com/documentation/foundation/nsstring/1417783-resolvingsymlinksinpath)Added [NSString.stringByStandardizingPath](https://developer.apple.com/documentation/foundation/nsstring/1407194-standardizingpath)NSPointerArray.hRemoved [-[NSPointerArray allObjects]](https://developer.apple.com/documentation/foundation/nspointerarray/1408081-allobjects)Removed [-[NSPointerArray count]](https://developer.apple.com/documentation/foundation/nspointerarray/1418453-count)Removed [-[NSPointerArray pointerFunctions]](https://developer.apple.com/documentation/foundation/nspointerarray/1413669-pointerfunctions)Removed [-[NSPointerArray setCount:]](https://developer.apple.com/documentation/foundation/nspointerarray/1418453-count)Added [NSPointerArray.allObjects](https://developer.apple.com/documentation/foundation/nspointerarray/1408081-allobjects)Added [NSPointerArray.count](https://developer.apple.com/documentation/foundation/nspointerarray/1418453-count)Added [NSPointerArray.pointerFunctions](https://developer.apple.com/documentation/foundation/nspointerarray/1413669-pointerfunctions)Modified [-[NSPointerArray initWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1408229-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithOptions:(NSPointerFunctionsOptions)options ``` | -- |
| To | ``` - (instancetype)initWithOptions:(NSPointerFunctionsOptions)options ``` | yes |

Modified [-[NSPointerArray initWithPointerFunctions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1416727-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithPointerFunctions:(NSPointerFunctions *)functions ``` | -- |
| To | ``` - (instancetype)initWithPointerFunctions:(NSPointerFunctions *)functions ``` | yes |

Modified [+[NSPointerArray pointerArrayWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1564845-pointerarraywithoptions)

|  | Declaration |
| --- | --- |
| From | ``` + (id)pointerArrayWithOptions:(NSPointerFunctionsOptions)options ``` |
| To | ``` + (NSPointerArray *)pointerArrayWithOptions:(NSPointerFunctionsOptions)options ``` |

Modified [+[NSPointerArray pointerArrayWithPointerFunctions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1564844-pointerarraywithpointerfunctions)

|  | Declaration |
| --- | --- |
| From | ``` + (id)pointerArrayWithPointerFunctions:(NSPointerFunctions *)functions ``` |
| To | ``` + (NSPointerArray *)pointerArrayWithPointerFunctions:(NSPointerFunctions *)functions ``` |

Modified [+[NSPointerArray strongObjectsPointerArray]](https://developer.apple.com/documentation/foundation/nspointerarray/1413102-strongobjects)

|  | Declaration |
| --- | --- |
| From | ``` + (id)strongObjectsPointerArray ``` |
| To | ``` + (NSPointerArray *)strongObjectsPointerArray ``` |

Modified [+[NSPointerArray weakObjectsPointerArray]](https://developer.apple.com/documentation/foundation/nspointerarray/1412795-weakobjectspointerarray)

|  | Declaration |
| --- | --- |
| From | ``` + (id)weakObjectsPointerArray ``` |
| To | ``` + (NSPointerArray *)weakObjectsPointerArray ``` |

NSPointerFunctions.hModified [-[NSPointerFunctions initWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerfunctions/1417715-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithOptions:(NSPointerFunctionsOptions)options ``` | -- |
| To | ``` - (instancetype)initWithOptions:(NSPointerFunctionsOptions)options ``` | yes |

Modified [+[NSPointerFunctions pointerFunctionsWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerfunctions/1451770-pointerfunctionswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` + (id)pointerFunctionsWithOptions:(NSPointerFunctionsOptions)options ``` |
| To | ``` + (NSPointerFunctions *)pointerFunctionsWithOptions:(NSPointerFunctionsOptions)options ``` |

NSPort.hRemoved [-[NSMachPort machPort]](https://developer.apple.com/documentation/foundation/nsmachport/1399539-machport)Removed [-[NSPort isValid]](https://developer.apple.com/documentation/foundation/nsport/1399503-valid)Removed [-[NSPort reservedSpaceLength]](https://developer.apple.com/documentation/foundation/port/1399529-reservedspacelength)Removed [-[NSSocketPort address]](https://developer.apple.com/documentation/foundation/nssocketport/1399480-address)Removed [-[NSSocketPort protocol]](https://developer.apple.com/documentation/foundation/nssocketport/1399557-protocol)Removed [-[NSSocketPort protocolFamily]](https://developer.apple.com/documentation/foundation/nssocketport/1399543-protocolfamily)Removed [-[NSSocketPort socket]](https://developer.apple.com/documentation/foundation/nssocketport/1399492-socket)Removed [-[NSSocketPort socketType]](https://developer.apple.com/documentation/foundation/nssocketport/1399565-sockettype)Added [NSMachPort.machPort](https://developer.apple.com/documentation/foundation/nsmachport/1399539-machport)Added [NSPort.reservedSpaceLength](https://developer.apple.com/documentation/foundation/nsport/1399529-reservedspacelength)Added [NSPort.valid](https://developer.apple.com/documentation/foundation/nsport/1399503-valid)Added [NSSocketPort.address](https://developer.apple.com/documentation/foundation/nssocketport/1399480-address)Added [NSSocketPort.protocol](https://developer.apple.com/documentation/foundation/socketport/1399557-protocol)Added [NSSocketPort.protocolFamily](https://developer.apple.com/documentation/foundation/socketport/1399543-protocolfamily)Added [NSSocketPort.socket](https://developer.apple.com/documentation/foundation/socketport/1399492-socket)Added [NSSocketPort.socketType](https://developer.apple.com/documentation/foundation/nssocketport/1399565-sockettype)Modified [-[NSMachPort initWithMachPort:]](https://developer.apple.com/documentation/foundation/nsmachport/1399499-initwithmachport)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMachPort:(uint32_t)machPort ``` |
| To | ``` - (instancetype)initWithMachPort:(uint32_t)machPort ``` |

Modified [-[NSMachPort initWithMachPort:options:]](https://developer.apple.com/documentation/foundation/nsmachport/1399559-initwithmachport)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithMachPort:(uint32_t)machPort options:(NSUInteger)f ``` | -- |
| To | ``` - (instancetype)initWithMachPort:(uint32_t)machPort options:(NSUInteger)f ``` | yes |

Modified [-[NSMachPortDelegate handleMachMessage:]](https://developer.apple.com/documentation/foundation/nsmachportdelegate/1399509-handlemachmessage)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPortDelegate handlePortMessage:]](https://developer.apple.com/documentation/foundation/nsportdelegate/1399513-handleportmessage)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSocketPort init]](https://developer.apple.com/documentation/foundation/socketport/1399549-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSSocketPort initRemoteWithProtocolFamily:socketType:protocol:address:]](https://developer.apple.com/documentation/foundation/nssocketport/1399535-initremotewithprotocolfamily)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initRemoteWithProtocolFamily:(int)family socketType:(int)type protocol:(int)protocol address:(NSData *)address ``` | -- |
| To | ``` - (instancetype)initRemoteWithProtocolFamily:(int)family socketType:(int)type protocol:(int)protocol address:(NSData *)address ``` | yes |

Modified [-[NSSocketPort initRemoteWithTCPPort:host:]](https://developer.apple.com/documentation/foundation/nssocketport/1399474-initremotewithtcpport)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initRemoteWithTCPPort:(unsigned short)port host:(NSString *)hostName ``` |
| To | ``` - (instancetype)initRemoteWithTCPPort:(unsigned short)port host:(NSString *)hostName ``` |

Modified [-[NSSocketPort initWithProtocolFamily:socketType:protocol:address:]](https://developer.apple.com/documentation/foundation/nssocketport/1399497-initwithprotocolfamily)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithProtocolFamily:(int)family socketType:(int)type protocol:(int)protocol address:(NSData *)address ``` | -- |
| To | ``` - (instancetype)initWithProtocolFamily:(int)family socketType:(int)type protocol:(int)protocol address:(NSData *)address ``` | yes |

Modified [-[NSSocketPort initWithProtocolFamily:socketType:protocol:socket:]](https://developer.apple.com/documentation/foundation/nssocketport/1399484-initwithprotocolfamily)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithProtocolFamily:(int)family socketType:(int)type protocol:(int)protocol socket:(NSSocketNativeHandle)sock ``` | -- |
| To | ``` - (instancetype)initWithProtocolFamily:(int)family socketType:(int)type protocol:(int)protocol socket:(NSSocketNativeHandle)sock ``` | yes |

Modified [-[NSSocketPort initWithTCPPort:]](https://developer.apple.com/documentation/foundation/socketport/1399488-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTCPPort:(unsigned short)port ``` |
| To | ``` - (instancetype)initWithTCPPort:(unsigned short)port ``` |

NSPortCoder.hRemoved [-[NSObject classForPortCoder]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/classForPortCoder)Added [NSObject.classForPortCoder](https://developer.apple.com/documentation/objectivec/nsobject/1580076-classforportcoder)NSPortMessage.hRemoved [-[NSPortMessage components]](https://developer.apple.com/documentation/foundation/nsportmessage/1407377-components)Removed [-[NSPortMessage msgid]](https://developer.apple.com/documentation/foundation/portmessage/1407880-msgid)Removed [-[NSPortMessage receivePort]](https://developer.apple.com/documentation/foundation/portmessage/1413908-receiveport)Removed [-[NSPortMessage sendPort]](https://developer.apple.com/documentation/foundation/portmessage/1417234-sendport)Removed [-[NSPortMessage setMsgid:]](https://developer.apple.com/documentation/foundation/portmessage/1407880-msgid)Added [NSPortMessage.components](https://developer.apple.com/documentation/foundation/nsportmessage/1407377-components)Added [NSPortMessage.msgid](https://developer.apple.com/documentation/foundation/portmessage/1407880-msgid)Added [NSPortMessage.receivePort](https://developer.apple.com/documentation/foundation/portmessage/1413908-receiveport)Added [NSPortMessage.sendPort](https://developer.apple.com/documentation/foundation/nsportmessage/1417234-sendport)Modified [-[NSPortMessage initWithSendPort:receivePort:components:]](https://developer.apple.com/documentation/foundation/portmessage/1417387-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithSendPort:(NSPort *)sendPort receivePort:(NSPort *)replyPort components:(NSArray *)components ``` | -- |
| To | ``` - (instancetype)initWithSendPort:(NSPort *)sendPort receivePort:(NSPort *)replyPort components:(NSArray *)components ``` | yes |

NSPortNameServer.hRemoved [-[NSSocketPortNameServer defaultNameServerPortNumber]](https://developer.apple.com/documentation/foundation/nssocketportnameserver/1806767-defaultnameserverportnumber)Removed [-[NSSocketPortNameServer setDefaultNameServerPortNumber:]](https://developer.apple.com/documentation/foundation/nssocketportnameserver/1806775-setdefaultnameserverportnumber)Added [NSSocketPortNameServer.defaultNameServerPortNumber](https://developer.apple.com/documentation/foundation/nssocketportnameserver/1401755-defaultnameserverportnumber)NSPredicate.hRemoved [-[NSPredicate predicateFormat]](https://developer.apple.com/documentation/foundation/nspredicate/1411605-predicateformat)Added [NSPredicate.predicateFormat](https://developer.apple.com/documentation/foundation/nspredicate/1411605-predicateformat)Modified [-[NSPredicate predicateWithSubstitutionVariables:]](https://developer.apple.com/documentation/foundation/nspredicate/1413227-withsubstitutionvariables)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPredicate *)predicateWithSubstitutionVariables:(NSDictionary *)variables ``` |
| To | ``` - (instancetype)predicateWithSubstitutionVariables:(NSDictionary *)variables ``` |

NSProcessInfo.hRemoved [-[NSProcessInfo activeProcessorCount]](https://developer.apple.com/documentation/foundation/processinfo/1408184-activeprocessorcount)Removed [-[NSProcessInfo arguments]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/arguments)Removed [-[NSProcessInfo automaticTerminationSupportEnabled]](https://developer.apple.com/documentation/foundation/nsprocessinfo/1407578-automaticterminationsupportenabl)Removed [-[NSProcessInfo environment]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/environment)Removed [-[NSProcessInfo globallyUniqueString]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/globallyUniqueString)Removed [-[NSProcessInfo hostName]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/hostName)Removed [-[NSProcessInfo operatingSystemVersionString]](https://developer.apple.com/documentation/foundation/processinfo/1408730-operatingsystemversionstring)Removed [-[NSProcessInfo physicalMemory]](https://developer.apple.com/documentation/foundation/processinfo/1408211-physicalmemory)Removed [-[NSProcessInfo processIdentifier]](https://developer.apple.com/documentation/foundation/processinfo/1415929-processidentifier)Removed [-[NSProcessInfo processName]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/processName)Removed [-[NSProcessInfo processorCount]](https://developer.apple.com/documentation/foundation/processinfo/1415622-processorcount)Removed [-[NSProcessInfo setAutomaticTerminationSupportEnabled:]](https://developer.apple.com/documentation/foundation/processinfo/1407578-automaticterminationsupportenabl)Removed [-[NSProcessInfo setProcessName:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/setProcessName:)Removed [-[NSProcessInfo systemUptime]](https://developer.apple.com/documentation/foundation/processinfo/1414553-systemuptime)Added [NSProcessInfo.activeProcessorCount](https://developer.apple.com/documentation/foundation/nsprocessinfo/1408184-activeprocessorcount)Added [NSProcessInfo.arguments](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415596-arguments)Added [NSProcessInfo.automaticTerminationSupportEnabled](https://developer.apple.com/documentation/foundation/nsprocessinfo/1407578-automaticterminationsupportenabl)Added [NSProcessInfo.environment](https://developer.apple.com/documentation/foundation/processinfo/1417911-environment)Added [NSProcessInfo.globallyUniqueString](https://developer.apple.com/documentation/foundation/nsprocessinfo/1416432-globallyuniquestring)Added [NSProcessInfo.hostName](https://developer.apple.com/documentation/foundation/processinfo/1417236-hostname)Added [-[NSProcessInfo isOperatingSystemAtLeastVersion:]](https://developer.apple.com/documentation/foundation/nsprocessinfo/1414876-isoperatingsystematleastversion)Added [NSProcessInfo.operatingSystemVersion](https://developer.apple.com/documentation/foundation/nsprocessinfo/1410906-operatingsystemversion)Added [NSProcessInfo.operatingSystemVersionString](https://developer.apple.com/documentation/foundation/nsprocessinfo/1408730-operatingsystemversionstring)Added [NSProcessInfo.physicalMemory](https://developer.apple.com/documentation/foundation/nsprocessinfo/1408211-physicalmemory)Added [NSProcessInfo.processIdentifier](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415929-processidentifier)Added [NSProcessInfo.processName](https://developer.apple.com/documentation/foundation/processinfo/1416428-processname)Added [NSProcessInfo.processorCount](https://developer.apple.com/documentation/foundation/processinfo/1415622-processorcount)Added [NSProcessInfo.systemUptime](https://developer.apple.com/documentation/foundation/nsprocessinfo/1414553-systemuptime)Added [NSOperatingSystemVersion](https://developer.apple.com/documentation/foundation/operatingsystemversion)Modified [-[NSProcessInfo operatingSystem]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/operatingSystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSProcessInfo operatingSystemName]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/instm/NSProcessInfo/operatingSystemName)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSHPUXOperatingSystem](https://developer.apple.com/documentation/foundation/1552984-anonymous/nshpuxoperatingsystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSMACHOperatingSystem](https://developer.apple.com/documentation/foundation/nsmachoperatingsystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSOSF1OperatingSystem](https://developer.apple.com/documentation/foundation/nsosf1operatingsystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSSolarisOperatingSystem](https://developer.apple.com/documentation/foundation/nssolarisoperatingsystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSSunOSOperatingSystem](https://developer.apple.com/documentation/foundation/nssunosoperatingsystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWindows95OperatingSystem](https://developer.apple.com/documentation/foundation/nswindows95operatingsystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [NSWindowsNTOperatingSystem](https://developer.apple.com/documentation/foundation/nswindowsntoperatingsystem)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSProgress.hRemoved [-[NSProgress userInfo]](https://developer.apple.com/documentation/foundation/progress/1413314-userinfo)Added [NSProgress.userInfo](https://developer.apple.com/documentation/foundation/nsprogress/1413314-userinfo)Modified [-[NSProgress initWithParent:userInfo:]](https://developer.apple.com/documentation/foundation/progress/1409133-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSPropertyList.hModified [+[NSPropertyListSerialization dataFromPropertyList:format:errorDescription:]](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1416061-datafrompropertylist)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.0 | OS X 10.10 |

Modified [+[NSPropertyListSerialization propertyListFromData:mutabilityOption:format:errorDescription:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1411993-propertylistfromdata)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.0 | OS X 10.10 |

NSProtocolChecker.hRemoved [-[NSProtocolChecker protocol]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProtocolChecker/Description.html#//apple_ref/occ/instm/NSProtocolChecker/protocol)Removed [-[NSProtocolChecker target]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProtocolChecker/Description.html#//apple_ref/occ/instm/NSProtocolChecker/target)Added [NSProtocolChecker.protocol](https://developer.apple.com/documentation/foundation/nsprotocolchecker/1413544-protocol)Added [NSProtocolChecker.target](https://developer.apple.com/documentation/foundation/nsprotocolchecker/1416619-target)Modified [-[NSProtocolChecker initWithTarget:protocol:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProtocolChecker/Description.html#//apple_ref/occ/instm/NSProtocolChecker/initWithTarget:protocol:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTarget:(NSObject *)anObject protocol:(Protocol *)aProtocol ``` |
| To | ``` - (instancetype)initWithTarget:(NSObject *)anObject protocol:(Protocol *)aProtocol ``` |

Modified [+[NSProtocolChecker protocolCheckerWithTarget:protocol:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProtocolChecker/Description.html#//apple_ref/occ/clm/NSProtocolChecker/protocolCheckerWithTarget:protocol:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)protocolCheckerWithTarget:(NSObject *)anObject protocol:(Protocol *)aProtocol ``` |
| To | ``` + (instancetype)protocolCheckerWithTarget:(NSObject *)anObject protocol:(Protocol *)aProtocol ``` |

NSProxy.hRemoved [-[NSProxy debugDescription]](https://developer.apple.com/documentation/foundation/nsproxy/1416366-debugdescription)Removed [-[NSProxy description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProxy/Description.html#//apple_ref/occ/instm/NSProxy/description)Added [NSProxy.debugDescription](https://developer.apple.com/documentation/foundation/nsproxy/1416366-debugdescription)Added [NSProxy.description](https://developer.apple.com/documentation/foundation/nsproxy/1416346-description)NSRange.hRemoved [-[NSValue rangeValue]](https://developer.apple.com/documentation/foundation/nsvalue/1413902-rangevalue)Added [NSValue.rangeValue](https://developer.apple.com/documentation/foundation/nsvalue/1413902-rangevalue)NSRegularExpression.hModified [-[NSDataDetector initWithTypes:error:]](https://developer.apple.com/documentation/foundation/nsdatadetector/1409829-initwithtypes)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithTypes:(NSTextCheckingTypes)checkingTypes error:(NSError **)error ``` | -- |
| To | ``` - (instancetype)initWithTypes:(NSTextCheckingTypes)checkingTypes error:(NSError **)error ``` | yes |

Modified [-[NSRegularExpression initWithPattern:options:error:]](https://developer.apple.com/documentation/foundation/nsregularexpression/1410900-initwithpattern)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithPattern:(NSString *)pattern options:(NSRegularExpressionOptions)options error:(NSError **)error ``` | -- |
| To | ``` - (instancetype)initWithPattern:(NSString *)pattern options:(NSRegularExpressionOptions)options error:(NSError **)error ``` | yes |

Modified [NSRegularExpression.pattern](https://developer.apple.com/documentation/foundation/nsregularexpression/1414932-pattern)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *pattern ``` |
| To | ``` @property(readonly, copy) NSString *pattern ``` |

NSRunLoop.hRemoved [-[NSRunLoop currentMode]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/currentMode)Added [NSRunLoop.currentMode](https://developer.apple.com/documentation/foundation/nsrunloop/1412652-currentmode)NSScanner.hRemoved [-[NSScanner caseSensitive]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/caseSensitive)Removed [-[NSScanner charactersToBeSkipped]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/charactersToBeSkipped)Removed [-[NSScanner isAtEnd]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/isAtEnd)Removed [-[NSScanner locale]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/locale)Removed [-[NSScanner scanLocation]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanLocation)Removed [-[NSScanner setCaseSensitive:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setCaseSensitive:)Removed [-[NSScanner setCharactersToBeSkipped:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setCharactersToBeSkipped:)Removed [-[NSScanner setLocale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setLocale:)Removed [-[NSScanner setScanLocation:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setScanLocation:)Removed [-[NSScanner string]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/string)Added [NSScanner.atEnd](https://developer.apple.com/documentation/foundation/scanner/1412801-isatend)Added [NSScanner.caseSensitive](https://developer.apple.com/documentation/foundation/scanner/1409488-casesensitive)Added [NSScanner.charactersToBeSkipped](https://developer.apple.com/documentation/foundation/scanner/1410204-characterstobeskipped)Added [NSScanner.locale](https://developer.apple.com/documentation/foundation/nsscanner/1409531-locale)Added [NSScanner.scanLocation](https://developer.apple.com/documentation/foundation/scanner/1413294-scanlocation)Added [NSScanner.string](https://developer.apple.com/documentation/foundation/nsscanner/1418109-string)Modified [-[NSScanner initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/initWithString:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithString:(NSString *)string ``` | -- |
| To | ``` - (instancetype)initWithString:(NSString *)string ``` | yes |

Modified [+[NSScanner scannerWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/clm/NSScanner/scannerWithString:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)scannerWithString:(NSString *)string ``` |
| To | ``` + (instancetype)scannerWithString:(NSString *)string ``` |

NSScriptClassDescription.hRemoved [-[NSObject classCode]](https://developer.apple.com/documentation/objectivec/nsobject/1413991-classcode)Removed [-[NSObject className]](https://developer.apple.com/documentation/objectivec/nsobject/1411337-classname)Removed [-[NSScriptClassDescription appleEventCode]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1414920-appleeventcode)Removed [-[NSScriptClassDescription className]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1418029-classname)Removed [-[NSScriptClassDescription defaultSubcontainerAttributeKey]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1410261-defaultsubcontainerattributekey)Removed [-[NSScriptClassDescription implementationClassName]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1409575-implementationclassname)Removed [-[NSScriptClassDescription suiteName]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1410782-suitename)Removed [-[NSScriptClassDescription superclassDescription]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1416243-superclassdescription)Added [NSObject.classCode](https://developer.apple.com/documentation/objectivec/nsobject/1413991-classcode)Added [NSObject.className](https://developer.apple.com/documentation/objectivec/nsobject/1411337-classname)Added [NSScriptClassDescription.appleEventCode](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1414920-appleeventcode)Added [NSScriptClassDescription.className](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1418029-classname)Added [NSScriptClassDescription.defaultSubcontainerAttributeKey](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1410261-defaultsubcontainerattributekey)Added [NSScriptClassDescription.implementationClassName](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1409575-implementationclassname)Added [NSScriptClassDescription.suiteName](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1410782-suitename)Added [NSScriptClassDescription.superclassDescription](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1416243-superclass)Modified [-[NSScriptClassDescription initWithSuiteName:className:dictionary:]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1410370-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithSuiteName:(NSString *)suiteName className:(NSString *)className dictionary:(NSDictionary *)classDeclaration ``` | -- |
| To | ``` - (instancetype)initWithSuiteName:(NSString *)suiteName className:(NSString *)className dictionary:(NSDictionary *)classDeclaration ``` | yes |

NSScriptCommand.hRemoved [-[NSScriptCommand appleEvent]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1415626-appleevent)Removed [-[NSScriptCommand arguments]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1414071-arguments)Removed [-[NSScriptCommand commandDescription]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1407452-commanddescription)Removed [-[NSScriptCommand directParameter]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1410675-directparameter)Removed [-[NSScriptCommand evaluatedArguments]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1413335-evaluatedarguments)Removed [-[NSScriptCommand evaluatedReceivers]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411257-evaluatedreceivers)Removed [-[NSScriptCommand isWellFormed]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1806810-iswellformed)Removed [-[NSScriptCommand receiversSpecifier]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1417016-receiversspecifier)Removed [-[NSScriptCommand scriptErrorExpectedTypeDescriptor]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411714-scripterrorexpectedtypedescripto)Removed [-[NSScriptCommand scriptErrorNumber]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411484-scripterrornumber)Removed [-[NSScriptCommand scriptErrorOffendingObjectDescriptor]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1417217-scripterroroffendingobjectdescri)Removed [-[NSScriptCommand scriptErrorString]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1414596-scripterrorstring)Removed [-[NSScriptCommand setArguments:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1414071-arguments)Removed [-[NSScriptCommand setDirectParameter:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1410675-directparameter)Removed [-[NSScriptCommand setReceiversSpecifier:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1417016-receiversspecifier)Removed [-[NSScriptCommand setScriptErrorExpectedTypeDescriptor:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411714-scripterrorexpectedtypedescripto)Removed [-[NSScriptCommand setScriptErrorNumber:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411484-scripterrornumber)Removed [-[NSScriptCommand setScriptErrorOffendingObjectDescriptor:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1417217-scripterroroffendingobjectdescri)Removed [-[NSScriptCommand setScriptErrorString:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1414596-scripterrorstring)Added [NSScriptCommand.appleEvent](https://developer.apple.com/documentation/foundation/nsscriptcommand/1415626-appleevent)Added [NSScriptCommand.arguments](https://developer.apple.com/documentation/foundation/nsscriptcommand/1414071-arguments)Added [NSScriptCommand.commandDescription](https://developer.apple.com/documentation/foundation/nsscriptcommand/1407452-commanddescription)Added [NSScriptCommand.directParameter](https://developer.apple.com/documentation/foundation/nsscriptcommand/1410675-directparameter)Added [NSScriptCommand.evaluatedArguments](https://developer.apple.com/documentation/foundation/nsscriptcommand/1413335-evaluatedarguments)Added [NSScriptCommand.evaluatedReceivers](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411257-evaluatedreceivers)Added [-[NSScriptCommand initWithCoder:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1417482-init)Added [NSScriptCommand.receiversSpecifier](https://developer.apple.com/documentation/foundation/nsscriptcommand/1417016-receiversspecifier)Added [NSScriptCommand.scriptErrorExpectedTypeDescriptor](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411714-scripterrorexpectedtypedescripto)Added [NSScriptCommand.scriptErrorNumber](https://developer.apple.com/documentation/foundation/nsscriptcommand/1411484-scripterrornumber)Added [NSScriptCommand.scriptErrorOffendingObjectDescriptor](https://developer.apple.com/documentation/foundation/nsscriptcommand/1417217-scripterroroffendingobjectdescri)Added [NSScriptCommand.scriptErrorString](https://developer.apple.com/documentation/foundation/nsscriptcommand/1414596-scripterrorstring)Added [NSScriptCommand.wellFormed](https://developer.apple.com/documentation/foundation/nsscriptcommand/1413090-wellformed)Modified [-[NSScriptCommand initWithCommandDescription:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1413516-initwithcommanddescription)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithCommandDescription:(NSScriptCommandDescription *)commandDef ``` | -- |
| To | ``` - (instancetype)initWithCommandDescription:(NSScriptCommandDescription *)commandDef ``` | yes |

NSScriptCommandDescription.hRemoved [-[NSScriptCommandDescription appleEventClassCode]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1416191-appleeventclasscode)Removed [-[NSScriptCommandDescription appleEventCode]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1408972-appleeventcode)Removed [-[NSScriptCommandDescription appleEventCodeForReturnType]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1408166-appleeventcodeforreturntype)Removed [-[NSScriptCommandDescription argumentNames]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1409125-argumentnames)Removed [-[NSScriptCommandDescription commandClassName]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1417478-commandclassname)Removed [-[NSScriptCommandDescription commandName]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1407512-commandname)Removed [-[NSScriptCommandDescription returnType]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1410754-returntype)Removed [-[NSScriptCommandDescription suiteName]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1413657-suitename)Added [NSScriptCommandDescription.appleEventClassCode](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1416191-appleeventclasscode)Added [NSScriptCommandDescription.appleEventCode](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1408972-appleeventcode)Added [NSScriptCommandDescription.appleEventCodeForReturnType](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1408166-appleeventcodeforreturntype)Added [NSScriptCommandDescription.argumentNames](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1409125-argumentnames)Added [NSScriptCommandDescription.commandClassName](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1417478-commandclassname)Added [NSScriptCommandDescription.commandName](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1407512-commandname)Added [-[NSScriptCommandDescription initWithCoder:]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1416525-init)Added [NSScriptCommandDescription.returnType](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1410754-returntype)Added [NSScriptCommandDescription.suiteName](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1413657-suitename)Modified [-[NSScriptCommandDescription initWithSuiteName:commandName:dictionary:]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1410038-initwithsuitename)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithSuiteName:(NSString *)suiteName commandName:(NSString *)commandName dictionary:(NSDictionary *)commandDeclaration ``` | -- |
| To | ``` - (instancetype)initWithSuiteName:(NSString *)suiteName commandName:(NSString *)commandName dictionary:(NSDictionary *)commandDeclaration ``` | yes |

NSScriptExecutionContext.hRemoved [-[NSScriptExecutionContext objectBeingTested]](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1412411-objectbeingtested)Removed [-[NSScriptExecutionContext rangeContainerObject]](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1416391-rangecontainerobject)Removed [-[NSScriptExecutionContext setObjectBeingTested:]](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1412411-objectbeingtested)Removed [-[NSScriptExecutionContext setRangeContainerObject:]](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1416391-rangecontainerobject)Removed [-[NSScriptExecutionContext setTopLevelObject:]](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1415288-toplevelobject)Removed [-[NSScriptExecutionContext topLevelObject]](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1415288-toplevelobject)Added [NSScriptExecutionContext.objectBeingTested](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1412411-objectbeingtested)Added [NSScriptExecutionContext.rangeContainerObject](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1416391-rangecontainerobject)Added [NSScriptExecutionContext.topLevelObject](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/1415288-toplevelobject)NSScriptObjectSpecifiers.hRemoved [-[NSIndexSpecifier index]](https://developer.apple.com/documentation/foundation/nsindexspecifier/1408567-index)Removed [-[NSIndexSpecifier setIndex:]](https://developer.apple.com/documentation/foundation/nsindexspecifier/1408567-index)Removed [-[NSNameSpecifier name]](https://developer.apple.com/documentation/foundation/nsnamespecifier/1407411-name)Removed [-[NSNameSpecifier setName:]](https://developer.apple.com/documentation/foundation/nsnamespecifier/1407411-name)Removed [-[NSObject objectSpecifier]](https://developer.apple.com/documentation/objectivec/nsobject/1409884-objectspecifier)Removed [-[NSPositionalSpecifier insertionContainer]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1414957-insertioncontainer)Removed [-[NSPositionalSpecifier insertionIndex]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1414703-insertionindex)Removed [-[NSPositionalSpecifier insertionKey]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1414059-insertionkey)Removed [-[NSPositionalSpecifier insertionReplaces]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1411646-insertionreplaces)Removed [-[NSPositionalSpecifier objectSpecifier]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1412839-objectspecifier)Removed [-[NSPositionalSpecifier position]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1413865-position)Removed [-[NSRangeSpecifier endSpecifier]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418470-endspecifier)Removed [-[NSRangeSpecifier setEndSpecifier:]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418470-endspecifier)Removed [-[NSRangeSpecifier setStartSpecifier:]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418394-startspecifier)Removed [-[NSRangeSpecifier startSpecifier]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418394-startspecifier)Removed [-[NSRelativeSpecifier baseSpecifier]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1409071-basespecifier)Removed [-[NSRelativeSpecifier relativePosition]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1416001-relativeposition)Removed [-[NSRelativeSpecifier setBaseSpecifier:]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1409071-basespecifier)Removed [-[NSRelativeSpecifier setRelativePosition:]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1416001-relativeposition)Removed [-[NSScriptObjectSpecifier childSpecifier]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1409882-child)Removed [-[NSScriptObjectSpecifier containerClassDescription]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1413179-containerclassdescription)Removed [-[NSScriptObjectSpecifier containerIsObjectBeingTested]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1410887-containerisobjectbeingtested)Removed [-[NSScriptObjectSpecifier containerIsRangeContainerObject]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416507-containerisrangecontainerobject)Removed [-[NSScriptObjectSpecifier containerSpecifier]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1414424-containerspecifier)Removed [-[NSScriptObjectSpecifier descriptor]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1410018-descriptor)Removed [-[NSScriptObjectSpecifier evaluationErrorNumber]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416938-evaluationerrornumber)Removed [-[NSScriptObjectSpecifier evaluationErrorSpecifier]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416385-evaluationerror)Removed [-[NSScriptObjectSpecifier key]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1412986-key)Removed [-[NSScriptObjectSpecifier keyClassDescription]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1417974-keyclassdescription)Removed [-[NSScriptObjectSpecifier objectsByEvaluatingSpecifier]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1413391-objectsbyevaluatingspecifier)Removed [-[NSScriptObjectSpecifier setChildSpecifier:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1409882-childspecifier)Removed [-[NSScriptObjectSpecifier setContainerClassDescription:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1413179-containerclassdescription)Removed [-[NSScriptObjectSpecifier setContainerIsObjectBeingTested:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1410887-containerisobjectbeingtested)Removed [-[NSScriptObjectSpecifier setContainerIsRangeContainerObject:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416507-containerisrangecontainerobject)Removed [-[NSScriptObjectSpecifier setContainerSpecifier:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1414424-containerspecifier)Removed [-[NSScriptObjectSpecifier setEvaluationErrorNumber:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416938-evaluationerrornumber)Removed [-[NSScriptObjectSpecifier setKey:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1412986-key)Removed [-[NSUniqueIDSpecifier setUniqueID:]](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/1415634-uniqueid)Removed [-[NSUniqueIDSpecifier uniqueID]](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/1415634-uniqueid)Removed [-[NSWhoseSpecifier endSubelementIdentifier]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1407761-endsubelementidentifier)Removed [-[NSWhoseSpecifier endSubelementIndex]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1416686-endsubelementindex)Removed [-[NSWhoseSpecifier setEndSubelementIdentifier:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1407761-endsubelementidentifier)Removed [-[NSWhoseSpecifier setEndSubelementIndex:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1416686-endsubelementindex)Removed [-[NSWhoseSpecifier setStartSubelementIdentifier:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1413408-startsubelementidentifier)Removed [-[NSWhoseSpecifier setStartSubelementIndex:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1417856-startsubelementindex)Removed [-[NSWhoseSpecifier setTest:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1412482-test)Removed [-[NSWhoseSpecifier startSubelementIdentifier]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1413408-startsubelementidentifier)Removed [-[NSWhoseSpecifier startSubelementIndex]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1417856-startsubelementindex)Removed [-[NSWhoseSpecifier test]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1412482-test)Added [NSIndexSpecifier.index](https://developer.apple.com/documentation/foundation/nsindexspecifier/1408567-index)Added [-[NSNameSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsnamespecifier/1412623-init)Added [NSNameSpecifier.name](https://developer.apple.com/documentation/foundation/nsnamespecifier/1407411-name)Added [NSObject.objectSpecifier](https://developer.apple.com/documentation/objectivec/nsobject/1409884-objectspecifier)Added [NSPositionalSpecifier.insertionContainer](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1414957-insertioncontainer)Added [NSPositionalSpecifier.insertionIndex](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1414703-insertionindex)Added [NSPositionalSpecifier.insertionKey](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1414059-insertionkey)Added [NSPositionalSpecifier.insertionReplaces](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1411646-insertionreplaces)Added [NSPositionalSpecifier.objectSpecifier](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1412839-objectspecifier)Added [NSPositionalSpecifier.position](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1413865-position)Added [NSRangeSpecifier.endSpecifier](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418470-endspecifier)Added [-[NSRangeSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418021-init)Added [NSRangeSpecifier.startSpecifier](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418394-startspecifier)Added [NSRelativeSpecifier.baseSpecifier](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1409071-basespecifier)Added [-[NSRelativeSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1412403-init)Added [NSRelativeSpecifier.relativePosition](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1416001-relativeposition)Added [NSScriptObjectSpecifier.childSpecifier](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1409882-child)Added [NSScriptObjectSpecifier.containerClassDescription](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1413179-containerclassdescription)Added [NSScriptObjectSpecifier.containerIsObjectBeingTested](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1410887-containerisobjectbeingtested)Added [NSScriptObjectSpecifier.containerIsRangeContainerObject](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416507-containerisrangecontainerobject)Added [NSScriptObjectSpecifier.containerSpecifier](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1414424-container)Added [NSScriptObjectSpecifier.descriptor](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1410018-descriptor)Added [NSScriptObjectSpecifier.evaluationErrorNumber](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416938-evaluationerrornumber)Added [NSScriptObjectSpecifier.evaluationErrorSpecifier](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1416385-evaluationerror)Added [-[NSScriptObjectSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1408941-init)Added [NSScriptObjectSpecifier.key](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1412986-key)Added [NSScriptObjectSpecifier.keyClassDescription](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1417974-keyclassdescription)Added [NSScriptObjectSpecifier.objectsByEvaluatingSpecifier](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1413391-objectsbyevaluatingspecifier)Added [-[NSUniqueIDSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/1414481-initwithcoder)Added [NSUniqueIDSpecifier.uniqueID](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/1415634-uniqueid)Added [NSWhoseSpecifier.endSubelementIdentifier](https://developer.apple.com/documentation/foundation/nswhosespecifier/1407761-endsubelementidentifier)Added [NSWhoseSpecifier.endSubelementIndex](https://developer.apple.com/documentation/foundation/nswhosespecifier/1416686-endsubelementindex)Added [-[NSWhoseSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1418262-initwithcoder)Added [NSWhoseSpecifier.startSubelementIdentifier](https://developer.apple.com/documentation/foundation/nswhosespecifier/1413408-startsubelementidentifier)Added [NSWhoseSpecifier.startSubelementIndex](https://developer.apple.com/documentation/foundation/nswhosespecifier/1417856-startsubelementindex)Added [NSWhoseSpecifier.test](https://developer.apple.com/documentation/foundation/nswhosespecifier/1412482-test)Modified [-[NSIndexSpecifier initWithContainerClassDescription:containerSpecifier:key:index:]](https://developer.apple.com/documentation/foundation/nsindexspecifier/1407502-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property index:(NSInteger)index ``` | -- |
| To | ``` - (instancetype)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property index:(NSInteger)index ``` | yes |

Modified [-[NSNameSpecifier initWithContainerClassDescription:containerSpecifier:key:name:]](https://developer.apple.com/documentation/foundation/nsnamespecifier/1408615-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property name:(NSString *)name ``` | -- |
| To | ``` - (instancetype)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property name:(NSString *)name ``` | yes |

Modified [-[NSPositionalSpecifier initWithPosition:objectSpecifier:]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1416546-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithPosition:(NSInsertionPosition)position objectSpecifier:(NSScriptObjectSpecifier *)specifier ``` | -- |
| To | ``` - (instancetype)initWithPosition:(NSInsertionPosition)position objectSpecifier:(NSScriptObjectSpecifier *)specifier ``` | yes |

Modified [-[NSRangeSpecifier initWithContainerClassDescription:containerSpecifier:key:startSpecifier:endSpecifier:]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1409215-initwithcontainerclassdescriptio)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property startSpecifier:(NSScriptObjectSpecifier *)startSpec endSpecifier:(NSScriptObjectSpecifier *)endSpec ``` | -- |
| To | ``` - (instancetype)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property startSpecifier:(NSScriptObjectSpecifier *)startSpec endSpecifier:(NSScriptObjectSpecifier *)endSpec ``` | yes |

Modified [-[NSRelativeSpecifier initWithContainerClassDescription:containerSpecifier:key:relativePosition:baseSpecifier:]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1409205-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property relativePosition:(NSRelativePosition)relPos baseSpecifier:(NSScriptObjectSpecifier *)baseSpecifier ``` | -- |
| To | ``` - (instancetype)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property relativePosition:(NSRelativePosition)relPos baseSpecifier:(NSScriptObjectSpecifier *)baseSpecifier ``` | yes |

Modified [-[NSScriptObjectSpecifier initWithContainerClassDescription:containerSpecifier:key:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1410480-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property ``` | -- |
| To | ``` - (instancetype)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property ``` | yes |

Modified [-[NSScriptObjectSpecifier initWithContainerSpecifier:key:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1409384-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContainerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property ``` |
| To | ``` - (instancetype)initWithContainerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property ``` |

Modified [-[NSUniqueIDSpecifier initWithContainerClassDescription:containerSpecifier:key:uniqueID:]](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/1416055-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property uniqueID:(id)uniqueID ``` | -- |
| To | ``` - (instancetype)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property uniqueID:(id)uniqueID ``` | yes |

Modified [-[NSWhoseSpecifier initWithContainerClassDescription:containerSpecifier:key:test:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1412173-initwithcontainerclassdescriptio)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property test:(NSScriptWhoseTest *)test ``` | -- |
| To | ``` - (instancetype)initWithContainerClassDescription:(NSScriptClassDescription *)classDesc containerSpecifier:(NSScriptObjectSpecifier *)container key:(NSString *)property test:(NSScriptWhoseTest *)test ``` | yes |

NSScriptStandardSuiteCommands.hRemoved [-[NSCloneCommand keySpecifier]](https://developer.apple.com/documentation/foundation/nsclonecommand/1407603-keyspecifier)Removed [-[NSCloseCommand saveOptions]](https://developer.apple.com/documentation/foundation/nsclosecommand/1415647-saveoptions)Removed [-[NSCreateCommand createClassDescription]](https://developer.apple.com/documentation/foundation/nscreatecommand/1413533-createclassdescription)Removed [-[NSCreateCommand resolvedKeyDictionary]](https://developer.apple.com/documentation/foundation/nscreatecommand/1407639-resolvedkeydictionary)Removed [-[NSDeleteCommand keySpecifier]](https://developer.apple.com/documentation/foundation/nsdeletecommand/1414705-keyspecifier)Removed [-[NSMoveCommand keySpecifier]](https://developer.apple.com/documentation/foundation/nsmovecommand/1413005-keyspecifier)Removed [-[NSQuitCommand saveOptions]](https://developer.apple.com/documentation/foundation/nsquitcommand/1407440-saveoptions)Removed [-[NSSetCommand keySpecifier]](https://developer.apple.com/documentation/foundation/nssetcommand/1415804-keyspecifier)Added [NSCloneCommand.keySpecifier](https://developer.apple.com/documentation/foundation/nsclonecommand/1407603-keyspecifier)Added [NSCloseCommand.saveOptions](https://developer.apple.com/documentation/foundation/nsclosecommand/1415647-saveoptions)Added [NSCreateCommand.createClassDescription](https://developer.apple.com/documentation/foundation/nscreatecommand/1413533-createclassdescription)Added [NSCreateCommand.resolvedKeyDictionary](https://developer.apple.com/documentation/foundation/nscreatecommand/1407639-resolvedkeydictionary)Added [NSDeleteCommand.keySpecifier](https://developer.apple.com/documentation/foundation/nsdeletecommand/1414705-keyspecifier)Added [NSMoveCommand.keySpecifier](https://developer.apple.com/documentation/foundation/nsmovecommand/1413005-keyspecifier)Added [NSQuitCommand.saveOptions](https://developer.apple.com/documentation/foundation/nsquitcommand/1407440-saveoptions)Added [NSSetCommand.keySpecifier](https://developer.apple.com/documentation/foundation/nssetcommand/1415804-keyspecifier)NSScriptSuiteRegistry.hRemoved [-[NSScriptSuiteRegistry suiteNames]](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/1414452-suitenames)Added [NSScriptSuiteRegistry.suiteNames](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/1414452-suitenames)NSScriptWhoseTests.hAdded [-[NSScriptWhoseTest init]](https://developer.apple.com/documentation/foundation/nsscriptwhosetest/1393856-init)Added [-[NSScriptWhoseTest initWithCoder:]](https://developer.apple.com/documentation/foundation/nsscriptwhosetest/1393846-init)Added [-[NSSpecifierTest initWithCoder:]](https://developer.apple.com/documentation/foundation/nsspecifiertest/1393881-init)Modified [-[NSLogicalTest initAndTestWithTests:]](https://developer.apple.com/documentation/foundation/nslogicaltest/1393854-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initAndTestWithTests:(NSArray *)subTests ``` | -- |
| To | ``` - (instancetype)initAndTestWithTests:(NSArray *)subTests ``` | yes |

Modified [-[NSLogicalTest initNotTestWithTest:]](https://developer.apple.com/documentation/foundation/nslogicaltest/1393879-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initNotTestWithTest:(NSScriptWhoseTest *)subTest ``` | -- |
| To | ``` - (instancetype)initNotTestWithTest:(NSScriptWhoseTest *)subTest ``` | yes |

Modified [-[NSLogicalTest initOrTestWithTests:]](https://developer.apple.com/documentation/foundation/nslogicaltest/1393875-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initOrTestWithTests:(NSArray *)subTests ``` | -- |
| To | ``` - (instancetype)initOrTestWithTests:(NSArray *)subTests ``` | yes |

Modified [-[NSSpecifierTest initWithObjectSpecifier:comparisonOperator:testObject:]](https://developer.apple.com/documentation/foundation/nsspecifiertest/1393833-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithObjectSpecifier:(NSScriptObjectSpecifier *)obj1 comparisonOperator:(NSTestComparisonOperation)compOp testObject:(id)obj2 ``` | -- |
| To | ``` - (instancetype)initWithObjectSpecifier:(NSScriptObjectSpecifier *)obj1 comparisonOperator:(NSTestComparisonOperation)compOp testObject:(id)obj2 ``` | yes |

NSSet.hRemoved [-[NSSet allObjects]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/allObjects)Removed [-[NSSet count]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/count)Removed [-[NSSet description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/description)Added [-[NSMutableSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutableset/1407369-initwithcoder)Added [NSSet.allObjects](https://developer.apple.com/documentation/foundation/nsset/1417653-allobjects)Added [NSSet.count](https://developer.apple.com/documentation/foundation/nsset/1416229-count)Added [NSSet.description](https://developer.apple.com/documentation/foundation/nsset/1418176-description)Added [-[NSSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsset/1408221-initwithcoder)Modified [-[NSCountedSet initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/initWithArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithArray:(NSArray *)array ``` |
| To | ``` - (instancetype)initWithArray:(NSArray *)array ``` |

Modified [-[NSCountedSet initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCapacity:(NSUInteger)numItems ``` |
| To | ``` - (instancetype)initWithCapacity:(NSUInteger)numItems ``` |

Modified [-[NSCountedSet initWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/initWithSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSet:(NSSet *)set ``` |
| To | ``` - (instancetype)initWithSet:(NSSet *)set ``` |

Modified [-[NSMutableSet init]](https://developer.apple.com/documentation/foundation/nsmutableset/1414518-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableSet initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/initWithCapacity:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSet init]](https://developer.apple.com/documentation/foundation/nsset/1409698-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSSortDescriptor.hRemoved [-[NSSortDescriptor ascending]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1408931-ascending)Removed [-[NSSortDescriptor comparator]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1411426-comparator)Removed [-[NSSortDescriptor key]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1415022-key)Removed [-[NSSortDescriptor reversedSortDescriptor]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1407712-reversedsortdescriptor)Removed [-[NSSortDescriptor selector]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1418337-selector)Added [NSSortDescriptor.ascending](https://developer.apple.com/documentation/foundation/nssortdescriptor/1408931-ascending)Added [NSSortDescriptor.comparator](https://developer.apple.com/documentation/foundation/nssortdescriptor/1411426-comparator)Added [NSSortDescriptor.key](https://developer.apple.com/documentation/foundation/nssortdescriptor/1415022-key)Added [NSSortDescriptor.reversedSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor/1407712-reversedsortdescriptor)Added [NSSortDescriptor.selector](https://developer.apple.com/documentation/foundation/nssortdescriptor/1418337-selector)Modified [-[NSSortDescriptor initWithKey:ascending:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1413572-initwithkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithKey:(NSString *)key ascending:(BOOL)ascending ``` |
| To | ``` - (instancetype)initWithKey:(NSString *)key ascending:(BOOL)ascending ``` |

Modified [-[NSSortDescriptor initWithKey:ascending:comparator:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1411607-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithKey:(NSString *)key ascending:(BOOL)ascending comparator:(NSComparator)cmptr ``` |
| To | ``` - (instancetype)initWithKey:(NSString *)key ascending:(BOOL)ascending comparator:(NSComparator)cmptr ``` |

Modified [-[NSSortDescriptor initWithKey:ascending:selector:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1412495-initwithkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithKey:(NSString *)key ascending:(BOOL)ascending selector:(SEL)selector ``` |
| To | ``` - (instancetype)initWithKey:(NSString *)key ascending:(BOOL)ascending selector:(SEL)selector ``` |

Modified [+[NSSortDescriptor sortDescriptorWithKey:ascending:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1503726-sortdescriptorwithkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sortDescriptorWithKey:(NSString *)key ascending:(BOOL)ascending ``` |
| To | ``` + (instancetype)sortDescriptorWithKey:(NSString *)key ascending:(BOOL)ascending ``` |

Modified [+[NSSortDescriptor sortDescriptorWithKey:ascending:comparator:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1503734-sortdescriptorwithkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sortDescriptorWithKey:(NSString *)key ascending:(BOOL)ascending comparator:(NSComparator)cmptr ``` |
| To | ``` + (instancetype)sortDescriptorWithKey:(NSString *)key ascending:(BOOL)ascending comparator:(NSComparator)cmptr ``` |

Modified [+[NSSortDescriptor sortDescriptorWithKey:ascending:selector:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1503730-sortdescriptorwithkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sortDescriptorWithKey:(NSString *)key ascending:(BOOL)ascending selector:(SEL)selector ``` |
| To | ``` + (instancetype)sortDescriptorWithKey:(NSString *)key ascending:(BOOL)ascending selector:(SEL)selector ``` |

NSSpellServer.hRemoved [-[NSSpellServer delegate]](https://developer.apple.com/documentation/foundation/nsspellserver/1414240-delegate)Removed [-[NSSpellServer setDelegate:]](https://developer.apple.com/documentation/foundation/nsspellserver/1414240-delegate)Added [NSSpellServer.delegate](https://developer.apple.com/documentation/foundation/nsspellserver/1414240-delegate)Modified [-[NSSpellServerDelegate spellServer:checkGrammarInString:language:details:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1409242-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpellServerDelegate spellServer:checkString:offset:types:options:orthography:wordCount:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1409733-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpellServerDelegate spellServer:didForgetWord:inLanguage:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1417315-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpellServerDelegate spellServer:didLearnWord:inLanguage:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1407851-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpellServerDelegate spellServer:findMisspelledWordInString:language:wordCount:countOnly:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1413235-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpellServerDelegate spellServer:recordResponse:toCorrection:forWord:language:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1412894-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpellServerDelegate spellServer:suggestCompletionsForPartialWordRange:inString:language:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1414606-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpellServerDelegate spellServer:suggestGuessesForWord:inLanguage:]](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/1410726-spellserver)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSStream.hRemoved [-[NSInputStream hasBytesAvailable]](https://developer.apple.com/documentation/foundation/inputstream/1409410-hasbytesavailable)Removed [-[NSOutputStream hasSpaceAvailable]](https://developer.apple.com/documentation/foundation/outputstream/1411335-hasspaceavailable)Removed [-[NSStream delegate]](https://developer.apple.com/documentation/foundation/stream/1418423-delegate)Removed [-[NSStream setDelegate:]](https://developer.apple.com/documentation/foundation/stream/1418423-delegate)Removed [-[NSStream streamError]](https://developer.apple.com/documentation/foundation/stream/1416359-streamerror)Removed [-[NSStream streamStatus]](https://developer.apple.com/documentation/foundation/nsstream/1413038-streamstatus)Added [NSInputStream.hasBytesAvailable](https://developer.apple.com/documentation/foundation/inputstream/1409410-hasbytesavailable)Added [NSOutputStream.hasSpaceAvailable](https://developer.apple.com/documentation/foundation/nsoutputstream/1411335-hasspaceavailable)Added [NSStream.delegate](https://developer.apple.com/documentation/foundation/nsstream/1418423-delegate)Added [+[NSStream getBoundStreamsWithBufferSize:inputStream:outputStream:]](https://developer.apple.com/documentation/foundation/stream/1412683-getboundstreams)Added [+[NSStream getStreamsToHostWithName:port:inputStream:outputStream:]](https://developer.apple.com/documentation/foundation/stream/1414311-getstreamstohost)Added [NSStream.streamError](https://developer.apple.com/documentation/foundation/nsstream/1416359-streamerror)Added [NSStream.streamStatus](https://developer.apple.com/documentation/foundation/stream/1413038-streamstatus)Added NSStream(NSStreamBoundPairCreationExtensions)Modified [-[NSInputStream initWithData:]](https://developer.apple.com/documentation/foundation/nsinputstream/1412470-initwithdata)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` | -- |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` | yes |

Modified [-[NSInputStream initWithFileAtPath:]](https://developer.apple.com/documentation/foundation/nsinputstream/1408976-initwithfileatpath)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFileAtPath:(NSString *)path ``` |
| To | ``` - (instancetype)initWithFileAtPath:(NSString *)path ``` |

Modified [-[NSInputStream initWithURL:]](https://developer.apple.com/documentation/foundation/inputstream/1417891-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url ``` | -- |
| To | ``` - (instancetype)initWithURL:(NSURL *)url ``` | yes |

Modified [+[NSInputStream inputStreamWithData:]](https://developer.apple.com/documentation/foundation/nsinputstream/1564842-inputstreamwithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (id)inputStreamWithData:(NSData *)data ``` |
| To | ``` + (instancetype)inputStreamWithData:(NSData *)data ``` |

Modified [+[NSInputStream inputStreamWithFileAtPath:]](https://developer.apple.com/documentation/foundation/nsinputstream/1564839-inputstreamwithfileatpath)

|  | Declaration |
| --- | --- |
| From | ``` + (id)inputStreamWithFileAtPath:(NSString *)path ``` |
| To | ``` + (instancetype)inputStreamWithFileAtPath:(NSString *)path ``` |

Modified [+[NSInputStream inputStreamWithURL:]](https://developer.apple.com/documentation/foundation/nsinputstream/1564838-inputstreamwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)inputStreamWithURL:(NSURL *)url ``` |
| To | ``` + (instancetype)inputStreamWithURL:(NSURL *)url ``` |

Modified [-[NSOutputStream initToBuffer:capacity:]](https://developer.apple.com/documentation/foundation/outputstream/1410805-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initToBuffer:(uint8_t *)buffer capacity:(NSUInteger)capacity ``` | -- |
| To | ``` - (instancetype)initToBuffer:(uint8_t *)buffer capacity:(NSUInteger)capacity ``` | yes |

Modified [-[NSOutputStream initToFileAtPath:append:]](https://developer.apple.com/documentation/foundation/outputstream/1416367-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initToFileAtPath:(NSString *)path append:(BOOL)shouldAppend ``` |
| To | ``` - (instancetype)initToFileAtPath:(NSString *)path append:(BOOL)shouldAppend ``` |

Modified [-[NSOutputStream initToMemory]](https://developer.apple.com/documentation/foundation/outputstream/1409909-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initToMemory ``` | -- |
| To | ``` - (instancetype)initToMemory ``` | yes |

Modified [-[NSOutputStream initWithURL:append:]](https://developer.apple.com/documentation/foundation/outputstream/1414446-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url append:(BOOL)shouldAppend ``` | -- |
| To | ``` - (instancetype)initWithURL:(NSURL *)url append:(BOOL)shouldAppend ``` | yes |

Modified [+[NSOutputStream outputStreamToBuffer:capacity:]](https://developer.apple.com/documentation/foundation/nsoutputstream/1564837-outputstreamtobuffer)

|  | Declaration |
| --- | --- |
| From | ``` + (id)outputStreamToBuffer:(uint8_t *)buffer capacity:(NSUInteger)capacity ``` |
| To | ``` + (instancetype)outputStreamToBuffer:(uint8_t *)buffer capacity:(NSUInteger)capacity ``` |

Modified [+[NSOutputStream outputStreamToFileAtPath:append:]](https://developer.apple.com/documentation/foundation/nsoutputstream/1564841-outputstreamtofileatpath)

|  | Declaration |
| --- | --- |
| From | ``` + (id)outputStreamToFileAtPath:(NSString *)path append:(BOOL)shouldAppend ``` |
| To | ``` + (instancetype)outputStreamToFileAtPath:(NSString *)path append:(BOOL)shouldAppend ``` |

Modified [+[NSOutputStream outputStreamToMemory]](https://developer.apple.com/documentation/foundation/nsoutputstream/1411948-outputstreamtomemory)

|  | Declaration |
| --- | --- |
| From | ``` + (id)outputStreamToMemory ``` |
| To | ``` + (instancetype)outputStreamToMemory ``` |

Modified [+[NSOutputStream outputStreamWithURL:append:]](https://developer.apple.com/documentation/foundation/nsoutputstream/1564840-outputstreamwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)outputStreamWithURL:(NSURL *)url append:(BOOL)shouldAppend ``` |
| To | ``` + (instancetype)outputStreamWithURL:(NSURL *)url append:(BOOL)shouldAppend ``` |

Modified [+[NSStream getStreamsToHost:port:inputStream:outputStream:]](https://developer.apple.com/documentation/foundation/stream/1412686-getstreamsto)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSStreamDelegate stream:handleEvent:]](https://developer.apple.com/documentation/foundation/streamdelegate/1410079-stream)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSString.hRemoved [-[NSString UTF8String]](https://developer.apple.com/documentation/foundation/nsstring/1411189-utf8string)Removed [-[NSString boolValue]](https://developer.apple.com/documentation/foundation/nsstring/1409420-boolvalue)Removed [-[NSString capitalizedString]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/capitalizedString)Removed [-[NSString decomposedStringWithCanonicalMapping]](https://developer.apple.com/documentation/foundation/nsstring/1409474-decomposedstringwithcanonicalmap)Removed [-[NSString decomposedStringWithCompatibilityMapping]](https://developer.apple.com/documentation/foundation/nsstring/1415417-decomposedstringwithcompatibilit)Removed [-[NSString description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/description)Removed [-[NSString doubleValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/doubleValue)Removed [-[NSString fastestEncoding]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/fastestEncoding)Removed [-[NSString floatValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/floatValue)Removed [-[NSString hash]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/hash)Removed [-[NSString intValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/intValue)Removed [-[NSString integerValue]](https://developer.apple.com/documentation/foundation/nsstring/1410267-integervalue)Removed [-[NSString length]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/length)Removed [-[NSString longLongValue]](https://developer.apple.com/documentation/foundation/nsstring/1417731-longlongvalue)Removed [-[NSString lowercaseString]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/lowercaseString)Removed [-[NSString precomposedStringWithCanonicalMapping]](https://developer.apple.com/documentation/foundation/nsstring/1412645-precomposedstringwithcanonicalma)Removed [-[NSString precomposedStringWithCompatibilityMapping]](https://developer.apple.com/documentation/foundation/nsstring/1412625-precomposedstringwithcompatibili)Removed [-[NSString smallestEncoding]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/smallestEncoding)Removed [-[NSString uppercaseString]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/uppercaseString)Added [NSString.UTF8String](https://developer.apple.com/documentation/foundation/nsstring/1411189-utf8string)Added [NSString.boolValue](https://developer.apple.com/documentation/foundation/nsstring/1409420-boolvalue)Added [NSString.capitalizedString](https://developer.apple.com/documentation/foundation/nsstring/1416784-capitalizedstring)Added [-[NSString containsString:]](https://developer.apple.com/documentation/foundation/nsstring/1414563-contains)Added [NSString.decomposedStringWithCanonicalMapping](https://developer.apple.com/documentation/foundation/nsstring/1409474-decomposedstringwithcanonicalmap)Added [NSString.decomposedStringWithCompatibilityMapping](https://developer.apple.com/documentation/foundation/nsstring/1415417-decomposedstringwithcompatibilit)Added [NSString.description](https://developer.apple.com/documentation/foundation/nsstring/1410889-description)Added [NSString.doubleValue](https://developer.apple.com/documentation/foundation/nsstring/1414031-doublevalue)Added [NSString.fastestEncoding](https://developer.apple.com/documentation/foundation/nsstring/1409567-fastestencoding)Added [NSString.floatValue](https://developer.apple.com/documentation/foundation/nsstring/1412321-floatvalue)Added [NSString.hash](https://developer.apple.com/documentation/foundation/nsstring/1417245-hash)Added [-[NSString initWithCoder:]](https://developer.apple.com/documentation/foundation/nsstring/1407488-init)Added [NSString.intValue](https://developer.apple.com/documentation/foundation/nsstring/1414988-intvalue)Added [NSString.integerValue](https://developer.apple.com/documentation/foundation/nsstring/1410267-integervalue)Added [NSString.length](https://developer.apple.com/documentation/foundation/nsstring/1414212-length)Added [-[NSString localizedCaseInsensitiveContainsString:]](https://developer.apple.com/documentation/foundation/nsstring/1412098-localizedcaseinsensitivecontains)Added [NSString.longLongValue](https://developer.apple.com/documentation/foundation/nsstring/1417731-longlongvalue)Added [NSString.lowercaseString](https://developer.apple.com/documentation/foundation/nsstring/1408467-lowercasestring)Added [NSString.precomposedStringWithCanonicalMapping](https://developer.apple.com/documentation/foundation/nsstring/1412645-precomposedstringwithcanonicalma)Added [NSString.precomposedStringWithCompatibilityMapping](https://developer.apple.com/documentation/foundation/nsstring/1412625-precomposedstringwithcompatibili)Added [NSString.smallestEncoding](https://developer.apple.com/documentation/foundation/nsstring/1418037-smallestencoding)Added [+[NSString stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:]](https://developer.apple.com/documentation/foundation/nsstring/1413576-stringencoding)Added [NSString.uppercaseString](https://developer.apple.com/documentation/foundation/nsstring/1409855-uppercased)Added NSString(NSStringEncodingDetection)Added [NSStringEncodingDetectionAllowLossyKey](https://developer.apple.com/documentation/foundation/nsstringencodingdetectionallowlossykey)Added [NSStringEncodingDetectionDisallowedEncodingsKey](https://developer.apple.com/documentation/foundation/nsstringencodingdetectiondisallowedencodingskey)Added [NSStringEncodingDetectionFromWindowsKey](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/1411305-fromwindowskey)Added [NSStringEncodingDetectionLikelyLanguageKey](https://developer.apple.com/documentation/foundation/nsstringencodingdetectionlikelylanguagekey)Added [NSStringEncodingDetectionLossySubstitutionKey](https://developer.apple.com/documentation/foundation/nsstringencodingdetectionlossysubstitutionkey)Added [NSStringEncodingDetectionSuggestedEncodingsKey](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/1410590-suggestedencodingskey)Added [NSStringEncodingDetectionUseOnlySuggestedEncodingsKey](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/1414394-useonlysuggestedencodingskey)Modified [-[NSMutableString initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSMutableString/initWithCapacity:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCapacity:(NSUInteger)capacity ``` |
| To | ``` - (NSMutableString *)initWithCapacity:(NSUInteger)capacity ``` |

Modified [+[NSMutableString stringWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSMutableString/stringWithCapacity:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)stringWithCapacity:(NSUInteger)capacity ``` |
| To | ``` + (NSMutableString *)stringWithCapacity:(NSUInteger)capacity ``` |

Modified [-[NSString init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSTask.hRemoved [-[NSTask arguments]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/arguments)Removed [-[NSTask currentDirectoryPath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/currentDirectoryPath)Removed [-[NSTask environment]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/environment)Removed [-[NSTask isRunning]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/isRunning)Removed [-[NSTask launchPath]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/launchPath)Removed [-[NSTask processIdentifier]](https://developer.apple.com/documentation/foundation/nstask/1412022-processidentifier)Removed [-[NSTask setArguments:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/setArguments:)Removed [-[NSTask setCurrentDirectoryPath:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/setCurrentDirectoryPath:)Removed [-[NSTask setEnvironment:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/setEnvironment:)Removed [-[NSTask setLaunchPath:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/setLaunchPath:)Removed [-[NSTask setStandardError:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/setStandardError:)Removed [-[NSTask setStandardInput:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/setStandardInput:)Removed [-[NSTask setStandardOutput:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/setStandardOutput:)Removed [-[NSTask standardError]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/standardError)Removed [-[NSTask standardInput]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/standardInput)Removed [-[NSTask standardOutput]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/standardOutput)Removed [-[NSTask terminationReason]](https://developer.apple.com/documentation/foundation/process/1415605-terminationreason)Removed [-[NSTask terminationStatus]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/terminationStatus)Added [NSTask.arguments](https://developer.apple.com/documentation/foundation/process/1408983-arguments)Added [NSTask.currentDirectoryPath](https://developer.apple.com/documentation/foundation/process/1413110-currentdirectorypath)Added [NSTask.environment](https://developer.apple.com/documentation/foundation/nstask/1409412-environment)Added [NSTask.launchPath](https://developer.apple.com/documentation/foundation/nstask/1414221-launchpath)Added [NSTask.processIdentifier](https://developer.apple.com/documentation/foundation/process/1412022-processidentifier)Added [NSTask.qualityOfService](https://developer.apple.com/documentation/foundation/process/1415794-qualityofservice)Added [NSTask.running](https://developer.apple.com/documentation/foundation/nstask/1415788-running)Added [NSTask.standardError](https://developer.apple.com/documentation/foundation/process/1414916-standarderror)Added [NSTask.standardInput](https://developer.apple.com/documentation/foundation/nstask/1411576-standardinput)Added [NSTask.standardOutput](https://developer.apple.com/documentation/foundation/nstask/1407627-standardoutput)Added [NSTask.terminationReason](https://developer.apple.com/documentation/foundation/nstask/1415605-terminationreason)Added [NSTask.terminationStatus](https://developer.apple.com/documentation/foundation/process/1415801-terminationstatus)Modified [-[NSTask init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)init ``` | -- |
| To | ``` - (instancetype)init ``` | yes |

NSTextCheckingResult.hModified [NSTextCheckingResult.URL](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1417843-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *URL ``` |
| To | ``` @property(readonly, copy) NSURL *URL ``` |

Modified [NSTextCheckingResult.addressComponents](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413728-addresscomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *addressComponents ``` |
| To | ``` @property(readonly, copy) NSDictionary *addressComponents ``` |

Modified [NSTextCheckingResult.alternativeStrings](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415454-alternativestrings)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *alternativeStrings ``` |
| To | ``` @property(readonly, copy) NSArray *alternativeStrings ``` |

Modified [NSTextCheckingResult.components](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407367-components)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *components ``` |
| To | ``` @property(readonly, copy) NSDictionary *components ``` |

Modified [NSTextCheckingResult.date](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1414289-date)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *date ``` |
| To | ``` @property(readonly, copy) NSDate *date ``` |

Modified [NSTextCheckingResult.grammarDetails](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1408959-grammardetails)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *grammarDetails ``` |
| To | ``` @property(readonly, copy) NSArray *grammarDetails ``` |

Modified [NSTextCheckingResult.orthography](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1414551-orthography)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSOrthography *orthography ``` |
| To | ``` @property(readonly, copy) NSOrthography *orthography ``` |

Modified [NSTextCheckingResult.phoneNumber](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415511-phonenumber)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *phoneNumber ``` |
| To | ``` @property(readonly, copy) NSString *phoneNumber ``` |

Modified [NSTextCheckingResult.regularExpression](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1417393-regularexpression)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSRegularExpression *regularExpression ``` |
| To | ``` @property(readonly, copy) NSRegularExpression *regularExpression ``` |

Modified [NSTextCheckingResult.replacementString](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1412681-replacementstring)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *replacementString ``` |
| To | ``` @property(readonly, copy) NSString *replacementString ``` |

Modified [NSTextCheckingResult.timeZone](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1418476-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSTimeZone *timeZone ``` |
| To | ``` @property(readonly, copy) NSTimeZone *timeZone ``` |

NSThread.hRemoved [-[NSThread isCancelled]](https://developer.apple.com/documentation/foundation/nsthread/1417366-cancelled)Removed [-[NSThread isExecuting]](https://developer.apple.com/documentation/foundation/nsthread/1411240-executing)Removed [-[NSThread isFinished]](https://developer.apple.com/documentation/foundation/thread/1409297-isfinished)Removed [-[NSThread isMainThread]](https://developer.apple.com/documentation/foundation/thread/1408455-ismainthread)Removed [-[NSThread name]](https://developer.apple.com/documentation/foundation/nsthread/1414122-name)Removed [-[NSThread setName:]](https://developer.apple.com/documentation/foundation/nsthread/1414122-name)Removed [-[NSThread setStackSize:]](https://developer.apple.com/documentation/foundation/nsthread/1415190-stacksize)Removed [-[NSThread setThreadPriority:]](https://developer.apple.com/documentation/foundation/nsthread/1411927-threadpriority)Removed [-[NSThread stackSize]](https://developer.apple.com/documentation/foundation/nsthread/1415190-stacksize)Removed [-[NSThread threadDictionary]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/instm/NSThread/threadDictionary)Removed [-[NSThread threadPriority]](https://developer.apple.com/documentation/foundation/thread/1411927-threadpriority)Added [NSThread.cancelled](https://developer.apple.com/documentation/foundation/thread/1417366-iscancelled)Added [NSThread.executing](https://developer.apple.com/documentation/foundation/thread/1411240-isexecuting)Added [NSThread.finished](https://developer.apple.com/documentation/foundation/thread/1409297-isfinished)Added [NSThread.isMainThread](https://developer.apple.com/documentation/foundation/nsthread/1408455-ismainthread)Added [NSThread.name](https://developer.apple.com/documentation/foundation/thread/1414122-name)Added [NSThread.qualityOfService](https://developer.apple.com/documentation/foundation/nsthread/1409426-qualityofservice)Added [NSThread.stackSize](https://developer.apple.com/documentation/foundation/nsthread/1415190-stacksize)Added [NSThread.threadDictionary](https://developer.apple.com/documentation/foundation/thread/1411433-threaddictionary)Added [NSThread.threadPriority](https://developer.apple.com/documentation/foundation/nsthread/1411927-threadpriority)Modified [-[NSThread init]](https://developer.apple.com/documentation/foundation/nsthread/1416464-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)init ``` | -- |
| To | ``` - (instancetype)init ``` | yes |

Modified [-[NSThread initWithTarget:selector:object:]](https://developer.apple.com/documentation/foundation/nsthread/1414773-initwithtarget)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTarget:(id)target selector:(SEL)selector object:(id)argument ``` |
| To | ``` - (instancetype)initWithTarget:(id)target selector:(SEL)selector object:(id)argument ``` |

NSTimeZone.hRemoved [-[NSTimeZone abbreviation]](https://developer.apple.com/documentation/foundation/nstimezone/1387195-abbreviation)Removed [-[NSTimeZone data]](https://developer.apple.com/documentation/foundation/nstimezone/1387213-data)Removed [-[NSTimeZone daylightSavingTimeOffset]](https://developer.apple.com/documentation/foundation/nstimezone/1387235-daylightsavingtimeoffset)Removed [-[NSTimeZone description]](https://developer.apple.com/documentation/foundation/nstimezone/1387217-description)Removed [-[NSTimeZone isDaylightSavingTime]](https://developer.apple.com/documentation/foundation/nstimezone/1387191-daylightsavingtime)Removed [-[NSTimeZone name]](https://developer.apple.com/documentation/foundation/nstimezone/1387233-name)Removed [-[NSTimeZone nextDaylightSavingTimeTransition]](https://developer.apple.com/documentation/foundation/nstimezone/1387183-nextdaylightsavingtimetransition)Removed [-[NSTimeZone secondsFromGMT]](https://developer.apple.com/documentation/foundation/nstimezone/1387221-secondsfromgmt)Added [NSTimeZone.abbreviation](https://developer.apple.com/documentation/foundation/nstimezone/1387195-abbreviation)Added [NSTimeZone.data](https://developer.apple.com/documentation/foundation/nstimezone/1387213-data)Added [NSTimeZone.daylightSavingTime](https://developer.apple.com/documentation/foundation/nstimezone/1387191-isdaylightsavingtime)Added [NSTimeZone.daylightSavingTimeOffset](https://developer.apple.com/documentation/foundation/nstimezone/1387235-daylightsavingtimeoffset)Added [NSTimeZone.description](https://developer.apple.com/documentation/foundation/nstimezone/1387217-description)Added [NSTimeZone.name](https://developer.apple.com/documentation/foundation/nstimezone/1387233-name)Added [NSTimeZone.nextDaylightSavingTimeTransition](https://developer.apple.com/documentation/foundation/nstimezone/1387183-nextdaylightsavingtimetransition)Added [NSTimeZone.secondsFromGMT](https://developer.apple.com/documentation/foundation/nstimezone/1387221-secondsfromgmt)Modified [-[NSTimeZone initWithName:]](https://developer.apple.com/documentation/foundation/nstimezone/1387215-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(NSString *)tzName ``` |
| To | ``` - (instancetype)initWithName:(NSString *)tzName ``` |

Modified [-[NSTimeZone initWithName:data:]](https://developer.apple.com/documentation/foundation/nstimezone/1387250-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(NSString *)tzName data:(NSData *)aData ``` |
| To | ``` - (instancetype)initWithName:(NSString *)tzName data:(NSData *)aData ``` |

Modified [+[NSTimeZone timeZoneForSecondsFromGMT:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/timeZoneForSecondsFromGMT:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)timeZoneForSecondsFromGMT:(NSInteger)seconds ``` |
| To | ``` + (instancetype)timeZoneForSecondsFromGMT:(NSInteger)seconds ``` |

Modified [+[NSTimeZone timeZoneWithAbbreviation:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/timeZoneWithAbbreviation:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)timeZoneWithAbbreviation:(NSString *)abbreviation ``` |
| To | ``` + (instancetype)timeZoneWithAbbreviation:(NSString *)abbreviation ``` |

Modified [+[NSTimeZone timeZoneWithName:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/timeZoneWithName:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)timeZoneWithName:(NSString *)tzName ``` |
| To | ``` + (instancetype)timeZoneWithName:(NSString *)tzName ``` |

Modified [+[NSTimeZone timeZoneWithName:data:]](https://developer.apple.com/documentation/foundation/nstimezone/1387219-timezonewithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)timeZoneWithName:(NSString *)tzName data:(NSData *)aData ``` |
| To | ``` + (instancetype)timeZoneWithName:(NSString *)tzName data:(NSData *)aData ``` |

NSTimer.hRemoved [-[NSTimer fireDate]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/instm/NSTimer/fireDate)Removed [-[NSTimer isValid]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/instm/NSTimer/isValid)Removed [-[NSTimer setFireDate:]](https://developer.apple.com/documentation/foundation/timer/1407353-firedate)Removed [-[NSTimer setTolerance:]](https://developer.apple.com/documentation/foundation/nstimer/1415085-tolerance)Removed [-[NSTimer timeInterval]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/instm/NSTimer/timeInterval)Removed [-[NSTimer tolerance]](https://developer.apple.com/documentation/foundation/nstimer/1415085-tolerance)Removed [-[NSTimer userInfo]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/instm/NSTimer/userInfo)Added [NSTimer.fireDate](https://developer.apple.com/documentation/foundation/timer/1407353-firedate)Added [NSTimer.timeInterval](https://developer.apple.com/documentation/foundation/nstimer/1409024-timeinterval)Added [NSTimer.tolerance](https://developer.apple.com/documentation/foundation/nstimer/1415085-tolerance)Added [NSTimer.userInfo](https://developer.apple.com/documentation/foundation/timer/1408911-userinfo)Added [NSTimer.valid](https://developer.apple.com/documentation/foundation/timer/1408249-isvalid)Modified [-[NSTimer initWithFireDate:interval:target:selector:userInfo:repeats:]](https://developer.apple.com/documentation/foundation/nstimer/1415700-initwithfiredate)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFireDate:(NSDate *)date interval:(NSTimeInterval)ti target:(id)t selector:(SEL)s userInfo:(id)ui repeats:(BOOL)rep ``` | -- |
| To | ``` - (instancetype)initWithFireDate:(NSDate *)date interval:(NSTimeInterval)ti target:(id)t selector:(SEL)s userInfo:(id)ui repeats:(BOOL)rep ``` | yes |

NSURL.hRemoved [-[NSString stringByRemovingPercentEncoding]](https://developer.apple.com/documentation/foundation/nsstring/1409569-removingpercentencoding)Removed [-[NSURL URLByDeletingLastPathComponent]](https://developer.apple.com/documentation/foundation/nsurl/1411592-urlbydeletinglastpathcomponent)Removed [-[NSURL URLByDeletingPathExtension]](https://developer.apple.com/documentation/foundation/nsurl/1412357-deletingpathextension)Removed [-[NSURL URLByResolvingSymlinksInPath]](https://developer.apple.com/documentation/foundation/nsurl/1415965-resolvingsymlinksinpath)Removed [-[NSURL URLByStandardizingPath]](https://developer.apple.com/documentation/foundation/nsurl/1414302-urlbystandardizingpath)Removed [-[NSURL absoluteString]](https://developer.apple.com/documentation/foundation/nsurl/1409868-absolutestring)Removed [-[NSURL absoluteURL]](https://developer.apple.com/documentation/foundation/nsurl/1414266-absoluteurl)Removed [-[NSURL baseURL]](https://developer.apple.com/documentation/foundation/nsurl/1412311-baseurl)Removed [-[NSURL filePathURL]](https://developer.apple.com/documentation/foundation/nsurl/1408442-filepathurl)Removed [-[NSURL fileSystemRepresentation]](https://developer.apple.com/documentation/foundation/nsurl/1412925-filesystemrepresentation)Removed [-[NSURL fragment]](https://developer.apple.com/documentation/foundation/nsurl/1413775-fragment)Removed [-[NSURL host]](https://developer.apple.com/documentation/foundation/nsurl/1413640-host)Removed [-[NSURL isFileURL]](https://developer.apple.com/documentation/foundation/nsurl/1408782-isfileurl)Removed [-[NSURL lastPathComponent]](https://developer.apple.com/documentation/foundation/nsurl/1417444-lastpathcomponent)Removed [-[NSURL parameterString]](https://developer.apple.com/documentation/foundation/nsurl/1412797-parameterstring)Removed [-[NSURL password]](https://developer.apple.com/documentation/foundation/nsurl/1412096-password)Removed [-[NSURL path]](https://developer.apple.com/documentation/foundation/nsurl/1408809-path)Removed [-[NSURL pathComponents]](https://developer.apple.com/documentation/foundation/nsurl/1407365-pathcomponents)Removed [-[NSURL pathExtension]](https://developer.apple.com/documentation/foundation/nsurl/1410208-pathextension)Removed [-[NSURL port]](https://developer.apple.com/documentation/foundation/nsurl/1413455-port)Removed [-[NSURL query]](https://developer.apple.com/documentation/foundation/nsurl/1407543-query)Removed [-[NSURL relativePath]](https://developer.apple.com/documentation/foundation/nsurl/1410263-relativepath)Removed [-[NSURL relativeString]](https://developer.apple.com/documentation/foundation/nsurl/1411417-relativestring)Removed [-[NSURL resourceSpecifier]](https://developer.apple.com/documentation/foundation/nsurl/1415309-resourcespecifier)Removed [-[NSURL scheme]](https://developer.apple.com/documentation/foundation/nsurl/1413437-scheme)Removed [-[NSURL standardizedURL]](https://developer.apple.com/documentation/foundation/nsurl/1411073-standardized)Removed [-[NSURL user]](https://developer.apple.com/documentation/foundation/nsurl/1418335-user)Removed [-[NSURLComponents URL]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1413469-url)Added [-[NSFileSecurity initWithCoder:]](https://developer.apple.com/documentation/foundation/nsfilesecurity/1418382-initwithcoder)Added [NSString.stringByRemovingPercentEncoding](https://developer.apple.com/documentation/foundation/nsstring/1409569-removingpercentencoding)Added [NSURL.URLByDeletingLastPathComponent](https://developer.apple.com/documentation/foundation/nsurl/1411592-urlbydeletinglastpathcomponent)Added [NSURL.URLByDeletingPathExtension](https://developer.apple.com/documentation/foundation/nsurl/1412357-deletingpathextension)Added [+[NSURL URLByResolvingAliasFileAtURL:options:error:]](https://developer.apple.com/documentation/foundation/nsurl/1416404-urlbyresolvingaliasfileaturl)Added [NSURL.URLByResolvingSymlinksInPath](https://developer.apple.com/documentation/foundation/nsurl/1415965-resolvingsymlinksinpath)Added [NSURL.URLByStandardizingPath](https://developer.apple.com/documentation/foundation/nsurl/1414302-standardizingpath)Added [NSURL.absoluteString](https://developer.apple.com/documentation/foundation/nsurl/1409868-absolutestring)Added [NSURL.absoluteURL](https://developer.apple.com/documentation/foundation/nsurl/1414266-absoluteurl)Added [NSURL.baseURL](https://developer.apple.com/documentation/foundation/nsurl/1412311-baseurl)Added [-[NSURL checkPromisedItemIsReachableAndReturnError:]](https://developer.apple.com/documentation/foundation/nsurl/1410411-checkpromiseditemisreachableandr)Added [NSURL.filePathURL](https://developer.apple.com/documentation/foundation/nsurl/1408442-filepathurl)Added [NSURL.fileSystemRepresentation](https://developer.apple.com/documentation/foundation/nsurl/1412925-filesystemrepresentation)Added [NSURL.fileURL](https://developer.apple.com/documentation/foundation/nsurl/1408782-isfileurl)Added [NSURL.fragment](https://developer.apple.com/documentation/foundation/nsurl/1413775-fragment)Added [-[NSURL getPromisedItemResourceValue:forKey:error:]](https://developer.apple.com/documentation/foundation/nsurl/1414238-getpromiseditemresourcevalue)Added [NSURL.host](https://developer.apple.com/documentation/foundation/nsurl/1413640-host)Added [NSURL.lastPathComponent](https://developer.apple.com/documentation/foundation/nsurl/1417444-lastpathcomponent)Added [NSURL.parameterString](https://developer.apple.com/documentation/foundation/nsurl/1412797-parameterstring)Added [NSURL.password](https://developer.apple.com/documentation/foundation/nsurl/1412096-password)Added [NSURL.path](https://developer.apple.com/documentation/foundation/nsurl/1408809-path)Added [NSURL.pathComponents](https://developer.apple.com/documentation/foundation/nsurl/1407365-pathcomponents)Added [NSURL.pathExtension](https://developer.apple.com/documentation/foundation/nsurl/1410208-pathextension)Added [NSURL.port](https://developer.apple.com/documentation/foundation/nsurl/1413455-port)Added [-[NSURL promisedItemResourceValuesForKeys:error:]](https://developer.apple.com/documentation/foundation/nsurl/1407746-promiseditemresourcevalues)Added [NSURL.query](https://developer.apple.com/documentation/foundation/nsurl/1407543-query)Added [NSURL.relativePath](https://developer.apple.com/documentation/foundation/nsurl/1410263-relativepath)Added [NSURL.relativeString](https://developer.apple.com/documentation/foundation/nsurl/1411417-relativestring)Added [NSURL.resourceSpecifier](https://developer.apple.com/documentation/foundation/nsurl/1415309-resourcespecifier)Added [NSURL.scheme](https://developer.apple.com/documentation/foundation/nsurl/1413437-scheme)Added [NSURL.standardizedURL](https://developer.apple.com/documentation/foundation/nsurl/1411073-standardized)Added [NSURL.user](https://developer.apple.com/documentation/foundation/nsurl/1418335-user)Added [NSURLComponents.URL](https://developer.apple.com/documentation/foundation/nsurlcomponents/1413469-url)Added [NSURLComponents.queryItems](https://developer.apple.com/documentation/foundation/nsurlcomponents/1407752-queryitems)Added [NSURLComponents.string](https://developer.apple.com/documentation/foundation/nsurlcomponents/1417970-string)Added [NSURLQueryItem](https://developer.apple.com/documentation/foundation/nsurlqueryitem)Added [-[NSURLQueryItem initWithName:value:]](https://developer.apple.com/documentation/foundation/nsurlqueryitem/1410963-init)Added [NSURLQueryItem.name](https://developer.apple.com/documentation/foundation/nsurlqueryitem/1407785-name)Added [+[NSURLQueryItem queryItemWithName:value:]](https://developer.apple.com/documentation/foundation/nsurlqueryitem/1572045-queryitemwithname)Added [NSURLQueryItem.value](https://developer.apple.com/documentation/foundation/nsurlqueryitem/1412041-value)Added [NSThumbnail1024x1024SizeKey](https://developer.apple.com/documentation/foundation/nsthumbnail1024x1024sizekey)Added NSURL(NSPromisedItems)Added [NSURLAddedToDirectoryDateKey](https://developer.apple.com/documentation/foundation/nsurladdedtodirectorydatekey)Added [NSURLDocumentIdentifierKey](https://developer.apple.com/documentation/foundation/nsurldocumentidentifierkey)Added [NSURLGenerationIdentifierKey](https://developer.apple.com/documentation/foundation/nsurlgenerationidentifierkey)Added [NSURLQuarantinePropertiesKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1417114-quarantinepropertieskey)Added [NSURLThumbnailDictionaryKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1410313-thumbnaildictionarykey)Added [NSURLThumbnailKey](https://developer.apple.com/documentation/foundation/nsurlthumbnailkey)Added [NSURLUbiquitousItemContainerDisplayNameKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415832-ubiquitousitemcontainerdisplayna)Added [NSURLUbiquitousItemDownloadRequestedKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadrequestedkey)Modified [+[NSCharacterSet URLFragmentAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1412537-urlfragmentallowed)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLFragmentAllowedCharacterSet ``` |
| To | ``` + (NSCharacterSet *)URLFragmentAllowedCharacterSet ``` |

Modified [+[NSCharacterSet URLHostAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416426-urlhostallowedcharacterset)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLHostAllowedCharacterSet ``` |
| To | ``` + (NSCharacterSet *)URLHostAllowedCharacterSet ``` |

Modified [+[NSCharacterSet URLPasswordAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1417313-urlpasswordallowed)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLPasswordAllowedCharacterSet ``` |
| To | ``` + (NSCharacterSet *)URLPasswordAllowedCharacterSet ``` |

Modified [+[NSCharacterSet URLPathAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416804-urlpathallowed)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLPathAllowedCharacterSet ``` |
| To | ``` + (NSCharacterSet *)URLPathAllowedCharacterSet ``` |

Modified [+[NSCharacterSet URLQueryAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1416698-urlqueryallowed)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLQueryAllowedCharacterSet ``` |
| To | ``` + (NSCharacterSet *)URLQueryAllowedCharacterSet ``` |

Modified [+[NSCharacterSet URLUserAllowedCharacterSet]](https://developer.apple.com/documentation/foundation/nscharacterset/1411851-urluserallowedcharacterset)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLUserAllowedCharacterSet ``` |
| To | ``` + (NSCharacterSet *)URLUserAllowedCharacterSet ``` |

Modified [+[NSURL URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:]](https://developer.apple.com/documentation/foundation/nsurl/1572035-urlbyresolvingbookmarkdata)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLByResolvingBookmarkData:(NSData *)bookmarkData options:(NSURLBookmarkResolutionOptions)options relativeToURL:(NSURL *)relativeURL bookmarkDataIsStale:(BOOL *)isStale error:(NSError **)error ``` |
| To | ``` + (instancetype)URLByResolvingBookmarkData:(NSData *)bookmarkData options:(NSURLBookmarkResolutionOptions)options relativeToURL:(NSURL *)relativeURL bookmarkDataIsStale:(BOOL *)isStale error:(NSError **)error ``` |

Modified [+[NSURL URLWithString:]](https://developer.apple.com/documentation/foundation/nsurl/1572047-urlwithstring)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLWithString:(NSString *)URLString ``` |
| To | ``` + (instancetype)URLWithString:(NSString *)URLString ``` |

Modified [+[NSURL URLWithString:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1572049-urlwithstring)

|  | Declaration |
| --- | --- |
| From | ``` + (id)URLWithString:(NSString *)URLString relativeToURL:(NSURL *)baseURL ``` |
| To | ``` + (instancetype)URLWithString:(NSString *)URLString relativeToURL:(NSURL *)baseURL ``` |

Modified [+[NSURL fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1411492-fileurlwithfilesystemrepresentat)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileURLWithFileSystemRepresentation:(const char *)path isDirectory:(BOOL)isDir relativeToURL:(NSURL *)baseURL ``` |
| To | ``` + (NSURL *)fileURLWithFileSystemRepresentation:(const char *)path isDirectory:(BOOL)isDir relativeToURL:(NSURL *)baseURL ``` |

Modified [+[NSURL fileURLWithPath:]](https://developer.apple.com/documentation/foundation/nsurl/1410828-fileurlwithpath)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileURLWithPath:(NSString *)path ``` |
| To | ``` + (NSURL *)fileURLWithPath:(NSString *)path ``` |

Modified [+[NSURL fileURLWithPath:isDirectory:]](https://developer.apple.com/documentation/foundation/nsurl/1414650-fileurlwithpath)

|  | Declaration |
| --- | --- |
| From | ``` + (id)fileURLWithPath:(NSString *)path isDirectory:(BOOL)isDir ``` |
| To | ``` + (NSURL *)fileURLWithPath:(NSString *)path isDirectory:(BOOL)isDir ``` |

Modified [-[NSURL initByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:]](https://developer.apple.com/documentation/foundation/nsurl/1413475-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initByResolvingBookmarkData:(NSData *)bookmarkData options:(NSURLBookmarkResolutionOptions)options relativeToURL:(NSURL *)relativeURL bookmarkDataIsStale:(BOOL *)isStale error:(NSError **)error ``` |
| To | ``` - (instancetype)initByResolvingBookmarkData:(NSData *)bookmarkData options:(NSURLBookmarkResolutionOptions)options relativeToURL:(NSURL *)relativeURL bookmarkDataIsStale:(BOOL *)isStale error:(NSError **)error ``` |

Modified [-[NSURL initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1411210-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initFileURLWithFileSystemRepresentation:(const char *)path isDirectory:(BOOL)isDir relativeToURL:(NSURL *)baseURL ``` | -- |
| To | ``` - (instancetype)initFileURLWithFileSystemRepresentation:(const char *)path isDirectory:(BOOL)isDir relativeToURL:(NSURL *)baseURL ``` | yes |

Modified [-[NSURL initFileURLWithPath:]](https://developer.apple.com/documentation/foundation/nsurl/1410301-initfileurlwithpath)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initFileURLWithPath:(NSString *)path ``` | -- |
| To | ``` - (instancetype)initFileURLWithPath:(NSString *)path ``` | yes |

Modified [-[NSURL initFileURLWithPath:isDirectory:]](https://developer.apple.com/documentation/foundation/nsurl/1417505-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initFileURLWithPath:(NSString *)path isDirectory:(BOOL)isDir ``` | -- |
| To | ``` - (instancetype)initFileURLWithPath:(NSString *)path isDirectory:(BOOL)isDir ``` | yes |

Modified [-[NSURL initWithScheme:host:path:]](https://developer.apple.com/documentation/foundation/nsurl/1414181-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithScheme:(NSString *)scheme host:(NSString *)host path:(NSString *)path ``` |
| To | ``` - (instancetype)initWithScheme:(NSString *)scheme host:(NSString *)host path:(NSString *)path ``` |

Modified [-[NSURL initWithString:]](https://developer.apple.com/documentation/foundation/nsurl/1413146-initwithstring)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithString:(NSString *)URLString ``` |
| To | ``` - (instancetype)initWithString:(NSString *)URLString ``` |

Modified [-[NSURL initWithString:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1417949-initwithstring)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithString:(NSString *)URLString relativeToURL:(NSURL *)baseURL ``` | -- |
| To | ``` - (instancetype)initWithString:(NSString *)URLString relativeToURL:(NSURL *)baseURL ``` | yes |

Modified [+[NSURLComponents componentsWithString:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1572054-componentswithstring)

|  | Declaration |
| --- | --- |
| From | ``` + (id)componentsWithString:(NSString *)URLString ``` |
| To | ``` + (instancetype)componentsWithString:(NSString *)URLString ``` |

Modified [+[NSURLComponents componentsWithURL:resolvingAgainstBaseURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1572050-componentswithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)componentsWithURL:(NSURL *)url resolvingAgainstBaseURL:(BOOL)resolve ``` |
| To | ``` + (instancetype)componentsWithURL:(NSURL *)url resolvingAgainstBaseURL:(BOOL)resolve ``` |

Modified [-[NSURLComponents init]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1414141-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSURLComponents initWithString:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410784-initwithstring)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithString:(NSString *)URLString ``` |
| To | ``` - (instancetype)initWithString:(NSString *)URLString ``` |

Modified [-[NSURLComponents initWithURL:resolvingAgainstBaseURL:]](https://developer.apple.com/documentation/foundation/nsurlcomponents/1416476-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url resolvingAgainstBaseURL:(BOOL)resolve ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url resolvingAgainstBaseURL:(BOOL)resolve ``` |

NSURLAuthenticationChallenge.hRemoved [-[NSURLAuthenticationChallenge error]](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1413033-error)Removed [-[NSURLAuthenticationChallenge failureResponse]](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1414978-failureresponse)Removed [-[NSURLAuthenticationChallenge previousFailureCount]](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1416522-previousfailurecount)Removed [-[NSURLAuthenticationChallenge proposedCredential]](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1417749-proposedcredential)Removed [-[NSURLAuthenticationChallenge protectionSpace]](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1410012-protectionspace)Removed [-[NSURLAuthenticationChallenge sender]](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1407533-sender)Added [NSURLAuthenticationChallenge.error](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1413033-error)Added [NSURLAuthenticationChallenge.failureResponse](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1414978-failureresponse)Added [NSURLAuthenticationChallenge.previousFailureCount](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1416522-previousfailurecount)Added [NSURLAuthenticationChallenge.proposedCredential](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1417749-proposedcredential)Added [NSURLAuthenticationChallenge.protectionSpace](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1410012-protectionspace)Added [NSURLAuthenticationChallenge.sender](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1407533-sender)Modified [-[NSURLAuthenticationChallenge initWithAuthenticationChallenge:sender:]](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1411154-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge sender:(id<NSURLAuthenticationChallengeSender>)sender ``` |
| To | ``` - (instancetype)initWithAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge sender:(id<NSURLAuthenticationChallengeSender>)sender ``` |

Modified [-[NSURLAuthenticationChallenge initWithProtectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:]](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/1416511-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProtectionSpace:(NSURLProtectionSpace *)space proposedCredential:(NSURLCredential *)credential previousFailureCount:(NSInteger)previousFailureCount failureResponse:(NSURLResponse *)response error:(NSError *)error sender:(id<NSURLAuthenticationChallengeSender>)sender ``` |
| To | ``` - (instancetype)initWithProtectionSpace:(NSURLProtectionSpace *)space proposedCredential:(NSURLCredential *)credential previousFailureCount:(NSInteger)previousFailureCount failureResponse:(NSURLResponse *)response error:(NSError *)error sender:(id<NSURLAuthenticationChallengeSender>)sender ``` |

Modified [-[NSURLAuthenticationChallengeSender performDefaultHandlingForAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/1414590-performdefaulthandling)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLAuthenticationChallengeSender rejectProtectionSpaceAndContinueWithChallenge:]](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallengesender/1417331-rejectprotectionspaceandcontinue)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSURLCache.hRemoved [-[NSCachedURLResponse data]](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1414011-data)Removed [-[NSCachedURLResponse response]](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1411077-response)Removed [-[NSCachedURLResponse storagePolicy]](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1412269-storagepolicy)Removed [-[NSCachedURLResponse userInfo]](https://developer.apple.com/documentation/foundation/cachedurlresponse/1411900-userinfo)Removed [-[NSURLCache currentDiskUsage]](https://developer.apple.com/documentation/foundation/nsurlcache/1407771-currentdiskusage)Removed [-[NSURLCache currentMemoryUsage]](https://developer.apple.com/documentation/foundation/nsurlcache/1408199-currentmemoryusage)Removed [-[NSURLCache diskCapacity]](https://developer.apple.com/documentation/foundation/urlcache/1413505-diskcapacity)Removed [-[NSURLCache memoryCapacity]](https://developer.apple.com/documentation/foundation/urlcache/1409781-memorycapacity)Removed [-[NSURLCache setDiskCapacity:]](https://developer.apple.com/documentation/foundation/nsurlcache/1413505-diskcapacity)Removed [-[NSURLCache setMemoryCapacity:]](https://developer.apple.com/documentation/foundation/urlcache/1409781-memorycapacity)Added [NSCachedURLResponse.data](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1414011-data)Added [NSCachedURLResponse.response](https://developer.apple.com/documentation/foundation/cachedurlresponse/1411077-response)Added [NSCachedURLResponse.storagePolicy](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1412269-storagepolicy)Added [NSCachedURLResponse.userInfo](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1411900-userinfo)Added [NSURLCache.currentDiskUsage](https://developer.apple.com/documentation/foundation/nsurlcache/1407771-currentdiskusage)Added [NSURLCache.currentMemoryUsage](https://developer.apple.com/documentation/foundation/nsurlcache/1408199-currentmemoryusage)Added [NSURLCache.diskCapacity](https://developer.apple.com/documentation/foundation/urlcache/1413505-diskcapacity)Added [-[NSURLCache getCachedResponseForDataTask:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlcache/1409184-getcachedresponsefordatatask)Added [NSURLCache.memoryCapacity](https://developer.apple.com/documentation/foundation/nsurlcache/1409781-memorycapacity)Added [-[NSURLCache removeCachedResponseForDataTask:]](https://developer.apple.com/documentation/foundation/nsurlcache/1412258-removecachedresponsefordatatask)Added [-[NSURLCache removeCachedResponsesSinceDate:]](https://developer.apple.com/documentation/foundation/nsurlcache/1415231-removecachedresponsessincedate)Added [-[NSURLCache storeCachedResponse:forDataTask:]](https://developer.apple.com/documentation/foundation/urlcache/1414434-storecachedresponse)Added NSURLCache(NSURLSessionTaskAdditions)Modified [NSCachedURLResponse](https://developer.apple.com/documentation/foundation/cachedurlresponse)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [-[NSCachedURLResponse initWithResponse:data:]](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1413035-initwithresponse)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithResponse:(NSURLResponse *)response data:(NSData *)data ``` |
| To | ``` - (instancetype)initWithResponse:(NSURLResponse *)response data:(NSData *)data ``` |

Modified [-[NSCachedURLResponse initWithResponse:data:userInfo:storagePolicy:]](https://developer.apple.com/documentation/foundation/cachedurlresponse/1411556-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithResponse:(NSURLResponse *)response data:(NSData *)data userInfo:(NSDictionary *)userInfo storagePolicy:(NSURLCacheStoragePolicy)storagePolicy ``` |
| To | ``` - (instancetype)initWithResponse:(NSURLResponse *)response data:(NSData *)data userInfo:(NSDictionary *)userInfo storagePolicy:(NSURLCacheStoragePolicy)storagePolicy ``` |

Modified [-[NSURLCache initWithMemoryCapacity:diskCapacity:diskPath:]](https://developer.apple.com/documentation/foundation/nsurlcache/1415637-initwithmemorycapacity)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMemoryCapacity:(NSUInteger)memoryCapacity diskCapacity:(NSUInteger)diskCapacity diskPath:(NSString *)path ``` |
| To | ``` - (instancetype)initWithMemoryCapacity:(NSUInteger)memoryCapacity diskCapacity:(NSUInteger)diskCapacity diskPath:(NSString *)path ``` |

NSURLConnection.hRemoved [-[NSURLConnection currentRequest]](https://developer.apple.com/documentation/foundation/nsurlconnection/1409060-currentrequest)Removed [-[NSURLConnection originalRequest]](https://developer.apple.com/documentation/foundation/nsurlconnection/1411340-originalrequest)Added [NSURLConnection.currentRequest](https://developer.apple.com/documentation/foundation/nsurlconnection/1409060-currentrequest)Added [NSURLConnection.originalRequest](https://developer.apple.com/documentation/foundation/nsurlconnection/1411340-originalrequest)Modified [-[NSURLConnection initWithRequest:delegate:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1414520-initwithrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRequest:(NSURLRequest *)request delegate:(id)delegate ``` |
| To | ``` - (instancetype)initWithRequest:(NSURLRequest *)request delegate:(id)delegate ``` |

Modified [-[NSURLConnection initWithRequest:delegate:startImmediately:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1418425-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRequest:(NSURLRequest *)request delegate:(id)delegate startImmediately:(BOOL)startImmediately ``` |
| To | ``` - (instancetype)initWithRequest:(NSURLRequest *)request delegate:(id)delegate startImmediately:(BOOL)startImmediately ``` |

Modified [-[NSURLConnectionDataDelegate connection:didReceiveData:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1414090-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDataDelegate connection:didReceiveResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1407728-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDataDelegate connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1418264-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDataDelegate connection:needNewBodyStream:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1412892-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDataDelegate connection:willCacheResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1414834-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDataDelegate connection:willSendRequest:redirectResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1415830-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDataDelegate connectionDidFinishLoading:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1416409-connectiondidfinishloading)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDelegate connection:canAuthenticateAgainstProtectionSpace:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1415706-connection)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[NSURLConnectionDelegate connection:didCancelAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1407177-connection)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[NSURLConnectionDelegate connection:didFailWithError:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1418443-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDelegate connection:didReceiveAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1417135-connection)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[NSURLConnectionDelegate connection:willSendRequestForAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1414078-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDelegate connectionShouldUseCredentialStorage:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1414890-connectionshouldusecredentialsto)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDownloadDelegate connection:didWriteData:totalBytesWritten:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1418304-connection)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLConnectionDownloadDelegate connectionDidResumeDownloading:totalBytesWritten:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1418157-connectiondidresumedownloading)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSURLCredential.hRemoved [-[NSURLCredential certificates]](https://developer.apple.com/documentation/foundation/urlcredential/1412369-certificates)Removed [-[NSURLCredential hasPassword]](https://developer.apple.com/documentation/foundation/nsurlcredential/1418072-haspassword)Removed [-[NSURLCredential identity]](https://developer.apple.com/documentation/foundation/urlcredential/1411514-identity)Removed [-[NSURLCredential password]](https://developer.apple.com/documentation/foundation/nsurlcredential/1417913-password)Removed [-[NSURLCredential persistence]](https://developer.apple.com/documentation/foundation/nsurlcredential/1416977-persistence)Removed [-[NSURLCredential user]](https://developer.apple.com/documentation/foundation/urlcredential/1408654-user)Added [NSURLCredential.certificates](https://developer.apple.com/documentation/foundation/urlcredential/1412369-certificates)Added [NSURLCredential.hasPassword](https://developer.apple.com/documentation/foundation/nsurlcredential/1418072-haspassword)Added [NSURLCredential.identity](https://developer.apple.com/documentation/foundation/nsurlcredential/1411514-identity)Added [NSURLCredential.password](https://developer.apple.com/documentation/foundation/urlcredential/1417913-password)Added [NSURLCredential.persistence](https://developer.apple.com/documentation/foundation/nsurlcredential/1416977-persistence)Added [NSURLCredential.user](https://developer.apple.com/documentation/foundation/urlcredential/1408654-user)Modified [-[NSURLCredential initWithIdentity:certificates:persistence:]](https://developer.apple.com/documentation/foundation/nsurlcredential/1418121-initwithidentity)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIdentity:(SecIdentityRef)identity certificates:(NSArray *)certArray persistence:(NSURLCredentialPersistence)persistence ``` |
| To | ``` - (instancetype)initWithIdentity:(SecIdentityRef)identity certificates:(NSArray *)certArray persistence:(NSURLCredentialPersistence)persistence ``` |

Modified [-[NSURLCredential initWithTrust:]](https://developer.apple.com/documentation/foundation/urlcredential/1413935-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTrust:(SecTrustRef)trust ``` |
| To | ``` - (instancetype)initWithTrust:(SecTrustRef)trust ``` |

Modified [-[NSURLCredential initWithUser:password:persistence:]](https://developer.apple.com/documentation/foundation/urlcredential/1417977-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithUser:(NSString *)user password:(NSString *)password persistence:(NSURLCredentialPersistence)persistence ``` |
| To | ``` - (instancetype)initWithUser:(NSString *)user password:(NSString *)password persistence:(NSURLCredentialPersistence)persistence ``` |

NSURLCredentialStorage.hRemoved [-[NSURLCredentialStorage allCredentials]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1413859-allcredentials)Added [NSURLCredentialStorage.allCredentials](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1413859-allcredentials)Added [-[NSURLCredentialStorage getCredentialsForProtectionSpace:task:completionHandler:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1418119-getcredentials)Added [-[NSURLCredentialStorage getDefaultCredentialForProtectionSpace:task:completionHandler:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1411794-getdefaultcredential)Added [-[NSURLCredentialStorage removeCredential:forProtectionSpace:options:task:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1407237-remove)Added [-[NSURLCredentialStorage setCredential:forProtectionSpace:task:]](https://developer.apple.com/documentation/foundation/nsurlcredentialstorage/1412703-setcredential)Added [-[NSURLCredentialStorage setDefaultCredential:forProtectionSpace:task:]](https://developer.apple.com/documentation/foundation/nsurlcredentialstorage/1416429-setdefaultcredential)Added NSURLCredentialStorage(NSURLSessionTaskAdditions)NSURLDownload.hRemoved [-[NSURLDownload deletesFileUponFailure]](https://developer.apple.com/documentation/foundation/nsurldownload/1409172-deletesfileuponfailure)Removed [-[NSURLDownload request]](https://developer.apple.com/documentation/foundation/nsurldownload/1416157-request)Removed [-[NSURLDownload resumeData]](https://developer.apple.com/documentation/foundation/nsurldownload/1413244-resumedata)Removed [-[NSURLDownload setDeletesFileUponFailure:]](https://developer.apple.com/documentation/foundation/nsurldownload/1409172-deletesfileuponfailure)Added [NSURLDownload.deletesFileUponFailure](https://developer.apple.com/documentation/foundation/nsurldownload/1409172-deletesfileuponfailure)Added [NSURLDownload.request](https://developer.apple.com/documentation/foundation/nsurldownload/1416157-request)Added [NSURLDownload.resumeData](https://developer.apple.com/documentation/foundation/nsurldownload/1413244-resumedata)Modified [-[NSURLDownload initWithRequest:delegate:]](https://developer.apple.com/documentation/foundation/nsurldownload/1416302-initwithrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRequest:(NSURLRequest *)request delegate:(id<NSURLDownloadDelegate>)delegate ``` |
| To | ``` - (instancetype)initWithRequest:(NSURLRequest *)request delegate:(id<NSURLDownloadDelegate>)delegate ``` |

Modified [-[NSURLDownload initWithResumeData:delegate:path:]](https://developer.apple.com/documentation/foundation/nsurldownload/1412919-initwithresumedata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithResumeData:(NSData *)resumeData delegate:(id<NSURLDownloadDelegate>)delegate path:(NSString *)path ``` |
| To | ``` - (instancetype)initWithResumeData:(NSData *)resumeData delegate:(id<NSURLDownloadDelegate>)delegate path:(NSString *)path ``` |

Modified [-[NSURLDownloadDelegate download:canAuthenticateAgainstProtectionSpace:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1417213-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:decideDestinationWithSuggestedFilename:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1413588-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:didCancelAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1416233-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:didCreateDestination:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1415265-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:didFailWithError:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1411640-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:didReceiveAuthenticationChallenge:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1411969-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:didReceiveDataOfLength:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1413663-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:didReceiveResponse:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1415460-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:shouldDecodeSourceDataOfMIMEType:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1408526-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:willResumeWithResponse:fromByte:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1409514-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate download:willSendRequest:redirectResponse:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1412181-download)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate downloadDidBegin:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1409618-downloaddidbegin)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate downloadDidFinish:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1408884-downloaddidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLDownloadDelegate downloadShouldUseCredentialStorage:]](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/1416506-downloadshouldusecredentialstora)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSURLError.hAdded [NSURLErrorBackgroundSessionInUseByAnotherProcess](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes/nsurlerrorbackgroundsessioninusebyanotherprocess)Added [NSURLErrorBackgroundSessionRequiresSharedContainer](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes/nsurlerrorbackgroundsessionrequiressharedcontainer)Added [NSURLErrorBackgroundSessionWasDisconnected](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes/nsurlerrorbackgroundsessionwasdisconnected)Added [NSURLErrorBackgroundTaskCancelledReasonKey](https://developer.apple.com/documentation/foundation/nsurlerrorbackgroundtaskcancelledreasonkey)Added [NSURLErrorCancelledReasonBackgroundUpdatesDisabled](https://developer.apple.com/documentation/foundation/nsurlerrorcancelledreasonbackgroundupdatesdisabled)Added [NSURLErrorCancelledReasonInsufficientSystemResources](https://developer.apple.com/documentation/foundation/1508626-background_task_cancellation_rea/nsurlerrorcancelledreasoninsufficientsystemresources)Added [NSURLErrorCancelledReasonUserForceQuitApplication](https://developer.apple.com/documentation/foundation/nsurlerrorcancelledreasonuserforcequitapplication)NSURLProtectionSpace.hRemoved [-[NSURLProtectionSpace authenticationMethod]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1415028-authenticationmethod)Removed [-[NSURLProtectionSpace distinguishedNames]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1417061-distinguishednames)Removed [-[NSURLProtectionSpace host]](https://developer.apple.com/documentation/foundation/urlprotectionspace/1418205-host)Removed [-[NSURLProtectionSpace isProxy]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1561656-isproxy)Removed [-[NSURLProtectionSpace port]](https://developer.apple.com/documentation/foundation/urlprotectionspace/1408716-port)Removed [-[NSURLProtectionSpace protocol]](https://developer.apple.com/documentation/foundation/urlprotectionspace/1411191-protocol)Removed [-[NSURLProtectionSpace proxyType]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1411924-proxytype)Removed [-[NSURLProtectionSpace realm]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1416007-realm)Removed [-[NSURLProtectionSpace receivesCredentialSecurely]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1415176-receivescredentialsecurely)Removed [-[NSURLProtectionSpace serverTrust]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1409926-servertrust)Added [NSURLProtectionSpace.authenticationMethod](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1415028-authenticationmethod)Added [NSURLProtectionSpace.distinguishedNames](https://developer.apple.com/documentation/foundation/urlprotectionspace/1417061-distinguishednames)Added [NSURLProtectionSpace.host](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1418205-host)Added [NSURLProtectionSpace.isProxy](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1561656-isproxy)Added [NSURLProtectionSpace.port](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1408716-port)Added [NSURLProtectionSpace.protocol](https://developer.apple.com/documentation/foundation/urlprotectionspace/1411191-protocol)Added [NSURLProtectionSpace.proxyType](https://developer.apple.com/documentation/foundation/urlprotectionspace/1411924-proxytype)Added [NSURLProtectionSpace.realm](https://developer.apple.com/documentation/foundation/urlprotectionspace/1416007-realm)Added [NSURLProtectionSpace.receivesCredentialSecurely](https://developer.apple.com/documentation/foundation/urlprotectionspace/1415176-receivescredentialsecurely)Added [NSURLProtectionSpace.serverTrust](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1409926-servertrust)Modified [-[NSURLProtectionSpace initWithHost:port:protocol:realm:authenticationMethod:]](https://developer.apple.com/documentation/foundation/urlprotectionspace/1414165-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithHost:(NSString *)host port:(NSInteger)port protocol:(NSString *)protocol realm:(NSString *)realm authenticationMethod:(NSString *)authenticationMethod ``` |
| To | ``` - (instancetype)initWithHost:(NSString *)host port:(NSInteger)port protocol:(NSString *)protocol realm:(NSString *)realm authenticationMethod:(NSString *)authenticationMethod ``` |

Modified [-[NSURLProtectionSpace initWithProxyHost:port:type:realm:authenticationMethod:]](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1417998-initwithproxyhost)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProxyHost:(NSString *)host port:(NSInteger)port type:(NSString *)type realm:(NSString *)realm authenticationMethod:(NSString *)authenticationMethod ``` |
| To | ``` - (instancetype)initWithProxyHost:(NSString *)host port:(NSInteger)port type:(NSString *)type realm:(NSString *)realm authenticationMethod:(NSString *)authenticationMethod ``` |

NSURLProtocol.hRemoved [-[NSURLProtocol cachedResponse]](https://developer.apple.com/documentation/foundation/nsurlprotocol/1418409-cachedresponse)Removed [-[NSURLProtocol client]](https://developer.apple.com/documentation/foundation/urlprotocol/1413722-client)Removed [-[NSURLProtocol request]](https://developer.apple.com/documentation/foundation/urlprotocol/1412383-request)Added [NSURLProtocol.cachedResponse](https://developer.apple.com/documentation/foundation/urlprotocol/1418409-cachedresponse)Added [+[NSURLProtocol canInitWithTask:]](https://developer.apple.com/documentation/foundation/urlprotocol/1416997-caninit)Added [NSURLProtocol.client](https://developer.apple.com/documentation/foundation/urlprotocol/1413722-client)Added [-[NSURLProtocol initWithTask:cachedResponse:client:]](https://developer.apple.com/documentation/foundation/urlprotocol/1417672-init)Added [NSURLProtocol.request](https://developer.apple.com/documentation/foundation/urlprotocol/1412383-request)Added [NSURLProtocol.task](https://developer.apple.com/documentation/foundation/urlprotocol/1407649-task)Added NSURLProtocol(NSURLSessionTaskAdditions)Modified [-[NSURLProtocol initWithRequest:cachedResponse:client:]](https://developer.apple.com/documentation/foundation/urlprotocol/1414366-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRequest:(NSURLRequest *)request cachedResponse:(NSCachedURLResponse *)cachedResponse client:(id<NSURLProtocolClient>)client ``` |
| To | ``` - (instancetype)initWithRequest:(NSURLRequest *)request cachedResponse:(NSCachedURLResponse *)cachedResponse client:(id<NSURLProtocolClient>)client ``` |

NSURLRequest.hRemoved [-[NSMutableURLRequest setAllHTTPHeaderFields:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414617-allhttpheaderfields)Removed [-[NSMutableURLRequest setAllowsCellularAccess:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1416749-allowscellularaccess)Removed [-[NSMutableURLRequest setCachePolicy:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414716-cachepolicy)Removed [-[NSMutableURLRequest setHTTPBody:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1409064-httpbody)Removed [-[NSMutableURLRequest setHTTPBodyStream:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1409529-httpbodystream)Removed [-[NSMutableURLRequest setHTTPMethod:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1413047-httpmethod)Removed [-[NSMutableURLRequest setHTTPShouldHandleCookies:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1415485-httpshouldhandlecookies)Removed [-[NSMutableURLRequest setHTTPShouldUsePipelining:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1412705-httpshouldusepipelining)Removed [-[NSMutableURLRequest setMainDocumentURL:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1415630-maindocumenturl)Removed [-[NSMutableURLRequest setNetworkServiceType:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1412378-networkservicetype)Removed [-[NSMutableURLRequest setTimeoutInterval:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414063-timeoutinterval)Removed [-[NSMutableURLRequest setURL:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1410342-url)Removed [-[NSURLRequest HTTPBody]](https://developer.apple.com/documentation/foundation/nsurlrequest/1411317-httpbody)Removed [-[NSURLRequest HTTPBodyStream]](https://developer.apple.com/documentation/foundation/nsurlrequest/1407341-httpbodystream)Removed [-[NSURLRequest HTTPMethod]](https://developer.apple.com/documentation/foundation/nsurlrequest/1413030-httpmethod)Removed [-[NSURLRequest HTTPShouldHandleCookies]](https://developer.apple.com/documentation/foundation/nsurlrequest/1418369-httpshouldhandlecookies)Removed [-[NSURLRequest HTTPShouldUsePipelining]](https://developer.apple.com/documentation/foundation/nsurlrequest/1409170-httpshouldusepipelining)Removed [-[NSURLRequest URL]](https://developer.apple.com/documentation/foundation/nsurlrequest/1408996-url)Removed [-[NSURLRequest allHTTPHeaderFields]](https://developer.apple.com/documentation/foundation/nsurlrequest/1418477-allhttpheaderfields)Removed [-[NSURLRequest allowsCellularAccess]](https://developer.apple.com/documentation/foundation/nsurlrequest/1412032-allowscellularaccess)Removed [-[NSURLRequest cachePolicy]](https://developer.apple.com/documentation/foundation/nsurlrequest/1407944-cachepolicy)Removed [-[NSURLRequest mainDocumentURL]](https://developer.apple.com/documentation/foundation/nsurlrequest/1414134-maindocumenturl)Removed [-[NSURLRequest networkServiceType]](https://developer.apple.com/documentation/foundation/nsurlrequest/1418333-networkservicetype)Removed [-[NSURLRequest timeoutInterval]](https://developer.apple.com/documentation/foundation/nsurlrequest/1418229-timeoutinterval)Added [NSMutableURLRequest.HTTPBody](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1409064-httpbody)Added [NSMutableURLRequest.HTTPBodyStream](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1409529-httpbodystream)Added [NSMutableURLRequest.HTTPMethod](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1413047-httpmethod)Added [NSMutableURLRequest.HTTPShouldHandleCookies](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1415485-httpshouldhandlecookies)Added [NSMutableURLRequest.HTTPShouldUsePipelining](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1412705-httpshouldusepipelining)Added [NSMutableURLRequest.URL](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1410342-url)Added [NSMutableURLRequest.allHTTPHeaderFields](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414617-allhttpheaderfields)Added [NSMutableURLRequest.allowsCellularAccess](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1416749-allowscellularaccess)Added [NSMutableURLRequest.cachePolicy](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414716-cachepolicy)Added [NSMutableURLRequest.mainDocumentURL](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1415630-maindocumenturl)Added [NSMutableURLRequest.networkServiceType](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1412378-networkservicetype)Added [NSMutableURLRequest.timeoutInterval](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414063-timeoutinterval)Added [NSURLRequest.HTTPBody](https://developer.apple.com/documentation/foundation/nsurlrequest/1411317-httpbody)Added [NSURLRequest.HTTPBodyStream](https://developer.apple.com/documentation/foundation/nsurlrequest/1407341-httpbodystream)Added [NSURLRequest.HTTPMethod](https://developer.apple.com/documentation/foundation/nsurlrequest/1413030-httpmethod)Added [NSURLRequest.HTTPShouldHandleCookies](https://developer.apple.com/documentation/foundation/nsurlrequest/1418369-httpshouldhandlecookies)Added [NSURLRequest.HTTPShouldUsePipelining](https://developer.apple.com/documentation/foundation/nsurlrequest/1409170-httpshouldusepipelining)Added [NSURLRequest.URL](https://developer.apple.com/documentation/foundation/nsurlrequest/1408996-url)Added [NSURLRequest.allHTTPHeaderFields](https://developer.apple.com/documentation/foundation/nsurlrequest/1418477-allhttpheaderfields)Added [NSURLRequest.allowsCellularAccess](https://developer.apple.com/documentation/foundation/nsurlrequest/1412032-allowscellularaccess)Added [NSURLRequest.cachePolicy](https://developer.apple.com/documentation/foundation/nsurlrequest/1407944-cachepolicy)Added [NSURLRequest.mainDocumentURL](https://developer.apple.com/documentation/foundation/nsurlrequest/1414134-maindocumenturl)Added [NSURLRequest.networkServiceType](https://developer.apple.com/documentation/foundation/nsurlrequest/1418333-networkservicetype)Added [NSURLRequest.timeoutInterval](https://developer.apple.com/documentation/foundation/nsurlrequest/1418229-timeoutinterval)Modified [-[NSURLRequest initWithURL:]](https://developer.apple.com/documentation/foundation/nsurlrequest/1410303-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)URL ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)URL ``` |

Modified [-[NSURLRequest initWithURL:cachePolicy:timeoutInterval:]](https://developer.apple.com/documentation/foundation/nsurlrequest/1416292-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)URL cachePolicy:(NSURLRequestCachePolicy)cachePolicy timeoutInterval:(NSTimeInterval)timeoutInterval ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)URL cachePolicy:(NSURLRequestCachePolicy)cachePolicy timeoutInterval:(NSTimeInterval)timeoutInterval ``` |

Modified [+[NSURLRequest requestWithURL:]](https://developer.apple.com/documentation/foundation/nsurlrequest/1528603-requestwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)requestWithURL:(NSURL *)URL ``` |
| To | ``` + (instancetype)requestWithURL:(NSURL *)URL ``` |

Modified [+[NSURLRequest requestWithURL:cachePolicy:timeoutInterval:]](https://developer.apple.com/documentation/foundation/nsurlrequest/1528579-requestwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)requestWithURL:(NSURL *)URL cachePolicy:(NSURLRequestCachePolicy)cachePolicy timeoutInterval:(NSTimeInterval)timeoutInterval ``` |
| To | ``` + (instancetype)requestWithURL:(NSURL *)URL cachePolicy:(NSURLRequestCachePolicy)cachePolicy timeoutInterval:(NSTimeInterval)timeoutInterval ``` |

NSURLResponse.hRemoved [-[NSHTTPURLResponse allHeaderFields]](https://developer.apple.com/documentation/foundation/nshttpurlresponse/1417930-allheaderfields)Removed [-[NSHTTPURLResponse statusCode]](https://developer.apple.com/documentation/foundation/httpurlresponse/1409395-statuscode)Removed [-[NSURLResponse MIMEType]](https://developer.apple.com/documentation/foundation/nsurlresponse/1411613-mimetype)Removed [-[NSURLResponse URL]](https://developer.apple.com/documentation/foundation/nsurlresponse/1414219-url)Removed [-[NSURLResponse expectedContentLength]](https://developer.apple.com/documentation/foundation/nsurlresponse/1413507-expectedcontentlength)Removed [-[NSURLResponse suggestedFilename]](https://developer.apple.com/documentation/foundation/nsurlresponse/1415924-suggestedfilename)Removed [-[NSURLResponse textEncodingName]](https://developer.apple.com/documentation/foundation/nsurlresponse/1408005-textencodingname)Added [NSHTTPURLResponse.allHeaderFields](https://developer.apple.com/documentation/foundation/httpurlresponse/1417930-allheaderfields)Added [NSHTTPURLResponse.statusCode](https://developer.apple.com/documentation/foundation/httpurlresponse/1409395-statuscode)Added [NSURLResponse.MIMEType](https://developer.apple.com/documentation/foundation/nsurlresponse/1411613-mimetype)Added [NSURLResponse.URL](https://developer.apple.com/documentation/foundation/nsurlresponse/1414219-url)Added [NSURLResponse.expectedContentLength](https://developer.apple.com/documentation/foundation/nsurlresponse/1413507-expectedcontentlength)Added [NSURLResponse.suggestedFilename](https://developer.apple.com/documentation/foundation/nsurlresponse/1415924-suggestedfilename)Added [NSURLResponse.textEncodingName](https://developer.apple.com/documentation/foundation/urlresponse/1408005-textencodingname)Modified [-[NSHTTPURLResponse initWithURL:statusCode:HTTPVersion:headerFields:]](https://developer.apple.com/documentation/foundation/nshttpurlresponse/1415870-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url statusCode:(NSInteger)statusCode HTTPVersion:(NSString *)HTTPVersion headerFields:(NSDictionary *)headerFields ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)url statusCode:(NSInteger)statusCode HTTPVersion:(NSString *)HTTPVersion headerFields:(NSDictionary *)headerFields ``` |

Modified [-[NSURLResponse initWithURL:MIMEType:expectedContentLength:textEncodingName:]](https://developer.apple.com/documentation/foundation/nsurlresponse/1413566-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)URL MIMEType:(NSString *)MIMEType expectedContentLength:(NSInteger)length textEncodingName:(NSString *)name ``` |
| To | ``` - (instancetype)initWithURL:(NSURL *)URL MIMEType:(NSString *)MIMEType expectedContentLength:(NSInteger)length textEncodingName:(NSString *)name ``` |

NSURLSession.hAdded [+[NSURLSessionConfiguration backgroundSessionConfigurationWithIdentifier:]](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1407496-backgroundsessionconfigurationwi)Added [NSURLSessionConfiguration.discretionary](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411552-isdiscretionary)Added [NSURLSessionConfiguration.sharedContainerIdentifier](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1409450-sharedcontaineridentifier)Added [NSURLSessionTask.priority](https://developer.apple.com/documentation/foundation/urlsessiontask/1410569-priority)Added #def NSURLSESSION_AVAILABLEAdded NSURLSessionConfiguration(NSURLSessionDeprecated)Added [NSURLSessionTaskPriorityDefault](https://developer.apple.com/documentation/foundation/urlsessiontask/1411624-defaultpriority)Added [NSURLSessionTaskPriorityHigh](https://developer.apple.com/documentation/foundation/urlsessiontask/1411513-highpriority)Added [NSURLSessionTaskPriorityLow](https://developer.apple.com/documentation/foundation/nsurlsessiontaskprioritylow)Modified [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSession.configuration](https://developer.apple.com/documentation/foundation/nsurlsession/1411477-configuration)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified -[NSURLSession dataTaskWithHTTPGetRequest:]

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified -[NSURLSession dataTaskWithHTTPGetRequest:completionHandler:]

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession dataTaskWithRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410592-datataskwithrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession dataTaskWithRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1407613-datataskwithrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession dataTaskWithURL:]](https://developer.apple.com/documentation/foundation/urlsession/1411554-datatask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession dataTaskWithURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410330-datataskwithurl)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSession.delegate](https://developer.apple.com/documentation/foundation/nsurlsession/1411530-delegate)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSession.delegateQueue](https://developer.apple.com/documentation/foundation/nsurlsession/1411571-delegatequeue)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession downloadTaskWithRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411481-downloadtaskwithrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession downloadTaskWithRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411511-downloadtaskwithrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession downloadTaskWithResumeData:]](https://developer.apple.com/documentation/foundation/urlsession/1409226-downloadtask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession downloadTaskWithResumeData:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411598-downloadtaskwithresumedata)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession downloadTaskWithURL:]](https://developer.apple.com/documentation/foundation/urlsession/1411482-downloadtask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession downloadTaskWithURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411608-downloadtaskwithurl)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession finishTasksAndInvalidate]](https://developer.apple.com/documentation/foundation/urlsession/1407428-finishtasksandinvalidate)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession flushWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411622-flush)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession getTasksWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411578-gettaskswithcompletionhandler)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession invalidateAndCancel]](https://developer.apple.com/documentation/foundation/urlsession/1411538-invalidateandcancel)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession resetWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411479-reset)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSession.sessionDescription](https://developer.apple.com/documentation/foundation/urlsession/1408277-sessiondescription)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [+[NSURLSession sessionWithConfiguration:]](https://developer.apple.com/documentation/foundation/urlsession/1411474-init)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [+[NSURLSession sessionWithConfiguration:delegate:delegateQueue:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411597-sessionwithconfiguration)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [+[NSURLSession sharedSession]](https://developer.apple.com/documentation/foundation/urlsession/1409000-shared)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession uploadTaskWithRequest:fromData:]](https://developer.apple.com/documentation/foundation/nsurlsession/1409763-uploadtaskwithrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession uploadTaskWithRequest:fromData:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsession/1411518-uploadtask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession uploadTaskWithRequest:fromFile:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411550-uploadtaskwithrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession uploadTaskWithRequest:fromFile:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411638-uploadtaskwithrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSession uploadTaskWithStreamedRequest:]](https://developer.apple.com/documentation/foundation/nsurlsession/1410934-uploadtaskwithstreamedrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.HTTPAdditionalHeaders](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411532-httpadditionalheaders)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.HTTPCookieAcceptPolicy](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1408933-httpcookieacceptpolicy)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.HTTPCookieStorage](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411599-httpcookiestorage)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.HTTPMaximumConnectionsPerHost](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1407597-httpmaximumconnectionsperhost)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.HTTPShouldSetCookies](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411589-httpshouldsetcookies)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.HTTPShouldUsePipelining](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411657-httpshouldusepipelining)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.TLSMaximumSupportedProtocol](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1409076-tlsmaximumsupportedprotocol)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.TLSMinimumSupportedProtocol](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411526-tlsminimumsupportedprotocol)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.URLCache](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410148-urlcache)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.URLCredentialStorage](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410947-urlcredentialstorage)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.allowsCellularAccess](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1409406-allowscellularaccess)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [+[NSURLSessionConfiguration backgroundSessionConfiguration:]](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411521-backgroundsessionconfiguration)

|  | Deprecation | Architectures |
| --- | --- | --- |
| From | -- | x86_64 |
| To | OS X 10.10 | i386,x86_64 |

Modified [NSURLSessionConfiguration.connectionProxyDictionary](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411499-connectionproxydictionary)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [+[NSURLSessionConfiguration defaultSessionConfiguration]](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411560-defaultsessionconfiguration)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [+[NSURLSessionConfiguration ephemeralSessionConfiguration]](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410529-ephemeral)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.identifier](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408987-identifier)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.networkServiceType](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411606-networkservicetype)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.protocolClasses](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411050-protocolclasses)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.requestCachePolicy](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411655-requestcachepolicy)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.timeoutIntervalForRequest](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1408259-timeoutintervalforrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionConfiguration.timeoutIntervalForResource](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408153-timeoutintervalforresource)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionDataDelegate](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionDataDelegate URLSession:dataTask:didBecomeDownloadTask:]](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1409936-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionDataDelegate URLSession:dataTask:didReceiveData:]](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411528-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionDataDelegate URLSession:dataTask:didReceiveResponse:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1410027-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionDataDelegate URLSession:dataTask:willCacheResponse:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1411612-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [NSURLSessionDataTask](https://developer.apple.com/documentation/foundation/urlsessiondatatask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionDelegate URLSession:didBecomeInvalidWithError:]](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1407776-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionDelegate URLSession:didReceiveChallenge:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1409308-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [NSURLSessionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didFinishDownloadingToURL:]](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/1411575-urlsession)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/1408142-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionDownloadDelegate URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:]](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1409408-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionDownloadTask cancelByProducingResumeData:]](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask/1411634-cancelbyproducingresumedata)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionTask cancel]](https://developer.apple.com/documentation/foundation/urlsessiontask/1411591-cancel)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.countOfBytesExpectedToReceive](https://developer.apple.com/documentation/foundation/urlsessiontask/1410663-countofbytesexpectedtoreceive)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.countOfBytesExpectedToSend](https://developer.apple.com/documentation/foundation/urlsessiontask/1411534-countofbytesexpectedtosend)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.countOfBytesReceived](https://developer.apple.com/documentation/foundation/urlsessiontask/1411581-countofbytesreceived)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.countOfBytesSent](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1410444-countofbytessent)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.currentRequest](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411649-currentrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.error](https://developer.apple.com/documentation/foundation/urlsessiontask/1408145-error)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.originalRequest](https://developer.apple.com/documentation/foundation/urlsessiontask/1411572-originalrequest)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.response](https://developer.apple.com/documentation/foundation/urlsessiontask/1410586-response)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionTask resume]](https://developer.apple.com/documentation/foundation/urlsessiontask/1411121-resume)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.state](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1409888-state)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionTask suspend]](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411565-suspend)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.taskDescription](https://developer.apple.com/documentation/foundation/urlsessiontask/1409798-taskdescription)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTask.taskIdentifier](https://developer.apple.com/documentation/foundation/urlsessiontask/1411231-taskidentifier)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [-[NSURLSessionTaskDelegate URLSession:task:didCompleteWithError:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411610-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionTaskDelegate URLSession:task:didReceiveChallenge:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411595-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionTaskDelegate URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:]](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1408299-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionTaskDelegate URLSession:task:needNewBodyStream:]](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1410001-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [-[NSURLSessionTaskDelegate URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1411626-urlsession)

|  | Architectures | Optional |
| --- | --- | --- |
| From | x86_64 | -- |
| To | i386,x86_64 | yes |

Modified [NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/nsurlsessionuploadtask)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified NSURLSession(NSURLSessionAsynchronousConvenience)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified NSURLSession(NSURLSessionDeprecated)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionAuthChallengeCancelAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengecancelauthenticationchallenge)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionAuthChallengeDisposition](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionAuthChallengePerformDefaultHandling](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/performdefaulthandling)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionAuthChallengeRejectProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengerejectprotectionspace)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionAuthChallengeUseCredential](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/usecredential)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionDownloadTaskResumeData](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtaskresumedata)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionResponseAllow](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponseallow)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionResponseBecomeDownload](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsebecomedownload)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionResponseCancel](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsecancel)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionResponseDisposition](https://developer.apple.com/documentation/foundation/urlsession/responsedisposition)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTaskState](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTaskStateCanceling](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate/nsurlsessiontaskstatecanceling)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTaskStateCompleted](https://developer.apple.com/documentation/foundation/urlsessiontask/state/completed)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTaskStateRunning](https://developer.apple.com/documentation/foundation/urlsessiontask/state/running)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTaskStateSuspended](https://developer.apple.com/documentation/foundation/nsurlsessiontaskstate/nsurlsessiontaskstatesuspended)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [NSURLSessionTransferSizeUnknown](https://developer.apple.com/documentation/foundation/nsurlsessiontransfersizeunknown)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

NSUUID.hRemoved [-[NSUUID UUIDString]](https://developer.apple.com/documentation/foundation/nsuuid/1416585-uuidstring)Added [NSUUID.UUIDString](https://developer.apple.com/documentation/foundation/nsuuid/1416585-uuidstring)Modified [+[NSUUID UUID]](https://developer.apple.com/documentation/foundation/nsuuid/1574571-uuid)

|  | Declaration |
| --- | --- |
| From | ``` + (id)UUID ``` |
| To | ``` + (instancetype)UUID ``` |

Modified [-[NSUUID init]](https://developer.apple.com/documentation/foundation/nsuuid/1415797-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)init ``` | -- |
| To | ``` - (instancetype)init ``` | yes |

Modified [-[NSUUID initWithUUIDBytes:]](https://developer.apple.com/documentation/foundation/nsuuid/1417039-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithUUIDBytes:(const uuid_t)bytes ``` |
| To | ``` - (instancetype)initWithUUIDBytes:(const uuid_t)bytes ``` |

Modified [-[NSUUID initWithUUIDString:]](https://developer.apple.com/documentation/foundation/nsuuid/1411662-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithUUIDString:(NSString *)string ``` |
| To | ``` - (instancetype)initWithUUIDString:(NSString *)string ``` |

NSUbiquitousKeyValueStore.hRemoved [-[NSUbiquitousKeyValueStore dictionaryRepresentation]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1411129-dictionaryrepresentation)Added [NSUbiquitousKeyValueStore.dictionaryRepresentation](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1411129-dictionaryrepresentation)NSUndoManager.hRemoved [-[NSUndoManager canRedo]](https://developer.apple.com/documentation/foundation/nsundomanager/1415212-canredo)Removed [-[NSUndoManager canUndo]](https://developer.apple.com/documentation/foundation/nsundomanager/1412394-canundo)Removed [-[NSUndoManager groupingLevel]](https://developer.apple.com/documentation/foundation/undomanager/1409006-groupinglevel)Removed [-[NSUndoManager groupsByEvent]](https://developer.apple.com/documentation/foundation/nsundomanager/1417407-groupsbyevent)Removed [-[NSUndoManager isRedoing]](https://developer.apple.com/documentation/foundation/nsundomanager/1411654-redoing)Removed [-[NSUndoManager isUndoRegistrationEnabled]](https://developer.apple.com/documentation/foundation/undomanager/1415464-isundoregistrationenabled)Removed [-[NSUndoManager isUndoing]](https://developer.apple.com/documentation/foundation/undomanager/1407345-isundoing)Removed [-[NSUndoManager levelsOfUndo]](https://developer.apple.com/documentation/foundation/undomanager/1409753-levelsofundo)Removed [-[NSUndoManager redoActionIsDiscardable]](https://developer.apple.com/documentation/foundation/nsundomanager/1413488-redoactionisdiscardable)Removed [-[NSUndoManager redoActionName]](https://developer.apple.com/documentation/foundation/undomanager/1417487-redoactionname)Removed [-[NSUndoManager redoMenuItemTitle]](https://developer.apple.com/documentation/foundation/nsundomanager/1409938-redomenuitemtitle)Removed [-[NSUndoManager runLoopModes]](https://developer.apple.com/documentation/foundation/undomanager/1409504-runloopmodes)Removed [-[NSUndoManager setGroupsByEvent:]](https://developer.apple.com/documentation/foundation/undomanager/1417407-groupsbyevent)Removed [-[NSUndoManager setLevelsOfUndo:]](https://developer.apple.com/documentation/foundation/nsundomanager/1409753-levelsofundo)Removed [-[NSUndoManager setRunLoopModes:]](https://developer.apple.com/documentation/foundation/undomanager/1409504-runloopmodes)Removed [-[NSUndoManager undoActionIsDiscardable]](https://developer.apple.com/documentation/foundation/undomanager/1415261-undoactionisdiscardable)Removed [-[NSUndoManager undoActionName]](https://developer.apple.com/documentation/foundation/nsundomanager/1415127-undoactionname)Removed [-[NSUndoManager undoMenuItemTitle]](https://developer.apple.com/documentation/foundation/nsundomanager/1412953-undomenuitemtitle)Added [NSUndoManager.canRedo](https://developer.apple.com/documentation/foundation/undomanager/1415212-canredo)Added [NSUndoManager.canUndo](https://developer.apple.com/documentation/foundation/nsundomanager/1412394-canundo)Added [NSUndoManager.groupingLevel](https://developer.apple.com/documentation/foundation/nsundomanager/1409006-groupinglevel)Added [NSUndoManager.groupsByEvent](https://developer.apple.com/documentation/foundation/nsundomanager/1417407-groupsbyevent)Added [NSUndoManager.levelsOfUndo](https://developer.apple.com/documentation/foundation/nsundomanager/1409753-levelsofundo)Added [NSUndoManager.redoActionIsDiscardable](https://developer.apple.com/documentation/foundation/nsundomanager/1413488-redoactionisdiscardable)Added [NSUndoManager.redoActionName](https://developer.apple.com/documentation/foundation/nsundomanager/1417487-redoactionname)Added [NSUndoManager.redoMenuItemTitle](https://developer.apple.com/documentation/foundation/nsundomanager/1409938-redomenuitemtitle)Added [NSUndoManager.redoing](https://developer.apple.com/documentation/foundation/nsundomanager/1411654-redoing)Added [NSUndoManager.runLoopModes](https://developer.apple.com/documentation/foundation/nsundomanager/1409504-runloopmodes)Added [NSUndoManager.undoActionIsDiscardable](https://developer.apple.com/documentation/foundation/nsundomanager/1415261-undoactionisdiscardable)Added [NSUndoManager.undoActionName](https://developer.apple.com/documentation/foundation/undomanager/1415127-undoactionname)Added [NSUndoManager.undoMenuItemTitle](https://developer.apple.com/documentation/foundation/undomanager/1412953-undomenuitemtitle)Added [NSUndoManager.undoRegistrationEnabled](https://developer.apple.com/documentation/foundation/undomanager/1415464-isundoregistrationenabled)Added [NSUndoManager.undoing](https://developer.apple.com/documentation/foundation/nsundomanager/1407345-undoing)NSUserActivity.h (Added)Added [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)Added [NSUserActivity.activityType](https://developer.apple.com/documentation/foundation/nsuseractivity/1409611-activitytype)Added [-[NSUserActivity addUserInfoEntriesFromDictionary:]](https://developer.apple.com/documentation/foundation/nsuseractivity/1410066-adduserinfoentriesfromdictionary)Added [-[NSUserActivity becomeCurrent]](https://developer.apple.com/documentation/foundation/nsuseractivity/1413665-becomecurrent)Added [NSUserActivity.delegate](https://developer.apple.com/documentation/foundation/nsuseractivity/1412329-delegate)Added [-[NSUserActivity getContinuationStreamsWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsuseractivity/1409931-getcontinuationstreams)Added [-[NSUserActivity init]](https://developer.apple.com/documentation/foundation/nsuseractivity/1409240-init)Added [-[NSUserActivity initWithActivityType:]](https://developer.apple.com/documentation/foundation/nsuseractivity/1410714-init)Added [-[NSUserActivity invalidate]](https://developer.apple.com/documentation/foundation/nsuseractivity/1416401-invalidate)Added [NSUserActivity.needsSave](https://developer.apple.com/documentation/foundation/nsuseractivity/1408791-needssave)Added [NSUserActivity.supportsContinuationStreams](https://developer.apple.com/documentation/foundation/nsuseractivity/1409195-supportscontinuationstreams)Added [NSUserActivity.title](https://developer.apple.com/documentation/foundation/nsuseractivity/1413375-title)Added [NSUserActivity.userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo)Added [NSUserActivity.webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl)Added [NSUserActivityDelegate](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate)Added [-[NSUserActivityDelegate userActivity:didReceiveInputStream:outputStream:]](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/1407386-useractivity)Added [-[NSUserActivityDelegate userActivityWasContinued:]](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/1413276-useractivitywascontinued)Added [-[NSUserActivityDelegate userActivityWillSave:]](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/1414848-useractivitywillsave)Added [NSUserActivityTypeBrowsingWeb](https://developer.apple.com/documentation/foundation/nsuseractivitytypebrowsingweb)NSUserDefaults.hRemoved [-[NSUserDefaults volatileDomainNames]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/volatileDomainNames)Added [NSUserDefaults.volatileDomainNames](https://developer.apple.com/documentation/foundation/nsuserdefaults/1414231-volatiledomainnames)Modified [-[NSUserDefaults init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[NSUserDefaults initWithSuiteName:]](https://developer.apple.com/documentation/foundation/userdefaults/1409957-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithSuiteName:(NSString *)suitename ``` | -- |
| To | ``` - (instancetype)initWithSuiteName:(NSString *)suitename ``` | yes |

NSUserNotification.hAdded [NSUserNotification.additionalActions](https://developer.apple.com/documentation/foundation/nsusernotification/1407829-additionalactions)Added [NSUserNotification.additionalActivationAction](https://developer.apple.com/documentation/foundation/nsusernotification/1413264-additionalactivationaction)Added [-[NSUserNotification init]](https://developer.apple.com/documentation/foundation/nsusernotification/1410841-init)Added [NSUserNotificationAction](https://developer.apple.com/documentation/foundation/nsusernotificationaction)Added [+[NSUserNotificationAction actionWithIdentifier:title:]](https://developer.apple.com/documentation/foundation/nsusernotificationaction/1415698-init)Added [NSUserNotificationAction.identifier](https://developer.apple.com/documentation/foundation/nsusernotificationaction/1414798-identifier)Added [NSUserNotificationAction.title](https://developer.apple.com/documentation/foundation/nsusernotificationaction/1410336-title)Added [NSUserNotificationActivationTypeAdditionalActionClicked](https://developer.apple.com/documentation/foundation/nsusernotificationactivationtype/nsusernotificationactivationtypeadditionalactionclicked)Modified [NSUserNotification.actualDeliveryDate](https://developer.apple.com/documentation/foundation/nsusernotification/1416009-actualdeliverydate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *actualDeliveryDate ``` |
| To | ``` @property(readonly, copy) NSDate *actualDeliveryDate ``` |

Modified [NSUserNotification.response](https://developer.apple.com/documentation/foundation/nsusernotification/1416115-response)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSAttributedString *response ``` |
| To | ``` @property(readonly, copy) NSAttributedString *response ``` |

Modified [NSUserNotificationCenter.deliveredNotifications](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1407791-deliverednotifications)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *deliveredNotifications ``` |
| To | ``` @property(readonly, copy) NSArray *deliveredNotifications ``` |

Modified [-[NSUserNotificationCenterDelegate userNotificationCenter:didActivateNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/1418378-usernotificationcenter)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSUserNotificationCenterDelegate userNotificationCenter:didDeliverNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/1410579-usernotificationcenter)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSUserNotificationCenterDelegate userNotificationCenter:shouldPresentNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/1409032-usernotificationcenter)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSUserScriptTask.hRemoved [-[NSUserScriptTask scriptURL]](https://developer.apple.com/documentation/foundation/nsuserscripttask/1408618-scripturl)Added [NSUserScriptTask.scriptURL](https://developer.apple.com/documentation/foundation/nsuserscripttask/1408618-scripturl)Modified [-[NSUserScriptTask initWithURL:error:]](https://developer.apple.com/documentation/foundation/nsuserscripttask/1409998-initwithurl)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url error:(NSError **)error ``` | -- |
| To | ``` - (instancetype)initWithURL:(NSURL *)url error:(NSError **)error ``` | yes |

NSValue.hRemoved [-[NSNumber boolValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/boolValue)Removed [-[NSNumber charValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/charValue)Removed [-[NSNumber doubleValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/doubleValue)Removed [-[NSNumber floatValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/floatValue)Removed [-[NSNumber intValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/intValue)Removed [-[NSNumber integerValue]](https://developer.apple.com/documentation/foundation/nsnumber/1412554-integervalue)Removed [-[NSNumber longLongValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/longLongValue)Removed [-[NSNumber longValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/longValue)Removed [-[NSNumber shortValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/shortValue)Removed [-[NSNumber stringValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/stringValue)Removed [-[NSNumber unsignedCharValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/unsignedCharValue)Removed [-[NSNumber unsignedIntValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/unsignedIntValue)Removed [-[NSNumber unsignedIntegerValue]](https://developer.apple.com/documentation/foundation/nsnumber/1413324-uintvalue)Removed [-[NSNumber unsignedLongLongValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/unsignedLongLongValue)Removed [-[NSNumber unsignedLongValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/unsignedLongValue)Removed [-[NSNumber unsignedShortValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/unsignedShortValue)Removed [-[NSValue nonretainedObjectValue]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/nonretainedObjectValue)Removed [-[NSValue objCType]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/objCType)Added [NSNumber.boolValue](https://developer.apple.com/documentation/foundation/nsnumber/1410865-boolvalue)Added [NSNumber.charValue](https://developer.apple.com/documentation/foundation/nsnumber/1407838-charvalue)Added [NSNumber.doubleValue](https://developer.apple.com/documentation/foundation/nsnumber/1414104-doublevalue)Added [NSNumber.floatValue](https://developer.apple.com/documentation/foundation/nsnumber/1418317-floatvalue)Added [-[NSNumber initWithCoder:]](https://developer.apple.com/documentation/foundation/nsnumber/1411476-initwithcoder)Added [NSNumber.intValue](https://developer.apple.com/documentation/foundation/nsnumber/1407153-int32value)Added [NSNumber.integerValue](https://developer.apple.com/documentation/foundation/nsnumber/1412554-integervalue)Added [NSNumber.longLongValue](https://developer.apple.com/documentation/foundation/nsnumber/1416870-longlongvalue)Added [NSNumber.longValue](https://developer.apple.com/documentation/foundation/nsnumber/1412566-longvalue)Added [NSNumber.shortValue](https://developer.apple.com/documentation/foundation/nsnumber/1407601-shortvalue)Added [NSNumber.stringValue](https://developer.apple.com/documentation/foundation/nsnumber/1415802-stringvalue)Added [NSNumber.unsignedCharValue](https://developer.apple.com/documentation/foundation/nsnumber/1409016-uint8value)Added [NSNumber.unsignedIntValue](https://developer.apple.com/documentation/foundation/nsnumber/1417875-unsignedintvalue)Added [NSNumber.unsignedIntegerValue](https://developer.apple.com/documentation/foundation/nsnumber/1413324-unsignedintegervalue)Added [NSNumber.unsignedLongLongValue](https://developer.apple.com/documentation/foundation/nsnumber/1414524-uint64value)Added [NSNumber.unsignedLongValue](https://developer.apple.com/documentation/foundation/nsnumber/1415252-unsignedlongvalue)Added [NSNumber.unsignedShortValue](https://developer.apple.com/documentation/foundation/nsnumber/1410604-unsignedshortvalue)Added [-[NSValue initWithCoder:]](https://developer.apple.com/documentation/foundation/nsvalue/1417896-init)Added [NSValue.nonretainedObjectValue](https://developer.apple.com/documentation/foundation/nsvalue/1412287-nonretainedobjectvalue)Added [NSValue.objCType](https://developer.apple.com/documentation/foundation/nsvalue/1412365-objctype)Modified [-[NSNumber initWithBool:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithBool:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithBool:(BOOL)value ``` | -- |
| To | ``` - (NSNumber *)initWithBool:(BOOL)value ``` | yes |

Modified [-[NSNumber initWithChar:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithChar:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithChar:(char)value ``` | -- |
| To | ``` - (NSNumber *)initWithChar:(char)value ``` | yes |

Modified [-[NSNumber initWithDouble:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithDouble:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithDouble:(double)value ``` | -- |
| To | ``` - (NSNumber *)initWithDouble:(double)value ``` | yes |

Modified [-[NSNumber initWithFloat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithFloat:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithFloat:(float)value ``` | -- |
| To | ``` - (NSNumber *)initWithFloat:(float)value ``` | yes |

Modified [-[NSNumber initWithInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithInt:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithInt:(int)value ``` | -- |
| To | ``` - (NSNumber *)initWithInt:(int)value ``` | yes |

Modified [-[NSNumber initWithInteger:]](https://developer.apple.com/documentation/foundation/nsnumber/1409397-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithInteger:(NSInteger)value ``` | -- |
| To | ``` - (NSNumber *)initWithInteger:(NSInteger)value ``` | yes |

Modified [-[NSNumber initWithLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithLong:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithLong:(long)value ``` | -- |
| To | ``` - (NSNumber *)initWithLong:(long)value ``` | yes |

Modified [-[NSNumber initWithLongLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithLongLong:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithLongLong:(long long)value ``` | -- |
| To | ``` - (NSNumber *)initWithLongLong:(long long)value ``` | yes |

Modified [-[NSNumber initWithShort:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithShort:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithShort:(short)value ``` | -- |
| To | ``` - (NSNumber *)initWithShort:(short)value ``` | yes |

Modified [-[NSNumber initWithUnsignedChar:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedChar:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithUnsignedChar:(unsigned char)value ``` | -- |
| To | ``` - (NSNumber *)initWithUnsignedChar:(unsigned char)value ``` | yes |

Modified [-[NSNumber initWithUnsignedInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedInt:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithUnsignedInt:(unsigned int)value ``` | -- |
| To | ``` - (NSNumber *)initWithUnsignedInt:(unsigned int)value ``` | yes |

Modified [-[NSNumber initWithUnsignedInteger:]](https://developer.apple.com/documentation/foundation/nsnumber/1412531-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithUnsignedInteger:(NSUInteger)value ``` | -- |
| To | ``` - (NSNumber *)initWithUnsignedInteger:(NSUInteger)value ``` | yes |

Modified [-[NSNumber initWithUnsignedLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedLong:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithUnsignedLong:(unsigned long)value ``` | -- |
| To | ``` - (NSNumber *)initWithUnsignedLong:(unsigned long)value ``` | yes |

Modified [-[NSNumber initWithUnsignedLongLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedLongLong:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithUnsignedLongLong:(unsigned long long)value ``` | -- |
| To | ``` - (NSNumber *)initWithUnsignedLongLong:(unsigned long long)value ``` | yes |

Modified [-[NSNumber initWithUnsignedShort:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedShort:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithUnsignedShort:(unsigned short)value ``` | -- |
| To | ``` - (NSNumber *)initWithUnsignedShort:(unsigned short)value ``` | yes |

Modified [-[NSValue initWithBytes:objCType:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/initWithBytes:objCType:)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithBytes:(const void *)value objCType:(const char *)type ``` | -- |
| To | ``` - (instancetype)initWithBytes:(const void *)value objCType:(const char *)type ``` | yes |

NSXMLDTD.hRemoved [-[NSXMLDTD publicID]](https://developer.apple.com/documentation/foundation/nsxmldtd/1408524-publicid)Removed [-[NSXMLDTD setPublicID:]](https://developer.apple.com/documentation/foundation/xmldtd/1408524-publicid)Removed [-[NSXMLDTD setSystemID:]](https://developer.apple.com/documentation/foundation/xmldtd/1410949-systemid)Removed [-[NSXMLDTD systemID]](https://developer.apple.com/documentation/foundation/nsxmldtd/1410949-systemid)Added [-[NSXMLDTD init]](https://developer.apple.com/documentation/foundation/xmldtd/1417840-init)Added [NSXMLDTD.publicID](https://developer.apple.com/documentation/foundation/nsxmldtd/1408524-publicid)Added [NSXMLDTD.systemID](https://developer.apple.com/documentation/foundation/xmldtd/1410949-systemid)Modified [-[NSXMLDTD initWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/foundation/nsxmldtd/1410482-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url options:(NSUInteger)mask error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url options:(NSUInteger)mask error:(NSError **)error ``` |

Modified [-[NSXMLDTD initWithData:options:error:]](https://developer.apple.com/documentation/foundation/xmldtd/1412807-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSUInteger)mask error:(NSError **)error ``` | -- |
| To | ``` - (instancetype)initWithData:(NSData *)data options:(NSUInteger)mask error:(NSError **)error ``` | yes |

NSXMLDTDNode.hRemoved [-[NSXMLDTDNode DTDKind]](https://developer.apple.com/documentation/foundation/xmldtdnode/1408902-dtdkind)Removed [-[NSXMLDTDNode isExternal]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1806489-isexternal)Removed [-[NSXMLDTDNode notationName]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1407292-notationname)Removed [-[NSXMLDTDNode publicID]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1415631-publicid)Removed [-[NSXMLDTDNode setDTDKind:]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1806486-setdtdkind)Removed [-[NSXMLDTDNode setNotationName:]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1407292-notationname)Removed [-[NSXMLDTDNode setPublicID:]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1415631-publicid)Removed [-[NSXMLDTDNode setSystemID:]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1410930-systemid)Removed [-[NSXMLDTDNode systemID]](https://developer.apple.com/documentation/foundation/xmldtdnode/1410930-systemid)Added [NSXMLDTDNode.DTDKind](https://developer.apple.com/documentation/foundation/xmldtdnode/1408902-dtdkind)Added [NSXMLDTDNode.external](https://developer.apple.com/documentation/foundation/xmldtdnode/1409467-isexternal)Added [-[NSXMLDTDNode init]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1416018-init)Added [-[NSXMLDTDNode initWithKind:options:]](https://developer.apple.com/documentation/foundation/xmldtdnode/1408553-init)Added [NSXMLDTDNode.notationName](https://developer.apple.com/documentation/foundation/xmldtdnode/1407292-notationname)Added [NSXMLDTDNode.publicID](https://developer.apple.com/documentation/foundation/xmldtdnode/1415631-publicid)Added [NSXMLDTDNode.systemID](https://developer.apple.com/documentation/foundation/xmldtdnode/1410930-systemid)Modified [-[NSXMLDTDNode initWithXMLString:]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1409605-initwithxmlstring)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithXMLString:(NSString *)string ``` | -- |
| To | ``` - (instancetype)initWithXMLString:(NSString *)string ``` | yes |

NSXMLDocument.hRemoved [-[NSXMLDocument DTD]](https://developer.apple.com/documentation/foundation/xmldocument/1418474-dtd)Removed [-[NSXMLDocument MIMEType]](https://developer.apple.com/documentation/foundation/xmldocument/1408633-mimetype)Removed [-[NSXMLDocument XMLData]](https://developer.apple.com/documentation/foundation/nsxmldocument/1411660-xmldata)Removed [-[NSXMLDocument characterEncoding]](https://developer.apple.com/documentation/foundation/nsxmldocument/1410987-characterencoding)Removed [-[NSXMLDocument documentContentKind]](https://developer.apple.com/documentation/foundation/nsxmldocument/1407426-documentcontentkind)Removed [-[NSXMLDocument isStandalone]](https://developer.apple.com/documentation/foundation/nsxmldocument/1806533-isstandalone)Removed [-[NSXMLDocument setCharacterEncoding:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1410987-characterencoding)Removed [-[NSXMLDocument setDTD:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1806529-setdtd)Removed [-[NSXMLDocument setDocumentContentKind:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1407426-documentcontentkind)Removed [-[NSXMLDocument setMIMEType:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1806541-setmimetype)Removed [-[NSXMLDocument setStandalone:]](https://developer.apple.com/documentation/foundation/xmldocument/1413655-isstandalone)Removed [-[NSXMLDocument setVersion:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1409066-version)Removed [-[NSXMLDocument version]](https://developer.apple.com/documentation/foundation/xmldocument/1409066-version)Added [NSXMLDocument.DTD](https://developer.apple.com/documentation/foundation/nsxmldocument/1418474-dtd)Added [NSXMLDocument.MIMEType](https://developer.apple.com/documentation/foundation/xmldocument/1408633-mimetype)Added [NSXMLDocument.XMLData](https://developer.apple.com/documentation/foundation/nsxmldocument/1411660-xmldata)Added [NSXMLDocument.characterEncoding](https://developer.apple.com/documentation/foundation/nsxmldocument/1410987-characterencoding)Added [NSXMLDocument.documentContentKind](https://developer.apple.com/documentation/foundation/xmldocument/1407426-documentcontentkind)Added [-[NSXMLDocument init]](https://developer.apple.com/documentation/foundation/nsxmldocument/1415210-init)Added [NSXMLDocument.standalone](https://developer.apple.com/documentation/foundation/xmldocument/1413655-isstandalone)Added [NSXMLDocument.version](https://developer.apple.com/documentation/foundation/nsxmldocument/1409066-version)Modified [-[NSXMLDocument initWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1418467-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url options:(NSUInteger)mask error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url options:(NSUInteger)mask error:(NSError **)error ``` |

Modified [-[NSXMLDocument initWithData:options:error:]](https://developer.apple.com/documentation/foundation/xmldocument/1413086-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSUInteger)mask error:(NSError **)error ``` | -- |
| To | ``` - (instancetype)initWithData:(NSData *)data options:(NSUInteger)mask error:(NSError **)error ``` | yes |

Modified [-[NSXMLDocument initWithRootElement:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1409062-initwithrootelement)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithRootElement:(NSXMLElement *)element ``` | -- |
| To | ``` - (instancetype)initWithRootElement:(NSXMLElement *)element ``` | yes |

Modified [-[NSXMLDocument initWithXMLString:options:error:]](https://developer.apple.com/documentation/foundation/xmldocument/1416228-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithXMLString:(NSString *)string options:(NSUInteger)mask error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithXMLString:(NSString *)string options:(NSUInteger)mask error:(NSError **)error ``` |

Modified [-[NSXMLDocument setRootElement:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1415610-setrootelement)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setRootElement:(NSXMLNode *)root ``` |
| To | ``` - (void)setRootElement:(NSXMLElement *)root ``` |

NSXMLElement.hRemoved [-[NSXMLElement attributes]](https://developer.apple.com/documentation/foundation/xmlelement/1388321-attributes)Removed [-[NSXMLElement namespaces]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388342-namespaces)Removed [-[NSXMLElement setAttributes:]](https://developer.apple.com/documentation/foundation/xmlelement/1388321-attributes)Removed [-[NSXMLElement setNamespaces:]](https://developer.apple.com/documentation/foundation/xmlelement/1388342-namespaces)Added [NSXMLElement.attributes](https://developer.apple.com/documentation/foundation/nsxmlelement/1388321-attributes)Added [-[NSXMLElement initWithKind:options:]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388323-initwithkind)Added [NSXMLElement.namespaces](https://developer.apple.com/documentation/foundation/xmlelement/1388342-namespaces)Modified [-[NSXMLElement initWithName:]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388319-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(NSString *)name ``` |
| To | ``` - (instancetype)initWithName:(NSString *)name ``` |

Modified [-[NSXMLElement initWithName:URI:]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388348-initwithname)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithName:(NSString *)name URI:(NSString *)URI ``` | -- |
| To | ``` - (instancetype)initWithName:(NSString *)name URI:(NSString *)URI ``` | yes |

Modified [-[NSXMLElement initWithName:stringValue:]](https://developer.apple.com/documentation/foundation/xmlelement/1388356-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(NSString *)name stringValue:(NSString *)string ``` |
| To | ``` - (instancetype)initWithName:(NSString *)name stringValue:(NSString *)string ``` |

Modified [-[NSXMLElement initWithXMLString:error:]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388325-initwithxmlstring)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithXMLString:(NSString *)string error:(NSError **)error ``` | -- |
| To | ``` - (instancetype)initWithXMLString:(NSString *)string error:(NSError **)error ``` | yes |

NSXMLNode.hRemoved [-[NSXMLNode URI]](https://developer.apple.com/documentation/foundation/xmlnode/1409774-uri)Removed [-[NSXMLNode XMLString]](https://developer.apple.com/documentation/foundation/xmlnode/1409772-xmlstring)Removed [-[NSXMLNode XPath]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409826-xpath)Removed [-[NSXMLNode childCount]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409808-childcount)Removed [-[NSXMLNode children]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409828-children)Removed [-[NSXMLNode description]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409788-description)Removed [-[NSXMLNode index]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409743-index)Removed [-[NSXMLNode kind]](https://developer.apple.com/documentation/foundation/xmlnode/1408882-kind)Removed [-[NSXMLNode level]](https://developer.apple.com/documentation/foundation/nsxmlnode/1407508-level)Removed [-[NSXMLNode localName]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409734-localname)Removed [-[NSXMLNode name]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409770-name)Removed [-[NSXMLNode nextNode]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409800-nextnode)Removed [-[NSXMLNode nextSibling]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409750-nextsibling)Removed [-[NSXMLNode objectValue]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409756-objectvalue)Removed [-[NSXMLNode parent]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409740-parent)Removed [-[NSXMLNode prefix]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409797-prefix)Removed [-[NSXMLNode previousNode]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409736-previousnode)Removed [-[NSXMLNode previousSibling]](https://developer.apple.com/documentation/foundation/xmlnode/1409764-previoussibling)Removed [-[NSXMLNode rootDocument]](https://developer.apple.com/documentation/foundation/xmlnode/1409830-rootdocument)Removed [-[NSXMLNode setName:]](https://developer.apple.com/documentation/foundation/xmlnode/1409770-name)Removed [-[NSXMLNode setObjectValue:]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409756-objectvalue)Removed [-[NSXMLNode setStringValue:]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409818-stringvalue)Removed [-[NSXMLNode setURI:]](https://developer.apple.com/documentation/foundation/nsxmlnode/1806643-seturi)Removed [-[NSXMLNode stringValue]](https://developer.apple.com/documentation/foundation/xmlnode/1409818-stringvalue)Added [NSXMLNode.URI](https://developer.apple.com/documentation/foundation/nsxmlnode/1409774-uri)Added [NSXMLNode.XMLString](https://developer.apple.com/documentation/foundation/nsxmlnode/1409772-xmlstring)Added [NSXMLNode.XPath](https://developer.apple.com/documentation/foundation/xmlnode/1409826-xpath)Added [NSXMLNode.childCount](https://developer.apple.com/documentation/foundation/nsxmlnode/1409808-childcount)Added [NSXMLNode.children](https://developer.apple.com/documentation/foundation/xmlnode/1409828-children)Added [NSXMLNode.description](https://developer.apple.com/documentation/foundation/xmlnode/1409788-description)Added [NSXMLNode.index](https://developer.apple.com/documentation/foundation/xmlnode/1409743-index)Added [-[NSXMLNode init]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409780-init)Added [NSXMLNode.kind](https://developer.apple.com/documentation/foundation/nsxmlnode/1408882-kind)Added [NSXMLNode.level](https://developer.apple.com/documentation/foundation/nsxmlnode/1407508-level)Added [NSXMLNode.localName](https://developer.apple.com/documentation/foundation/xmlnode/1409734-localname)Added [NSXMLNode.name](https://developer.apple.com/documentation/foundation/nsxmlnode/1409770-name)Added [NSXMLNode.nextNode](https://developer.apple.com/documentation/foundation/nsxmlnode/1409800-nextnode)Added [NSXMLNode.nextSibling](https://developer.apple.com/documentation/foundation/xmlnode/1409750-nextsibling)Added [NSXMLNode.objectValue](https://developer.apple.com/documentation/foundation/xmlnode/1409756-objectvalue)Added [NSXMLNode.parent](https://developer.apple.com/documentation/foundation/xmlnode/1409740-parent)Added [NSXMLNode.prefix](https://developer.apple.com/documentation/foundation/nsxmlnode/1409797-prefix)Added [NSXMLNode.previousNode](https://developer.apple.com/documentation/foundation/nsxmlnode/1409736-previousnode)Added [NSXMLNode.previousSibling](https://developer.apple.com/documentation/foundation/xmlnode/1409764-previoussibling)Added [NSXMLNode.rootDocument](https://developer.apple.com/documentation/foundation/nsxmlnode/1409830-rootdocument)Added [NSXMLNode.stringValue](https://developer.apple.com/documentation/foundation/nsxmlnode/1409818-stringvalue)Modified [-[NSXMLNode initWithKind:]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409766-initwithkind)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithKind:(NSXMLNodeKind)kind ``` |
| To | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind ``` |

Modified [-[NSXMLNode initWithKind:options:]](https://developer.apple.com/documentation/foundation/xmlnode/1409747-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithKind:(NSXMLNodeKind)kind options:(NSUInteger)options ``` | -- |
| To | ``` - (instancetype)initWithKind:(NSXMLNodeKind)kind options:(NSUInteger)options ``` | yes |

NSXMLParser.hRemoved [-[NSXMLParser columnNumber]](https://developer.apple.com/documentation/foundation/xmlparser/1416983-columnnumber)Removed [-[NSXMLParser delegate]](https://developer.apple.com/documentation/foundation/nsxmlparser/1416209-delegate)Removed [-[NSXMLParser lineNumber]](https://developer.apple.com/documentation/foundation/nsxmlparser/1413404-linenumber)Removed [-[NSXMLParser parserError]](https://developer.apple.com/documentation/foundation/nsxmlparser/1417446-parsererror)Removed [-[NSXMLParser publicID]](https://developer.apple.com/documentation/foundation/nsxmlparser/1414516-publicid)Removed [-[NSXMLParser setDelegate:]](https://developer.apple.com/documentation/foundation/nsxmlparser/1416209-delegate)Removed [-[NSXMLParser setShouldProcessNamespaces:]](https://developer.apple.com/documentation/foundation/nsxmlparser/1418380-shouldprocessnamespaces)Removed [-[NSXMLParser setShouldReportNamespacePrefixes:]](https://developer.apple.com/documentation/foundation/xmlparser/1410809-shouldreportnamespaceprefixes)Removed [-[NSXMLParser setShouldResolveExternalEntities:]](https://developer.apple.com/documentation/foundation/xmlparser/1414143-shouldresolveexternalentities)Removed [-[NSXMLParser shouldProcessNamespaces]](https://developer.apple.com/documentation/foundation/nsxmlparser/1418380-shouldprocessnamespaces)Removed [-[NSXMLParser shouldReportNamespacePrefixes]](https://developer.apple.com/documentation/foundation/xmlparser/1410809-shouldreportnamespaceprefixes)Removed [-[NSXMLParser shouldResolveExternalEntities]](https://developer.apple.com/documentation/foundation/xmlparser/1414143-shouldresolveexternalentities)Removed [-[NSXMLParser systemID]](https://developer.apple.com/documentation/foundation/xmlparser/1411917-systemid)Added [NSXMLParser.allowedExternalEntityURLs](https://developer.apple.com/documentation/foundation/nsxmlparser/1412380-allowedexternalentityurls)Added [NSXMLParser.columnNumber](https://developer.apple.com/documentation/foundation/nsxmlparser/1416983-columnnumber)Added [NSXMLParser.delegate](https://developer.apple.com/documentation/foundation/nsxmlparser/1416209-delegate)Added [NSXMLParser.externalEntityResolvingPolicy](https://developer.apple.com/documentation/foundation/xmlparser/1407399-externalentityresolvingpolicy)Added [NSXMLParser.lineNumber](https://developer.apple.com/documentation/foundation/xmlparser/1413404-linenumber)Added [NSXMLParser.parserError](https://developer.apple.com/documentation/foundation/nsxmlparser/1417446-parsererror)Added [NSXMLParser.publicID](https://developer.apple.com/documentation/foundation/xmlparser/1414516-publicid)Added [NSXMLParser.shouldProcessNamespaces](https://developer.apple.com/documentation/foundation/xmlparser/1418380-shouldprocessnamespaces)Added [NSXMLParser.shouldReportNamespacePrefixes](https://developer.apple.com/documentation/foundation/nsxmlparser/1410809-shouldreportnamespaceprefixes)Added [NSXMLParser.shouldResolveExternalEntities](https://developer.apple.com/documentation/foundation/xmlparser/1414143-shouldresolveexternalentities)Added [NSXMLParser.systemID](https://developer.apple.com/documentation/foundation/xmlparser/1411917-systemid)Added [NSXMLParserExternalEntityResolvingPolicy](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy)Added [NSXMLParserResolveExternalEntitiesAlways](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/always)Added [NSXMLParserResolveExternalEntitiesNever](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/never)Added [NSXMLParserResolveExternalEntitiesNoNetwork](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/nonetwork)Added [NSXMLParserResolveExternalEntitiesSameOriginOnly](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/sameoriginonly)Modified [-[NSXMLParser initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/xmlparser/1415575-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |

Modified [-[NSXMLParser initWithData:]](https://developer.apple.com/documentation/foundation/nsxmlparser/1418103-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [-[NSXMLParser initWithStream:]](https://developer.apple.com/documentation/foundation/nsxmlparser/1415904-initwithstream)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithStream:(NSInputStream *)stream ``` |
| To | ``` - (instancetype)initWithStream:(NSInputStream *)stream ``` |

Modified [-[NSXMLParserDelegate parser:didEndElement:namespaceURI:qualifiedName:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1417955-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:didEndMappingPrefix:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1412878-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:didStartElement:namespaceURI:qualifiedName:attributes:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1415894-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:didStartMappingPrefix:toURI:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1416738-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1416969-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundCDATA:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1407687-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundCharacters:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1412539-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundComment:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1417651-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundElementDeclarationWithName:model:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1411043-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundExternalEntityDeclarationWithName:publicID:systemID:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1408156-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundIgnorableWhitespace:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1416470-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundInternalEntityDeclarationWithName:value:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1414803-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundNotationDeclarationWithName:publicID:systemID:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1411925-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundProcessingInstructionWithTarget:data:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1412929-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1412907-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:parseErrorOccurred:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1412379-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:resolveExternalEntityName:systemID:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1416221-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:validationErrorOccurred:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1417838-parser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parserDidEndDocument:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1418172-parserdidenddocument)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parserDidStartDocument:]](https://developer.apple.com/documentation/foundation/nsxmlparserdelegate/1412065-parserdidstartdocument)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

NSXPCConnection.hRemoved [-[NSXPCConnection remoteObjectProxy]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1411031-remoteobjectproxy)Removed [-[NSXPCListener endpoint]](https://developer.apple.com/documentation/foundation/nsxpclistener/1408519-endpoint)Added [NSXPCConnection.remoteObjectProxy](https://developer.apple.com/documentation/foundation/nsxpcconnection/1411031-remoteobjectproxy)Added [NSXPCListener.endpoint](https://developer.apple.com/documentation/foundation/nsxpclistener/1408519-endpoint)Modified [NSXPCConnection.endpoint](https://developer.apple.com/documentation/foundation/nsxpcconnection/1411757-endpoint)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSXPCListenerEndpoint *endpoint ``` |
| To | ``` @property(readonly, retain) NSXPCListenerEndpoint *endpoint ``` |

Modified [-[NSXPCConnection initWithListenerEndpoint:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1416298-initwithlistenerendpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithListenerEndpoint:(NSXPCListenerEndpoint *)endpoint ``` |
| To | ``` - (instancetype)initWithListenerEndpoint:(NSXPCListenerEndpoint *)endpoint ``` |

Modified [-[NSXPCConnection initWithMachServiceName:options:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1418074-initwithmachservicename)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMachServiceName:(NSString *)name options:(NSXPCConnectionOptions)options ``` |
| To | ``` - (instancetype)initWithMachServiceName:(NSString *)name options:(NSXPCConnectionOptions)options ``` |

Modified [-[NSXPCConnection initWithServiceName:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1416370-initwithservicename)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithServiceName:(NSString *)serviceName ``` |
| To | ``` - (instancetype)initWithServiceName:(NSString *)serviceName ``` |

Modified [NSXPCConnection.serviceName](https://developer.apple.com/documentation/foundation/nsxpcconnection/1413751-servicename)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *serviceName ``` |
| To | ``` @property(readonly, copy) NSString *serviceName ``` |

Modified [+[NSXPCListener anonymousListener]](https://developer.apple.com/documentation/foundation/nsxpclistener/1412648-anonymouslistener)

|  | Declaration |
| --- | --- |
| From | ``` + (id)anonymousListener ``` |
| To | ``` + (NSXPCListener *)anonymousListener ``` |

Modified [-[NSXPCListener initWithMachServiceName:]](https://developer.apple.com/documentation/foundation/nsxpclistener/1414106-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithMachServiceName:(NSString *)name ``` | -- |
| To | ``` - (instancetype)initWithMachServiceName:(NSString *)name ``` | yes |

Modified [+[NSXPCListener serviceListener]](https://developer.apple.com/documentation/foundation/nsxpclistener/1408414-servicelistener)

|  | Declaration |
| --- | --- |
| From | ``` + (id)serviceListener ``` |
| To | ``` + (NSXPCListener *)serviceListener ``` |

Modified [-[NSXPCListenerDelegate listener:shouldAcceptNewConnection:]](https://developer.apple.com/documentation/foundation/nsxpclistenerdelegate/1410381-listener)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
