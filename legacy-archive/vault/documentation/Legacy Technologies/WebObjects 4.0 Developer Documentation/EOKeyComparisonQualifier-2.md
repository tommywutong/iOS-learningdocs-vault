---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOKeyComparisonQualifier.html
archived_at: '2026-07-18T01:28:36.353885Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOGlobalID-2.md)
[!](EOKeyGlobalID-2.md)

---

# EOKeyComparisonQualifier

__Inherits From:__
EOQualifier : NSObject

__Conforms To:__ EOQualifierEvaluation
EOQualifierSQLGeneration

__Declared in:__ EOControl/EOQualifier.h

EOKeyComparisonQualifier is a subclass of EOQualifier that compares a named property of an object with a named value of another object. For example, to return all of the employees whose salaries are greater than those of their managers, you might use an expression such as "salary > manager.salary", where "salary" is the _left key_ and "manager.salary" is the _right key_. The "left key" is the property of the first object that's being compared to a property in a second object; the property in the second object is the "right key." Both the left key and the right key might be key paths. You can use EOKeyComparisonQualifier to compare properties of two different objects or to compare two properties of the same object.

EOKeyComparisonQualifier adopts the EOQualifierEvaluation protocol, which defines the method [__evaluateWithObject:__](EOQualifierEvaluation-2.md)for in-memory evaluation. When an EOKeyComparisonQualifier object receives an [__evaluateWithObject:__](EOQualifierEvaluation-2.md)message, it evaluates the given object to determine if it satisfies the qualifier criteria.

In addition to performing in-memory filtering, EOKeyComparisonQualifier can be used to generate SQL. When it's used for this purpose, the key should be a valid property name of the root entity for the qualifier (or a valid key path).

---

## Adopted Protocols

**EOQualifierEvaluation**

**[- evaluateWithObject:](EOQualifierEvaluation-2.md)**

**EOQualifierSQLGeneration**

**- sqlStringForSQLExpression:

**- schemaBasedQualifierWithRootEntity:****

---

#### evaluateWithObject:

@protocol EOQualifierEvaluation

- (BOOL)`evaluateWithObject:`_object_

Returns YES if the object _object_ satisfies the qualifier, NO otherwise. When an EOKeyComparisonQualifier object receives an `evaluateWithObject:` message, it evaluates _object_ to determine if it meets the qualifier criteria. This method can raise one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### initWithLeftKey:operatorSelector:rightKey:

- `initWithLeftKey:`(NSString \*)_leftKey_ `operatorSelector:`(SEL)_selector_ `rightKey:`(NSString \*)_rightKey_

Initializes the receiver to compare the properties named by _leftKey_ and _rightKey_, using the operator selector _selector_.

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

For example, the following excerpt creates an EOKeyComparisonQualifier `qual` that has the left key "lastName", the operator selector EOQualifierOperatorEqual, and the right key "member.lastName". Once constructed, the qualifier `qual` is used to filter an in-memory array. The code excerpt returns an array of Guest objects whose __lastName__ properties have the same value as the __lastName__ property of the guest's sponsoring member (this example is based on the Rentals sample database).

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

#### leftKey

- (NSString \*)`leftKey`

Returns the receiver's left key_._

---

#### rightKey

- (NSString \*)`rightKey`

Returns the receiver's right key.

---

#### selector

- (SEL)`selector`

Returns the receiver's selector.

---

[!](EOGlobalID-2.md)
[!](EOKeyGlobalID-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
