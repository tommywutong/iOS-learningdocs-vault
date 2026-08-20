---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Performance.html
archived_at: '2026-07-15T07:16:14.845281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Designing for Performance

Key-value coding is efficient, especially when you rely on the default implementation to do most of the work, but it does add a level of indirection that is slightly slower than direct method invocations. Use key-value coding only when you can benefit from the flexibility that it provides, or to allow your objects to participate in the Cocoa technologies that depend on it.

### Overriding Key-Value Coding Methods

Typically, you make your objects key-value coding compliant by ensuring that they inherit from `NSObject`, and then providing the property-specific accessors and related methods as described throughout this book. You rarely need to override the default implementations of the key-value coded accessors, such as `valueForKey:` and `setValue:forKey:`, or the key-based validation methods like `validateValue:forKey:`. Because these implementations cache information about the runtime environment to increase efficiency, if you do override them to introduce custom logic, make sure that you invoke the default implementation in the superclass before returning.

### Optimizing To-Many Relationships

When you implement to-many relationships, the indexed form of the accessors provides significant performance gains in many cases, especially for mutable collections. See [Accessing Collection Properties](AccessingCollectionProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedilktk4yq) and [Defining Collection Methods](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc) for further information.

[Describing Property Relationships](Relationships.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tmlkcijbuirchinbq)

[Compliance Checklist](Compliant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3telkciffekqkjivcq)
