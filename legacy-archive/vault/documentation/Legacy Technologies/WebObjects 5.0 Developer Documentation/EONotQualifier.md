---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EONotQualifier.html
archived_at: '2026-07-15T08:13:47.082070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EONotQualifier

> **__Inherits from:__**
> : [EOQualifier](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvc5lbnruwm2lfoi)

> **__Implements:__**
> : NSCoding: EOKeyValueArchiving

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EONotQualifier is a subclass of EOQualifier that contains a single qualifier. When an EONotQualifier object is evaluated, it returns the inverse of the result obtained by evaluating the qualifier it contains.

EONotQualifier implements the EOQualifierEvaluation interface, which defines the method evaluateWithObject for in-memory evaluation. When an EONotQualifier object receives an __evaluateWithObject__ message, it evaluates the given object to determine if it satisfies the qualifier criteria.

You can generate SQL code for an EONotQualifier using the EOSQLExpression static method __sqlStringForNegatedQualifier__.

## Interfaces Implemented

---

> : EOQualifierEvaluation: evaluateWithObject: : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjzxxiulvmfwgsztjmvzc6y3mmfzxgrtpojbw6zdfoi): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ttporixkylmnftgszlsf5sgky3pmrsu6ytkmvrxi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjzxxiulvmfwgsztjmvzc6zlomnxwizkxnf2gqq3pmrsxe): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ttporixkylmnftgszlsf5sgky3pmrsvo2lunbfwk6kwmfwhkzkvnzqxey3inf3gk4q): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjzxxiulvmfwgsztjmvzc6zlomnxwizkxnf2gqs3fpflgc3dvmvaxey3inf3gk4q):

## Constructors

---

### EONotQualifier

`public com.webobjects.eocontrol.EONotQualifier(EOQualifier aQualifier)`

Creates and returns a new EONotQualifier

If _aQualifier_ is specified, it is used as the qualifier. For example, the following code excerpt constructs a qualifier, `baseQual`, and uses it to initialize an EONotQualifier, `negQual`. The EONotQualifier `negQual` is then used to filter an in-memory array. The code excerpt returns an array of Guest objects whose __lastName__ properties do _not_ have the same value as the __lastName__ property of the guest's sponsoring member (this example is based on the Rentals sample database). In other words, the EONotQualifier `negQual` inverts the effects of `baseQual`.

> ```
> NSArray guests /* Assume this exists */
> EOQualifier baseQual;
> EONotQualifier negQual;
>
> baseQual = EOQualifier.qualifierWithQualifierFormat("lastName = member.lastName", null);
> negQual = new EONotQualifier(baseQual);
> return EOQualifier.filteredArrayWithQualifier(guests, negQual);
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

### encodeWithKeyValueArchiver

`public void encodeWithKeyValueArchiver(EOKeyValueArchiver archiver)`

Conformance to EOKeyValueArchiving.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to NSCoding.

---

### evaluateWithObject

`public boolean evaluateWithObject(NSKeyValueCodingAdditions anObject)`

Returns true if the object _anObject_ satisfies the EONotQualifier, false otherwise. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

### qualifier

`public EOQualifier qualifier()`

Returns the receiver's qualifier.

---

### __qualifierWithBindings__

`public EOQualifier qualifierWithBindings( NSDictionary, boolean)`

Description forthcoming.

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
