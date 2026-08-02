---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/ObjectiveC.html
archived_at: '2026-07-18T02:56:27.091557Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# ObjectiveC Changes

## ObjectiveC

Removed NSUIntegerMaxAdded objc_method_description.init()Added objc_method_description.init(name: Selector, types: UnsafeMutablePointer<Int8>)Added objc_object.init()Added objc_object.init(isa: AnyClass!)Added objc_property_attribute_t.init()Added objc_property_attribute_t.init(name: UnsafePointer<Int8>, value: UnsafePointer<Int8>)Added objc_super.init()Added objc_super.init(receiver: AnyObject!, super_class: AnyClass!)Modified NSObject.alloc() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func alloc() -> Self! ``` | iOS 8.0 |
| To | ``` class func alloc() -> Self ``` | iOS 8.3 |

Modified NSObject.allocWithZone(NSZone) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func allocWithZone(_ zone: NSZone) -> Self! ``` | iOS 8.1 |
| To | ``` class func allocWithZone(_ zone: NSZone) -> Self ``` | iOS 8.3 |

Modified NSObject.new() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func `new`() -> Self! ``` | iOS 8.0 |
| To | ``` class func new() -> Self ``` | iOS 8.3 |

Modified NSObjectProtocol.self() -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func `self`() -> Self! ``` | iOS 8.0 |
| To | ``` func `self`() -> Self ``` | iOS 8.3 |

Modified objc_method_description [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_method_description {     var name: Selector     var types: UnsafeMutablePointer<Int8> } ``` |
| To | ``` struct objc_method_description {     var name: Selector     var types: UnsafeMutablePointer<Int8>     init()     init(name name: Selector, types types: UnsafeMutablePointer<Int8>) } ``` |

Modified objc_object [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_object {     var isa: AnyClass! } ``` |
| To | ``` struct objc_object {     var isa: AnyClass!     init()     init(isa isa: AnyClass!) } ``` |

Modified objc_property_attribute_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_property_attribute_t {     var name: UnsafePointer<Int8>     var value: UnsafePointer<Int8> } ``` |
| To | ``` struct objc_property_attribute_t {     var name: UnsafePointer<Int8>     var value: UnsafePointer<Int8>     init()     init(name name: UnsafePointer<Int8>, value value: UnsafePointer<Int8>) } ``` |

Modified objc_super [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct objc_super {     var receiver: AnyObject!     var super_class: AnyClass! } ``` |
| To | ``` struct objc_super {     var receiver: AnyObject!     var super_class: AnyClass!     init()     init(receiver receiver: AnyObject!, super_class super_class: AnyClass!) } ``` |

Modified autoreleasepool(() -> ())

|  | Declaration |
| --- | --- |
| From | ``` func autoreleasepool(_ code: () -> ()) ``` |
| To | ``` func autoreleasepool(_ code: @noescape () -> ()) ``` |

Modified class_addIvar(AnyClass!, UnsafePointer<Int8>, Int, UInt8, UnsafePointer<Int8>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func class_addIvar(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ size: UInt, _ alignment: UInt8, _ types: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` func class_addIvar(_ cls: AnyClass!, _ name: UnsafePointer<Int8>, _ size: Int, _ alignment: UInt8, _ types: UnsafePointer<Int8>) -> Bool ``` |

Modified class_getInstanceSize(AnyClass!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func class_getInstanceSize(_ cls: AnyClass!) -> UInt ``` |
| To | ``` func class_getInstanceSize(_ cls: AnyClass!) -> Int ``` |

Modified method_getArgumentType(Method, UInt32, UnsafeMutablePointer<Int8>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func method_getArgumentType(_ m: Method, _ index: UInt32, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: UInt) ``` |
| To | ``` func method_getArgumentType(_ m: Method, _ index: UInt32, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: Int) ``` |

Modified method_getReturnType(Method, UnsafeMutablePointer<Int8>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func method_getReturnType(_ m: Method, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: UInt) ``` |
| To | ``` func method_getReturnType(_ m: Method, _ dst: UnsafeMutablePointer<Int8>, _ dst_len: Int) ``` |

Modified objc_allocateClassPair(AnyClass!, UnsafePointer<Int8>, Int) -> AnyClass!

|  | Declaration |
| --- | --- |
| From | ``` func objc_allocateClassPair(_ superclass: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: UInt) -> AnyClass! ``` |
| To | ``` func objc_allocateClassPair(_ superclass: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: Int) -> AnyClass! ``` |

Modified objc_duplicateClass(AnyClass!, UnsafePointer<Int8>, Int) -> AnyClass!

|  | Declaration |
| --- | --- |
| From | ``` func objc_duplicateClass(_ original: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: UInt) -> AnyClass! ``` |
| To | ``` func objc_duplicateClass(_ original: AnyClass!, _ name: UnsafePointer<Int8>, _ extraBytes: Int) -> AnyClass! ``` |

Modified objc_memmove_collectable(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_memmove_collectable(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ size: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func objc_memmove_collectable(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ size: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified objc_setCollectionRatio(Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_setCollectionRatio(_ ratio: UInt) ``` | iOS 8.0 |
| To | ``` func objc_setCollectionRatio(_ ratio: Int) ``` | iOS 8.3 |

Modified objc_setCollectionThreshold(Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_setCollectionThreshold(_ threshold: UInt) ``` | iOS 8.0 |
| To | ``` func objc_setCollectionThreshold(_ threshold: Int) ``` | iOS 8.3 |

Modified objc_set_collection_ratio(Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_set_collection_ratio(_ ratio: UInt) ``` | iOS 8.0 |
| To | ``` func objc_set_collection_ratio(_ ratio: Int) ``` | iOS 8.3 |

Modified objc_set_collection_threshold(Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objc_set_collection_threshold(_ threshold: UInt) ``` | iOS 8.0 |
| To | ``` func objc_set_collection_threshold(_ threshold: Int) ``` | iOS 8.3 |

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
