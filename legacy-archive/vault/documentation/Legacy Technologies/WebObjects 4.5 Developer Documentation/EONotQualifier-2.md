---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EONotQualifier.html
archived_at: '2026-07-15T08:11:39.880028Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EONotQualifier

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

EONotQualifier is a subclass of EOQualifier that contains
a single qualifier. When an EONotQualifier object is evaluated,
it returns the inverse of the result obtained by evaluating the
qualifier it contains.

EONotQualifier adopts the EOQualifierEvaluation protocol,
which defines the method [evaluateWithObject:](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du) for
in-memory evaluation. When an EONotQualifier object receives an __evaluateWithObject:__ message,
it evaluates the given object to determine if it satisfies the qualifier criteria.

You can generate SQL code for an EONotQualifier using the
EOSQLExpression static method __sqlStringForNegatedQualifier__.

## Adopted Protocols

---

> EOQualifierEvaluation: [- evaluateWithObject:](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du)
>
> EOQualifierSQLGeneration: __- sqlStringForSQLExpression:__
> : __- schemaBasedQualifierWithRootEntity:__

## Instance Methods

---

### evaluateWithObject:

`- (BOOL)evaluateWithObject:anObject`

Returns YES if the object _anObject_ satisfies
the EONotQualifier, NO otherwise. This method can raise one of several
possible exceptions if an error occurs. If your application allows
users to construct arbitrary qualifiers (such as through a user
interface), you may want to put exception handlers around this method
to properly respond to errors (for example, by displaying a panel
saying that the user typed a poorly formed qualifier).

---

### initWithQualifier:

`- initWithQualifier:(EOQualifier
*)aQualifier`

Initializes the receiver with the EOQualifier _aQualifier_.
For example, the following code excerpt constructs a qualifier,
baseQual, and uses it to initialize an EONotQualifier, negQual.
The EONotQualifier negQual is then used to filter an in-memory array.
The code excerpt returns an array of Guest objects whose __lastName__ properties
do _not_ have the same value as the __lastName__ property
of the guest's sponsoring member (this example is based on the
Rentals sample database). In other words, the EONotQualifier negQual
inverts the effects of baseQual.
> ```
> NSArray *guests;     /* Assume this exists. */
> EOQualifier *baseQual, *negQual;
>
> baseQual = [EOQualifier qualifierWithQualifierFormat:@"lastName = member.lastName"];
> negQual = [[EONotQualifier alloc] initWithQualifier:baseQual];
> return [guests filteredArrayUsingQualifier:negQual];
> ```

---

### qualifier

`- (EOQualifier *)qualifier`

Returns the receiver's qualifier_._

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
