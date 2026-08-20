---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EONotQualifier.html
archived_at: '2026-07-15T08:11:37.779988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EONotQualifier

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

EONotQualifier is a subclass of EOQualifier that contains
a single qualifier. When an EONotQualifier object is evaluated,
it returns the inverse of the result obtained by evaluating the
qualifier it contains.

EONotQualifier implements the EOQualifierEvaluation interface,
which defines the method [evaluateWithObject](EOQualifierEvaluation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi) for
in-memory evaluation. When an EONotQualifier object receives an `evaluateWithObject` message,
it evaluates the given object to determine if it satisfies the qualifier criteria.

You can generate SQL code for an EONotQualifier using the
EOSQLExpression static method `sqlStringForNegatedQualifier`.

## Interfaces Implemented

---

> EOQualifierEvaluation: [evaluateWithObject](EOQualifierEvaluation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi)
>
> NSCoding
> (com.apple.client.eocontrol only): `classForCoder`
> : `encodeWithCoder`

## Constructors

---

### EONotQualifier

`public com.apple.yellow.eocontrol.EONotQualifier(EOQualifier aQualifier)`

Creates and returns a new EONotQualifier

If _aQualifier_ is
specified, it is used as the qualifier. For example, the following
code excerpt constructs a qualifier, `baseQual`,
and uses it to initialize an EONotQualifier, `negQual`.
The EONotQualifier `negQual` is
then used to filter an in-memory array. The code excerpt returns
an array of Guest objects whose `lastName` properties
do _not_ have the same value as the `lastName` property
of the guest's sponsoring member (this example is based on the
Rentals sample database). In other words, the EONotQualifier `negQual` inverts
the effects of `baseQual`.

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

## Instance Methods

---

### evaluateWithObject

`public boolean evaluateWithObject(Object anObject)`

Returns true if the object _anObject_ satisfies
the EONotQualifier, false otherwise. This method can throw one of
several possible exceptions if an error occurs. If your application
allows users to construct arbitrary qualifiers (such as through
a user interface), you may want to write code to catch any exceptions
and respond to errors (for example, by displaying a panel saying
that the user typed a poorly formed qualifier).

---

### qualifier

`EOQualifier qualifier()`

Returns the receiver's qualifier _._

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
