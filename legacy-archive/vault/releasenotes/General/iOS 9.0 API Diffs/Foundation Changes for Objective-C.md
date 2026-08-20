---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/Foundation.html
archived_at: '2026-07-18T02:56:32.864324Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Foundation Changes for Objective-C

### Foundation

#### FoundationErrors.h

Added [NSBundleErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleerrormaximum)Added [NSBundleErrorMinimum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleerrorminimum)Added [NSBundleOnDemandResourceExceededMaximumSizeError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleondemandresourceexceededmaximumsizeerror)Added [NSBundleOnDemandResourceInvalidTagError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleondemandresourceinvalidtagerror)Added [NSBundleOnDemandResourceOutOfSpaceError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nsbundleondemandresourceoutofspaceerror)Added [NSCoderErrorMaximum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscodererrormaximum)Added [NSCoderErrorMinimum](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscodererrorminimum)Added [NSCoderReadCorruptError](https://developer.apple.com/documentation/foundation/1448136-nserror_codes/nscoderreadcorrupterror)Added [NSCoderValueNotFoundError](https://developer.apple.com/documentation/foundation/nscodervaluenotfounderror)

#### NSArray.h

Modified [-[NSArray arrayByAddingObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/arrayByAddingObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)arrayByAddingObject:(id)anObject ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)arrayByAddingObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSArray arrayByAddingObjectsFromArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/arrayByAddingObjectsFromArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)arrayByAddingObjectsFromArray:(NSArray *)otherArray ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)arrayByAddingObjectsFromArray:(NSArray<ObjectType> * _Nonnull)otherArray ``` |

Modified [+[NSArray arrayWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithArray:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)arrayWithArray:(NSArray *)array ``` |
| To | ``` + (instancetype _Nonnull)arrayWithArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [+[NSArray arrayWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)arrayWithContentsOfFile:(NSString *)path ``` |
| To | ``` + (NSArray<ObjectType> * _Nullable)arrayWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [+[NSArray arrayWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsarray/1460060-arraywithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)arrayWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (NSArray<ObjectType> * _Nullable)arrayWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [+[NSArray arrayWithObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObject:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)arrayWithObject:(id)anObject ``` |
| To | ``` + (instancetype _Nonnull)arrayWithObject:(ObjectType _Nonnull)anObject ``` |

Modified [+[NSArray arrayWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObjects:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)arrayWithObjects:(id)firstObj, ... ``` |
| To | ``` + (instancetype _Nonnull)arrayWithObjects:(ObjectType _Nonnull)firstObj, ... ``` |

Modified [+[NSArray arrayWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/clm/NSArray/arrayWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)arrayWithObjects:(const id [])objects count:(NSUInteger)cnt ``` |
| To | ``` + (instancetype _Nonnull)arrayWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |

Modified [-[NSArray containsObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/containsObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsObject:(id)anObject ``` |
| To | ``` - (BOOL)containsObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSArray enumerateObjectsAtIndexes:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsarray/1417577-enumerateobjectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsAtIndexes:(NSIndexSet *)s options:(NSEnumerationOptions)opts usingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsAtIndexes:(NSIndexSet * _Nonnull)s options:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [-[NSArray enumerateObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsarray/1415846-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsUsingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsUsingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [-[NSArray enumerateObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsarray/1413010-enumerateobjectswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [NSArray.firstObject](https://developer.apple.com/documentation/foundation/nsarray/1412852-firstobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id firstObject ``` |
| To | ``` @property(nonatomic, readonly, nullable) ObjectType firstObject ``` |

Modified [-[NSArray firstObjectCommonWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/firstObjectCommonWithArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)firstObjectCommonWithArray:(NSArray *)otherArray ``` |
| To | ``` - (ObjectType _Nullable)firstObjectCommonWithArray:(NSArray<ObjectType> * _Nonnull)otherArray ``` |

Modified [-[NSArray getObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/getObjects:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getObjects:(id [])objects ``` |
| To | ``` - (void)getObjects:(ObjectType  _Nonnull [])objects ``` |

Modified [-[NSArray getObjects:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/getObjects:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getObjects:(id [])objects range:(NSRange)range ``` |
| To | ``` - (void)getObjects:(ObjectType  _Nonnull [])objects range:(NSRange)range ``` |

Modified [-[NSArray indexesOfObjectsAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1413512-indexesofobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexSet *)indexesOfObjectsAtIndexes:(NSIndexSet *)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSIndexSet * _Nonnull)indexesOfObjectsAtIndexes:(NSIndexSet * _Nonnull)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSArray indexesOfObjectsPassingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1417603-indexesofobjectspassingtest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexSet *)indexesOfObjectsPassingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSIndexSet * _Nonnull)indexesOfObjectsPassingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSArray indexesOfObjectsWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1415087-indexesofobjectswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexSet *)indexesOfObjectsWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSIndexSet * _Nonnull)indexesOfObjectsWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSArray indexOfObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObject:(id)anObject ``` |
| To | ``` - (NSUInteger)indexOfObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSArray indexOfObject:inRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObject:inRange:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObject:(id)anObject inRange:(NSRange)range ``` |
| To | ``` - (NSUInteger)indexOfObject:(ObjectType _Nonnull)anObject inRange:(NSRange)range ``` |

Modified [-[NSArray indexOfObject:inSortedRange:options:usingComparator:]](https://developer.apple.com/documentation/foundation/nsarray/1412722-indexofobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObject:(id)obj inSortedRange:(NSRange)r options:(NSBinarySearchingOptions)opts usingComparator:(NSComparator)cmp ``` |
| To | ``` - (NSUInteger)indexOfObject:(ObjectType _Nonnull)obj inSortedRange:(NSRange)r options:(NSBinarySearchingOptions)opts usingComparator:(NSComparator _Nonnull)cmp ``` |

Modified [-[NSArray indexOfObjectAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1407652-indexofobjectatindexes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectAtIndexes:(NSIndexSet *)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSUInteger)indexOfObjectAtIndexes:(NSIndexSet * _Nonnull)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSArray indexOfObjectIdenticalTo:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObjectIdenticalTo:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectIdenticalTo:(id)anObject ``` |
| To | ``` - (NSUInteger)indexOfObjectIdenticalTo:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSArray indexOfObjectIdenticalTo:inRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/indexOfObjectIdenticalTo:inRange:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectIdenticalTo:(id)anObject inRange:(NSRange)range ``` |
| To | ``` - (NSUInteger)indexOfObjectIdenticalTo:(ObjectType _Nonnull)anObject inRange:(NSRange)range ``` |

Modified [-[NSArray indexOfObjectPassingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1408043-indexofobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectPassingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSUInteger)indexOfObjectPassingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSArray indexOfObjectWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsarray/1417053-indexofobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSUInteger)indexOfObjectWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSArray initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithArray:(NSArray *)array ``` |
| To | ``` - (instancetype _Nonnull)initWithArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [-[NSArray initWithArray:copyItems:]](https://developer.apple.com/documentation/foundation/nsarray/1408557-initwitharray)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithArray:(NSArray *)array copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithArray:(NSArray<ObjectType> * _Nonnull)array copyItems:(BOOL)flag ``` |

Modified [-[NSArray initWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (NSArray<ObjectType> * _Nullable)initWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [-[NSArray initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsarray/1410518-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (NSArray<ObjectType> * _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [-[NSArray initWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(id)firstObj, ... ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(ObjectType _Nonnull)firstObj, ... ``` |

Modified [-[NSArray initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |

Modified [-[NSArray isEqualToArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/isEqualToArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToArray:(NSArray *)otherArray ``` |
| To | ``` - (BOOL)isEqualToArray:(NSArray<ObjectType> * _Nonnull)otherArray ``` |

Modified [NSArray.lastObject](https://developer.apple.com/documentation/foundation/nsarray/1408316-lastobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id lastObject ``` |
| To | ``` @property(nonatomic, readonly, nullable) ObjectType lastObject ``` |

Modified [-[NSArray objectAtIndex:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/objectAtIndex:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtIndex:(NSUInteger)index ``` |
| To | ``` - (ObjectType _Nonnull)objectAtIndex:(NSUInteger)index ``` |

Modified [-[NSArray objectAtIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsarray/1414084-subscript)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtIndexedSubscript:(NSUInteger)idx ``` |
| To | ``` - (ObjectType _Nonnull)objectAtIndexedSubscript:(NSUInteger)idx ``` |

Modified [-[NSArray objectEnumerator]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/objectEnumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)objectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)objectEnumerator ``` |

Modified [-[NSArray objectsAtIndexes:]](https://developer.apple.com/documentation/foundation/nsarray/1411296-objectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)objectsAtIndexes:(NSIndexSet *)indexes ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)objectsAtIndexes:(NSIndexSet * _Nonnull)indexes ``` |

Modified [-[NSArray reverseObjectEnumerator]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/reverseObjectEnumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)reverseObjectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)reverseObjectEnumerator ``` |

Modified [-[NSArray sortedArrayUsingComparator:]](https://developer.apple.com/documentation/foundation/nsarray/1411195-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingComparator:(NSComparator)cmptr ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingComparator:(NSComparator _Nonnull)cmptr ``` |

Modified [-[NSArray sortedArrayUsingFunction:context:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingFunction:context:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingFunction:(NSInteger (*)(id, id, void *))comparator context:(void *)context ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingFunction:(NSInteger (* _Nonnull)(ObjectType _Nonnull, ObjectType _Nonnull, void * _Nullable))comparator context:(void * _Nullable)context ``` |

Modified [-[NSArray sortedArrayUsingFunction:context:hint:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingFunction:context:hint:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingFunction:(NSInteger (*)(id, id, void *))comparator context:(void *)context hint:(NSData *)hint ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingFunction:(NSInteger (* _Nonnull)(ObjectType _Nonnull, ObjectType _Nonnull, void * _Nullable))comparator context:(void * _Nullable)context hint:(NSData * _Nullable)hint ``` |

Modified [-[NSArray sortedArrayUsingSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingSelector:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingSelector:(SEL)comparator ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingSelector:(SEL _Nonnull)comparator ``` |

Modified [-[NSArray sortedArrayWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsarray/1417804-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayWithOptions:(NSSortOptions)opts usingComparator:(NSComparator)cmptr ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayWithOptions:(NSSortOptions)opts usingComparator:(NSComparator _Nonnull)cmptr ``` |

Modified [-[NSArray subarrayWithRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/subarrayWithRange:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)subarrayWithRange:(NSRange)range ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)subarrayWithRange:(NSRange)range ``` |

Modified [-[NSMutableArray addObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/addObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObject:(id)anObject ``` |
| To | ``` - (void)addObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSMutableArray addObjectsFromArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/addObjectsFromArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObjectsFromArray:(NSArray *)otherArray ``` |
| To | ``` - (void)addObjectsFromArray:(NSArray<ObjectType> * _Nonnull)otherArray ``` |

Modified [+[NSMutableArray arrayWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1460079-arraywithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableArray *)arrayWithContentsOfFile:(NSString *)path ``` |
| To | ``` + (NSMutableArray<ObjectType> * _Nullable)arrayWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [+[NSMutableArray arrayWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1460070-arraywithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableArray *)arrayWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (NSMutableArray<ObjectType> * _Nullable)arrayWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [-[NSMutableArray initWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1414670-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMutableArray *)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (NSMutableArray<ObjectType> * _Nullable)initWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [-[NSMutableArray initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1411688-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMutableArray *)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (NSMutableArray<ObjectType> * _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [-[NSMutableArray insertObject:atIndex:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/insertObject:atIndex:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertObject:(id)anObject atIndex:(NSUInteger)index ``` |
| To | ``` - (void)insertObject:(ObjectType _Nonnull)anObject atIndex:(NSUInteger)index ``` |

Modified [-[NSMutableArray insertObjects:atIndexes:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1416482-insertobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertObjects:(NSArray *)objects atIndexes:(NSIndexSet *)indexes ``` |
| To | ``` - (void)insertObjects:(NSArray<ObjectType> * _Nonnull)objects atIndexes:(NSIndexSet * _Nonnull)indexes ``` |

Modified [-[NSMutableArray removeObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObject:(id)anObject ``` |
| To | ``` - (void)removeObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSMutableArray removeObject:inRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObject:inRange:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObject:(id)anObject inRange:(NSRange)range ``` |
| To | ``` - (void)removeObject:(ObjectType _Nonnull)anObject inRange:(NSRange)range ``` |

Modified [-[NSMutableArray removeObjectIdenticalTo:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectIdenticalTo:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectIdenticalTo:(id)anObject ``` |
| To | ``` - (void)removeObjectIdenticalTo:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSMutableArray removeObjectIdenticalTo:inRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectIdenticalTo:inRange:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectIdenticalTo:(id)anObject inRange:(NSRange)range ``` |
| To | ``` - (void)removeObjectIdenticalTo:(ObjectType _Nonnull)anObject inRange:(NSRange)range ``` |

Modified [-[NSMutableArray removeObjectsInArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectsInArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectsInArray:(NSArray *)otherArray ``` |
| To | ``` - (void)removeObjectsInArray:(NSArray<ObjectType> * _Nonnull)otherArray ``` |

Modified [-[NSMutableArray replaceObjectAtIndex:withObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/replaceObjectAtIndex:withObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceObjectAtIndex:(NSUInteger)index withObject:(id)anObject ``` |
| To | ``` - (void)replaceObjectAtIndex:(NSUInteger)index withObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSMutableArray replaceObjectsAtIndexes:withObjects:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1418287-replaceobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceObjectsAtIndexes:(NSIndexSet *)indexes withObjects:(NSArray *)objects ``` |
| To | ``` - (void)replaceObjectsAtIndexes:(NSIndexSet * _Nonnull)indexes withObjects:(NSArray<ObjectType> * _Nonnull)objects ``` |

Modified [-[NSMutableArray replaceObjectsInRange:withObjectsFromArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/replaceObjectsInRange:withObjectsFromArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceObjectsInRange:(NSRange)range withObjectsFromArray:(NSArray *)otherArray ``` |
| To | ``` - (void)replaceObjectsInRange:(NSRange)range withObjectsFromArray:(NSArray<ObjectType> * _Nonnull)otherArray ``` |

Modified [-[NSMutableArray replaceObjectsInRange:withObjectsFromArray:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/replaceObjectsInRange:withObjectsFromArray:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceObjectsInRange:(NSRange)range withObjectsFromArray:(NSArray *)otherArray range:(NSRange)otherRange ``` |
| To | ``` - (void)replaceObjectsInRange:(NSRange)range withObjectsFromArray:(NSArray<ObjectType> * _Nonnull)otherArray range:(NSRange)otherRange ``` |

Modified [-[NSMutableArray setArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/setArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setArray:(NSArray *)otherArray ``` |
| To | ``` - (void)setArray:(NSArray<ObjectType> * _Nonnull)otherArray ``` |

Modified [-[NSMutableArray setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1460093-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)obj atIndexedSubscript:(NSUInteger)idx ``` |
| To | ``` - (void)setObject:(ObjectType _Nonnull)obj atIndexedSubscript:(NSUInteger)idx ``` |

Modified [-[NSMutableArray sortUsingFunction:context:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/sortUsingFunction:context:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sortUsingFunction:(NSInteger (*)(id, id, void *))compare context:(void *)context ``` |
| To | ``` - (void)sortUsingFunction:(NSInteger (* _Nonnull)(ObjectType _Nonnull, ObjectType _Nonnull, void * _Nullable))compare context:(void * _Nullable)context ``` |

#### NSAttributedString.h

Modified [-[NSAttributedString attributesAtIndex:effectiveRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/attributesAtIndex:effectiveRange:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)attributesAtIndex:(NSUInteger)location effectiveRange:(NSRangePointer)range ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)attributesAtIndex:(NSUInteger)location effectiveRange:(NSRangePointer _Nullable)range ``` |

Modified [-[NSAttributedString attributesAtIndex:longestEffectiveRange:inRange:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/attributesAtIndex:longestEffectiveRange:inRange:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)attributesAtIndex:(NSUInteger)location longestEffectiveRange:(NSRangePointer)range inRange:(NSRange)rangeLimit ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)attributesAtIndex:(NSUInteger)location longestEffectiveRange:(NSRangePointer _Nullable)range inRange:(NSRange)rangeLimit ``` |

Modified [-[NSAttributedString enumerateAttributesInRange:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsattributedstring/1412070-enumerateattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateAttributesInRange:(NSRange)enumerationRange options:(NSAttributedStringEnumerationOptions)opts usingBlock:(void (^)(NSDictionary *attrs, NSRange range, BOOL *stop))block ``` |
| To | ``` - (void)enumerateAttributesInRange:(NSRange)enumerationRange options:(NSAttributedStringEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(NSDictionary<NSString *,id> * _Nonnull attrs, NSRange range, BOOL * _Nonnull stop))block ``` |

Modified [-[NSAttributedString initWithString:attributes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/initWithString:attributes:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithString:(NSString *)str attributes:(NSDictionary *)attrs ``` |
| To | ``` - (instancetype _Nonnull)initWithString:(NSString * _Nonnull)str attributes:(NSDictionary<NSString *,id> * _Nullable)attrs ``` |

Modified [-[NSMutableAttributedString addAttributes:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/addAttributes:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAttributes:(NSDictionary *)attrs range:(NSRange)range ``` |
| To | ``` - (void)addAttributes:(NSDictionary<NSString *,id> * _Nonnull)attrs range:(NSRange)range ``` |

Modified [-[NSMutableAttributedString setAttributes:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/setAttributes:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setAttributes:(NSDictionary *)attrs range:(NSRange)range ``` |
| To | ``` - (void)setAttributes:(NSDictionary<NSString *,id> * _Nullable)attrs range:(NSRange)range ``` |

#### NSBundle.h

Added [-[NSBundle preservationPriorityForTag:]](https://developer.apple.com/documentation/foundation/nsbundle/1614839-preservationpriorityfortag)Added [-[NSBundle setPreservationPriority:forTags:]](https://developer.apple.com/documentation/foundation/nsbundle/1614845-setpreservationpriority)Added [NSBundleResourceRequest](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest)Added [-[NSBundleResourceRequest beginAccessingResourcesWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614840-beginaccessingresources)Added [NSBundleResourceRequest.bundle](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614844-bundle)Added [-[NSBundleResourceRequest conditionallyBeginAccessingResourcesWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614834-conditionallybeginaccessingresou)Added [-[NSBundleResourceRequest endAccessingResources]](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614843-endaccessingresources)Added [-[NSBundleResourceRequest initWithTags:]](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614837-initwithtags)Added [-[NSBundleResourceRequest initWithTags:bundle:]](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614842-initwithtags)Added [NSBundleResourceRequest.loadingPriority](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614841-loadingpriority)Added [NSBundleResourceRequest.progress](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614838-progress)Added [NSBundleResourceRequest.tags](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614833-tags)Added [-[NSString variantFittingPresentationWidth:]](https://developer.apple.com/documentation/foundation/nsstring/1413104-variantfittingpresentationwidth)Added NSBundle(NSBundleResourceRequestAdditions)Added [NSBundleResourceRequestLoadingPriorityUrgent](https://developer.apple.com/documentation/foundation/nsbundleresourcerequestloadingpriorityurgent)Added [NSBundleResourceRequestLowDiskSpaceNotification](https://developer.apple.com/documentation/foundation/nsbundleresourcerequestlowdiskspacenotification)Added NSString(NSBundleExtensionMethods)Modified [+[NSBundle allBundles]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/allBundles)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)allBundles ``` |
| To | ``` + (NSArray<NSBundle *> * _Nonnull)allBundles ``` |

Modified [+[NSBundle allFrameworks]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/allFrameworks)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)allFrameworks ``` |
| To | ``` + (NSArray<NSBundle *> * _Nonnull)allFrameworks ``` |

Modified [NSBundle.executableArchitectures](https://developer.apple.com/documentation/foundation/nsbundle/1415499-executablearchitectures)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *executableArchitectures ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSNumber *> *executableArchitectures ``` |

Modified [NSBundle.infoDictionary](https://developer.apple.com/documentation/foundation/nsbundle/1413477-infodictionary)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *infoDictionary ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,id> *infoDictionary ``` |

Modified [NSBundle.localizations](https://developer.apple.com/documentation/foundation/nsbundle/1417415-localizations)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *localizations ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *localizations ``` |

Modified [NSBundle.localizedInfoDictionary](https://developer.apple.com/documentation/foundation/nsbundle/1407645-localizedinfodictionary)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *localizedInfoDictionary ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,id> *localizedInfoDictionary ``` |

Modified [+[NSBundle pathsForResourcesOfType:inDirectory:]](https://developer.apple.com/documentation/foundation/nsbundle/1415876-pathsforresourcesoftype)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)pathsForResourcesOfType:(NSString *)ext inDirectory:(NSString *)bundlePath ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)pathsForResourcesOfType:(NSString * _Nullable)ext inDirectory:(NSString * _Nonnull)bundlePath ``` |

Modified [-[NSBundle pathsForResourcesOfType:inDirectory:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/pathsForResourcesOfType:inDirectory:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)pathsForResourcesOfType:(NSString *)ext inDirectory:(NSString *)subpath ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)pathsForResourcesOfType:(NSString * _Nullable)ext inDirectory:(NSString * _Nullable)subpath ``` |

Modified [-[NSBundle pathsForResourcesOfType:inDirectory:forLocalization:]](https://developer.apple.com/documentation/foundation/bundle/1416940-paths)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)pathsForResourcesOfType:(NSString *)ext inDirectory:(NSString *)subpath forLocalization:(NSString *)localizationName ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)pathsForResourcesOfType:(NSString * _Nullable)ext inDirectory:(NSString * _Nullable)subpath forLocalization:(NSString * _Nullable)localizationName ``` |

Modified [NSBundle.preferredLocalizations](https://developer.apple.com/documentation/foundation/bundle/1413220-preferredlocalizations)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *preferredLocalizations ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *preferredLocalizations ``` |

Modified [+[NSBundle preferredLocalizationsFromArray:]](https://developer.apple.com/documentation/foundation/bundle/1417249-preferredlocalizations)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)preferredLocalizationsFromArray:(NSArray *)localizationsArray ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)preferredLocalizationsFromArray:(NSArray<NSString *> * _Nonnull)localizationsArray ``` |

Modified [+[NSBundle preferredLocalizationsFromArray:forPreferences:]](https://developer.apple.com/documentation/foundation/bundle/1409418-preferredlocalizations)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)preferredLocalizationsFromArray:(NSArray *)localizationsArray forPreferences:(NSArray *)preferencesArray ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)preferredLocalizationsFromArray:(NSArray<NSString *> * _Nonnull)localizationsArray forPreferences:(NSArray<NSString *> * _Nullable)preferencesArray ``` |

Modified [-[NSBundle URLsForResourcesWithExtension:subdirectory:]](https://developer.apple.com/documentation/foundation/bundle/1407424-urls)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)URLsForResourcesWithExtension:(NSString *)ext subdirectory:(NSString *)subpath ``` |
| To | ``` - (NSArray<NSURL *> * _Nullable)URLsForResourcesWithExtension:(NSString * _Nullable)ext subdirectory:(NSString * _Nullable)subpath ``` |

Modified [+[NSBundle URLsForResourcesWithExtension:subdirectory:inBundleWithURL:]](https://developer.apple.com/documentation/foundation/nsbundle/1409807-urlsforresourceswithextension)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)URLsForResourcesWithExtension:(NSString *)ext subdirectory:(NSString *)subpath inBundleWithURL:(NSURL *)bundleURL ``` |
| To | ``` + (NSArray<NSURL *> * _Nullable)URLsForResourcesWithExtension:(NSString * _Nullable)ext subdirectory:(NSString * _Nullable)subpath inBundleWithURL:(NSURL * _Nonnull)bundleURL ``` |

Modified [-[NSBundle URLsForResourcesWithExtension:subdirectory:localization:]](https://developer.apple.com/documentation/foundation/nsbundle/1414688-urlsforresourceswithextension)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)URLsForResourcesWithExtension:(NSString *)ext subdirectory:(NSString *)subpath localization:(NSString *)localizationName ``` |
| To | ``` - (NSArray<NSURL *> * _Nullable)URLsForResourcesWithExtension:(NSString * _Nullable)ext subdirectory:(NSString * _Nullable)subpath localization:(NSString * _Nullable)localizationName ``` |

#### NSCache.h

Modified [-[NSCache objectForKey:]](https://developer.apple.com/documentation/foundation/nscache/1415458-object)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKey:(id)key ``` |
| To | ``` - (ObjectType _Nullable)objectForKey:(KeyType _Nonnull)key ``` |

Modified [-[NSCache removeObjectForKey:]](https://developer.apple.com/documentation/foundation/nscache/1409900-removeobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectForKey:(id)key ``` |
| To | ``` - (void)removeObjectForKey:(KeyType _Nonnull)key ``` |

Modified [-[NSCache setObject:forKey:]](https://developer.apple.com/documentation/foundation/nscache/1408223-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)obj forKey:(id)key ``` |
| To | ``` - (void)setObject:(ObjectType _Nonnull)obj forKey:(KeyType _Nonnull)key ``` |

Modified [-[NSCache setObject:forKey:cost:]](https://developer.apple.com/documentation/foundation/nscache/1416399-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)obj forKey:(id)key cost:(NSUInteger)g ``` |
| To | ``` - (void)setObject:(ObjectType _Nonnull)obj forKey:(KeyType _Nonnull)key cost:(NSUInteger)g ``` |

#### NSCalendar.h

Modified [NSCalendar.eraSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1415038-erasymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *eraSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *eraSymbols ``` |

Modified [NSCalendar.longEraSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414285-longerasymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *longEraSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *longEraSymbols ``` |

Modified [NSCalendar.monthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414872-monthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *monthSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *monthSymbols ``` |

Modified [NSCalendar.quarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1411517-quartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *quarterSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *quarterSymbols ``` |

Modified [NSCalendar.shortMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1408952-shortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *shortMonthSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *shortMonthSymbols ``` |

Modified [NSCalendar.shortQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1414864-shortquartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *shortQuarterSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *shortQuarterSymbols ``` |

Modified [NSCalendar.shortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1418180-shortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *shortStandaloneMonthSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *shortStandaloneMonthSymbols ``` |

Modified [NSCalendar.shortStandaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1409823-shortstandalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *shortStandaloneQuarterSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *shortStandaloneQuarterSymbols ``` |

Modified [NSCalendar.shortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1413871-shortstandaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *shortStandaloneWeekdaySymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *shortStandaloneWeekdaySymbols ``` |

Modified [NSCalendar.shortWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1407268-shortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *shortWeekdaySymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *shortWeekdaySymbols ``` |

Modified [NSCalendar.standaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1409598-standalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *standaloneMonthSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *standaloneMonthSymbols ``` |

Modified [NSCalendar.standaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1407159-standalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *standaloneQuarterSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *standaloneQuarterSymbols ``` |

Modified [NSCalendar.standaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1411219-standaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *standaloneWeekdaySymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *standaloneWeekdaySymbols ``` |

Modified [NSCalendar.veryShortMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1412779-veryshortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *veryShortMonthSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *veryShortMonthSymbols ``` |

Modified [NSCalendar.veryShortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nscalendar/1408035-veryshortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *veryShortStandaloneMonthSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *veryShortStandaloneMonthSymbols ``` |

Modified [NSCalendar.veryShortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1418273-veryshortstandaloneweekdaysymbol)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *veryShortStandaloneWeekdaySymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *veryShortStandaloneWeekdaySymbols ``` |

Modified [NSCalendar.veryShortWeekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1417207-veryshortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *veryShortWeekdaySymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *veryShortWeekdaySymbols ``` |

Modified [NSCalendar.weekdaySymbols](https://developer.apple.com/documentation/foundation/nscalendar/1412939-weekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *weekdaySymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *weekdaySymbols ``` |

#### NSCoder.h

Added [-[NSCoder decodeTopLevelObjectAndReturnError:]](https://developer.apple.com/documentation/foundation/nscoder/1442553-decodetoplevelobjectandreturnerr)Added [-[NSCoder decodeTopLevelObjectForKey:error:]](https://developer.apple.com/documentation/foundation/nscoder/1442541-decodetoplevelobjectforkey)Added [-[NSCoder decodeTopLevelObjectOfClass:forKey:error:]](https://developer.apple.com/documentation/foundation/nscoder/1442575-decodetoplevelobjectofclass)Added [-[NSCoder decodeTopLevelObjectOfClasses:forKey:error:]](https://developer.apple.com/documentation/foundation/nscoder/1442539-decodetoplevelobjectofclasses)Added [-[NSCoder failWithError:]](https://developer.apple.com/documentation/foundation/nscoder/1411455-failwitherror)Modified [NSCoder.allowedClasses](https://developer.apple.com/documentation/foundation/nscoder/1412486-allowedclasses)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSSet *allowedClasses ``` |
| To | ``` @property(readonly, copy, nullable) NSSet<Class> *allowedClasses ``` |

Modified [-[NSCoder decodeObjectOfClasses:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1442560-decodeobjectofclasses)

|  | Declaration |
| --- | --- |
| From | ``` - (id)decodeObjectOfClasses:(NSSet *)classes forKey:(NSString *)key ``` |
| To | ``` - (id _Nullable)decodeObjectOfClasses:(NSSet<Class> * _Nullable)classes forKey:(NSString * _Nonnull)key ``` |

#### NSComparisonPredicate.h

Added [-[NSComparisonPredicate initWithCoder:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1417900-initwithcoder)Modified [-[NSComparisonPredicate initWithLeftExpression:rightExpression:customSelector:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1409054-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSComparisonPredicate initWithLeftExpression:rightExpression:modifier:type:options:]](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/1413523-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSCompoundPredicate.h

Added [-[NSCompoundPredicate initWithCoder:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1417889-initwithcoder)Modified [+[NSCompoundPredicate andPredicateWithSubpredicates:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1407855-andpredicatewithsubpredicates)

|  | Declaration |
| --- | --- |
| From | ``` + (NSCompoundPredicate *)andPredicateWithSubpredicates:(NSArray *)subpredicates ``` |
| To | ``` + (NSCompoundPredicate * _Nonnull)andPredicateWithSubpredicates:(NSArray<NSPredicate *> * _Nonnull)subpredicates ``` |

Modified [-[NSCompoundPredicate initWithType:subpredicates:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1407744-initwithtype)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithType:(NSCompoundPredicateType)type subpredicates:(NSArray *)subpredicates ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithType:(NSCompoundPredicateType)type subpredicates:(NSArray<NSPredicate *> * _Nonnull)subpredicates ``` | yes |

Modified [+[NSCompoundPredicate orPredicateWithSubpredicates:]](https://developer.apple.com/documentation/foundation/nscompoundpredicate/1417873-orpredicatewithsubpredicates)

|  | Declaration |
| --- | --- |
| From | ``` + (NSCompoundPredicate *)orPredicateWithSubpredicates:(NSArray *)subpredicates ``` |
| To | ``` + (NSCompoundPredicate * _Nonnull)orPredicateWithSubpredicates:(NSArray<NSPredicate *> * _Nonnull)subpredicates ``` |

#### NSDate.h

Modified [+[NSDate distantFuture]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/distantFuture)

|  | Declaration |
| --- | --- |
| From | ``` + (id)distantFuture ``` |
| To | ``` + (NSDate * _Nonnull)distantFuture ``` |

Modified [+[NSDate distantPast]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/clm/NSDate/distantPast)

|  | Declaration |
| --- | --- |
| From | ``` + (id)distantPast ``` |
| To | ``` + (NSDate * _Nonnull)distantPast ``` |

#### NSDateFormatter.h

Modified [NSDateFormatter.eraSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1418282-erasymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *eraSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified eraSymbols ``` |

Modified [NSDateFormatter.longEraSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1418081-longerasymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *longEraSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified longEraSymbols ``` |

Modified [NSDateFormatter.monthSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1412049-monthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *monthSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified monthSymbols ``` |

Modified [NSDateFormatter.quarterSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1417587-quartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *quarterSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified quarterSymbols ``` |

Modified [NSDateFormatter.shortMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1409209-shortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *shortMonthSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified shortMonthSymbols ``` |

Modified [NSDateFormatter.shortQuarterSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1409851-shortquartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *shortQuarterSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified shortQuarterSymbols ``` |

Modified [NSDateFormatter.shortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1414771-shortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *shortStandaloneMonthSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified shortStandaloneMonthSymbols ``` |

Modified [NSDateFormatter.shortStandaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1416421-shortstandalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *shortStandaloneQuarterSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified shortStandaloneQuarterSymbols ``` |

Modified [NSDateFormatter.shortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1409119-shortstandaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *shortStandaloneWeekdaySymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified shortStandaloneWeekdaySymbols ``` |

Modified [NSDateFormatter.shortWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1416121-shortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *shortWeekdaySymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified shortWeekdaySymbols ``` |

Modified [NSDateFormatter.standaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1416227-standalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *standaloneMonthSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified standaloneMonthSymbols ``` |

Modified [NSDateFormatter.standaloneQuarterSymbols](https://developer.apple.com/documentation/foundation/dateformatter/1411487-standalonequartersymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *standaloneQuarterSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified standaloneQuarterSymbols ``` |

Modified [NSDateFormatter.standaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1413618-standaloneweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *standaloneWeekdaySymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified standaloneWeekdaySymbols ``` |

Modified [NSDateFormatter.veryShortMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1413632-veryshortmonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *veryShortMonthSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified veryShortMonthSymbols ``` |

Modified [NSDateFormatter.veryShortStandaloneMonthSymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1413322-veryshortstandalonemonthsymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *veryShortStandaloneMonthSymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified veryShortStandaloneMonthSymbols ``` |

Modified [NSDateFormatter.veryShortStandaloneWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1418238-veryshortstandaloneweekdaysymbol)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *veryShortStandaloneWeekdaySymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified veryShortStandaloneWeekdaySymbols ``` |

Modified [NSDateFormatter.veryShortWeekdaySymbols](https://developer.apple.com/documentation/foundation/dateformatter/1415109-veryshortweekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *veryShortWeekdaySymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified veryShortWeekdaySymbols ``` |

Modified [NSDateFormatter.weekdaySymbols](https://developer.apple.com/documentation/foundation/nsdateformatter/1412405-weekdaysymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *weekdaySymbols ``` |
| To | ``` @property(copy) NSArray<NSString *> * _Null_unspecified weekdaySymbols ``` |

#### NSDictionary.h

Added [-[NSDictionary getObjects:andKeys:count:]](https://developer.apple.com/documentation/foundation/nsdictionary/1409973-getobjects)Added NSDictionary(NSDeprecated)Modified [NSDictionary.allKeys](https://developer.apple.com/documentation/foundation/nsdictionary/1409150-allkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *allKeys ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<KeyType> *allKeys ``` |

Modified [-[NSDictionary allKeysForObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/allKeysForObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)allKeysForObject:(id)anObject ``` |
| To | ``` - (NSArray<KeyType> * _Nonnull)allKeysForObject:(ObjectType _Nonnull)anObject ``` |

Modified [NSDictionary.allValues](https://developer.apple.com/documentation/foundation/nsdictionary/1408915-allvalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *allValues ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<ObjectType> *allValues ``` |

Modified [+[NSDictionary dictionaryWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)dictionaryWithContentsOfFile:(NSString *)path ``` |
| To | ``` + (NSDictionary<KeyType,ObjectType> * _Nullable)dictionaryWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [+[NSDictionary dictionaryWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsdictionary/1574185-dictionarywithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)dictionaryWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (NSDictionary<KeyType,ObjectType> * _Nullable)dictionaryWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [+[NSDictionary dictionaryWithDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithDictionary:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)dictionaryWithDictionary:(NSDictionary *)dict ``` |
| To | ``` + (instancetype _Nonnull)dictionaryWithDictionary:(NSDictionary<KeyType,ObjectType> * _Nonnull)dict ``` |

Modified [+[NSDictionary dictionaryWithObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObject:forKey:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)dictionaryWithObject:(id)object forKey:(id<NSCopying>)key ``` |
| To | ``` + (instancetype _Nonnull)dictionaryWithObject:(ObjectType _Nonnull)object forKey:(id<NSCopying> _Nonnull)key ``` |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)dictionaryWithObjects:(NSArray *)objects forKeys:(NSArray *)keys ``` |
| To | ``` + (instancetype _Nonnull)dictionaryWithObjects:(NSArray<ObjectType> * _Nonnull)objects forKeys:(NSArray<id<NSCopying>> * _Nonnull)keys ``` |

Modified [+[NSDictionary dictionaryWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/clm/NSDictionary/dictionaryWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)dictionaryWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt ``` |
| To | ``` + (instancetype _Nonnull)dictionaryWithObjects:(const ObjectType  _Nonnull [])objects forKeys:(const id<NSCopying>  _Nonnull [])keys count:(NSUInteger)cnt ``` |

Modified [-[NSDictionary enumerateKeysAndObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsdictionary/1414570-enumeratekeysandobjectsusingbloc)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateKeysAndObjectsUsingBlock:(void (^)(id key, id obj, BOOL *stop))block ``` |
| To | ``` - (void)enumerateKeysAndObjectsUsingBlock:(void (^ _Nonnull)(KeyType _Nonnull key, ObjectType _Nonnull obj, BOOL * _Nonnull stop))block ``` |

Modified [-[NSDictionary enumerateKeysAndObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsdictionary/1409739-enumeratekeysandobjectswithoptio)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateKeysAndObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^)(id key, id obj, BOOL *stop))block ``` |
| To | ``` - (void)enumerateKeysAndObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(KeyType _Nonnull key, ObjectType _Nonnull obj, BOOL * _Nonnull stop))block ``` |

Modified [-[NSDictionary getObjects:andKeys:]](https://developer.apple.com/documentation/foundation/nsdictionary/1409428-getobjects)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (void)getObjects:(id [])objects andKeys:(id [])keys ``` | -- |
| To | ``` - (void)getObjects:(ObjectType  _Nonnull [])objects andKeys:(KeyType  _Nonnull [])keys ``` | iOS 9.0 |

Modified [-[NSDictionary initWithContentsOfFile:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithContentsOfFile:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (NSDictionary<KeyType,ObjectType> * _Nullable)initWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [-[NSDictionary initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsdictionary/1416069-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (NSDictionary<KeyType,ObjectType> * _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [-[NSDictionary initWithDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithDictionary:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDictionary:(NSDictionary *)otherDictionary ``` |
| To | ``` - (instancetype _Nonnull)initWithDictionary:(NSDictionary<KeyType,ObjectType> * _Nonnull)otherDictionary ``` |

Modified [-[NSDictionary initWithDictionary:copyItems:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithDictionary:copyItems:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDictionary:(NSDictionary *)otherDictionary copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithDictionary:(NSDictionary<KeyType,ObjectType> * _Nonnull)otherDictionary copyItems:(BOOL)flag ``` |

Modified [-[NSDictionary initWithObjects:forKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(NSArray *)objects forKeys:(NSArray *)keys ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(NSArray<ObjectType> * _Nonnull)objects forKeys:(NSArray<id<NSCopying>> * _Nonnull)keys ``` |

Modified [-[NSDictionary initWithObjects:forKeys:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/initWithObjects:forKeys:count:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const id [])objects forKeys:(const id<NSCopying> [])keys count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(const ObjectType  _Nonnull [])objects forKeys:(const id<NSCopying>  _Nonnull [])keys count:(NSUInteger)cnt ``` |

Modified [-[NSDictionary isEqualToDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/isEqualToDictionary:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToDictionary:(NSDictionary *)otherDictionary ``` |
| To | ``` - (BOOL)isEqualToDictionary:(NSDictionary<KeyType,ObjectType> * _Nonnull)otherDictionary ``` |

Modified [-[NSDictionary keyEnumerator]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/keyEnumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)keyEnumerator ``` |
| To | ``` - (NSEnumerator<KeyType> * _Nonnull)keyEnumerator ``` |

Modified [-[NSDictionary keysOfEntriesPassingTest:]](https://developer.apple.com/documentation/foundation/nsdictionary/1407186-keysofentriespassingtest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)keysOfEntriesPassingTest:(BOOL (^)(id key, id obj, BOOL *stop))predicate ``` |
| To | ``` - (NSSet<KeyType> * _Nonnull)keysOfEntriesPassingTest:(BOOL (^ _Nonnull)(KeyType _Nonnull key, ObjectType _Nonnull obj, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSDictionary keysOfEntriesWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsdictionary/1416706-keysofentrieswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)keysOfEntriesWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id key, id obj, BOOL *stop))predicate ``` |
| To | ``` - (NSSet<KeyType> * _Nonnull)keysOfEntriesWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(KeyType _Nonnull key, ObjectType _Nonnull obj, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSDictionary keysSortedByValueUsingComparator:]](https://developer.apple.com/documentation/foundation/nsdictionary/1411105-keyssortedbyvalueusingcomparator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)keysSortedByValueUsingComparator:(NSComparator)cmptr ``` |
| To | ``` - (NSArray<KeyType> * _Nonnull)keysSortedByValueUsingComparator:(NSComparator _Nonnull)cmptr ``` |

Modified [-[NSDictionary keysSortedByValueUsingSelector:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/keysSortedByValueUsingSelector:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)keysSortedByValueUsingSelector:(SEL)comparator ``` |
| To | ``` - (NSArray<KeyType> * _Nonnull)keysSortedByValueUsingSelector:(SEL _Nonnull)comparator ``` |

Modified [-[NSDictionary keysSortedByValueWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsdictionary/1415717-keyssortedbyvaluewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)keysSortedByValueWithOptions:(NSSortOptions)opts usingComparator:(NSComparator)cmptr ``` |
| To | ``` - (NSArray<KeyType> * _Nonnull)keysSortedByValueWithOptions:(NSSortOptions)opts usingComparator:(NSComparator _Nonnull)cmptr ``` |

Modified [-[NSDictionary objectEnumerator]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/objectEnumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)objectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)objectEnumerator ``` |

Modified [-[NSDictionary objectForKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/objectForKey:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKey:(id)aKey ``` |
| To | ``` - (ObjectType _Nullable)objectForKey:(KeyType _Nonnull)aKey ``` |

Modified [-[NSDictionary objectForKeyedSubscript:]](https://developer.apple.com/documentation/foundation/nsdictionary/1415430-subscript)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKeyedSubscript:(id)key ``` |
| To | ``` - (ObjectType _Nullable)objectForKeyedSubscript:(KeyType _Nonnull)key ``` |

Modified [-[NSDictionary objectsForKeys:notFoundMarker:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSDictionary/objectsForKeys:notFoundMarker:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)objectsForKeys:(NSArray *)keys notFoundMarker:(id)marker ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)objectsForKeys:(NSArray<KeyType> * _Nonnull)keys notFoundMarker:(ObjectType _Nonnull)marker ``` |

Modified [+[NSDictionary sharedKeySetForKeys:]](https://developer.apple.com/documentation/foundation/nsdictionary/1408190-sharedkeyset)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sharedKeySetForKeys:(NSArray *)keys ``` |
| To | ``` + (id _Nonnull)sharedKeySetForKeys:(NSArray<id<NSCopying>> * _Nonnull)keys ``` |

Modified [-[NSMutableDictionary addEntriesFromDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/addEntriesFromDictionary:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addEntriesFromDictionary:(NSDictionary *)otherDictionary ``` |
| To | ``` - (void)addEntriesFromDictionary:(NSDictionary<KeyType,ObjectType> * _Nonnull)otherDictionary ``` |

Modified [+[NSMutableDictionary dictionaryWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1574188-dictionarywithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableDictionary *)dictionaryWithContentsOfFile:(NSString *)path ``` |
| To | ``` + (NSMutableDictionary<KeyType,ObjectType> * _Nullable)dictionaryWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [+[NSMutableDictionary dictionaryWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1574182-dictionarywithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableDictionary *)dictionaryWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (NSMutableDictionary<KeyType,ObjectType> * _Nullable)dictionaryWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [+[NSMutableDictionary dictionaryWithSharedKeySet:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1412658-dictionarywithsharedkeyset)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMutableDictionary *)dictionaryWithSharedKeySet:(id)keyset ``` |
| To | ``` + (NSMutableDictionary<KeyType,ObjectType> * _Nonnull)dictionaryWithSharedKeySet:(id _Nonnull)keyset ``` |

Modified [-[NSMutableDictionary initWithContentsOfFile:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1407593-initwithcontentsoffile)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMutableDictionary *)initWithContentsOfFile:(NSString *)path ``` |
| To | ``` - (NSMutableDictionary<KeyType,ObjectType> * _Nullable)initWithContentsOfFile:(NSString * _Nonnull)path ``` |

Modified [-[NSMutableDictionary initWithContentsOfURL:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1410409-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMutableDictionary *)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (NSMutableDictionary<KeyType,ObjectType> * _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [-[NSMutableDictionary removeObjectForKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/removeObjectForKey:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectForKey:(id)aKey ``` |
| To | ``` - (void)removeObjectForKey:(KeyType _Nonnull)aKey ``` |

Modified [-[NSMutableDictionary removeObjectsForKeys:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/removeObjectsForKeys:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectsForKeys:(NSArray *)keyArray ``` |
| To | ``` - (void)removeObjectsForKeys:(NSArray<KeyType> * _Nonnull)keyArray ``` |

Modified [-[NSMutableDictionary setDictionary:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/setDictionary:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDictionary:(NSDictionary *)otherDictionary ``` |
| To | ``` - (void)setDictionary:(NSDictionary<KeyType,ObjectType> * _Nonnull)otherDictionary ``` |

Modified [-[NSMutableDictionary setObject:forKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/instm/NSMutableDictionary/setObject:forKey:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)anObject forKey:(id<NSCopying>)aKey ``` |
| To | ``` - (void)setObject:(ObjectType _Nonnull)anObject forKey:(id<NSCopying> _Nonnull)aKey ``` |

Modified [-[NSMutableDictionary setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1574187-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)obj forKeyedSubscript:(id<NSCopying>)key ``` |
| To | ``` - (void)setObject:(ObjectType _Nullable)obj forKeyedSubscript:(id<NSCopying> _Nonnull)key ``` |

#### NSEnumerator.h

Modified [NSEnumerator.allObjects](https://developer.apple.com/documentation/foundation/nsenumerator/1417755-allobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *allObjects ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<ObjectType> *allObjects ``` |

Modified [-[NSEnumerator nextObject]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSEnumerator/Description.html#//apple_ref/occ/instm/NSEnumerator/nextObject)

|  | Declaration |
| --- | --- |
| From | ``` - (id)nextObject ``` |
| To | ``` - (ObjectType _Nullable)nextObject ``` |

#### NSError.h

Added [+[NSError setUserInfoValueProviderForDomain:provider:]](https://developer.apple.com/documentation/foundation/nserror/1408064-setuserinfovalueproviderfordomai)Added [+[NSError userInfoValueProviderForDomain:]](https://developer.apple.com/documentation/foundation/nserror/1413427-userinfovalueprovider)Modified [NSError.localizedRecoveryOptions](https://developer.apple.com/documentation/foundation/nserror/1415950-localizedrecoveryoptions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *localizedRecoveryOptions ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSString *> *localizedRecoveryOptions ``` |

Modified [NSError.recoveryAttempter](https://developer.apple.com/documentation/foundation/nserror/1408864-recoveryattempter)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id recoveryAttempter ``` |
| To | ``` @property(readonly, strong, nullable) id recoveryAttempter ``` |

#### NSException.h

Modified [NSException.callStackReturnAddresses](https://developer.apple.com/documentation/foundation/nsexception/1412165-callstackreturnaddresses)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *callStackReturnAddresses ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSNumber *> *callStackReturnAddresses ``` |

Modified [NSException.callStackSymbols](https://developer.apple.com/documentation/foundation/nsexception/1416845-callstacksymbols)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *callStackSymbols ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *callStackSymbols ``` |

#### NSExpression.h

Added [+[NSExpression expressionForConditional:trueExpression:falseExpression:]](https://developer.apple.com/documentation/foundation/nsexpression/1418004-expressionforconditional)Added [NSExpression.falseExpression](https://developer.apple.com/documentation/foundation/nsexpression/1416488-falseexpression)Added [-[NSExpression initWithCoder:]](https://developer.apple.com/documentation/foundation/nsexpression/1415409-initwithcoder)Added [NSExpression.trueExpression](https://developer.apple.com/documentation/foundation/nsexpression/1411874-trueexpression)Added [NSConditionalExpressionType](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype/conditional)Modified [NSExpression.arguments](https://developer.apple.com/documentation/foundation/nsexpression/1411559-arguments)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *arguments ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSExpression *> *arguments ``` |

Modified [NSExpression.expressionBlock](https://developer.apple.com/documentation/foundation/nsexpression/1409139-expressionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) id (^expressionBlock)(id, NSArray *, NSMutableDictionary *) ``` |
| To | ``` @property(readonly, copy, nonnull) id  (^ _Nonnull)(id _Nullable, NSArray * _Nonnull, NSMutableDictionary * _Nullable) expressionBlock ``` |

Modified [+[NSExpression expressionForBlock:arguments:]](https://developer.apple.com/documentation/foundation/nsexpression/1407823-expressionforblock)

|  | Declaration |
| --- | --- |
| From | ``` + (NSExpression *)expressionForBlock:(id (^)(id evaluatedObject, NSArray *expressions, NSMutableDictionary *context))block arguments:(NSArray *)arguments ``` |
| To | ``` + (NSExpression * _Nonnull)expressionForBlock:(id  _Nonnull (^ _Nonnull)(id _Nullable evaluatedObject, NSArray * _Nonnull expressions, NSMutableDictionary * _Nullable context))block arguments:(NSArray<NSExpression *> * _Nullable)arguments ``` |

Modified [-[NSExpression initWithExpressionType:]](https://developer.apple.com/documentation/foundation/nsexpression/1418351-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSFileCoordinator.h

Modified [-[NSFileCoordinator coordinateAccessWithIntents:queue:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1411533-coordinate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)coordinateAccessWithIntents:(NSArray *)intents queue:(NSOperationQueue *)queue byAccessor:(void (^)(NSError *error))accessor ``` |
| To | ``` - (void)coordinateAccessWithIntents:(NSArray<NSFileAccessIntent *> * _Nonnull)intents queue:(NSOperationQueue * _Nonnull)queue byAccessor:(void (^ _Nonnull)(NSError * _Nullable error))accessor ``` |

Modified [+[NSFileCoordinator filePresenters]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1407685-filepresenters)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)filePresenters ``` |
| To | ``` + (NSArray<id<NSFilePresenter>> * _Nonnull)filePresenters ``` |

Modified [-[NSFileCoordinator prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1412420-prepareforreadingitemsaturls)

|  | Declaration |
| --- | --- |
| From | ``` - (void)prepareForReadingItemsAtURLs:(NSArray *)readingURLs options:(NSFileCoordinatorReadingOptions)readingOptions writingItemsAtURLs:(NSArray *)writingURLs options:(NSFileCoordinatorWritingOptions)writingOptions error:(NSError **)outError byAccessor:(void (^)(void (^completionHandler)(void)))batchAccessor ``` |
| To | ``` - (void)prepareForReadingItemsAtURLs:(NSArray<NSURL *> * _Nonnull)readingURLs options:(NSFileCoordinatorReadingOptions)readingOptions writingItemsAtURLs:(NSArray<NSURL *> * _Nonnull)writingURLs options:(NSFileCoordinatorWritingOptions)writingOptions error:(NSError * _Nullable * _Nullable)outError byAccessor:(void (^ _Nonnull)(void (^ _Nonnull)(void) completionHandler))batchAccessor ``` |

#### NSFileHandle.h

Modified [-[NSFileHandle acceptConnectionInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/filehandle/1412997-acceptconnectioninbackgroundandn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)acceptConnectionInBackgroundAndNotifyForModes:(NSArray *)modes ``` |
| To | ``` - (void)acceptConnectionInBackgroundAndNotifyForModes:(NSArray<NSString *> * _Nullable)modes ``` |

Modified [-[NSFileHandle readInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1416294-readinbackgroundandnotifyformode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)readInBackgroundAndNotifyForModes:(NSArray *)modes ``` |
| To | ``` - (void)readInBackgroundAndNotifyForModes:(NSArray<NSString *> * _Nullable)modes ``` |

Modified [-[NSFileHandle readToEndOfFileInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/nsfilehandle/1417321-readtoendoffileinbackgroundandno)

|  | Declaration |
| --- | --- |
| From | ``` - (void)readToEndOfFileInBackgroundAndNotifyForModes:(NSArray *)modes ``` |
| To | ``` - (void)readToEndOfFileInBackgroundAndNotifyForModes:(NSArray<NSString *> * _Nullable)modes ``` |

Modified [-[NSFileHandle waitForDataInBackgroundAndNotifyForModes:]](https://developer.apple.com/documentation/foundation/filehandle/1414643-waitfordatainbackgroundandnotify)

|  | Declaration |
| --- | --- |
| From | ``` - (void)waitForDataInBackgroundAndNotifyForModes:(NSArray *)modes ``` |
| To | ``` - (void)waitForDataInBackgroundAndNotifyForModes:(NSArray<NSString *> * _Nullable)modes ``` |

#### NSFileManager.h

Added [NSFileManagerUnmountOptions](https://developer.apple.com/documentation/foundation/nsfilemanagerunmountoptions)Modified [NSDirectoryEnumerator.directoryAttributes](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1411357-directoryattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *directoryAttributes ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,id> *directoryAttributes ``` |

Modified [NSDirectoryEnumerator.fileAttributes](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/1413284-fileattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *fileAttributes ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,id> *fileAttributes ``` |

Modified [-[NSFileManager attributesOfFileSystemForPath:error:]](https://developer.apple.com/documentation/foundation/filemanager/1411896-attributesoffilesystem)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)attributesOfFileSystemForPath:(NSString *)path error:(NSError **)error ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)attributesOfFileSystemForPath:(NSString * _Nonnull)path error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager attributesOfItemAtPath:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1410452-attributesofitematpath)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)attributesOfItemAtPath:(NSString *)path error:(NSError **)error ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)attributesOfItemAtPath:(NSString * _Nonnull)path error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager componentsToDisplayForPath:]](https://developer.apple.com/documentation/foundation/filemanager/1413929-componentstodisplay)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)componentsToDisplayForPath:(NSString *)path ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)componentsToDisplayForPath:(NSString * _Nonnull)path ``` |

Modified [-[NSFileManager contentsOfDirectoryAtPath:error:]](https://developer.apple.com/documentation/foundation/filemanager/1414584-contentsofdirectory)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)contentsOfDirectoryAtPath:(NSString *)path error:(NSError **)error ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)contentsOfDirectoryAtPath:(NSString * _Nonnull)path error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1413768-contentsofdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)contentsOfDirectoryAtURL:(NSURL *)url includingPropertiesForKeys:(NSArray *)keys options:(NSDirectoryEnumerationOptions)mask error:(NSError **)error ``` |
| To | ``` - (NSArray<NSURL *> * _Nullable)contentsOfDirectoryAtURL:(NSURL * _Nonnull)url includingPropertiesForKeys:(NSArray<NSString *> * _Nullable)keys options:(NSDirectoryEnumerationOptions)mask error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]](https://developer.apple.com/documentation/foundation/filemanager/1407884-createdirectory)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)createDirectoryAtPath:(NSString *)path withIntermediateDirectories:(BOOL)createIntermediates attributes:(NSDictionary *)attributes error:(NSError **)error ``` |
| To | ``` - (BOOL)createDirectoryAtPath:(NSString * _Nonnull)path withIntermediateDirectories:(BOOL)createIntermediates attributes:(NSDictionary<NSString *,id> * _Nullable)attributes error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1415371-createdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)createDirectoryAtURL:(NSURL *)url withIntermediateDirectories:(BOOL)createIntermediates attributes:(NSDictionary *)attributes error:(NSError **)error ``` |
| To | ``` - (BOOL)createDirectoryAtURL:(NSURL * _Nonnull)url withIntermediateDirectories:(BOOL)createIntermediates attributes:(NSDictionary<NSString *,id> * _Nullable)attributes error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager createFileAtPath:contents:attributes:]](https://developer.apple.com/documentation/foundation/filemanager/1410695-createfile)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)createFileAtPath:(NSString *)path contents:(NSData *)data attributes:(NSDictionary *)attr ``` |
| To | ``` - (BOOL)createFileAtPath:(NSString * _Nonnull)path contents:(NSData * _Nullable)data attributes:(NSDictionary<NSString *,id> * _Nullable)attr ``` |

Modified [-[NSFileManager enumeratorAtPath:]](https://developer.apple.com/documentation/foundation/filemanager/1408726-enumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDirectoryEnumerator *)enumeratorAtPath:(NSString *)path ``` |
| To | ``` - (NSDirectoryEnumerator<NSString *> * _Nullable)enumeratorAtPath:(NSString * _Nonnull)path ``` |

Modified [-[NSFileManager enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1409571-enumeratoraturl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDirectoryEnumerator *)enumeratorAtURL:(NSURL *)url includingPropertiesForKeys:(NSArray *)keys options:(NSDirectoryEnumerationOptions)mask errorHandler:(BOOL (^)(NSURL *url, NSError *error))handler ``` |
| To | ``` - (NSDirectoryEnumerator<NSURL *> * _Nullable)enumeratorAtURL:(NSURL * _Nonnull)url includingPropertiesForKeys:(NSArray<NSString *> * _Nullable)keys options:(NSDirectoryEnumerationOptions)mask errorHandler:(BOOL (^ _Nullable)(NSURL * _Nonnull url, NSError * _Nonnull error))handler ``` |

Modified [-[NSFileManager mountedVolumeURLsIncludingResourceValuesForKeys:options:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1409626-mountedvolumeurlsincludingresour)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)mountedVolumeURLsIncludingResourceValuesForKeys:(NSArray *)propertyKeys options:(NSVolumeEnumerationOptions)options ``` |
| To | ``` - (NSArray<NSURL *> * _Nullable)mountedVolumeURLsIncludingResourceValuesForKeys:(NSArray<NSString *> * _Nullable)propertyKeys options:(NSVolumeEnumerationOptions)options ``` |

Modified [-[NSFileManager setAttributes:ofItemAtPath:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1413667-setattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setAttributes:(NSDictionary *)attributes ofItemAtPath:(NSString *)path error:(NSError **)error ``` |
| To | ``` - (BOOL)setAttributes:(NSDictionary<NSString *,id> * _Nonnull)attributes ofItemAtPath:(NSString * _Nonnull)path error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager subpathsAtPath:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1413742-subpathsatpath)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)subpathsAtPath:(NSString *)path ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)subpathsAtPath:(NSString * _Nonnull)path ``` |

Modified [-[NSFileManager subpathsOfDirectoryAtPath:error:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1417353-subpathsofdirectoryatpath)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)subpathsOfDirectoryAtPath:(NSString *)path error:(NSError **)error ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)subpathsOfDirectoryAtPath:(NSString * _Nonnull)path error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSFileManager URLsForDirectory:inDomains:]](https://developer.apple.com/documentation/foundation/nsfilemanager/1407726-urlsfordirectory)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)URLsForDirectory:(NSSearchPathDirectory)directory inDomains:(NSSearchPathDomainMask)domainMask ``` |
| To | ``` - (NSArray<NSURL *> * _Nonnull)URLsForDirectory:(NSSearchPathDirectory)directory inDomains:(NSSearchPathDomainMask)domainMask ``` |

#### NSFilePresenter.h

Modified [-[NSFilePresenter relinquishPresentedItemToReader:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1410743-relinquishpresenteditemtoreader)

|  | Declaration |
| --- | --- |
| From | ``` - (void)relinquishPresentedItemToReader:(void (^)(void (^reacquirer)(void)))reader ``` |
| To | ``` - (void)relinquishPresentedItemToReader:(void (^ _Nonnull)(void (^ _Nullable)(void) reacquirer))reader ``` |

Modified [-[NSFilePresenter relinquishPresentedItemToWriter:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413688-relinquishpresenteditemtowriter)

|  | Declaration |
| --- | --- |
| From | ``` - (void)relinquishPresentedItemToWriter:(void (^)(void (^reacquirer)(void)))writer ``` |
| To | ``` - (void)relinquishPresentedItemToWriter:(void (^ _Nonnull)(void (^ _Nullable)(void) reacquirer))writer ``` |

#### NSFileVersion.h

Modified [+[NSFileVersion getNonlocalVersionsOfItemAtURL:completionHandler:]](https://developer.apple.com/documentation/foundation/nsfileversion/1416051-getnonlocalversionsofitematurl)

|  | Declaration |
| --- | --- |
| From | ``` + (void)getNonlocalVersionsOfItemAtURL:(NSURL *)url completionHandler:(void (^)(NSArray *nonlocalFileVersions, NSError *error))completionHandler ``` |
| To | ``` + (void)getNonlocalVersionsOfItemAtURL:(NSURL * _Nonnull)url completionHandler:(void (^ _Nonnull)(NSArray<NSFileVersion *> * _Nullable nonlocalFileVersions, NSError * _Nullable error))completionHandler ``` |

Modified [+[NSFileVersion otherVersionsOfItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfileversion/1418163-otherversionsofitematurl)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)otherVersionsOfItemAtURL:(NSURL *)url ``` |
| To | ``` + (NSArray<NSFileVersion *> * _Nullable)otherVersionsOfItemAtURL:(NSURL * _Nonnull)url ``` |

Modified [+[NSFileVersion unresolvedConflictVersionsOfItemAtURL:]](https://developer.apple.com/documentation/foundation/nsfileversion/1417854-unresolvedconflictversionsofitem)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)unresolvedConflictVersionsOfItemAtURL:(NSURL *)url ``` |
| To | ``` + (NSArray<NSFileVersion *> * _Nullable)unresolvedConflictVersionsOfItemAtURL:(NSURL * _Nonnull)url ``` |

#### NSFileWrapper.h

Modified [NSFileWrapper.fileAttributes](https://developer.apple.com/documentation/foundation/nsfilewrapper/1412745-fileattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *fileAttributes ``` |
| To | ``` @property(copy, nonnull) NSDictionary<NSString *,id> *fileAttributes ``` |

Modified [NSFileWrapper.fileWrappers](https://developer.apple.com/documentation/foundation/filewrapper/1409437-filewrappers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *fileWrappers ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,NSFileWrapper *> *fileWrappers ``` |

Modified [-[NSFileWrapper initDirectoryWithFileWrappers:]](https://developer.apple.com/documentation/foundation/nsfilewrapper/1415121-initdirectorywithfilewrappers)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initDirectoryWithFileWrappers:(NSDictionary *)childrenByPreferredName ``` |
| To | ``` - (instancetype _Nonnull)initDirectoryWithFileWrappers:(NSDictionary<NSString *,NSFileWrapper *> * _Nonnull)childrenByPreferredName ``` |

#### NSFormatter.h

Modified [-[NSFormatter attributedStringForObjectValue:withDefaultAttributes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/attributedStringForObjectValue:withDefaultAttributes:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSAttributedString *)attributedStringForObjectValue:(id)obj withDefaultAttributes:(NSDictionary *)attrs ``` |
| To | ``` - (NSAttributedString * _Nullable)attributedStringForObjectValue:(id _Nonnull)obj withDefaultAttributes:(NSDictionary<NSString *,id> * _Nullable)attrs ``` |

#### NSHashTable.h

Removed [NSHashTableCopyIn](https://developer.apple.com/documentation/foundation/nshashtablecopyin)Removed [NSHashTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nshashtableobjectpointerpersonality)Removed [NSHashTableStrongMemory](https://developer.apple.com/documentation/foundation/nshashtablestrongmemory)Removed [NSHashTableWeakMemory](https://developer.apple.com/documentation/foundation/nshashtablezeroingweakmemory)Added [NSHashTableCopyIn](https://developer.apple.com/documentation/foundation/nshashtablecopyin)Added [NSHashTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nshashtableobjectpointerpersonality)Added [NSHashTableStrongMemory](https://developer.apple.com/documentation/foundation/nshashtablestrongmemory)Added [NSHashTableWeakMemory](https://developer.apple.com/documentation/foundation/nshashtableweakmemory)Modified [-[NSHashTable addObject:]](https://developer.apple.com/documentation/foundation/nshashtable/1411690-addobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObject:(id)object ``` |
| To | ``` - (void)addObject:(ObjectType _Nullable)object ``` |

Modified [NSHashTable.allObjects](https://developer.apple.com/documentation/foundation/nshashtable/1410223-allobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *allObjects ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<ObjectType> *allObjects ``` |

Modified [NSHashTable.anyObject](https://developer.apple.com/documentation/foundation/nshashtable/1410639-anyobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id anyObject ``` |
| To | ``` @property(nonatomic, readonly, nullable) ObjectType anyObject ``` |

Modified [-[NSHashTable containsObject:]](https://developer.apple.com/documentation/foundation/nshashtable/1415113-containsobject)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsObject:(id)anObject ``` |
| To | ``` - (BOOL)containsObject:(ObjectType _Nullable)anObject ``` |

Modified [+[NSHashTable hashTableWithOptions:]](https://developer.apple.com/documentation/foundation/nshashtable/1415284-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSHashTable *)hashTableWithOptions:(NSPointerFunctionsOptions)options ``` |
| To | ``` + (NSHashTable<ObjectType> * _Nonnull)hashTableWithOptions:(NSPointerFunctionsOptions)options ``` |

Modified [-[NSHashTable intersectHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1408509-intersect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)intersectHashTable:(NSHashTable *)other ``` |
| To | ``` - (void)intersectHashTable:(NSHashTable<ObjectType> * _Nonnull)other ``` |

Modified [-[NSHashTable intersectsHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1416474-intersectshashtable)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)intersectsHashTable:(NSHashTable *)other ``` |
| To | ``` - (BOOL)intersectsHashTable:(NSHashTable<ObjectType> * _Nonnull)other ``` |

Modified [-[NSHashTable isEqualToHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1410816-isequal)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToHashTable:(NSHashTable *)other ``` |
| To | ``` - (BOOL)isEqualToHashTable:(NSHashTable<ObjectType> * _Nonnull)other ``` |

Modified [-[NSHashTable isSubsetOfHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1417518-issubsetofhashtable)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isSubsetOfHashTable:(NSHashTable *)other ``` |
| To | ``` - (BOOL)isSubsetOfHashTable:(NSHashTable<ObjectType> * _Nonnull)other ``` |

Modified [-[NSHashTable member:]](https://developer.apple.com/documentation/foundation/nshashtable/1417991-member)

|  | Declaration |
| --- | --- |
| From | ``` - (id)member:(id)object ``` |
| To | ``` - (ObjectType _Nullable)member:(ObjectType _Nullable)object ``` |

Modified [-[NSHashTable minusHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1414557-minushashtable)

|  | Declaration |
| --- | --- |
| From | ``` - (void)minusHashTable:(NSHashTable *)other ``` |
| To | ``` - (void)minusHashTable:(NSHashTable<ObjectType> * _Nonnull)other ``` |

Modified [-[NSHashTable objectEnumerator]](https://developer.apple.com/documentation/foundation/nshashtable/1416308-objectenumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)objectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)objectEnumerator ``` |

Modified [-[NSHashTable removeObject:]](https://developer.apple.com/documentation/foundation/nshashtable/1415369-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObject:(id)object ``` |
| To | ``` - (void)removeObject:(ObjectType _Nullable)object ``` |

Modified [NSHashTable.setRepresentation](https://developer.apple.com/documentation/foundation/nshashtable/1414641-setrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSSet *setRepresentation ``` |
| To | ``` @property(readonly, copy, nonnull) NSSet<ObjectType> *setRepresentation ``` |

Modified [-[NSHashTable unionHashTable:]](https://developer.apple.com/documentation/foundation/nshashtable/1413481-union)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unionHashTable:(NSHashTable *)other ``` |
| To | ``` - (void)unionHashTable:(NSHashTable<ObjectType> * _Nonnull)other ``` |

Modified [+[NSHashTable weakObjectsHashTable]](https://developer.apple.com/documentation/foundation/nshashtable/1412241-weakobjectshashtable)

|  | Declaration |
| --- | --- |
| From | ``` + (NSHashTable *)weakObjectsHashTable ``` |
| To | ``` + (NSHashTable<ObjectType> * _Nonnull)weakObjectsHashTable ``` |

#### NSHTTPCookie.h

Modified [+[NSHTTPCookie cookiesWithResponseHeaderFields:forURL:]](https://developer.apple.com/documentation/foundation/httpcookie/1393011-cookies)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)cookiesWithResponseHeaderFields:(NSDictionary *)headerFields forURL:(NSURL *)URL ``` |
| To | ``` + (NSArray<NSHTTPCookie *> * _Nonnull)cookiesWithResponseHeaderFields:(NSDictionary<NSString *,NSString *> * _Nonnull)headerFields forURL:(NSURL * _Nonnull)URL ``` |

Modified [+[NSHTTPCookie cookieWithProperties:]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392967-cookiewithproperties)

|  | Declaration |
| --- | --- |
| From | ``` + (NSHTTPCookie *)cookieWithProperties:(NSDictionary *)properties ``` |
| To | ``` + (NSHTTPCookie * _Nullable)cookieWithProperties:(NSDictionary<NSString *,id> * _Nonnull)properties ``` |

Modified [-[NSHTTPCookie initWithProperties:]](https://developer.apple.com/documentation/foundation/nshttpcookie/1392975-initwithproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithProperties:(NSDictionary *)properties ``` |
| To | ``` - (instancetype _Nullable)initWithProperties:(NSDictionary<NSString *,id> * _Nonnull)properties ``` |

Modified [NSHTTPCookie.portList](https://developer.apple.com/documentation/foundation/httpcookie/1393027-portlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *portList ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSNumber *> *portList ``` |

Modified [NSHTTPCookie.properties](https://developer.apple.com/documentation/foundation/nshttpcookie/1393017-properties)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *properties ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,id> *properties ``` |

Modified [+[NSHTTPCookie requestHeaderFieldsWithCookies:]](https://developer.apple.com/documentation/foundation/nshttpcookie/1393021-requestheaderfieldswithcookies)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)requestHeaderFieldsWithCookies:(NSArray *)cookies ``` |
| To | ``` + (NSDictionary<NSString *,NSString *> * _Nonnull)requestHeaderFieldsWithCookies:(NSArray<NSHTTPCookie *> * _Nonnull)cookies ``` |

#### NSHTTPCookieStorage.h

Added [+[NSHTTPCookieStorage sharedCookieStorageForGroupContainerIdentifier:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1411361-sharedcookiestorageforgroupconta)Modified [NSHTTPCookieStorage.cookies](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1418390-cookies)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *cookies ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSHTTPCookie *> *cookies ``` |

Modified [-[NSHTTPCookieStorage cookiesForURL:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1412100-cookiesforurl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)cookiesForURL:(NSURL *)URL ``` |
| To | ``` - (NSArray<NSHTTPCookie *> * _Nullable)cookiesForURL:(NSURL * _Nonnull)URL ``` |

Modified [-[NSHTTPCookieStorage getCookiesForTask:completionHandler:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1408517-getcookiesfortask)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getCookiesForTask:(NSURLSessionTask *)task completionHandler:(void (^)(NSArray *cookies))completionHandler ``` |
| To | ``` - (void)getCookiesForTask:(NSURLSessionTask * _Nonnull)task completionHandler:(void (^ _Nonnull)(NSArray<NSHTTPCookie *> * _Nullable cookies))completionHandler ``` |

Modified [-[NSHTTPCookieStorage setCookies:forURL:mainDocumentURL:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1412510-setcookies)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setCookies:(NSArray *)cookies forURL:(NSURL *)URL mainDocumentURL:(NSURL *)mainDocumentURL ``` |
| To | ``` - (void)setCookies:(NSArray<NSHTTPCookie *> * _Nonnull)cookies forURL:(NSURL * _Nullable)URL mainDocumentURL:(NSURL * _Nullable)mainDocumentURL ``` |

Modified [-[NSHTTPCookieStorage sortedCookiesUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nshttpcookiestorage/1413730-sortedcookiesusingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedCookiesUsingDescriptors:(NSArray *)sortOrder ``` |
| To | ``` - (NSArray<NSHTTPCookie *> * _Nonnull)sortedCookiesUsingDescriptors:(NSArray<NSSortDescriptor *> * _Nonnull)sortOrder ``` |

Modified [-[NSHTTPCookieStorage storeCookies:forTask:]](https://developer.apple.com/documentation/foundation/httpcookiestorage/1415381-storecookies)

|  | Declaration |
| --- | --- |
| From | ``` - (void)storeCookies:(NSArray *)cookies forTask:(NSURLSessionTask *)task ``` |
| To | ``` - (void)storeCookies:(NSArray<NSHTTPCookie *> * _Nonnull)cookies forTask:(NSURLSessionTask * _Nonnull)task ``` |

#### NSIndexPath.h

Added [-[NSIndexPath getIndexes:range:]](https://developer.apple.com/documentation/foundation/nsindexpath/1413360-getindexes)Added NSIndexPath(NSDeprecated)Modified [-[NSIndexPath getIndexes:]](https://developer.apple.com/documentation/foundation/nsindexpath/1417753-getindexes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### NSItemProvider.h

Added [NSItemProviderUnavailableCoercionError](https://developer.apple.com/documentation/foundation/nsitemprovider/errorcode/unavailablecoercionerror)

#### NSKeyedArchiver.h

Removed [-[NSKeyedArchiver setRequiresSecureCoding:]](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417084-requiressecurecoding)Removed [-[NSKeyedUnarchiver setRequiresSecureCoding:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410824-requiressecurecoding)Added [NSKeyedArchiver.requiresSecureCoding](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417084-requiressecurecoding)Added [NSKeyedUnarchiver.requiresSecureCoding](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410824-requiressecurecoding)Added [+[NSKeyedUnarchiver unarchiveTopLevelObjectWithData:error:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1574811-unarchivetoplevelobjectwithdata)Modified [-[NSKeyedUnarchiverDelegate unarchiver:cannotDecodeObjectOfClassName:originalClasses:]](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/1409948-unarchiver)

|  | Declaration |
| --- | --- |
| From | ``` - (Class)unarchiver:(NSKeyedUnarchiver *)unarchiver cannotDecodeObjectOfClassName:(NSString *)name originalClasses:(NSArray *)classNames ``` |
| To | ``` - (Class _Nullable)unarchiver:(NSKeyedUnarchiver * _Nonnull)unarchiver cannotDecodeObjectOfClassName:(NSString * _Nonnull)name originalClasses:(NSArray<NSString *> * _Nonnull)classNames ``` |

Modified [+[NSObject classFallbacksForKeyedArchiver]](https://developer.apple.com/documentation/objectivec/nsobject/1411048-classfallbacksforkeyedarchiver)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)classFallbacksForKeyedArchiver ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)classFallbacksForKeyedArchiver ``` |

#### NSKeyValueCoding.h

Modified [-[NSDictionary valueForKey:]](https://developer.apple.com/documentation/foundation/nsdictionary/1410210-value)

|  | Declaration |
| --- | --- |
| From | ``` - (id)valueForKey:(NSString *)key ``` |
| To | ``` - (ObjectType _Nullable)valueForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSMutableDictionary setValue:forKey:]](https://developer.apple.com/documentation/foundation/nsmutabledictionary/1416335-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setValue:(id)value forKey:(NSString *)key ``` |
| To | ``` - (void)setValue:(ObjectType _Nullable)value forKey:(NSString * _Nonnull)key ``` |

Modified [-[NSObject dictionaryWithValuesForKeys:]](https://developer.apple.com/documentation/objectivec/nsobject/1411319-dictionarywithvalues)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)dictionaryWithValuesForKeys:(NSArray *)keys ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)dictionaryWithValuesForKeys:(NSArray<NSString *> * _Nonnull)keys ``` |

Modified [-[NSObject setValuesForKeysWithDictionary:]](https://developer.apple.com/documentation/objectivec/nsobject/1417515-setvaluesforkeyswithdictionary)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setValuesForKeysWithDictionary:(NSDictionary *)keyedValues ``` |
| To | ``` - (void)setValuesForKeysWithDictionary:(NSDictionary<NSString *,id> * _Nonnull)keyedValues ``` |

#### NSKeyValueObserving.h

Modified [+[NSObject keyPathsForValuesAffectingValueForKey:]](https://developer.apple.com/documentation/objectivec/nsobject/1414299-keypathsforvaluesaffectingvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (NSSet *)keyPathsForValuesAffectingValueForKey:(NSString *)key ``` |
| To | ``` + (NSSet<NSString *> * _Nonnull)keyPathsForValuesAffectingValueForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSObject observeValueForKeyPath:ofObject:change:context:]](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath)

|  | Declaration |
| --- | --- |
| From | ``` - (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context ``` |
| To | ``` - (void)observeValueForKeyPath:(NSString * _Nullable)keyPath ofObject:(id _Nullable)object change:(NSDictionary<NSString *,id> * _Nullable)change context:(void * _Nullable)context ``` |

#### NSLinguisticTagger.h

Modified [+[NSLinguisticTagger availableTagSchemesForLanguage:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1408694-availabletagschemesforlanguage)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableTagSchemesForLanguage:(NSString *)language ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)availableTagSchemesForLanguage:(NSString * _Nonnull)language ``` |

Modified [-[NSLinguisticTagger initWithTagSchemes:options:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1414576-initwithtagschemes)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithTagSchemes:(NSArray *)tagSchemes options:(NSUInteger)opts ``` |
| To | ``` - (instancetype _Nonnull)initWithTagSchemes:(NSArray<NSString *> * _Nonnull)tagSchemes options:(NSUInteger)opts ``` |

Modified [-[NSLinguisticTagger possibleTagsAtIndex:scheme:tokenRange:sentenceRange:scores:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1408537-possibletags)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)possibleTagsAtIndex:(NSUInteger)charIndex scheme:(NSString *)tagScheme tokenRange:(NSRangePointer)tokenRange sentenceRange:(NSRangePointer)sentenceRange scores:(NSArray **)scores ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)possibleTagsAtIndex:(NSUInteger)charIndex scheme:(NSString * _Nonnull)tagScheme tokenRange:(NSRangePointer _Nullable)tokenRange sentenceRange:(NSRangePointer _Nullable)sentenceRange scores:(NSArray<NSValue *> * _Nullable * _Nullable)scores ``` |

Modified [NSLinguisticTagger.tagSchemes](https://developer.apple.com/documentation/foundation/nslinguistictagger/1409018-tagschemes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *tagSchemes ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *tagSchemes ``` |

Modified [-[NSLinguisticTagger tagsInRange:scheme:options:tokenRanges:]](https://developer.apple.com/documentation/foundation/nslinguistictagger/1417826-tags)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)tagsInRange:(NSRange)range scheme:(NSString *)tagScheme options:(NSLinguisticTaggerOptions)opts tokenRanges:(NSArray **)tokenRanges ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)tagsInRange:(NSRange)range scheme:(NSString * _Nonnull)tagScheme options:(NSLinguisticTaggerOptions)opts tokenRanges:(NSArray<NSValue *> * _Nullable * _Nullable)tokenRanges ``` |

Modified [-[NSString linguisticTagsInRange:scheme:options:orthography:tokenRanges:]](https://developer.apple.com/documentation/foundation/nsstring/1416530-linguistictagsinrange)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)linguisticTagsInRange:(NSRange)range scheme:(NSString *)tagScheme options:(NSLinguisticTaggerOptions)opts orthography:(NSOrthography *)orthography tokenRanges:(NSArray **)tokenRanges ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)linguisticTagsInRange:(NSRange)range scheme:(NSString * _Nonnull)tagScheme options:(NSLinguisticTaggerOptions)opts orthography:(NSOrthography * _Nullable)orthography tokenRanges:(NSArray<NSValue *> * _Nullable * _Nullable)tokenRanges ``` |

#### NSLocale.h

Modified [+[NSLocale availableLocaleIdentifiers]](https://developer.apple.com/documentation/foundation/nslocale/1410448-availablelocaleidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableLocaleIdentifiers ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)availableLocaleIdentifiers ``` |

Modified [+[NSLocale commonISOCurrencyCodes]](https://developer.apple.com/documentation/foundation/nslocale/1407272-commonisocurrencycodes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)commonISOCurrencyCodes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)commonISOCurrencyCodes ``` |

Modified [+[NSLocale componentsFromLocaleIdentifier:]](https://developer.apple.com/documentation/foundation/nslocale/1409220-componentsfromlocaleidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)componentsFromLocaleIdentifier:(NSString *)string ``` |
| To | ``` + (NSDictionary<NSString *,NSString *> * _Nonnull)componentsFromLocaleIdentifier:(NSString * _Nonnull)string ``` |

Modified [+[NSLocale ISOCountryCodes]](https://developer.apple.com/documentation/foundation/nslocale/1413869-isocountrycodes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)ISOCountryCodes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)ISOCountryCodes ``` |

Modified [+[NSLocale ISOCurrencyCodes]](https://developer.apple.com/documentation/foundation/nslocale/1417834-isocurrencycodes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)ISOCurrencyCodes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)ISOCurrencyCodes ``` |

Modified [+[NSLocale ISOLanguageCodes]](https://developer.apple.com/documentation/foundation/nslocale/1418015-isolanguagecodes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)ISOLanguageCodes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)ISOLanguageCodes ``` |

Modified [+[NSLocale localeIdentifierFromComponents:]](https://developer.apple.com/documentation/foundation/nslocale/1412439-localeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (NSString *)localeIdentifierFromComponents:(NSDictionary *)dict ``` |
| To | ``` + (NSString * _Nonnull)localeIdentifierFromComponents:(NSDictionary<NSString *,NSString *> * _Nonnull)dict ``` |

Modified [+[NSLocale preferredLanguages]](https://developer.apple.com/documentation/foundation/nslocale/1415614-preferredlanguages)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)preferredLanguages ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)preferredLanguages ``` |

#### NSMapTable.h

Removed [NSMapTableCopyIn](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptablecopyin)Removed [NSMapTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptableobjectpointerpersonality)Removed [NSMapTableStrongMemory](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptablestrongmemory)Removed [NSMapTableWeakMemory](https://developer.apple.com/documentation/foundation/nsmaptableoptions/nsmaptableweakmemory)Added [NSMapTableCopyIn](https://developer.apple.com/documentation/foundation/nsmaptablecopyin)Added [NSMapTableObjectPointerPersonality](https://developer.apple.com/documentation/foundation/nsmaptableobjectpointerpersonality)Added [NSMapTableStrongMemory](https://developer.apple.com/documentation/foundation/nsmaptablestrongmemory)Added [NSMapTableWeakMemory](https://developer.apple.com/documentation/foundation/nsmaptableweakmemory)Modified [-[NSMapTable dictionaryRepresentation]](https://developer.apple.com/documentation/foundation/nsmaptable/1391402-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)dictionaryRepresentation ``` |
| To | ``` - (NSDictionary<KeyType,ObjectType> * _Nonnull)dictionaryRepresentation ``` |

Modified [-[NSMapTable keyEnumerator]](https://developer.apple.com/documentation/foundation/nsmaptable/1391398-keyenumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)keyEnumerator ``` |
| To | ``` - (NSEnumerator<KeyType> * _Nonnull)keyEnumerator ``` |

Modified [+[NSMapTable mapTableWithKeyOptions:valueOptions:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391414-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMapTable *)mapTableWithKeyOptions:(NSPointerFunctionsOptions)keyOptions valueOptions:(NSPointerFunctionsOptions)valueOptions ``` |
| To | ``` + (NSMapTable<KeyType,ObjectType> * _Nonnull)mapTableWithKeyOptions:(NSPointerFunctionsOptions)keyOptions valueOptions:(NSPointerFunctionsOptions)valueOptions ``` |

Modified [-[NSMapTable objectEnumerator]](https://developer.apple.com/documentation/foundation/nsmaptable/1391400-objectenumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)objectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nullable)objectEnumerator ``` |

Modified [-[NSMapTable objectForKey:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391444-objectforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKey:(id)aKey ``` |
| To | ``` - (ObjectType _Nullable)objectForKey:(KeyType _Nullable)aKey ``` |

Modified [-[NSMapTable removeObjectForKey:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391461-removeobjectforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectForKey:(id)aKey ``` |
| To | ``` - (void)removeObjectForKey:(KeyType _Nullable)aKey ``` |

Modified [-[NSMapTable setObject:forKey:]](https://developer.apple.com/documentation/foundation/nsmaptable/1391457-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)anObject forKey:(id)aKey ``` |
| To | ``` - (void)setObject:(ObjectType _Nullable)anObject forKey:(KeyType _Nullable)aKey ``` |

Modified [+[NSMapTable strongToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391440-strongtostrongobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMapTable *)strongToStrongObjectsMapTable ``` |
| To | ``` + (NSMapTable<KeyType,ObjectType> * _Nonnull)strongToStrongObjectsMapTable ``` |

Modified [+[NSMapTable strongToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391366-strongtoweakobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMapTable *)strongToWeakObjectsMapTable ``` |
| To | ``` + (NSMapTable<KeyType,ObjectType> * _Nonnull)strongToWeakObjectsMapTable ``` |

Modified [+[NSMapTable weakToStrongObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391346-weaktostrongobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMapTable *)weakToStrongObjectsMapTable ``` |
| To | ``` + (NSMapTable<KeyType,ObjectType> * _Nonnull)weakToStrongObjectsMapTable ``` |

Modified [+[NSMapTable weakToWeakObjectsMapTable]](https://developer.apple.com/documentation/foundation/nsmaptable/1391430-weaktoweakobjectsmaptable)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMapTable *)weakToWeakObjectsMapTable ``` |
| To | ``` + (NSMapTable<KeyType,ObjectType> * _Nonnull)weakToWeakObjectsMapTable ``` |

#### NSMetadata.h

Modified [NSMetadataItem.attributes](https://developer.apple.com/documentation/foundation/nsmetadataitem/1418347-attributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *attributes ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *attributes ``` |

Modified [-[NSMetadataItem valuesForAttributes:]](https://developer.apple.com/documentation/foundation/nsmetadataitem/1409934-valuesforattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)valuesForAttributes:(NSArray *)keys ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)valuesForAttributes:(NSArray<NSString *> * _Nonnull)keys ``` |

Modified [NSMetadataQuery.groupedResults](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416579-groupedresults)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *groupedResults ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSMetadataQueryResultGroup *> *groupedResults ``` |

Modified [NSMetadataQuery.groupingAttributes](https://developer.apple.com/documentation/foundation/nsmetadataquery/1409191-groupingattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *groupingAttributes ``` |
| To | ``` @property(copy, nullable) NSArray<NSString *> *groupingAttributes ``` |

Modified [NSMetadataQuery.sortDescriptors](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *sortDescriptors ``` |
| To | ``` @property(copy, nonnull) NSArray<NSSortDescriptor *> *sortDescriptors ``` |

Modified [NSMetadataQuery.valueListAttributes](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407767-valuelistattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *valueListAttributes ``` |
| To | ``` @property(copy, nonnull) NSArray<NSString *> *valueListAttributes ``` |

Modified [NSMetadataQuery.valueLists](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418401-valuelists)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *valueLists ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSArray<NSMetadataQueryAttributeValueTuple *> *> *valueLists ``` |

Modified [NSMetadataQueryResultGroup.subgroups](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/1409929-subgroups)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *subgroups ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSMetadataQueryResultGroup *> *subgroups ``` |

#### NSNetServices.h

Modified [NSNetService.addresses](https://developer.apple.com/documentation/foundation/netservice/1408528-addresses)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *addresses ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSData *> *addresses ``` |

Modified [+[NSNetService dataFromTXTRecordDictionary:]](https://developer.apple.com/documentation/foundation/netservice/1413150-data)

|  | Declaration |
| --- | --- |
| From | ``` + (NSData *)dataFromTXTRecordDictionary:(NSDictionary *)txtDictionary ``` |
| To | ``` + (NSData * _Nonnull)dataFromTXTRecordDictionary:(NSDictionary<NSString *,NSData *> * _Nonnull)txtDictionary ``` |

Modified [+[NSNetService dictionaryFromTXTRecordData:]](https://developer.apple.com/documentation/foundation/netservice/1408164-dictionary)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)dictionaryFromTXTRecordData:(NSData *)txtData ``` |
| To | ``` + (NSDictionary<NSString *,NSData *> * _Nonnull)dictionaryFromTXTRecordData:(NSData * _Nonnull)txtData ``` |

Modified [-[NSNetService initWithDomain:type:name:port:]](https://developer.apple.com/documentation/foundation/nsnetservice/1413364-initwithdomain)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didFindDomain:moreComing:]](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/1407204-netservicebrowser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didFindDomain:(NSString *)domainString moreComing:(BOOL)moreComing ``` |
| To | ``` - (void)netServiceBrowser:(NSNetServiceBrowser * _Nonnull)browser didFindDomain:(NSString * _Nonnull)domainString moreComing:(BOOL)moreComing ``` |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didFindService:moreComing:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1417979-netservicebrowser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didFindService:(NSNetService *)aNetService moreComing:(BOOL)moreComing ``` |
| To | ``` - (void)netServiceBrowser:(NSNetServiceBrowser * _Nonnull)browser didFindService:(NSNetService * _Nonnull)service moreComing:(BOOL)moreComing ``` |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didNotSearch:]](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/1410567-netservicebrowser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didNotSearch:(NSDictionary *)errorDict ``` |
| To | ``` - (void)netServiceBrowser:(NSNetServiceBrowser * _Nonnull)browser didNotSearch:(NSDictionary<NSString *,NSNumber *> * _Nonnull)errorDict ``` |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didRemoveDomain:moreComing:]](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/1412712-netservicebrowser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didRemoveDomain:(NSString *)domainString moreComing:(BOOL)moreComing ``` |
| To | ``` - (void)netServiceBrowser:(NSNetServiceBrowser * _Nonnull)browser didRemoveDomain:(NSString * _Nonnull)domainString moreComing:(BOOL)moreComing ``` |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowser:didRemoveService:moreComing:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1412917-netservicebrowser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didRemoveService:(NSNetService *)aNetService moreComing:(BOOL)moreComing ``` |
| To | ``` - (void)netServiceBrowser:(NSNetServiceBrowser * _Nonnull)browser didRemoveService:(NSNetService * _Nonnull)service moreComing:(BOOL)moreComing ``` |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowserDidStopSearch:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1418341-netservicebrowserdidstopsearch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netServiceBrowserDidStopSearch:(NSNetServiceBrowser *)aNetServiceBrowser ``` |
| To | ``` - (void)netServiceBrowserDidStopSearch:(NSNetServiceBrowser * _Nonnull)browser ``` |

Modified [-[NSNetServiceBrowserDelegate netServiceBrowserWillSearch:]](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1408173-netservicebrowserwillsearch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netServiceBrowserWillSearch:(NSNetServiceBrowser *)aNetServiceBrowser ``` |
| To | ``` - (void)netServiceBrowserWillSearch:(NSNetServiceBrowser * _Nonnull)browser ``` |

Modified [-[NSNetServiceDelegate netService:didNotPublish:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1417101-netservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netService:(NSNetService *)sender didNotPublish:(NSDictionary *)errorDict ``` |
| To | ``` - (void)netService:(NSNetService * _Nonnull)sender didNotPublish:(NSDictionary<NSString *,NSNumber *> * _Nonnull)errorDict ``` |

Modified [-[NSNetServiceDelegate netService:didNotResolve:]](https://developer.apple.com/documentation/foundation/nsnetservicedelegate/1414161-netservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)netService:(NSNetService *)sender didNotResolve:(NSDictionary *)errorDict ``` |
| To | ``` - (void)netService:(NSNetService * _Nonnull)sender didNotResolve:(NSDictionary<NSString *,NSNumber *> * _Nonnull)errorDict ``` |

#### NSNotificationQueue.h

Modified [-[NSNotificationQueue enqueueNotification:postingStyle:coalesceMask:forModes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/instm/NSNotificationQueue/enqueueNotification:postingStyle:coalesceMask:forModes:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enqueueNotification:(NSNotification *)notification postingStyle:(NSPostingStyle)postingStyle coalesceMask:(NSUInteger)coalesceMask forModes:(NSArray *)modes ``` |
| To | ``` - (void)enqueueNotification:(NSNotification * _Nonnull)notification postingStyle:(NSPostingStyle)postingStyle coalesceMask:(NSNotificationCoalescing)coalesceMask forModes:(NSArray<NSString *> * _Nullable)modes ``` |

#### NSNumberFormatter.h

Added [NSNumberFormatterCurrencyAccountingStyle](https://developer.apple.com/documentation/foundation/nsnumberformatterstyle/nsnumberformattercurrencyaccountingstyle)Added [NSNumberFormatterCurrencyISOCodeStyle](https://developer.apple.com/documentation/foundation/nsnumberformatterstyle/nsnumberformattercurrencyisocodestyle)Added [NSNumberFormatterCurrencyPluralStyle](https://developer.apple.com/documentation/foundation/nsnumberformatterstyle/nsnumberformattercurrencypluralstyle)Added [NSNumberFormatterOrdinalStyle](https://developer.apple.com/documentation/foundation/nsnumberformatterstyle/nsnumberformatterordinalstyle)Modified [NSNumberFormatter.textAttributesForNegativeInfinity](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410417-textattributesfornegativeinfinit)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *textAttributesForNegativeInfinity ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *textAttributesForNegativeInfinity ``` |

Modified [NSNumberFormatter.textAttributesForNegativeValues](https://developer.apple.com/documentation/foundation/nsnumberformatter/1414530-textattributesfornegativevalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *textAttributesForNegativeValues ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *textAttributesForNegativeValues ``` |

Modified [NSNumberFormatter.textAttributesForNil](https://developer.apple.com/documentation/foundation/numberformatter/1408943-textattributesfornil)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *textAttributesForNil ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *textAttributesForNil ``` |

Modified [NSNumberFormatter.textAttributesForNotANumber](https://developer.apple.com/documentation/foundation/nsnumberformatter/1410959-textattributesfornotanumber)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *textAttributesForNotANumber ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *textAttributesForNotANumber ``` |

Modified [NSNumberFormatter.textAttributesForPositiveInfinity](https://developer.apple.com/documentation/foundation/nsnumberformatter/1408176-textattributesforpositiveinfinit)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *textAttributesForPositiveInfinity ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *textAttributesForPositiveInfinity ``` |

Modified [NSNumberFormatter.textAttributesForPositiveValues](https://developer.apple.com/documentation/foundation/nsnumberformatter/1409563-textattributesforpositivevalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *textAttributesForPositiveValues ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *textAttributesForPositiveValues ``` |

Modified [NSNumberFormatter.textAttributesForZero](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415971-textattributesforzero)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *textAttributesForZero ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *textAttributesForZero ``` |

#### NSObjCRuntime.h

Removed [NSNotFound](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSNotFound)Added #def NS_REFINED_FOR_SWIFTAdded #def NS_SWIFT_NAMEAdded #def NS_SWIFT_NOTHROWAdded #def NS_SWIFT_UNAVAILABLEAdded [#def NSFoundationVersionNumber10_10](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10)Added [#def NSFoundationVersionNumber10_10_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_1)Added [#def NSFoundationVersionNumber10_10_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_2)Added [#def NSFoundationVersionNumber10_10_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_10_3)Added [#def NSFoundationVersionNumber_iOS_8_0](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_0)Added [#def NSFoundationVersionNumber_iOS_8_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_1)Added [#def NSFoundationVersionNumber_iOS_8_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_2)Added [#def NSFoundationVersionNumber_iOS_8_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_8_3)Added [NSNotFound](https://developer.apple.com/documentation/foundation/nsnotfound)Modified #def NS_DESIGNATED_INITIALIZER

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

#### NSObject.h

Modified [-[NSCoding initWithCoder:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCoding/Description.html#//apple_ref/occ/intfm/NSCoding/initWithCoder:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nullable)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

#### NSOperation.h

Removed NSOperationQueueDefaultMaxConcurrentOperationCountAdded [NSOperationQueueDefaultMaxConcurrentOperationCount](https://developer.apple.com/documentation/foundation/operationqueue/1411680-defaultmaxconcurrentoperationcou)Modified [NSBlockOperation.executionBlocks](https://developer.apple.com/documentation/foundation/nsblockoperation/1416555-executionblocks)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *executionBlocks ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<void (^executionBlocks)(void)> * ``` |

Modified [NSOperation.dependencies](https://developer.apple.com/documentation/foundation/operation/1416668-dependencies)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *dependencies ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSOperation *> *dependencies ``` |

Modified [-[NSOperationQueue addOperations:waitUntilFinished:]](https://developer.apple.com/documentation/foundation/operationqueue/1408358-addoperations)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOperations:(NSArray *)ops waitUntilFinished:(BOOL)wait ``` |
| To | ``` - (void)addOperations:(NSArray<NSOperation *> * _Nonnull)ops waitUntilFinished:(BOOL)wait ``` |

Modified [NSOperationQueue.operations](https://developer.apple.com/documentation/foundation/operationqueue/1415168-operations)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *operations ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<__kindof NSOperation *> *operations ``` |

#### NSOrderedSet.h

Modified [-[NSMutableOrderedSet addObject:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1408009-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObject:(id)object ``` |
| To | ``` - (void)addObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSMutableOrderedSet addObjects:count:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1413840-addobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObjects:(const id [])objects count:(NSUInteger)count ``` |
| To | ``` - (void)addObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)count ``` |

Modified [-[NSMutableOrderedSet addObjectsFromArray:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1417200-addobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObjectsFromArray:(NSArray *)array ``` |
| To | ``` - (void)addObjectsFromArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [-[NSMutableOrderedSet insertObject:atIndex:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1416634-insertobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertObject:(id)object atIndex:(NSUInteger)idx ``` |
| To | ``` - (void)insertObject:(ObjectType _Nonnull)object atIndex:(NSUInteger)idx ``` |

Modified [-[NSMutableOrderedSet insertObjects:atIndexes:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410287-insert)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertObjects:(NSArray *)objects atIndexes:(NSIndexSet *)indexes ``` |
| To | ``` - (void)insertObjects:(NSArray<ObjectType> * _Nonnull)objects atIndexes:(NSIndexSet * _Nonnull)indexes ``` |

Modified [-[NSMutableOrderedSet intersectOrderedSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1408541-intersect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)intersectOrderedSet:(NSOrderedSet *)other ``` |
| To | ``` - (void)intersectOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSMutableOrderedSet intersectSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1415257-intersectset)

|  | Declaration |
| --- | --- |
| From | ``` - (void)intersectSet:(NSSet *)other ``` |
| To | ``` - (void)intersectSet:(NSSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSMutableOrderedSet minusOrderedSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1407987-minusorderedset)

|  | Declaration |
| --- | --- |
| From | ``` - (void)minusOrderedSet:(NSOrderedSet *)other ``` |
| To | ``` - (void)minusOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSMutableOrderedSet minusSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411229-minusset)

|  | Declaration |
| --- | --- |
| From | ``` - (void)minusSet:(NSSet *)other ``` |
| To | ``` - (void)minusSet:(NSSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSMutableOrderedSet removeObject:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1416776-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObject:(id)object ``` |
| To | ``` - (void)removeObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSMutableOrderedSet removeObjectsInArray:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411635-removeobjectsinarray)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObjectsInArray:(NSArray *)array ``` |
| To | ``` - (void)removeObjectsInArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [-[NSMutableOrderedSet replaceObjectAtIndex:withObject:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1412115-replaceobjectatindex)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceObjectAtIndex:(NSUInteger)idx withObject:(id)object ``` |
| To | ``` - (void)replaceObjectAtIndex:(NSUInteger)idx withObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSMutableOrderedSet replaceObjectsAtIndexes:withObjects:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1416127-replaceobjectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceObjectsAtIndexes:(NSIndexSet *)indexes withObjects:(NSArray *)objects ``` |
| To | ``` - (void)replaceObjectsAtIndexes:(NSIndexSet * _Nonnull)indexes withObjects:(NSArray<ObjectType> * _Nonnull)objects ``` |

Modified [-[NSMutableOrderedSet replaceObjectsInRange:withObjects:count:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1415340-replaceobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceObjectsInRange:(NSRange)range withObjects:(const id [])objects count:(NSUInteger)count ``` |
| To | ``` - (void)replaceObjectsInRange:(NSRange)range withObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)count ``` |

Modified [-[NSMutableOrderedSet setObject:atIndex:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1411158-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)obj atIndex:(NSUInteger)idx ``` |
| To | ``` - (void)setObject:(ObjectType _Nonnull)obj atIndex:(NSUInteger)idx ``` |

Modified [-[NSMutableOrderedSet setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1543323-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id)obj atIndexedSubscript:(NSUInteger)idx ``` |
| To | ``` - (void)setObject:(ObjectType _Nonnull)obj atIndexedSubscript:(NSUInteger)idx ``` |

Modified [-[NSMutableOrderedSet unionOrderedSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410973-unionorderedset)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unionOrderedSet:(NSOrderedSet *)other ``` |
| To | ``` - (void)unionOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSMutableOrderedSet unionSet:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1413853-unionset)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unionSet:(NSSet *)other ``` |
| To | ``` - (void)unionSet:(NSSet<ObjectType> * _Nonnull)other ``` |

Modified [NSOrderedSet.array](https://developer.apple.com/documentation/foundation/nsorderedset/1411531-array)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *array ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray<ObjectType> *array ``` |

Modified [-[NSOrderedSet containsObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408681-containsobject)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsObject:(id)object ``` |
| To | ``` - (BOOL)containsObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSOrderedSet enumerateObjectsAtIndexes:options:usingBlock:]](https://developer.apple.com/documentation/foundation/nsorderedset/1412332-enumerateobjectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsAtIndexes:(NSIndexSet *)s options:(NSEnumerationOptions)opts usingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsAtIndexes:(NSIndexSet * _Nonnull)s options:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [-[NSOrderedSet enumerateObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413531-enumerateobjectsusingblock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsUsingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsUsingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [-[NSOrderedSet enumerateObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409354-enumerateobjectswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [NSOrderedSet.firstObject](https://developer.apple.com/documentation/foundation/nsorderedset/1409765-firstobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id firstObject ``` |
| To | ``` @property(nonatomic, readonly, nullable) ObjectType firstObject ``` |

Modified [-[NSOrderedSet getObjects:range:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411401-getobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getObjects:(id [])objects range:(NSRange)range ``` |
| To | ``` - (void)getObjects:(ObjectType  _Nonnull [])objects range:(NSRange)range ``` |

Modified [-[NSOrderedSet indexesOfObjectsAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413586-indexesofobjectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexSet *)indexesOfObjectsAtIndexes:(NSIndexSet *)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSIndexSet * _Nonnull)indexesOfObjectsAtIndexes:(NSIndexSet * _Nonnull)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSOrderedSet indexesOfObjectsPassingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411331-indexes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexSet *)indexesOfObjectsPassingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSIndexSet * _Nonnull)indexesOfObjectsPassingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSOrderedSet indexesOfObjectsWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1415944-indexes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexSet *)indexesOfObjectsWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSIndexSet * _Nonnull)indexesOfObjectsWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSOrderedSet indexOfObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411856-indexofobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObject:(id)object ``` |
| To | ``` - (NSUInteger)indexOfObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSOrderedSet indexOfObject:inSortedRange:options:usingComparator:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417701-index)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObject:(id)object inSortedRange:(NSRange)range options:(NSBinarySearchingOptions)opts usingComparator:(NSComparator)cmp ``` |
| To | ``` - (NSUInteger)indexOfObject:(ObjectType _Nonnull)object inSortedRange:(NSRange)range options:(NSBinarySearchingOptions)opts usingComparator:(NSComparator _Nonnull)cmp ``` |

Modified [-[NSOrderedSet indexOfObjectAtIndexes:options:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417531-index)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectAtIndexes:(NSIndexSet *)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSUInteger)indexOfObjectAtIndexes:(NSIndexSet * _Nonnull)s options:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSOrderedSet indexOfObjectPassingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413003-index)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectPassingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSUInteger)indexOfObjectPassingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSOrderedSet indexOfObjectWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408700-indexofobjectwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObjectWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, NSUInteger idx, BOOL *stop))predicate ``` |
| To | ``` - (NSUInteger)indexOfObjectWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSOrderedSet initWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408623-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithArray:(NSArray *)array ``` |
| To | ``` - (instancetype _Nonnull)initWithArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [-[NSOrderedSet initWithArray:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1418006-initwitharray)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithArray:(NSArray *)set copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithArray:(NSArray<ObjectType> * _Nonnull)set copyItems:(BOOL)flag ``` |

Modified [-[NSOrderedSet initWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409272-initwitharray)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithArray:(NSArray *)set range:(NSRange)range copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithArray:(NSArray<ObjectType> * _Nonnull)set range:(NSRange)range copyItems:(BOOL)flag ``` |

Modified [-[NSOrderedSet initWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413883-initwithobject)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObject:(id)object ``` |
| To | ``` - (instancetype _Nonnull)initWithObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSOrderedSet initWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543287-initwithobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(id)firstObj, ... ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(ObjectType _Nonnull)firstObj, ... ``` |

Modified [-[NSOrderedSet initWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411910-initwithobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |

Modified [-[NSOrderedSet initWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1412402-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithOrderedSet:(NSOrderedSet *)set ``` |
| To | ``` - (instancetype _Nonnull)initWithOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)set ``` |

Modified [-[NSOrderedSet initWithOrderedSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411658-initwithorderedset)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithOrderedSet:(NSOrderedSet *)set copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)set copyItems:(BOOL)flag ``` |

Modified [-[NSOrderedSet initWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1417751-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithOrderedSet:(NSOrderedSet *)set range:(NSRange)range copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)set range:(NSRange)range copyItems:(BOOL)flag ``` |

Modified [-[NSOrderedSet initWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1416344-initwithset)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSet:(NSSet *)set ``` |
| To | ``` - (instancetype _Nonnull)initWithSet:(NSSet<ObjectType> * _Nonnull)set ``` |

Modified [-[NSOrderedSet initWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411246-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSet:(NSSet *)set copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithSet:(NSSet<ObjectType> * _Nonnull)set copyItems:(BOOL)flag ``` |

Modified [-[NSOrderedSet intersectsOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414364-intersectsorderedset)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)intersectsOrderedSet:(NSOrderedSet *)other ``` |
| To | ``` - (BOOL)intersectsOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSOrderedSet intersectsSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408625-intersectsset)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)intersectsSet:(NSSet *)set ``` |
| To | ``` - (BOOL)intersectsSet:(NSSet<ObjectType> * _Nonnull)set ``` |

Modified [-[NSOrderedSet isEqualToOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1408049-isequal)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToOrderedSet:(NSOrderedSet *)other ``` |
| To | ``` - (BOOL)isEqualToOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSOrderedSet isSubsetOfOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1411496-issubset)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isSubsetOfOrderedSet:(NSOrderedSet *)other ``` |
| To | ``` - (BOOL)isSubsetOfOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)other ``` |

Modified [-[NSOrderedSet isSubsetOfSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1418464-issubsetofset)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isSubsetOfSet:(NSSet *)set ``` |
| To | ``` - (BOOL)isSubsetOfSet:(NSSet<ObjectType> * _Nonnull)set ``` |

Modified [NSOrderedSet.lastObject](https://developer.apple.com/documentation/foundation/nsorderedset/1409143-lastobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id lastObject ``` |
| To | ``` @property(nonatomic, readonly, nullable) ObjectType lastObject ``` |

Modified [-[NSOrderedSet objectAtIndex:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414734-objectatindex)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtIndex:(NSUInteger)idx ``` |
| To | ``` - (ObjectType _Nonnull)objectAtIndex:(NSUInteger)idx ``` |

Modified [-[NSOrderedSet objectAtIndexedSubscript:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414253-subscript)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtIndexedSubscript:(NSUInteger)idx ``` |
| To | ``` - (ObjectType _Nonnull)objectAtIndexedSubscript:(NSUInteger)idx ``` |

Modified [-[NSOrderedSet objectEnumerator]](https://developer.apple.com/documentation/foundation/nsorderedset/1409430-objectenumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)objectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)objectEnumerator ``` |

Modified [-[NSOrderedSet objectsAtIndexes:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414943-objects)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)objectsAtIndexes:(NSIndexSet *)indexes ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)objectsAtIndexes:(NSIndexSet * _Nonnull)indexes ``` |

Modified [+[NSOrderedSet orderedSetWithArray:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543310-orderedsetwitharray)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithArray:(NSArray *)array ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [+[NSOrderedSet orderedSetWithArray:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543321-orderedsetwitharray)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithArray:(NSArray *)array range:(NSRange)range copyItems:(BOOL)flag ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithArray:(NSArray<ObjectType> * _Nonnull)array range:(NSRange)range copyItems:(BOOL)flag ``` |

Modified [+[NSOrderedSet orderedSetWithObject:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543339-orderedsetwithobject)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithObject:(id)object ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithObject:(ObjectType _Nonnull)object ``` |

Modified [+[NSOrderedSet orderedSetWithObjects:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543312-orderedsetwithobjects)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithObjects:(id)firstObj, ... ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithObjects:(ObjectType _Nonnull)firstObj, ... ``` |

Modified [+[NSOrderedSet orderedSetWithObjects:count:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543334-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithObjects:(const id [])objects count:(NSUInteger)cnt ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |

Modified [+[NSOrderedSet orderedSetWithOrderedSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543280-orderedsetwithorderedset)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithOrderedSet:(NSOrderedSet *)set ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)set ``` |

Modified [+[NSOrderedSet orderedSetWithOrderedSet:range:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543292-orderedsetwithorderedset)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithOrderedSet:(NSOrderedSet *)set range:(NSRange)range copyItems:(BOOL)flag ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithOrderedSet:(NSOrderedSet<ObjectType> * _Nonnull)set range:(NSRange)range copyItems:(BOOL)flag ``` |

Modified [+[NSOrderedSet orderedSetWithSet:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543298-orderedsetwithset)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithSet:(NSSet *)set ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithSet:(NSSet<ObjectType> * _Nonnull)set ``` |

Modified [+[NSOrderedSet orderedSetWithSet:copyItems:]](https://developer.apple.com/documentation/foundation/nsorderedset/1543331-orderedsetwithset)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orderedSetWithSet:(NSSet *)set copyItems:(BOOL)flag ``` |
| To | ``` + (instancetype _Nonnull)orderedSetWithSet:(NSSet<ObjectType> * _Nonnull)set copyItems:(BOOL)flag ``` |

Modified [NSOrderedSet.reversedOrderedSet](https://developer.apple.com/documentation/foundation/nsorderedset/1411022-reversedorderedset)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSOrderedSet *reversedOrderedSet ``` |
| To | ``` @property(readonly, copy, nonnull) NSOrderedSet<ObjectType> *reversedOrderedSet ``` |

Modified [-[NSOrderedSet reverseObjectEnumerator]](https://developer.apple.com/documentation/foundation/nsorderedset/1407607-reverseobjectenumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)reverseObjectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)reverseObjectEnumerator ``` |

Modified [NSOrderedSet.set](https://developer.apple.com/documentation/foundation/nsorderedset/1413944-set)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSSet *set ``` |
| To | ``` @property(readonly, strong, nonnull) NSSet<ObjectType> *set ``` |

Modified [-[NSOrderedSet sortedArrayUsingComparator:]](https://developer.apple.com/documentation/foundation/nsorderedset/1413383-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingComparator:(NSComparator)cmptr ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingComparator:(NSComparator _Nonnull)cmptr ``` |

Modified [-[NSOrderedSet sortedArrayWithOptions:usingComparator:]](https://developer.apple.com/documentation/foundation/nsorderedset/1414806-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayWithOptions:(NSSortOptions)opts usingComparator:(NSComparator)cmptr ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayWithOptions:(NSSortOptions)opts usingComparator:(NSComparator _Nonnull)cmptr ``` |

#### NSOrthography.h

Modified [NSOrthography.allLanguages](https://developer.apple.com/documentation/foundation/nsorthography/1416205-alllanguages)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *allLanguages ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *allLanguages ``` |

Modified [NSOrthography.allScripts](https://developer.apple.com/documentation/foundation/nsorthography/1410722-allscripts)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *allScripts ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *allScripts ``` |

Modified [-[NSOrthography initWithDominantScript:languageMap:]](https://developer.apple.com/documentation/foundation/nsorthography/1408708-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDominantScript:(NSString *)script languageMap:(NSDictionary *)map ``` |
| To | ``` - (instancetype _Nonnull)initWithDominantScript:(NSString * _Nonnull)script languageMap:(NSDictionary<NSString *,NSArray<NSString *> *> * _Nonnull)map ``` |

Modified [NSOrthography.languageMap](https://developer.apple.com/documentation/foundation/nsorthography/1409533-languagemap)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *languageMap ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSArray<NSString *> *> *languageMap ``` |

Modified [-[NSOrthography languagesForScript:]](https://developer.apple.com/documentation/foundation/nsorthography/1412606-languages)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)languagesForScript:(NSString *)script ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)languagesForScript:(NSString * _Nonnull)script ``` |

Modified [+[NSOrthography orthographyWithDominantScript:languageMap:]](https://developer.apple.com/documentation/foundation/nsorthography/1585529-orthographywithdominantscript)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orthographyWithDominantScript:(NSString *)script languageMap:(NSDictionary *)map ``` |
| To | ``` + (instancetype _Nonnull)orthographyWithDominantScript:(NSString * _Nonnull)script languageMap:(NSDictionary<NSString *,NSArray<NSString *> *> * _Nonnull)map ``` |

#### NSPathUtilities.h

Modified [-[NSArray pathsMatchingExtensions:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/pathsMatchingExtensions:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)pathsMatchingExtensions:(NSArray *)filterTypes ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)pathsMatchingExtensions:(NSArray<NSString *> * _Nonnull)filterTypes ``` |

Modified [-[NSString completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)completePathIntoString:(NSString **)outputName caseSensitive:(BOOL)flag matchesIntoArray:(NSArray **)outputArray filterTypes:(NSArray *)filterTypes ``` |
| To | ``` - (NSUInteger)completePathIntoString:(NSString * _Nonnull * _Nullable)outputName caseSensitive:(BOOL)flag matchesIntoArray:(NSArray<NSString *> * _Nonnull * _Nullable)outputArray filterTypes:(NSArray<NSString *> * _Nullable)filterTypes ``` |

Modified [NSString.pathComponents](https://developer.apple.com/documentation/foundation/nsstring/1414489-pathcomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *pathComponents ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *pathComponents ``` |

Modified [+[NSString pathWithComponents:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/pathWithComponents:)

|  | Declaration |
| --- | --- |
| From | ``` + (NSString *)pathWithComponents:(NSArray *)components ``` |
| To | ``` + (NSString * _Nonnull)pathWithComponents:(NSArray<NSString *> * _Nonnull)components ``` |

Modified [-[NSString stringsByAppendingPaths:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringsByAppendingPaths:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)stringsByAppendingPaths:(NSArray *)paths ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)stringsByAppendingPaths:(NSArray<NSString *> * _Nonnull)paths ``` |

Modified [NSSearchPathForDirectoriesInDomains()](https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma)

|  | Declaration |
| --- | --- |
| From | ``` NSArray * NSSearchPathForDirectoriesInDomains (     NSSearchPathDirectory directory,     NSSearchPathDomainMask domainMask,     BOOL expandTilde ); ``` |
| To | ``` NSArray<NSString *> * _Nonnull NSSearchPathForDirectoriesInDomains (     NSSearchPathDirectory directory,     NSSearchPathDomainMask domainMask,     BOOL expandTilde ); ``` |

#### NSPersonNameComponents.h (Added)

Added [NSPersonNameComponents](https://developer.apple.com/documentation/foundation/nspersonnamecomponents)Added [NSPersonNameComponents.familyName](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1413354-familyname)Added [NSPersonNameComponents.givenName](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1407259-givenname)Added [NSPersonNameComponents.middleName](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1418183-middlename)Added [NSPersonNameComponents.namePrefix](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1410275-nameprefix)Added [NSPersonNameComponents.nameSuffix](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1410776-namesuffix)Added [NSPersonNameComponents.nickname](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1414892-nickname)Added [NSPersonNameComponents.phoneticRepresentation](https://developer.apple.com/documentation/foundation/nspersonnamecomponents/1412193-phoneticrepresentation)

#### NSPersonNameComponentsFormatter.h (Added)

Added [NSPersonNameComponentsFormatter](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter)Added [-[NSPersonNameComponentsFormatter annotatedStringFromPersonNameComponents:]](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1408241-annotatedstring)Added [-[NSPersonNameComponentsFormatter getObjectValue:forString:errorDescription:]](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1408262-getobjectvalue)Added [+[NSPersonNameComponentsFormatter localizedStringFromPersonNameComponents:style:options:]](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1408258-localizedstring)Added [NSPersonNameComponentsFormatter.phonetic](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1408242-isphonetic)Added [-[NSPersonNameComponentsFormatter stringFromPersonNameComponents:]](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1408243-string)Added [NSPersonNameComponentsFormatter.style](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatter/1408260-style)Added [NSPersonNameComponentDelimiter](https://developer.apple.com/documentation/foundation/nspersonnamecomponentdelimiter)Added [NSPersonNameComponentFamilyName](https://developer.apple.com/documentation/foundation/nspersonnamecomponentfamilyname)Added [NSPersonNameComponentGivenName](https://developer.apple.com/documentation/foundation/nspersonnamecomponentgivenname)Added [NSPersonNameComponentKey](https://developer.apple.com/documentation/foundation/nspersonnamecomponentkey)Added [NSPersonNameComponentMiddleName](https://developer.apple.com/documentation/foundation/nspersonnamecomponentmiddlename)Added [NSPersonNameComponentNickname](https://developer.apple.com/documentation/foundation/nspersonnamecomponentnickname)Added [NSPersonNameComponentPrefix](https://developer.apple.com/documentation/foundation/nspersonnamecomponentprefix)Added [NSPersonNameComponentsFormatterOptions](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatteroptions)Added [NSPersonNameComponentsFormatterPhonetic](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/options/1408240-phonetic)Added [NSPersonNameComponentsFormatterStyle](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle)Added [NSPersonNameComponentsFormatterStyleAbbreviated](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstyleabbreviated)Added [NSPersonNameComponentsFormatterStyleDefault](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstyledefault)Added [NSPersonNameComponentsFormatterStyleLong](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/style/long)Added [NSPersonNameComponentsFormatterStyleMedium](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsformatterstyle/nspersonnamecomponentsformatterstylemedium)Added [NSPersonNameComponentsFormatterStyleShort](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/style/short)Added [NSPersonNameComponentSuffix](https://developer.apple.com/documentation/foundation/nspersonnamecomponentsuffix)

#### NSPointerFunctions.h

Modified [NSPointerFunctions.acquireFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1410537-acquirefunction)

|  | Declaration |
| --- | --- |
| From | ``` @property void *(*acquireFunction)(const void *src, NSUInteger (*size)(const void *item), BOOL shouldCopy) ``` |
| To | ``` @property(nonnull) void * (* _Nullable)(const void * _Nonnull src, NSUInteger (* _Nullablesize)(const void * _Nonnull item), BOOL shouldCopy) acquireFunction ``` |

Modified [NSPointerFunctions.descriptionFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1415200-descriptionfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property NSString *(*descriptionFunction)(const void *item) ``` |
| To | ``` @property(nullable) NSString * (* _Nullable)(const void * _Nonnull item) descriptionFunction ``` |

#### NSPort.h

Added [NSMachPortOptions](https://developer.apple.com/documentation/foundation/nsmachportoptions)Modified [-[NSMachPort initWithMachPort:]](https://developer.apple.com/documentation/foundation/nsmachport/1399499-initwithmachport)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSMachPort initWithMachPort:options:]](https://developer.apple.com/documentation/foundation/nsmachport/1399559-initwithmachport)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithMachPort:(uint32_t)machPort options:(NSUInteger)f ``` |
| To | ``` - (instancetype _Nonnull)initWithMachPort:(uint32_t)machPort options:(NSMachPortOptions)f ``` |

Modified [+[NSMachPort portWithMachPort:options:]](https://developer.apple.com/documentation/foundation/nsmachport/1399551-portwithmachport)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPort *)portWithMachPort:(uint32_t)machPort options:(NSUInteger)f ``` |
| To | ``` + (NSPort * _Nonnull)portWithMachPort:(uint32_t)machPort options:(NSMachPortOptions)f ``` |

#### NSPredicate.h

Modified [-[NSArray filteredArrayUsingPredicate:]](https://developer.apple.com/documentation/foundation/nsarray/1411033-filtered)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)filteredArrayUsingPredicate:(NSPredicate *)predicate ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)filteredArrayUsingPredicate:(NSPredicate * _Nonnull)predicate ``` |

Modified [-[NSOrderedSet filteredOrderedSetUsingPredicate:]](https://developer.apple.com/documentation/foundation/nsorderedset/1415807-filtered)

|  | Declaration |
| --- | --- |
| From | ``` - (NSOrderedSet *)filteredOrderedSetUsingPredicate:(NSPredicate *)p ``` |
| To | ``` - (NSOrderedSet<ObjectType> * _Nonnull)filteredOrderedSetUsingPredicate:(NSPredicate * _Nonnull)p ``` |

Modified [-[NSPredicate evaluateWithObject:substitutionVariables:]](https://developer.apple.com/documentation/foundation/nspredicate/1407759-evaluatewithobject)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)evaluateWithObject:(id)object substitutionVariables:(NSDictionary *)bindings ``` |
| To | ``` - (BOOL)evaluateWithObject:(id _Nullable)object substitutionVariables:(NSDictionary<NSString *,id> * _Nullable)bindings ``` |

Modified [+[NSPredicate predicateWithBlock:]](https://developer.apple.com/documentation/foundation/nspredicate/1416182-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)predicateWithBlock:(BOOL (^)(id evaluatedObject, NSDictionary *bindings))block ``` |
| To | ``` + (NSPredicate * _Nonnull)predicateWithBlock:(BOOL (^ _Nonnull)(id _Nonnull evaluatedObject, NSDictionary<NSString *,id> * _Nullable bindings))block ``` |

Modified [-[NSPredicate predicateWithSubstitutionVariables:]](https://developer.apple.com/documentation/foundation/nspredicate/1413227-withsubstitutionvariables)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)predicateWithSubstitutionVariables:(NSDictionary *)variables ``` |
| To | ``` - (instancetype _Nonnull)predicateWithSubstitutionVariables:(NSDictionary<NSString *,id> * _Nonnull)variables ``` |

Modified [-[NSSet filteredSetUsingPredicate:]](https://developer.apple.com/documentation/foundation/nsset/1416324-filtered)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)filteredSetUsingPredicate:(NSPredicate *)predicate ``` |
| To | ``` - (NSSet<ObjectType> * _Nonnull)filteredSetUsingPredicate:(NSPredicate * _Nonnull)predicate ``` |

#### NSProcessInfo.h

Removed NSProcessInfo()Added [NSProcessInfo.lowPowerModeEnabled](https://developer.apple.com/documentation/foundation/nsprocessinfo/1617047-lowpowermodeenabled)Added NSProcessInfo(NSProcessInfoActivity)Added NSProcessInfo(NSProcessInfoPowerState)Added NSProcessInfo(NSProcessInfoThermalState)Added [NSProcessInfoPowerStateDidChangeNotification](https://developer.apple.com/documentation/foundation/nsprocessinfopowerstatedidchangenotification)Added [NSProcessInfoThermalState](https://developer.apple.com/documentation/foundation/nsprocessinfothermalstate)Modified [NSProcessInfo.arguments](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415596-arguments)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *arguments ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *arguments ``` |

Modified [NSProcessInfo.environment](https://developer.apple.com/documentation/foundation/processinfo/1417911-environment)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *environment ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSString *> *environment ``` |

#### NSProgress.h

Added [-[NSProgress addChild:withPendingUnitCount:]](https://developer.apple.com/documentation/foundation/progress/1417260-addchild)Added [+[NSProgress discreteProgressWithTotalUnitCount:]](https://developer.apple.com/documentation/foundation/nsprogress/1410951-discreteprogresswithtotalunitcou)Added [+[NSProgress progressWithTotalUnitCount:parent:pendingUnitCount:]](https://developer.apple.com/documentation/foundation/progress/1409014-init)Added [-[NSProgress resume]](https://developer.apple.com/documentation/foundation/nsprogress/1413616-resume)Added [NSProgress.resumingHandler](https://developer.apple.com/documentation/foundation/nsprogress/1410158-resuminghandler)Added [NSProgressReporting](https://developer.apple.com/documentation/foundation/progressreporting)Added [NSProgressReporting.progress](https://developer.apple.com/documentation/foundation/progressreporting/1412781-progress)

#### NSRegularExpression.h

Modified [-[NSRegularExpression matchesInString:options:range:]](https://developer.apple.com/documentation/foundation/nsregularexpression/1412446-matches)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)matchesInString:(NSString *)string options:(NSMatchingOptions)options range:(NSRange)range ``` |
| To | ``` - (NSArray<NSTextCheckingResult *> * _Nonnull)matchesInString:(NSString * _Nonnull)string options:(NSMatchingOptions)options range:(NSRange)range ``` |

#### NSRunLoop.h

Modified [-[NSObject performSelector:withObject:afterDelay:inModes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/performSelector:withObject:afterDelay:inModes:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performSelector:(SEL)aSelector withObject:(id)anArgument afterDelay:(NSTimeInterval)delay inModes:(NSArray *)modes ``` |
| To | ``` - (void)performSelector:(SEL _Nonnull)aSelector withObject:(id _Nullable)anArgument afterDelay:(NSTimeInterval)delay inModes:(NSArray<NSString *> * _Nonnull)modes ``` |

Modified [-[NSRunLoop performSelector:target:argument:order:modes:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/performSelector:target:argument:order:modes:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performSelector:(SEL)aSelector target:(id)target argument:(id)arg order:(NSUInteger)order modes:(NSArray *)modes ``` |
| To | ``` - (void)performSelector:(SEL _Nonnull)aSelector target:(id _Nonnull)target argument:(id _Nullable)arg order:(NSUInteger)order modes:(NSArray<NSString *> * _Nonnull)modes ``` |

#### NSSet.h

Modified [-[NSCountedSet addObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/addObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObject:(id)object ``` |
| To | ``` - (void)addObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSCountedSet countForObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/countForObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)countForObject:(id)object ``` |
| To | ``` - (NSUInteger)countForObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSCountedSet initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/initWithArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithArray:(NSArray *)array ``` |
| To | ``` - (instancetype _Nonnull)initWithArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [-[NSCountedSet initWithCapacity:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/initWithCapacity:)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSCountedSet initWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/initWithSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSet:(NSSet *)set ``` |
| To | ``` - (instancetype _Nonnull)initWithSet:(NSSet<ObjectType> * _Nonnull)set ``` |

Modified [-[NSCountedSet objectEnumerator]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/objectEnumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)objectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)objectEnumerator ``` |

Modified [-[NSCountedSet removeObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCountedSet/Description.html#//apple_ref/occ/instm/NSCountedSet/removeObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObject:(id)object ``` |
| To | ``` - (void)removeObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSMutableSet addObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/addObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObject:(id)object ``` |
| To | ``` - (void)addObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSMutableSet addObjectsFromArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/addObjectsFromArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addObjectsFromArray:(NSArray *)array ``` |
| To | ``` - (void)addObjectsFromArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [-[NSMutableSet intersectSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/intersectSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)intersectSet:(NSSet *)otherSet ``` |
| To | ``` - (void)intersectSet:(NSSet<ObjectType> * _Nonnull)otherSet ``` |

Modified [-[NSMutableSet minusSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/minusSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)minusSet:(NSSet *)otherSet ``` |
| To | ``` - (void)minusSet:(NSSet<ObjectType> * _Nonnull)otherSet ``` |

Modified [-[NSMutableSet removeObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/removeObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeObject:(id)object ``` |
| To | ``` - (void)removeObject:(ObjectType _Nonnull)object ``` |

Modified [-[NSMutableSet setSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/setSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSet:(NSSet *)otherSet ``` |
| To | ``` - (void)setSet:(NSSet<ObjectType> * _Nonnull)otherSet ``` |

Modified [-[NSMutableSet unionSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/unionSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unionSet:(NSSet *)otherSet ``` |
| To | ``` - (void)unionSet:(NSSet<ObjectType> * _Nonnull)otherSet ``` |

Modified [NSSet.allObjects](https://developer.apple.com/documentation/foundation/nsset/1417653-allobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *allObjects ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<ObjectType> *allObjects ``` |

Modified [-[NSSet anyObject]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/anyObject)

|  | Declaration |
| --- | --- |
| From | ``` - (id)anyObject ``` |
| To | ``` - (ObjectType _Nullable)anyObject ``` |

Modified [-[NSSet containsObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/containsObject:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsObject:(id)anObject ``` |
| To | ``` - (BOOL)containsObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSSet enumerateObjectsUsingBlock:]](https://developer.apple.com/documentation/foundation/nsset/1418129-enumerateobjectsusingblock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsUsingBlock:(void (^)(id obj, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsUsingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, BOOL * _Nonnull stop))block ``` |

Modified [-[NSSet enumerateObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/foundation/nsset/1412024-enumerateobjectswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^)(id obj, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, BOOL * _Nonnull stop))block ``` |

Modified [-[NSSet initWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithArray:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithArray:(NSArray *)array ``` |
| To | ``` - (instancetype _Nonnull)initWithArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [-[NSSet initWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(id)firstObj, ... ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(ObjectType _Nonnull)firstObj, ... ``` |

Modified [-[NSSet initWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjects:(const id [])objects count:(NSUInteger)cnt ``` |
| To | ``` - (instancetype _Nonnull)initWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |

Modified [-[NSSet initWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSet:(NSSet *)set ``` |
| To | ``` - (instancetype _Nonnull)initWithSet:(NSSet<ObjectType> * _Nonnull)set ``` |

Modified [-[NSSet initWithSet:copyItems:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/initWithSet:copyItems:)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSet:(NSSet *)set copyItems:(BOOL)flag ``` |
| To | ``` - (instancetype _Nonnull)initWithSet:(NSSet<ObjectType> * _Nonnull)set copyItems:(BOOL)flag ``` |

Modified [-[NSSet intersectsSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/intersectsSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)intersectsSet:(NSSet *)otherSet ``` |
| To | ``` - (BOOL)intersectsSet:(NSSet<ObjectType> * _Nonnull)otherSet ``` |

Modified [-[NSSet isEqualToSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/isEqualToSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToSet:(NSSet *)otherSet ``` |
| To | ``` - (BOOL)isEqualToSet:(NSSet<ObjectType> * _Nonnull)otherSet ``` |

Modified [-[NSSet isSubsetOfSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/isSubsetOfSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isSubsetOfSet:(NSSet *)otherSet ``` |
| To | ``` - (BOOL)isSubsetOfSet:(NSSet<ObjectType> * _Nonnull)otherSet ``` |

Modified [-[NSSet member:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/member:)

|  | Declaration |
| --- | --- |
| From | ``` - (id)member:(id)object ``` |
| To | ``` - (ObjectType _Nullable)member:(ObjectType _Nonnull)object ``` |

Modified [-[NSSet objectEnumerator]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/objectEnumerator)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEnumerator *)objectEnumerator ``` |
| To | ``` - (NSEnumerator<ObjectType> * _Nonnull)objectEnumerator ``` |

Modified [-[NSSet objectsPassingTest:]](https://developer.apple.com/documentation/foundation/nsset/1414392-objectspassingtest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)objectsPassingTest:(BOOL (^)(id obj, BOOL *stop))predicate ``` |
| To | ``` - (NSSet<ObjectType> * _Nonnull)objectsPassingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSSet objectsWithOptions:passingTest:]](https://developer.apple.com/documentation/foundation/nsset/1416826-objectswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)objectsWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^)(id obj, BOOL *stop))predicate ``` |
| To | ``` - (NSSet<ObjectType> * _Nonnull)objectsWithOptions:(NSEnumerationOptions)opts passingTest:(BOOL (^ _Nonnull)(ObjectType _Nonnull obj, BOOL * _Nonnull stop))predicate ``` |

Modified [-[NSSet setByAddingObject:]](https://developer.apple.com/documentation/foundation/nsset/1416316-setbyaddingobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)setByAddingObject:(id)anObject ``` |
| To | ``` - (NSSet<ObjectType> * _Nonnull)setByAddingObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[NSSet setByAddingObjectsFromArray:]](https://developer.apple.com/documentation/foundation/nsset/1418438-addingobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)setByAddingObjectsFromArray:(NSArray *)other ``` |
| To | ``` - (NSSet<ObjectType> * _Nonnull)setByAddingObjectsFromArray:(NSArray<ObjectType> * _Nonnull)other ``` |

Modified [-[NSSet setByAddingObjectsFromSet:]](https://developer.apple.com/documentation/foundation/nsset/1408217-setbyaddingobjectsfromset)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)setByAddingObjectsFromSet:(NSSet *)other ``` |
| To | ``` - (NSSet<ObjectType> * _Nonnull)setByAddingObjectsFromSet:(NSSet<ObjectType> * _Nonnull)other ``` |

Modified [+[NSSet setWithArray:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithArray:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)setWithArray:(NSArray *)array ``` |
| To | ``` + (instancetype _Nonnull)setWithArray:(NSArray<ObjectType> * _Nonnull)array ``` |

Modified [+[NSSet setWithObject:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObject:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)setWithObject:(id)object ``` |
| To | ``` + (instancetype _Nonnull)setWithObject:(ObjectType _Nonnull)object ``` |

Modified [+[NSSet setWithObjects:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)setWithObjects:(id)firstObj, ... ``` |
| To | ``` + (instancetype _Nonnull)setWithObjects:(ObjectType _Nonnull)firstObj, ... ``` |

Modified [+[NSSet setWithObjects:count:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithObjects:count:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)setWithObjects:(const id [])objects count:(NSUInteger)cnt ``` |
| To | ``` + (instancetype _Nonnull)setWithObjects:(const ObjectType  _Nonnull [])objects count:(NSUInteger)cnt ``` |

Modified [+[NSSet setWithSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/clm/NSSet/setWithSet:)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)setWithSet:(NSSet *)set ``` |
| To | ``` + (instancetype _Nonnull)setWithSet:(NSSet<ObjectType> * _Nonnull)set ``` |

#### NSSortDescriptor.h

Added [-[NSSortDescriptor initWithCoder:]](https://developer.apple.com/documentation/foundation/nssortdescriptor/1412503-initwithcoder)Modified [-[NSArray sortedArrayUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsarray/1415069-sortedarrayusingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingDescriptors:(NSArray *)sortDescriptors ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingDescriptors:(NSArray<NSSortDescriptor *> * _Nonnull)sortDescriptors ``` |

Modified [-[NSMutableArray sortUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsmutablearray/1410745-sortusingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sortUsingDescriptors:(NSArray *)sortDescriptors ``` |
| To | ``` - (void)sortUsingDescriptors:(NSArray<NSSortDescriptor *> * _Nonnull)sortDescriptors ``` |

Modified [-[NSMutableOrderedSet sortUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410023-sort)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sortUsingDescriptors:(NSArray *)sortDescriptors ``` |
| To | ``` - (void)sortUsingDescriptors:(NSArray<NSSortDescriptor *> * _Nonnull)sortDescriptors ``` |

Modified [-[NSOrderedSet sortedArrayUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsorderedset/1409953-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingDescriptors:(NSArray *)sortDescriptors ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingDescriptors:(NSArray<NSSortDescriptor *> * _Nonnull)sortDescriptors ``` |

Modified [-[NSSet sortedArrayUsingDescriptors:]](https://developer.apple.com/documentation/foundation/nsset/1416427-sortedarray)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sortedArrayUsingDescriptors:(NSArray *)sortDescriptors ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)sortedArrayUsingDescriptors:(NSArray<NSSortDescriptor *> * _Nonnull)sortDescriptors ``` |

#### NSString.h

Added [-[NSMutableString applyTransform:reverse:range:updatedRange:]](https://developer.apple.com/documentation/foundation/nsmutablestring/1415742-applytransform)Added [NSString.localizedCapitalizedString](https://developer.apple.com/documentation/foundation/nsstring/1414885-localizedcapitalized)Added [NSString.localizedLowercaseString](https://developer.apple.com/documentation/foundation/nsstring/1414125-localizedlowercasestring)Added [-[NSString localizedStandardContainsString:]](https://developer.apple.com/documentation/foundation/nsstring/1416328-localizedstandardcontainsstring)Added [-[NSString localizedStandardRangeOfString:]](https://developer.apple.com/documentation/foundation/nsstring/1413574-localizedstandardrange)Added [NSString.localizedUppercaseString](https://developer.apple.com/documentation/foundation/nsstring/1413331-localizeduppercasestring)Added [-[NSString stringByApplyingTransform:reverse:]](https://developer.apple.com/documentation/foundation/nsstring/1407787-applyingtransform)Added [NSStringTransformFullwidthToHalfwidth](https://developer.apple.com/documentation/foundation/stringtransform/1412408-fullwidthtohalfwidth)Added [NSStringTransformHiraganaToKatakana](https://developer.apple.com/documentation/foundation/nsstringtransformhiraganatokatakana)Added [NSStringTransformLatinToArabic](https://developer.apple.com/documentation/foundation/stringtransform/1409724-latintoarabic)Added [NSStringTransformLatinToCyrillic](https://developer.apple.com/documentation/foundation/stringtransform/1417172-latintocyrillic)Added [NSStringTransformLatinToGreek](https://developer.apple.com/documentation/foundation/nsstringtransformlatintogreek)Added [NSStringTransformLatinToHangul](https://developer.apple.com/documentation/foundation/nsstringtransformlatintohangul)Added [NSStringTransformLatinToHebrew](https://developer.apple.com/documentation/foundation/stringtransform/1413608-latintohebrew)Added [NSStringTransformLatinToHiragana](https://developer.apple.com/documentation/foundation/stringtransform/1412376-latintohiragana)Added [NSStringTransformLatinToKatakana](https://developer.apple.com/documentation/foundation/nsstringtransformlatintokatakana)Added [NSStringTransformLatinToThai](https://developer.apple.com/documentation/foundation/nsstringtransformlatintothai)Added [NSStringTransformMandarinToLatin](https://developer.apple.com/documentation/foundation/nsstringtransformmandarintolatin)Added [NSStringTransformStripCombiningMarks](https://developer.apple.com/documentation/foundation/nsstringtransformstripcombiningmarks)Added [NSStringTransformStripDiacritics](https://developer.apple.com/documentation/foundation/stringtransform/1416044-stripdiacritics)Added [NSStringTransformToLatin](https://developer.apple.com/documentation/foundation/stringtransform/1409674-tolatin)Added [NSStringTransformToUnicodeName](https://developer.apple.com/documentation/foundation/stringtransform/1408644-tounicodename)Added [NSStringTransformToXMLHex](https://developer.apple.com/documentation/foundation/stringtransform/1407218-toxmlhex)Modified [-[NSString commonPrefixWithString:options:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/commonPrefixWithString:options:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)commonPrefixWithString:(NSString *)aString options:(NSStringCompareOptions)mask ``` |
| To | ``` - (NSString * _Nonnull)commonPrefixWithString:(NSString * _Nonnull)str options:(NSStringCompareOptions)mask ``` |

Modified [-[NSString componentsSeparatedByCharactersInSet:]](https://developer.apple.com/documentation/foundation/nsstring/1410120-componentsseparatedbycharactersi)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)componentsSeparatedByCharactersInSet:(NSCharacterSet *)separator ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)componentsSeparatedByCharactersInSet:(NSCharacterSet * _Nonnull)separator ``` |

Modified [-[NSString componentsSeparatedByString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/componentsSeparatedByString:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)componentsSeparatedByString:(NSString *)separator ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)componentsSeparatedByString:(NSString * _Nonnull)separator ``` |

Modified [-[NSString containsString:]](https://developer.apple.com/documentation/foundation/nsstring/1414563-contains)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsString:(NSString *)aString ``` |
| To | ``` - (BOOL)containsString:(NSString * _Nonnull)str ``` |

Modified [-[NSString getCharacters:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/getCharacters:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getCharacters:(unichar *)buffer range:(NSRange)aRange ``` |
| To | ``` - (void)getCharacters:(unichar * _Nonnull)buffer range:(NSRange)range ``` |

Modified [-[NSString hasPrefix:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/hasPrefix:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)hasPrefix:(NSString *)aString ``` |
| To | ``` - (BOOL)hasPrefix:(NSString * _Nonnull)str ``` |

Modified [-[NSString hasSuffix:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/hasSuffix:)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)hasSuffix:(NSString *)aString ``` |
| To | ``` - (BOOL)hasSuffix:(NSString * _Nonnull)str ``` |

Modified [-[NSString localizedCaseInsensitiveContainsString:]](https://developer.apple.com/documentation/foundation/nsstring/1412098-localizedcaseinsensitivecontains)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)localizedCaseInsensitiveContainsString:(NSString *)aString ``` |
| To | ``` - (BOOL)localizedCaseInsensitiveContainsString:(NSString * _Nonnull)str ``` |

Modified [-[NSString rangeOfCharacterFromSet:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet *)aSet ``` |
| To | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet * _Nonnull)searchSet ``` |

Modified [-[NSString rangeOfCharacterFromSet:options:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:options:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet *)aSet options:(NSStringCompareOptions)mask ``` |
| To | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet * _Nonnull)searchSet options:(NSStringCompareOptions)mask ``` |

Modified [-[NSString rangeOfCharacterFromSet:options:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:options:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet *)aSet options:(NSStringCompareOptions)mask range:(NSRange)searchRange ``` |
| To | ``` - (NSRange)rangeOfCharacterFromSet:(NSCharacterSet * _Nonnull)searchSet options:(NSStringCompareOptions)mask range:(NSRange)searchRange ``` |

Modified [-[NSString rangeOfString:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfString:(NSString *)aString ``` |
| To | ``` - (NSRange)rangeOfString:(NSString * _Nonnull)searchString ``` |

Modified [-[NSString rangeOfString:options:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfString:(NSString *)aString options:(NSStringCompareOptions)mask ``` |
| To | ``` - (NSRange)rangeOfString:(NSString * _Nonnull)searchString options:(NSStringCompareOptions)mask ``` |

Modified [-[NSString rangeOfString:options:range:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:range:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfString:(NSString *)aString options:(NSStringCompareOptions)mask range:(NSRange)searchRange ``` |
| To | ``` - (NSRange)rangeOfString:(NSString * _Nonnull)searchString options:(NSStringCompareOptions)mask range:(NSRange)searchRange ``` |

Modified [-[NSString rangeOfString:options:range:locale:]](https://developer.apple.com/documentation/foundation/nsstring/1417348-range)

|  | Declaration |
| --- | --- |
| From | ``` - (NSRange)rangeOfString:(NSString *)aString options:(NSStringCompareOptions)mask range:(NSRange)searchRange locale:(NSLocale *)locale ``` |
| To | ``` - (NSRange)rangeOfString:(NSString * _Nonnull)searchString options:(NSStringCompareOptions)mask range:(NSRange)searchRange locale:(NSLocale * _Nullable)locale ``` |

Modified [+[NSString stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:]](https://developer.apple.com/documentation/foundation/nsstring/1413576-stringencoding)

|  | Declaration |
| --- | --- |
| From | ``` + (NSStringEncoding)stringEncodingForData:(NSData *)data encodingOptions:(NSDictionary *)opts convertedString:(NSString **)string usedLossyConversion:(BOOL *)usedLossyConversion ``` |
| To | ``` + (NSStringEncoding)stringEncodingForData:(NSData * _Nonnull)data encodingOptions:(NSDictionary<NSString *,id> * _Nullable)opts convertedString:(NSString * _Nullable * _Nullable)string usedLossyConversion:(BOOL * _Nullable)usedLossyConversion ``` |

#### NSTextCheckingResult.h

Modified [+[NSTextCheckingResult addressCheckingResultWithRange:components:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413828-addresscheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` + (NSTextCheckingResult *)addressCheckingResultWithRange:(NSRange)range components:(NSDictionary *)components ``` |
| To | ``` + (NSTextCheckingResult * _Nonnull)addressCheckingResultWithRange:(NSRange)range components:(NSDictionary<NSString *,NSString *> * _Nonnull)components ``` |

Modified [NSTextCheckingResult.addressComponents](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1413728-addresscomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *addressComponents ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,NSString *> *addressComponents ``` |

Modified [NSTextCheckingResult.alternativeStrings](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1415454-alternativestrings)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *alternativeStrings ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSString *> *alternativeStrings ``` |

Modified [NSTextCheckingResult.components](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407367-components)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *components ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,NSString *> *components ``` |

Modified [+[NSTextCheckingResult correctionCheckingResultWithRange:replacementString:alternativeStrings:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1416640-correctioncheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` + (NSTextCheckingResult *)correctionCheckingResultWithRange:(NSRange)range replacementString:(NSString *)replacementString alternativeStrings:(NSArray *)alternativeStrings ``` |
| To | ``` + (NSTextCheckingResult * _Nonnull)correctionCheckingResultWithRange:(NSRange)range replacementString:(NSString * _Nonnull)replacementString alternativeStrings:(NSArray<NSString *> * _Nonnull)alternativeStrings ``` |

Modified [+[NSTextCheckingResult grammarCheckingResultWithRange:details:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1407190-grammarcheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` + (NSTextCheckingResult *)grammarCheckingResultWithRange:(NSRange)range details:(NSArray *)details ``` |
| To | ``` + (NSTextCheckingResult * _Nonnull)grammarCheckingResultWithRange:(NSRange)range details:(NSArray<NSString *> * _Nonnull)details ``` |

Modified [NSTextCheckingResult.grammarDetails](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1408959-grammardetails)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *grammarDetails ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSString *> *grammarDetails ``` |

Modified [+[NSTextCheckingResult transitInformationCheckingResultWithRange:components:]](https://developer.apple.com/documentation/foundation/nstextcheckingresult/1408575-transitinformationcheckingresult)

|  | Declaration |
| --- | --- |
| From | ``` + (NSTextCheckingResult *)transitInformationCheckingResultWithRange:(NSRange)range components:(NSDictionary *)components ``` |
| To | ``` + (NSTextCheckingResult * _Nonnull)transitInformationCheckingResultWithRange:(NSRange)range components:(NSDictionary<NSString *,NSString *> * _Nonnull)components ``` |

#### NSThread.h

Modified [-[NSObject performSelector:onThread:withObject:waitUntilDone:modes:]](https://developer.apple.com/documentation/objectivec/nsobject/1417922-perform)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performSelector:(SEL)aSelector onThread:(NSThread *)thr withObject:(id)arg waitUntilDone:(BOOL)wait modes:(NSArray *)array ``` |
| To | ``` - (void)performSelector:(SEL _Nonnull)aSelector onThread:(NSThread * _Nonnull)thr withObject:(id _Nullable)arg waitUntilDone:(BOOL)wait modes:(NSArray<NSString *> * _Nullable)array ``` |

Modified [-[NSObject performSelectorOnMainThread:withObject:waitUntilDone:modes:]](https://developer.apple.com/documentation/objectivec/nsobject/1411637-performselectoronmainthread)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performSelectorOnMainThread:(SEL)aSelector withObject:(id)arg waitUntilDone:(BOOL)wait modes:(NSArray *)array ``` |
| To | ``` - (void)performSelectorOnMainThread:(SEL _Nonnull)aSelector withObject:(id _Nullable)arg waitUntilDone:(BOOL)wait modes:(NSArray<NSString *> * _Nullable)array ``` |

Modified [+[NSThread callStackReturnAddresses]](https://developer.apple.com/documentation/foundation/nsthread/1409565-callstackreturnaddresses)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)callStackReturnAddresses ``` |
| To | ``` + (NSArray<NSNumber *> * _Nonnull)callStackReturnAddresses ``` |

Modified [+[NSThread callStackSymbols]](https://developer.apple.com/documentation/foundation/thread/1414836-callstacksymbols)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)callStackSymbols ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)callStackSymbols ``` |

#### NSTimeZone.h

Modified [+[NSTimeZone abbreviationDictionary]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/clm/NSTimeZone/abbreviationDictionary)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)abbreviationDictionary ``` |
| To | ``` + (NSDictionary<NSString *,NSString *> * _Nonnull)abbreviationDictionary ``` |

Modified [+[NSTimeZone knownTimeZoneNames]](https://developer.apple.com/documentation/foundation/nstimezone/1387223-knowntimezonenames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)knownTimeZoneNames ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)knownTimeZoneNames ``` |

Modified +[NSTimeZone setAbbreviationDictionary:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setAbbreviationDictionary:(NSDictionary *)dict ``` |
| To | ``` + (void)setAbbreviationDictionary:(NSDictionary<NSString *,NSString *> * _Nonnull)dict ``` |

#### NSUbiquitousKeyValueStore.h

Modified [-[NSUbiquitousKeyValueStore dictionaryForKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1416241-dictionary)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)dictionaryForKey:(NSString *)aKey ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)dictionaryForKey:(NSString * _Nonnull)aKey ``` |

Modified [NSUbiquitousKeyValueStore.dictionaryRepresentation](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1411129-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *dictionaryRepresentation ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,id> *dictionaryRepresentation ``` |

Modified [-[NSUbiquitousKeyValueStore setDictionary:forKey:]](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417155-setdictionary)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDictionary:(NSDictionary *)aDictionary forKey:(NSString *)aKey ``` |
| To | ``` - (void)setDictionary:(NSDictionary<NSString *,id> * _Nullable)aDictionary forKey:(NSString * _Nonnull)aKey ``` |

#### NSUndoManager.h

Removed NSUndoCloseGroupingRunLoopOrderingAdded [-[NSUndoManager registerUndoWithTarget:handler:]](https://developer.apple.com/documentation/foundation/nsundomanager/1437863-registerundowithtarget)Added [NSUndoCloseGroupingRunLoopOrdering](https://developer.apple.com/documentation/foundation/nsundoclosegroupingrunloopordering)Modified [NSUndoManager.runLoopModes](https://developer.apple.com/documentation/foundation/nsundomanager/1409504-runloopmodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *runLoopModes ``` |
| To | ``` @property(copy, nonnull) NSArray<NSString *> *runLoopModes ``` |

#### NSURL.h

Added [+[NSURL absoluteURLWithDataRepresentation:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1412404-absoluteurlwithdatarepresentatio)Added [NSURL.dataRepresentation](https://developer.apple.com/documentation/foundation/nsurl/1407656-datarepresentation)Added [+[NSURL fileURLWithPath:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1413020-fileurlwithpath)Added [+[NSURL fileURLWithPath:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1413201-fileurlwithpath)Added [NSURL.hasDirectoryPath](https://developer.apple.com/documentation/foundation/nsurl/1411475-hasdirectorypath)Added [-[NSURL initAbsoluteURLWithDataRepresentation:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1410750-init)Added [-[NSURL initFileURLWithPath:isDirectory:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1417932-init)Added [-[NSURL initFileURLWithPath:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1415077-initfileurlwithpath)Added [-[NSURL initWithDataRepresentation:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1416851-init)Added [+[NSURL URLWithDataRepresentation:relativeToURL:]](https://developer.apple.com/documentation/foundation/nsurl/1572042-urlwithdatarepresentation)Added [NSURLComponents.rangeOfFragment](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415180-rangeoffragment)Added [NSURLComponents.rangeOfHost](https://developer.apple.com/documentation/foundation/nsurlcomponents/1408894-rangeofhost)Added [NSURLComponents.rangeOfPassword](https://developer.apple.com/documentation/foundation/nsurlcomponents/1415024-rangeofpassword)Added [NSURLComponents.rangeOfPath](https://developer.apple.com/documentation/foundation/nsurlcomponents/1418459-rangeofpath)Added [NSURLComponents.rangeOfPort](https://developer.apple.com/documentation/foundation/nsurlcomponents/1411790-rangeofport)Added [NSURLComponents.rangeOfQuery](https://developer.apple.com/documentation/foundation/nsurlcomponents/1409456-rangeofquery)Added [NSURLComponents.rangeOfScheme](https://developer.apple.com/documentation/foundation/nsurlcomponents/1410099-rangeofscheme)Added [NSURLComponents.rangeOfUser](https://developer.apple.com/documentation/foundation/nsurlcomponents/1414961-rangeofuser)Added [NSURLFileProtectionComplete](https://developer.apple.com/documentation/foundation/urlfileprotection/1617177-complete)Added [NSURLFileProtectionCompleteUnlessOpen](https://developer.apple.com/documentation/foundation/nsurlfileprotectioncompleteunlessopen)Added [NSURLFileProtectionCompleteUntilFirstUserAuthentication](https://developer.apple.com/documentation/foundation/urlfileprotection/1617288-completeuntilfirstuserauthentica)Added [NSURLFileProtectionKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1616246-fileprotectionkey)Added [NSURLFileProtectionNone](https://developer.apple.com/documentation/foundation/urlfileprotection/1616634-none)Added [NSURLIsApplicationKey](https://developer.apple.com/documentation/foundation/nsurlisapplicationkey)Modified [-[NSString stringByAddingPercentEscapesUsingEncoding:]](https://developer.apple.com/documentation/foundation/nsstring/1415058-addingpercentescapes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[NSString stringByReplacingPercentEscapesUsingEncoding:]](https://developer.apple.com/documentation/foundation/nsstring/1407783-stringbyreplacingpercentescapesu)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[NSURL bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:]](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)bookmarkDataWithOptions:(NSURLBookmarkCreationOptions)options includingResourceValuesForKeys:(NSArray *)keys relativeToURL:(NSURL *)relativeURL error:(NSError **)error ``` |
| To | ``` - (NSData * _Nullable)bookmarkDataWithOptions:(NSURLBookmarkCreationOptions)options includingResourceValuesForKeys:(NSArray<NSString *> * _Nullable)keys relativeToURL:(NSURL * _Nullable)relativeURL error:(NSError * _Nullable * _Nullable)error ``` |

Modified [+[NSURL fileURLWithPathComponents:]](https://developer.apple.com/documentation/foundation/nsurl/1414206-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` + (NSURL *)fileURLWithPathComponents:(NSArray *)components ``` |
| To | ``` + (NSURL * _Nullable)fileURLWithPathComponents:(NSArray<NSString *> * _Nonnull)components ``` |

Modified [-[NSURL initWithScheme:host:path:]](https://developer.apple.com/documentation/foundation/nsurl/1414181-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [NSURL.pathComponents](https://developer.apple.com/documentation/foundation/nsurl/1407365-pathcomponents)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *pathComponents ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSString *> *pathComponents ``` |

Modified [-[NSURL promisedItemResourceValuesForKeys:error:]](https://developer.apple.com/documentation/foundation/nsurl/1407746-promiseditemresourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)promisedItemResourceValuesForKeys:(NSArray *)keys error:(NSError **)error ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)promisedItemResourceValuesForKeys:(NSArray<NSString *> * _Nonnull)keys error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSURL resourceValuesForKeys:error:]](https://developer.apple.com/documentation/foundation/nsurl/1417657-resourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)resourceValuesForKeys:(NSArray *)keys error:(NSError **)error ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)resourceValuesForKeys:(NSArray<NSString *> * _Nonnull)keys error:(NSError * _Nullable * _Nullable)error ``` |

Modified [+[NSURL resourceValuesForKeys:fromBookmarkData:]](https://developer.apple.com/documentation/foundation/nsurl/1418097-resourcevaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)resourceValuesForKeys:(NSArray *)keys fromBookmarkData:(NSData *)bookmarkData ``` |
| To | ``` + (NSDictionary<NSString *,id> * _Nullable)resourceValuesForKeys:(NSArray<NSString *> * _Nonnull)keys fromBookmarkData:(NSData * _Nonnull)bookmarkData ``` |

Modified [-[NSURL setResourceValues:error:]](https://developer.apple.com/documentation/foundation/nsurl/1408208-setresourcevalues)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setResourceValues:(NSDictionary *)keyedValues error:(NSError **)error ``` |
| To | ``` - (BOOL)setResourceValues:(NSDictionary<NSString *,id> * _Nonnull)keyedValues error:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSURLComponents.queryItems](https://developer.apple.com/documentation/foundation/nsurlcomponents/1407752-queryitems)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *queryItems ``` |
| To | ``` @property(copy, nullable) NSArray<NSURLQueryItem *> *queryItems ``` |

#### NSURLConnection.h

Modified [+[NSURLConnection connectionWithRequest:delegate:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1569746-connectionwithrequest)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[NSURLConnection initWithRequest:delegate:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1414520-initwithrequest)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[NSURLConnection initWithRequest:delegate:startImmediately:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1418425-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [+[NSURLConnection sendAsynchronousRequest:queue:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1418125-sendasynchronousrequest)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [+[NSURLConnection sendSynchronousRequest:returningResponse:error:]](https://developer.apple.com/documentation/foundation/nsurlconnection/1411393-sendsynchronousrequest)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### NSURLCredentialStorage.h

Modified [NSURLCredentialStorage.allCredentials](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1413859-allcredentials)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *allCredentials ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSURLProtectionSpace *,NSDictionary<NSString *,NSURLCredential *> *> *allCredentials ``` |

Modified [-[NSURLCredentialStorage credentialsForProtectionSpace:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1413910-credentials)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)credentialsForProtectionSpace:(NSURLProtectionSpace *)space ``` |
| To | ``` - (NSDictionary<NSString *,NSURLCredential *> * _Nullable)credentialsForProtectionSpace:(NSURLProtectionSpace * _Nonnull)space ``` |

Modified [-[NSURLCredentialStorage getCredentialsForProtectionSpace:task:completionHandler:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1418119-getcredentials)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getCredentialsForProtectionSpace:(NSURLProtectionSpace *)protectionSpace task:(NSURLSessionTask *)task completionHandler:(void (^)(NSDictionary *credentials))completionHandler ``` |
| To | ``` - (void)getCredentialsForProtectionSpace:(NSURLProtectionSpace * _Nonnull)protectionSpace task:(NSURLSessionTask * _Nonnull)task completionHandler:(void (^ _Nonnull)(NSDictionary<NSString *,NSURLCredential *> * _Nullable credentials))completionHandler ``` |

Modified [-[NSURLCredentialStorage removeCredential:forProtectionSpace:options:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1407695-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeCredential:(NSURLCredential *)credential forProtectionSpace:(NSURLProtectionSpace *)space options:(NSDictionary *)options ``` |
| To | ``` - (void)removeCredential:(NSURLCredential * _Nonnull)credential forProtectionSpace:(NSURLProtectionSpace * _Nonnull)space options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[NSURLCredentialStorage removeCredential:forProtectionSpace:options:task:]](https://developer.apple.com/documentation/foundation/urlcredentialstorage/1407237-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeCredential:(NSURLCredential *)credential forProtectionSpace:(NSURLProtectionSpace *)protectionSpace options:(NSDictionary *)options task:(NSURLSessionTask *)task ``` |
| To | ``` - (void)removeCredential:(NSURLCredential * _Nonnull)credential forProtectionSpace:(NSURLProtectionSpace * _Nonnull)protectionSpace options:(NSDictionary<NSString *,id> * _Nullable)options task:(NSURLSessionTask * _Nonnull)task ``` |

#### NSURLError.h

Added [NSURLErrorAppTransportSecurityRequiresSecureConnection](https://developer.apple.com/documentation/foundation/1508628-url_loading_system_error_codes/nsurlerrorapptransportsecurityrequiressecureconnection)

#### NSURLProtectionSpace.h

Modified [NSURLProtectionSpace.distinguishedNames](https://developer.apple.com/documentation/foundation/urlprotectionspace/1417061-distinguishednames)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *distinguishedNames ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSData *> *distinguishedNames ``` |

#### NSURLProtocol.h

Modified [-[NSURLProtocol initWithRequest:cachedResponse:client:]](https://developer.apple.com/documentation/foundation/urlprotocol/1414366-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSURLRequest.h

Modified [NSMutableURLRequest.allHTTPHeaderFields](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1414617-allhttpheaderfields)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *allHTTPHeaderFields ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,NSString *> *allHTTPHeaderFields ``` |

Modified [NSURLRequest.allHTTPHeaderFields](https://developer.apple.com/documentation/foundation/nsurlrequest/1418477-allhttpheaderfields)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *allHTTPHeaderFields ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,NSString *> *allHTTPHeaderFields ``` |

Modified [-[NSURLRequest initWithURL:cachePolicy:timeoutInterval:]](https://developer.apple.com/documentation/foundation/nsurlrequest/1416292-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSURLResponse.h

Modified [-[NSHTTPURLResponse initWithURL:statusCode:HTTPVersion:headerFields:]](https://developer.apple.com/documentation/foundation/nshttpurlresponse/1415870-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)url statusCode:(NSInteger)statusCode HTTPVersion:(NSString *)HTTPVersion headerFields:(NSDictionary *)headerFields ``` |
| To | ``` - (instancetype _Nullable)initWithURL:(NSURL * _Nonnull)url statusCode:(NSInteger)statusCode HTTPVersion:(NSString * _Nullable)HTTPVersion headerFields:(NSDictionary<NSString *,NSString *> * _Nullable)headerFields ``` |

Modified [-[NSURLResponse initWithURL:MIMEType:expectedContentLength:textEncodingName:]](https://developer.apple.com/documentation/foundation/nsurlresponse/1413566-initwithurl)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSURLSession.h

Removed -[NSURLSession dataTaskWithHTTPGetRequest:]Removed -[NSURLSession dataTaskWithHTTPGetRequest:completionHandler:]Removed NSURLSession(NSURLSessionDeprecated)Added [-[NSURLSession getAllTasksWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411618-getalltaskswithcompletionhandler)Added [-[NSURLSession streamTaskWithHostName:port:]](https://developer.apple.com/documentation/foundation/urlsession/1411587-streamtask)Added [-[NSURLSession streamTaskWithNetService:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411545-streamtaskwithnetservice)Added [NSURLSessionConfiguration.shouldUseExtendedBackgroundIdleMode](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1409517-shoulduseextendedbackgroundidlem)Added [-[NSURLSessionDataDelegate URLSession:dataTask:didBecomeStreamTask:]](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1411648-urlsession)Added [NSURLSessionStreamDelegate](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate)Added [-[NSURLSessionStreamDelegate URLSession:betterRouteDiscoveredForStreamTask:]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamdelegate/1407527-urlsession)Added [-[NSURLSessionStreamDelegate URLSession:readClosedForStreamTask:]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamdelegate/1411501-urlsession)Added [-[NSURLSessionStreamDelegate URLSession:streamTask:didBecomeInputStream:outputStream:]](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/1411625-urlsession)Added [-[NSURLSessionStreamDelegate URLSession:writeClosedForStreamTask:]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamdelegate/1411507-urlsession)Added [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/urlsessionstreamtask)Added [-[NSURLSessionStreamTask captureStreams]](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1410132-capturestreams)Added [-[NSURLSessionStreamTask closeRead]](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411558-closeread)Added [-[NSURLSessionStreamTask closeWrite]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1411347-closewrite)Added [-[NSURLSessionStreamTask readDataOfMinLength:maxLength:timeout:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1411604-readdataofminlength)Added [-[NSURLSessionStreamTask startSecureConnection]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1411567-startsecureconnection)Added [-[NSURLSessionStreamTask stopSecureConnection]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1407337-stopsecureconnection)Added [-[NSURLSessionStreamTask writeData:timeout:completionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask/1411602-writedata)Added [NSURLSessionResponseBecomeStream](https://developer.apple.com/documentation/foundation/nsurlsessionresponsedisposition/nsurlsessionresponsebecomestream)Modified [-[NSURLSession getTasksWithCompletionHandler:]](https://developer.apple.com/documentation/foundation/nsurlsession/1411578-gettaskswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getTasksWithCompletionHandler:(void (^)(NSArray *dataTasks, NSArray *uploadTasks, NSArray *downloadTasks))completionHandler ``` |
| To | ``` - (void)getTasksWithCompletionHandler:(void (^ _Nonnull)(NSArray<NSURLSessionDataTask *> * _Nonnull dataTasks, NSArray<NSURLSessionUploadTask *> * _Nonnull uploadTasks, NSArray<NSURLSessionDownloadTask *> * _Nonnull downloadTasks))completionHandler ``` |

Modified [NSURLSessionConfiguration.protocolClasses](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411050-protocolclasses)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *protocolClasses ``` |
| To | ``` @property(copy, nullable) NSArray<Class> *protocolClasses ``` |

#### NSUserActivity.h

Added [NSUserActivity.eligibleForHandoff](https://developer.apple.com/documentation/foundation/nsuseractivity/1410971-eligibleforhandoff)Added [NSUserActivity.eligibleForPublicIndexing](https://developer.apple.com/documentation/foundation/nsuseractivity/1414701-iseligibleforpublicindexing)Added [NSUserActivity.eligibleForSearch](https://developer.apple.com/documentation/foundation/nsuseractivity/1417761-iseligibleforsearch)Added [NSUserActivity.expirationDate](https://developer.apple.com/documentation/foundation/nsuseractivity/1413745-expirationdate)Added [NSUserActivity.keywords](https://developer.apple.com/documentation/foundation/nsuseractivity/1408023-keywords)Added [NSUserActivity.requiredUserInfoKeys](https://developer.apple.com/documentation/foundation/nsuseractivity/1417256-requireduserinfokeys)Added [-[NSUserActivity resignCurrent]](https://developer.apple.com/documentation/foundation/nsuseractivity/1409596-resigncurrent)

#### NSUserDefaults.h

Modified [-[NSUserDefaults dictionaryForKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/dictionaryForKey:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)dictionaryForKey:(NSString *)defaultName ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)dictionaryForKey:(NSString * _Nonnull)defaultName ``` |

Modified [-[NSUserDefaults dictionaryRepresentation]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/dictionaryRepresentation)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)dictionaryRepresentation ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)dictionaryRepresentation ``` |

Modified [-[NSUserDefaults persistentDomainForName:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/persistentDomainForName:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)persistentDomainForName:(NSString *)domainName ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nullable)persistentDomainForName:(NSString * _Nonnull)domainName ``` |

Modified [-[NSUserDefaults registerDefaults:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/registerDefaults:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)registerDefaults:(NSDictionary *)registrationDictionary ``` |
| To | ``` - (void)registerDefaults:(NSDictionary<NSString *,id> * _Nonnull)registrationDictionary ``` |

Modified [-[NSUserDefaults setPersistentDomain:forName:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/setPersistentDomain:forName:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setPersistentDomain:(NSDictionary *)domain forName:(NSString *)domainName ``` |
| To | ``` - (void)setPersistentDomain:(NSDictionary<NSString *,id> * _Nonnull)domain forName:(NSString * _Nonnull)domainName ``` |

Modified [-[NSUserDefaults setVolatileDomain:forName:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/setVolatileDomain:forName:)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setVolatileDomain:(NSDictionary *)domain forName:(NSString *)domainName ``` |
| To | ``` - (void)setVolatileDomain:(NSDictionary<NSString *,id> * _Nonnull)domain forName:(NSString * _Nonnull)domainName ``` |

Modified [-[NSUserDefaults stringArrayForKey:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/stringArrayForKey:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)stringArrayForKey:(NSString *)defaultName ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)stringArrayForKey:(NSString * _Nonnull)defaultName ``` |

Modified [-[NSUserDefaults volatileDomainForName:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/volatileDomainForName:)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)volatileDomainForName:(NSString *)domainName ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)volatileDomainForName:(NSString * _Nonnull)domainName ``` |

Modified [NSUserDefaults.volatileDomainNames](https://developer.apple.com/documentation/foundation/nsuserdefaults/1414231-volatiledomainnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *volatileDomainNames ``` |
| To | ``` @property(readonly, copy, nonnull) NSArray<NSString *> *volatileDomainNames ``` |

#### NSValue.h

Modified [NSValue.nonretainedObjectValue](https://developer.apple.com/documentation/foundation/nsvalue/1412287-nonretainedobjectvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id nonretainedObjectValue ``` |
| To | ``` @property(readonly, nullable) id nonretainedObjectValue ``` |

Modified [NSValue.pointerValue](https://developer.apple.com/documentation/foundation/nsvalue/1410668-pointervalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void *)pointerValue ``` |
| To | ``` @property(readonly, nullable) void *pointerValue ``` |

#### NSValueTransformer.h

Modified [+[NSValueTransformer valueTransformerNames]](https://developer.apple.com/documentation/foundation/valuetransformer/1402012-valuetransformernames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)valueTransformerNames ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)valueTransformerNames ``` |

#### NSXMLParser.h

Modified [NSXMLParser.allowedExternalEntityURLs](https://developer.apple.com/documentation/foundation/nsxmlparser/1412380-allowedexternalentityurls)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSSet *allowedExternalEntityURLs ``` |
| To | ``` @property(copy, nullable) NSSet<NSURL *> *allowedExternalEntityURLs ``` |

Modified [-[NSXMLParser initWithData:]](https://developer.apple.com/documentation/foundation/nsxmlparser/1418103-initwithdata)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSXMLParserDelegate parser:didStartElement:namespaceURI:qualifiedName:attributes:]](https://developer.apple.com/documentation/foundation/xmlparserdelegate/1415894-parser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)parser:(NSXMLParser *)parser didStartElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName attributes:(NSDictionary *)attributeDict ``` |
| To | ``` - (void)parser:(NSXMLParser * _Nonnull)parser didStartElement:(NSString * _Nonnull)elementName namespaceURI:(NSString * _Nullable)namespaceURI qualifiedName:(NSString * _Nullable)qName attributes:(NSDictionary<NSString *,NSString *> * _Nonnull)attributeDict ``` |

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
