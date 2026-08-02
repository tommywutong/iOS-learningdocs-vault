---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOQualifier.html
archived_at: '2026-07-15T08:11:39.970002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOQualifier

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSCopying

> __Declared in:__ : EOControl/EOQualifier.h

---

## Class Description

---

EOQualifier is an abstract class for objects that hold information
used to restrict selections on objects or database rows according
to specified criteria. With the exception of EOSQLQualifier (EOAccess), qualifiers
aren't based on SQL and they don't rely upon an EOModel (EOAccess).
Thus, the same qualifier can be used both to perform in-memory searches
and to fetch from the database.

You never instantiate an instance of EOQualifier. Rather,
you use one of its subclasses-one of the following or your own
custom EOQualifier subclass:

|  |  |
| --- | --- |
| __Subclass__ | __Purpose__ |
| [EOKeyValueQualifier](EOKeyValueQualifier-2.md#apple-jnsxsvtbnr2wkulvmfwgsztjmvza) | Compares the named property of an object to a supplied value, for example, "weight > 150". |
| [EOKeyComparisonQualifier](EOKeyComparisonQualifier-2.md#apple-jnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvza) | Compares the named property of one object with the named property of another, for example "name = wife.name". |
| [EOAndQualifier](EOAndQualifier-2.md#apple-ifxgiulvmfwgsztjmvza) | Contains multiple qualifiers, which it conjoins. For example, "name = 'Fred' AND age < 20". |
| [EOOrQualifier](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOOrQualifier.html#EOOrQualifier) | Contains multiple qualifiers, which it disjoins. For example, "name = 'Fred' OR name = 'Ethel'". |
| [EONotQualifier](EONotQualifier-2.md#apple-ivhu433ukf2wc3djmzuwk4q) | Contains a single qualifier, which it negates. For example, "NOT (name = 'Fred')". |
| EOSQLQualifier | Contains unstructured text that can be transformed into a SQL expression. EOSQLQualifier provides a way to create SQL expressions with any arbitrary SQL. Because EOSQLQualifiers can't be evaluated against objects in memory and because they contain database and SQL-specific content, you should use EOQualifier wherever possible. |

The protocol EOQualifierEvaluation defines how qualifiers
are evaluated in memory. To evaluate qualifiers in a database, methods
in EOSQLExpression (EOAccess) and EOEntity (EOAccess) are used to
generate SQL for qualifiers. Note that all of the SQL generation
functionality is contained in the access layer.

For more information on using EOQualifiers, see the sections

- ["Creating a Qualifier"](EOQualifier-4.md#apple-ijbugqsgjfdeq)
- ["Constructing Format Strings"](EOQualifier-4.md#apple-ijbesq2ginfem)
- ["Checking for NULL Values"](EOQualifier-4.md#apple-ijbugrciirbus)
- ["Using Wildcards and the like Operator"](EOQualifier-4.md#apple-ijbesqsjijaue)
- ["Using Selectors in Qualifier Expressions"](EOQualifier-4.md#apple-ijbugrcei5buu)
- ["Using Different Data Types in Format Strings"](EOQualifier-4.md#apple-ijbesrcgivaum)
- ["Using EOQualifier's Subclasses"](EOQualifier-4.md#apple-ijbugqsijbdug)
- ["Creating Subclasses"](EOQualifier-4.md#apple-ijbugrcei5buq)

## Constants

---

In EOQualifier.h, EOControl defines the
following selector constants to represent the qualifier operators:

|  |  |
| --- | --- |
| EOQualifierOperatorEqual | EOQualifierOperatorGreaterThanOrEqualTo |
| EOQualifierOperatorNotEqual | EOQualifierOperatorContains |
| EOQualifierOperatorLessThan | EOQualifierOperatorLike |
| EOQualifierOperatorGreaterThan | EOQualifierOperatorCaseInsensitiveLike |
| EOQualifierOperatorLessThanOrEqualTo |  |

## Adopted Protocols

---

> NSCopying

## Method Types

---

> **Creating a qualifier**
> : [+ qualifierWithQualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxc5lbnruwm2lfojlws5dikf2wc3djmzuwk4sgn5zg2yluhi)
> : [+ stringForOperatorSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxg5dsnfxgortpojhxazlsmf2g64stmvwgky3un5zdu)
> : [+ qualifierToMatchAllValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxc5lbnruwm2lfojkg6tlborrwqqlmnrlgc3dvmvztu)
> : [+ qualifierToMatchAnyValue:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxc5lbnruwm2lfojkg6tlborrwqqlopflgc3dvmu5a)
> : [- qualifierWithBindings:requiresAllVariables:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3rovqwy2lgnfsxev3joruee2lomruw4z3thjzgk4lvnfzgk42bnrwfmylsnfqwe3dfom5a)
>
> **In-memory filtering**
> : [- evaluateWithObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3fozqwy5lborsvo2lunbhwe2tfmn2du)
>
> **Converting strings and
> operators**
> : [+ operatorSelectorForString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixw64dfojqxi33sknswyzldorxxertpojjxi4tjnzttu)
> : [+ stringForOperatorSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxg5dsnfxgortpojhxazlsmf2g64stmvwgky3un5zdu)
>
> **Get EOQualifier operators**
> : [+ allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixwc3dmkf2wc3djmzuwk4spobsxeylun5zhg)
> : [+ relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt)
>
> **Accessing a qualifiers
> keys**
> : [- allQualifierKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3bnrwfc5lbnruwm2lfojfwk6lt)
> : [- addQualifierKeysToSet:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3bmrsfc5lbnruwm2lfojfwk6ltkrxvgzluhi)
>
> **Accessing a qualifier's
> binding keys**
> : [- bindingKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3cnfxgi2lom5fwk6lt)
> : [- keyPathForBindingKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3lmv4vaylunbdg64scnfxgi2lom5fwk6j2)
>
> **Validating a qualifier's
> keys**
> : [- validateKeysWithRootClassDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3wmfwgszdborsuwzlzonlws5dikjxw65cdnrqxg42emvzwg4tjob2gs33ohi)

## Class Methods

---

### allQualifierOperators

`+ (NSArray *)allQualifierOperators`

Returns an NSArray containing all of the operators
supported by EOQualifier: =, !=, <, <=, >, >=, "like", and
"caseInsensitiveLike".

__See Also:__  [+ relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt)

---

### operatorSelectorForString:

`+ (SEL)operatorSelectorForString:(NSString
*)aString`

Returns an operator selector based on the string _aString_.
This method is used in parsing a qualifier. For example, the following
statement returns the selector __isNotEqualTo:__.
> ```
> selector = [EOQualifier operatorSelectorForString:@"!="];
> ```

The
possible values of _aString_ are =,
==, !=, <, >, <=, >=, "like", and "caseInsensitiveLike".

You'd
probably only use this method if you were writing your own qualifier
parser.

__See Also:__  [+ stringForOperatorSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixxg5dsnfxgortpojhxazlsmf2g64stmvwgky3un5zdu)

---

### qualifierToMatchAllValues:

`+ (EOQualifier *)qualifierToMatchAllValues:(NSDictionary
*)values`

Takes a dictionary of search criteria, from
which the method creates EOKeyValueQualifiers (one for each dictionary
entry). The method ANDs these qualifiers together, and returns the
resulting EOAndQualifier.

---

### qualifierToMatchAnyValue:

`+ (EOQualifier *)qualifierToMatchAnyValue:(NSDictionary
*)values`

Takes a dictionary of search criteria, from
which the method creates EOKeyValueQualifiers (one for each dictionary
entry). The method ORs these qualifiers together, and returns the
resulting EOOrQualifier.

---

### qualifierWithQualifierFormat:

`+ (EOQualifier *)qualifierWithQualifierFormat:(NSString
*)qualifierFormat,
...`

Parses the format string _qualifierFormat_,
uses it to create an EOQualifier, and returns the EOQualifier.

Based
on the content of _qualifierFormat_,
this method generates a tree of the basic qualifier types. For example,
the format string "firstName = 'Joe' AND department = 'Facilities'"
generates an EOAndQualifier that contains two "sub" EOKeyValueQualifiers.
The following code excerpt shows a typical way to use the __qualifierWithQualifierFormat:__ method.
The excerpt constructs an EOFetchSpecification, which includes an
entity name and a qualifier. It then applies the EOFetchSpecification
to the EODisplayGroup's data source and tells the EODisplayGroup
to fetch.

> ```
> EODisplayGroup *displayGroup;     /* Assume this exists.*/
> EOFetchSpecification *fetchSpec;
> EODatabaseDataSource *dataSource;
>
> dataSource = [displayGroup dataSource];
> fetchSpec = [EOFetchSpecification
>     fetchSpecificationWithEntityName:@"Member"
>     qualifier:[EOQualifier qualifierWithQualifierFormat:
>             @"cardType = 'Visa' "]
>     sortOrderings:nil];
> [dataSource setFetchSpecification:fetchSpec];
> [displayGroup fetch];
> ```

__qualifierWithQualifierFormat__ performs
no verification to ensure that keys referred to by the format string _qualifierFormat_ exist.
It raises an NSInvalidArgumentException if _qualifierFormat_ contains
any syntax errors.

---

### qualifierWithQualifierFormat:arguments:

`+ (EOQualifier *)qualifierWithQualifierFormat:(NSString
*)qualifierFormat
arguments:(NSArray *)arguments`

Parses the format string _qualifierFormat_ and
the specified _arguments_, uses them
to create an EOQualifier, and returns the EOQualifier. This method
is equivalent to __qualifierWithQualifierFormat:__ except
that format characters (for example, %@, %d, %f) in _qualifierFormat_ cause
the method to search in the arguments array for values rather than
in a variable argument list. Note that although %d and %f can be
used when constructing qualifiers, they don't work with most other
string formatting methods such as NSString's __stringWithFormat:__.

---

### __qualifierWithQualifierFormat:varargList:__

`+ (EOQualifier *)qualifierWithQualifierFormat:(NSString
*)format
varargList:(va_list)args`

Parses the format string _qualifierFormat_ and
the corresponding arguments in _args_,
uses the arguments to create an EOQualifier, and returns the EOQualifier.
This method is equivalent to __qualifierWithQualifierFormat:__.

---

### relationalQualifierOperators

`+ (NSArray *)relationalQualifierOperators`

Returns an NSArray containing all of the relational
operators supported by EOQualifier: =, !=, <, <=, >, and
>=. In other words, returns all of the EOQualifier operators
except for the ones that work exclusively on strings: "like"
and "caseInsensitiveLike".

__See Also:__  [+ allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixwc3dmkf2wc3djmzuwk4spobsxeylun5zhg)

---

### stringForOperatorSelector:

`+ (NSString *)stringForOperatorSelector:(SEL)aSelector`

Returns a string representation of the selector _aSelector_.
For example, the following statement returns the string "!=":
> ```
> operator = [EOQualifier stringForOperatorSelector:EOQualifierOperatorNotEqual];
> ```

The
possible values for _selector_ are
as follows:

- [EOQualifierOperatorEqual](#apple-ijbesqsejbbuc)
- [EOQualifierOperatorNotEqual](#apple-ijbesq2cizbuq)
- [EOQualifierOperatorLessThan](#apple-ijbesq2firces)
- [EOQualifierOperatorGreaterThan](#apple-ijbesq2eirbeu)
- [EOQualifierOperatorLessThanOrEqualTo](#apple-ijbesrcei5cue)
- [EOQualifierOperatorGreaterThanOrEqualTo](#apple-ijbesrckivduk)
- [EOQualifierOperatorContains](#apple-ijbesrcgjjdum)
- [EOQualifierOperatorLike](#apple-ijbesq2divauc)
- [EOQualifierOperatorCaseInsensitiveLike](#apple-ijbesq2kinbek)

You'd
probably use this method only if you were writing your own parser.

__See
Also:__  [+ operatorSelectorForString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvc5lbnruwm2lfoixw64dfojqxi33sknswyzldorxxertpojjxi4tjnzttu)

---

## Instance Methods

---

### addQualifierKeysToSet:

`- (void)addQualifierKeysToSet:(NSMutableSet
*)qualKeys`

Adds the receiver's qualifier keys to _qualKeys_.
The subclasses in the EOControl framework do this by traversing
the tree of qualifiers. Node qualifiers (such as EOAndQualifier)
recursively invoke this method until they reach a leaf qualifier
(such as EOKeyValueQualifier) which adds its key to the set.

Subclasses
of EOQualifier must implement this method.

---

### allQualifierKeys

`- (NSSet *)allQualifierKeys`

Returns an NSSet of strings, which are the left-hand
sides of all the qualifiers in the receiver. For example, if you
have a qualifier

salary > 10000 AND manager.lastName =
'smith'

__allQualifierKeys__ returns
an array containing the strings "salary" and "manager.lastName".

Subclasses
should not override this method, instead they should override [addQualifierKeysToSet:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3bmrsfc5lbnruwm2lfojfwk6ltkrxvgzluhi).

---

### bindingKeys

`- (NSArray *)bindingKeys`

Returns an array of strings which are the names
of the known variables. Multiple occurrences of the same variable
will only appear once in this list.

---

### evaluateWithObject:

`- (BOOL)evaluateWithObject:(id)object`

Implemented by subclasses to return `YES` if _object_ matches
the criteria specified in the receiver, `NO` otherwise.
The argument, object, should be an enterprise object, a snapshot
dictionary, or something that implements key-value coding.

---

### keyPathForBindingKey:

`- (NSString *)keyPathForBindingKey:(NSString
*)key`

Returns a string which is the "left-hand-side"
of the variable in the qualifier. e.g. If you have a qualifier "salary
> $amount and manager.lastName = $manager", then calling bindingKeys
would return the array ("amount", "manager"). Calling __keyPathForBindingKey__ would
return salary for amount, and manager.lastname for manager.

---

### qualifierWithBindings:requiresAllVariables:

`- (EOQualifier *)qualifierWithBindings:(NSDictionary
*)bindings
requiresAllVariables:(BOOL)requiresAll`

Returns a new qualifier substituting all variables
with values found in _bindings_. If _requiresAll_ is YES, any
variable not found in _bindings_ raises
an EOQualifierVariableSubstitutionException. If _requiresAll_ is NO,
missing variable values cause the qualifier node to be pruned from
the tree.

---

### validateKeysWithRootClassDescription:

`- (NSException *)validateKeysWithRootClassDescription:(EOClassDescription
*)classDesc`

Ensures that the receiver contains keys and
key paths that belong to or originate from _classDesc_.
This method returns an NSInternalInconsistencyException if an unknown
key is found, otherwise it returns `nil` to
indicate that the keys contained by the qualifier are valid.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
