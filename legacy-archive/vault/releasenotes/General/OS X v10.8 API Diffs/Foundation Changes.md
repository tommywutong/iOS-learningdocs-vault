---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/Foundation.html
archived_at: '2026-07-18T02:54:00.837900Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# Foundation Changes

## Foundation

FoundationErrors.hAdded [NSFeatureUnsupportedError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsfeatureunsupportederror)Added [NSXPCConnectionErrorMaximum](https://developer.apple.com/documentation/foundation/nsxpcconnectionerrormaximum)Added [NSXPCConnectionErrorMinimum](https://developer.apple.com/documentation/foundation/nsxpcconnectionerrorminimum)Added [NSXPCConnectionInterrupted](https://developer.apple.com/documentation/foundation/nsxpcconnectioninterrupted)Added [NSXPCConnectionInvalid](https://developer.apple.com/documentation/foundation/nsxpcconnectioninvalid)Added [NSXPCConnectionReplyInvalid](https://developer.apple.com/documentation/foundation/nsxpcconnectionreplyinvalid)Added NS_ENUM_AVAILABLE (no architecture available)NSAppleEventDescriptor.hModified [NSAppleEventDescriptor](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCopying, NSSecureCoding |

NSArchiver.hRemoved -[NSUnarchiver NS_AUTOMATED_REFCOUNT_UNAVAILABLE] (no architecture available)NSArray.hAdded -[NSArray NS_OPTIONS] (no architecture available)Added [-[NSArray objectAtIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsarray/1414084-subscript)Added [-[NSMutableArray setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1460093-setobject)Modified [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

NSAttributedString.hAdded -[NSAttributedString NS_OPTIONS] (no architecture available)NSByteCountFormatter.hAdded [NSByteCountFormatter](https://developer.apple.com/documentation/foundation/nsbytecountformatter)Added [NSByteCountFormatter.adaptive](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1417887-adaptive)Added [NSByteCountFormatter.allowedUnits](https://developer.apple.com/documentation/foundation/bytecountformatter/1409137-allowedunits)Added [NSByteCountFormatter.allowsNonnumericFormatting](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1408929-allowsnonnumericformatting)Added [NSByteCountFormatter.countStyle](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1417194-countstyle)Added [NSByteCountFormatter.includesActualByteCount](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1411068-includesactualbytecount)Added [NSByteCountFormatter.includesCount](https://developer.apple.com/documentation/foundation/nsbytecountformatter/1409874-includescount)Added [NSByteCountFormatter.includesUnit](https://developer.apple.com/documentation/foundation/bytecountformatter/1415784-includesunit)Added [-[NSByteCountFormatter stringFromByteCount:]](https://developer.apple.com/documentation/foundation/bytecountformatter/1415338-string)Added [+[NSByteCountFormatter stringFromByteCount:countStyle:]](https://developer.apple.com/documentation/foundation/bytecountformatter/1408178-string)Added [NSByteCountFormatter.zeroPadsFractionDigits](https://developer.apple.com/documentation/foundation/bytecountformatter/1409630-zeropadsfractiondigits)Added [NSByteCountFormatterCountStyle](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle)Added [NSByteCountFormatterCountStyleBinary](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle/nsbytecountformattercountstylebinary)Added [NSByteCountFormatterCountStyleDecimal](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle/nsbytecountformattercountstyledecimal)Added [NSByteCountFormatterCountStyleFile](https://developer.apple.com/documentation/foundation/nsbytecountformattercountstyle/nsbytecountformattercountstylefile)Added [NSByteCountFormatterCountStyleMemory](https://developer.apple.com/documentation/foundation/bytecountformatter/countstyle/memory)Added [NSByteCountFormatterUnits](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits)Added [NSByteCountFormatterUseAll](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatteruseall)Added [NSByteCountFormatterUseBytes](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusebytes)Added [NSByteCountFormatterUseDefault](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusedefault)Added [NSByteCountFormatterUseEB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatteruseeb)Added [NSByteCountFormatterUseGB](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1408366-usegb)Added [NSByteCountFormatterUseKB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusekb)Added [NSByteCountFormatterUseMB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusemb)Added [NSByteCountFormatterUsePB](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1412971-usepb)Added [NSByteCountFormatterUseTB](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1408225-usetb)Added [NSByteCountFormatterUseYBOrHigher](https://developer.apple.com/documentation/foundation/bytecountformatter/units/1418399-useyborhigher)Added [NSByteCountFormatterUseZB](https://developer.apple.com/documentation/foundation/nsbytecountformatterunits/nsbytecountformatterusezb)Added NS_ENUM() (no architecture available)Added NS_OPTIONS() (no architecture available)NSCalendar.hAdded [-[NSDateComponents isLeapMonth]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408836-isleapmonth)Added [-[NSDateComponents setLeapMonth:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1408836-leapmonth)Modified [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSCoder.hRemoved -[NSCoder NS_AUTOMATED_REFCOUNT_UNAVAILABLE] (no architecture available)Added [-[NSCoder allowedClasses]](https://developer.apple.com/documentation/foundation/nscoder/1412486-allowedclasses)Added [-[NSCoder decodeObjectOfClass:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1442558-decodeobjectofclass)Added [-[NSCoder decodeObjectOfClasses:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1442560-decodeobjectofclasses)Added [-[NSCoder decodePropertyListForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1416284-decodepropertylist)Added [-[NSCoder requiresSecureCoding]](https://developer.apple.com/documentation/foundation/nscoder/1409845-requiressecurecoding)NSData.hAdded [NSDataWritingWithoutOverwriting](https://developer.apple.com/documentation/foundation/nsdatawritingoptions/nsdatawritingwithoutoverwriting)Added NS_ENUM_AVAILABLE() (no architecture available)Modified [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

NSDate.hModified [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSDateFormatter.hAdded -[NSDateFormatter NS_ENUM] (no architecture available)NSDictionary.hAdded [-[NSDictionary objectForKeyedSubscript:]](https://developer.apple.com/documentation/foundation/nsdictionary/1415430-subscript)Added [+[NSDictionary sharedKeySetForKeys:]](https://developer.apple.com/documentation/foundation/nsdictionary/1408190-sharedkeyset)Added [+[NSMutableDictionary dictionaryWithSharedKeySet:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1412658-dictionarywithsharedkeyset)Added [-[NSMutableDictionary setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1574187-setobject)Added NSDictionary(NSSharedKeySetDictionary)Added NSMutableDictionary(NSSharedKeySetDictionary)Modified [-[NSMutableDictionary setObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/setObject:forKey:)

|  | Declaration |
| --- | --- |
| From | - (void)setObject:(id)anObject forKey:(id)aKey |
| To | - (void)setObject:(id)anObject forKey:(id < NSCopying >)aKey |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id[])objects forKeys:(const id[])keys count:(NSUInteger)cnt |
| To | - (id)initWithObjects:(const id[])objects forKeys:(const id < NSCopying >[])keys count:(NSUInteger)cnt |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObjects:(const id[])objects forKeys:(const id[])keys count:(NSUInteger)cnt |
| To | + (id)dictionaryWithObjects:(const id[])objects forKeys:(const id < NSCopying >[])keys count:(NSUInteger)cnt |

Modified [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

Modified [+[NSDictionary dictionaryWithObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObject:forKey:)

|  | Declaration |
| --- | --- |
| From | + (id)dictionaryWithObject:(id)object forKey:(id)key |
| To | + (id)dictionaryWithObject:(id)object forKey:(id < NSCopying >)key |

NSError.hModified [NSError](https://developer.apple.com/documentation/foundation/nserror)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSFileCoordinator.hAdded [-[NSFileCoordinator itemAtURL:willMoveToURL:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1408668-itematurl)NSFileHandle.hModified [NSFileHandle](https://developer.apple.com/documentation/foundation/filehandle)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSSecureCoding |

NSFileManager.hAdded [-[NSFileManager trashItemAtURL:resultingItemURL:error:]](https://developer.apple.com/documentation/foundation/filemanager/1414306-trashitem)Added [-[NSFileManager ubiquityIdentityToken]](https://developer.apple.com/documentation/foundation/nsfilemanager/1408036-ubiquityidentitytoken)Added [NSUbiquityIdentityDidChangeNotification](https://developer.apple.com/documentation/foundation/nsubiquityidentitydidchangenotification)NSFilePresenter.hAdded [NSFilePresenter.primaryPresentedItemURL](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415415-primarypresenteditemurl)NSGarbageCollector.hModified [-[NSGarbageCollector disableCollectorForPointer:]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431013-disablecollectorforpointer)

|  | Declaration |
| --- | --- |
| From | - (void)disableCollectorForPointer:(void \*)ptr |
| To | - (void)disableCollectorForPointer:(const void \*)ptr |

Modified [-[NSGarbageCollector enableCollectorForPointer:]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431017-enablecollectorforpointer)

|  | Declaration |
| --- | --- |
| From | - (void)enableCollectorForPointer:(void \*)ptr |
| To | - (void)enableCollectorForPointer:(const void \*)ptr |

NSHashTable.hAdded [+[NSHashTable weakObjectsHashTable]](https://developer.apple.com/documentation/foundation/nshashtable/1412241-weakobjectshashtable)Added [NSHashTableWeakMemory](https://developer.apple.com/documentation/foundation/nshashtablezeroingweakmemory)Added NS_ENUM_DEPRECATED_MAC (no architecture available)Modified [+[NSHashTable hashTableWithWeakObjects]](https://developer.apple.com/documentation/foundation/nshashtable/1591430-hashtablewithweakobjects)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSIndexPath.hModified [-[NSIndexPath initWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416906-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithIndexes:(NSUInteger \*)indexes length:(NSUInteger)length |
| To | - (id)initWithIndexes:(const NSUInteger[])indexes length:(NSUInteger)length |

Modified [+[NSIndexPath indexPathWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1521015-indexpathwithindexes)

|  | Declaration |
| --- | --- |
| From | + (id)indexPathWithIndexes:(NSUInteger \*)indexes length:(NSUInteger)length |
| To | + (id)indexPathWithIndexes:(const NSUInteger[])indexes length:(NSUInteger)length |

NSLocale.hAdded -[NSLocale NS_ENUM] (no architecture available)Modified [NSLocale](https://developer.apple.com/documentation/foundation/nslocale)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSMapTable.hAdded [+[NSMapTable strongToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391440-strongtostrongobjectsmaptable)Added [+[NSMapTable strongToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391366-strongtoweakobjectsmaptable)Added [+[NSMapTable weakToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391346-weaktostrongobjectsmaptable)Added [+[NSMapTable weakToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391430-weaktoweakobjectsmaptable)Added [NSMapTableWeakMemory](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptableweakmemory)Modified [+[NSMapTable mapTableWithStrongToStrongObjects]](https://developer.apple.com/documentation/foundation/nsmaptable/1391376-maptablewithstrongtostrongobject)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [+[NSMapTable mapTableWithWeakToStrongObjects]](https://developer.apple.com/documentation/foundation/nsmaptable/1391436-maptablewithweaktostrongobjects)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [+[NSMapTable mapTableWithStrongToWeakObjects]](https://developer.apple.com/documentation/foundation/nsmaptable/1391372-maptablewithstrongtoweakobjects)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [+[NSMapTable mapTableWithWeakToWeakObjects]](https://developer.apple.com/documentation/foundation/nsmaptable/1391374-maptablewithweaktoweakobjects)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSNetServices.hModified [-[NSNetService getInputStream:outputStream:]](https://developer.apple.com/documentation/foundation/netservice/1418325-getinputstream)

|  | Declaration |
| --- | --- |
| From | - (BOOL)getInputStream:(NSInputStream \*\*)inputStream outputStream:(NSOutputStream \*\*)outputStream |
| To | - (BOOL)getInputStream:(out NSInputStream \*\*)inputStream outputStream:(out NSOutputStream \*\*)outputStream |

NSNull.hModified [NSNull](https://developer.apple.com/documentation/foundation/nsnull)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSNumberFormatter.hAdded -[NSNumberFormatter NS_ENUM] (no architecture available)NSObjCRuntime.hAdded #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_NAAdded [#def NSFoundationVersionNumber10_6_6](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_6)Added [#def NSFoundationVersionNumber10_6_7](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_7)Added [#def NSFoundationVersionNumber10_6_8](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_8)Added [#def NSFoundationVersionNumber10_7](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7)Added [#def NSFoundationVersionNumber10_7_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_1)Added [#def NSFoundationVersionNumber10_7_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_2)Added [#def NSFoundationVersionNumber10_7_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_3)Added [#def NSFoundationVersionNumber10_7_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_7_4)Added #def NS_AUTOMATED_REFCOUNT_WEAK_UNAVAILABLEAdded #def NS_CLASS_AVAILABLE_IOSAdded #def NS_CLASS_AVAILABLE_MACAdded #def NS_ENUMAdded #def NS_ENUM_AVAILABLEAdded #def NS_ENUM_AVAILABLE_IOSAdded #def NS_ENUM_AVAILABLE_MACAdded #def NS_ENUM_DEPRECATEDAdded #def NS_ENUM_DEPRECATED_IOSAdded #def NS_ENUM_DEPRECATED_MACAdded #def NS_OPTIONSAdded #def NS_RELEASES_ARGUMENTAdded #def NS_REPLACES_RECEIVERAdded #def NS_REQUIRES_PROPERTY_DEFINITIONSAdded #def NS_RETURNS_INNER_POINTERAdded #def NS_ROOT_CLASSAdded [#def NS_VALID_UNTIL_END_OF_SCOPE](https://developer.apple.com/documentation/foundation/ns_valid_until_end_of_scope)NSObject.hRemoved -[NSObject NS_AUTOMATED_REFCOUNT_UNAVAILABLE] (no architecture available)Removed -[NSObject NS_UNAVAILABLE] (no architecture available)Added [-[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)Added [NSSecureCoding](https://developer.apple.com/documentation/foundation/nssecurecoding)Added +[NSSecureCoding supportsSecureCoding]Modified [NSCopyObject()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSCopyObject)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSOperation.hAdded -[NSOperation NS_ENUM] (no architecture available)NSOrderedSet.hAdded [-[NSMutableOrderedSet setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1543323-setobject)Added [-[NSOrderedSet objectAtIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414253-subscript)Modified [NSOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

NSPathUtilities.hAdded [NSApplicationScriptsDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nsapplicationscriptsdirectory)Added [NSTrashDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/trashdirectory)NSPointerArray.hRemoved NSPointerArray(NSArrayConveniences)Added [+[NSPointerArray strongObjectsPointerArray]](https://developer.apple.com/documentation/foundation/nspointerarray/1413102-strongobjects)Added [+[NSPointerArray weakObjectsPointerArray]](https://developer.apple.com/documentation/foundation/nspointerarray/1412795-weakobjectspointerarray)Added NSPointerArray(NSPointerArrayConveniences)Modified [+[NSPointerArray pointerArrayWithWeakObjects]](https://developer.apple.com/documentation/foundation/nspointerarray/1564846-pointerarraywithweakobjects)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [+[NSPointerArray pointerArrayWithStrongObjects]](https://developer.apple.com/documentation/foundation/nspointerarray/1564843-pointerarraywithstrongobjects)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSPointerFunctions.hAdded [NSPointerFunctionsWeakMemory](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionsweakmemory)NSProxy.hRemoved -[NSProxy NS_UNAVAILABLE] (no architecture available)Added [-[NSProxy debugDescription]](https://developer.apple.com/documentation/foundation/nsproxy/1416366-debugdescription)NSSet.hModified [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration, NSMutableCopying, NSSecureCoding |

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | - (id)initWithObjects:(const id \*)objects count:(NSUInteger)cnt |
| To | - (id)initWithObjects:(const id[])objects count:(NSUInteger)cnt |

Modified [+[NSSet setWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | + (id)setWithObjects:(const id \*)objects count:(NSUInteger)cnt |
| To | + (id)setWithObjects:(const id[])objects count:(NSUInteger)cnt |

NSString.hAdded -[NSString NS_OPTIONS] (no architecture available)Added [-[NSString capitalizedStringWithLocale:]](https://developer.apple.com/documentation/foundation/nsstring/1414023-capitalized)Added [-[NSString lowercaseStringWithLocale:]](https://developer.apple.com/documentation/foundation/nsstring/1417298-lowercasestringwithlocale)Added [-[NSString uppercaseStringWithLocale:]](https://developer.apple.com/documentation/foundation/nsstring/1413316-uppercased)Modified [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

NSTimeZone.hAdded -[NSTimeZone NS_ENUM] (no architecture available)Modified [NSTimeZone](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/cl/NSTimeZone)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSURL.hRemoved [NSURLFileScheme](https://developer.apple.com/documentation/foundation/nsurlfilescheme)Added -[NSURL NS_ENUM_AVAILABLE] (no architecture available)Added -[NSURL NS_OPTIONS] (no architecture available)Added [-[NSURL startAccessingSecurityScopedResource]](https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso)Added [-[NSURL stopAccessingSecurityScopedResource]](https://developer.apple.com/documentation/foundation/nsurl/1413736-stopaccessingsecurityscopedresou)Added [NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationsecurityscopeallowonlyreadaccess)Added [NSURLBookmarkCreationWithSecurityScope](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationwithsecurityscope)Added [NSURLBookmarkResolutionWithSecurityScope](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/1412803-withsecurityscope)Added [NSURLIsExcludedFromBackupKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1408756-isexcludedfrombackupkey)Added [NSURLPathKey](https://developer.apple.com/documentation/foundation/nsurlpathkey)Modified [NSURLUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitempercentdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [NSURL](https://developer.apple.com/documentation/foundation/nsurl)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSURLHandleClient |
| To | NSCopying, NSSecureCoding, NSURLHandleClient |

Modified [NSURLUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1572055-ubiquitousitempercentuploadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

NSURLAuthenticationChallenge.hModified [NSURLAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCoding |

NSURLConnection.hRemoved -[NSURLConnectionDelegate connection:didReceiveData:]Removed -[NSURLConnectionDelegate connection:didReceiveResponse:]Removed -[NSURLConnectionDelegate connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:]Removed -[NSURLConnectionDelegate connection:needNewBodyStream:]Removed -[NSURLConnectionDelegate connection:willCacheResponse:]Removed -[NSURLConnectionDelegate connection:willSendRequest:redirectResponse:]Removed -[NSURLConnectionDelegate connectionDidFinishLoading:]Added [NSURLConnectionDataDelegate](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate)Added [-[NSURLConnectionDataDelegate connection:didReceiveData:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1414090-connection)Added [-[NSURLConnectionDataDelegate connection:didReceiveResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1407728-connection)Added [-[NSURLConnectionDataDelegate connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1418264-connection)Added [-[NSURLConnectionDataDelegate connection:needNewBodyStream:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1412892-connection)Added [-[NSURLConnectionDataDelegate connection:willCacheResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1414834-connection)Added [-[NSURLConnectionDataDelegate connection:willSendRequest:redirectResponse:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1415830-connection)Added [-[NSURLConnectionDataDelegate connectionDidFinishLoading:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/1416409-connectiondidfinishloading)Added [NSURLConnectionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate)Added [-[NSURLConnectionDownloadDelegate connection:didWriteData:totalBytesWritten:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1418304-connection)Added [-[NSURLConnectionDownloadDelegate connectionDidFinishDownloading:destinationURL:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1412126-connectiondidfinishdownloading)Added [-[NSURLConnectionDownloadDelegate connectionDidResumeDownloading:totalBytesWritten:expectedTotalBytes:]](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/1418157-connectiondidresumedownloading)NSURLCredential.hModified [NSURLCredential](https://developer.apple.com/documentation/foundation/urlcredential)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

NSURLProtectionSpace.hModified [NSURLProtectionSpace](https://developer.apple.com/documentation/foundation/nsurlprotectionspace)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

NSURLRequest.hAdded [-[NSMutableURLRequest setAllowsCellularAccess:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1416749-allowscellularaccess)Added [-[NSURLRequest allowsCellularAccess]](https://developer.apple.com/documentation/foundation/nsurlrequest/1412032-allowscellularaccess)NSURLResponse.hAdded [-[NSHTTPURLResponse initWithURL:statusCode:HTTPVersion:headerFields:]](https://developer.apple.com/documentation/foundation/nshttpurlresponse/1415870-initwithurl)NSUUID.hAdded [NSUUID](https://developer.apple.com/documentation/foundation/nsuuid)Added [+[NSUUID UUID]](https://developer.apple.com/documentation/foundation/nsuuid/1574571-uuid)Added [-[NSUUID UUIDString]](https://developer.apple.com/documentation/foundation/nsuuid/1416585-uuidstring)Added [-[NSUUID getUUIDBytes:]](https://developer.apple.com/documentation/foundation/nsuuid/1411420-getbytes)Added [-[NSUUID init]](https://developer.apple.com/documentation/foundation/nsuuid/1415797-init)Added [-[NSUUID initWithUUIDBytes:]](https://developer.apple.com/documentation/foundation/nsuuid/1417039-init)Added [-[NSUUID initWithUUIDString:]](https://developer.apple.com/documentation/foundation/nsuuid/1411662-init)NSUbiquitousKeyValueStore.hAdded [NSUbiquitousKeyValueStoreAccountChange](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreaccountchange)NSUserNotification.hAdded [NSUserNotification](https://developer.apple.com/documentation/foundation/nsusernotification)Added [NSUserNotification.actionButtonTitle](https://developer.apple.com/documentation/foundation/nsusernotification/1411669-actionbuttontitle)Added [NSUserNotification.activationType](https://developer.apple.com/documentation/foundation/nsusernotification/1416143-activationtype)Added [NSUserNotification.actualDeliveryDate](https://developer.apple.com/documentation/foundation/nsusernotification/1416009-actualdeliverydate)Added [NSUserNotification.deliveryDate](https://developer.apple.com/documentation/foundation/nsusernotification/1407781-deliverydate)Added [NSUserNotification.deliveryRepeatInterval](https://developer.apple.com/documentation/foundation/nsusernotification/1411500-deliveryrepeatinterval)Added [NSUserNotification.deliveryTimeZone](https://developer.apple.com/documentation/foundation/nsusernotification/1416406-deliverytimezone)Added [NSUserNotification.hasActionButton](https://developer.apple.com/documentation/foundation/nsusernotification/1411564-hasactionbutton)Added [NSUserNotification.informativeText](https://developer.apple.com/documentation/foundation/nsusernotification/1416180-informativetext)Added [NSUserNotification.otherButtonTitle](https://developer.apple.com/documentation/foundation/nsusernotification/1412410-otherbuttontitle)Added [NSUserNotification.presented](https://developer.apple.com/documentation/foundation/nsusernotification/1409281-presented)Added [NSUserNotification.remote](https://developer.apple.com/documentation/foundation/nsusernotification/1411995-isremote)Added [NSUserNotification.soundName](https://developer.apple.com/documentation/foundation/nsusernotification/1412612-soundname)Added [NSUserNotification.subtitle](https://developer.apple.com/documentation/foundation/nsusernotification/1413777-subtitle)Added [NSUserNotification.title](https://developer.apple.com/documentation/foundation/nsusernotification/1415172-title)Added [NSUserNotification.userInfo](https://developer.apple.com/documentation/foundation/nsusernotification/1415675-userinfo)Added [NSUserNotificationCenter](https://developer.apple.com/documentation/foundation/nsusernotificationcenter)Added [+[NSUserNotificationCenter defaultUserNotificationCenter]](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1416403-defaultusernotificationcenter)Added [NSUserNotificationCenter.delegate](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1410385-delegate)Added [-[NSUserNotificationCenter deliverNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1414633-delivernotification)Added [NSUserNotificationCenter.deliveredNotifications](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1407791-deliverednotifications)Added [-[NSUserNotificationCenter removeAllDeliveredNotifications]](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1416204-removealldeliverednotifications)Added [-[NSUserNotificationCenter removeDeliveredNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1416057-removedeliverednotification)Added [-[NSUserNotificationCenter removeScheduledNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1415613-removeschedulednotification)Added [-[NSUserNotificationCenter scheduleNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1407647-schedulenotification)Added [NSUserNotificationCenter.scheduledNotifications](https://developer.apple.com/documentation/foundation/nsusernotificationcenter/1411832-schedulednotifications)Added [NSUserNotificationCenterDelegate](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate)Added [-[NSUserNotificationCenterDelegate userNotificationCenter:didActivateNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/1418378-usernotificationcenter)Added [-[NSUserNotificationCenterDelegate userNotificationCenter:didDeliverNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/1410579-usernotificationcenter)Added [-[NSUserNotificationCenterDelegate userNotificationCenter:shouldPresentNotification:]](https://developer.apple.com/documentation/foundation/nsusernotificationcenterdelegate/1409032-usernotificationcenter)Added [NSUserNotificationActivationType](https://developer.apple.com/documentation/foundation/nsusernotification/activationtype)Added [NSUserNotificationActivationTypeActionButtonClicked](https://developer.apple.com/documentation/foundation/nsusernotificationactivationtype/nsusernotificationactivationtypeactionbuttonclicked)Added [NSUserNotificationActivationTypeContentsClicked](https://developer.apple.com/documentation/foundation/nsusernotification/activationtype/contentsclicked)Added [NSUserNotificationActivationTypeNone](https://developer.apple.com/documentation/foundation/nsusernotification/activationtype/none)Added [NSUserNotificationDefaultSoundName](https://developer.apple.com/documentation/foundation/nsusernotificationdefaultsoundname)NSUserScriptTask.hAdded [NSUserAppleScriptTask](https://developer.apple.com/documentation/foundation/nsuserapplescripttask)Added [-[NSUserAppleScriptTask executeWithAppleEvent:completionHandler:]](https://developer.apple.com/documentation/foundation/nsuserapplescripttask/1416515-execute)Added [NSUserAutomatorTask](https://developer.apple.com/documentation/foundation/nsuserautomatortask)Added [-[NSUserAutomatorTask executeWithInput:completionHandler:]](https://developer.apple.com/documentation/foundation/nsuserautomatortask/1418079-executewithinput)Added [NSUserAutomatorTask.variables](https://developer.apple.com/documentation/foundation/nsuserautomatortask/1418099-variables)Added [NSUserScriptTask](https://developer.apple.com/documentation/foundation/nsuserscripttask)Added [-[NSUserScriptTask executeWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsuserscripttask/1410967-execute)Added [-[NSUserScriptTask initWithURL:error:]](https://developer.apple.com/documentation/foundation/nsuserscripttask/1409998-initwithurl)Added [-[NSUserScriptTask scriptURL]](https://developer.apple.com/documentation/foundation/nsuserscripttask/1408618-scripturl)Added [NSUserUnixTask](https://developer.apple.com/documentation/foundation/nsuserunixtask)Added [-[NSUserUnixTask executeWithArguments:completionHandler:]](https://developer.apple.com/documentation/foundation/nsuserunixtask/1412077-executewitharguments)Added [NSUserUnixTask.standardError](https://developer.apple.com/documentation/foundation/nsuserunixtask/1411522-standarderror)Added [NSUserUnixTask.standardInput](https://developer.apple.com/documentation/foundation/nsuserunixtask/1407821-standardinput)Added [NSUserUnixTask.standardOutput](https://developer.apple.com/documentation/foundation/nsuserunixtask/1418151-standardoutput)Added [NSUserAutomatorTaskCompletionHandler](https://developer.apple.com/documentation/foundation/nsuserautomatortaskcompletionhandler)Added [NSUserScriptTaskCompletionHandler](https://developer.apple.com/documentation/foundation/nsuserscripttask/completionhandler)Added [NSUserUnixTaskCompletionHandler](https://developer.apple.com/documentation/foundation/nsuserunixtask/completionhandler)NSValue.hModified [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

NSXPCConnection.hAdded [NSXPCConnection](https://developer.apple.com/documentation/foundation/nsxpcconnection)Added [NSXPCConnection.auditSessionIdentifier](https://developer.apple.com/documentation/foundation/nsxpcconnection/1410393-auditsessionidentifier)Added [NSXPCConnection.effectiveGroupIdentifier](https://developer.apple.com/documentation/foundation/nsxpcconnection/1407793-effectivegroupidentifier)Added [NSXPCConnection.effectiveUserIdentifier](https://developer.apple.com/documentation/foundation/nsxpcconnection/1408346-effectiveuseridentifier)Added [NSXPCConnection.endpoint](https://developer.apple.com/documentation/foundation/nsxpcconnection/1411757-endpoint)Added [NSXPCConnection.exportedInterface](https://developer.apple.com/documentation/foundation/nsxpcconnection/1408106-exportedinterface)Added [NSXPCConnection.exportedObject](https://developer.apple.com/documentation/foundation/nsxpcconnection/1412016-exportedobject)Added [-[NSXPCConnection initWithListenerEndpoint:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1416298-initwithlistenerendpoint)Added [-[NSXPCConnection initWithMachServiceName:options:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1418074-initwithmachservicename)Added [-[NSXPCConnection initWithServiceName:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1416370-initwithservicename)Added [NSXPCConnection.interruptionHandler](https://developer.apple.com/documentation/foundation/nsxpcconnection/1407915-interruptionhandler)Added [-[NSXPCConnection invalidate]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1412618-invalidate)Added [NSXPCConnection.invalidationHandler](https://developer.apple.com/documentation/foundation/nsxpcconnection/1414358-invalidationhandler)Added [NSXPCConnection.processIdentifier](https://developer.apple.com/documentation/foundation/nsxpcconnection/1411428-processidentifier)Added [NSXPCConnection.remoteObjectInterface](https://developer.apple.com/documentation/foundation/nsxpcconnection/1411472-remoteobjectinterface)Added [-[NSXPCConnection remoteObjectProxy]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1411031-remoteobjectproxy)Added [-[NSXPCConnection remoteObjectProxyWithErrorHandler:]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1407905-remoteobjectproxywitherrorhandle)Added [-[NSXPCConnection resume]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1408677-resume)Added [NSXPCConnection.serviceName](https://developer.apple.com/documentation/foundation/nsxpcconnection/1413751-servicename)Added [-[NSXPCConnection suspend]](https://developer.apple.com/documentation/foundation/nsxpcconnection/1410778-suspend)Added [NSXPCInterface](https://developer.apple.com/documentation/foundation/nsxpcinterface)Added [-[NSXPCInterface classesForSelector:argumentIndex:ofReply:]](https://developer.apple.com/documentation/foundation/nsxpcinterface/1418323-classesforselector)Added [-[NSXPCInterface interfaceForSelector:argumentIndex:ofReply:]](https://developer.apple.com/documentation/foundation/nsxpcinterface/1409127-interfaceforselector)Added [+[NSXPCInterface interfaceWithProtocol:]](https://developer.apple.com/documentation/foundation/nsxpcinterface/1410202-interfacewithprotocol)Added [NSXPCInterface.protocol](https://developer.apple.com/documentation/foundation/nsxpcinterface/1416353-protocol)Added [-[NSXPCInterface setClasses:forSelector:argumentIndex:ofReply:]](https://developer.apple.com/documentation/foundation/nsxpcinterface/1415555-setclasses)Added [-[NSXPCInterface setInterface:forSelector:argumentIndex:ofReply:]](https://developer.apple.com/documentation/foundation/nsxpcinterface/1414293-setinterface)Added [NSXPCListener](https://developer.apple.com/documentation/foundation/nsxpclistener)Added [+[NSXPCListener anonymousListener]](https://developer.apple.com/documentation/foundation/nsxpclistener/1412648-anonymouslistener)Added [NSXPCListener.delegate](https://developer.apple.com/documentation/foundation/nsxpclistener/1408939-delegate)Added [-[NSXPCListener endpoint]](https://developer.apple.com/documentation/foundation/nsxpclistener/1408519-endpoint)Added [-[NSXPCListener initWithMachServiceName:]](https://developer.apple.com/documentation/foundation/nsxpclistener/1414106-init)Added [-[NSXPCListener invalidate]](https://developer.apple.com/documentation/foundation/nsxpclistener/1418427-invalidate)Added [-[NSXPCListener resume]](https://developer.apple.com/documentation/foundation/nsxpclistener/1409652-resume)Added [+[NSXPCListener serviceListener]](https://developer.apple.com/documentation/foundation/nsxpclistener/1408414-servicelistener)Added [-[NSXPCListener suspend]](https://developer.apple.com/documentation/foundation/nsxpclistener/1411596-suspend)Added [NSXPCListenerDelegate](https://developer.apple.com/documentation/foundation/nsxpclistenerdelegate)Added [-[NSXPCListenerDelegate listener:shouldAcceptNewConnection:]](https://developer.apple.com/documentation/foundation/nsxpclistenerdelegate/1410381-listener)Added [NSXPCListenerEndpoint](https://developer.apple.com/documentation/foundation/nsxpclistenerendpoint)Added [NSXPCProxyCreating](https://developer.apple.com/documentation/foundation/nsxpcproxycreating)Added [-[NSXPCProxyCreating remoteObjectProxy]](https://developer.apple.com/documentation/foundation/nsxpcproxycreating/1418403-remoteobjectproxy)Added [-[NSXPCProxyCreating remoteObjectProxyWithErrorHandler:]](https://developer.apple.com/documentation/foundation/nsxpcproxycreating/1415611-remoteobjectproxywitherrorhandle)Added [NSXPCConnectionOptions](https://developer.apple.com/documentation/foundation/nsxpcconnectionoptions)Added [NSXPCConnectionPrivileged](https://developer.apple.com/documentation/foundation/nsxpcconnectionoptions/nsxpcconnectionprivileged)NSZone.hModified [NSRealMemoryAvailable()](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSRealMemoryAvailable)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

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
