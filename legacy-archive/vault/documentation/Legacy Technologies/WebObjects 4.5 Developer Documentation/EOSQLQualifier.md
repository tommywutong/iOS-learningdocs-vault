---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOSQLQualifier.html
archived_at: '2026-07-15T08:11:32.013084Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOSQLQualifier

> __Inherits
> from:__  EOQualifier : NSObject

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

EOSQLQualifier is a subclass of EOQualifier that contains
unstructured text that can be transformed into an SQL expression.
EOSQLQualifier provides a way to create SQL expressions with any
arbitrary SQL. EOSQLQualifier formats are not parsed, they simply
perform substitution for keys and format characters. The qualifying
information is expressed in the database server's query language
(nearly always SQL), and you're responsible for ensuring that
the query language statement is valid for your database server.
EOSQLQualifiers can't be evaluated against objects in memory.
As a result, you should use EOQualifier whenever possible and only
use EOSQLQualifier in cases that absolutely require it.

To create an EOSQLQualifier, provide to the constructor a
root entity for the qualifier and a format string like that used
with the EOQualifier creation method __qualifierWithQualifierFormat__.
(You can't use the __qualifierWithQualifierFormat__ method
because it doesn't take an entity as an argument and an SQL qualifier
must be rooted to an entity.)

## Constructors

---

### EOSQLQualifier

`public EOSQLQualifier(
EOEntity entity,
String qualifierFormat)`

Creates and returns a newly allocated EOSQLQualifier
rooted in _entity_ and built from a
format string _qualifierFormat_. _qualifierFormat_ is
a __printf()__-style format string like that
used with EOQualifier's __qualifierWithQualifierFormat__ method.
Returns a new EOSQLQualifier if it can parse _qualifierFormat_ successfully, __null__ otherwise.

---

## Static Methods

---

### qualifierMigratedFromEntity

`public static com.apple.yellow.eocontrol.EOQualifier qualifierMigratedFromEntity(
com.apple.yellow.eocontrol.EOQualifier aQualifier,
EOEntity entity,
String relationshipPath)`

Creates a copy of _aQualifier_,
translates all the copy's keys to work with the entity specified
in _relationshipPath_, and returns
the copy. The receiver's keys are all specified in terms of _entity_.
For example, assume that an Employee entity has a relationship named
"department" to a Department entity. You could create a qualifier
described in terms of the Employee entity (department.name = ‘Finance',
for example) to a qualifier described in terms of the Department
entity (name = ‘Finance'). To do so, send a __qualifierMigratedFromEntity__ message
with the Employee entity as the entity and "department" as the
relationship path.

---

### qualifierWithQualifierFormat

`public static com.apple.yellow.eocontrol.EOQualifier qualifierWithQualifierFormat(String format)`

Throws an exception. An EOSQLQualifier must
be created with an entity, and this method does not provide one.
Use a constructor and provide an entity to create an EOSQLQualifier.

---

## Instance Methods

---

### qualifierWithBindings

`public com.apple.yellow.eocontrol.EOQualifier qualifierWithBindings(
NSDictionary aDictionary,
boolean flag)`

Returns a new qualifier created by substituting
all EOQualifierVariables with the values contained in _aDictionary_.
If _flag_ is true, then the new qualifier
requires all its variables. If _flag_ is
false, then the new qualifier doesn't require all its variables;
and if any variable is not found in _aDictionary_,
the node containing that variable is simply pruned from the qualifier
tree. Note that __null__ and EONull are not
the same in this context. If a value in _aDictionary_ is __null__,
this method prunes it from the qualifier tree. If a value is EONull,
this method assumes that you are looking for an object with a __null__ value.

---

### validateKeysWithRootClassDescription

`public Throwable validateKeysWithRootClassDescription(
com.apple.yellow.eocontrol.EOClassDescription classDesc)`

Validates that a qualifier contains keys and
key paths that belong to or originate from classDesc. This method
returns an `NSInternalInconsistencyException` if
an unknown key is found, otherwise it returns null to indicate that
the keys contained by the qualifier are valid.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
