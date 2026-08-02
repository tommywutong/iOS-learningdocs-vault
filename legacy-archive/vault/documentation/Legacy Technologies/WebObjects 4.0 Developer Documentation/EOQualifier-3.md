---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOQualifier.html
archived_at: '2026-07-18T01:28:37.223940Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOOrQualifier-2.md)
[!](EOQualifier-4.md)

---

# EOQualifier

__Inherits From:__
NSObject

__Conforms To:__ NSCopying

__Declared in:__ EOControl/EOQualifier.h

EOQualifier is an abstract class for objects that hold information used to restrict selections on objects or database rows according to specified criteria. With the exception of EOSQLQualifier (EOAccess), qualifiers aren't based on SQL and they don't rely upon an EOModel (EOAccess). Thus, the same qualifier can be used both to perform in-memory searches and to fetch from the database.

You never instantiate an instance of EOQualifier. Rather, you use one of its subclasses-one of the following or your own custom EOQualifier subclass:

| __Subclass__ | __Purpose__ |
| [EOKeyValueQualifier](EOKeyValueQualifier-2.md) | Compares the named property of an object to a supplied value, for example, "weight > 150". |
| [EOKeyComparisonQuali fier](EOKeyComparisonQualifier-2.md) | Compares the named property of one object with the named property of another, for example "name = wife.name". |
| [EOAndQualifier](EOAndQualifier-2.md) | Contains multiple qualifiers, which it conjoins. For example, "name = 'Fred' AND age < 20". |
| [EOOrQualifier](EOOrQualifier-2.md) | Contains multiple qualifiers, which it disjoins. For example, "name = 'Fred' OR name = 'Ethel'". |
| [EONotQualifier](EONotQualifier-2.md) | Contains a single qualifier, which it negates. For example, "NOT (name = 'Fred')". |
| EOSQLQualifier | Contains unstructured text that can be transformed into a SQL expression. EOSQLQualifier provides a way to create SQL expressions with any arbitrary SQL. Because EOSQLQualifiers can't be evaluated against objects in memory and because they contain database and SQL-specific content, you should use EOQualifier wherever possible. EOSQLQualifier is also provided for backward compatibility with pre-2.0 Enterprise Objects Framework releases, which didn't offer a SQL-independent qualifier. |

```
```

The protocol EOQualifierEvaluation defines how qualifiers are evaluated in memory. To evaluate qualifiers in a database, methods in EOSQLExpression (EOAccess) and EOEntity (EOAccess) are used to generate SQL for qualifiers. Note that all of the SQL generation functionality is contained in the access layer.

For more information on using EOQualifiers, see the sections

- [Creating a Qualifier](EOQualifier-4.md)
- [Constructing Format Strings](EOQualifier-4.md)
- [Checking for NULL Values](EOQualifier-4.md)
- [Using Wildcards and the like Operator](EOQualifier-4.md)
- [Using Selectors in Qualifier Expressions](EOQualifier-4.md)
- [Using Different Data Types in Format Strings](EOQualifier-4.md)
- [Using EOQualifier's Subclasses](EOQualifier-4.md)
- [Creating Subclasses](EOQualifier-4.md)

## Constants

The following selector constants are defined to represent the different qualifier operators:

|  |  |
| EOQualifierOperatorEqual | EOQualifierOperatorLessThanOrEqualTo |
| EOQualifierOperatorNotEqual | EOQualifierOperatorGreaterThanOrEqualTo |
| EOQualifierOperatorLessThan | EOQualifierOperatorContains |
| EOQualifierOperatorGreaterThan | EOQualifierOperatorLike |
|  | EOQualifierOperatorCaseInsensitiveLike |

```
```

---

## Adopted Protocols

**NSCopying

**Creating a qualifier****

**+ qualifierWithQualifierFormat:

**+ qualifierWithQualifierFormat:arguments:

**+ qualifierToMatchAllValues:

**+ qualifierToMatchAnyValue:

**- qualifierWithBindings:requiresAllVariables:**********

**Converting strings and operators**

**+ operatorSelectorForString:

**+ stringForOperatorSelector:****

**Get EOQualifier operators**

**+ allQualifierOperators

**+ relationalQualifierOperators****

**Accessing a qualifier's keys**

**- bindingKeys

**- keyPathForBindingKey:****

**Validating a qualifier's keys**

**- validateKeysWithRootClassDescription:**

---

#### allQualifierOperators

+ (NSArray \*)__allQualifierOperators__

Returns an NSArray containing all of the operators supported by EOQualifier: =, !=, <, <=, >, >=, "like", and "caseInsensitiveLike".

__See also:__ + __relationalQualifierOperators__

---

#### operatorSelectorForString:

+ (SEL)__operatorSelectorForString:__ (NSString \*)_aString_

Returns an operator selector based on the string _aString_. This method is used in parsing a qualifier. For example, the following statement returns the selector __isNotEqualTo:__ .

> ```
> selector = [EOQualifier operatorSelectorForString:@"!="];
> ```

The possible values of _aString_ are =, ==, !=, <, >, <=, >=, "like", and "caseInsensitiveLike".

You'd probably only use this method if you were writing your own qualifier parser.

__See also:__ + __stringForOperatorSelector:__

---

#### qualifierToMatchAllValues:

+ (EOQualifier \*)qualifierToMatchAllValues:(NSDictionary \*)_values_;

Takes a dictionary of search criteria, from which the method creates EOKeyValueQualifiers (one for each dictionary entry). The method ANDs these qualifiers together, and returns the resulting EOAndQualifier.

__See also:__

---

#### qualifierToMatchAnyValue:

+ (EOQualifier \*)qualifierToMatchAnyValue:(NSDictionary \*)_values_;

Takes a dictionary of search criteria, from which the method creates EOKeyValueQualifiers (one for each dictionary entry). The method ORs these qualifiers together, and returns the resulting EOOrQualifier.

__See also:__

---

#### qualifierWithQualifierFormat:

+ (EOQualifier \*)__qualifierWithQualifierFormat:__ (NSString \*)_qualifierFormat, ..._

Parses the format string _qualifierFormat_, usesit to create an EOQualifier, and returns the EOQualifier. Based on the content of _qualifierFormat_, this method generates a tree of the basic qualifier types. For example, the format string "firstName = 'Joe' AND department = 'Facilities'" generates an EOAndQualifier that contains two "sub" EOKeyValueQualifiers. The following code excerpt shows a typical way to use the __qualifierWithQualifierFormat:__ method. The excerpt constructs an EOFetchSpecification, which includes an entity name and a qualifier. It then applies the EOFetchSpecification to the EODisplayGroup's data source and tells the EODisplayGroup to fetch.

> ```
> EODisplayGroup *displayGroup;     /* Assume this exists.*/
> EOFetchSpecification *fetchSpec;
> EODatabaseDataSource *dataSource;
>
> dataSource = [displayGroup dataSource];
> fetchSpec = [EOFetchSpecification
>     fetchSpecificationWithEntityName:@"Member"
>     qualifier:[EOQualifier qualifierWithQualifierFormat:
>     @"cardType = 'Visa' "]
>     sortOrderings:nil];
> [dataSource setFetchSpecification:fetchSpec];
> [displayGroup fetch];
> ```

__qualifierWithQualifierFormat__ performs no verification to ensure that keys referred to by the format string _qualifierFormat_ exist. It raises an NSInvalidArgumentException if _qualifierFormat_ contains any syntax errors.

---

#### qualifierWithQualifierFormat:arguments:

+ (EOQualifier \*)__qualifierWithQualifierFormat:__ (NSString \*)_qualifierFormat_
__arguments:__ (NSArray \*)_arguments_

Parses the format string _qualifierFormat_ and the specified _arguments_, uses them to create an EOQualifier, and returns the EOQualifier. This method is equivalent to __qualifierWithQualifierFormat:__ except that format characters (for example, %@, %d, %f) in _qualifierFormat_ cause the method to search in the arguments array for values rather than in a variable argument list. Note that although %d and %f can be used when constructing qualifiers, they don't work with most other string formatting methods such as NSString's stringWithFormat:.

---

#### relationalQualifierOperators

+ (NSArray \*)__relationalQualifierOperators__

Returns an NSArray containing all of the relational operators supported by EOQualifier: =, !=, <, <=, >, and >=. In other words, returns all of the EOQualifier operators except for the ones that work exclusively on strings: "like" and "caseInsensitiveLike".

__See also:__ + __allQualifierOperators__

---

#### stringForOperatorSelector:

+ (NSString \*)__stringForOperatorSelector:__ (SEL)_aSelector_

Returns an NSString representation of the selector _aSelector_. For example, the following statement returns the string "!=":

> ```
> operator = [EOQualifier stringForOperatorSelector:EOQualifierOperatorNotEqual];
> ```

The possible values for _selector_ are as follows:

- EOQualifierOperatorEqual
- EOQualifierOperatorNotEqual
- EOQualifierOperatorLessThan
- EOQualifierOperatorGreaterThan
- EOQualifierOperatorLessThanOrEqualTo
- EOQualifierOperatorGreaterThanOrEqualTo
- EOQualifierOperatorContains
- EOQualifierOperatorLike
- EOQualifierOperatorCaseInsensitiveLike

You'd probably only use this method if you were writing your own parser.

__See also:__ + __operatorSelectorForString:__

---

#### bindingKeys

- (NSArray \*)__bindingKeys__

Returns an array of strings which are the names of the known variables. Multiple occurrences of the same variable will only appear once in this list.

---

#### keyPathForBindingKey:

- (NSString \*)__keyPathForBindingKey:__ (NSString \*)_key_

Returns a string which is the "left-hand-side" of the variable in the qualifier. e.g. If you have a qualifier "salary > $amount and manager.lastName = $manager", then calling bindingKeys would return the array ("amount", "manager"). Calling __keyPathForBindingKey__ would return salary for amount, and manager.lastname for manager.

---

#### qualifierWithBindings:requiresAllVariables:

- (EOQualifier \*)qualifierWithBindings:(NSDictionary \*)_bindings_ requiresAllVariables:(BOOL)_requiresAll_;

Returns a new qualifier substituting all variables with values found in _bindings_. If _requiresAll_ is YES, any variable not found in _bindings_ will cause an EOQualifierVariableSubstitutionException to be raised. If _requiresAll_ is NO, missing variable values will cause the qualifier node to be pruned from the tree.

---

#### validateKeysWithRootClassDescription:

- (NSException \*)__validateKeysWithRootClassDescription:__ (EOClassDescription \*)_classDesc_

Validates that the receiver contains keys and key paths that belong to or originate from _classDesc_. This method returns an NSInternalInconsistencyException if an unknown key is found, otherwise it returns nil to indicate that the keys contained by the qualifier are valid.

---

[!](EOOrQualifier-2.md)
[!](EOQualifier-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
