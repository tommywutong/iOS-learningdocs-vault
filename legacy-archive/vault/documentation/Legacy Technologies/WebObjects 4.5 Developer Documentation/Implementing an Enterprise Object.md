---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/EOsI3.html
archived_at: '2026-07-15T08:03:07.479475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Designing%20Enterprise%20Objects.md) [!Previous Section](Defining%20the%20Model.md)

# Implementing an Enterprise Object

As discussed in the section["EOGenericRecord or Custom Class?"](Defining%20the%20Model.md#apple-hazdk), one of the first decisions you need to make about an enterprise object is whether you want it to be an EOGenericRecord or a custom class. Use EOGenericRecords to represent enterprise objects that don't require custom behavior, and create custom classes to represent enterprise objects that do.

Enterprise Objects Framework interacts with generic records and custom classes the same way. It defines the set of methods for supporting operations common to all enterprise objects and uses only those methods. The EOEnterpriseObject interface (or informal protocol in Objective-C) specifies the complete set. It includes methods for initializing instances, announcing changes, setting and retrieving property values, and performing validation of state.
You rarely need to implement the EOEnterpriseObject interface from scratch. The Framework provides default implementations of all its methods. In Java, the class EOCustomObject implements the interface, so your custom classes should inherit from it. In Objective-C, categories on the root class, NSObject, provide default implementations. Regardless of what language you choose, some of the default method implementations are for custom classes to override, but most are meant to be used as defined by the Framework. Many methods are used internally by the Framework and are rarely invoked by your application code. For more information on EOEnterpriseObject and its methods, see the interface specification in _Enterprise Objects Framework Reference_.
The remainder of this chapter describes implementing custom classes.

## Generating Source Files

The easiest way to create a custom enterprise object is with EOModeler's Generate Java Files, Generate ObjC Files, and Generate Client Java Files commands. These commands take the attributes and relationships you've defined in your model, and use them to generate source code for a corresponding enterprise object class.
You can generate the source code in Java (Generate Java Files) or Objective-C (Generate ObjC Files). The Generate Client Java Files command creates source code for classes that will be used in the client side of a distributed WebObjects application.
If you choose Java as your language, EOModeler creates a __.java__ file for your class. If you choose Objective-C, it creates both a header (__.h__) and an implementation (__.m__) file. No matter what the language, the source files created by EOModeler are completely functional.

## Superclass

EOModeler assumes that your custom classes descend from EOCustomObject (or NSObject in Objective-C) so that they inherit the Framework's default implementations of the EOEnterpriseObject interface.

## Instance Variables

EOModeler's generated source code files contain instance variables for all of the corresponding entities class properties, both attributes and relationships alike. For example, the following code excerpts show the instance variables created for the Member class:
In Java, (from __Member.java__)

```
protected String city;
protected NSGregorianDate memberSince;
protected String phone;
protected String state;
protected String streetAddress;
protected String zip;
protected Number customerID;
protected String firstName;
protected String lastName;
protected CreditCard creditCard;
protected NSMutableArray rentals;
```


In Objective-C (from __Member.h__)

```
NSString *city;
NSCalendarDate *memberSince;
NSString *phone;
NSString *state;
NSString *streetAddress;
NSString *zip;
NSNumber *customerID;
NSString *firstName;
NSString *lastName;
CreditCard *creditCard;
NSMutableArray *rentals;
```


All of the instance variables correspond to attributes in the Member entity except for __creditCard__ and __rentals__, which correspond to relationships.

### Primary key generation

Enterprise objects don't have to declare instance variables for primary key and foreign key values. The Framework manages primary and foreign keys automatically.
The default mechanism for assigning unique primary keys is provided with the EOAdaptorChannel method __primaryKeyForNewRowWithEntity__ (or __primaryKeyForNewRowWithEntity:__ in Objective-C). If you need to provide a custom mechanism for assigning primary keys, you can implement the EODatabaseContext delegate method __databaseContextNewPrimaryKey__ (or __databaseContext:newPrimaryKeyForObject:entity:__ in Objective-C). Using either of these two techniques means you don't need to store the primary key in your enterprise object. For more discussion of primary keys, see the chapter ["Answers to Common Design Questions"](Answers%20to%20Common%20Design%20Questions.md#apple-g44tkoa).

Note that Enterprise Objects Framework doesn't support modifiable primary key values-you shouldn't design your application so that users can change a primary key's value. If you really need this behavior, you have to implement it by deleting an affected object and reinserting it with a new primary key.

## Writing Accessor Methods

When you generate source files for custom classes in EOModeler, the resulting files include default accessor methods. Accessor methods let you set and return the values of your class properties (instance variables). For example, here are some of Customer's accessor methods:
In Java, (from __Member.java__)

```
public NSGregorianDate memberSince() {
    willChange();
    return memberSince;
}

public void setMemberSince(NSGregorianDate value) {
    willChange();
    memberSince = value;
}

public CreditCard creditCard() {
    willChange();
    return creditCard;
}

public void setCreditCard(CreditCard value) {
    willChange();
    creditCard = value;
}

public NSArray rentals() {
    willRead();
    return rentals;
}

public void setRentals(NSMutableArray value) {
    willChange();
    rentals = value;
}

public void addToRentals(Rental object) {
    willChange();
    rentals.addObject(object);
}

public void removeFromRentals(Rental object) {
    willChange();
    rentals.removeObject(object);
}
```


In Objective-C (from __Member.m__)

```objc
- (void)setMemberSince:(NSCalendarDate *)value
{
    [self willChange];
    [memberSince autorelease];
    memberSince = [value retain];
}
- (NSCalendarDate *)memberSince { return memberSince; }

- (void)setCreditCard:(CreditCard *)value
{
    // a to-one relationship
    [self willChange];
    [creditCard autorelease];
    creditCard = [value retain];
}
- (CreditCard *)creditCard { return creditCard; }

- (void)addToRentals:(Rental *)object
{
    // a to-many relationship
    [self willChange];
    [rentals addObject:object];
}
- (void)removeFromRentals:(Rental *)object
{
    // a to-many relationship
    [self willChange];
    [rentals removeObject:object];
}
- (NSArray *)rentals { return rentals; }
```


Features introduced by these code excerpts are discussed in the following sections.
__Note:__  You don't have to provide accessor methods for your object's properties. The Framework can access your object's properties directly (through its instance variables). For more information, see the section ["Accessing an Enterprise Object's Data"](#apple-he2deni)."

### Change Notification

In the above code excerpts from Member source files__,__ you can see that each of the "set" methods includes an invocation of the __willChange__ method.
In Enterprise Objects Framework, objects that need to know about changes to an enterprise object register as observers for change notifications. When an enterprise object is about to change, it has the responsibility of posting a change notification so that registered observers are notified. To do this, enterprise objects should invoke the method __willChange__ prior to altering their state. This is invoked by default in generated source code's "set" methods, but whenever you add your own methods that change the object's state, you need to remember to include an invocation.
An implementation of __willChange__ is provided in EOCustomObject (or NSObject in Objective-C), so you don't have to implement it yourself. For more information on change notification, see the specification for the control layer's EOObserverCenter class in _Enterprise Objects Framework Reference_.
__Note:__  If you're using EOGenericRecord, you don't have to worry about invoking __willChange__. As the default enterprise object class, EOGenericRecord handles change notifications as part of its normal behavior.

### Faulting

Similar to the way "set" methods invoke the __willChange__ method, Java "get" methods include an invocation of __willRead__. This method is part of Enterprise Objects Framework's _faulting_ mechanism for postponing an object's initialization until its actually needed. Faulting is also provided with Objective-C, but its implementation is different and doesn't require the __willRead__ method.
In Java, the __willRead__ method and a handful of others are defined in the Framework's EOFaulting interface. EOFaulting is a part of EOEnterpriseObject, so your custom classes inherit a default implementation of it. The default implementation of __willRead__ checks to see if the receiver has already been fully initialized. If it hasn't been, it fills the object with values fetched from the database. Before your application attempts to message an object, you must ensure that it has its data. To do this, enterprise objects invoke the method __willRead__ prior to any attempt to access the object's state, most typically in "get" methods. Enterprise Objects don't have to invoke __willRead__ in "set" methods, because the __willChange__ method invokes __willRead__ for you.
For more information on faulting, see the interface specification for EOFaulting in _Enterprise Objects Framework Reference_. For more information on Objective-C's faulting mechanism, see the EOFault class specification.

### Accessing Data through Relationships

Relationships and flattened properties are treated no differently than properties based on the entity's original attributes.
For example, Customer can use its __creditCard__ relationship to traverse the object graph and change values in the CreditCard object. If you want to access information about a Customer's credit card, your code can do something like this:
In Java:

```
customer.creditCard().limit();
```


In Objective-C:

```
[[member creditCard] limit];
```


You can also modify attributes in the object graph regardless of what table they came from. For example, suppose that Customer's __streetAddress__ attribute was flattened from an Address entity. Customer could have a __setStreetAddress__ method that modified the attribute, even though it's not actually stored in the Customer table.

### Accessing an Enterprise Object's Data

In implementing your enterprise object classes, you want to focus on the code that's unique to your application, not on code that deals with fitting your objects into the Framework. To this end, the Framework uses a standard interface for accessing an enterprise object's properties and provides a default implementation that takes advantage of methods you're likely to write for your own use anyway.
This data transport mechanism is defined by the EOKeyValueCoding interface (or informal protocol in Objective-C). It specifies that properties of an object are accessed indirectly by name (or _key_), rather than directly through invocation of an accessor method or as instance variables. EOKeyValueCoding is incorporated in the EOEnterpriseObject interfaces, so your custom classes automatically inherit key-value coding behavior that is sufficient for most purposes.
The basic methods for accessing an object's values are __takeValueForKey__ and __valueForKey__ (__takeValue:forKey:__ and __valueForKey:__ in Objective-C), which set or return the value for the specified key, respectively. The default implementations use the accessor methods normally implemented by objects (or to access instance variables directly if need be), so that you don't have to write special code simply to integrate your objects into the Enterprise Objects Framework.
There are corresponding methods __takeStoredValueForKey__ and __storedValueForKey__ (__takeStoredValue:forKey:__ and __storedValueForKey:__ in Objective-C) are similar, but they're considered to be private to the Framework and to the enterprise object class that provides them. The stored value methods are for use by the Framework for transporting data to and from trusted sources. For example, __takeStoredValueForKey__ is used to initialize an object's properties with values fetched from the database, whereas __takeValueForKey__ is used to modify an object's properties to values provided by a user.
Public Access with the Basic Methods
When accessing an object's class properties, the default implementations of the basic key-value coding methods use the class definition. They look for "set" methods in the following sequence:

```
setProperty
_setProperty
```


where _property_ is the name of the property as in __lastName__. Note that the first letter of the property name is made uppercase as in __setLastName__.
Similarly, the key-value coding methods look for "get" methods in the following sequence:

```
getProperty
property
_getProperty
_property
```


If no accessor methods can be found, the key-value coding methods look for instance variables containing the property's name and sets or retrieves their value directly. The search order for instance variables is as follows:

```
property
_property
```


where _property_ is the name of the property as in __lastName__.
By using the accessor methods you normally define for your objects, the default implementations of the key-value coding methods allow you to concentrate on implementing custom behavior. They also allow your objects to determine how their properties are accessed. For example, your Employee class can define a __salary__ method that just returns an employee's salary directly or calculates it from another value.
__Note:__  You shouldn't use "set" methods to perform validation. Rather, you should use the validation methods, described in["Performing Validation"](#apple-he4dqna).

Private Access with the Stored Value Methods
The stored value methods, __takeStoredValueForKey__ and __storedValueForKey__, are used by the framework to store and restore an enterprise object's properties, either from the database or from an in-memory snapshot (for undoing changes to an object and for synchronizing objects between child and parent editing contexts in a nested configuration, for example).This access is considered private to the enterprise object and is invoked by the Framework to effect persistence on the object's behalf. On the other hand, the basic key-value coding methods are the public API to an enterprise object. They are invoked by clients external to the object, such as for interactions with the user interface or with other enterprise objects.
Like the basic key-value coding methods, the stored value methods access an object's properties by invoking property-specific accessor methods or by directly accessing instance variables. However, the stored value methods use a different search order for resolving the property key: they search for a private accessor first (a method beginning with an underbar), then for an instance variable, and finally for a public accessor. Enterprise object classes can take advantage of this distinction to simply set or get values when properties are accessed through the private API (on behalf of a trusted source) and to perform additional processing when properties are accessed through the public API. Put another way, the stored value methods allow you bypass the logic in your public accessor methods, whereas the basic key-value coding methods execute that logic.
The stored value methods are especially useful in cases where property values are interdependent. For example, suppose you need to update a total whenever an object's __bonus__ property is set:
In Java:

```
void setBonus(double newBonus) {
    willChange();
    _total += (newBonus - _bonus);
    _bonus = newBonus;
}
```


In Objective-C:

```objc
-  (void)setBonus:(double)newBonus {
    [self willChange];
    _total += (newBonus - _bonus);
    _bonus = newBonus;
}
```


This total-updating code should be activated when the object is updated with values provided by a user (through the user interface), but not when the __bonus__ property is restored from the database. Since the Framework restores the property using __takeStoredValueForKey__ and since this method accesses the ___bonus__ instance variable in preference to calling the public accessor, the unnecessary (and possibly expensive and harmful) recomputation of ___total__ is avoided. If the object actually wants to intervene when a property is set from the database, it has two options:

- Implement ___setBonus__ (___setBonus:__ in Objective-C).
- Replace the Framework's default stored value search order with the same search order used by the basic methods. To do this, in your custom class, implement the static method __useStoredAccessor__ to return __false__. (In Objective-C, override the class method __useStoredAccessor__ to return NO.)

Error Handling methods

EOKeyValueCoding defines two additional methods for handling error conditions: __handleQueryWithUnboundKey__ and __handleTakeValueForUnboundKey__ (__handleQueryWithUnboundKey:__ and __handleTakeValue:forUnboundKey:__ in Objective-C). The default implementation of the key-value coding methods invoke these methods when they receive a key for which they can find no accessor methods or instance variables. The default implementations throw exceptions, but you can override them to handle the error in a way that's appropriate for your custom class.

## Writing Derived Methods

The source files generated by EOModeler provide a basic implementation that doesn't go beyond the functionality provided by an EOGenericRecord. But you can use the files as a basis for adding behavior to your enterprise object.
One kind of behavior you might want to add to your enterprise object class is the ability to apply a filter to an object's to-many relationship property and return a subset of the destination objects. For example, you could have an __overdueRentals__ method in the Customer class that returns the subset of a customer's rentals that are overdue:
In Java:

```
public NSArray overdueRentals() {
    EOQualifier qualifier;

    qualifier = new EOKeyValueQualifier(
        "isOverdue",
        EOQualifier.QualifierOperatorEqual,
        new Boolean(true));

    return EOQualifier.filteredArrayWithQualifier(
        allRentals(),
        qualifier);
}
```


In Objective-C:

```objc
- (NSArray *)overdueRentals {
    EOQualifier *qualifier;

    qualifier = [[[EOKeyValueQualifier alloc]
        initWithKey:@"isOverdue"
        operatorSelector:EOQualifierOperatorEqual
        value:[NSNumber numberWithBool:YES]autorelease];

    return [[self allRentals]
        filteredArrayUsingQualifier:qualifier];
}
```


The __overdueRentals__ method creates a qualifier to find all of a customer's overdue rentals. The qualifier is performed in memory against the complete set of a customer's rentals.
With the addition of this method, Customer has a "get" accessor method with no corresponding "set" method. A __setOverdueRentals__ method doesn't make sense because __overdueRentals__ is derived. However, since Enterprise Objects Framework invokes accessor methods automatically, you may wonder if the absence of a __setOverdueRentals__ method can cause problems. The answer is no, you don't have to define a corresponding set method. Enterprise Objects Framework will not attempt to invoke __setOverdueRentals__ unless you bind the __overdueRentals__ property to an editable user interface object.

## Performing Validation

A good part of your application's business logic is usually validation-for example, verifying that customers don't exceed their credit limits, that return dates don't come before their corresponding check out dates, and so on. In your enterprise object classes, you implement methods that check for invalid data, and the framework automatically invokes them before saving anything to the database.
The EOValidation interface (informal protocol in Objective-C) defines the way that enterprise objects validate their values. The validation methods can check for illegal value types, values outside of established limits, illegal relationships, and so on. Like EOKeyValueCoding, EOValidation is incorporated in the EOEnterpriseObject interface, so your custom classes automatically inherit some basic validation behavior. The default implementations of these methods check the object's state against constraints and rules defined in your model.
There are two kinds of validation methods. The first validates an entire object to see if it's ready for a specific operation (inserting, updating, and deleting) and the second validates individual properties. The two different types are discussed in more detail in the following sections. For more a more detailed discussion, see the EOValidation interface specification in the _Enterprise Objects Framework Reference_.

### Validating Before an Operation

The methods for validating an object before a specific operation are:

- validateForSave
- validateForDelete
- validateForInsert
- validateForUpdate

When you perform a particular operation on an enterprise object (such as attempting to delete it), the EOEditingContext sends a validation message to your enterprise object appropriate to the operation. Based on the result, the operation is either accepted or refused. For example, referential integrity constraints in your model might state that you can't delete a Customer object that has Rentals. If a user attempts to delete a customer that has rentals, the deletion is refused.
You might want to override these methods to perform additional validation to what can be specified in a model. For example, your application should never allow a fee to be deleted if it hasn't been paid. You could implement this in a Fee class as follows:
In Java:

```
public void validateForDelete() throws
EOValidation.Exception
{
    EOValidation.Exception superException = null;
    EOValidation.Exception myException = null;

    try {
        super.validateForDelete()
    } catch (EOValidation.Exception s) {
        superException = s;
    }

    if (!isPaid())
        myException = new EOValidation.Exception(
            "You can't remove an unpaid fee.");

    if (superException && myException) {
        NSMutableArray exceptions = new NSMutableArray();
        exceptions.addObject(superException);
        exceptions.addObject(myException);
        throw

EOValidation.Exception.aggregateExceptionWithExceptions(
                exceptions);
    } else if (superException) {
        throw(superException);
    } else if (myException) {
        throw(myException);
    }
}
```


In Objective-C:

```objc
- (NSException *)validateForDelete
{
    NSException *superException = [super validateForSave];
    NSException *myException = nil;

    if (![self isPaid])
        myException = [NSException
validationExceptionWithFormat:
            @"You can't remove an unpaid fee."];

    if (superException && myException) {
        return [NSException
aggregateExceptionWithExceptions:
            [NSArray arrayWithObjects:
            superException, myException, nil];
    } else if (superException) {
        return superException;
    } else if (myException) {
        return myException)
    }

    return nil;
}
```


The default implementation of __validateForDelete__ inherited by your custom classes performs basic checking based on referential integrity rules specified in your model. Your custom classes should therefore invoke super's implementation before performing their own validation as and should combine any exception thrown by super's implementation with their own as shown above.
Note that the Java and Objective-C validation methods work slightly differently. The Java methods throw exceptions to indicate a validation failure whereas the Objective-C methods create and return exceptions for the Framework to raise.
The advantage of using one of the __validateFor...__ methods is that they allow you to perform both "inter-" and "intra-" object validation before a particular operation occurs. This is useful if you have an enterprise object whose properties have interdependencies. For example, if you're saving rental data, you might want to confirm that the check out date precedes the return date before committing the changes.

### Validating Individual Properties

EOValidation defines a fifth method for validating individual properties: __validateValueForKey__ (__validateValue:forKey:__ in Objective-C). It's like the key-value coding methods in that it validates properties by name (or _key_). The default implementation of __validateValueForKey__ that your custom classes inherit searches for a method of the form __validate__Key and invokes it if it exists. These are the methods that your custom classes can implement to validate individual properties. For example, the Customer class might have a __validateStreetAddress__ method:
In Java:

```
public void validateStreetAddress(String address)
    throws EOValidation.Exception
{
    if (/** address is invalid */)
        throw new EOValidation.Exception("Invalid
address.");
}
```


In Objective-C:

```objc
- (NSException *)validateStreetAddress:(NSString
*)address
{
    if (/* address is invalid...*/)
        return [NSException validationExceptionWithFormat:
            @"Invalid address."];

    return nil;
}
```


If a user tries to assign a value to __streetAddress__, the default implementation of __validateValueForKey__ invokes the __validateStreetAddress__ method. Based on the result, the operation is either accepted or refused.
Prior to invoking your validateKey methods, the default implementation of __validateValueForKey__ validates the property against constraints specified in your model (such as NULL constraints).
Note that the default implementations of __validateForSave__, __validateForInsert__, and __validateForUpdate__ provided by EOCustomObject (NSObject in Objective-C) invoke __validateValueForKey__ for each of an object's class properties.

### Validating User Input

Besides putting validation in a model and in an enterprise object class, you can also put validation in the user interface. The way that validation is normally added to the user interface is through formatters, which perform data type and formatting validation when users enter values.
Additionally, you can design your Application Kit and Java client applications so that the validation in your enterprise objects is performed as soon as a user attempts to leave an editable field in the user interface. There are two steps to doing this:

- In Interface Builder, display the Attributes view of the EODisplayGroup Inspector and check "Validate immediately".
- In your enterprise object class, implement __validate__Propertyto check the value of the key for which the user is entering a value. For example, if the key is __salary__, you'd implement the method __validateSalary__.

If __validateSalary__ fails (that is, if the salary value isn't within acceptable bounds), the user is forced to correct the value before being allowed to leave the field.
Note that in this scenario, __validateValueForKey__ is invoked with values directly from the user interface. When __validateValueForKey__ is invoked from __validateForSave__, __validateForInsert__, or __validateForUpdate__, it's invoked with values that are already in the object.

## Creating and Inserting Objects

In an Enterprise Objects Framework application, when new enterprise objects are inserted into the database, it's often through a display group-either an EODisplayGroup for Application Kit and Java client applications or a WODisplayGroup for WebObjects applications (assuming the application has a graphical user interface). However, it's also common to create and insert an enterprise object programmatically-either because your application doesn't have a graphical user interface, or because you're creating and inserting objects as the by-product of another operation.
To create an instance of a custom Java enterprise object class, you invoke a constructor of the following form:

```
public MyCustomEO (
    EOEditingContext  anEOEditingContext,
    EOClassDescription  anEOClassDescription,
    EOGlobalID  anEOGlobalID)
```


Typically you invoke this constructor with __null__ arguments as follows:

```
rental = new MyCustomEO(null, null, null);
```


You can provide real values, but most enterprise object classes don't make use of the arguments. The only common exception to this is EOGenericRecord, which requires the arguments to identify the object's class description. EOGenericRecord is handled in a different way, as described later in this section.
In Objective-C, you use __alloc__ and __init__ like you would with any other object, so you don't have to worry about providing arguments.
Once you create an object, you insert it into an EOEditingContext using EOEditingContext's __insertObject__ method (__insertObject:__ in Objective-C). For example, the following code excerpts for the Customer class create Fee and Rental enterprise objects as the by-product of a customer renting a unit at a video store. Once the objects have been created, they're inserted into the current enterprise object's EOEditingContext.
In Java:

```
public void rentUnit(Unit unit)
{
    EOEditingContext ec;
    Fee fee;
    Rental rental;

    ec = editingContext();

    // Create new objects and insert them into the editing
context
    fee = new Fee(null, null, null);
    ec.insertObject(fee);
    rental = new Rental(null, null, null);
    ec.insertObject(rental);

    // Manipulate relationships
    rental addObjectToBothSidesOfRelationshipWithKey(fee,
"fees");
    rental.addObjectToBothSidesOfRelationshipWithKey(unit,
"unit");
    addObjectToBothSidesOfRelationshipWithKey(rental,
"rentals");
}
```


In Objective-C:

```objc
- (void)rentUnit:(Unit *)unit
{
    EOEditingContext *ec;
    Fee *fee;
    Rental *rental;

    ec = [self editingContext];

    // Create new objects and insert them into the editing
context
    fee = [[[Fee alloc] init] autorelease];
    [ec insertObject:fee];
    rental = [[[Rental alloc] init] autorelease];
    [ec insertObject:rental];

    [rental addObject:fee
        toBothSidesOfRelationshipWithKey:@"fees"];
    [rental addObject:unit
        toBothSidesOfRelationshipWithKey:@"unit"];

    [self addObject:rental
        toBothSidesOfRelationshipWithKey:@"rentals"];
}
```


EOEditingContext's __insertObject__ method has the effect of registering the specified enterprise object with the editing context. In other words, it registers the object to be inserted in the database the next time the editing context saves changes. Inserting a new object into an editing context also has the side effect of further initializing the object, so you should always insert new objects into an editing context before modifying them (such as by manipulating their relationships). For more information, see the section["Setting Defaults for New Enterprise Objects"](#apple-ha2de).

You create an instances of EOGenericRecord differently from the way you create custom objects: To create a generic record, use EOClassDescription's __createInstanceWithEditingContext__ method (__createInstanceWithEditingContext:globalID:zone:__ in Objective-C) as follows:
In Java:

```
String entityName; // Assume this exists.
EOEditingContext editingContext; // Assume this exists.
EOClassDescription classDescription;
EOEnterpriseObject eo;

classDescription =
EOClassDescription.classDescriptionForEntityName(entityN
ame);

eo = classDescription.createInstanceWithEditingContext(
        editingContext, null);

if (eo) editingContext.insertObject(eo);
```


In Objective-C:

```
NSString *entityName; // Assume this exists.
EOEditingContext *editingContext; // Assume this exists.
EOClassDescription classDescription;
id eo;

classDescription = [EOClassDescription
        classDescriptionForEntityName:entityName];
eo = [classDescription
        createInstanceWithEditingContext:editingContext
        globalID:nil
        zone:[editingContext zone]];

if (eo) [editingContext insertObject:eo];
```


The EOClassDescription method createInstanceWithEditingContext is preferable to using an EOGenericRecord constructor (or to using EOGenericRecord's __init...__ method in Objective-C) because the same code works if you later use a custom enterprise object class instead of EOGenericRecord. Strictly speaking, it's better to use EOClassDescription's __createInstanceWithEditingContext__ for all types of enterprise objects-EOGenericRecords as well as your custom classes. The createInstanceWithEditingContext method is the most general way to create an enterprise object-it works regardless of whether the object is represented by a custom class or an EOGenericRecord.

### Working with Relationships

In the code excerpt shown in the preceding section, notice that before the objects are inserted into the EOEditingContext, the method __addObjectToBothSidesOfRelationshipWithKey__ (__addObject:toBothSidesOfRelationshipWithKey:__ in Objective-C) is used. This method is part of the EORelationshipManipulation interface (informal protocol in Objective-C). EORelationshipManipulation provides methods for manipulating an enterprise object's relationship properties. It is a part of the EOEnterpriseObject interface, and so your custom classes inherit a default implementation from EOCustomObject (or NSObject in Objective-C).
__addObjectToBothSidesOfRelationshipWithKey__ is used to manage reciprocal relationships, in which the destination entity of a relationship has a back reference to the source. For example, Fee and Unit both have back references to Rental, and Rental has a back reference to Customer. In other words, not only does the model define a relationship from Customer to Fee and Rental, it also defines a relationship from Rental back to Customer and from Fee to Rental. When you insert an object into a relationship (such as adding a new Rental object to Customer's __rentals__ relationship property, which is an NSArray) _and_ the inserted object has a back reference to the enterprise object, you need to be sure to add the object to both sides of the relationship. Otherwise, your object graph will get out of sync-your Customer object's __rentals__ array will contain the Rental object, but the Rental object won't know the Customer who rented it.
You can update object references explicitly-that is, you can directly update the Rental object's __customer__ property, which represents its relationship to the Customer object. But it's simpler to just use __addObjectToBothSidesOfRelationshipWithKey__. This method is safe to use regardless of whether the source relationship is to-one or to-many, whether the reciprocal relationship is to-one or to-many, or whether the relationship is reciprocal at all.
You should observe the following guidelines in working with relationships:

- For non-reciprocal relationships, you can just use your class's regular accessor methods. These methods have the form __addTo__Property (__addTo__Property__:__ in Objective-C) where _Property_ is a relationship array.
- When in doubt, use the method __addObjectToBothSidesOfRelationshipWithKey__. This method works for reciprocal and non-reciprocal relationships alike, and it's the safest choice if you don't know ahead of time what objects your code will be working with-for example, if you're providing a framework to be used by others.
- If you're working with reciprocal relationships and you do know the objects you'll be working with ahead of time, the best choice is to implement custom accessor methods in your enterprise object class to handle the reciprocal relationships. Custom accessor methods are preferable to __addObjectToBothSidesOfRelationshipWithKey__ simply because they provide type checking.

In addition to the __addObjectToBothSidesOfRelationshipWithKey__ method, EORelationshipManipulation defines the following methods:

- addObjectToPropertyWithKey
- removeObjectFromPropertyWithKey
- removeObjectFromBothSidesOfRelationshipWithKey

The method __addObjectToPropertyWithKey__ (__addObject:toPropertyWithKey:__ in Objective-C) adds a specified object to the relationship property (an NSArray) with the specified name (key). This method is the primitive used by __addObjectToBothSidesOfRelationshipWithKey__. The default implementation uses the class definition as follows:

- If this method is passed the key __projects__, for example, the default implementation looks for a method with the name __addToProjects__.
- If the __addToProjects__ method isn't found, __addObjectToPropertyWithKey__ looks for a property called __projects__. If it finds it, it adds the argument to the array (assuming the array is mutable). If the array is immutable, it creates a new version of the array that includes the new element.
- If the property is __null__ (__nil__ in Objective-C), a new empty array is created and assigned to the object.

The method __removeObjectFromPropertyWithKey__ (__removeObject:fromPropertyWithKey:__ in Objective-C) removes a specified object from the relationship property (an NSArray) with the specified name (key).
This method follows the same pattern as __addObjectToPropertyWithKey__. That is, it looks for a selector of the form __removeFromProjects__, and then for a property called __projects__. If neither of these can be found, it throws an exception. If it finds the property but it doesn't contain the specified object, this method simply returns.
The method __removeObjectFromBothSidesOfRelationshipWithKey__ (__removeObject:fromBothSidesOfRelationshipWithKey:__ in Objective-C) removes a specified object from both sides of a relationship property with the specified name. Like __addObjectToBothSidesOfRelationshipWithKey__, this method is safe to use regardless of whether the source relationship is to-one or to-many, or whether the reciprocal relationship is to-one or to-many.

## Setting Defaults for New Enterprise Objects

When new objects are created in your application and inserted into the database, it's common to assign default values to some of their properties. For example, the Member class has a __memberSince__ property. It's likely that you would assign that property a value when you create and insert a new object instead of forcing the user to supply a value for it.
To assign default values to newly created enterprise objects, you use the method __awakeFromInsertionInEditingContext__ (__awakeFromInsertionInEditingContext:__ in Objective-C). This method is automatically invoked immediately after your enterprise object class creates a new object and inserts it into the EOEditingContext.
The following implementation of __awakeFromInsertion__ in the Member class sets the current date as the value of the __memberSince__ property:
In Java:

```
public void awakeFromInsertion(EOEditingContext ec)
{
    super.awakeFromInsertion(ec);
    // Assign current date to memberSince
    if (memberSince == null)
        memberSince = new NSGregorianDate();
}
```


In Objective-C:

```objc
- (void)
awakeFromInsertionInEditingContext:(EOEditingContext
*)ec
{
    [super awakeFromInsertionInEditingContext:ec];
    // Assign current date to memberSince
    if (!memberSince)
        memberSince = [[NSCalendarDate date] retain];
}
```


You use the __awakeFromInsertion__ method to set default values for enterprise objects that represent new data. For enterprise objects that represent existing data, the Enterprise Objects Framework provides the method __awakeFromFetch__ (__awakeFromFetchInEditingContext:__ in Objective-C), which is sent to an enterprise object that has just been created from a database row and initialized with database values. Your enterprise objects can implement this method to provide additional initialization. Because the Framework is still busy fetching when an enterprise object receives __awakeFromFetch__, the object must be careful about sending messages to other enterprise objects that might need to be _faulted_ in. For more information about faulting, see the chapter "Behind the Scenes" and the EOFaulting interface specification in the _Enterprise Objects Framework Reference_.

### Initializing Enterprise Objects

Since all of an enterprise object's class property values are assigned through the key-value coding methods, no special initialization is usually needed in your constructors (or __init...__ methods in Objective-C). Specifically, you don't generally assign default values to your enterprise objects in constructors since it is invoked to create instances of your class being fetched from the database. Any values you assign in a constructor will be overwritten by the values fetched from the database.
However you can take advantage of extra information available at the time your enterprise object is initialized. In Java, instances of custom classes must provide a constructor of the following form:

```
public MyCustomEO (
    EOEditingContext  anEOEditingContext,
    EOClassDescription  anEOClassDescription,
    EOGlobalID  anEOGlobalID)
```


The Framework uses such a constructor to create your objects, so you can use the provided arguments to influence the creation. In Objective-C, enterprise objects can be created with either __init__ or __initWithEditingContext:classDescription:globalID:__. If an enterprise object implements the __initWithEditingContext:classDescription:globalID:__ method, the Framework uses this method instead of __init__, allowing the object to affect its creation based on the data provided.

## Writing Business Logic

So far the examples in this chapter have focused on working with your enterprise objects in fairly simple ways: creating them, accessing their data, modifying them, and validating changes before you save them to the database. But enterprise object classes can also implement more sophisticated business logic. For example, suppose you need a pay method in your Fee class that sets the fee's __datePaid__ property and also notifies the fee's rental that the fee has been paid. You could implement this as follows:
In Java:

```
public void pay()
{
    setDatePaid(new NSGregorianDate());

    // Notify the rental that this fee has been paid.
    rental.feePaid();
}
```


In Objective-C:

```objc
- (void)pay
{
    [self setDatePaid:[[NSCalendarDate calendarDate]
retain];

    // Notify the rental that this fee has been paid.
    [rental feePaid];
}
```


When you implement a method such as this in your enterprise object class, you don't have to be concerned with registering the changes or updating the values displayed in the user interface. An Enterprise Objects Framework application revolves around the graph of enterprise objects, and the Framework assumes responsibility for making sure that all parts of your application are notified when an object's value changes. Thus, all parts of your application have the same view of the data and remain in sync.

[!Table of Contents](Designing%20Enterprise%20Objects.md) [!Next Section](Gotchas.md)
