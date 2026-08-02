---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOOrQualifier.html
archived_at: '2026-07-15T08:13:47.197043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOOrQualifier

> **__Inherits from:__**
> : [EOQualifier](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvc5lbnruwm2lfoi)

> **__Implements:__**
> : NSCoding: EOKeyValueArchiving

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOOrQualifier is a subclass of EOQualifier that contains multiple qualifiers. EOOrQualifier implements the EOQualifierEvaluation interface, which defines the method evaluateWithObject for in-memory evaluation. When an EOOrQualifier object receives an __evaluateWithObject__ message, it evaluates each of its qualifiers until one of them returns true. If one of its qualifiers returns true, the EOOrQualifier object returns true immediately. If all of its qualifiers return false, the EOOrQualifier object returns false.

## Interfaces Implemented

---

> : EOQualifierEvaluation: evaluateWithObject: : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5zfc5lbnruwm2lfoixwg3dbonzum33sinxwizls): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3skf2wc3djmzuwk4rpmrswg33emvhwe2tfmn2a): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5zfc5lbnruwm2lfoixwk3tdn5sgkv3jorueg33emvza): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3skf2wc3djmzuwk4rpmrswg33emvlws5dijnsxsvtbnr2wkvlomfzgg2djozsxe): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5zfc5lbnruwm2lfoixwk3tdn5sgkv3joruewzlzkzqwy5lfifzgg2djozsxe):

## Constructors

---

### EOOrQualifier

`public EOOrQualifier(NSArray qualifiers)`

Creates and returns a new EOOrQualifier. If _qualifiers_ is provided, the EOOrQualifier is initialized with the qualifiers in _qualifiers_.

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

`public boolean evaluateWithObject(NSKeyValueCodingAdditions anObject);`

Returns true if _anObject_ satisfies the qualifier, false otherwise. When an EOOrQualifier object receives an [evaluateWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5zfc5lbnruwm2lfoixwk5tbnr2wc5dfk5uxi2cpmjvgky3u) message, it evaluates each of its qualifiers until one of them returns true. If any of its qualifiers returns true, the EOOrQualifier object returns true immediately. If all of its qualifiers return false, the EOOrQualifier object returns false. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

### qualifiers

`NSArray qualifiers()`

Returns the receiver's qualifiers.

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
