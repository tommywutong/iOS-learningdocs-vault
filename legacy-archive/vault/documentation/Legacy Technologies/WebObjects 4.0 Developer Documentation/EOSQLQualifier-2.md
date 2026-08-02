---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOSQLQualifier.html
archived_at: '2026-07-18T01:28:17.516920Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](More%20about%20EOSQLExpression.md)
[!](EOStoredProcedure-2.md)

---

# EOSQLQualifier

__Inherits From:__
EOQualifier : NSObject

__Conforms To:__
EOQualifierSQLGeneration, NSObject (NSObject)

__Declared in:__
EOAccess/EOSQLQualifier.h

---

## Class Description

EOSQLQualifier is a subclass of EOQualifier that contains unstructured text that can be transformed into an SQL expression. EOSQLQualifier is provided for backwards compatibility with pre-2.0 Enterprise Objects Framework releases and to provide a way to create SQL expressions with any arbitrary SQL. EOSQLQualifier formats are not parsed, they simply perform substitution for keys and format characters. The qualifying information is expressed in the database server's query language (nearly always SQL), and you're responsible for ensuring that the query language statement is valid for your database server. EOSQLQualifiers can't be evaluated against objects in memory. As a result, you should use EOQualifier whenever possible and only use EOSQLQualifier in cases that absolutely require it.

You create an SQL qualifier using `alloc...` and [`initWithEntity:qualifierFormat:`](#apple-gm2tana). This method takes as arguments the root entity for the qualifier and a format string like that used with the standard creation method `qualifierWithQualifierFormat:`.

__Note:__
Because an SQL qualifier must be rooted to an entity, you can't use `qualifierWithQualifierFormat:`
to create EOSQLQualifier objects.

---

# Adopted Protocols

**EOQualifierSQLGeneration**

**- schemaBasedQualifierWithRootEntity:

**- sqlStringForSQLExpression:****

---

## Class Methods

---

### qualifierWithQualifierFormat:

+ (EOQualifier \*)`qualifierWithQualifierFormat:`(NSString \*)_format_, ...

Raises an exception. An EOSQLQualifier must be created with an entity, and this method does not provide one. Use `alloc...` and [`initWithEntity:qualifierFormat:`](#apple-gm2tana) to create an EOSQLQualifier.

---

## Instance Methods

---

### initWithEntity:qualifierFormat:

- `initWithEntity:`(EOEntity \*)_entity_ `qualifierFormat:`(NSString \*)_qualifierFormat_, ...

Initializes a newly allocated EOSQLQualifier rooted in _entity_ and built from a format string. _qualifierFormat_ is a `printf()`-style format string like that used with EOQualifier's `qualifierWithQualifierFormat:` method. This is the designated initializer for the EOSQLQualifier class. Returns `self` if _qualifierFormat_ is successfully parsed, `nil` otherwise.

---

[!](More%20about%20EOSQLExpression.md)
[!](EOStoredProcedure-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
