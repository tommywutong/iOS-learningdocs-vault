---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOOrQualifier.html
archived_at: '2026-07-15T08:11:37.882909Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOOrQualifier

> **__Inherits
> from:__**
> : [(com.apple.client.eocontrol) EOQualifier](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvc5lbnruwm2lfoi) : Object
> (com.apple.yellow.eocontrol) EOQualifier : NSObject

> **__Implements:__**
> : [EOQualifierEvaluation](EOQualifierEvaluation.md#apple-ijaucq2dijdum)
> : (com.apple.client.eocontrol only) NSCoding

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOOrQualifier is a subclass of EOQualifier that contains multiple
qualifiers. EOOrQualifier implements the EOQualifierEvaluation interface,
which defines the method [evaluateWithObject](EOQualifierEvaluation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi) for in-memory
evaluation. When an EOOrQualifier object receives an `evaluateWithObject` message,
it evaluates each of its qualifiers until one of them returns true.
If one of its qualifiers returns true, the EOOrQualifier object
returns true immediately. If all of its qualifiers return false,
the EOOrQualifier object returns false.

## Interfaces Implemented

---

> EOQualifierEvaluation: [evaluateWithObject](EOQualifierEvaluation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi)
>
> NSCoding
> (com.apple.client.eocontrol only): `classForCoder`
> : `encodeWithCoder`

## Constructors

---

### EOOrQualifier

`public EOOrQualifier(NSArray qualifiers)`

Creates and returns a new EOOrQualifier. If _qualifiers_ is
provided, the EOOrQualifier is initialized with the qualifiers in _qualifiers._

---

## Instance Methods

---

### evaluateWithObject:

`(com.apple.client.eocontrol) public boolean
evaluateWithObject(EOKeyValueCodingAdditions anObject);`

`(com.apple.yellow.eocontrol) public boolean evaluateWithObject(Object anObject)`

Returns true if _anObject_ satisfies
the qualifier, false otherwise. When an EOOrQualifier object receives an [evaluateWithObject:](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5zfc5lbnruwm2lfoixwk5tbnr2wc5dfk5uxi2cpmjvgky3uhi) message,
it evaluates each of its qualifiers until one of them returns true.
If any of its qualifiers returns true, the EOOrQualifier object
returns true immediately. If all of its qualifiers return false,
the EOOrQualifier object returns false. This method can throw one
of several possible exceptions if an error occurs. If your application
allows users to construct arbitrary qualifiers (such as through
a user interface), you may want to write code to catch any exceptions
and respond to errors (for example, by displaying a panel saying
that the user typed a poorly formed qualifier).

---

### qualifiers

`NSArray qualifiers()`

Returns the receiver's qualifiers.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
