---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOAndQualifier.html
archived_at: '2026-07-15T08:11:39.139087Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOAndQualifier

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

EOAndQualifier is a subclass of EOQualifier that contains
multiple qualifiers. EOAndQualifier adopts the EOQualifierEvaluation protocol,
which defines the method [evaluateWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bnzsfc5lbnruwm2lfoixwk5tbnr2wc5dfk5uxi2cpmjvgky3uhi) for
in-memory evaluation. When an EOAndQualifier object receives an __evaluateWithObject:__ message,
it evaluates each of its qualifiers until one of them returns NO.
If one of its qualifiers returns NO, the EOAndQualifier object returns NO immediately.
If all of its qualifiers return YES, the EOAndQualifier object returns YES.

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

`- (BOOL)evaluateWithObject:(id)anObject`

Returns YES if _anObject_ satisfies
the qualifier, NO otherwise. When an EOAndQualifier object receives
an [evaluateWithObject:](EOQualifierEvaluation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4l3fozqwy5lborsvo2lunbhwe2tfmn2du) message,
it evaluates each of its qualifiers until one of them returns NO.
If any of its qualifiers returns NO, the EOAndQualifier object returns NO immediately.
If all of its qualifiers return YES, the object returns YES. This
method can raise one of several possible exceptions if an error
occurs. If your application allows users to construct arbitrary
qualifiers (such as through a user interface), you may want to write
code to catch any exceptions and properly respond to errors (for
example, by displaying a panel saying that the user typed a poorly
formed qualifier).

---

### initWithQualifierArray:

`- initWithQualifierArray:(NSArray
*)qualifiers`

Initializes the receiver with the qualifiers
in _qualifiers_ and returns `self`.
This method is the designated initializer for EOAndQualifier.

---

### initWithQualifiers:

`- initWithQualifiers:(EOQualifier
*)qualifiers, ...`

Initializes the receiver with the nil-terminated
list of qualifiers in _qualifiers_.
Works by invoking initWithQualifierArray:. For example, the following
code excerpt constructs two qualifiers, `qual1` and `qual2`.
It then uses these qualifiers to initialize an EOAndQualifier, `andQual`.
The qualifier `andQual` is
then used to filter an in-memory array.
> ```
> NSArray *guests;    /* Assume this exists. */
> EOQualifier *qual1, *qual2, *andQual;
>
> qual1 = [EOQualifier qualifierWithQualifierFormat:@"lastName = 'Nunez'"];
> qual2 = [EOQualifier qualifierWithQualifierFormat:@"firstName = 'Maria'"];
> andQual = [[EOAndQualifier alloc] initWithQualifiers:qual1, qual2, nil];
> return [guests filteredArrayUsingQualifier:andQual];
> ```

---

### qualifiers

`- (NSArray *)qualifiers`

Returns the receiver's qualifiers.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
