---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAndQualifier.html
archived_at: '2026-07-18T01:28:33.837625Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOArrayDataSource-2.md)
[!](EOClassDescription-3.md)

---

# EOAndQualifier

__Inherits From:__
EOQualifier : NSObject

__Conforms To:__ EOQualifierEvaluation
EOQualifierSQLGeneration

__Declared in:__ EOControl/EOQualifier.h

EOAndQualifier is a subclass of EOQualifier that contains multiple qualifiers. EOAndQualifier adopts the EOQualifierEvaluation protocol, which defines the method __evaluateWithObject:__ for in-memory evaluation. When an EOAndQualifier object receives an __evaluateWithObject:__ message, it evaluates each of its qualifiers until one of them returns NO. If one of its qualifiers returns NO, the EOAndQualifier object returns NO immediately. If all of its qualifiers return YES, the EOAndQualifier object returnsYES.

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

Returns YES if _anObject_ satisfies the qualifier, NO otherwise. When an EOAndQualifier object receives an [__evaluateWithObject:__](EOQualifierEvaluation-2.md)message, it evaluates each of its qualifiers until one of them returns NO. If any of its qualifiers returns NO, the EOAndQualifier object returns NO immediately. If all of its qualifiers return YES, the object returns YES. This method can raise one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### initWithQualifierArray:

- `initWithQualifierArray:`(NSArray \*)_qualifiers_

Initializes the receiver with the qualifiers _qualifiers_ and returns `self`. This method is the designated initializer for EOAndQualifier.

---

#### initWithQualifiers:

- `initWithQualifiers:`(EOQualifier \*)_qualifiers, ..._

Initializes the receiver with the `nil`-terminated list of qualifiers _qualifiers_. Works by invoking `initWithQualifierArray:`. For example, the following code excerpt constructs two qualifiers, `qual1` and `qual2`. It then uses these qualifiers to initialize an EOAndQualifier, `andQual`. `andQual` is then used to filter an in-memory array.

> ```
> NSArray *guests;    /* Assume this exists. */
>
> EOQualifier *qual1, *qual2, *andQual;
>
> qual1 = [EOQualifier qualifierWithQualifierFormat:@"lastName = 'Nunez'"];
>
> qual2 = [EOQualifier qualifierWithQualifierFormat:@"firstName = 'Maria'"];
>
> andQual = [[EOAndQualifier alloc] initWithQualifiers:qual1, qual2, nil];
>
> return [guests filteredArrayUsingQualifier:andQual];
> ```

---

#### qualifiers

- (NSArray \*)`qualifiers`

Returns the receiver's qualifiers.

---

[!](EOArrayDataSource-2.md)
[!](EOClassDescription-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
