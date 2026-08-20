---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOQualifierEvaluation.html
archived_at: '2026-07-18T01:28:33.304796Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOQualifier.Comparison.md)
[!](EORelationshipManipulation.md)

---

# EOQualifierEvaluation

__Implemented By:__

**EOKeyValueQualifier

**EOKeyComparisonQualifier

**EOAndQualifier

**EOOrQualifier

**EONotQualifier**********

## Protocol Description

The EOQualifierEvaluation interface defines a method, __evaluateWithObject__ , that performs in-memory evaluation of qualifiers. All qualifier classes whose objects can be evaluated in memory must implement this interface.

## Instance Methods

---

#### evaluateWithObject

public boolean __evaluateWithObject__ (java.lang.Object _object_)

Returns __true__ if the argument _object_ satisfies the qualifier, __false__ otherwise. This method can throw one of several possible exceptions if an error occurs, depending on the implementation.

---

[!](EOQualifier.Comparison.md)
[!](EORelationshipManipulation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
