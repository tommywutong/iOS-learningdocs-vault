---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOQualifierEvaluation.html
archived_at: '2026-07-18T01:28:41.630318Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOObserving-2.md)
[!](EORelationshipManipulation-2.md)

---

# EOQualifierEvaluation

__Adopted By:__

**EOKeyValueQualifier

**EOKeyComparisonQualifier

**EOAndQualifier

**EOOrQualifier

**EONotQualifier**********

## Protocol Description

The EOQualifierEvaluation protocol defines a method, __evaluateWithObject:__ , that performs in-memory evaluation of qualifiers. All qualifier classes whose objects can be evaluated in memory must implement this protocol.

---

#### evaluateWithObject:

- (BOOL)`evaluateWithObject:`_object_

Returns YES if the argument _object_ satisfies the qualifier, NO otherwise. This method can raise one of several possible exceptions if an error occurs, depending on the implementation.

---

[!](EOObserving-2.md)
[!](EORelationshipManipulation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
