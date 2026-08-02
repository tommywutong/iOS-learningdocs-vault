---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOKeyComparisonQualifier.html
archived_at: '2026-07-18T01:28:26.363697Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOGlobalID.md)
[!](EOKeyGlobalID.md)

---

# EOKeyComparisonQualifier

__Inherits From:__
EOQualifier

__Implements:__
EOQualifierEvaluation
NSCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOKeyComparisonQualifier is a subclass of EOQualifier that compares a named property of an object with a named value of another object. For example, to return all of the employees whose salaries are greater than those of their managers, you might use an expression such as "salary > manager.salary", where "salary" is the _left key_ and "manager.salary" is the _right key_. The "left key" is the property of the first object that's being compared to a property in a second object; the property in the second object is the "right key." Both the left key and the right key might be key paths. You can use EOKeyComparisonQualifier to compare properties of two different objects or to compare two properties of the same object.

EOKeyComparisonQualifier implements the EOQualifierEvaluation interface, which defines the method [__evaluateWithObject__](EOQualifierEvaluation.md)for in-memory evaluation. When an EOKeyComparisonQualifier object receives an [__evaluateWithObject__](EOQualifierEvaluation.md)message, it evaluates the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyComparisonQualifier can be used to generate SQL. When it's used for this purpose, the key should be a valid property name of the root entity for the qualifier (or a valid key path).

## Interfaces Implemented

**EOQualifierEvaluation**

**[- evaluateWithObject](EOQualifierEvaluation.md)**

**NSCoding (Java Client only)**

**classForCoder

**encodeWithCoder****

## Constructors

---

#### EOKeyComparisonQualifier

public __EOKeyComparisonQualifier__ (java.lang.String _leftKey_, NSSelector _selector_, java.lang.String _rightKey_)

Creates and returns a new EOKeyComparisonQualifier object that compares the properties named by _leftKey_ and _rightKey_, using the operator method _selector_.

- [QualifierOperatorEqual](EOQualifier.md)
- [QualifierOperatorNotEqual](EOQualifier.md)
- [QualifierOperatorLessThan](EOQualifier.md)
- [QualifierOperatorGreaterThan](EOQualifier.md)
- [QualifierOperatorLessThanOrEqualTo](EOQualifier.md)
- [QualifierOperatorGreaterThanOrEqualTo](EOQualifier.md)
- [QualifierOperatorContains](EOQualifier.md)
- [QualifierOperatorLike](EOQualifier.md)
- [QualifierOperatorCaseInsensitiveLike](EOQualifier.md)

Enterprise Objects Framework supports SQL generation for these methods only. You can generate SQL using the SQLExpression static method __sqlStringForKeyComparisonQualifier__ .

For example, the following excerpt creates an EOKeyComparisonQualifier `qual` that has the left key "lastName", the operator method EOQualifierOperatorEqual, and the right key "member.lastName". Once constructed, the qualifier `qual` is used to filter an in-memory array. The code excerpt returns an array of Guest objects whose __lastName__ properties have the same value as the __lastName__ property of the guest's sponsoring member (this example is based on the Rentals sample database).

> ```
> NSArray guests; /* Assume this exists */
> EOKeyComparisonQualifier qual = new EOKeyComparisonQualifier("lastName",
>     EOQualifier.QualifierOperatorEqual,
>     "member.lastName");
>
> return EOQualifier.filteredArrayWithQualifier(guests, qual);
> ```

## Instance Methods

---

#### evaluateWithObject

EOQualifierEvaluation interface

public boolean __evaluateWithObject__ (java.lang.Object _object_)

Returns __true__ if the object _object_ satisfies the qualifier, __false__ otherwise. When an EOKeyComparisonQualifier object receives an `evaluateWithObject` message, it evaluates _object_ to determine if it meets the qualifier criteria. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### leftKey

public java.lang.String __leftKey__ ()

Returns the receiver's left key_._

---

#### rightKey

public java.lang.String __rightKey__ ()

Returns the receiver's right key.

---

#### selector

public NSSelector __selector__ ()

Returns the receiver's selector.

---

[!](EOGlobalID.md)
[!](EOKeyGlobalID.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
