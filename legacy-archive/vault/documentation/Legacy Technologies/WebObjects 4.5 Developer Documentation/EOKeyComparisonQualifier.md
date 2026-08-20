---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOKeyComparisonQualifier.html
archived_at: '2026-07-15T08:11:37.690824Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOKeyComparisonQualifier

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

EOKeyComparisonQualifier is a subclass of EOQualifier that
compares a named property of an object with a named value of another
object. For example, to return all of the employees whose salaries
are greater than those of their managers, you might use an expression
such as "salary > manager.salary", where "salary" is
the __left key__ and "manager.salary" is the __right
key__. The "left key" is the property of the first object
that's being compared to a property in a second object; the property
in the second object is the "right key." Both the left key and
the right key might be key paths. You can use EOKeyComparisonQualifier
to compare properties of two different objects or to compare two properties
of the same object.

EOKeyComparisonQualifier implements the EOQualifierEvaluation interface,
which defines the method [evaluateWithObject](EOQualifierEvaluation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi) for
in-memory evaluation. When an EOKeyComparisonQualifier object receives
an `evaluateWithObject` message, it evaluates
the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyComparisonQualifier
can be used to generate SQL. When it's used for this purpose,
the key should be a valid property name of the root entity for the qualifier
(or a valid key path).

## Interfaces Implemented

---

> EOQualifierEvaluation: [evaluateWithObject](EOQualifierEvaluation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi)
>
> NSCoding
> (com.apple.client.eocontrol only): `classForCoder`
> : `encodeWithCoder`

## Constructors

---

### EOKeyComparisonQualifier

`public EOKeyComparisonQualifier(
String leftKey,
NSSelector selector,
String rightKey)`

Creates and returns a new EOKeyComparisonQualifier
object that compares the properties named by _leftKey_ and _rightKey,_
using the operator method _selector,_
one of:

- [QualifierOperatorEqual](EOQualifier.md#apple-ijbesqsejbbuc)
- [QualifierOperatorNotEqual](EOQualifier.md#apple-ijbesq2cizbuq)
- [QualifierOperatorLessThan](EOQualifier.md#apple-ijbesq2firces)
- [QualifierOperatorGreaterThan](EOQualifier.md#apple-ijbesq2eirbeu)
- [QualifierOperatorLessThanOrEqualTo](EOQualifier.md#apple-ijbesrcei5cue)
- [QualifierOperatorGreaterThanOrEqualTo](EOQualifier.md#apple-ijbesrckivduk)
- [QualifierOperatorContains](EOQualifier.md#apple-ijbesrcgjjdum)
- [QualifierOperatorLike](EOQualifier.md#apple-ijbesq2divauc)
- [QualifierOperatorCaseInsensitiveLike](EOQualifier.md#apple-ijbesq2kinbek)

Enterprise
Objects Framework supports SQL generation for these methods only.
You can generate SQL using the EOSQLExpression static method `sqlStringForKeyComparisonQualifier`.

For
example, the following excerpt creates an EOKeyComparisonQualifier `qual` that
has the left key "lastName", the operator method EOQualifierOperatorEqual,
and the right key "member.lastName". Once constructed, the qualifier `qual` is
used to filter an in-memory array. The code excerpt returns an array
of Guest objects whose `lastName` properties
have the same value as the `lastName` property
of the guest's sponsoring member (this example is based on the
Rentals sample database).

> ```
> NSArray guests; /* Assume this exists */
> EOKeyComparisonQualifier qual = new EOKeyComparisonQualifier("lastName",
>     EOQualifier.QualifierOperatorEqual,
>     "member.lastName");
>
> return EOQualifier.filteredArrayWithQualifier(guests, qual);
> ```

---

## Instance Methods

---

### evaluateWithObject

`public boolean evaluateWithObject(Object object)`

Returns true if the object _object_ satisfies
the qualifier, false otherwise. When an EOKeyComparisonQualifier
object receives an evaluateWithObject message, it evaluates _object_ to determine
if it meets the qualifier criteria. This method can throw one of
several possible exceptions if an error occurs. If your application
allows users to construct arbitrary qualifiers (such as through
a user interface), you may want to write code to catch any exceptions
and properly respond to errors (for example, by displaying a panel
saying that the user typed a poorly formed qualifier).

---

### leftKey

`public String leftKey()`

Returns the receiver's left key _._

---

### rightKey

`public String rightKey()`

Returns the receiver's right key.

---

### selector

`public NSSelector selector()`

Returns the receiver's selector.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
