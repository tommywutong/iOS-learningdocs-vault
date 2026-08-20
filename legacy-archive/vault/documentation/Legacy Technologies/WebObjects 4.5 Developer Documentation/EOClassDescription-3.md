---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOClassDescription.html
archived_at: '2026-07-15T08:11:39.169684Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOClassDescription

> **__Inherits
> from:__**
> : NSObject

> __Declared in:__ : EOControl/EOClassDescription.h

---

## Class Description

---

The EOClassDescription class provides a mechanism for extending
classes by giving them access to metadata not available in the run-time
system. This is achieved as follows:

- EOClassDescription provides a bridge between
  enterprise objects and the metadata contained in an external source
  of information, such as an EOModel (EOAccess). It defines a standard
  API for accessing the information in an external source. It also
  manages the registration of EOClassDescription objects in your application.
- The EOEnterpriseObject informal protocol declares several
  EOClassDescription-related methods that define basic enterprise
  objects behavior, such as undo and validation. The Enterprise Objects Framework
  extends NSObject by providing implementations of these methods. An
  enterprise object class can either accept the default implementations or
  it can provide its own implementation by overriding. This is discussed
  in more detail in the section ["Using EOClassDescription"](EOClassDescription-4.md#apple-ijduoq2iifdum).

Enterprise Objects Framework implements a default subclass
of EOClassDescription in EOAccess, EOEntityClassDescription. EOEntityClassDescription
extends the behavior of enterprise objects by deriving information
about them (such as NULL constraints and referential integrity rules)
from an associated EOModel.

For more information on using EOClassDescription, see the
sections

- ["How Does It Work?"](EOClassDescription-4.md#apple-ijduoq2hijcus)
- ["Using EOClassDescription"](EOClassDescription-4.md#apple-ijduoq2iifdum)
- ["EOEntityClassDescription"](EOClassDescription-4.md#apple-ijduoqseizfes)
- ["The EOClassDescription's Delegate"](EOClassDescription-4.md#apple-ijduoq2djbbue)

## Constants

---

In EOClassDescription.h, EOControl defines
the enumeration type `EODeleteRule`.
It's constants are:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EODeleteRuleNullify | When the source object is deleted, any references a destination object has to the source are removed or "nullified." For example, suppose a department has a to-many relationship to multiple employees. When the department is deleted, any back references an employee has to the department are set to nil. |
| EODeleteRuleCascade | When the source object (department) is deleted, any destination objects (employees) are also deleted. |
| EODeleteRuleDeny | If the source object (department) has any destination objects (employees), a delete operation is refused. |
| EODeleteRuleNoAction | When the source object is deleted, its relationship is ignored and no action is taken to propagate the deletion to destination objects.This rule is useful for tuning performance.To perform a deletion, Enterprise Objects Framework fires all the faults of the deleted object and then fires any to-many faults that point back to the deleted object. For example, suppose you have a simple application based on the sample Movies database. Deleting a Movie object has the effect of firing a to-one fault for the Movie's studio relationship, and then firing the to-many movies fault for that studio. In this scenario, it would make sense to set the delete rule `EODeleteRuleNoAction` for Movie's studio relationship. However, you should use this delete rule with great caution since it can result in dangling references in your object graph. |

EOClassDescription.h also defines string
constants for the names of the notifications it posts. For more information,
see the section ["Notifications"](#apple-ijaucrcdivcuo).

## Method Types

---

> **Managing EOClassDescriptions**
> : [+ invalidateClassDescriptionCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3jnz3gc3djmrqxizkdnrqxg42emvzwg4tjob2gs33oinqwg2df)
> : [+ registerClassDescription:forClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3smvtws43umvzeg3dbonzuizltmnzgs4dunfxw4otgn5zeg3dbonztu)
>
> **Getting EOClassDescriptions**
> : [+ classDescriptionForClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3dnrqxg42emvzwg4tjob2gs33oizxxeq3mmfzxgoq)
> : [+ classDescriptionForEntityName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3dnrqxg42emvzwg4tjob2gs33oizxxerlooruxi6komfwwkoq)
>
> **Creating new object instances**
> : [- createInstanceWithEditingContext:globalID:zone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5rxezlborsus3ttorqw4y3fk5uxi2cfmruxi2lom5bw63tumv4hiothnrxweylmjfcdu6tpnzstu)
>
> **Propagating delete**
> : [- propagateDeleteForObject:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5yhe33qmftwc5dfirswyzlumvdg64spmjvgky3uhjswi2lunfxgoq3pnz2gk6duhi)
>
> **Returning information
> from the EOClassDescription**
> : [- entityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sw45djor4u4ylnmu)
> : [- attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxi5dsnfrhk5dfjnsxs4y)
> : [- classDescriptionForDestinationKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5rwyyltoncgk43dojuxa5djn5xem33sirsxg5djnzqxi2lpnzfwk6j2)
> : [- toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg)
> : [- toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6t3omvjgk3dboruw63ttnbuxas3fpfzq)
> : [- inverseForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5uw45tfojzwkrtpojjgk3dboruw63ttnbuxas3fpe5a)
> : [- ownsDestinationObjectsForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5xxo3ttirsxg5djnzqxi2lpnzhwe2tfmn2hgrtpojjgk3dboruw63ttnbuxas3fpe5a)
> : [- deleteRuleForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2)
>
> **Performing validation**
> : [- validateObjectForDelete:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of53gc3djmrqxizkpmjvgky3uizxxerdfnrsxizj2)
> : [- validateObjectForSave:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of53gc3djmrqxizkpmjvgky3uizxxeu3bozstu)
> : [- validateValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of53gc3djmrqxizkwmfwhkzj2mzxxes3fpe5a)
>
> **Providing default characteristics
> for key display**
> : [- defaultFormatterForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgkztbovwhirtpojwwc5dumvzem33sjnsxsoq)
> : [- defaultFormatterForKeyPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgkztbovwhirtpojwwc5dumvzem33sjnsxsudborudu)
> : [- displayNameForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgs43qnrqxsttbnvsum33sjnsxsoq)
>
> **Handling newly inserted
> and newly fetched objects**
> : [- awakeObject:fromFetchInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxoyllmvhwe2tfmn2duztsn5wumzlumnues3sfmruxi2lom5bw63tumv4hioq)
> : [- awakeObject:fromInsertionInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxoyllmvhwe2tfmn2duztsn5wus3ttmvzhi2lpnzew4rlenf2gs3thinxw45dfpb2du)
>
> **Setting the delegate**
> : [+ classDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3dnrqxg42emvwgkz3borsq)
> : [+ setClassDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3tmv2eg3dbonzuizlmmvtwc5dfhi)
>
> **Getting an object's
> description**
> : [- userPresentableDescriptionForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52xgzlskbzgk43fnz2gcytmmvcgk43dojuxa5djn5xem33sj5rguzldoq5a)
>
> **Getting fetch specifications**
> : [- fetchSpecificationNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5tgk5ddnbjxazldnftgsy3boruw63somfwwkzb2)

## Class Methods

---

### classDelegate

`+ (id)classDelegate`

Returns the delegate for the EOClassDescription
class (as opposed to EOClassDescription instances).

__See
Also:__  [+ setClassDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3tmv2eg3dbonzuizlmmvtwc5dfhi)

---

### classDescriptionForClass:

`+ (EOClassDescription *)classDescriptionForClass:(Class)aClass`

Invoked by the default implementations of the [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq) informal
protocol method [classDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xa) to return the EOClassDescription
for _aClass_. It's generally not
safe to use this method directly-for example, individual EOGenericRecord
instances can have different class descriptions. If a class description
for _aClass_ isn't found, this method
posts an [EOClassDescriptionNeededForClassNotification](#apple-ijaucrkcizbes) on
behalf of the receiver's class, allowing an observer to register
a an EOClassDescription.

---

### classDescriptionForEntityName:

`+ (EOClassDescription *)classDescriptionForEntityName:(NSString
*)entityName`

Returns the EOClassDescription registered under _entityName_.

---

### invalidateClassDescriptionCache

`+ (void)invalidateClassDescriptionCache`

Flushes the EOClassDescription cache.
Because the EOModel objects in an application supply and register
EOClassDescriptions on demand, the cache continues to be repopulated
as needed after you invalidate it. (The EOModel class is defined
in EOAccess.)

You'd use this method when a provider
of EOClassDescriptions (such as an EOModel) has newly become available,
or is about to go away. However, you should rarely need to directly
invoke this method unless you're using an external source of information
other than an EOModel.

---

### registerClassDescription:forClass:

`+ (void)registerClassDescription:(EOClassDescription
*)description
forClass:(Class)class`

Registers an EOClassDescription object for _class_ in
the EOClassDescription cache.You
should rarely need to directly invoke this method unless you're
using an external source of information other than an EOModel (EOAccess).

---

### setClassDelegate:

`+ (void)setClassDelegate:(id)delegate`

Sets the delegate for the EOClassDescription
class (as opposed to EOClassDescription instances) to _delegate_,
without retaining it. For more information on the class delegate,
see the [EOClassDescription ClassDelegate](EOClassDescription%20ClassDelegate.md#apple-indeeq2eijcei) informal
protocol specification.

__See Also:__  [+ classDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3dnrqxg42emvwgkz3borsq)

---

## Instance Methods

---

### attributeKeys

`- (NSArray *)attributeKeys`

Overridden by subclasses to return an array
of attribute keys (NSStrings) for objects described by the receiver.
"Attributes" contain immutable data (such as NSNumbers and NSStrings),
as opposed to "relationships" that are references to other enterprise
objects. For example, a class description that describes Movie objects
could return the attribute keys "title," "dateReleased,"
and "rating."

EOClassDescription's implementation of
this method simply returns.

__See Also:__  [- entityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sw45djor4u4ylnmu), [- toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6t3omvjgk3dboruw63ttnbuxas3fpfzq), [- toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg)

---

### awakeObject:fromFetchInEditingContext:

`- (void)awakeObject:(id)object
fromFetchInEditingContext:(EOEditingContext
*)anEditingContext`

Overridden by subclasses to perform standard
post-fetch initialization for _object_ in _anEditingContext._ EOClassDescription's
implementation of this method does nothing.

---

### awakeObject:fromInsertionInEditingContext:

`- (void)awakeObject:(id)object
fromInsertionInEditingContext:(EOEditingContext
*)anEditingContext`

Assigns empty arrays to to-many relationship
properties of newly inserted enterprise objects. Can be overridden
by subclasses to propagate inserts for the newly inserted _object_ in _anEditingContext_.
More specifically, if _object_ has
a relationship (or relationships) that propagates the object's
primary key and if no object yet exists at the destination of that
relationship, subclasses should create the new object at the destination
of the relationship. Use this method to put default values in your
enterprise object.

---

### classDescriptionForDestinationKey:

`- (EOClassDescription *)classDescriptionForDestinationKey:(NSString
*)detailKey`

Overridden by subclasses to return the class
description for objects at the destination of the to-one relationship
identified by _detailKey_. For example,
the statement:
> ```
> [movie classDescriptionForDestinationKey:@"studio"];
> ```

might
return the class description for the Studio class. EOClassDescription's
implementation of this method returns nil.

---

### createInstanceWithEditingContext:globalID:zone:

`- (id)createInstanceWithEditingContext:(EOEditingContext
*)anEditingContext
globalID:(EOGlobalID *)globalID
zone:(NSZone *)zone`

Overridden by subclasses to create an object
of the appropriate class in _anEditingContext_ with _globalID_ and
in _zone_. In typical usage, all three of
the method's arguments are nil. If the object responds to __initWithEditingContext:classDescription:globalID__ subclasses
should invoke that method, otherwise they should invoke __init__. Implementations
of this method should return an autoreleased object. Enterprise
Objects Framework uses this method to create new instances of objects
when fetching existing enterprise objects or inserting new ones
in an interface layer EODisplayGroup. EOClassDescription's implementation
of this method returns nil.

---

### defaultFormatterForKey:

`- (NSFormatter *)defaultFormatterForKey:(NSString
*)key`

Returns the default NSFormatter to use
when parsing values for assignment to _key_. EOClassDescription's
implementation returns nil. The access layer's EOEntityClassDescription's implementation
returns an NSFormatter based on the Objective-C value class specified
for _key_ in the associated model file.
Code that creates a user interface, like a wizard, can use this
method to assign formatters to user interface elements.

---

### defaultFormatterForKeyPath:

`- (NSFormatter *)defaultFormatterForKeyPath:(NSString
*)keyPath`

Similar to __defaultFormatterForKey:__,
except this method traverses _keyPath_ and
returns the formatter for the key at the end of the path (using __defaultFormatterForKey:__).

---

### deleteRuleForRelationshipKey:

`- (EODeleteRule)deleteRuleForRelationshipKey:(NSString
*)relationshipKey`

Overridden by subclasses to return a delete
rule indicating how to treat the destination of the given relationship
when the receiving object is deleted. The delete rule is one of:

- [EODeleteRuleCascade](#apple-ijaucrccirbuo)
- [EODeleteRuleDeny](#apple-ijaucrchivdeo)
- [EODeleteRuleNullify](#apple-ijaucq2ei5bek)
- [EODeleteRuleNoAction](#apple-ijaucrchjjfem)

EOClassDescription's
implementation of this method returns the delete rule EODeleteRuleNullify.
In the common case, the delete rule for an enterprise object is
defined in its EOModel. (The EOModel class is defined in EOAccess.)

__See
Also:__  [- propagateDeleteWithEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5yhe33qmftwc5dfirswyzlumvlws5diivsgs5djnztug33oorsxq5b2) (EOEnterpriseObject)

---

### displayNameForKey:

`- (NSString *)displayNameForKey:(NSString
*)key`

Returns the default string to use in the
user interface when displaying _key_.
By convention, lowercase words are capitalized (for example, "revenue"
becomes "Revenue"), and spaces are inserted into words with
mixed case (for example, "firstName" becomes "First Name").
This method is useful if you're creating a user interface from
only a class description, such as with a wizard or a Direct To Web application.

---

### entityName

`- (NSString *)entityName`

Overridden by subclasses to return a unique
type name for objects of this class. For example, the access layer's
EOEntityClassDescription returns its EOEntity's name. EOClassDescription's
implementation of this method returns nil.

__See
Also:__  [- attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxi5dsnfrhk5dfjnsxs4y), [- toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6t3omvjgk3dboruw63ttnbuxas3fpfzq), [- toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg)

---

### fetchSpecificationNamed:

`- (EOFetchSpecification *)fetchSpecificationNamed:(NSString
*)name`

Overridden by subclasses to
return the fetch specification associated with _name_. For
example, the access layer's EOEntityClassDescription returns the
fetch specification in its EOEntity named name (if any). EOClassDescription's
implementation returns `nil`.

---

### inverseForRelationshipKey:

`- (NSString *)inverseForRelationshipKey:(NSString
*)relationshipKey`

Overridden by subclasses to return the name
of the relationship pointing back at the receiver from the destination
of the relationship specified by _relationshipKey_.
For example, suppose an Employee object has a relationship called
department to a Department object, and Department has a relationship
called employees back to Employee. The statement:
> ```
> [employee inverseForRelationshipKey:@"department"];
> ```

returns
the string "employees".

EOClassDescription's
implementation of this method returns nil.

---

### ownsDestinationObjectsForRelationshipKey:

`- (BOOL)ownsDestinationObjectsForRelationshipKey:(NSString
*)relationshipKey`

Overridden by subclasses to return YES or NO to
indicate whether the objects at the destination of the relationship
specified by _relationshipKey_ should
be deleted if they are removed from the relationship (and not transferred
to the corresponding relationship of another object). For example,
an Invoice object owns its line items. If a LineItem object is removed
from an Invoice it should be deleted since it can't exist outside
of an Invoice. EOClassDescription's implementation of this method
returns NO.In the common case, this
behavior for an enterprise object is defined in its EOModel. (The
EOModel class is defined in EOAccess.)

---

### propagateDeleteForObject:editingContext:

`- (void)propagateDeleteForObject:(id)object
editingContext:(EOEditingContext
*)anEditingContext`

Propagates a delete operation for _object_ in _anEditingContext_,
according to the delete rules specified in the EOModel. This method
is invoked whenever a delete operation needs to be propagated, as indicated
by the delete rule specified for the corresponding EOEntity's
relationship key. (The EOModel and EOEntity classes are defined
in EOAccess.) For more discussion of delete rules, see the [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq) informal
protocol specification.

__See Also:__  [- deleteRuleForRelationshipKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sgk3dforsve5lmmvdg64ssmvwgc5djn5xhg2djobfwk6j2)

---

### toManyRelationshipKeys

`- (NSArray *)toManyRelationshipKeys`

Overridden by subclasses to return the keys
for the to-many relationship properties of the receiver. To-many
relationship properties contain arrays of enterprise objects. EOClassDescription's implementation
of this method returns nil.

__See
Also:__  [- entityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sw45djor4u4ylnmu), [- toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6t3omvjgk3dboruw63ttnbuxas3fpfzq), [- attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxi5dsnfrhk5dfjnsxs4y)

---

### toOneRelationshipKeys

`- (NSArray *)toOneRelationshipKeys`

Overridden by subclasses to return the keys
for the to-one relationship properties of the receiver. To-one relationship
properties are other enterprise objects. EOClassDescription's
implementation of this method returns nil.

__See
Also:__  [- entityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sw45djor4u4ylnmu), [- toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6tlbnz4vezlmmf2gs33oonugs4clmv4xg), [- attributeKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxi5dsnfrhk5dfjnsxs4y)

---

### userPresentableDescriptionForObject:

`- (NSString *)userPresentableDescriptionForObject:(id)anObject`

Returns a short (no longer than 60 characters)
description of _anObject_ based on
its data. This method enumerates _anObject_'s
attributeKeys and returns each attribute's value, separated by
commas and with the default formatter applied for numbers and dates.

---

### validateObjectForDelete:

`- (NSException *)validateObjectForDelete:(id)object`

Overridden by subclasses to determine whether
it's permissible to delete _object_.
Subclasses should return `nil` if
the delete operation should proceed, or return an exception containing
a user-presentable (localized) error message if not. EOClassDescription's
implementation of this method returns `nil`.

---

### validateObjectForSave:

`- (NSException *)validateObjectForSave:(id)object`

Overridden by subclasses to determine whether
the values being saved for _object_ are
acceptable. Subclasses should return `nil` if
the values are acceptable and the save operation should proceed,
or return an exception containing a user-presentable (localized)
error message if not. EOClassDescription's implementation of this
method returns `nil`.

---

### validateValue:forKey:

`- (NSException *)validateValue:(id
*)valueP
forKey:(NSString *)key`

Overridden by subclasses to validate the value
pointed to by _valueP_. Subclasses
should return nil if the value is acceptable, or return an exception
containing a user-presentable (localized) error message if not. Implementations
can replace _valueP_ with a converted
value (for example, an EOAttribute might convert an NSString to
an NSNumber). EOClassDescription's implementation of this method
returns nil.

An enterprise object performs custom attribute
specific validation with a method of the form `validateKey`.
See the [EOValidation](EOValidation-3.md#apple-infemqsfifcui) protocol specification
for more information.

---

## Notifications

---

The following notifications are declared by EOClassDescription
and posted by enterprise objects in your application.

### EOClassDescriptionNeededForClassNotification

`EOCONTROL_EXTERN NSString *EOClassDescriptionNeededForClassNotification`

One of the EOClassDescription-related
methods that Enterprise Objects Framework adds to NSObject to extend
the behavior of enterprise objects is [classDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xa). The first time
an enterprise object receives a __classDescription__ message
(for example, when changes to the object are being saved to the database),
it posts `EOClassDescriptionNeededForClassNotification` to
notify observers that a class description is needed. The observer
then locates the appropriate class description and registers it
in the application. By default, EOModel objects are registered as
observers for this notification and register EOClassDescriptions
on demand.

|  |  |
| --- | --- |
| Notification Object | Enterprise object class |
| userInfo Dictionary | None |

### EOClassDescriptionNeededForEntityNameNotification

`EOCONTROL_EXTERN NSString *EOClassDescriptionNeededForEntityNameNotification`

When [classDescriptionForEntityName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3dnrqxg42emvzwg4tjob2gs33oizxxerlooruxi6komfwwkoq) is
invoked for a previously unregistered entity name, this notification
is broadcast with the requested entity name as the object of the
notification. By default, EOModel objects are registered as observers
for this notification and register EOClassDescriptions on demand.

|  |  |
| --- | --- |
| Notification Object | Entity name (NSString) |
| userInfo Dictionary | None |

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
