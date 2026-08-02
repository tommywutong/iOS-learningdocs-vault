---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/Foundation.html
archived_at: '2026-07-18T02:58:43.086365Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# Foundation Changes

## Foundation

FoundationErrors.hAdded [NSFileWriteVolumeReadOnlyError](https://developer.apple.com/documentation/foundation/nsfilewritevolumereadonlyerror)Added [NSPropertyListErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nspropertylisterrormaximum)Added [NSPropertyListErrorMinimum](https://developer.apple.com/documentation/foundation/nspropertylisterrorminimum)Added [NSPropertyListReadCorruptError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nspropertylistreadcorrupterror)Added [NSPropertyListReadStreamError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nspropertylistreadstreamerror)Added [NSPropertyListReadUnknownVersionError](https://developer.apple.com/documentation/foundation/nspropertylistreadunknownversionerror)Added [NSPropertyListWriteStreamError](https://developer.apple.com/documentation/foundation/nspropertylistwritestreamerror)NSArray.hAdded [-[NSArray enumerateObjectsAtIndexes:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsarray/1417577-enumerateobjectsatindexes) (no architecture available)Added [-[NSArray enumerateObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsarray/1415846-enumerateobjects) (no architecture available)Added [-[NSArray enumerateObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsarray/1413010-enumerateobjectswithoptions) (no architecture available)Added [-[NSArray indexOfObjectAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1407652-indexofobjectatindexes) (no architecture available)Added [-[NSArray indexOfObjectPassingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1408043-indexofobject) (no architecture available)Added [-[NSArray indexOfObjectWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1417053-indexofobject) (no architecture available)Added [-[NSArray indexesOfObjectsAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1413512-indexesofobjects) (no architecture available)Added [-[NSArray indexesOfObjectsPassingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1417603-indexesofobjectspassingtest) (no architecture available)Added [-[NSArray indexesOfObjectsWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1415087-indexesofobjectswithoptions) (no architecture available)Added [-[NSArray sortedArrayUsingComparator:]](https://developer.apple.com/documentation/foundation/nsarray/1411195-sortedarray) (no architecture available)Added [-[NSArray sortedArrayWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsarray/1417804-sortedarray) (no architecture available)Added [-[NSMutableArray sortUsingComparator:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1414904-sortusingcomparator) (no architecture available)Added [-[NSMutableArray sortWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1414396-sortwithoptions) (no architecture available)Modified [-[NSMutableArray removeObjectsFromIndices:numIndices:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectsFromIndices:numIndices:)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSAttributedString.hAdded [-[NSAttributedString enumerateAttribute:inRange:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1412461-enumerateattribute) (no architecture available)Added [-[NSAttributedString enumerateAttributesInRange:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1412070-enumerateattributes) (no architecture available)Added [NSAttributedStringEnumerationLongestEffectiveRangeNotRequired](https://developer.apple.com/documentation/foundation/nsattributedstringenumerationoptions/nsattributedstringenumerationlongesteffectiverangenotrequired) (no architecture available)Added [NSAttributedStringEnumerationOptions](https://developer.apple.com/documentation/foundation/nsattributedstring/enumerationoptions) (no architecture available)Added [NSAttributedStringEnumerationReverse](https://developer.apple.com/documentation/foundation/nsattributedstringenumerationoptions/nsattributedstringenumerationreverse) (no architecture available)NSBundle.hAdded [-[NSBundle URLForAuxiliaryExecutable:]](https://developer.apple.com/documentation/foundation/bundle/1411412-url)Added [-[NSBundle URLForResource:withExtension:]](https://developer.apple.com/documentation/foundation/nsbundle/1411540-urlforresource)Added [-[NSBundle URLForResource:withExtension:subdirectory:]](https://developer.apple.com/documentation/foundation/nsbundle/1416712-urlforresource)Added [+[NSBundle URLForResource:withExtension:subdirectory:inBundleWithURL:]](https://developer.apple.com/documentation/foundation/bundle/1416361-url)Added [-[NSBundle URLForResource:withExtension:subdirectory:localization:]](https://developer.apple.com/documentation/foundation/bundle/1417378-url)Added [-[NSBundle URLsForResourcesWithExtension:subdirectory:]](https://developer.apple.com/documentation/foundation/bundle/1407424-urls)Added [+[NSBundle URLsForResourcesWithExtension:subdirectory:inBundleWithURL:]](https://developer.apple.com/documentation/foundation/nsbundle/1409807-urlsforresourceswithextension)Added [-[NSBundle URLsForResourcesWithExtension:subdirectory:localization:]](https://developer.apple.com/documentation/foundation/nsbundle/1414688-urlsforresourceswithextension)Added [-[NSBundle builtInPlugInsURL]](https://developer.apple.com/documentation/foundation/nsbundle/1409603-builtinpluginsurl)Added [-[NSBundle bundleURL]](https://developer.apple.com/documentation/foundation/bundle/1415654-bundleurl)Added [+[NSBundle bundleWithURL:]](https://developer.apple.com/documentation/foundation/nsbundle/1494992-bundlewithurl)Added [-[NSBundle executableURL]](https://developer.apple.com/documentation/foundation/bundle/1410470-executableurl)Added [-[NSBundle initWithURL:]](https://developer.apple.com/documentation/foundation/nsbundle/1409352-initwithurl)Added [-[NSBundle privateFrameworksURL]](https://developer.apple.com/documentation/foundation/bundle/1417617-privateframeworksurl)Added [-[NSBundle resourceURL]](https://developer.apple.com/documentation/foundation/bundle/1414821-resourceurl)Added [-[NSBundle sharedFrameworksURL]](https://developer.apple.com/documentation/foundation/nsbundle/1411774-sharedframeworksurl)Added [-[NSBundle sharedSupportURL]](https://developer.apple.com/documentation/foundation/bundle/1416823-sharedsupporturl)NSCache.hAdded [NSCache](https://developer.apple.com/documentation/foundation/nscache)Added [-[NSCache countLimit]](https://developer.apple.com/documentation/foundation/nscache/1416355-countlimit)Added [-[NSCache delegate]](https://developer.apple.com/documentation/foundation/nscache/1413061-delegate)Added [-[NSCache evictsObjectsWithDiscardedContent]](https://developer.apple.com/documentation/foundation/nscache/1408469-evictsobjectswithdiscardedconten)Added [-[NSCache name]](https://developer.apple.com/documentation/foundation/nscache/1409941-name)Added [-[NSCache objectForKey:]](https://developer.apple.com/documentation/foundation/nscache/1415458-object)Added [-[NSCache removeAllObjects]](https://developer.apple.com/documentation/foundation/nscache/1411382-removeallobjects)Added [-[NSCache removeObjectForKey:]](https://developer.apple.com/documentation/foundation/nscache/1409900-removeobject)Added [-[NSCache setCountLimit:]](https://developer.apple.com/documentation/foundation/nscache/1416355-countlimit)Added [-[NSCache setDelegate:]](https://developer.apple.com/documentation/foundation/nscache/1413061-delegate)Added [-[NSCache setEvictsObjectsWithDiscardedContent:]](https://developer.apple.com/documentation/foundation/nscache/1408469-evictsobjectswithdiscardedconten)Added [-[NSCache setName:]](https://developer.apple.com/documentation/foundation/nscache/1409941-name)Added [-[NSCache setObject:forKey:]](https://developer.apple.com/documentation/foundation/nscache/1408223-setobject)Added [-[NSCache setObject:forKey:cost:]](https://developer.apple.com/documentation/foundation/nscache/1416399-setobject)Added [-[NSCache setTotalCostLimit:]](https://developer.apple.com/documentation/foundation/nscache/1407672-totalcostlimit)Added [-[NSCache totalCostLimit]](https://developer.apple.com/documentation/foundation/nscache/1407672-totalcostlimit)Added [NSCacheDelegate](https://developer.apple.com/documentation/foundation/nscachedelegate)Added [-[NSCacheDelegate cache:willEvictObject:]](https://developer.apple.com/documentation/foundation/nscachedelegate/1416107-cache)NSCalendar.hAdded [-[NSDateComponents quarter]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416503-quarter)Added [-[NSDateComponents setQuarter:]](https://developer.apple.com/documentation/foundation/nsdatecomponents/1416503-quarter)Added [NSQuarterCalendarUnit](https://developer.apple.com/documentation/foundation/nscalendar/unit/1414015-nsquartercalendarunit)NSCalendarDate.hRemoved [-[NSCalendarDate description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCalendarDate/Description.html#//apple_ref/occ/instm/NSCalendarDate/description)Removed NSDate(NSNaturalLangage)NSConnection.hModified [+[NSConnection defaultConnection]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/clm/NSConnection/defaultConnection)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSData.hAdded [NSPurgeableData](https://developer.apple.com/documentation/foundation/nspurgeabledata)NSDate.hAdded [-[NSDate dateByAddingTimeInterval:]](https://developer.apple.com/documentation/foundation/nsdate/1408823-addingtimeinterval)Added [+[NSDate dateWithTimeInterval:sinceDate:]](https://developer.apple.com/documentation/foundation/nsdate/1591578-datewithtimeinterval)Added [-[NSDate initWithTimeIntervalSince1970:]](https://developer.apple.com/documentation/foundation/nsdate/1416453-init)Added [NSSystemClockDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1414255-nssystemclockdidchange)Modified [-[NSDate addTimeInterval:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/addTimeInterval:)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [-[NSDate initWithTimeIntervalSinceNow:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeIntervalSinceNow:)

|  | Declaration |
| --- | --- |
| Old | - (id)initWithTimeIntervalSinceNow:(NSTimeInterval)secsToBeAddedToNow |
| New | - (id)initWithTimeIntervalSinceNow:(NSTimeInterval)secs |

Modified [-[NSDate descriptionWithLocale:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/descriptionWithLocale:)

|  | Header |
| --- | --- |
| Old | NSCalendarDate.h |
| New | NSDate.h |

NSDateFormatter.hRemoved -[NSDateFormatter init]Added [+[NSDateFormatter localizedStringFromDate:dateStyle:timeStyle:]](https://developer.apple.com/documentation/foundation/dateformatter/1415241-localizedstring)Modified [-[NSDateFormatter getObjectValue:forString:range:error:]](https://developer.apple.com/documentation/foundation/dateformatter/1409248-getobjectvalue)

|  | Declaration |
| --- | --- |
| Old | - (BOOL)getObjectValue:(id \*)obj forString:(NSString \*)string range:(inout NSRange \*)rangep error:(NSError \*\*)error |
| New | - (BOOL)getObjectValue:(out id \*)obj forString:(NSString \*)string range:(inout NSRange \*)rangep error:(out NSError \*\*)error |

NSDebug.hModified +[NSAutoreleasePool resetTotalAutoreleasedObjects]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool poolCountHighWaterResolution]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool enableRelease:]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool autoreleasedObjectCount]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool topAutoreleasePoolCount]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool totalAutoreleasedObjects]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool setPoolCountHighWaterResolution:]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool setPoolCountHighWaterMark:]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool enableFreedObjectCheck:]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified +[NSAutoreleasePool poolCountHighWaterMark]

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

NSDictionary.hAdded [-[NSDictionary enumerateKeysAndObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsdictionary/1414570-enumeratekeysandobjectsusingbloc) (no architecture available)Added [-[NSDictionary enumerateKeysAndObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsdictionary/1409739-enumeratekeysandobjectswithoptio) (no architecture available)Added [-[NSDictionary keysSortedByValueUsingComparator:]](https://developer.apple.com/documentation/foundation/nsdictionary/1411105-keyssortedbyvalueusingcomparator) (no architecture available)Added [-[NSDictionary keysSortedByValueWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsdictionary/1415717-keyssortedbyvaluewithoptions) (no architecture available)NSError.hAdded [-[NSError helpAnchor]](https://developer.apple.com/documentation/foundation/nserror/1414718-helpanchor)Added [NSHelpAnchorErrorKey](https://developer.apple.com/documentation/foundation/nshelpanchorerrorkey)NSException.hAdded [NSAssertionHandlerKey](https://developer.apple.com/documentation/foundation/nsassertionhandlerkey)NSExpression.hAdded [-[NSExpression expressionBlock]](https://developer.apple.com/documentation/foundation/nsexpression/1409139-expressionblock) (no architecture available)Added [+[NSExpression expressionForBlock:arguments:]](https://developer.apple.com/documentation/foundation/nsexpression/1407823-expressionforblock) (no architecture available)Added [NSBlockExpressionType](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype/block)NSFileManager.hAdded [-[NSFileManager copyItemAtURL:toURL:error:]](https://developer.apple.com/documentation/foundation/filemanager/1412957-copyitem)Added [-[NSFileManager linkItemAtURL:toURL:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1414456-linkitematurl)Added [-[NSFileManager moveItemAtURL:toURL:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1414750-moveitematurl)Added [-[NSFileManager removeItemAtURL:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1413590-removeitematurl)Added -[NSObject fileManager:shouldCopyItemAtURL:toURL:]Added -[NSObject fileManager:shouldLinkItemAtURL:toURL:]Added -[NSObject fileManager:shouldMoveItemAtURL:toURL:]Added -[NSObject fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:]Added -[NSObject fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:]Added -[NSObject fileManager:shouldProceedAfterError:movingItemAtURL:toURL:]Added -[NSObject fileManager:shouldProceedAfterError:removingItemAtURL:]Added -[NSObject fileManager:shouldRemoveItemAtURL:]NSFormatter.hModified [-[NSFormatter getObjectValue:forString:errorDescription:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/getObjectValue:forString:errorDescription:)

|  | Declaration |
| --- | --- |
| Old | - (BOOL)getObjectValue:(id \*)obj forString:(NSString \*)string errorDescription:(NSString \*\*)error |
| New | - (BOOL)getObjectValue:(out id \*)obj forString:(NSString \*)string errorDescription:(out NSString \*\*)error |

NSGeometry.hModified [-[NSCoder encodePoint:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1391114-encodepoint)

|  | Header |
| --- | --- |
| Old | NSKeyedArchiver.h |
| New | NSGeometry.h |

Modified [-[NSCoder decodeRectForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1391116-decoderectforkey)

|  | Header |
| --- | --- |
| Old | NSKeyedArchiver.h |
| New | NSGeometry.h |

Modified [-[NSCoder encodeSize:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1391176-encodesize)

|  | Header |
| --- | --- |
| Old | NSKeyedArchiver.h |
| New | NSGeometry.h |

Modified NSCoder(NSGeometryKeyedCoding)

|  | Header |
| --- | --- |
| Old | NSKeyedArchiver.h |
| New | NSGeometry.h |

Modified [-[NSCoder decodeSizeForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1391253-decodesize)

|  | Header |
| --- | --- |
| Old | NSKeyedArchiver.h |
| New | NSGeometry.h |

Modified [-[NSCoder decodePointForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1391214-decodepoint)

|  | Header |
| --- | --- |
| Old | NSKeyedArchiver.h |
| New | NSGeometry.h |

Modified [-[NSCoder encodeRect:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1391287-encode)

|  | Header |
| --- | --- |
| Old | NSKeyedArchiver.h |
| New | NSGeometry.h |

NSIndexSet.hAdded [-[NSIndexSet enumerateIndexesInRange:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsindexset/1408162-enumerateindexesinrange) (no architecture available)Added [-[NSIndexSet enumerateIndexesUsingBlock:]](https://developer.apple.com/documentation/foundation/nsindexset/1411395-enumerateindexesusingblock) (no architecture available)Added [-[NSIndexSet enumerateIndexesWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsindexset/1414545-enumerate) (no architecture available)Added [-[NSIndexSet indexInRange:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsindexset/1415301-index) (no architecture available)Added [-[NSIndexSet indexPassingTest:]](https://developer.apple.com/documentation/foundation/nsindexset/1408471-index) (no architecture available)Added [-[NSIndexSet indexWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsindexset/1415860-index) (no architecture available)NSInvocation.hModified [NSObjCUnionType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCUnionType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCNoType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCNoType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCFloatType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCFloatType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCDoubleType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCDoubleType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCSelectorType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCSelectorType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCLonglongType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCLonglongType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCCharType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCCharType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified NSObjCBoolType

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCVoidType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCVoidType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCObjectType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCObjectType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSObjCValue)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCStructType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCStructType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCPointerType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCPointerType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCBitfield](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCBitfield)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCLongType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCLongType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCStringType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCStringType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCShortType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCShortType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified [NSObjCArrayType](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSObjCArrayType)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

NSJavaSetup.hRemoved [NSJavaBundleCleanup()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806670-nsjavabundlecleanup)Removed [NSJavaBundleSetup()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806677-nsjavabundlesetup)Removed NSJavaClassesRemoved [NSJavaClassesForBundle()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806687-nsjavaclassesforbundle)Removed [NSJavaClassesFromPath()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806697-nsjavaclassesfrompath)Removed [NSJavaDidCreateVirtualMachineNotification](https://developer.apple.com/documentation/foundation/object_runtime/java_support/nsjavadidcreatevirtualmachinenotification)Removed [NSJavaDidSetupVirtualMachineNotification](https://developer.apple.com/documentation/foundation/object_runtime/java_support/nsjavadidsetupvirtualmachinenotification)Removed NSJavaLibraryPathRemoved [NSJavaNeedsToLoadClasses()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806703-nsjavaneedstoloadclasses)Removed [NSJavaNeedsVirtualMachine()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806712-nsjavaneedsvirtualmachine)Removed [NSJavaObjectNamedInPath()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806720-nsjavaobjectnamedinpath)Removed NSJavaOwnVirtualMachineRemoved NSJavaPathRemoved NSJavaPathSeparatorRemoved [NSJavaProvidesClasses()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806727-nsjavaprovidesclasses)Removed NSJavaRootRemoved [NSJavaSetup()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806733-nsjavasetup)Removed [NSJavaSetupVirtualMachine()](https://developer.apple.com/documentation/foundation/object_runtime/java_support/1806737-nsjavasetupvirtualmachine)Removed NSJavaUserPathRemoved [NSJavaWillCreateVirtualMachineNotification](https://developer.apple.com/documentation/foundation/object_runtime/java_support/nsjavawillcreatevirtualmachinenotification)Removed [NSJavaWillSetupVirtualMachineNotification](https://developer.apple.com/documentation/foundation/object_runtime/java_support/nsjavawillsetupvirtualmachinenotification)NSLocale.hAdded [NSISO8601Calendar](https://developer.apple.com/documentation/foundation/nsiso8601calendar)Added [NSIndianCalendar](https://developer.apple.com/documentation/foundation/nsindiancalendar)Added [NSPersianCalendar](https://developer.apple.com/documentation/foundation/nspersiancalendar)Added NSTaiwaneseCalendarNSNumberFormatter.hRemoved -[NSNumberFormatter init]Added [+[NSNumberFormatter localizedStringFromNumber:numberStyle:]](https://developer.apple.com/documentation/foundation/numberformatter/1416418-localizedstring)NSObjCRuntime.hAdded NSComparisonResult() (no architecture available)Added [NSEnumerationConcurrent](https://developer.apple.com/documentation/foundation/nsenumerationoptions/nsenumerationconcurrent) (no architecture available)Added [NSEnumerationOptions](https://developer.apple.com/documentation/foundation/nsenumerationoptions) (no architecture available)Added [NSEnumerationReverse](https://developer.apple.com/documentation/foundation/nsenumerationoptions/1395159-reverse) (no architecture available)Added [#def NSFoundationVersionNumber10_5](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_5)Added [#def NSFoundationVersionNumber10_5_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_5_1)Added [NSSortConcurrent](https://developer.apple.com/documentation/foundation/nssortoptions/nssortconcurrent) (no architecture available)Added [NSSortOptions](https://developer.apple.com/documentation/foundation/nssortoptions) (no architecture available)Added [NSSortStable](https://developer.apple.com/documentation/foundation/nssortoptions/1395062-stable) (no architecture available)Added #def NS_BLOCKS_AVAILABLEAdded obj2 (no architecture available)NSObject.hAdded [NSDiscardableContent](https://developer.apple.com/documentation/foundation/nsdiscardablecontent)Added [-[NSDiscardableContent beginContentAccess]](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/1412187-begincontentaccess)Added [-[NSDiscardableContent discardContentIfPossible]](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/1408998-discardcontentifpossible)Added [-[NSDiscardableContent endContentAccess]](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/1407535-endcontentaccess)Added [-[NSDiscardableContent isContentDiscarded]](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/1417470-iscontentdiscarded)Added [-[NSObject autoContentAccessingProxy]](https://developer.apple.com/documentation/objectivec/nsobject/1409224-autocontentaccessingproxy)Added [-[NSObject forwardingTargetForSelector:]](https://developer.apple.com/documentation/objectivec/nsobject/1418855-forwardingtarget)Added NSObject(NSDiscardableContentProxy)NSOrthography.hAdded [NSOrthography](https://developer.apple.com/documentation/foundation/nsorthography)Added [NSOrthography.allLanguages](https://developer.apple.com/documentation/foundation/nsorthography/1416205-alllanguages)Added [NSOrthography.allScripts](https://developer.apple.com/documentation/foundation/nsorthography/1410722-allscripts)Added [NSOrthography.dominantLanguage](https://developer.apple.com/documentation/foundation/nsorthography/1415229-dominantlanguage)Added [-[NSOrthography dominantLanguageForScript:]](https://developer.apple.com/documentation/foundation/nsorthography/1407326-dominantlanguage)Added [NSOrthography.dominantScript](https://developer.apple.com/documentation/foundation/nsorthography/1407965-dominantscript)Added [-[NSOrthography initWithDominantScript:languageMap:]](https://developer.apple.com/documentation/foundation/nsorthography/1408708-init)Added [NSOrthography.languageMap](https://developer.apple.com/documentation/foundation/nsorthography/1409533-languagemap)Added [-[NSOrthography languagesForScript:]](https://developer.apple.com/documentation/foundation/nsorthography/1412606-languages)Added [+[NSOrthography orthographyWithDominantScript:languageMap:]](https://developer.apple.com/documentation/foundation/nsorthography/1585529-orthographywithdominantscript)Added NSOrthography(NSOrthographyCreation)Added NSOrthography(NSOrthographyExtended)NSPredicate.hAdded [+[NSPredicate predicateWithBlock:]](https://developer.apple.com/documentation/foundation/nspredicate/1416182-init) (no architecture available)NSProcessInfo.hAdded [-[NSProcessInfo disableSuddenTermination]](https://developer.apple.com/documentation/foundation/processinfo/1412841-disablesuddentermination)Added [-[NSProcessInfo enableSuddenTermination]](https://developer.apple.com/documentation/foundation/processinfo/1409836-enablesuddentermination)Added [-[NSProcessInfo systemUptime]](https://developer.apple.com/documentation/foundation/processinfo/1414553-systemuptime)NSPropertyList.hAdded [+[NSPropertyListSerialization dataWithPropertyList:format:options:error:]](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1418309-datawithpropertylist)Added [+[NSPropertyListSerialization propertyListWithData:options:format:error:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1409678-propertylist)Added [+[NSPropertyListSerialization propertyListWithStream:options:format:error:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1415468-propertylist)Added [+[NSPropertyListSerialization writePropertyList:toStream:format:options:error:]](https://developer.apple.com/documentation/foundation/propertylistserialization/1407862-writepropertylist)Added [NSPropertyListReadOptions](https://developer.apple.com/documentation/foundation/nspropertylistreadoptions)Added [NSPropertyListWriteOptions](https://developer.apple.com/documentation/foundation/propertylistserialization/writeoptions)NSSet.hAdded [-[NSSet enumerateObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsset/1418129-enumerateobjectsusingblock) (no architecture available)Added [-[NSSet enumerateObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsset/1412024-enumerateobjectswithoptions) (no architecture available)NSSortDescriptor.hAdded [-[NSSortDescriptor comparator]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1411426-comparator) (no architecture available)Added [-[NSSortDescriptor initWithKey:ascending:comparator:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1411607-init) (no architecture available)Added [+[NSSortDescriptor sortDescriptorWithKey:ascending:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1503726-sortdescriptorwithkey)Added [+[NSSortDescriptor sortDescriptorWithKey:ascending:comparator:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1503734-sortdescriptorwithkey) (no architecture available)Added [+[NSSortDescriptor sortDescriptorWithKey:ascending:selector:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1503730-sortdescriptorwithkey)NSString.hAdded [-[NSString enumerateLinesUsingBlock:]](https://developer.apple.com/documentation/foundation/nsstring/1408459-enumeratelinesusingblock) (no architecture available)Added [-[NSString enumerateSubstringsInRange:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsstring/1416774-enumeratesubstringsinrange) (no architecture available)Added [NSStringEnumerationByComposedCharacterSequences](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1407290-bycomposedcharactersequences) (no architecture available)Added [NSStringEnumerationByLines](https://developer.apple.com/documentation/foundation/nsstringenumerationoptions/nsstringenumerationbylines) (no architecture available)Added [NSStringEnumerationByParagraphs](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1409744-byparagraphs) (no architecture available)Added [NSStringEnumerationBySentences](https://developer.apple.com/documentation/foundation/nsstringenumerationoptions/nsstringenumerationbysentences) (no architecture available)Added [NSStringEnumerationByWords](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1407663-bywords) (no architecture available)Added [NSStringEnumerationLocalized](https://developer.apple.com/documentation/foundation/nsstringenumerationoptions/nsstringenumerationlocalized) (no architecture available)Added [NSStringEnumerationOptions](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions) (no architecture available)Added [NSStringEnumerationReverse](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/1412250-reverse) (no architecture available)Added [NSStringEnumerationSubstringNotRequired](https://developer.apple.com/documentation/foundation/nsstringenumerationoptions/nsstringenumerationsubstringnotrequired) (no architecture available)NSTextCheckingResult.hAdded [NSTextCheckingResult](https://developer.apple.com/documentation/foundation/nstextcheckingresult)Added [NSTextCheckingResult.URL](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1417843-url)Added [+[NSTextCheckingResult addressCheckingResultWithRange:components:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413828-addresscheckingresult)Added [NSTextCheckingResult.addressComponents](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413728-addresscomponents)Added [+[NSTextCheckingResult correctionCheckingResultWithRange:replacementString:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415946-correctioncheckingresultwithrang)Added [+[NSTextCheckingResult dashCheckingResultWithRange:replacementString:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1409525-dashcheckingresult)Added [NSTextCheckingResult.date](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1414289-date)Added [+[NSTextCheckingResult dateCheckingResultWithRange:date:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1410401-datecheckingresult)Added [+[NSTextCheckingResult grammarCheckingResultWithRange:details:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407190-grammarcheckingresult)Added [NSTextCheckingResult.grammarDetails](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1408959-grammardetails)Added [+[NSTextCheckingResult linkCheckingResultWithRange:URL:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413056-linkcheckingresult)Added [NSTextCheckingResult.orthography](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1414551-orthography)Added [+[NSTextCheckingResult orthographyCheckingResultWithRange:orthography:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415506-orthographycheckingresultwithran)Added [+[NSTextCheckingResult quoteCheckingResultWithRange:replacementString:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413783-quotecheckingresult)Added [NSTextCheckingResult.range](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415852-range)Added [+[NSTextCheckingResult replacementCheckingResultWithRange:replacementString:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1416651-replacementcheckingresult)Added [NSTextCheckingResult.replacementString](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1412681-replacementstring)Added [NSTextCheckingResult.resultType](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407779-resulttype)Added [+[NSTextCheckingResult spellCheckingResultWithRange:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1416255-spellcheckingresultwithrange)Added [NSTextCheckingAllCustomTypes](https://developer.apple.com/documentation/foundation/nstextcheckingallcustomtypes)Added [NSTextCheckingAllSystemTypes](https://developer.apple.com/documentation/foundation/1476845-anonymous/nstextcheckingallsystemtypes)Added [NSTextCheckingAllTypes](https://developer.apple.com/documentation/foundation/1476845-anonymous/nstextcheckingalltypes)Added [NSTextCheckingCityKey](https://developer.apple.com/documentation/foundation/nstextcheckingcitykey)Added [NSTextCheckingCountryKey](https://developer.apple.com/documentation/foundation/nstextcheckingcountrykey)Added [NSTextCheckingJobTitleKey](https://developer.apple.com/documentation/foundation/nstextcheckingkey/1416460-jobtitle)Added [NSTextCheckingNameKey](https://developer.apple.com/documentation/foundation/nstextcheckingnamekey)Added [NSTextCheckingOrganizationKey](https://developer.apple.com/documentation/foundation/nstextcheckingkey/1415671-organization)Added [NSTextCheckingPhoneKey](https://developer.apple.com/documentation/foundation/nstextcheckingphonekey)Added NSTextCheckingResult(NSTextCheckingResultCreation)Added NSTextCheckingResult(NSTextCheckingResultOptional)Added [NSTextCheckingStateKey](https://developer.apple.com/documentation/foundation/nstextcheckingkey/1411629-state)Added [NSTextCheckingStreetKey](https://developer.apple.com/documentation/foundation/nstextcheckingkey/1409986-street)Added [NSTextCheckingType](https://developer.apple.com/documentation/foundation/nstextcheckingtype)Added [NSTextCheckingTypeAddress](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/1408236-address)Added [NSTextCheckingTypeCorrection](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/1407319-correction)Added [NSTextCheckingTypeDash](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/1414568-dash)Added [NSTextCheckingTypeDate](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/1416011-date)Added [NSTextCheckingTypeGrammar](https://developer.apple.com/documentation/foundation/nstextcheckingtype/nstextcheckingtypegrammar)Added [NSTextCheckingTypeLink](https://developer.apple.com/documentation/foundation/nstextcheckingtype/nstextcheckingtypelink)Added [NSTextCheckingTypeOrthography](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/1409704-orthography)Added [NSTextCheckingTypeQuote](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/1411424-quote)Added [NSTextCheckingTypeReplacement](https://developer.apple.com/documentation/foundation/nstextcheckingtype/nstextcheckingtypereplacement)Added [NSTextCheckingTypeSpelling](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/1410170-spelling)Added [NSTextCheckingTypes](https://developer.apple.com/documentation/foundation/nstextcheckingtypes)Added [NSTextCheckingZIPKey](https://developer.apple.com/documentation/foundation/nstextcheckingkey/1414844-zip)NSTimeZone.hAdded +[NSTimeZone setAbbreviationDictionary:]NSURL.hAdded [+[NSURL URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:]](https://developer.apple.com/documentation/foundation/nsurl/1572035-urlbyresolvingbookmarkdata)Added [-[NSURL bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:]](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions)Added [-[NSURL checkResourceIsReachableAndReturnError:]](https://developer.apple.com/documentation/foundation/nsurl/1410597-checkresourceisreachableandretur)Added [-[NSURL filePathURL]](https://developer.apple.com/documentation/foundation/nsurl/1408442-filepathurl)Added [-[NSURL fileReferenceURL]](https://developer.apple.com/documentation/foundation/nsurl/1408631-filereferenceurl)Added [-[NSURL getResourceValue:forKey:error:]](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue)Added [-[NSURL initByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:]](https://developer.apple.com/documentation/foundation/nsurl/1413475-init)Added [-[NSURL isFileReferenceURL]](https://developer.apple.com/documentation/foundation/nsurl/1408507-isfilereferenceurl)Added [-[NSURL resourceValuesForKeys:error:]](https://developer.apple.com/documentation/foundation/nsurl/1417657-resourcevalues)Added [+[NSURL resourceValuesForKeys:fromBookmarkData:]](https://developer.apple.com/documentation/foundation/nsurl/1418097-resourcevaluesforkeys)Added [-[NSURL setResourceValue:forKey:error:]](https://developer.apple.com/documentation/foundation/nsurl/1413819-setresourcevalue)Added [-[NSURL setResourceValues:error:]](https://developer.apple.com/documentation/foundation/nsurl/1408208-setresourcevalues)Added [NSURLAttributeModificationDateKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1407860-attributemodificationdatekey)Added [NSURLBookmarkCreationMinimalBookmark](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/1409050-minimalbookmark)Added [NSURLBookmarkCreationOptions](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions)Added [NSURLBookmarkCreationPreferFileIDResolution](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationpreferfileidresolution)Added [NSURLBookmarkResolutionOptions](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions)Added [NSURLBookmarkResolutionWithoutMounting](https://developer.apple.com/documentation/foundation/nsurlbookmarkresolutionoptions/nsurlbookmarkresolutionwithoutmounting)Added [NSURLBookmarkResolutionWithoutUI](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/1408876-withoutui)Added [NSURLContentAccessDateKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1408314-contentaccessdatekey)Added [NSURLContentModificationDateKey](https://developer.apple.com/documentation/foundation/nsurlcontentmodificationdatekey)Added [NSURLCreationDateKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1410073-creationdatekey)Added [NSURLCustomIconKey](https://developer.apple.com/documentation/foundation/nsurlcustomiconkey)Added [NSURLEffectiveIconKey](https://developer.apple.com/documentation/foundation/nsurleffectiveiconkey)Added [NSURLFileAllocatedSizeKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1409814-fileallocatedsizekey)Added [NSURLFileSizeKey](https://developer.apple.com/documentation/foundation/nsurlfilesizekey)Added [NSURLHasHiddenExtensionKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415558-hashiddenextensionkey)Added [NSURLIsDirectoryKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1410514-isdirectorykey)Added [NSURLIsHiddenKey](https://developer.apple.com/documentation/foundation/nsurlishiddenkey)Added [NSURLIsPackageKey](https://developer.apple.com/documentation/foundation/nsurlispackagekey)Added [NSURLIsRegularFileKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415194-isregularfilekey)Added [NSURLIsSymbolicLinkKey](https://developer.apple.com/documentation/foundation/nsurlissymboliclinkkey)Added [NSURLIsSystemImmutableKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1412518-issystemimmutablekey)Added [NSURLIsUserImmutableKey](https://developer.apple.com/documentation/foundation/nsurlisuserimmutablekey)Added [NSURLIsVolumeKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1411744-isvolumekey)Added [NSURLLabelColorKey](https://developer.apple.com/documentation/foundation/nsurllabelcolorkey)Added [NSURLLabelNumberKey](https://developer.apple.com/documentation/foundation/nsurllabelnumberkey)Added [NSURLLinkCountKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416647-linkcountkey)Added [NSURLLocalizedLabelKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1413879-localizedlabelkey)Added [NSURLLocalizedNameKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1412706-localizednamekey)Added [NSURLLocalizedTypeDescriptionKey](https://developer.apple.com/documentation/foundation/nsurllocalizedtypedescriptionkey)Added [NSURLNameKey](https://developer.apple.com/documentation/foundation/nsurlnamekey)Added [NSURLParentDirectoryURLKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1412731-parentdirectoryurlkey)Added [NSURLTypeIdentifierKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416354-typeidentifierkey)Added [NSURLVolumeAvailableCapacityKey](https://developer.apple.com/documentation/foundation/nsurlvolumeavailablecapacitykey)Added [NSURLVolumeIsJournalingKey](https://developer.apple.com/documentation/foundation/nsurlvolumeisjournalingkey)Added [NSURLVolumeLocalizedFormatDescriptionKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1417503-volumelocalizedformatdescription)Added [NSURLVolumeResourceCountKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1414852-volumeresourcecountkey)Added [NSURLVolumeSupportsCasePreservedNamesKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416422-volumesupportscasepreservednames)Added [NSURLVolumeSupportsCaseSensitiveNamesKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportscasesensitivenameskey)Added [NSURLVolumeSupportsHardLinksKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportshardlinkskey)Added [NSURLVolumeSupportsJournalingKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportsjournalingkey)Added [NSURLVolumeSupportsPersistentIDsKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportspersistentidskey)Added [NSURLVolumeSupportsSparseFilesKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1409702-volumesupportssparsefileskey)Added [NSURLVolumeSupportsSymbolicLinksKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportssymboliclinkskey)Added [NSURLVolumeSupportsZeroRunsKey](https://developer.apple.com/documentation/foundation/nsurlvolumesupportszerorunskey)Added [NSURLVolumeTotalCapacityKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1415933-volumetotalcapacitykey)Added [NSURLVolumeURLKey](https://developer.apple.com/documentation/foundation/nsurlvolumeurlkey)

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
