---
title: Key-Value Observing Programming Guide
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOImplementation.html
archived_at: '2026-07-15T07:16:19.095971Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Observing Programming Guide](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Registering%20Dependent%20Keys.md)

# Key-Value Observing Implementation Details

Automatic key-value observing is implemented using a technique called _isa-swizzling_.

The `isa` pointer, as the name suggests, points to the object's class which maintains a dispatch table. This dispatch table essentially contains pointers to the methods the class implements, among other data.

When an observer is registered for an attribute of an object the isa pointer of the observed object is modified, pointing to an intermediate class rather than at the true class. As a result the value of the isa pointer does not necessarily reflect the actual class of the instance.

You should never rely on the `isa` pointer to determine class membership. Instead, you should use the [class](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class) method to determine the class of an object instance.

[Next](Document%20Revision%20History.md)[Previous](Registering%20Dependent%20Keys.md)

