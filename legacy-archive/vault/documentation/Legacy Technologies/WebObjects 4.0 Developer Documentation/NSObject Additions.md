---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/NSObjectAdditions.html
archived_at: '2026-07-18T01:28:40.533780Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](NSException%20Additions.md)
[!](EOClassDescriptionClassDelegate.md)

---

# NSObject Additions

__Inherits From:__
none _(NSObject is a root class)_

__Declared in:__ EOControl/EOClassDescription.h
EOControl/EOEditingContext.h
EOControl/EOKeyValueCoding.h
EOControl/EOObserver.h

---

### Class At a Glance:

**---

#### Purpose**

Defines basic functionality for all enterprise objects. Create a subclass when you need a custom enterprise object class to perform business logic; otherwise use EOGenericRecords.

**---

#### Principal Attributes**

- EOClassDescription
- EOEditingContext

  **---

  #### Creation

  | - init | Designated initializer. |
  | - initWithEditingContext:classDescription:globalID: | Optional initializer. |
  | - awakeFromFetchInEditingContext: | Performs additional initialization after the object is fetched. |
  | - awakeFromInsertionInEditingContext: | Performs additional initialization after the object is created in memory. |

```
```

  **---

  #### Commonly Used Methods

  | - willChange | Notifies observers of a change in state. |
  | - editingContext | Returns the receiver's EOEditingContext. |
  | - addObject:toBothSidesOfRelationshipWithKey: | Adds an object to a relationship property and the receiver to the reciprocal relationship. |
  | - removeObject:fromBothSidesOfRelationshipWithKey: | Removes an object from a relationship property and the receiver from the reciprocal relationship. |

```
```

  **---

  #### Methods to Implement or Override******

  The following methods are invoked by the Framework.

  | - set_Key_: | Sets the value for the property named _key_. |
  | - _key_ | Retrieves the value for the property named _key_. |
  | - addTo_Key_: | Adds an object to a relationship property named _key_. |
  | - removeFrom_Key_: | Removes an object from the property named _key_. |
  | - handleTakeValue:forUnboundKey: | Handles a failure of __takeValue:forKey:__ to find a property. |
  | - handleQueryWithUnboundKey: | Handles a failure of __valueForKey:__ to find a property. |
  | - unableToSetNilForKey: | Handles an attempt to set a non-object property's value to __nil__ . |
  | - validate_Key_: | Validates a value for the property named _key_. |
  | - validateForDelete | Validates all properties before deleting the receiver. |
  | - validateForInsert | Validates all properties before inserting the receiver. |
  | - validateForSave | Validates all properties before saving the receiver. |
  | - validateForUpdate | Validates all properties before updating the receiver. |

```
```

  Enterprise Objects Framework adds a number of methods to NSObject for supporting operations common to all enterprise objects. Among these are methods for initializing instances, announcing changes, setting and retrieving property values, and performing validation of state. Some of these methods are for enterprise objects to implement or override, and some are meant to be used as defined by the Framework. Many methods are used internally by the Framework and rarely invoked by application code. The implementation or use of each method is highlighted in the following sections, which describe the major functional groups.

  ---

  ### Initialization Methods

  Enterprise objects are initialized using the __initWithEditingContext:classDescription:globalID:__ , which by default simply invokes __init__ . You can place your custom initialization code in __init__ , or you can override __initWithEditingContext:classDescription:globalID:__ to take advantage of the extra information available with this method.

  After initialization, an enterprise object receives an __awake...__ message. The particular message depends on whether the object has been fetched from a database or created anew in the application. In the former case, it receives an __awakeFromFetchInEditingContext:__ message. In the latter, it receives an __awakeFromInsertionInEditingContext:__ message. The receiver can override either method to perform extra initialization-such as setting default values-based on how it was created.

  ---

  ### Announcing Changes

  For the Framework to keep all areas of an application synchronized, enterprise objects must notify their observers when their state changes. Objects do this by simply invoking __willChange__ before altering any instance variable or other kind of state. This method informs all observers that the invoker is about to change. See the EOObserverCenter class specification for more information on change notification.

  The primary observer of changes in an object is its EOEditingContext. EOEditingContext is a subclass of EOObjectStore that manages collections of objects in memory, tracking inserts, deletes, and updates, and propagating changes to the persistent store as needed. You can get the EOEditingContext that contains an object by sending the object an __editingContext__ message.

  ---

  ### Getting Object and Class Metadata

  One of the larger groups of methods added to NSObject provides information about an object's properties. Most of these methods consult an EOClassDescription to provide their answers. The __classDescription__ method return an object's EOClassDescription. See that class specification for the methods it implements. Methods you can send directly to any object include __entityName__ , which provides the name of the entity mapped to the receiver's class; __allPropertyKeys__ , which returns the names of all the receiver's class properties, attributes and relationships alike; and __attributeKeys__ , which returns just the names of the attributes.

  Some methods return information about relationships. __toOneRelationshipKeys__ and __toManyRelationshipKeys__ return the names of the receiver's relationships, while __isToManyKey:__ tells which kind a particular relationship is. __deleteRuleForRelationshipKey:__ indicates what should happen to the receiver's relationships when it's deleted. Similarly, __ownsDestinationObjectsForRelationshipKey:__ indicates what should happen when another object is added to or removed from the receiver's relationship. Another method, __classDescriptionForDestinationKey:__ , returns the EOClassDescription for the objects at the destination of a relationship.

  These methods are all properly implemented in terms of the receiver's EOClassDescription, so unless your object class doesn't have an EOClassDescription, there's little need to override them. One method you might override in your enterprise object class, however, is __inverseForRelationshipKey:__ . Given the name of one of the receiver's relationships, this method finds the destination object's class data and determines the name of the relationship that points back at the receiver. The default implementation of this method looks for a relationship predicated on the same attributes in both the source and destination, which works correctly in most cases. If, however, you define a reciprocal pair of relationships on different attributes, you should override this method to take that into account. See the method description for an example.

  ---

  ### Key-Value Coding Methods

  A special set of methods form the Framework's main data transport mechanism, in which the properties of an enterprise object are accessed indirectly by name (or key), rather than directly through invocation of an accessor method or as instance variables. Thus, any object's state can be accessed in a consistent manner.

  The basic methods for accessing an enterprise object's values are __takeValue:forKey:__ and __valueForKey:__ . These two methods are defined by NSObject to use the accessor methods normally implemented by objects (or to access instance variables directly if need be), so that you don't have to write special code simply to integrate your enterprise objects into the Framework. Another pair of methods, __takeValuesFromDictionary:__ and __valuesForKeys:__ , gives access to groups of properties. Lastly, __valueForKeyPath:__ and __valueForKeyPath:__ give access to properties across key paths of the form _relationship.property_; for example, "department.name".

  All of the `takeValue...` methods have corresponding `takeStoredValue...` methods for setting object values from object store values: __takeStoredValue:forKey:__ , __takeStoredValue:forKeyPath:__ , and __takeStoredValuesFromDictionary:__ . To enable them, override __useStoredAccessor__ to return YES. This is discussed in more detail below.

  ---

  #### Default Implementations; Handling Access Errors

  The Framework provides default implementations of __takeValue:forKey:__ and __valueForKey:__ that work for all objects. The other four access methods are implemented in terms of these two. These implementations are general enough that your enterprise object classes should rarely need to override either key-value coding method. In accessing an object's property, the default NSObject implementations of the key-value coding methods use the class definition as follows:

  - The key-value coding method looks for an accessor method based on the key. For example, with a key of "lastName", __takeValue:forKey:__ looks for a method named __setLastName:__ (note that the first letter of the property name is made uppercase), and __valueForKey:__ looks for a method of the form __lastName__ .
  - If the key-value coding method doesn't find an accessor method, and the class responds YES to an __accessInstanceVariablesDirectly__ message (which it does by default), it looks for an instance variable whose name is the same as the key and sets or retrieves its value directly. In setting an instance variable that's an object, __takeValue:forKey:__ retains the new value and autoreleases the old one.
  - If neither an accessor method nor an instance variable can be found, the default implementations invoke methods that your custom objects can override to handle failures. __handleTakeValue:forUnboundKey:__ is invoked from __takeValue:forKey:__ , and __handleQueryWithUnboundKey:__ is invoked from __valueForKey:__ . Normally these methods raise an exception, but you can implement them to set or get a value in whatever way is needed.The Framework also provides methods for setting object values from object store values: __takeStoredValue:forKey:__ , __takeStoredValue:forKeyPath:__ , and __takeStoredValuesFromDictionary:__ . You cause these methods to be used instead of their `takeValue...` counterparts by overriding __useStoredAccessor__ to return YES. When you override __useStoredAccessor__ to return YES, the `takeStoredValue...` methods are used whenever an object moves from one object store to another-for example, when you instantiate objects from database data, or when you transfer objects between EOEditingContexts. In all other cases the regular `takeValue...` methods are used, such as when a user modifies an object by providing a new value for it in a user interface. To think of it another way, the `takeStoredValue...` methods let you bypass the logic in your `set...` methods, whereas the `takeValue...` methods execute that logic.

  The `takeStoredValue...` methods are especially useful in cases where an object has instance variables whose values are interdependent. For example, suppose you have a Product object with `status` and `dateOfSale` attributes. When the Product's `status` changes to "sold," you'd also want to set its `dateOfSale` value-in all likelihood, by invoking `setDateOfSale:` from the object's `setStatus:` method. If you were using __takeValue:forKey:__ , initializing a Product object from database data would have the effect of invoking the object's `setStatus:` method, which in turn would attempt to change the object's `dateOfSale` date. You can prevent this from happening from using the `takeStoredValue...` methods.

  When you override __useStoredAccessor__ to return YES and you're changing the value of an object's property, the default NSObject implementations of the key-value coding methods use the class definition as follows:

  - The key-value coding method looks for an instance variable whose name is the same as the key, but preceded by an underbar. It then sets the instance variable's value directly. For example, with a key of "lastName", __takeStoredValue:forKey:__ looks for an instance variable called `_lastName`.
  - If the key-value coding method doesn't find an instance variable, it looks for an accessor method based on key, preceded by an underbar. For example, with a key of "lastName", __takeStoredValue:forKey:__ looks for a method called `_setLastName.`
  - If the key-value coding method doesn't find an underbar-preceded instance variable or accessor method, it looks for an instance variable whose name is the same as the key (`lastName`) and sets its value directly.
  - Finally, the key-value coding method looks for an accessor method based on the key. For the key "lastName", this would be `setLastName:`.
  - If none of the above instance variables or accessor methods can be found, the default implementations invoke methods that your custom objects can override to handle failures. __handleTakeValue:forUnboundKey:__ is invoked from __takeValue:forKey:__ , and __handleQueryWithUnboundKey:__ is invoked from __valueForKey:__ . Normally these methods raise an exception, but you can implement them to set or get a value in whatever way is needed.The key-value coding methods cache attribute bindings for both accessor methods and instance variables, making lookups efficient. If you need to clear these bindings-as when you add or remove a class from the run-time system-you can invoke __flushAllKeyBindings__ to do so.

  Some subclasses of NSObject override the default implementations. EOGenericRecord's implementations, for example, simply store and retrieve the properties in an NSDictionary object held by the EOGenericRecord. NSDictionary and NSMutableDictionary, though not suitable for use as enterprise objects, meaningfully implement these methods by directly accessing their key-value pairs.

  ---

  #### Type Checking and Type Conversion

  The default implementations of the key-value coding methods accept any object as a value, and do no type checking or type conversion among object classes. It's possible, for example, to pass an NSString to __takeValue:forKey:__ as the value for a property the receiver expects to be an NSDate. The sender of a key-value coding message is thus responsible for ensuring that a values is of the proper class, typically by using the __validateValue:forKey:__ method to coerce it to the proper type. The interface layer's EODisplayGroup uses this on all values received from interface user objects, for example, as well as relying on number and date formatters to interpret string values typed by the user. For more information on the __validateValue:forKey:__ method, see the EOClassDescription and EOEntityClassDescription class specifications.

  The key-value coding methods handle one special case with regard to value types. For enterprise objects that access numeric values as C scalar types, these methods automatically convert between the scalar types and NSNumber objects. For example, suppose your enterprise object defines these accessor methods:

  - (void)__setSalary:__ (unsigned int)_salary_- (unsigned int)__salary__

  For the __setSalary:__ method, __takeValue:forKey:__ converts the object value for the "salary" key in the dictionary to an __unsigned int__ and passes it as _salary_. Similarly, __valueForKey:__ converts the return value of the __salary__ method to an NSNumber and returns that.

  The default implementations support the following scalar types:

  | char | unsigned char |
  | short | unsigned short |
  | int | unsigned int |
  | long | unsigned long |
  | float | double |

```
```

  Object values are converted to these types with the standard messages __charValue__ , __intValue__ , __floatValue__ , and so on. Note that the key-value coding methods don't check that an object value actually responds to these messages; this can result in a run-time error if the object doesn't respond to the appropriate message.

  One type of conversion these methods can't perform is that from a __nil__ object value to a scalar value. C scalar values define no equivalent of a database system's NULL value, so these must be handled by the object itself. Upon encountering an __nil__ while setting a scalar value, the __takeValue:forKey:__ invokes __unableToSetNilForKey:__ , which by default simply raises an exception. Enterprise object classes that use scalar values which may be NULL in the database should override this method to substitute the appropriate scalar value for __nil__ , reinvoking __takeValue:forKey:__ to set the substitute value. This method works in general to handle setting scalar properties to __nil__ .

  ---

  #### EONull in Collections

  Because collection objects such as NSArray and NSDictionary can't contain __nil__ as a value, it must represented by a special object, EONull. EONull provides a single instance that represents the NULL value for object attributes. The default implementations of __takeValuesFromDictionary:__ and __valuesForKeys:__ translate EONull and __nil__ between NSDictionaries and enterprise objects, removing the need for your objects to explicitly test for EONull values.

  ---

  ### Relationship Accessor Methods

  Building on the key-value coding methods, another group of methods allows you to modify relationship properties by adding and removing single objects, rather than replacing the entire content of the relationship, and to modify relationships so that reciprocal relationships are automatically adjusted. __addObject:toPropertyWithKey:__ and __removeObject:fromPropertyWithKey:__ handle the first situation, doing all the work of altering arrays for to-many relationships. They both check first for a method you might implement, __addTo__ _Key___:__ or __removeFrom__ _Key___:__ , invoking that method if it's implemented, otherwise using the basic key-value coding methods to do the work.

  Reciprocal relationships are handled by __addObject:toBothSidesOfRelationshipWithKey:__ and __removeObject:fromBothSidesOfRelationshipWithKey:__ . For example, when you add an Employee to a Department's __employees__ relationship, or remove it, you also want the Employee's __department__ relationship altered to suit. These two methods take care of tracing the inverse relationship and use __addObject:toPropertyWithKey:__ and __removeObject:fromPropertyWithKey:__ to alter both relationships, whether they're to-one or to-many. Unless you have specific reasons to do otherwise, you should always use the methods that handle reciprocal relationships so that back pointers are properly updated.

  Two other methods that affect relationships are typically used internally by the Framework. You should rarely have a need either to invoke or override them. __propagateDeleteWithEditingContext:__ applies an object's delete rule to the destinations of its relationships. The delete rule specifies whether a destination object should be ignored, also deleted, or whether the deletion should be disallowed if a destination exists. __clearProperties__ simply sets all of the receiver's relationship properties to __nil__ . An EOEditingContext uses this method to break circular references between its objects when the context is deallocated.

  ---

  ### Snapshots

  The key-value coding methods define a general mechanism for accessing an object's properties, but you first have to know what those properties are. Sometimes, however, you just want to preserve an object's entire state for later use, whether to undo changes to the object, compare the values that have changed, or just keep a record of the changes. The snapshotting methods provide this service, extracting or setting all properties at once and performing the necessary conversions for proper behavior. __snapshot__ returns an NSDictionary containing all the receiver's properties, with EONull substituted for __nil__ and arrays reproduced as shallow, immutable copies. __updateFromSnapshot:__ sets properties of the receiver to the values in a snapshot, converting EONull to __nil__ , and making shallow, mutable copies of any array values (allowing the object to add to and remove from the array).

  ---

  ### Validation

  Validating new values is a vital part of business logic. Several methods added to NSObject support validation at different stages of an object's life. Validation methods check for illegal value types, values outside of established limits, illegal relationships, and so on. All validation methods return __nil__ if the values under consideration are valid, or an NSException indicating how the values aren't valid.

  There are two kinds of validation methods that you can override. The first covers individual properties, when it's important to validate a value before it changes. These methods are invoked automatically by the Framework when it changes a property value, such as when the user makes an edit in the user interface. These methods are dynamically invoked based on the property name. The second kind covers operations to the external store-inserting, updating, and deleting. These methods are invoked when the associated operation is performed. You can override these methods in your custom enterprise object classes to perform delayed validation of properties, to compare multiple properties against one another, and to allow or refuse the operation based on property values. For example, a Fee object might refuse to be deleted if it hasn't been paid yet.

  ---

  #### Immediate Validation of Individual Properties

  The most general method, __validateValue:forKey:__ , is used by the Framework when an EODisplayGroup passes an updated value to the object and when the object is saved. This method does two things: coerce the value into an appropriate type for the object, and validate it according to the object's rules. Coercion is performed automatically for you, so all you need handle is validation itself.

  The default implementation of __validateValue:forKey:__ consults the object's EOClassDescription for basic errors, such as a __nil__ value when that isn't allowed. If no basic errors exist, this method then examines the object's class itself for a method of the form __validate__ _Key___:__ and invokes that. These are the methods that your custom classes can implement to validate individual properties, such as __validateAge:__ to check that the value the user entered is within acceptable limits.

  For example, suppose that Member objects have an __age__ attribute stored as an integer. This attribute has an lower limit of 16, defined by the Member class. Now, suppose the user types "12" into a text field for the age. Before the EODisplayGroup updates the selected object, it sends the object a __validateValue:forKey:__ message. The object uses its EOEntityClassDescription to convert the string "12" into an NSNumber, then invokes __validateAge:__ with that NSNumber. Member's implementation of this method compares the age to its limit of 16 and returns an EOValidationException:

  > ```
  > - (NSException *)validateAge:(NSNumber *)age
  > {
  >     if ([age intValue] < 16) {
  >         return [NSException
  >             validationExceptionWithFormat:@"Age of %@ is below minimum.", age];
  >     }
  >     return nil;
  >
  > }
  > ```

  The Framework adds the __validationExceptionWithFormat:__ method to NSException for convenient creation of validation exceptions. The userInfo dictionaries in the exceptions raised by these methods contain the enterprise object being validated and the key (where applicable).

  ---

  #### Validation for Specific Operations

  The other validation methods are invoked at specific times-such as before the object is written to or deleted from the external store-and are particularly useful when properties must be compared or when expensive calculation is necessary. The methods are __validateForInsert__ , __validateForUpdate__ , __validateForSave__ , and __validateForDelete__ , and they're invoked automatically for the operations indicated by the method name. You can override these methods to check values individually or in groups; for example, you might verify that a pair of dates is in the proper temporal order:

  > ```
  > - (NSException *)validateForSave
  > {
  >     if ([startDate compare:endDate] == NSOrderedDescending) {
  >         return [NSException
  >             validationExceptionWithFormat:@"Start date must not follow end date."];
  >     }
  >     return [super validateForSave];
  >
  > }
  > ```

  Note that this method also invokes __super__ 's implementation. This is important, as the default implementations of the __validateFor...__ pass the check on to the object's EOClassDescription, which performs basic checking among properties. The access layer's EOEntityClassDescription class verifies constraints based on an EOModel, such as delete rules. For example, the delete rule for a Department object might state that it can't be deleted if it still contains Employee objects.

  __validateForSave__ is the generic validation method for when an object is written to the external store. The default implementations of __validateForInsert__ and __validateForUpdate__ both invoke this method. If an object performs validation that isn't specific to insertion or to updating, it should go in __validateForSave__ .

  **Initializing enterprise objects**

  **- initWithEditingContext:classDescription:globalID:

  **- awakeFromFetchInEditingContext:

  **- awakeFromInsertionInEditingContext:******

  **Announcing changes**

  **- willChange**

  **Getting an object's EOEditingContext**

  **- editingContext**

  **Getting class description information**

  **- allPropertyKeys

  **- attributeKeys

  **- classDescription

  **- classDescriptionForDestinationKey:

  **- deleteRuleForRelationshipKey:

  **- entityName

  **- inverseForRelationshipKey:

  **- isToManyKey:

  **- ownsDestinationObjectsForRelationshipKey:

  **- toManyRelationshipKeys

  **- toOneRelationshipKeys**********************

  **Key-value coding**

  **- takeValue:forKey:

  **- valueForKey:

  **- takeValuesFromDictionary:

  **- valuesForKeys:

  **- takeValue:forKeyPath:

  **- valueForKeyPath:

  **- takeStoredValue:forKey:

  **- takeStoredValue:forKeyPath:

  **- takeStoredValuesFromDictionary:

  **- handleQueryWithUnboundKey:

  **- handleTakeValue:forUnboundKey:

  **- unableToSetNilForKey:

  **+ accessInstanceVariablesDirectly

  **+ flushClassKeyBindings

  **+ flushAllKeyBindings

  **+ useStoredAccessor********************************

  **Modifying relationships**

  **- addObject:toPropertyWithKey:

  **- removeObject:fromPropertyWithKey:

  **- addObject:toBothSidesOfRelationshipWithKey:

  **- removeObject:fromBothSidesOfRelationshipWithKey:

  **- propagateDeleteWithEditingContext:

  **- clearProperties************

  **Working with snapshots**

  **- snapshot

  **- updateFromSnapshot:****

  **Validating values**

  **- validateForDelete

  **- validateForInsert

  **- validateForSave

  **- validateForUpdate

  **- validateValue:forKey:**********

  **Getting descriptions**

  **- eoDescription

  **- eoShallowDescription

  **- userPresentableDescription******

  ---

  #### accessInstanceVariablesDirectly

  + (BOOL)__accessInstanceVariablesDirectly__

  Returns YES if the default implementations of the key-value coding methods, on finding no accessor method for a property, should access the corresponding instance variable directly. Returns NO if they shouldn't. NSObject's implementation of this method returns YES. Subclasses can override it to return NO, in which case the other methods won't access instance variables.

  ---

  #### flushAllKeyBindings

  + (void)__flushAllKeyBindings__

  Invalidates the cached key binding information for all classes (caches are kept of key-to-method or instance variable bindings in order to make key-value coding efficient).

  __See also:__ + __flushClassKeyBindings__

  ---

  #### flushClassKeyBindings

  + (void)__flushClassKeyBindings__

  Invalidates the cached key binding information for the receiving class. This method should be invoked whenever a class is modified or removed from the run-time system.

  __See also:__ + __flushAllKeyBindings__

  ---

  #### useStoredAccessor

  + (BOOL)`useStoredAccessor`

  Returns YES if the default implementations of the key-value coding methods should be accessed using the `takeStoredValue...` methods, NO otherwise. NSObject's implementation of this method returns NO. Subclasses can override it to return YES. For more discussion of this topic, see the section ""Key-Value Coding Methods"" in the class description.

  __See also:__ - __takeStoredValue:forKey:__ , - __takeStoredValue:forKeyPath:__ , - __takeStoredValuesFromDictionary:__

  ---

  #### addObject:toBothSidesOfRelationshipWithKey:

  - (void)__addObject:__ (id)_anObject_ __toBothSidesOfRelationshipWithKey:__ (NSString \*)_key_

  Sets or adds _anObject_ as the destination for the receiver's relationship identified by _key_, and also sets or adds the receiver for _anObject_'s reciprocal relationship if there is one. For a to-one relationship, _anObject_ is set using __takeValue:forKey:__ . For a to-many relationship, _anObject_ is added using __addObject:toPropertyWithKey:__ .

  This method also properly handles removing __self__ and _anObject_ from their previous relationship as needed. For example, if an Employee object belongs to the Research department, invoking this method with the Maintenance department removes the Employee from the Research department as well as setting the Employee's department to Maintenance.

  __See also:__ - __removeObject:fromBothSidesOfRelationshipWithKey:__

  ---

  #### addObject:toPropertyWithKey:

  - (void)__addObject:__ (id)_anObject_ __toPropertyWithKey:__ (NSString \*)_key_

  Adds _anObject_ to the receiver's to-many relationship identified by _key_, without setting a reciprocal relationship. Similar to the implementation of __takeValue:forKey:__ , NSObject's implementation of this method first attempts to invoke a method of the form __addTo__ _Key___:__ . If the receiver doesn't have such a method, this method gets the property array using __valueForKey:__ and operates directly on that. If the array is mutable, this method simply adds _anObject_. Otherwise it constructs a new array containing any existing objects and _anObject_, then sets it using __takeValue:forKey:__ .

  __See also:__ - __removeObject:fromPropertyWithKey:__ , - __addObject:toBothSidesOfRelationshipWithKey:__

  ---

  #### allPropertyKeys

  - (NSArray \*)__allPropertyKeys__

  Returns all of the receiver's property keys, as returned by __attributeKeys__ , __toOneRelationshipKeys__ , and __toManyRelationshipKeys__ .

  ---

  #### attributeKeys

  - (NSArray \*)__attributeKeys__

  Returns the names of the receiver's attributes, as determined from the EOClassDescription. You might wish to override this method to add keys for attributes not defined by the EOClassDescription. The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of attributes designated as class properties.

  __See also:__ - __toOneRelationshipKeys__ , - __toManyRelationshipKeys__ ., [- __attributeKeys__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### awakeFromFetchInEditingContext:

  - (void)__awakeFromFetchInEditingContext:__ (EOEditingContext \*)_anEditingContext_

  Overridden by subclasses to perform additional initialization on the receiver upon its being fetched from the external repository into _anEditingContext_. NSObject's implementation merely sends an [__awakeObject:fromFetchInEditingContext:__](EOClassDescription-3.md)to the receiver's EOClassDescription. Subclasses should invoke __super__ 's implementation before performing their own initialization.

  __See also:__ - __awakeFromInsertionInEditingContext:__

  ---

  #### awakeFromInsertionInEditingContext:

  - (void)__awakeFromInsertionInEditingContext:__ (EOEditingContext \*)_anEditingContext_

  Overridden by subclasses to perform additional initialization on the receiver upon its being inserted into _anEditingContext_. This is commonly used to assign default values or record the time of insertion. NSObject's implementation merely sends an [__awakeObject:fromInsertionInEditingContext:__](EOClassDescription-3.md)to the receiver's EOClassDescription. Subclasses should invoke __super__ 's implementation before performing their own initialization.

  __See also:__ - __awakeFromFetchInEditingContext:__

  ---

  #### classDescription

  - (EOClassDescription \*)__classDescription__

  Returns the EOClassDescription registered for the receiver's class. If none is found, posts an [EOClassDescriptionNeededForClassNotification](EOClassDescription-3.md) on behalf of the receiver's class, allowing an observer to register a an EOClassDescription. See the [EOClassDescription](EOClassDescription-3.md) class specification for more information.

  __See also:__ [+ __registerClassDescription:forClass:__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### classDescriptionForDestinationKey:

  - (EOClassDescription \*)__classDescriptionForDestinationKey:__ (NSString \*)_key_

  Returns the EOClassDescription for the destination objects of the relationship identified by _key_. If none is found, posts an [EOClassDescriptionNeededForClassNotification](EOClassDescription-3.md) on behalf of the destination objects' class, allowing an observer to register a an EOClassDescription. See the [EOClassDescription](EOClassDescription-3.md) class specification for more information.

  __See also:__ [+ __registerClassDescription:forClass:__](EOClassDescription-3.md)(EOClassDescription), __[- classDescriptionForDestinationKey:](EOClassDescription-3.md)__ (EOClassDescription)

  ---

  #### clearProperties

  - (void)__clearProperties__

  Sets all of the receiver's to-one and to-many relationships to __nil__ . EOEditingContexts use this method to break circular references among objects when they're deallocated. You should never need to invoke this method or override it.

  __See also:__ - __toOneRelationshipKeys__ , - __toManyRelationshipKeys__ , - __takeValue:forKey:__

  ---

  #### deleteRuleForRelationshipKey:

  - (EODeleteRule)__deleteRuleForRelationshipKey:__ (NSString \*)_relationshipKey_

  Returns a rule indicating how to handle the destination of the receiver's relationship named by _relationshipKey_ when the receiver is deleted. The delete rule is one of:

  - EODeleteRuleNullify
  - EODeleteRuleCascade
  - EODeleteRuleDeny
  - EODeleteRuleNoAction

  For example, an Invoice object might return EODeleteRuleCascade for the relationship named "lineItems", since when an invoice is deleted, its line items should be deleted as well.

  __See also:__ - __propagateDeleteWithEditingContext:__ , - __validateForDelete__ , [- __deleteRuleForRelationshipKey:__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### editingContext

  - (EOEditingContext \*)__editingContext__

  Returns the EOEditingContext that holds the receiver.

  ---

  #### entityName

  - (NSString \*)__entityName__

  Returns the name of the receiver's entity, or __nil__ if it doesn't have one.

  __See also:__ [- __entityName__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### eoDescription

  - (NSString \*)__eoDescription__

  Returns a full description of the receiver's property values by extracting them using the key-value coding methods. An object referenced through relationships is listed with the results of an __eoShallowDescription__ message (to avoid infinite recursion through cyclical relationships).

  This method is useful for debugging. You can implement a __description__ method that invokes this one, and the debugger's print-object command (__po__ on the command line) automatically displays this description. You can also invoke this method directly on the command line of the debugger.

  __See also:__ - __userPresentableDescription__

  ---

  #### eoShallowDescription

  - (NSString \*)__eoShallowDescription__

  Returns a string containing the receiver's class and entity names, along with the memory address of its __id__ .

  __See also:__ - __userPresentableDescription__

  ---

  #### handleQueryWithUnboundKey:

  - (id)__handleQueryWithUnboundKey:__ (NSString \*)_key_

  Invoked from __valueForKey:__ when it finds no property binding for _key_. NSObject's implementation raises an NSInvalidArgumentException. Subclasses can override it to handle the query in some other way.

  ---

  #### handleTakeValue:forUnboundKey:

  - (void)__handleTakeValue:__ (id)_value_ __forUnboundKey:__ (NSString \*)_key_

  Invoked from __takeValue:forKey:__ when it finds no property binding for _key_. NSObject's implementation raises an NSInvalidArgumentException. Subclasses can override it to handle the request in some other way.

  ---

  #### initWithEditingContext:classDescription:globalID:

  - __initWithEditingContext:__ (EOEditingContext \*)_anEditingContext___classDescription:__ (EOClassDescription \*)_aClassDescription___globalID:__ (EOGlobalID \*)_globalID_

  Overridden by subclasses to perform initialization with the extra arguments provided. NSObject's implementation simply invokes __init__ .

  __See also:__ [- __createInstanceWithEditingContext:globalID:zone:__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### inverseForRelationshipKey:

  - (NSString \*)__inverseForRelationshipKey:__ (NSString \*)_relationshipKey_

  Returns the name of the relationship pointing back to the receiver's class or entity from that named by _relationshipKey_, or __nil__ if there isn't one. With the access layer's EOEntity and EORelationship, for example, reciprocality is determined by the join attributes of the two EORelationships.

  You might override this method for reciprocal relationships that aren't defined using the same join attributes. For example, if a Member object has a relationship to CreditCard based on the card number, but a CreditCard has a relationship to Member based on the Member's primary key, both classes need to override this method. This is how Member might implement it:

  > ```
  > - (NSString *)inverseForRelationshipKey:(NSString *)relationshipKey
  > {
  >     if ([relationshipKey isEqual:@"creditCard"]) return @"member";
  >         return [super inverseForRelationshipKey:relationshipKey];
  > }
  > ```

  __See also:__ [- __inverseForRelationshipKey:__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### isToManyKey:

  - (BOOL)__isToManyKey:__ (NSString \*)_key_

  Returns YES if the receiver has a to-many relationship identified by _key_, NO otherwise.

  __See also:__ - __toManyRelationshipKeys__ , - __toOneRelationshipKeys__

  ---

  #### ownsDestinationObjectsForRelationshipKey:

  - (BOOL)__ownsDestinationObjectsForRelationshipKey:__ (NSString \*)_key_

  Returns YES if the receiver has a relationship identified by _key_ that owns its destination, NO otherwise. If an object owns the destination for a relationship, then when that destination object is removed from the relationship, it's automatically deleted. Ownership of a relationship thus contrasts with a delete rule, in that the first applies when the destination is removed and the second applies when the source is deleted.

  __See also:__ - __deleteRuleForRelationshipKey:__ , [- __ownsDestinationObjectsForRelationshipKey:__](EOClassDescription-3.md)(EOClassDescription), - __ownsDestination__ (the access layer's EORelationship)

  ---

  #### propagateDeleteWithEditingContext:

  - (void)__propagateDeleteWithEditingContext:__ (EOEditingContext \*)_anEditingContext_

  Sends a [__propagateDeleteForObject:editingContext:__](EOClassDescription-3.md)message to the receiver's EOClassDescription. This causes the destination objects of the receiver's relationships to be deleted according to the delete rule for each relationship:

  | __Delete Rule__ | __Action__ |
  | EODeleteRuleNullify | The destination object is simply removed from the relationship, and the receiver is likewise removed from the destination's reciprocal l relationship if there is one. |
  | EODeleteRuleCascade | As above, but the destination object is also deleted and sent a __propagateDeleteWithEditingContext:__ message. |
  | EODeleteRuleDeny | Applied in __validateForDelete__ , not in this method. |
  | EODeleteRuleNoAction | The relationship is ignored when the receiver is deleted. The EODeleteRuleNoAction option is useful for tuning performance. In order to perform a deletion, Enterprise Objects Framework fires all the faults of the deleted object and then fires any to-many faults that point back to the deleted object. For example, suppose you have a simple application based on the sample Movies database. Deleting a Movie object has the effect of firing a to-one fault for the Movie's `studio` relationship, and then firing the to-many `movies` fault for that studio. In this scenario, it would make sense to set the delete rule EODeleteRuleNoAction for Movie's `studio` relationship. However, you should use this delete rule with great caution since it can result in dangling references in your object graph. |

```
```

  __See also:__ - __deleteRuleForRelationshipKey:__

  ---

  #### removeObject:fromBothSidesOfRelationshipWithKey:

  - (void)__removeObject:__ (id)_anObject_ __fromBothSidesOfRelationshipWithKey:__ (NSString \*)_key_

  Removes _anObject_ from the receiver's relationship identified by _key_, and also removes the receiver from _anObject_'s reciprocal relationship if there is one. For a to-one relationship, _anObject_ is removed using __takeValue:forKey:__ with __nil__ as the value. For a to-many relationship, _anObject_ is removed using __removeObject:fromPropertyWithKey:__ .

  __See also:__ - __addObject:toBothSidesOfRelationshipWithKey:__

  ---

  #### removeObject:fromPropertyWithKey:

  - (void)__removeObject:__ (id)_anObject_ __fromPropertyWithKey:__ (NSString \*)_key_

  Removes _anObject_ from the receiver's to-many relationship identified by _key_, without modifying a reciprocal relationship. Similar to the implementation of __takeValue:forKey:__ , NSObject's implementation of this method first attempts to invoke a method of the form __removeFrom__ _Key___:__ . If the receiver doesn't have such a method, this method gets the property array using __valueForKey:__ and operates directly on that. If the array is mutable, this method simply locates _anObject_ and removes it. Otherwise it constructs a new array containing any existing objects minus _anObject_, then sets it using __takeValue:forKey:__ .

  __See also:__ - __addObject:toPropertyWithKey:__ , - __removeObject:fromBothSidesOfRelationshipWithKey:__

  ---

  #### snapshot

  - (NSDictionary \*)__snapshot__

  Returns a dictionary whose keys are those of the receiver's attributes, to-one relationships, and to-many relationships, and whose values are the values of those properties, with EONull substituted for __nil__ . For to-many relationships, the dictionary contains shallow copies of the arrays to preserve the __id__ s of the contents.

  __See also:__ - __updateFromSnapshot:__ , - __allPropertyKeys__ , - __valueForKey:__

  ---

  #### takeStoredValue:forKey:

  - (void)`takeStoredValue:`(id)_value_ `forKey:`(NSString \*)_key_

  Sets the property identified by _key_ to _value_. If you haven't overridden __useStoredAccessor__ to return YES, this method simply invokes __takeValue:forKey:__ . If you have overridden __useStoredAccessor__ to return YES, the default implementation does the following:

  - Searches for an instance variable whose name is the same as the key, but preceded by an underbar. Sets its value directly. For example, with a key of "lastName", __takeStoredValue:forKey:__ looks for an instance variable called `_lastName`.
  - If the instance variable isn't found, searches for an accessor method based on the key, but preceded by an underbar. For example, with a key of "lastName", __takeStoredValue:forKey:__ looks for a method called `_setLastName.`
  - If neither an underbar-preceded instance variable or accessor method is found, searches for an instance variable whose name is the same as the key and sets its value directly.
  - Finally, searches for an accessor method based on the key. For the key "lastName", this would be `setLastName:`.Classes can override this method to add custom behavior. The default implementation raises an exception if an unknown key is passed in. For more discussion of key-value coding, see the section ""Key-Value Coding Methods"" in the class description.

  __See also:__ + __useStoredAccessor__ , - __takeStoredValue:forKeyPath:__ , - __takeStoredValuesFromDictionary:__

  ---

  #### takeStoredValue:forKeyPath:

  - (void)`takeStoredValue:`(id)_value_ `forKeyPath:`(NSString \*)_keyPath_

  Sets the value for the derived property identified by _key__Path_ to _value_. For example, suppose you have the following code:

  > ```
  > [myEmployee takeStoredValue:aStreet forKeyPath:@"address.street"];
  > ```

  This code would first get the address object by invoking `[myEmployee valueForKey:@"address"]`, and then it would set the value using `[address setStoredValue:aStreet forKey:@"street"]`.

  __See also:__ + __useStoredAccessor__ , - __takeValue:forKey:__ , - __takeStoredValuesFromDictionary:__

  ---

  #### takeStoredValuesFromDictionary:

  - (void)`takeStoredValuesFromDictionary:`(NSDictionary \*)_aDictionary_

  Sets properties of the receiver with values from _aDictionary_, using their keys to identify the properties. NSObject's implementation invokes __takeStoredValue:forKey:__ for each key-value pair, substituting __nil__ for EONull values in _aDictionary_.

  __See also:__ + __useStoredAccessor__ , - __takeValue:forKey:__ , - __takeValue:forKeyPath:__

  ---

  #### takeValue:forKey:

  - (void)__takeValue:__ (id)_value_ __forKey:__ (NSString \*)_key_

  Sets the value for the property identified by _key_ to _value_. NSObject's implementation does so by first checking the receiver for a selector of the form __set__ _Key___:__ , invoking it if there is one. If there's no such method, and __accessInstanceVariablesDirectly__ returns YES, NSObject's implementation checks for an instance variable named _key_ and sets the value directly, autoreleasing the old value and retaining the new one.

  If there's neither an accessor method nor an instance variable matching _key_, NSObject's implementation invokes __handleTakeValue:forUnboundKey:__ as a fallback mechanism. Subclasses can override __handleTakeValue:forUnboundKey:__ to handle the request in some other way. For more discussion of key-value coding, see the section "Key-Value Coding Methods" in the class description.

  __See also:__ - __takeValue:forKeyPath:__ , - __takeValuesFromDictionary:__ , - __valueForKey:__

  ---

  #### takeValue:forKeyPath:

  - (void)__takeValue:__ (id)_value_ __forKeyPath:__ (NSString \*)_keyPath_

  Sets the value for the derived property identified by _keyPath_ to _value_. A key path has the form _relationship.property_ (with one or more relationships); for example "department.name". NSObject's implementation of this method gets the destination object for each relationship using __valueForKey:__ , and sends the final object a __takeValue:forKey:__ message with _value_ and _property_.

  __See also:__ - __takeValuesFromDictionary:__ , - __valueForKeyPath:__

  ---

  #### takeValuesFromDictionary:

  - (void)__takeValuesFromDictionary:__ (NSDictionary \*)_aDictionary_

  Sets properties of the receiver with values from _aDictionary_, using the keys to identify the properties. NSObject's implementation invokes __takeValue:forKey:__ for each key-value pair, substituting __nil__ for EONull values in _aDictionary_.

  __See also:__ - __updateFromSnapshot:__ , - __takeValue:forKeyPath:__ , - __valuesForKeys:__

  ---

  #### toManyRelationshipKeys

  - (NSArray \*)__toManyRelationshipKeys__

  Returns the names of the receiver's to-many relationships, as determined from the EOClassDescription. You might wish to override this method to add keys for relationships not defined by the EOClassDescription. The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-many relationships designated as class properties.

  __See also:__ - __toOneRelationshipKeys__ ., - __attributeKeys__ , [- __toManyRelationshipKeys__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### toOneRelationshipKeys

  - (NSArray \*)__toOneRelationshipKeys__

  Returns the names of the receiver's to-one relationships, as determined from the EOClassDescription. You might wish to override this method to add keys for relationships not defined by the EOClassDescription. The access layer's subclass of EOClassDescription, EOEntityClassDescription, returns the names of to-one relationships designated as class properties.

  __See also:__ - __attributeKeys__ , - __toManyRelationshipKeys__ ., [- __toOneRelationshipKeys__](EOClassDescription-3.md)(EOClassDescription)

  ---

  #### unableToSetNilForKey:

  - (void)__unableToSetNilForKey:__ (NSString \*)_key_

  Invoked from __takeValue:forKey:__ when it's given a __nil__ value for a scalar property (such as an __int__ or a __float__ ). NSObject's implementation raises an NSInvalidArgumentException. Subclasses can override it to handle the request in some other way, such as by substituting zero or a sentinel value and invoking __takeValue:forKey:__ again.

  ---

  #### updateFromSnapshot:

  - (void)__updateFromSnapshot:__ (NSDictionary \*)_aSnapshot_

  Takes the values from _aSnapshot_, setting each one according to its key using __takeValue:forKey:__ . In the process, EONull values are converted to __nil__ , and array values are set as shallow mutable copies to preserve the __id__ s of the contents.

  __See also:__ - __takeValuesFromDictionary:__ , - __snapshot__

  ---

  #### userPresentableDescription

  - (NSString \*)`userPresentableDescription`

  Returns a short (no longer than 60 characters) description of an enterprise object based on its data. NSObject's implementation first checks to see if the enterprise object has an attribute called "name" and if so, it returns its value. Otherwise, checks for an attribute called "title". If neither of those attributes exists, this method enumerates the object's __attributeKeys__ and returns the values of all of its properties, separated by commas (applying the default formatter for numbers and dates).

  __See also:__ - __eoDescription__ , - __eoShallowDescription__

  ---

  #### validateForDelete

  - (NSException \*)__validateForDelete__

  Confirms that the receiver can be deleted in its current state, returning __nil__ if it can or an NSException that the sender may raise if it can't. For example, an object can't be deleted if it has a relationship with a delete rule of EODeleteRuleDeny and that relationship has a destination object.

  NSObject's implementation sends the receiver's EOClassDescription a [__validateObjectForDelete:__](EOClassDescription-3.md)message (which performs basic checking based on the presence or absence of values). Subclasses should invoke __super__ 's implementation before performing their own validation, and should combine any exception returned by __super__ 's implementation with their own:

  > ```
  > - (NSException *)validateForDelete
  > {
  >     NSException *exception = [super validateForDelete];
  >
  >     if (/* some other violation */ ) {
  >         NSException *newException = /* the extra exception */;
  >         exception = [NSException aggregateExceptionWithExceptions:[NSArray
  >              arrayWithObjects:exception, newException, nil]];
  >     }
  >
  >     return exception;
  >
  > }
  > ```

  __See also:__ - __validateForInsert__ , - __validateForSave__ , - __validateForUpdate__ , - __validateValue:forKey:__ , + __validationExceptionWithFormat:__ (NSException Additions)

  ---

  #### validateForInsert

  - (NSException \*)__validateForInsert__

  Confirms that the receiver can be inserted in its current state, returning __nil__ if it can or an NSException that can be raised if it can't. NSObject's implementation simply invokes __validateForSave__ .

  __See also:__ - __validateForDelete__ , - __validateForUpdate__ , - __validateValue:forKey:__ , + __validationExceptionWithFormat:__ (NSException Additions)

  ---

  #### validateForSave

  - (NSException \*)__validateForSave__

  Confirms that the receiver can be saved in its current state, returning __nil__ if it can or an NSException that the sender may raise if it can't. NSObject's implementation sends the receiver's EOClassDescription a [__validateObjectForSave:__](EOClassDescription-3.md)message, then iterates through all of the receiver's properties, invoking __validateValue:forKey:__ for each one. If this results in more than one exception, the exception returned contains the additional ones in its __userInfo__ dictionary under the EOAdditionalExceptions key . Subclasses should invoke __super__ 's implementation before performing their own validation, and should combine any exception returned by __super__ 's implementation with their own:

  > ```
  > - (NSException *)validateForSave
  > {
  >     NSException *exception = [super validateForSave];
  >
  >     if (/* some other violation */ ) {
  >         NSException *newException = /* the extra exception */;
  >         exception = [NSException aggregateExceptionWithExceptions:[NSArray
  >              arrayWithObjects:exception, newException, nil]];
  >     }
  >
  >     return exception;
  > }
  > ```

  Enterprise objects can implement this method to check that certain relations between properties hold; for example, that the end date of a vacation period follows the begin date. To validate an individual property, you can simply implement a method for it as described under __validateValue:forKey:__ .

  __See also:__ - __validateForDelete__ , - __validateForInsert__ , - __validateForUpdate__ , + __validationExceptionWithFormat:__ (NSException Additions), + __aggregateExceptionWithExceptions:__ (NSException Additions)

  ---

  #### validateForUpdate

  - (NSException \*)__validateForUpdate__

  Confirms that the receiver can be updated in its current state, returning __nil__ if it can or an NSException that the sender may raise if it can't. NSObject's implementation simply invokes __validateForSave__ .

  __See also:__ - __validateForDelete__ , - __validateForInsert__ , - __validateForSave__ , - __validateValue:forKey:__ , [+ __validationExceptionWithFormat:__](NSException%20Additions.md)(NSException Additions)

  ---

  #### validateValue:forKey:

  - (NSException \*)__validateValue:__ (id \*)_valuePointer_ __forKey:__ (NSString \*)_key_

  Confirms that the value referenced by _valuePointer_ is legal for the receiver's property named by _key_. Returns __nil__ if it can confirm that the value is legal or an EOValidationException that the sender may raise if it can't. NSObject's implementation sends a [__validateValue:forKey:__](EOClassDescription-3.md)message to the receiver's EOClassDescription. If that message doesn't return an exception, it checks for a method of the form __validate__ _Key___:__ (for example, __validateBudget:__ for a _key_ of "budget") and invokes it, returning the result.

  Enterprise objects can implement individual __validate__ _Key___:__ methods to check limits, test for nonsense values, and otherwise confirm individual properties. To validate multiple properties based on relations among them, override the appropriate __validateFor...__ method.

  __See also:__ - __validateForDelete__ , - __validateForInsert__ , - __validateForSave__ , - __validateForUpdate__ , [+ __validationExceptionWithFormat:__](NSException%20Additions.md)(NSException Additions)

  ---

  #### valueForKey:

  - (id)__valueForKey:__ (NSString \*)_key_

  Returns the value for the property identified by _key_. NSObject's implementation does so by first checking the receiver for a method named _key_, invoking it if there is one. If there's no such method, and __accessInstanceVariablesDirectly__ returns YES, NSObject's implementation checks for an instance variable named _key_ and returns the instance variable. If there's neither an accessor method nor an instance variable matching _key_, NSObject's implementation invokes __handleQueryWithUnboundKey:__ as a fallback mechanism. Subclasses can override __handleQueryWithUnboundKey:__ to handle the request in some other way.

  __See also:__ - __valueForKeyPath:__ , - __valuesForKeys:__ , - __takeValue:forKey:__

  ---

  #### valueForKeyPath:

  - (id)__valueForKeyPath:__ (NSString \*)_keyPath_

  Returns the value for the derived property identified by _keyPath_. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.Talent.lastName". NSObject's implementation of this method gets the destination object for each relationship using __valueForKey:__ , and returns the result of a __valueForKey:__ message to the final object.

  __See also:__ - __valuesForKeys:__ , - __takeValue:forKeyPath:__

  ---

  #### valuesForKeys:

  - (NSDictionary \*)__valuesForKeys:__ (NSArray \*)_keys_

  Returns a dictionary containing the property values identified by each of _keys_. NSObject's implementation invokes __valueForKey:__ for each key in _keys_, substituting EONull in the dictionary for returned __nil__ values.

  __See also:__ - __valueForKeyPath:__ , - __takeValuesFromDictionary:__

  ---

  #### willChange

  - (void)__willChange__

  Notifies any observers that the receiver's state is about to change, by sending each an [__objectWillChange:__](EOObserving-2.md)message (see the EOObserverCenter class specification for more information). A subclass should not override this method, but should invoke it prior to altering their state, most typically in "set" methods such as the following:

  > ```
  > - (void)setRoleName:(NSString *)value {
  >     [self willChange];
  >     [roleName autorelease];
  >     roleName = [value retain];
  > }
  > ```

  ---

  [!](NSException%20Additions.md)
  [!](EOClassDescriptionClassDelegate.md)

  ---

  _Copyright © 1998, Apple Computer, Inc. All rights reserved._
