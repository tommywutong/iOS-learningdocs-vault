---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOKeyValueQualifier.html
archived_at: '2026-07-15T08:11:37.748532Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOKeyValueQualifier

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

EOKeyValueQualifier is a subclass of EOQualifier that compares
a named property of an object with a supplied value, for example,
"salary > 1500". EOKeyValueQualifier implements the EOQualifierEvaluation interface,
which defines the method [evaluateWithObject](EOQualifierEvaluation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi) for
in-memory evaluation. When an EOKeyValueQualifier object receives
an `evaluateWithObject` message, it evaluates the
given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyValueQualifier
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

### EOKeyValueQualifier

`public EOKeyValueQualifier(
String key,
NSSelector selector,
Object value)`

Creates and returns a new EOKeyValueQualifier.

If _key,_ _selector,_
and _value_ are provided, the EOKeyValueQualifier
compares values for _key_ to _value_ using
the operator method _selector._ The
possible values for _selector_ are
as follows:

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
You can generate SQL using the EOSQLExpression static method `sqlStringForKeyValueQualifier`.

For
example, the following excerpt creates an EOKeyValueQualifier `qual` that
has the key "name", the operator method `QualifierOperatorEqual`,
and the value "Smith". Once constructed, the qualifier `qual` is
used to filter an in-memory array.

> ```
> NSArray employees /* Assume this exists */
> EOKeyValueQualifier qual = new EOKeyValueQualifier("name",
>     EOQualifier.QualifierOperatorEqual, "Smith");
> return EOQualifier.filteredArrayWithQualifier(employees, qual);
> ```

---

## Instance Methods

---

### evaluateWithObject

`public boolean evaluateWithObject(Object anObject)`

Returns true if the object _anObject_ satisfies
the qualifier, false otherwise. When an EOKeyValueQualifier object
receives the `evaluateWithObject`message,
it evaluates _anObject_ to determine
if it meets the qualifier criteria. This method can throw one of
several possible exceptions if an error occurs. If your application
allows users to construct arbitrary qualifiers (such as through
a user interface), you may want to write code to catch any exceptions
and properly respond to errors (for example, by displaying a panel
saying that the user typed a poorly formed qualifier).

---

### key

`public String key()`

Returns the receiver's key.

---

### selector

`public NSSelector selector()`

Returns the receiver's selector.

---

### value

`public Object value()`

Returns the receiver's value.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
