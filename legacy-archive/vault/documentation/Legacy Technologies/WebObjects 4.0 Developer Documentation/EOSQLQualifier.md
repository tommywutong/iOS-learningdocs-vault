---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOSQLQualifier.html
archived_at: '2026-07-18T01:28:10.729118Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOSQLExpression-2.md)
[!](EOStoredProcedure.md)

---

# EOSQLQualifier

__Inherits From:__
EOQualifier : NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

EOSQLQualifier is a subclass of EOQualifier that contains unstructured text that can be transformed into an SQL expression. EOSQLQualifier providesa way to create SQL expressions with any arbitrary SQL. EOSQLQualifier formats are not parsed, they simply perform substitution for keys and format characters. The qualifying information is expressed in the database server's query language (nearly always SQL), and you're responsible for ensuring that the query language statement is valid for your database server. EOSQLQualifiers can't be evaluated against objects in memory. As a result, you should use EOQualifier whenever possible and only use EOSQLQualifier in cases that absolutely require it.

To create an EOSQLQualifer, provide to the constructor a root entity for the qualifier and a format string like that used with the EOQualifier creation method __qualifierWithQualifierFormat__. (You can't use the __qualifierWithQualifierFormat__ method because it doesn't take an entity as an argument and an SQL qualifier must be rooted to an entity.)

---

## Constructors

public `EOSQLQualifier`()

public `EOSQLQualifier`(EOEntity _entity_,java.lang.String _qualifierFormat_)

Creates and returns a newly allocated EOSQLQualifier rooted in _entity_ and built from a format string _qualifierFormat_. _qualifierFormat_ is a `printf()`-style format string like that used with EOQualifier's `qualifierWithQualifierFormat:` method. Returns a new EOSQLQualifier if it can parse _qualifierFormat_ successfully, `null` otherwise.

#

---

### qualifierMigratedFromEntityWithRelationshipPath

public static com.apple.yellow.eocontrol.EOQualifier `qualifierMigratedFromEntityWithRelationshipPath`(com.apple.yellow.eocontrol.EOQualifier _aQualifier_, EOEntity _entity_, java.lang.String _relationshipPath_)

Creates a copy of _aQualifier_, translates all the copy's keys to work with the entity specified in _relationshipPath_, and returns the copy. The receiver's keys are all specified in terms of _entity_. For example, assume that an Employee entity has a relationship named "department" to a Department entity. You could create a qualifier described in terms of the Employee entity (department.name = `Finance', for example) to a qualifier described in terms of the Department entity (name = `Finance'). To do so, send a `qualifierMigratedFromEntityWithRelationshipPath` message with the Employee entity as the entity and "department" as the relationship path.

---

### qualifierWithQualifierFormat

public static com.apple.yellow.eocontrol.EOQualifier `qualifierWithQualifierFormat`(
java.lang.String _format_)

Throws an exception. An EOSQLQualifier must be created with an entity, and this method does not provide one. Use a constructor and provide an entity to create an EOSQLQualifier.

---

## Instance Methods

---

### qualifierWithBindings

public com.apple.yellow.eocontrol.EOQualifier `qualifierWithBindings`(NSDictionary _aDictionary_, boolean _flag_)

Returns a new qualifier created by substituting all EOQualifierVariables with the values contained in _aDictionary_. If _flag_ is true, then the new qualifier requires all its variables. If _flag_ is false, then the new qualifier doesn't require all its variables; and if any variable is not found in _aDictionary_, the node containing that variable is simply pruned from the qualifier tree. Note that `null` and EONull are not the same in this context. If a value in _aDictionary_ is `null`, this method prunes it from the qualifier tree. If a value is EONull, this method assumes that you are looking for an object with a `null` value..

---

### validateKeysWithRootClassDescription

public java.lang.Throwable `validateKeysWithRootClassDescription`(
com.apple.yellow.eocontrol.EOClassDescription _classDesc_)

Validates that a qualifier contains keys and key paths that belong to or originate from _classDesc_. This method returns an NSInternalInconsistencyException if an unknown key is found, otherwise it returns null to indicate that the keys contained by the qualifier are valid.

---

[!](EOSQLExpression-2.md)
[!](EOStoredProcedure.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
