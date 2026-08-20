---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOKeyValueQualifier.html
archived_at: '2026-07-15T08:11:39.866327Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOKeyValueQualifier

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

EOKeyValueQualifier is a subclass of EOQualifier that compares
a named property of an object with a supplied value, for example,
"salary > 1500". EOKeyValueQualifier adopts the EOQualifierEvaluation protocol,
which defines the method [evaluateWithObject:](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du) for
in-memory evaluation. When an EOKeyValueQualifier object receives
an __evaluateWithObject:__ message,
it evaluates the given object to determine if it satisfies the qualifier
criteria.

In addition to performing in-memory filtering, EOKeyValueQualifier
can be used to generate SQL. When it's used for this purpose,
the key should be a valid property name of the root entity for the qualifier
(or a valid key path).

## Adopted Protocols

---

> EOQualifierEvaluation: [- evaluateWithObject:](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du)
>
> EOQualifierSQLGeneration: __- sqlStringForSQLExpression:__
> : __- schemaBasedQualifierWithRootEntity:__

## Instance Methods

---

### evaluateWithObject

`- (BOOL)evaluateWithObject:anObject`

Returns YES if the object _anObject_ satisfies
the qualifier, NO otherwise. When an EOKeyValueQualifier object
receives the __evaluateWithObject__message,
it evaluates _anObject_ to determine
if it meets the qualifier criteria. This method can raise one of
several possible exceptions if an error occurs. If your application
allows users to construct arbitrary qualifiers (such as through
a user interface), you may want to write code to catch any exceptions
and properly respond to errors (for example, by displaying a panel
saying that the user typed a poorly formed qualifier).

---

### initWithKey:operatorSelector:value:

`- initWithKey:(NSString
*)key operatorSelector:(SEL)selector
value:(id)value`

Initializes the receiver to compare values
for _key_ to _value_ using
the operator selector _selector_.The possible
values for _selector_ are as follows:

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
example, the following excerpt creates an EOKeyValueQualifier qual
that has the key "name", the operator selector EOQualifierOperatorEqual,
and the value "Smith". Once constructed, the qualifier qual
is used to filter an in-memory array.

> ```
> NSArray *employees;    /* Assume this exists. */
> EOQualifier *qual = [[EOKeyValueQualifier alloc] initWithKey:@"name"
>         operatorSelector:EOQualifierOperatorEqual
>         value:@"Smith"];
> return [employees filteredArrayUsingQualifier:qual];
> ```

---

### key

`- (NSString *)key`

Returns the receiver's key.

---

### selector

`- (SEL)selector`

Returns the receiver's selector.

---

### value

`- (id)value`

Returns the receiver's value.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
