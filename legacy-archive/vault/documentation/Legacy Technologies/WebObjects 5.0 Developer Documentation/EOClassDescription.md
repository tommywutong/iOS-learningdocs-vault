---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOClassDescription.html
archived_at: '2026-07-15T08:13:46.145273Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOClassDescription

> __Inherits from:__ Object

> __Implements:__ Serializable

> __Package:__ com.webobjects.eocontrol

---

## Class Description

---

The EOClassDescription class provides a mechanism for extending classes by giving them access to metadata not available in the run-time system. This is achieved as follows:

- EOClassDescription provides a bridge between enterprise objects and the metadata contained in an external source of information, such as an EOModel (EOAccess). It defines a standard API for accessing the information in an external source. It also manages the registration of EOClassDescription objects in your application.
- The EOEnterpriseObject interface declares several EOClassDescription-related methods that define basic enterprise objects behavior, such as undo and validation. The EOCustomObject and EOGenericRecord classes implement the EOEnterpriseObject interface. An enterprise object class can either accept the default implementations by subclassing from EOCustomObject or it can provide its own implementation by overriding. This is discussed in more detail in the section ["EOClassDescription" (page 41)](EOClassDescription.Concepts.md#apple-jzjv6rcfkzpuit2dizhveotpmjvggx3dnrqxg4z2ivhug3dbonzuizltmnzgs4dunfxw4).

Enterprise Objects Framework implements a default subclass of EOClassDescription in EOAccess, EOEntityClassDescription. EOEntityClassDescription extends the behavior of enterprise objects by deriving information about them (such as NULL constraints and referential integrity rules) from an associated EOModel.

For more information on using EOClassDescription, see the sections

- ["How Does It Work?" (page 57)](EOClassDescription.Concepts.md#apple-mvwgk3lfnz2eszbng43dqna)
- ["Using EOClassDescription" (page 58)](EOClassDescription.Concepts.md#apple-mvwgk3lfnz2eszbng43dsma)
- ["EOEntityClassDescription" (page 60)](EOClassDescription.Concepts.md#apple-mvwgk3lfnz2eszbng43dsni)
- ["The EOClassDescription's Delegate" (page 61)](EOClassDescription.Concepts.md#apple-mvwgk3lfnz2eszbng43tama)

## Constants

---

EOClassDescription defines the following `int` constants:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| DeleteRuleNullify | When the source object is deleted, any references a destination object has to the source are removed or "nullified." For example, suppose a department has a to-many relationship to multiple employees. When the department is deleted, any back references an employee has to the department are set to `null`. |
| DeleteRuleCascade | When the source object (department) is deleted, any destination objects (employees) are also deleted. |
| DeleteRuleDeny | If the source object (department) has any destination objects (employees), a delete operation is refused. |
| DeleteRuleNoAction | When the source object is deleted, its relationship is ignored and no action is taken to propagate the deletion to destination objects.This rule is useful for tuning performance.To perform a deletion, Enterprise Objects Framework fires all the faults of the deleted object and then fires any to-many faults that point back to the deleted object. For example, suppose you have a simple application based on the sample Movies database. Deleting a Movie object has the effect of firing a to-one fault for the Movie's studio relationship, and then firing the to-many movies fault for that studio. In this scenario, it would make sense to set the delete rule `DeleteRuleNoAction` for Movie's studio relationship. However, you should use this delete rule with great caution since it can result in dangling references in your object graph. |

EOClassDescription also defines string constants for the names of the notifications it posts. For more information, see the section ["Notifications" (page 54)](#apple-ijaucrcdivcuo).

## Method Types

---

> Managing EOClassDescriptions
> [invalidateClassDescriptionCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpnfxhmylmnfsgc5dfinwgc43tirsxgy3snfyhi2lpnzbwcy3imu)[registerClassDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpojswo2ltorsxeq3mmfzxgrdfonrxe2lqoruw63q)
>
> Getting EOClassDescriptions
> [classDescriptionForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpmnwgc43tirsxgy3snfyhi2lpnzdg64sdnrqxg4y)[classDescriptionForEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpmnwgc43tirsxgy3snfyhi2lpnzdg64sfnz2gs5dzjzqw2zi)
>
> Creating new object instances
> [createInstanceWithEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwg4tfmf2gksloon2gc3tdmvlws5diivsgs5djnztug33oorsxq5a)
>
> Propagating delete
> [propagateDeleteForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxa4tpobqwoylumvcgk3dforsum33sj5rguzldoq)
>
> Returning information from the EOClassDescription
> [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwk3tunf2hsttbnvsq)[attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc5duojuwe5lumvfwk6lt)[classDescriptionForDestinationKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwg3dbonzuizltmnzgs4dunfxw4rtpojcgk43unfxgc5djn5xewzlz)[toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)[toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32pnzsvezlmmf2gs33oonugs4clmv4xg)[inverseForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxws3twmvzhgzkgn5zfezlmmf2gs33oonugs4clmv4q)[ownsDestinationObjectsForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxw653ooncgk43unfxgc5djn5xe6ytkmvrxi42gn5zfezlmmf2gs33oonugs4clmv4q)[deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz)
>
> Performing validation
> [validateObjectForDelete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxmylmnfsgc5dfj5rguzldordg64semvwgk5df)[validateObjectForSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxmylmnfsgc5dfj5rguzldordg64stmf3gk)[validateValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxmylmnfsgc5dfkzqwy5lfizxxes3fpe)
>
> Providing default characteristics for key display
> [defaultFormatterForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwizlgmf2wy5cgn5zg2yluorsxertpojfwk6i)[defaultFormatterForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwizlgmf2wy5cgn5zg2yluorsxertpojfwk6kqmf2gq)[displayNameForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwi2ltobwgc6komfwwkrtpojfwk6i)
>
> Handling newly inserted and newly fetched objects
> [awakeObjectFromFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc53bnnsu6ytkmvrxirtsn5wumzlumnua)[awakeObjectFromInsertion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc53bnnsu6ytkmvrxirtsn5wus3ttmvzhi2lpny)
>
> Setting the delegate
> [classDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpmnwgc43tirswyzlhmf2gk)[setClassDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rponsxiq3mmfzxgrdfnrswoylumu)
>
> Getting an object's description
> [userPresentableDescriptionForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4rtpojhwe2tfmn2a)
>
> Getting fetch specifications
> [fetchSpecificationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwmzlumnufg4dfmnuwm2ldmf2gs33ojzqw2zle)

## Static Methods

---

### classDelegate

`public static Object classDelegate()`

Returns the delegate for the EOClassDescription class (as opposed to EOClassDescription instances).

__See Also:__ [setClassDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rponsxiq3mmfzxgrdfnrswoylumu)

---

### classDescriptionForClass

`public static EOClassDescription classDescriptionForClass(Class aClass)`

Invoked by the default implementations of the EOEnterpriseObject interface method classDescription to return the EOClassDescription for _aClass_. It's generally not safe to use this method directly-for example, individual EOGenericRecord instances can have different class descriptions. If a class description for _aClass_ isn't found, this method posts an [ClassDescriptionNeededForClassNotification](#apple-ijaucrkcizbes) on behalf of the receiver's class, allowing an observer to register a an EOClassDescription.

---

### classDescriptionForEntityName

`public static EOClassDescription classDescriptionForEntityName(String entityName)`

Returns the EOClassDescription registered under _entityName_.

---

### invalidateClassDescriptionCache

`public static void invalidateClassDescriptionCache()`

Flushes the EOClassDescription cache. Because the EOModel objects in an application supply and register EOClassDescriptions on demand, the cache continues to be repopulated as needed after you invalidate it. (The EOModel class is defined in EOAccess.)

You'd use this method when a provider of EOClassDescriptions (such as an EOModel) has newly become available, or is about to go away. However, you should rarely need to directly invoke this method unless you're using an external source of information other than an EOModel.

---

### registerClassDescription

`public static void registerClassDescription( EOClassDescription description, Class class)`

Registers an EOClassDescription object for _class_ in the EOClassDescription cache.You should rarely need to directly invoke this method unless you're using an external source of information other than an EOModel (EOAccess).

---

### setClassDelegate

`public static void setClassDelegate(Object delegate)`

Sets the delegate for the EOClassDescription class (as opposed to EOClassDescription instances) to _delegate_. For more information on the class delegate, see the EOClassDescription.ClassDelegate interface specification.

__See Also:__ [classDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpmnwgc43tirswyzlhmf2gk)

---

## Instance Methods

---

### attributeKeys

`public NSArray attributeKeys()`

Overridden by subclasses to return an array of attribute keys (Strings) for objects described by the receiver. "Attributes" contain immutable data (such as Numbers and Strings), as opposed to "relationships" that are references to other enterprise objects. For example, a class description that describes Movie objects could return the attribute keys "title," "dateReleased," and "rating."

EOClassDescription's implementation of this method simply returns.

__See Also:__ [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwk3tunf2hsttbnvsq), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32pnzsvezlmmf2gs33oonugs4clmv4xg), [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)

---

### awakeObjectFromFetch

`public void awakeObjectFromFetch( EOEnterpriseObject object, EOEditingContext anEditingContext)`

Overridden by subclasses to perform standard post-fetch initialization for _object_ in _anEditingContext._ EOClassDescription's implementation of this method does nothing.

---

### awakeObjectFromInsertion

`public void awakeObjectFromInsertion( EOEnterpriseObject object, EOEditingContext anEditingContext)`

Assigns empty arrays to to-many relationship properties of newly inserted enterprise objects. Can be overridden by subclasses to propagate inserts for the newly inserted _object_ in _anEditingContext_. More specifically, if _object_ has a relationship (or relationships) that propagates the object's primary key and if no object yet exists at the destination of that relationship, subclasses should create the new object at the destination of the relationship. Use this method to put default values in your enterprise object.

---

### classDescriptionForDestinationKey

`public EOClassDescription classDescriptionForDestinationKey(String detailKey)`

Overridden by subclasses to return the class description for objects at the destination of the to-one relationship identified by _detailKey_. For example, the statement:

```
movie.classDescriptionForDestinationKey("studio")
```

might return the class description for the Studio class. EOClassDescription's implementation of this method returns `null`.

---

### clientAttributeKeys

`public NSArray clientAttributeKeys()`

Returns an array containing the names of the attributes that are bound to the client-side class that corresponds to the receiver's entity.

---

### clientToManyRelationshipKeys

`public NSArray clientToManyRelationshipKeys()`

Returns an array containing the names of the to-many relationships that are bound to the client-side class that corresponds to the receiver's entity.

---

### clientToOneRelationshipKeys

`public NSArray clientToOneRelationshipKeys()`

Returns an array containing the names of the to-one relationships that are bound to the client-side class that corresponds to the receiver's entity.

---

### createInstanceWithEditingContext

`public EOEnterpriseObject createInstanceWithEditingContext( EOEditingContext anEditingContext, EOGlobalID globalID)`

Overridden by subclasses to create an object of the appropriate class in _anEditingContext_ with _globalID_. In typical usage, both of the method's arguments are `null`. To create the object, the subclass should pass _anEditingContext_, itself, and _globalID_ to the appropriate constructor. Implementations of this method should return an autoreleased object. Enterprise Objects Framework uses this method to create new instances of objects when fetching existing enterprise objects or inserting new ones in an interface layer EODisplayGroup. EOClassDescription's implementation of this method returns `null`.

---

### defaultFormatterForKey

`public java.text.Format defaultFormatterForKey(String key)`

Returns the default NSFormatter to use when parsing values for assignment to _key_. EOClassDescription's implementation returns `null`. The access layer's EOEntityClassDescription's implementation returns an NSFormatter based on the Java value class specified for _key_ in the associated model file. Code that creates a user interface, like a wizard, can use this method to assign formatters to user interface elements.

---

### defaultFormatterForKeyPath

`public java.text.Format defaultFormatterForKeyPath(String key)`

Similar to __defaultFormatterForKey__, except this method traverses _keyPath_ and returns the formatter for the key at the end of the path (using __defaultFormatterForKey__).

---

### deleteRuleForRelationshipKey

`public int deleteRuleForRelationshipKey(String relationshipKey)`

Overridden by subclasses to return a delete rule indicating how to treat the destination of the given relationship when the receiving object is deleted. The delete rule is one of:

- [DeleteRuleCascade](#apple-ijaucrccirbuo)
- [DeleteRuleDeny](#apple-ijaucrchivdeo)
- [DeleteRuleNullify](#apple-ijaucq2ei5bek)
- [DeleteRuleNoAction](#apple-ijaucrchjjfem)

EOClassDescription's implementation of this method returns the delete rule EODeleteRuleNullify. In the common case, the delete rule for an enterprise object is defined in its EOModel. (The EOModel class is defined in EOAccess.)

__See Also:__ propagateDeleteWithEditingContext (EOEnterpriseObject)

---

### displayNameForKey

`public String displayNameForKey(String key)`

Returns the default string to use in the user interface when displaying _key_. By convention, lowercase words are capitalized (for example, "revenue" becomes "Revenue"), and spaces are inserted into words with mixed case (for example, "firstName" becomes "First Name"). This method is useful if you're creating a user interface from only a class description, such as with a wizard or a Direct To Web application.

---

### entityName

`public String entityName()`

Overridden by subclasses to return a unique type name for objects of this class. For example, the access layer's EOEntityClassDescription returns its EOEntity's name. EOClassDescription's implementation of this method returns `null`.

__See Also:__ [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc5duojuwe5lumvfwk6lt), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32pnzsvezlmmf2gs33oonugs4clmv4xg), [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y)

---

### fetchSpecificationNamed

`public EOFetchSpecification fetchSpecificationNamed(String name)`

Overridden by subclasses to return the fetch specification associated with _name_. For example, the access layer's EOEntityClassDescription returns the fetch specification in its EOEntity named name (if any). EOClassDescription's implementation returns `nil`.

---

### __finalize__

`public void finalize() throws Throwable`

Description forthcoming.

---

### inverseForRelationshipKey

`public String inverseForRelationshipKey(String relationshipKey)`

Overridden by subclasses to return the name of the relationship pointing back at the receiver from the destination of the relationship specified by _relationshipKey_. For example, suppose an Employee object has a relationship called department to a Department object, and Department has a relationship called employees back to Employee. The statement:

```
employee.inverseForRelationshipKey("department");
```

returns the string "employees".

EOClassDescription's implementation of this method returns `null`.

---

### ownsDestinationObjectsForRelationshipKey

`public boolean ownsDestinationObjectsForRelationshipKey(String relationshipKey)`

Overridden by subclasses to return `true` or `false` to indicate whether the objects at the destination of the relationship specified by _relationshipKey_ should be deleted if they are removed from the relationship (and not transferred to the corresponding relationship of another object). For example, an Invoice object owns its line items. If a LineItem object is removed from an Invoice it should be deleted since it can't exist outside of an Invoice. EOClassDescription's implementation of this method returns `false`.In the common case, this behavior for an enterprise object is defined in its EOModel. (The EOModel class is defined in EOAccess.)

---

### propagateDeleteForObject

`public void propagateDeleteForObject( EOEnterpriseObject object, EOEditingContext anEditingContext)`

Propagates a delete operation for _object_ in _anEditingContext_, according to the delete rules specified in the EOModel. This method is invoked whenever a delete operation needs to be propagated, as indicated by the delete rule specified for the corresponding EOEntity's relationship key. (The EOModel and EOEntity classes are defined in EOAccess.) For more discussion of delete rules, see the EOEnterpriseObject interface specification.

__See Also:__ [deleteRuleForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwizlmmv2gkutvnrsum33skjswyylunfxw443infyewzlz)

---

### superClassDescription

`public EOClassDescription superClassDescription()`

Description forthcoming.

---

### toManyRelationshipKeys

`public NSArray toManyRelationshipKeys()`

Overridden by subclasses to return the keys for the to-many relationship properties of the receiver. To-many relationship properties contain arrays of enterprise objects. EOClassDescription's implementation of this method returns `null`.

__See Also:__ [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwk3tunf2hsttbnvsq), [toOneRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32pnzsvezlmmf2gs33oonugs4clmv4xg), [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc5duojuwe5lumvfwk6lt)

---

### toOneRelationshipKeys

`public NSArray toOneRelationshipKeys()`

Overridden by subclasses to return the keys for the to-one relationship properties of the receiver. To-one relationship properties are other enterprise objects. EOClassDescription's implementation of this method returns `null`.

__See Also:__ [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwk3tunf2hsttbnvsq), [toManyRelationshipKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32nmfxhsutfnrqxi2lpnzzwq2lqjnsxs4y), [attributeKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc5duojuwe5lumvfwk6lt)

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

### userPresentableDescriptionForObject

`public String userPresentableDescriptionForObject(EOEnterpriseObject anObject)`

Returns a short (no longer than 60 characters) description of _anObject_ based on its data. This method enumerates _anObject_'s attributeKeys and returns each attribute's value, separated by commas and with the default formatter applied for numbers and dates.

---

### validateObjectForDelete

`public void validateObjectForDelete(EOEnterpriseObject object) throws NSValidation.ValidationException`

Overridden by subclasses to determine whether it's permissible to delete _object_. Subclasses should complete normally if the delete operation should proceed, or throw an exception containing a user-presentable (localized) error message if not. EOClassDescription's implementation of this method completes normally.

---

### validateObjectForSave

`public void validateObjectForSave(EOEnterpriseObject object) throws NSValidation.ValidationException`

Overridden by subclasses to determine whether the values being saved for _object_ are acceptable. Subclasses should complete normally if the values are acceptable and the save operation should proceed, or throw exception containing a user-presentable (localized) error message if not. EOClassDescription's implementation of this method completes normally.

---

### validateValueForKey

`public Object validateValueForKey( Object value, String key) throws NSValidation.ValidationException`

Overridden by subclasses to validate _value_. Subclasses should return `null` if the value is acceptable, or throw an exception containing a user-presentable (localized) error message if not. Implementations can replace _value_ by returning a new value. EOClassDescription's implementation of this method returns `null`.

An enterprise object performs custom attribute specific validation with a method of the form `validateKey`. See the EOValidation interface specification for more information.

---

## Notifications

---

The following notifications are declared by EOClassDescription and posted by enterprise objects in your application.

### ClassDescriptionNeededForClassNotification

`public static final String ClassDescriptionNeededForClassNotification`

One of the EOClassDescription-related methods in the EOEnterpriseObject interface to extend the behavior of enterprise objects is classDescription. The first time an enterprise object receives a __classDescription__ message (for example, when changes to the object are being saved to the database), it posts `ClassDescriptionNeededForClassNotification` to notify observers that a class description is needed. The observer then locates the appropriate class description and registers it in the application. By default, EOModel objects are registered as observers for this notification and register EOClassDescriptions on demand.

|  |  |
| --- | --- |
| Notification Object | Enterprise object class |
| userInfo Dictionary | None |

### ClassDescriptionNeededForEntityNameNotification

`public static final String ClassDescriptionNeededForEntityNameNotification`

When [classDescriptionForEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpmnwgc43tirsxgy3snfyhi2lpnzdg64sfnz2gs5dzjzqw2zi) is invoked for a previously unregistered entity name, this notification is broadcast with the requested entity name as the object of the notification. By default, EOModel objects are registered as observers for this notification and register EOClassDescriptions on demand.

|  |  |
| --- | --- |
| Notification Object | Entity name (String) |
| userInfo Dictionary | None |

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
