---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/Foundation.html
archived_at: '2026-07-18T02:51:49.121991Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Foundation Changes

## Foundation

FoundationErrors.hAdded [NSUserActivityConnectionUnavailableError](https://developer.apple.com/documentation/foundation/nsuseractivityconnectionunavailableerror)Added [NSUserActivityErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsuseractivityerrormaximum)Added [NSUserActivityErrorMinimum](https://developer.apple.com/documentation/foundation/nsuseractivityerrorminimum)Added [NSUserActivityHandoffFailedError](https://developer.apple.com/documentation/foundation/nsuseractivityhandofffailederror)Added [NSUserActivityHandoffUserInfoTooLargeError](https://developer.apple.com/documentation/foundation/nsuseractivityhandoffuserinfotoolargeerror)Added [NSUserActivityRemoteApplicationTimedOutError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsuseractivityremoteapplicationtimedouterror)NSAffineTransform.hModified [-[NSAffineTransform init]](https://developer.apple.com/documentation/foundation/nsaffinetransform/1411498-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSAppleEventDescriptor.hModified [-[NSAppleEventDescriptor initWithAEDescNoCopy:]](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/1415233-initwithaedescnocopy)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSAppleScript.hModified [-[NSAppleScript initWithContentsOfURL:error:]](https://developer.apple.com/documentation/foundation/nsapplescript/1412508-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSAppleScript initWithSource:]](https://developer.apple.com/documentation/foundation/nsapplescript/1414313-initwithsource)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSArchiver.hModified [-[NSArchiver initForWritingWithMutableData:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArchiver/Description.html#//apple_ref/occ/instm/NSArchiver/initForWritingWithMutableData:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSUnarchiver initForReadingWithData:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUnarchiver/Description.html#//apple_ref/occ/instm/NSUnarchiver/initForReadingWithData:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSArray.hModified [-[NSArray init]](https://developer.apple.com/documentation/foundation/nsarray/1414315-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSArray initWithCoder:]](https://developer.apple.com/documentation/foundation/nsarray/1407810-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

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

Modified [-[NSMutableArray initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1409527-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSBackgroundActivityScheduler.hModified [-[NSBackgroundActivityScheduler initWithIdentifier:]](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1407482-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSBundle.hModified [-[NSBundle initWithPath:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/initWithPath:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSCalendar.hModified [-[NSCalendar initWithCalendarIdentifier:]](https://developer.apple.com/documentation/foundation/nscalendar/1415991-initwithcalendaridentifier)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSCharacterSet.hModified [-[NSCharacterSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nscharacterset/1408497-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDate.hModified [-[NSDate init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDate initWithCoder:]](https://developer.apple.com/documentation/foundation/nsdate/1412602-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDate initWithTimeIntervalSinceReferenceDate:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/instm/NSDate/initWithTimeIntervalSinceReferenceDate:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDecimalNumber.hModified [-[NSDecimalNumber initWithDecimal:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/instm/NSDecimalNumber/initWithDecimal:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDecimalNumberHandler initWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumberHandler/Description.html#//apple_ref/occ/instm/NSDecimalNumberHandler/initWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDictionary.hModified [-[NSDictionary init]](https://developer.apple.com/documentation/foundation/nsdictionary/1418147-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDictionary initWithCoder:]](https://developer.apple.com/documentation/foundation/nsdictionary/1417987-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

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

Modified [-[NSMutableDictionary initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1418255-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDistantObject.hModified [-[NSDistantObject initWithCoder:]](https://developer.apple.com/documentation/foundation/nsdistantobject/1442605-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSDistributedLock.hModified [-[NSDistributedLock initWithPath:]](https://developer.apple.com/documentation/foundation/nsdistributedlock/1410387-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSError.hModified [-[NSError initWithDomain:code:userInfo:]](https://developer.apple.com/documentation/foundation/nserror/1417063-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSException.hModified [-[NSException initWithName:reason:userInfo:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/instm/NSException/initWithName:reason:userInfo:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSExtensionContext.hRemoved NSExtensionBackgroundTaskIdentifierNSFileCoordinator.hModified [-[NSFileCoordinator initWithFilePresenter:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1416795-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSFileHandle.hModified [-[NSFileHandle initWithCoder:]](https://developer.apple.com/documentation/foundation/filehandle/1411174-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileHandle initWithFileDescriptor:closeOnDealloc:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1408522-initwithfiledescriptor)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSFileWrapper.hModified [-[NSFileWrapper initDirectoryWithFileWrappers:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415121-initdirectorywithfilewrappers)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileWrapper initRegularFileWithContents:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1409508-initregularfilewithcontents)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileWrapper initSymbolicLinkWithDestinationURL:]](https://developer.apple.com/documentation/foundation/filewrapper/1415098-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileWrapper initWithCoder:]](https://developer.apple.com/documentation/foundation/filewrapper/1416358-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileWrapper initWithSerializedRepresentation:]](https://developer.apple.com/documentation/foundation/filewrapper/1407515-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSFileWrapper initWithURL:options:error:]](https://developer.apple.com/documentation/foundation/filewrapper/1415658-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSGarbageCollector.hModified [-[NSGarbageCollector collectExhaustively]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431022-collectexhaustively)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSGarbageCollector collectIfNeeded]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431015-collectifneeded)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[NSGarbageCollector defaultCollector]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431012-defaultcollector)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSGarbageCollector disable]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431016-disable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSGarbageCollector disableCollectorForPointer:]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431013-disablecollectorforpointer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSGarbageCollector enable]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431020-enable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSGarbageCollector enableCollectorForPointer:]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431017-enablecollectorforpointer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSGarbageCollector isEnabled]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431014-isenabled)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[NSGarbageCollector zone]](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431011-zone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

NSGeometry.hAdded [NSValue.edgeInsetsValue](https://developer.apple.com/documentation/foundation/nsvalue/1391123-edgeinsetsvalue)Added [+[NSValue valueWithEdgeInsets:]](https://developer.apple.com/documentation/foundation/nsvalue/1391181-init)Added #def NSEDGEINSETS_DEFINEDAdded [NSEdgeInsetsEqual()](https://developer.apple.com/documentation/foundation/1391230-nsedgeinsetsequal)Added [NSEdgeInsetsZero](https://developer.apple.com/documentation/foundation/nsedgeinsetszero)Modified [NSEdgeInsets](https://developer.apple.com/documentation/foundation/nsedgeinsets)

|  | Header |
| --- | --- |
| From | AppKit/NSLayoutConstraint.h |
| To | Foundation/NSGeometry.h |

Modified [NSEdgeInsetsMake()](https://developer.apple.com/documentation/foundation/1391130-nsedgeinsetsmake)

|  | Header |
| --- | --- |
| From | AppKit/NSLayoutConstraint.h |
| To | Foundation/NSGeometry.h |

NSHashTable.hModified [-[NSHashTable initWithOptions:capacity:]](https://developer.apple.com/documentation/foundation/nshashtable/1411066-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSHashTable initWithPointerFunctions:capacity:]](https://developer.apple.com/documentation/foundation/nshashtable/1416331-initwithpointerfunctions)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSIndexPath.hModified [-[NSIndexPath initWithIndexes:length:]](https://developer.apple.com/documentation/foundation/nsindexpath/1416906-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSIndexSet.hModified [-[NSIndexSet initWithIndexSet:]](https://developer.apple.com/documentation/foundation/nsindexset/1415602-initwithindexset)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSIndexSet initWithIndexesInRange:]](https://developer.apple.com/documentation/foundation/nsindexset/1414013-initwithindexesinrange)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSItemProvider.hRemoved [NSExtensionJavaScriptFinalizeArgumentKey](https://developer.apple.com/documentation/foundation/nsextensionjavascriptfinalizeargumentkey)Modified [-[NSItemProvider initWithItem:typeIdentifier:]](https://developer.apple.com/documentation/foundation/nsitemprovider/1403933-initwithitem)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSLinguisticTagger.hModified [-[NSLinguisticTagger initWithTagSchemes:options:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1414576-initwithtagschemes)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSLocale.hModified [-[NSLocale initWithCoder:]](https://developer.apple.com/documentation/foundation/nslocale/1415424-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLocale initWithLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1414217-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSLock.hModified [-[NSConditionLock initWithCondition:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/instm/NSConditionLock/initWithCondition:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSMapTable.hModified [-[NSMapTable initWithKeyOptions:valueOptions:capacity:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391382-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMapTable initWithKeyPointerFunctions:valuePointerFunctions:capacity:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391429-initwithkeypointerfunctions)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSMetadata.hModified [-[NSMetadataItem initWithURL:]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1414919-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSNotification.hModified [-[NSNotification initWithCoder:]](https://developer.apple.com/documentation/foundation/nsnotification/1412464-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNotification initWithName:object:userInfo:]](https://developer.apple.com/documentation/foundation/nsnotification/1415764-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSNotificationQueue.hModified [-[NSNotificationQueue initWithNotificationCenter:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/instm/NSNotificationQueue/initWithNotificationCenter:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSObjCRuntime.hAdded #def NS_ASSUME_NONNULL_BEGINAdded #def NS_ASSUME_NONNULL_ENDNSOperation.hModified [-[NSInvocationOperation initWithInvocation:]](https://developer.apple.com/documentation/foundation/nsinvocationoperation/1543647-initwithinvocation)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSOrderedSet.hModified [-[NSMutableOrderedSet init]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410545-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableOrderedSet initWithCapacity:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411583-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableOrderedSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1413074-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOrderedSet init]](https://developer.apple.com/documentation/foundation/nsorderedset/1417735-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOrderedSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417543-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOrderedSet initWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411910-initwithobjects)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSOrthography.hModified [-[NSOrthography initWithCoder:]](https://developer.apple.com/documentation/foundation/nsorthography/1408410-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOrthography initWithDominantScript:languageMap:]](https://developer.apple.com/documentation/foundation/nsorthography/1408708-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSPointerArray.hModified [-[NSPointerArray initWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1408229-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPointerArray initWithPointerFunctions:]](https://developer.apple.com/documentation/foundation/nspointerarray/1416727-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSPointerFunctions.hModified [-[NSPointerFunctions initWithOptions:]](https://developer.apple.com/documentation/foundation/nspointerfunctions/1417715-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSPort.hModified [-[NSMachPort initWithMachPort:options:]](https://developer.apple.com/documentation/foundation/nsmachport/1399559-initwithmachport)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSocketPort initRemoteWithProtocolFamily:socketType:protocol:address:]](https://developer.apple.com/documentation/foundation/nssocketport/1399535-initremotewithprotocolfamily)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSocketPort initWithProtocolFamily:socketType:protocol:address:]](https://developer.apple.com/documentation/foundation/nssocketport/1399497-initwithprotocolfamily)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSocketPort initWithProtocolFamily:socketType:protocol:socket:]](https://developer.apple.com/documentation/foundation/nssocketport/1399484-initwithprotocolfamily)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSPortMessage.hModified [-[NSPortMessage initWithSendPort:receivePort:components:]](https://developer.apple.com/documentation/foundation/portmessage/1417387-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSProcessInfo.hAdded [NSProcessInfo.thermalState](https://developer.apple.com/documentation/foundation/processinfo/1417480-thermalstate)Added [NSProcessInfoThermalState](https://developer.apple.com/documentation/foundation/nsprocessinfothermalstate)Added [NSProcessInfoThermalStateCritical](https://developer.apple.com/documentation/foundation/processinfo/thermalstate/critical)Added [NSProcessInfoThermalStateDidChangeNotification](https://developer.apple.com/documentation/foundation/nsprocessinfothermalstatedidchangenotification)Added [NSProcessInfoThermalStateFair](https://developer.apple.com/documentation/foundation/nsprocessinfothermalstate/nsprocessinfothermalstatefair)Added [NSProcessInfoThermalStateNominal](https://developer.apple.com/documentation/foundation/processinfo/thermalstate/nominal)Added [NSProcessInfoThermalStateSerious](https://developer.apple.com/documentation/foundation/processinfo/thermalstate/serious)NSProgress.hModified [-[NSProgress initWithParent:userInfo:]](https://developer.apple.com/documentation/foundation/progress/1409133-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSRegularExpression.hModified [-[NSDataDetector initWithTypes:error:]](https://developer.apple.com/documentation/foundation/nsdatadetector/1409829-initwithtypes)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSRegularExpression initWithPattern:options:error:]](https://developer.apple.com/documentation/foundation/nsregularexpression/1410900-initwithpattern)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSScanner.hModified [-[NSScanner initWithString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/initWithString:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSScriptClassDescription.hModified [-[NSScriptClassDescription initWithSuiteName:className:dictionary:]](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/1410370-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSScriptCommand.hModified [-[NSScriptCommand initWithCommandDescription:]](https://developer.apple.com/documentation/foundation/nsscriptcommand/1413516-initwithcommanddescription)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSScriptCommandDescription.hModified [-[NSScriptCommandDescription initWithCoder:]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1416525-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSScriptCommandDescription initWithSuiteName:commandName:dictionary:]](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/1410038-initwithsuitename)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSScriptObjectSpecifiers.hModified [-[NSIndexSpecifier initWithContainerClassDescription:containerSpecifier:key:index:]](https://developer.apple.com/documentation/foundation/nsindexspecifier/1407502-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNameSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsnamespecifier/1412623-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNameSpecifier initWithContainerClassDescription:containerSpecifier:key:name:]](https://developer.apple.com/documentation/foundation/nsnamespecifier/1408615-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSPositionalSpecifier initWithPosition:objectSpecifier:]](https://developer.apple.com/documentation/foundation/nspositionalspecifier/1416546-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSRangeSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1418021-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSRangeSpecifier initWithContainerClassDescription:containerSpecifier:key:startSpecifier:endSpecifier:]](https://developer.apple.com/documentation/foundation/nsrangespecifier/1409215-initwithcontainerclassdescriptio)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSRelativeSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1412403-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSRelativeSpecifier initWithContainerClassDescription:containerSpecifier:key:relativePosition:baseSpecifier:]](https://developer.apple.com/documentation/foundation/nsrelativespecifier/1409205-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSScriptObjectSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1408941-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSScriptObjectSpecifier initWithContainerClassDescription:containerSpecifier:key:]](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/1410480-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSUniqueIDSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/1414481-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSUniqueIDSpecifier initWithContainerClassDescription:containerSpecifier:key:uniqueID:]](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/1416055-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWhoseSpecifier initWithCoder:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1418262-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSWhoseSpecifier initWithContainerClassDescription:containerSpecifier:key:test:]](https://developer.apple.com/documentation/foundation/nswhosespecifier/1412173-initwithcontainerclassdescriptio)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSScriptWhoseTests.hModified [-[NSLogicalTest initAndTestWithTests:]](https://developer.apple.com/documentation/foundation/nslogicaltest/1393854-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLogicalTest initNotTestWithTest:]](https://developer.apple.com/documentation/foundation/nslogicaltest/1393879-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSLogicalTest initOrTestWithTests:]](https://developer.apple.com/documentation/foundation/nslogicaltest/1393875-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSScriptWhoseTest init]](https://developer.apple.com/documentation/foundation/nsscriptwhosetest/1393856-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSScriptWhoseTest initWithCoder:]](https://developer.apple.com/documentation/foundation/nsscriptwhosetest/1393846-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpecifierTest initWithCoder:]](https://developer.apple.com/documentation/foundation/nsspecifiertest/1393881-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSpecifierTest initWithObjectSpecifier:comparisonOperator:testObject:]](https://developer.apple.com/documentation/foundation/nsspecifiertest/1393833-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSSet.hModified [-[NSMutableSet init]](https://developer.apple.com/documentation/foundation/nsmutableset/1414518-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableSet initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/initWithCapacity:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMutableSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsmutableset/1407369-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSet init]](https://developer.apple.com/documentation/foundation/nsset/1409698-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSet initWithCoder:]](https://developer.apple.com/documentation/foundation/nsset/1408221-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSStream.hModified [-[NSInputStream initWithData:]](https://developer.apple.com/documentation/foundation/nsinputstream/1412470-initwithdata)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSInputStream initWithURL:]](https://developer.apple.com/documentation/foundation/inputstream/1417891-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutputStream initToBuffer:capacity:]](https://developer.apple.com/documentation/foundation/outputstream/1410805-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutputStream initToMemory]](https://developer.apple.com/documentation/foundation/outputstream/1409909-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSOutputStream initWithURL:append:]](https://developer.apple.com/documentation/foundation/outputstream/1414446-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSString.hModified [-[NSString init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSString initWithCoder:]](https://developer.apple.com/documentation/foundation/nsstring/1407488-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSTask.hModified [-[NSTask init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/instm/NSTask/init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSThread.hModified [-[NSThread init]](https://developer.apple.com/documentation/foundation/nsthread/1416464-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSTimer.hModified [-[NSTimer initWithFireDate:interval:target:selector:userInfo:repeats:]](https://developer.apple.com/documentation/foundation/nstimer/1415700-initwithfiredate)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSURL.hModified [-[NSFileSecurity initWithCoder:]](https://developer.apple.com/documentation/foundation/nsfilesecurity/1418382-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURL initFileURLWithFileSystemRepresentation:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1411210-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURL initFileURLWithPath:]](https://developer.apple.com/documentation/foundation/nsurl/1410301-initfileurlwithpath)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURL initFileURLWithPath:isDirectory:]](https://developer.apple.com/documentation/foundation/nsurl/1417505-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURL initWithString:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1417949-initwithstring)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSURLQueryItem initWithName:value:]](https://developer.apple.com/documentation/foundation/nsurlqueryitem/1410963-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSUUID.hModified [-[NSUUID init]](https://developer.apple.com/documentation/foundation/nsuuid/1415797-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSUserDefaults.hModified [-[NSUserDefaults initWithSuiteName:]](https://developer.apple.com/documentation/foundation/userdefaults/1409957-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSUserNotification.hModified [-[NSUserNotification init]](https://developer.apple.com/documentation/foundation/nsusernotification/1410841-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSUserScriptTask.hModified [-[NSUserScriptTask initWithURL:error:]](https://developer.apple.com/documentation/foundation/nsuserscripttask/1409998-initwithurl)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSValue.hModified [-[NSNumber initWithBool:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithBool:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithChar:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithChar:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithCoder:]](https://developer.apple.com/documentation/foundation/nsnumber/1411476-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithDouble:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithDouble:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithFloat:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithFloat:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithInt:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithInteger:]](https://developer.apple.com/documentation/foundation/nsnumber/1409397-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithLong:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithLongLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithLongLong:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithShort:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithShort:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithUnsignedChar:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedChar:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithUnsignedInt:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedInt:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithUnsignedInteger:]](https://developer.apple.com/documentation/foundation/nsnumber/1412531-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithUnsignedLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedLong:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithUnsignedLongLong:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedLongLong:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNumber initWithUnsignedShort:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithUnsignedShort:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSValue initWithBytes:objCType:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/initWithBytes:objCType:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSValue initWithCoder:]](https://developer.apple.com/documentation/foundation/nsvalue/1417896-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSXMLDTD.hModified [-[NSXMLDTD init]](https://developer.apple.com/documentation/foundation/xmldtd/1417840-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLDTD initWithData:options:error:]](https://developer.apple.com/documentation/foundation/xmldtd/1412807-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSXMLDTDNode.hModified [-[NSXMLDTDNode init]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1416018-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLDTDNode initWithKind:options:]](https://developer.apple.com/documentation/foundation/xmldtdnode/1408553-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLDTDNode initWithXMLString:]](https://developer.apple.com/documentation/foundation/nsxmldtdnode/1409605-initwithxmlstring)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSXMLDocument.hModified [-[NSXMLDocument init]](https://developer.apple.com/documentation/foundation/nsxmldocument/1415210-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLDocument initWithData:options:error:]](https://developer.apple.com/documentation/foundation/xmldocument/1413086-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLDocument initWithRootElement:]](https://developer.apple.com/documentation/foundation/nsxmldocument/1409062-initwithrootelement)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSXMLElement.hModified [-[NSXMLElement initWithName:URI:]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388348-initwithname)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLElement initWithXMLString:error:]](https://developer.apple.com/documentation/foundation/nsxmlelement/1388325-initwithxmlstring)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSXMLNode.hModified [-[NSXMLNode init]](https://developer.apple.com/documentation/foundation/nsxmlnode/1409780-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLNode initWithKind:options:]](https://developer.apple.com/documentation/foundation/xmlnode/1409747-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

NSXMLParser.hAdded [NSXMLParser.allowedExternalEntityURLs](https://developer.apple.com/documentation/foundation/nsxmlparser/1412380-allowedexternalentityurls)Added [NSXMLParser.externalEntityResolvingPolicy](https://developer.apple.com/documentation/foundation/xmlparser/1407399-externalentityresolvingpolicy)Added [NSXMLParserExternalEntityResolvingPolicy](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy)Added [NSXMLParserResolveExternalEntitiesAlways](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/always)Added [NSXMLParserResolveExternalEntitiesNever](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/never)Added [NSXMLParserResolveExternalEntitiesNoNetwork](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/nonetwork)Added [NSXMLParserResolveExternalEntitiesSameOriginOnly](https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy/sameoriginonly)NSXPCConnection.hModified [-[NSXPCListener initWithMachServiceName:]](https://developer.apple.com/documentation/foundation/nsxpclistener/1414106-init)

|  | Designated Initializer |
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
