---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOKeyComparisonQlfr.html
archived_at: '2026-07-15T08:11:39.852159Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOKeyComparisonQualifier

> **__Inherits
> from:__**
> : [EOQualifier](EOQualifier-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5ixkylmnftgszls) : NSObject

> **__Conforms to:__**
> : [EOQualifierEvaluation](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgf5cu6ulvmfwgsztjmvzek5tbnr2wc5djn5xa)
> : EOQualifierSQLGeneration

> __Declared in:__ : EOControl/EOQualifier.h

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

EOKeyComparisonQualifier adopts the EOQualifierEvaluation protocol,
which defines the method [evaluateWithObject:](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du) for
in-memory evaluation. When an EOKeyComparisonQualifier object receives an __evaluateWithObject:__ message,
it evaluates the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyComparisonQualifier
can be used to generate SQL. When it's used for this purpose,
the key should be a valid property name of the root entity for the qualifier
(or a valid key path).

## Adopted Protocols

---

> EOQualifierEvaluation: [- evaluateWithObject:](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du)
>
> EOQualifierSQLGeneration
> (EOAccess): __- sqlStringForSQLExpression:__
> : __- schemaBasedQualifierWithRootEntity:__

## Instance Methods

---

### evaluateWithObject:

`- (BOOL)evaluateWithObject:object`

Returns YES if the object _object_ satisfies
the qualifier, NO otherwise. When an EOKeyComparisonQualifier object
receives an evaluateWithObject: message, it evaluates _object_ to determine
if it meets the qualifier criteria. This method can raise one of
several possible exceptions if an error occurs. If your application
allows users to construct arbitrary qualifiers (such as through
a user interface), you may want to write code to catch any exceptions
and properly respond to errors (for example, by displaying a panel
saying that the user typed a poorly formed qualifier).

---

### initWithLeftKey:operatorSelector:rightKey:

`- initWithLeftKey:(NSString
*)leftKey operatorSelector:(SEL)selector
rightKey:(NSString *)rightKey`

Initializes the receiver to compare the
properties named by _leftKey_ and _rightKey_,
using the operator selector _selector_,
one of:

- [EOQualifierOperatorEqual](EOQualifier-3.md#apple-ijbesqsejbbuc)
- [EOQualifierOperatorNotEqual](EOQualifier-3.md#apple-ijbesq2cizbuq)
- [EOQualifierOperatorLessThan](EOQualifier-3.md#apple-ijbesq2firces)
- [EOQualifierOperatorGreaterThan](EOQualifier-3.md#apple-ijbesq2eirbeu)
- [EOQualifierOperatorLessThanOrEqualTo](EOQualifier-3.md#apple-ijbesrcei5cue)
- [EOQualifierOperatorGreaterThanOrEqualTo](EOQualifier-3.md#apple-ijbesrckivduk)
- [EOQualifierOperatorContains](EOQualifier-3.md#apple-ijbesrcgjjdum)
- [EOQualifierOperatorLike](EOQualifier-3.md#apple-ijbesq2divauc)
- [EOQualifierOperatorCaseInsensitiveLike](EOQualifier-3.md#apple-ijbesq2kinbek)

Enterprise
Objects Framework supports SQL generation for these selectors only.

For
example, the following excerpt creates an EOKeyComparisonQualifier
qual that has the left key "lastName", the operator selector
EOQualifierOperatorEqual, and the right key "member.lastName". Once
constructed, the qualifier qual is used to filter an in-memory array.
The code excerpt returns an array of Guest objects whose __lastName__ properties
have the same value as the __lastName__ property
of the guest's sponsoring member (this example is based on the
Rentals sample database).

> ```
> NSArray *guests;    /* Assume this exists. */
> EOQualifier *qual = [[EOKeyComparisonQualifier alloc]
>     initWithLeftKey:@"lastName"
>     operatorSelector:EOQualifierOperatorEqual
>     rightKey:@"member.lastName"];
>
> return [guests filteredArrayUsingQualifier:qual];
> ```

---

### leftKey

`- (NSString *)leftKey`

Returns the receiver's left key_._

---

### rightKey

`- (NSString *)rightKey`

Returns the receiver's right key.

---

### selector

`- (SEL)selector`

Returns the receiver's selector.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
