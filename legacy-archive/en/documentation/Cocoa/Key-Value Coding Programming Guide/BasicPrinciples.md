---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html
archived_at: '2026-07-15T07:16:11.064656Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Accessing Object Properties

An object typically specifies _properties_ in its interface declaration, and these properties belong to one of several categories:

- __Attributes.__ These are simple values, such as a scalars, strings, or Boolean values. Value objects such as `NSNumber` and other immutable types such as as `NSColor` are also considered attributes.
- __To-one relationships.__ These are mutable objects with properties of their own. An object’s properties can change without the object itself changing. For example, a bank account object might have an owner property that is an instance of a `Person` object, which itself has an address property. The owner’s address may change without changing the owner reference held by the bank account. The bank account’s owner did not change. Only her address did.
- __To-many relationships.__ These are collection objects. You commonly use an instance of `NSArray` or `NSSet` to hold such a collection, although custom collection classes are also possible.

The `BankAccount` object declared in Listing 2-1 demonstrates one of each type of property.

__Listing 2-1__Properties of the `BankAccount` object

1. `@interface BankAccount : NSObject`
3. `@property (nonatomic) NSNumber* currentBalance; // An attribute`
4. `@property (nonatomic) Person* owner; // A to-one relation`
5. `@property (nonatomic) NSArray< Transaction* >* transactions; // A to-many relation`
7. `@end`

In order to maintain encapsulation, an object typically provides accessor methods for the properties on its interface. The object’s author may write these methods explicitly or may rely on the compiler to synthesize them automatically. Either way, the author of code using one of these accessors must write the property name into the code before compiling it. The name of the accessor method becomes a static part of the code that is using it. For example, given the bank account object declared in Listing 2-1, the compiler synthesizes a setter that you can invoke for the `myAccount` instance:

1. `[myAccount setCurrentBalance:@(100.0)];`

This is direct, but lacks flexibility. A key-value coding compliant object, on the other hand, offers a more general mechanism to access an object’s properties using string identifiers.

### Identifying an Object’s Properties with Keys and Key Paths

A _key_ is a string that identifies a specific property. Typically, by convention, the key representing a property is the name of the property itself as it appears in code. Keys must use ASCII encoding, may not contain whitespace, and usually begin with a lowercase letter (though there are exceptions, such as the `URL` property found in many classes).

Because the `BankAccount` class in Listing 2-1 is key-value coding compliant, it recognizes the keys `owner`, `currentBalance`, and `transactions`, which are the names of its properties. Instead of calling the `setCurrentBalance:` method, you can set the value by its key:

1. `[myAccount setValue:@(100.0) forKey:@"currentBalance"];`

In fact, you can set all the properties of the `myAccount` object with the same method, using different key parameters. Because the parameter is a string, it can be a variable that is manipulated at run-time.

A _key path_ is a string of dot-separated keys used to specify a sequence of object properties to traverse. The property of the first key in the sequence is relative to the receiver, and each subsequent key is evaluated relative to the value of the previous property. Key paths are useful for drilling down into a hierarchy of objects with a single method call.

For example, the key path `owner.address.street` applied to a bank account instance refers to the value of the street string that is stored in the address of the bank account’s owner, assuming the `Person` and `Address` classes are also key-value coding compliant.

> [!NOTE]
> 

### Getting Attribute Values Using Keys

An object is key-value coding compliant when it adopts the `NSKeyValueCoding` protocol. An object that inherits from [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject), which provides a default implementation of the protocol’s essential methods, automatically adopts this protocol with certain default behaviors. Such an object implements at least the following basic key-based getters:

- [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) - Returns the value of a property named by the key parameter. If the property named by the key cannot be found according to the rules described in [Accessor Search Patterns](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq), then the object sends itself a [valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value) message. The default implementation of [valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value) raises an `NSUndefinedKeyException`, but subclasses may override this behavior and handle the situation more gracefully.
- [valueForKeyPath:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKeyPath:) - Returns the value for the specified key path relative to the receiver. Any object in the key path sequence that is not key-value coding compliant for a particular key—that is, for which the default implementation of `valueForKey:` cannot find an accessor method—receives a [valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value) message.
- [dictionaryWithValuesForKeys:](https://developer.apple.com/documentation/objectivec/nsobject/1411319-dictionarywithvalues) - Returns the values for an array of keys relative to the receiver. The method calls `valueForKey:` for each key in the array. The returned `NSDictionary` contains values for all the keys in the array.

> [!NOTE]
> 

When you use a key path to address a property, if any but the final key in the key path is a to-many relationship (that is, it references a collection), the returned value is a collection containing all the values for the keys to the right of the to-many key. For example, requesting the value of the key path `transactions.payee` returns an array containing all the `payee` objects for all the transactions. This also works for multiple arrays in the key path. The key path `accounts.transactions.payee` returns an array with all the payee objects for all the transactions in all the accounts.

### Setting Attribute Values Using Keys

As with getters, key-value coding compliant objects also provide a small group of generalized setters with default behavior based upon the implementation of the `NSKeyValueCoding` protocol found in [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject):

- [setValue:forKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415969-setvalue) - Sets the value of the specified key relative to the object receiving the message to the given value. The default implementation of `setValue:forKey:` automatically unwraps `NSNumber` and `NSValue` objects that represent scalars and structs and assigns them to the property. See [Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq) for details on the wrapping and unwrapping semantics.

  If the specified key corresponds to a property that the object receiving the setter call does not have, the object sends itself a [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) message. The default implementation of `setValue:forUndefinedKey:` raises an `NSUndefinedKeyException`. However, subclasses may override this method to handle the request in a custom manner.
- [setValue:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1418139-setvalue) - Sets the given value at the specified key path relative to the receiver. Any object in the key path sequence that is not key-value coding compliant for a particular key receives a [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) message.
- [setValuesForKeysWithDictionary:](https://developer.apple.com/documentation/objectivec/nsobject/1417515-setvaluesforkeyswithdictionary) - Sets the properties of the receiver with the values in the specified dictionary, using the dictionary keys to identify the properties. The default implementation invokes `setValue:forKey:` for each key-value pair, substituting `nil` for `NSNull` objects as required.

In the default implementation, when you attempt to set a non-object property to a `nil` value, the key-value coding compliant object sends itself a [setNilValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415174-setnilvalueforkey) message. The default implementation of `setNilValueForKey:` raises an [NSInvalidArgumentException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSInvalidArgumentException), but an object may override this behavior to substitute a default value or a marker value instead, as described in [Handling Non-Object Values](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq).

### Using Keys to Simplify Object Access

To see how key-based getters and setters can simplify your code, consider the following example. In macOS, [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) and [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview) objects associate an identifier string with each of their columns. If the model object backing the table is not key-value coding compliant, the table’s data source method is forced to examine each column identifier in turn to find the correct property to return, as shown in Listing 2-2. Further, in the future, when you add another property to your model, in this case the `Person` object, you must also revisit the data source method, adding another condition to test for the new property and return the relevant value.

__Listing 2-2__Implementation of data source method without key-value coding

1. `- (id)tableView:(NSTableView *)tableview objectValueForTableColumn:(id)column row:(NSInteger)row`
2. `{`
3. `id result = nil;`
4. `Person *person = [self.people objectAtIndex:row];`
6. `if ([[column identifier] isEqualToString:@"name"]) {`
7. `result = [person name];`
8. `} else if ([[column identifier] isEqualToString:@"age"]) {`
9. `result = @([person age]); // Wrap age, a scalar, as an NSNumber`
10. `} else if ([[column identifier] isEqualToString:@"favoriteColor"]) {`
11. `result = [person favoriteColor];`
12. `} // And so on...`
14. `return result;`
15. `}`

On the other hand, Listing 2-3 shows a much more compact implementation of the same data source method that takes advantage of a key-value coding compliant `Person` object. Using only the [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) getter, the data source method returns the appropriate value using the column identifier as a key. In addition to being shorter, it is also more general, because it continues to work unchanged when new columns are added later, as long as the column identifiers always match the model object’s property names.

__Listing 2-3__Implementation of data source method with key-value coding

1. `- (id)tableView:(NSTableView *)tableview objectValueForTableColumn:(id)column row:(NSInteger)row`
2. `{`
3. `return [[self.people objectAtIndex:row] valueForKey:[column identifier]];`
4. `}`

[About Key-Value Coding](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydolktk4yq)

[Accessing Collection Properties](AccessingCollectionProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedilktk4yq)
