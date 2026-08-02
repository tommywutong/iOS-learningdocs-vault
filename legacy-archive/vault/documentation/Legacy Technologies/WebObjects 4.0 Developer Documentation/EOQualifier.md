---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOQualifier.html
archived_at: '2026-07-18T01:28:27.188095Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOOrQualifier.md)
[!](EOQualifier-2.md)

---

# EOQualifier

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOQualifier is an abstract class for objects that hold information used to restrict selections on objects or database rows according to specified criteria. With the exception of EOSQLQualifier (EOAccess), qualifiers aren't based on SQL and they don't rely upon an EOModel (EOAccess). Thus, the same qualifier can be used both to perform in-memory searches and to fetch from the database.

You never instantiate an instance of EOQualifier. Rather, you use one of its subclasses-one of the following or your own custom EOQualifier subclass:

| __Subclass__ | __Purpose__ |
| [EOKeyValueQualifier](EOKeyValueQualifier.md) | Compares the named property of an object to a supplied value, for example, "weight > 150". |
| [EOKeyComparisonQualifier](EOKeyComparisonQualifier.md) | Compares the named property of one object with the named property of another, for example "name = wife.name". |
| [EOAndQualifier](EOAndQualifier.md) | Contains multiple qualifiers, which it conjoins. For example, "name = 'Fred' AND age < 20". |
| [EOOrQualifier](EOOrQualifier.md) | Contains multiple qualifiers, which it disjoins. For example, "name = 'Fred' OR name = 'Ethel'". |
| [EONotQualifier](EONotQualifier.md) | Contains a single qualifier, which it negates. For example, "NOT (name = 'Fred')". |
| EOSQLQualifier | Contains unstructured text that can be transformed into a SQL expression. EOSQLQualifier provides a way to create SQL expressions with any arbitrary SQL. Because EOSQLQualifiers can't be evaluated against objects in memory and because they contain database and SQL-specific content, you should use EOQualifier wherever possible. |

```
```

The interface EOQualifierEvaluation defines how qualifiers are evaluated in memory. To evaluate qualifiers in a database, methods in EOSQLExpression (EOAccess) and EOEntity (EOAccess) are used to generate SQL for qualifiers. Note that all of the SQL generation functionality is contained in the access layer.

For more information on using EOQualifiers, see the sections

- [Creating a Qualifier](EOQualifier-2.md)
- [Constructing Format Strings](EOQualifier-2.md)
- [Checking for NULL Values](EOQualifier-2.md)
- [Using Wildcards and the like Operator](EOQualifier-2.md)
- [Using Selectors in Qualifier Expressions](EOQualifier-2.md)
- [Using Different Data Types in Format Strings](EOQualifier-2.md)
- [Using EOQualifier's Subclasses](EOQualifier-2.md)
- [Creating Subclasses](EOQualifier-2.md)

## Constants

The following NSSelector constants are defined to represent the different qualifier operators:

|  |  |
| QualifierOperatorEqual | QualifierOperatorLessThanOrEqualTo |
| QualifierOperatorNotEqual | QualifierOperatorGreaterThanOrEqualTo |
| QualifierOperatorLessThan | QualifierOperatorContains |
| QualifierOperatorGreaterThan | QualifierOperatorLike |
|  | QualifierOperatorCaseInsensitiveLike |

```
```

## Method Types

**Constructors**

**EOQualifier**

**Creating a qualifier**

**+ qualifierWithQualifierFormat (Yellow Box only)

**+ qualifierToMatchAllValues

**+ qualifierToMatchAnyValue

**- qualifierWithBindings********

**In-memory filtering**

**filteredArrayWithQualifier

**filterArrayWithQualifier****

**Converting strings and operators**

**+ operatorSelectorForString

**+ stringForOperatorSelector****

**Get EOQualifier operators**

**+ allQualifierOperators

**+ relationalQualifierOperators****

**Accessing a qualifier's keys**

**- bindingKeys

**- keyPathForBindingKey****

**Validating a qualifier's keys**

**- validateKeysWithRootClassDescription**

## Constructors

---

#### EOQualifier

public __com.apple.yellow.eocontrol.EOQualifier__ (java.lang.String _qualifierFormat_, next.util.ImmutableVector _arguments_)

Creates and returns a new EOQualifier object. Parses the format string _qualifierFormat_ and the specified arguments, initializes the new EOQualifier with them, and returns that EOQualifier. Conversion specifications (occurrences of %@) in _qualifierFormat_ are replaced using the value objects in _arguments_. For more information on how _qualifierFormat_ and _arguments_ are used, see the method description for the static method __qualifierWithQualifierFormat__ .

You would never use this constructor to create an EOQualifier. Instead, you'd use the static method __qualifierWithQualifierFormat__ to create an instance of one of the qualifier subclasses.

A subclass of EOQualifier should write a constructor with the same _formatString_ and _arguments_ arguments that invokes the EOQualifier implementation.

## Static Methods

---

#### allQualifierOperators

public static NSArray __allQualifierOperators__ ()

Returns an NSArray containing all of the operators supported by EOQualifier: =, !=, <, <=, >, >=, "like", and "caseInsensitiveLike".

__See also:__ + __relationalQualifierOperators__

---

#### filterArrayWithQualifier

public static void __filterArrayWithQualifier__ (NSMutableArray _objects_, EOQualifier _aQualifier_)

Filters _objects_ in place so that it contains only objects matching _aQualifier_.

__See also:__ __filteredArrayWithQualifier__

---

#### filteredArrayWithQualifier

public static NSArray __filteredArrayWithQualifier__ (NSArray _objects_, EOQualifier _aQualifier_)

Returns a new array that contains only the objects from _objects_ matching _aQualifier_.

__See also:__ __filterArrayWithQualifier__

---

#### operatorSelectorForString

public static NSSelector __operatorSelectorForString__ (java.lang.String _aString_)

Returns an operator selector based on the string _aString_. This method is used in parsing a qualifier. For example, the following statement returns the selector QualifierOperatorNotEqual.

> ```
> Selector selector = Qualifier.operatorSelectorForString("!=");
> ```

The possible values of _aString_ are =, ==, !=, <, >, <=, >=, "like", and "caseInsensitiveLike".

You'd probably only use this method if you were writing your own qualifier parser.

__See also:__ + __stringForOperatorSelector__

---

#### qualifierToMatchAllValues

public static EOQualifier __qualifierToMatchAllValues__ (NSDictionary _aNSDictionary_)

This method is only available in Yellow Box; there is no equivalent in Java Client. Takes a dictionary of search criteria, from which the method creates EOKeyValueQualifiers (one for each dictionary entry). The method ANDs these qualifiers together, and returns the resulting EOAndQualifier.

__See also:__

---

#### qualifierToMatchAnyValue

public static EOQualifier __qualifierToMatchAnyValue__ (NSDictionary _aNSDictionary_)

This method is only available in Yellow Box; there is no equivalent in Java Client. Takes a dictionary of search criteria, from which the method creates EOKeyValueQualifiers (one for each dictionary entry). The method ORs these qualifiers together, and returns the resulting EOOrQualifier.

__See also:__

---

#### qualifierWithQualifierFormat

public static EOQualifier __qualifierWithQualifierFormat__ (java.lang.String _qualifierFormat_, NSArray _arguments_)

This method is only available in Yellow Box; there is no equivalent in Java Client. Parses the format string _qualifierFormat_ and the specified arguments, uses them to create an EOQualifier, and returns the EOQualifier. Conversion specifications (occurrences of %@) in _qualifierFormat_ are replaced using the value objects in _arguments_.

Based on the content of _qualifierFormat_, this method generates a tree of the basic qualifier types. For example, the format string "firstName = 'Joe' AND department = 'Facilities'" generates an EOAndQualifier that contains two "sub" EOKeyValueQualifiers. The following code excerpt shows a typical way to use the __qualifierWithQualifierFormat__ method. The excerpt constructs an EOFetchSpecification, which includes an entity name and a qualifier. It then applies the EOFetchSpecification to the EODisplayGroup's data source and tells the EODisplayGroup to fetch.

> ```
> EODisplayGroup displayGroup;     /* Assume this exists.*/
> EOQualifier qualifier;
> EOFetchSpecification fetchSpec;
> EODatabaseDataSource dataSource;
>
> dataSource = (EODatabaseDataSource)displayGroup.dataSource();
> qualifier = EOQualifier.qualifierWithQualifierFormat("cardType = 'Visa'");
> fetchSpec = new EOFetchSpecification("Member", qualifier, null), null);
>
> dataSource.setFetchSpecification(fetchSpec);
> displayGroup.fetch();
> ```

__qualifierWithQualifierFormat__ performs no verification to ensure that keys referred to by the format string _qualifierFormat_ exist. It throws an exception if _qualifierFormat_ contains any syntax errors.

---

#### relationalQualifierOperators

public static NSArray __relationalQualifierOperators__ ()

Returns an NSArray containing all of the relational operators supported by EOQualifier: =, !=, <, <=, >, and >=. In other words, returns all of the EOQualifier operators except for the ones that work exclusively on strings: "like" and "caseInsensitiveLike".

__See also:__ + __allQualifierOperators__

---

#### stringForOperatorSelector

public static java.lang.String __stringForOperatorSelector__ (NSSelector _aSelector_)

Returns a string representation of the selector _aSelector_. For example, the following statement returns the string "!=":

> ```
> java.lang.String operator =
>     EOQualifier.stringForOperatorSelector(EOQualifier.QualifierOperatorNotEqual);
> ```

The possible values for _selector_ are as follows:

- QualifierOperatorEqual
- QualifierOperatorNotEqual
- QualifierOperatorLessThan
- QualifierOperatorGreaterThan
- QualifierOperatorLessThanOrEqualTo
- QualifierOperatorGreaterThanOrEqualTo
- QualifierOperatorContains
- QualifierOperatorLike
- QualifierOperatorCaseInsensitiveLike

You'd probably only use this method if you were writing your own parser.

__See also:__ + __operatorSelectorForString__

## Instance Methods

---

#### bindingKeys

NSArray __bindingKeys__ ()

This method is only available in Yellow Box; there is no equivalent in Java Client. Returns an array of strings which are the names of the known variables. Multiple occurrences of the same variable will only appear once in this list.

---

#### keyPathForBindingKey

public java.lang.String __keyPathForBindingKey__ (java.lang.String _key_)

This method is only available in Yellow Box; there is no equivalent in Java Client. Returns a string which is the "left-hand-side" of the variable in the qualifier. e.g. If you have a qualifier "salary > $amount and manager.lastName = $manager", then calling bindingKeys would return the array ("amount", "manager"). Calling __keyPathForBindingKey__ would return salary for amount, and manager.lastname for manager.

---

#### qualifierWithBindings

public abstract EOQualifier __qualifierWithBindings__ (NSDictionary _bindings_, boolean _requiresAll_)

This method is only available in Yellow Box; there is no equivalent in Java Client. Returns a new qualifier substituting all variables with values found in _bindings_. If _requiresAll_ is YES, any variable not found in _bindings_ will throw a QualifierVariableSubstitutionException. If _requiresAll_ is NO, missing variable values will cause the qualifier node to be pruned from the tree.

---

#### validateKeysWithRootClassDescription

public abstract java.lang.Throwable __validateKeysWithRootClassDescription__ (EOClassDescription _classDesc_)

This method is only available in Yellow Box; there is no equivalent in Java Client. Validates that the receiver contains keys and key paths that belong to or originate from _classDesc_. This method returns an exception if an unknown key is found, otherwise it returns `null` to indicate that the keys contained by the qualifier are valid.

---

[!](EOOrQualifier.md)
[!](EOQualifier-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
