---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSArrayOperator.html
archived_at: '2026-07-15T08:13:56.760943Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSArray.Operator

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The NSArray.Operator interface defines an API for performing operations on the elements in an array. The method, [compute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstifzheylzfzhxazlsmf2g64rpmnxw24dvorsq), takes as its arguments an array and a key path. The array provides the objects on which to operate, and the optional key path further specifies a particular property on which to operate.

As an example, consider an operator that computes averages. To get the average salary for a set of Employee objects, send the operator a __compute__ message with "salary" as the key path. The operator gets the __salary__ value from each of the objects in the array and then returns the computed average.

Instead of invoking __compute__ directly on an operator, you can use NSArray's key-value coding methods with a specially formatted key. The character "@" introduces the name of the operator you want to perform. For example, to compute the average salary of an array's elements, you could invoke [valueForKeyPath](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf53gc3dvmvdg64slmv4vayluna) on the array with "@avg.salary" as the key path. For more information, see the [NSArray](NSArray.md#apple-ijbuqr2ei5cum) class specification.

Additionally, NSArray provides a set of default operators. To access the operators, use the method [operatorForKey](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3pobsxeylun5zem33sjnsxs), specifying the name of the operator as an argument. For information on the default operators, see the NSArray class specification.

You can augment the set of default operators with your own custom operator. Simply create a class that implements NSArray.Operator. To make it available to NSArray for use with key-value coding, use the method [setOperatorForKey](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3tmv2e64dfojqxi33sizxxes3fpe).

## Instance Methods

---

### compute

`public Object compute( NSArray values, String keyPath)`

Performs an operation on the elements in _values_ and returns the result. The _keyPath_ argument optionally specifies a particular property of the elements in values to perform the operation on.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
