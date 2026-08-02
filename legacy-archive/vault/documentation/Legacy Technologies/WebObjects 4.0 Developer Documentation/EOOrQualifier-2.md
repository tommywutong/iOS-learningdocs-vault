---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOOrQualifier.html
archived_at: '2026-07-18T01:28:37.147855Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOObserverProxy-2.md)
[!](EOQualifier-3.md)

---

# EOOrQualifier

__Inherits From:__
EOQualifier : NSObject

__Conforms To:__ EOQualifierEvaluation
EOQualifierSQLGeneration

__Declared in:__ EOControl/EOQualifier.h

EOOrQualifier is a subclass of EOQualifier that contains multiple qualifiers. EOOrQualifier adopts the EOQualifierEvaluation protocol, which defines the method [__evaluateWithObject:__](EOQualifierEvaluation-2.md)for in-memory evaluation. When an EOOrQualifier object receives an [__evaluateWithObject:__](EOQualifierEvaluation-2.md)message, it evaluates each of its qualifiers until one of them returns YES. If one of its qualifiers returns YES, the EOOrQualifier object returns YES immediately. If all of its qualifiers return NO, the EOOrQualifier object returns NO.

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

- (BOOL)`evaluateWithObject:`(id)_anObject_

Returns YES if _anObject_ satisfies the qualifier, NO otherwise. When an EOOrQualifier object receives an `evaluateWithObject:` message, it evaluates each of its qualifiers until one of them returns YES. If any of its qualifiers returns YES, the EOOrQualifier object returns YES immediately. If all of its qualifiers return NO, the EOOrQualifier object returns NO. This method can raise one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### initWithQualifierArray:

- `initWithQualifierArray:`(NSArray \*)_qualifiers_

Initializes the receiver with the qualifiers _qualifiers_ and returns `self`. This method is the designated initializer for EOOrQualifier.

---

#### initWithQualifiers:

- `initWithQualifiers:`(EOQualifier \*)_qualifiers,..._

Initializes the receiver with the `nil`-terminated list of qualifiers _qualifiers_. Works by invoking `initWithQualifierArray:`. For example, the following code excerpt constructs three qualifiers, `qual1`, `qual2`, and `qual3`. It then uses these qualifiers to initialize an EOOrQualifier, `orQual`. `orQual` is then used to filter an in-memory array.

> ```
> NSArray *guests;    /* Assume this exists. */
> EOQualifier *qual1, *qual2, *qual3, *orQual;
> qual1 = [EOQualifier qualifierWithQualifierFormat:@"lastName = 'Nunez'"];
> qual2 = [EOQualifier qualifierWithQualifierFormat:@"lastName = 'Wren'"];
> qual3 = [EOQualifier qualifierWithQualifierFormat:@"lastName = 'Wilson'"];
> /* Initialize the EOOrQualifier orQual using a nil-terminated list of
>  * qualifiers.
>  */
> orQual = [[EOOrQualifier alloc] initWithQualifiers:qual1, qual2, qual3, nil];
> /* Use orQual to filter the array guests. */
> return [guests filteredArrayUsingQualifier:orQual];
> ```

---

#### qualifiers

- (NSArray \*)`qualifiers`

**Returns the receiver's qualifiers.**

---

[!](EOObserverProxy-2.md)
[!](EOQualifier-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
