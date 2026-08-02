---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOAndQualifier.html
archived_at: '2026-07-15T08:13:46.115719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOAndQualifier

> **__Inherits from:__**
> : [EOQualifier](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvc5lbnruwm2lfoi)

> **__Implements:__**
> : NSCoding,: EOKeyValueArchiving

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOAndQualifier is a subclass of EOQualifier that contains multiple qualifiers. EOAndQualifier implements the EOQualifierEvaluation interface, which defines the method [evaluateWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifxgiulvmfwgsztjmvzc6zlwmfwhkylumvlws5dij5rguzldoq) for in-memory evaluation. When an EOAndQualifier object receives an __evaluateWithObject__ message, it evaluates each of its qualifiers until one of them returns `false`. If one of its qualifiers returns `false`, the EOAndQualifier object returns `false` immediately. If all of its qualifiers return `true`, the EOAndQualifier object returns `true`.

## Interfaces Implemented

---

> : EOQualifierEvaluation: [evaluateWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifxgiulvmfwgsztjmvzc6zlwmfwhkylumvlws5dij5rguzldoq): : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifxgiulvmfwgsztjmvzc6y3mmfzxgrtpojbw6zdfoi): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlomrixkylmnftgszlsf5sgky3pmrsu6ytkmvrxi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifxgiulvmfwgsztjmvzc6zlomnxwizkxnf2gqq3pmrsxe): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlomrixkylmnftgszlsf5sgky3pmrsvo2lunbfwk6kwmfwhkzkvnzqxey3inf3gk4q): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifxgiulvmfwgsztjmvzc6zlomnxwizkxnf2gqs3fpflgc3dvmvaxey3inf3gk4q):

## Constructors

---

### EOAndQualifier

`public EOAndQualifier(NSArray qualifiers)`

Creates a new EOAndQualifier. If _qualifiers_ is provided, the new EOAndQualifier is initialized with the EOQualifier objects in _qualifiers_.

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

Returns `true` if _anObject_ satisfies the qualifier, `false` otherwise. When an EOAndQualifier object receives an evaluateWithObject message, it evaluates each of its qualifiers until one of them returns `false`. If any of its qualifiers returns `false`, the EOAndQualifier object returns `false` immediately. If all of its qualifiers return `true`, the object returns `true`. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

### qualifiers

`public NSArray qualifiers()`

Returns the receiver's qualifiers.

---

### qualifierWithBindings

`public EOQualifier qualifierWithBindings( NSDictionary, boolean)`

Description forthcoming.

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

### validateKeysWithRootClassDescription

`public void validateKeysWithRootClassDescription( EOClassDescription classDesc)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
