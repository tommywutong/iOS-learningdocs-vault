---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOKeyValueQualifier.html
archived_at: '2026-07-18T01:28:26.506316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOKeyGlobalID.md)
[!](EONotQualifier.md)

---

# EOKeyValueQualifier

__Inherits From:__
EOQualifier

__Implements:__
EOQualifierEvaluation
NSCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOKeyValueQualifier is a subclass of EOQualifier that compares a named property of an object with a supplied value, for example, "salary > 1500". EOKeyValueQualifier implements the EOQualifierEvaluation interface, which defines the method [__evaluateWithObject__](EOQualifierEvaluation.md)for in-memory evaluation. When an EOKeyValueQualifier object receives an [__evaluateWithObject__](EOQualifierEvaluation.md)message, it evaluates the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyValueQualifier can be used to generate SQL. When it's used for this purpose, the key should be a valid property name of the root entity for the qualifier (or a valid key path).

## Interfaces Implemented

**EOQualifierEvaluation**

**[- evaluateWithObject](EOQualifierEvaluation.md)**

**NSCoding (Java Client only)**

**classForCoder

**encodeWithCoder****

## Constructors

---

#### EOKeyValueQualifier

public __EOKeyValueQualifier__ (java.lang.String _key_, NSSelector _selector_, java.lang.Object _value_)

Creates and returns a new EOKeyValueQualifier.

If key, selector, and value are provided, the EOKeyValueQualifier compares values for _key_ to _value_ using the operator method _selector_.The possible values for _selector_ are as follows:

- [QualifierOperatorEqual](EOQualifier.md)
- [QualifierOperatorNotEqual](EOQualifier.md)
- [QualifierOperatorLessThan](EOQualifier.md)
- [QualifierOperatorGreaterThan](EOQualifier.md)
- [QualifierOperatorLessThanOrEqualTo](EOQualifier.md)
- [QualifierOperatorGreaterThanOrEqualTo](EOQualifier.md)
- [QualifierOperatorContains](EOQualifier.md)
- [QualifierOperatorLike](EOQualifier.md)
- [QualifierOperatorCaseInsensitiveLike](EOQualifier.md)

Enterprise Objects Framework supports SQL generation for these methods only. You can generate SQL using the SQLExpression static method __sqlStringForKeyValueQualifier__ .

For example, the following excerpt creates an EOKeyValueQualifier `qual` that has the key "name", the operator method QualifierOperatorEqual, and the value "Smith". Once constructed, the qualifier `qual` is used to filter an in-memory array.

> ```
> NSArray employees /* Assume this exists */
> EOKeyValueQualifier qual = new EOKeyValueQualifier("name",
>     EOQualifier.QualifierOperatorEqual, "Smith");
> return EOQualifier.filteredArrayWithQualifier(employees, qual);
> ```

## Instance Methods

---

#### evaluateWithObject

EOQualifierEvaluation interface

public boolean __evaluateWithObject__ (java.lang.Object _anObject_)

Returns __true__ if the object _anObject_ satisfies the qualifier, __false__ otherwise. When an EOKeyValueQualifier object receives the `evaluateWithObject` message, it evaluates _anObject_ to determine if it meets the qualifier criteria. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### key

public java.lang.String __key__ ()

Returns the receiver's key.

---

#### selector

public NSSelector __selector__ ()

Returns the receiver's selector.

---

#### value

public java.lang.Object __value__ ()

Returns the receiver's value.

---

[!](EOKeyGlobalID.md)
[!](EONotQualifier.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
