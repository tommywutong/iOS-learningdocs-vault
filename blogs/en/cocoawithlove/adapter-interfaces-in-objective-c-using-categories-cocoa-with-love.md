---
title: 'Adapter interfaces in Objective-C, using categories. | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/adapter-interfaces-in-objective-c-using.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:c41fc4be79894981'
translated: false
---

> 原文：[Adapter interfaces in Objective-C, using categories. | Cocoa with Love](https://www.cocoawithlove.com/2008/05/adapter-interfaces-in-objective-c-using.html)　·　Cocoa with Love (Matt Gallagher)

The Categories feature of Objective-C lets the programmer add extra sets of methods after compilation, something impossible in most compiled languages. Using this feature, here is an Objective-C variant of the classic "Adapter" design pattern that allows two classes to work closely together, without two-way coupling dependency problems.

## Connecting two classes: the simple version

This article is about making two (or more) classes work together. The traditional way that happens is like this:

1. Implement "Class A" with a given set of methods
2. Implement 'Class B', invoking methods that 'Class A' already provides

Obviously, this is how almost all class interaction works. And it works well, especially in situations where "Class B" is dependent on "Class A" but "Class A" remains independent.

## Working closely together works badly

When both classes need to work closely together, keeping their interfaces and operation clean and clear becomes difficult.

### What can we do when the second class needs information that the first class doesn't provide?

We could keep adding methods to "Class A" to give "Class B" everything it needs but coupling two classes together (by adding extra design features to one purely for the other to use) is generally considered bad for maintenance reasons.

If the extra methods are useful in a more general sense, then this isn't a problem but if these extra methods are only useful for "Class B", then we are really breaking the abstraction between the two classes because the "Class A" now knows everything that "Class B" needs internally. Non-hierarchic coupling of classes is normally considered an "anti-pattern" (bad design choice) for this reason.

### How do we neatly perform a calculation that needs parts inside each class?

If we are performing an aggregate calculation where parts of the calculation need to be performed inside each of the two classes, then the algorithm may be difficult to read and maintain because it is split across multiple modules.

We could create a third class or module to perform the calculation in a unified place but that may generate the same coupling issues described in the previous section, where the third class now needs specifically tailored interfaces into "Class A" and "Class B" in order to access the data it needs to perform its work.

## A solution using categories

Most of the time, categories in Objective-C are used to define extra methods for a class in a separate library — where the original set of methods on a class can't be changed. Categories can also be used to break up a class according to areas of concern. This is how we will use it in this solution: breaking coupling issues between classes by dividing the classes up according to their areas of concern.

Our problem consists of these constraints:

1. "Class B" needs some detailed information from "Class A"
2. It's not really "Class A"'s job to care about what "Class B" is doing.

We can solve this problem by creating extra "Class A" methods inside "Class B"'s source file. Specifically, we create a category of "Class A" inside the source file for "Class B".

This allows the source file for "Class A" to remain independent of "Class B", yet still allows "Class B" to obtain specially catered information. The result is that the methods in the source file for "Class A" are those public "Class A" methods that any class may use, whereas "Class B" defines its own private interface — so private that the base "Class A" definition remains unaware of it. It also allows a calculation which may be split across both classes to be performed entirely in one source file, for neatness and clarity.

The "Adapter" interface described in the article title refers to the "Adapter" design pattern. Normally, an Adapter is a third class written for the purposes of linking two incompatible classes. In this case, Objective-C's categories let us create the Adapter inteface as an extension of "Class A" but residing inside the implementation file for "Class B".

## Summary

The Adapter interface is structured as follows.

Class A's implementation:

```objc
@implementation Class_A
// Class_A's methods
@end
```

Class_B's implementation:

```objc
@ implementation Class_A (Class_B_Adapter)
// Methods to allow Class_B to connect to Class_A
// Methods that Class_B can use to calculate values dependent on both Class_A
//   and Class_B
@end

@ implementation Class_B
// Class_B's methods
@end
```

Note that these are the "implementation" files, not the "interface" files. Since this is a private interface for "Class B" to interact with "Class A", the "Class_A (ClassBAdapter)" should not appear in the interface file.

This type of design allows "Class B" to work closely with "Class A" without forcing the default implementation of "Class A" to change just to suit "Class B" and further allows the implementation of the "ClassBAdapter" methods to live close to their usage.
