---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOKeyComparisonQualifier.html
archived_at: '2026-07-15T08:13:46.987561Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyComparisonQualifier

> **__Inherits from:__**
> : [EOQualifier](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvc5lbnruwm2lfoi)

> **__Implements:__**
> : EOQualifierEvaluation: NSCoding: EOKeyValueArchiving

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOKeyComparisonQualifier is a subclass of EOQualifier that compares a named property of an object with a named value of another object. For example, to return all of the employees whose salaries are greater than those of their managers, you might use an expression such as "salary > manager.salary", where "salary" is the __left key__ and "manager.salary" is the __right key__. The "left key" is the property of the first object that's being compared to a property in a second object; the property in the second object is the "right key." Both the left key and the right key might be key paths. You can use EOKeyComparisonQualifier to compare properties of two different objects or to compare two properties of the same object.

EOKeyComparisonQualifier implements the EOQualifierEvaluation interface, which defines the method evaluateWithObject for in-memory evaluation. When an EOKeyComparisonQualifier object receives an __evaluateWithObject__ message, it evaluates the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyComparisonQualifier can be used to generate SQL. When it's used for this purpose, the key should be a valid property name of the root entity for the qualifier (or a valid key path).

## Interfaces Implemented

---

> : EOQualifierEvaluation: evaluateWithObject: : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvzc6y3mmfzxgrtpojbw6zdfoi): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpfbw63lqmfzgs43pnzixkylmnftgszlsf5sgky3pmrsu6ytkmvrxi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvzc6zlomnxwizkxnf2gqq3pmrsxe): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpfbw63lqmfzgs43pnzixkylmnftgszlsf5sgky3pmrsvo2lunbfwk6kwmfwhkzkvnzqxey3inf3gk4q): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvzc6zlomnxwizkxnf2gqs3fpflgc3dvmvaxey3inf3gk4q):

## Constructors

---

### EOKeyComparisonQualifier

`public EOKeyComparisonQualifier( String leftKey, NSSelector selector, String rightKey)`

Creates and returns a new EOKeyComparisonQualifier object that compares the properties named by _leftKey_ and _rightKey_, using the operator method _selector_, one of:

- QualifierOperatorEqual
- QualifierOperatorNotEqual
- QualifierOperatorLessThan
- QualifierOperatorGreaterThan
- QualifierOperatorLessThanOrEqualTo
- QualifierOperatorGreaterThanOrEqualTo
- QualifierOperatorContains
- QualifierOperatorLike
- QualifierOperatorCaseInsensitiveLike

Enterprise Objects Framework supports SQL generation for these methods only. You can generate SQL using the EOSQLExpression static method __sqlStringForKeyComparisonQualifier__.

For example, the following excerpt creates an EOKeyComparisonQualifier `qual` that has the left key "lastName", the operator method EOQualifierOperatorEqual, and the right key "member.lastName". Once constructed, the qualifier `qual` is used to filter an in-memory array. The code excerpt returns an array of Guest objects whose __lastName__ properties have the same value as the __lastName__ property of the guest's sponsoring member (this example is based on the Rentals sample database).

> ```
> NSArray guests; /* Assume this exists */
> EOKeyComparisonQualifier qual = new EOKeyComparisonQualifier("lastName",
>     EOQualifier.QualifierOperatorEqual,
>     "member.lastName");
>
> return EOQualifier.filteredArrayWithQualifier(guests, qual);
> ```

---

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Conformance to NSCoding.

---

### decodeWithKeyValueUnarchiver

`public static Object decodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

## Instance Methods

---

### __addQualifierKeysToSet__

`public void addQualifierKeysToSet(NSMutableSet aSet)`

Description forthcoming.

---

### classForCoder

`public Class classForCoder()`

Conformance to NSCoding.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to NSCoding.

---

### encodeWithKeyValueArchiver

`public void encodeWithKeyValueArchiver(EOKeyValueArchiver archiver)`

Conformance to EOKeyValueArchiving.

---

### evaluateWithObject

`public boolean evaluateWithObject(NSKeyValueCodingAdditions object)`

Returns true if the object _object_ satisfies the qualifier, false otherwise. When an EOKeyComparisonQualifier object receives an evaluateWithObject message, it evaluates _object_ to determine if it meets the qualifier criteria. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

### leftKey

`public String leftKey()`

Returns the receiver's left key_._

---

### __qualifierWithBindings__

`public EOQualifier qualifierWithBindings( NSDictionary, boolean)`

Description forthcoming.

---

### rightKey

`public String rightKey()`

Returns the receiver's right key.

---

### selector

`public NSSelector selector()`

Returns the receiver's selector.

---

### __toString__

`public String toString()`

Description forthcoming.

---

### validateKeysWithRootClassDescription

`public void validateKeysWithRootClassDescription(EOClassDescription classDesc)`

Ensures that the receiver contains keys and key paths that belong to or originate from _classDesc_. This method raises an exception if an unknown key is found, otherwise it returns `null` to indicate that the keys contained by the qualifier are valid.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
