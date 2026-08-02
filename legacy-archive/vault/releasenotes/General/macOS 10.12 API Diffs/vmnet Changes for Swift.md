---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/vmnet.html
archived_at: '2026-07-18T02:51:43.186088Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# vmnet Changes for Swift

### vmnet

Modified [interface_event_t [struct]](https://developer.apple.com/documentation/vmnet/interface_event_t)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct interface_event_t : OptionSetType {     init(rawValue rawValue: UInt32)     static var VMNET_INTERFACE_PACKETS_AVAILABLE: interface_event_t { get } } ``` | OptionSetType |
| To | ``` struct interface_event_t : OptionSet {     init(rawValue rawValue: UInt32)     static var VMNET_INTERFACE_PACKETS_AVAILABLE: interface_event_t { get }     func intersect(_ other: interface_event_t) -> interface_event_t     func exclusiveOr(_ other: interface_event_t) -> interface_event_t     mutating func unionInPlace(_ other: interface_event_t)     mutating func intersectInPlace(_ other: interface_event_t)     mutating func exclusiveOrInPlace(_ other: interface_event_t)     func isSubsetOf(_ other: interface_event_t) -> Bool     func isDisjointWith(_ other: interface_event_t) -> Bool     func isSupersetOf(_ other: interface_event_t) -> Bool     mutating func subtractInPlace(_ other: interface_event_t)     func isStrictSupersetOf(_ other: interface_event_t) -> Bool     func isStrictSubsetOf(_ other: interface_event_t) -> Bool } extension interface_event_t {     func union(_ other: interface_event_t) -> interface_event_t     func intersection(_ other: interface_event_t) -> interface_event_t     func symmetricDifference(_ other: interface_event_t) -> interface_event_t } extension interface_event_t {     func contains(_ member: interface_event_t) -> Bool     mutating func insert(_ newMember: interface_event_t) -> (inserted: Bool, memberAfterInsert: interface_event_t)     mutating func remove(_ member: interface_event_t) -> interface_event_t?     mutating func update(with newMember: interface_event_t) -> interface_event_t? } extension interface_event_t {     convenience init()     mutating func formUnion(_ other: interface_event_t)     mutating func formIntersection(_ other: interface_event_t)     mutating func formSymmetricDifference(_ other: interface_event_t) } extension interface_event_t {     convenience init<S : Sequence where S.Iterator.Element == interface_event_t>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: interface_event_t...)     mutating func subtract(_ other: interface_event_t)     func isSubset(of other: interface_event_t) -> Bool     func isSuperset(of other: interface_event_t) -> Bool     func isDisjoint(with other: interface_event_t) -> Bool     func subtracting(_ other: interface_event_t) -> interface_event_t     var isEmpty: Bool { get }     func isStrictSuperset(of other: interface_event_t) -> Bool     func isStrictSubset(of other: interface_event_t) -> Bool } ``` | OptionSet |

Modified [interface_ref](https://developer.apple.com/documentation/vmnet/interface_ref)

|  | Declaration |
| --- | --- |
| From | ``` typealias interface_ref = COpaquePointer ``` |
| To | ``` typealias interface_ref = OpaquePointer ``` |

Modified [vmnet_interface_set_event_callback(_: interface_ref, _: interface_event_t, _: DispatchQueue?, _: ( (interface_event_t, xpc_object_t) -> Swift.Void)?) -> vmnet_return_t](https://developer.apple.com/documentation/vmnet/1419568-vmnet_interface_set_event_callba)

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_interface_set_event_callback(_ interface: interface_ref, _ flags: interface_event_t, _ queue: dispatch_queue_t?, _ handler: ((interface_event_t, xpc_object_t) -> Void)?) -> vmnet_return_t ``` |
| To | ``` func vmnet_interface_set_event_callback(_ interface: interface_ref, _ flags: interface_event_t, _ queue: DispatchQueue?, _ handler: (@escaping (interface_event_t, xpc_object_t) -> Swift.Void)?) -> vmnet_return_t ``` |

Modified [vmnet_start_interface(_: xpc_object_t, _: DispatchQueue, _: (vmnet_return_t, xpc_object_t?) -> Swift.Void) -> interface_ref?](https://developer.apple.com/documentation/vmnet/1419500-vmnet_start_interface)

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_start_interface(_ interface_desc: xpc_object_t, _ queue: dispatch_queue_t, _ handler: (vmnet_return_t, xpc_object_t?) -> Void) -> interface_ref ``` |
| To | ``` func vmnet_start_interface(_ interface_desc: xpc_object_t, _ queue: DispatchQueue, _ handler: @escaping (vmnet_return_t, xpc_object_t?) -> Swift.Void) -> interface_ref? ``` |

Modified [vmnet_stop_interface(_: interface_ref, _: DispatchQueue, _: (vmnet_return_t) -> Swift.Void) -> vmnet_return_t](https://developer.apple.com/documentation/vmnet/1419526-vmnet_stop_interface)

|  | Declaration |
| --- | --- |
| From | ``` func vmnet_stop_interface(_ interface: interface_ref, _ queue: dispatch_queue_t, _ handler: (vmnet_return_t) -> Void) -> vmnet_return_t ``` |
| To | ``` func vmnet_stop_interface(_ interface: interface_ref, _ queue: DispatchQueue, _ handler: @escaping (vmnet_return_t) -> Swift.Void) -> vmnet_return_t ``` |

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
