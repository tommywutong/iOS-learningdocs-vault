---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOQualifier.html
archived_at: '2026-07-15T08:11:37.896539Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOQualifier

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

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
| [EOKeyValueQualifier](EOKeyValueQualifier.md#apple-jnsxsvtbnr2wkulvmfwgsztjmvza) | Compares the named property of an object to a supplied value, for example, "weight > 150". |
| [EOKeyComparisonQualifier](EOKeyComparisonQualifier.md#apple-jnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvza) | Compares the named property of one object with the named property of another, for example "name = wife.name". |
| [EOAndQualifier](EOAndQualifier.md#apple-ifxgiulvmfwgsztjmvza) | Contains multiple qualifiers, which it conjoins. For example, "name = 'Fred' AND age < 20". |
| [EOOrQualifier](EOOrQualifier.md#apple-ivhu64srovqwy2lgnfsxe) | Contains multiple qualifiers, which it disjoins. For example, "name = 'Fred' OR name = 'Ethel'". |
| [EONotQualifier](EONotQualifier.md#apple-ivhu433ukf2wc3djmzuwk4q) | Contains a single qualifier, which it negates. For example, "NOT (name = 'Fred')". |
| EOSQLQualifier | Contains unstructured text that can be transformed into a SQL expression. EOSQLQualifier provides a way to create SQL expressions with any arbitrary SQL. Because EOSQLQualifiers can't be evaluated against objects in memory and because they contain database and SQL-specific content, you should use EOQualifier wherever possible. |

The interface EOQualifierEvaluation defines how qualifiers
are evaluated in memory. To evaluate qualifiers in a database, methods
in EOSQLExpression (EOAccess) and EOEntity (EOAccess) are used to
generate SQL for qualifiers. Note that all of the SQL generation
functionality is contained in the access layer.

For more information on using EOQualifiers, see the sections

- ["Creating a Qualifier"](EOQualifier-2.md#apple-ijbugqsgjfdeq)
- ["Constructing Format Strings"](EOQualifier-2.md#apple-ijbesq2ginfem)
- ["Checking for NULL Values"](EOQualifier-2.md#apple-ijbugrciirbus)
- ["Using Wildcards and the like Operator"](EOQualifier-2.md#apple-ijbesqsjijaue)
- ["Using Selectors in Qualifier Expressions"](EOQualifier-2.md#apple-ijbugrcei5buu)
- ["Using EOQualifier's Subclasses"](EOQualifier-2.md#apple-ijbugqsijbdug)
- ["Creating Subclasses"](EOQualifier-2.md#apple-ijbugrcei5buq)

## Constants

---

EOQualifier defines the following NSSelector constants to
represent the qualifier operators:

|  |  |
| --- | --- |
| QualifierOperatorEqual | QualifierOperatorGreaterThanOrEqualTo |
| QualifierOperatorNotEqual | QualifierOperatorContains |
| QualifierOperatorLessThan | QualifierOperatorLike |
| QualifierOperatorGreaterThan | QualifierOperatorCaseInsensitiveLike |
| QualifierOperatorLessThanOrEqualTo |  |

## Method Types

---

> **Creating a qualifier**
> : [qualifierWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc64lvmfwgsztjmvzfo2lunbixkylmnftgszlsizxxe3lboq) (com.apple.yellow.eocontrol only)
> : [qualifierToMatchAllValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc64lvmfwgsztjmvzfi32nmf2gg2cbnrwfmylmovsxg)
> : [qualifierToMatchAnyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc64lvmfwgsztjmvzfi32nmf2gg2cbnz4vmylmovsq)
> : [qualifierWithBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpof2wc3djmzuwk4sxnf2gqqtjnzsgs3thom)
>
> **In-memory filtering**
> : [filterArrayWithQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc6ztjnr2gk4sbojzgc6kxnf2gqulvmfwgsztjmvza)
> : [filteredArrayWithQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc6ztjnr2gk4tfmraxe4tbpflws5dikf2wc3djmzuwk4q)
> : [evaluateWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpmv3gc3dvmf2gkv3jorue6ytkmvrxi)
>
> **Converting strings and
> operators**
> : [operatorSelectorForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc633qmvzgc5dpojjwk3dfmn2g64sgn5zfg5dsnfxgo)
> : [stringForOperatorSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc643uojuw4z2gn5ze64dfojqxi33sknswyzldorxxe)
>
> **Get EOQualifier operators**
> : [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y)
> : [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som)
>
> **Accessing a qualifiers
> keys**
> : [allQualifierKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpmfwgyulvmfwgsztjmvzewzlzom)
> : [addQualifierKeysToSet:](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpmfsgiulvmfwgsztjmvzewzlzonkg6u3foq5a)
>
> **Accessing a qualifier's
> binding keys**
> : [bindingKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpmjuw4zdjnztuwzlzom)
> : [keyPathForBindingKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpnnsxsudboruem33sijuw4zdjnztuwzlz)
>
> **Validating a qualifier's
> keys**
> : [validateKeysWithRootClassDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpozqwy2lemf2gks3fpfzvo2lunbjg633uinwgc43tirsxgy3snfyhi2lpny)

## Static Methods

---

### allQualifierOperators

`public static NSArray allQualifierOperators()`

Returns an NSArray containing all of the operators
supported by EOQualifier: =, !=, <, <=, >, >=, "like", and
"caseInsensitiveLike".

__See Also:__  [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som)

---

### filterArrayWithQualifier

`public static void filterArrayWithQualifier(
NSMutableArray objects,
EOQualifier aQualifier)`

Filters _objects_ in
place so that it contains only objects matching _aQualifier._

---

### filteredArrayWithQualifier

`public static NSArray filteredArrayWithQualifier(
NSArray objects,
EOQualifier aQualifier)`

Returns a new array that contains only the objects
from _objects_ matching _aQualifier._

---

### operatorSelectorForString

`public static NSSelector operatorSelectorForString(String aString)`

Returns an operator selector based on the string _aString._
This method is used in parsing a qualifier. For example, the following
statement returns the selector QualifierOperatorNotEqual.
> ```
> Selector selector = Qualifier.operatorSelectorForString("!=");
> ```

The
possible values of _aString_ are =,
==, !=, <, >, <=, >=, "like", and "caseInsensitiveLike".

You'd
probably only use this method if you were writing your own qualifier
parser.

__See Also:__  [stringForOperatorSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc643uojuw4z2gn5ze64dfojqxi33sknswyzldorxxe)

---

### qualifierToMatchAllValues

`public static EOQualifier qualifierToMatchAllValues(NSDictionary dictionary)`

Takes a dictionary of search criteria, from
which the method creates EOKeyValueQualifiers (one for each dictionary
entry). The method ANDs these qualifiers together, and returns the
resulting EOAndQualifier.

---

### qualifierToMatchAnyValue

`public static EOQualifier qualifierToMatchAnyValue(NSDictionary dictionary)`

Takes a dictionary of search criteria, from
which the method creates EOKeyValueQualifiers (one for each dictionary
entry). The method ORs these qualifiers together, and returns the
resulting EOOrQualifier.

---

### qualifierWithQualifierFormat

`public static EOQualifier qualifierWithQualifierFormat(
String qualifierFormat,
NSArray arguments)`

(com.apple.yellow.eocontrol only) Parses the
format string _qualifierFormat_ and
the specified arguments, uses them to create an EOQualifier, and
returns the EOQualifier. Conversion specifications (occurrences
of %@) in qualifierFormat are replaced using the value objects in
arguments.

Based on the content of _qualifierFormat,_
this method generates a tree of the basic qualifier types. For example,
the format string "firstName = 'Joe' AND department = 'Facilities'"
generates an EOAndQualifier that contains two "sub" EOKeyValueQualifiers.
The following code excerpt shows a typical way to use the `qualifierWithQualifierFormat` method.
The excerpt constructs an EOFetchSpecification, which includes an
entity name and a qualifier. It then applies the EOFetchSpecification
to the EODisplayGroup's data source and tells the EODisplayGroup
to fetch.

> ```
> EODisplayGroup displayGroup;     /* Assume this exists.*/
> EOQualifier qualifier;
> EOFetchSpecification fetchSpec;
> EODatabaseDataSource dataSource;
>
> dataSource = (EODatabaseDataSource)displayGroup.dataSource();
> qualifier =
>     EOQualifier.qualifierWithQualifierFormat("cardType = 'Visa'", null);
> fetchSpec = new EOFetchSpecification("Member", qualifier, null), null);
>
> dataSource.setFetchSpecification(fetchSpec);
> displayGroup.fetch();
> ```

`qualifierWithQualifierFormat` performs
no verification to ensure that keys referred to by the format string _qualifierFormat_ exist.
It throws an exception if _qualifierFormat_ contains
any syntax errors.

---

### relationalQualifierOperators

`public static NSArray relationalQualifierOperators()`

Returns an NSArray containing all of the relational
operators supported by EOQualifier: =, !=, <, <=, >, and
>=. In other words, returns all of the EOQualifier operators
except for the ones that work exclusively on strings: "like"
and "caseInsensitiveLike".

__See Also:__  [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y)

---

### stringForOperatorSelector

`public static String stringForOperatorSelector(NSSelector aSelector)`

Returns a string representation of the selector _aSelector._
For example, the following statement returns the string "!=":
> ```
> String operator =
>     EOQualifier.stringForOperatorSelector(EOQualifier.QualifierOperatorNotEqual);
> ```

The
possible values for _selector_ are
as follows:

- [QualifierOperatorEqual](#apple-ijbesqsejbbuc)
- [QualifierOperatorNotEqual](#apple-ijbesq2cizbuq)
- [QualifierOperatorLessThan](#apple-ijbesq2firces)
- [QualifierOperatorGreaterThan](#apple-ijbesq2eirbeu)
- [QualifierOperatorLessThanOrEqualTo](#apple-ijbesrcei5cue)
- [QualifierOperatorGreaterThanOrEqualTo](#apple-ijbesrckivduk)
- [QualifierOperatorContains](#apple-ijbesrcgjjdum)
- [QualifierOperatorLike](#apple-ijbesq2divauc)
- [QualifierOperatorCaseInsensitiveLike](#apple-ijbesq2kinbek)

You'd
probably use this method only if you were writing your own parser.

__See
Also:__  [operatorSelectorForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc633qmvzgc5dpojjwk3dfmn2g64sgn5zfg5dsnfxgo)

---

## Instance Methods

---

### addQualifierKeysToSet:

`public void addQualifierKeysToSet(NSMutableSet qualKeys)`

Adds the receiver's qualifier keys to _qualKeys._
The subclasses in the EOControl framework do this by traversing
the tree of qualifiers. Node qualifiers (such as EOAndQualifier)
recursively invoke this method until they reach a leaf qualifier
(such as EOKeyValueQualifier) which adds its key to the set.

Subclasses
of EOQualifier must implement this method.

---

### allQualifierKeys

`public NSSet allQualifierKeys()`

Returns an NSSet of strings, which are the left-hand
sides of all the qualifiers in the receiver. For example, if you
have a qualifier

salary > 10000 AND manager.lastName =
'smith'

`allQualifierKeys` returns
an array containing the strings "salary" and "manager.lastName".

Subclasses
should not override this method, instead they should override [addQualifierKeysToSet:](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpmfsgiulvmfwgsztjmvzewzlzonkg6u3foq5a).

---

### bindingKeys

`NSArray bindingKeys()`

Returns an array of strings which are the names
of the known variables. Multiple occurrences of the same variable
will only appear once in this list.

---

### evaluateWithObject

`(com.apple.client.eocontrol) public boolean evaluateWithObject(EOKeyValueCodingAdditions object)`

`(com.apple.yellow.eocontrol) public boolean evaluateWithObject(Object object)`

Implemented by subclasses to return `YES` if _object_ matches
the criteria specified in the receiver, `NO` otherwise.
The argument, object, should be an enterprise object, a snapshot
dictionary, or something that implements key-value coding.

---

### keyPathForBindingKey

`public String keyPathForBindingKey(String key)`

Returns a string which is the "left-hand-side"
of the variable in the qualifier. e.g. If you have a qualifier "salary
> $amount and manager.lastName = $manager", then calling bindingKeys
would return the array ("amount", "manager"). Calling `keyPathForBindingKey` would
return salary for amount, and manager.lastname for manager.

---

### qualifierWithBindings

`public abstract EOQualifier qualifierWithBindings(
NSDictionary bindings,
boolean requiresAll)`

Returns a new qualifier substituting all variables
with values found in _bindings._ If _requiresAll_ is true, any
variable not found in _bindings_ throws
an exception. If _requiresAll_ is false,
missing variable values cause the qualifier node to be pruned from
the tree.

---

### validateKeysWithRootClassDescription

`(com.apple.client.eocontrol) public abstract void
validateKeysWithRootClassDescription(EOClassDescription classDesc)`

Ensures that the receiver contains keys and
key paths that belong to or originate from _classDesc._
This method raises an exception if an unknown key is found, otherwise
it returns `null` to indicate
that the keys contained by the qualifier are valid.

`(com.apple.yellow.eocontrol) public abstract Throwable validateKeysWithRootClassDescription(EOClassDescription classDesc)`

Ensures that the receiver contains keys and
key paths that belong to or originate from _classDesc._
This method returns an exception if an unknown key is found, otherwise
it returns `null` to indicate
that the keys contained by the qualifier are valid.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
