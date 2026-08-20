---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOKeyValueQualifier.html
archived_at: '2026-07-15T08:13:47.063598Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyValueQualifier

> **__Inherits from:__**
> : [EOQualifier](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvc5lbnruwm2lfoi)

> **__Implements:__**
> : NSCoding: EOKeyValueArchiving

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOKeyValueQualifier is a subclass of EOQualifier that compares a named property of an object with a supplied value, for example, "salary > 1500". EOKeyValueQualifier implements the EOQualifierEvaluation interface, which defines the method evaluateWithObject for in-memory evaluation. When an EOKeyValueQualifier object receives an __evaluateWithObject__ message, it evaluates the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyValueQualifier can be used to generate SQL. When it's used for this purpose, the key should be a valid property name of the root entity for the qualifier (or a valid key path).

## Interfaces Implemented

---

> : EOQualifierEvaluation: evaluateWithObject: : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsvtbnr2wkulvmfwgsztjmvzc6y3mmfzxgrtpojbw6zdfoi): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvixkylmnftgszlsf5sgky3pmrsu6ytkmvrxi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsvtbnr2wkulvmfwgsztjmvzc6zlomnxwizkxnf2gqq3pmrsxe): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvixkylmnftgszlsf5sgky3pmrsvo2lunbfwk6kwmfwhkzkvnzqxey3inf3gk4q): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjnsxsvtbnr2wkulvmfwgsztjmvzc6zlomnxwizkxnf2gqs3fpflgc3dvmvaxey3inf3gk4q):

## Constructors

---

### EOKeyValueQualifier

`public EOKeyValueQualifier( String key, NSSelector selector, Object value)`

Creates and returns a new EOKeyValueQualifier.

If _key_, _selector_, and _value_ are provided, the EOKeyValueQualifier compares values for _key_ to _value_ using the operator method _selector_.The possible values for _selector_ are as follows:

- QualifierOperatorEqual
- QualifierOperatorNotEqual
- QualifierOperatorLessThan
- QualifierOperatorGreaterThan
- QualifierOperatorLessThanOrEqualTo
- QualifierOperatorGreaterThanOrEqualTo
- QualifierOperatorContains
- QualifierOperatorLike
- QualifierOperatorCaseInsensitiveLike

Enterprise Objects Framework supports SQL generation for these methods only. You can generate SQL using the EOSQLExpression static method __sqlStringForKeyValueQualifier__.

For example, the following excerpt creates an EOKeyValueQualifier `qual` that has the key "name", the operator method `QualifierOperatorEqual`, and the value "Smith". Once constructed, the qualifier `qual` is used to filter an in-memory array.

> ```
> NSArray employees /* Assume this exists */
> EOKeyValueQualifier qual = new EOKeyValueQualifier("name",
>     EOQualifier.QualifierOperatorEqual, "Smith");
> return EOQualifier.filteredArrayWithQualifier(employees, qual);
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

`public boolean evaluateWithObject(NSKeyValueCodingAdditions anObject)`

Returns true if the object _anObject_ satisfies the qualifier, false otherwise. When an EOKeyValueQualifier object receives the __evaluateWithObject__message, it evaluates _anObject_ to determine if it meets the qualifier criteria. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

### key

`public String key()`

Returns the receiver's key.

---

### __qualifierWithBindings__

`public EOQualifier qualifierWithBindings( NSDictionary, boolean)`

Description forthcoming.

---

### selector

`public NSSelector selector()`

Returns the receiver's selector.

---

### __toString__

`public String toString()`

Description forthcoming.

---

### value

`public Object value()`

Returns the receiver's value.

---

### validateKeysWithRootClassDescription

`public voidvalidateKeysWithRootClassDescription(EOClassDescription classDesc)`

Ensures that the receiver contains keys and key paths that belong to or originate from _classDesc_. This method raises an exception if an unknown key is found, otherwise it returns `null` to indicate that the keys contained by the qualifier are valid.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
