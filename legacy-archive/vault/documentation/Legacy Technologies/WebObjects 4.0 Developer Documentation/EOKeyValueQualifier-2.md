---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOKeyValueQualifier.html
archived_at: '2026-07-18T01:28:36.507075Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOKeyGlobalID-2.md)
[!](EONotQualifier-2.md)

---

# EOKeyValueQualifier

__Inherits From:__
EOQualifier : NSObject

__Conforms To:__ EOQualifierEvaluation
EOQualifierSQLGeneration

__Declared in:__ EOControl/EOQualifier.h

EOKeyValueQualifier is a subclass of EOQualifier that compares a named property of an object with a supplied value, for example, "salary > 1500". EOKeyValueQualifier adopts the EOQualifierEvaluation protocol, which defines the method [__evaluateWithObject:__](EOQualifierEvaluation-2.md)for in-memory evaluation. When an EOKeyValueQualifier object receives an [__evaluateWithObject:__](EOQualifierEvaluation-2.md)message, it evaluates the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyValueQualifier can be used to generate SQL. When it's used for this purpose, the key should be a valid property name of the root entity for the qualifier (or a valid key path).

---

## Adopted Protocols

**EOQualifierEvaluation**

**[- evaluateWithObject:](EOQualifierEvaluation-2.md)**

**EOQualifierSQLGeneration**

**- sqlStringForSQLExpression:

**- schemaBasedQualifierWithRootEntity:****

---

#### evaluateWithObject

@protocol EOQualifierEvaluation

- (BOOL)`evaluateWithObject:`_anObject_

Returns YES if the object _anObject_ satisfies the qualifier, NO otherwise. When an EOKeyValueQualifier object receives the `evaluateWithObject:` message, it evaluates _anObject_ to determine if it meets the qualifier criteria. This method can raise one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### initWithKey:operatorSelector:value:

- `initWithKey:`(NSString \*)_key_ `operatorSelector:`(SEL)_selector_ `value:`(id)_value_

Initializes the receiver to compare values for _key_ to _value_ using the operator selector _selector_.The possible values for _selector_ are as follows:

- [EOQualifierOperatorEqual](EOQualifier-3.md)
- [EOQualifierOperatorNotEqual](EOQualifier-3.md)
- [EOQualifierOperatorLessThan](EOQualifier-3.md)
- [EOQualifierOperatorGreaterThan](EOQualifier-3.md)
- [EOQualifierOperatorLessThanOrEqualTo](EOQualifier-3.md)
- [EOQualifierOperatorGreaterThanOrEqualTo](EOQualifier-3.md)
- [EOQualifierOperatorContains](EOQualifier-3.md)
- [EOQualifierOperatorLike](EOQualifier-3.md)
- [EOQualifierOperatorCaseInsensitiveLike](EOQualifier-3.md)

Enterprise Objects Framework supports SQL generation for these selectors only.

For example, the following excerpt creates an EOKeyValueQualifier `qual` that has the key "name", the operator selector EOQualifierOperatorEqual, and the value "Smith". Once constructed, the qualifier `qual` is used to filter an in-memory array.

> ```
> NSArray *employees;    /* Assume this exists. */
> EOQualifier *qual = [[EOKeyValueQualifier alloc] initWithKey:@"name"
>         operatorSelector:EOQualifierOperatorEqual
>         value:@"Smith"];
> return [employees filteredArrayUsingQualifier:qual];
> ```

---

#### key

- (NSString \*)`key`

Returns the receiver's key.

---

#### selector

- (SEL)`selector`

Returns the receiver's selector.

---

#### value

- (id)`value`

Returns the receiver's value.

---

[!](EOKeyGlobalID-2.md)
[!](EONotQualifier-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
