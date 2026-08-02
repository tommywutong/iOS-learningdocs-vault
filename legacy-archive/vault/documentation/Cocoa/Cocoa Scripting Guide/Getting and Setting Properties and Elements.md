---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_get_set/SAppsGetSet.html
archived_at: '2026-07-15T07:18:50.804174Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](Object%20Specifiers.md)[Previous](Preparing%20a%20Scripting%20Definition%20File.md)

# Getting and Setting Properties and Elements

This chapter describes how to work with Cocoa scripting to allow it to get and set the values of properties and elements in your scriptable application. It also provides examples of KVC-compliant accessor methods.

Allowing scripters to get and set values of scriptable objects is an important part of scriptability. In your sdef, you define keys for scriptable properties and elements. In your application, properties are equivalent to attribute and to-one relationships, while elements are represented by to-many relationships.

Cocoa scripting supports getting and setting values through the use of key-value coding (KVC). For your application to work with this support, you must comply with KVC conventions in naming the keys in your sdef file and the corresponding accessor methods (or instance variables) in your scriptable classes:

- In your sdef file, you define keys for the scriptable properties and elements of your scriptable classes, as described in [Provide Keys for Key-Value Coding](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolktk4yq). Cocoa scripting uses these keys when it invokes KVC to get and set values.
- In your application code, accessors (or instance variables) for scriptable properties and elements must match the keys specified in your sdef file and the naming conventions described in [Maintain KVC Compliance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona).

In handling `get` and `set` scripting commands, Cocoa scripting takes care of the following automatically:

- It provides the `NSGetCommand` and `NSSetCommand` classes and automatically instantiates the appropriate object when your application receives a `get` or `set` Apple event. You rarely need to subclass these classes.
- It automatically invokes key-value coding (KVC) methods to get or set values when a `get` or `set` command is executed—your application doesn't need to call KVC methods directly.

For a description of how Cocoa scripting and an application work together to perform a `set` command, see [A Real World Scripting Example](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfuytcnbzhaydm).

When Cocoa scripting uses KVC to get and set values, it calls one of several KVC methods, depending on the type of relationship involved (properties or elements) and on whether the operation is a get or a set. These include two primitive instance methods of the [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) class: `valueForKey:` and `setValue:forKey:`. These methods are used primarily in dealing with properties, though they can also handle element collections in a simple but potentially inefficient way. For more efficient handling of collections, KVC invokes `mutableArrayValueForKey:`.

These KVC methods in turn search your method list for specific methods in a specific order, as described in _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_. Templates for the methods KVC looks for are described in [Maintain KVC Compliance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona).

Your application doesn't invoke or override KVC methods—it just names its accessor methods or instance variables so that KVC can find them.

For Cocoa scripting to work successfully with KVC, every scriptable class in your application must be KVC-compliant for every key corresponding to its scriptable properties and elements. To ensure this, you must define keys in your sdef file as described in [Provide Keys for Key-Value Coding](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolktk4yq), and you must adhere to the following naming conventions for your accessor methods or instance variables (where you replace <key> or <Key> with the key string to construct the actual method name):

- For properties (attributes and to-one relationships), you implement `<key>` and, if the property is not read-only, `set<Key>:` accessors.
- For element classes (to-many relationships), you implement `<key>` and, if the element class is not read-only, `insertObject:in<Key>AtIndex:` and `removeObjectFrom<Key>AtIndex:` methods. For better performance, you may also need to implement `replaceObjectIn<Key>AtIndex:withObject:`.

  If there is no way to efficiently implement `<key>` (for example, if the value of the to-many relationship is not naturally stored in an instance of `NSArray`), you can instead implement `countOf<Key>` and `objectIn<Key>AtIndex:`. KVC's `valueForKey:` and `mutableArrayValueForKey:`, which are invoked by Cocoa scripting, will return collection proxies that invoke your methods when appropriate.
- To let Cocoa automatically create an array proxy to handle element collections, you can implement `countOf<Key>` and `objectIn<Key>AtIndex:` methods.

  If the to-many relationship is mutable, you should also implement `insertObject:in<Key>AtIndex:` and `removeObjectFrom<Key>AtIndex:` methods.

  And for better performance, you may need to implement `replaceObjectIn<Key>AtIndex:withObject:`.

  KVC invokes these methods regardless of the class used to model the relationship, so you can use array-based or non-array-based collections, including custom collections you have defined. But it's up to you to implement the methods to work with your underlying data. The code should be quite straightforward; if you are working with arrays, it often requires just a call to an array method that corresponds to the accessor method.
- As an alternative to implementing accessor methods, you can take advantage of KVC's direct instance variable access feature. You do this by merely giving an instance variable a name that matches a key defined in your sdef, with an optional leading underscore—for example, `xPosition` or `_xPosition`,

  Instance variables corresponding to writable element classes must be of type `NSMutableArray` if you do not implement the `insertObject:in<Key>AtIndex:` and `removeObjectFrom<Key>AtIndex:` methods.
- For element classes that can be accessed by name or ID (that is, the class has properties identified by the four character code `'pnam'` or `'ID '`), you can optimize the evaluation of name and ID specifiers by implementing the methods `valueIn<Key>WithName:` or `valueIn<Key>WithUniqueID:`, respectively.

If you follow standard Cocoa naming conventions for accessors, you're already on the way to KVC compliance:

- A “get” accessor should start with a lower case letter and have the same name as the variable it is accessing—for example, `xPosition`.
- A “set” accessor should start with “set”, followed by the name of the variable, with the first letter capitalized—for example, `setXPosition`.

For examples of KVC-compliant accessor methods based on the templates described here, see [Sample KVC-Compliant Accessor Methods](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvomq).

The use of accessor methods supports data encapsulation, a standard coding practice. However, in cases where you are providing KVC access to your data solely to support scriptability (or Cocoa bindings), encapsulation may be less important, and you might choose to omit accessor methods altogether. If so, you need only maintain KVC compliance in naming your instance variables to match the keys in your sdef.

You might also choose to use direct instance variable access as a convenience during prototyping or feasibility testing, then add accessor methods later in the development cycle.

KVC access to simple values is fast enough that it should not be a performance bottleneck. In general, KVC is smart enough to search for the most efficient methods your classes provide that match the KVC naming conventions. For example, for to-many relationships, KVC looks first for collection mutation methods, then for setter methods; if neither is available, it tries for direct instance variable access.

[Maintain KVC Compliance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona) describes the collection methods you should implement for best performance (`insertObject:in<Key>AtIndex:` and `removeObjectFrom<Key>AtIndex:`).

You can instead merely implement a setter method (as in, `set<Key>:`) and KVC will invoke it, but be aware of what KVC, as used by Cocoa Scripting, must do in that case: for an insertion or removal, it must get the value array, make a mutable copy of it, mutate the copy, and then set it again. This can be slow.

Because Cocoa scripting invokes `setValue:forKey:` instead of `takeValue:forKey:` (a deprecated KVC method), changes to model objects made by AppleScript scripts are observable using automatic key-value observing. However, if the container in question overrides `takeValue:forKey:`, Cocoa scripting invokes `takeValue:forKey:` for backward binary compatibility.

Cocoa scripting does not depend on KVO. However, if your application uses Cocoa bindings, you should follow the guidelines described in _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_. For related information in this document, see [Interaction With Cocoa Bindings and Core Data](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfvjvomjt).

The default implementations of the KVC methods `valueForKey:` and `setValue:forKey:` provide support for automatic object wrapping of scalar data types such as `BOOL`, `char`, `double`, `float`, `int`, and structures such as `NSPoint`, `NSRange`, and `NSRect`. When Cocoa scripting invokes `valueForKey:` to get a value, KVC automatically converts the value to an `NSNumber` object (for scalars) or `NSValue` object (for structures) if necessary.

Similarly, `setValue:forKey:` determines the data type required by the appropriate accessor or instance variable for the specified key. If the data type is not an object, then the value is extracted from the passed object using the appropriate `NSNumber` or`NSValue` method.

For more information, including a table of the supported types, see [Scalar and Structure Support](../Key-Value%20Coding%20Programming%20Guide/DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tc) in _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_.

Cocoa defines the category `NSScriptKeyValueCoding` to provide scripting-related additions to the key-value coding methods implemented in `NSObject`. The methods in this category on `NSObject` provide additional capabilities for working with key-value coding, including getting and setting key values by index in a collection and coercing (or converting) a key value. Additional methods allow the implementer of a scriptable container class to provide fast access to elements that are referenced by name and unique ID.

Suppose you have a `DrawingCanvas` class that you want to make scriptable. In a simple scenario, you want scripts to be able to access the properties of graphical shapes associated with a canvas object, and you also want scripts to be able to access a boolean value indicating whether the canvas has been modified. Assume that scripters can get and set properties of a shape, but can only read the current value of the modified property.

First, you specify the keys `"shape"` and `"modified"` in the scriptability information for your application. To do this, you could define the following entries in the `class` definition for the `drawing canvas` scriptable object class in your sdef file:

```
    <property name="modified" code="iMod" type="boolean" access="ro"
        description="Has the canvas been modified since the last save?">
    </property>
    <element type="shape">
```

The two keys also become instance variables of the `DrawingCanvas` class. Remember that Cocoa scripting pluralizes the key for an element, as shown in the declared array variable, `shapes`. However, the instance variable names don't have to match the keys if you provide complete KVC-compliant method coverage.

```objc
@interface DrawingCanvas: NSObject <NSCoding> {
    NSMutableArray *shapes; // An array of shape objects
    BOOL modified; // Whether the canvas has been modified
    // ...
```

The following sections provide sample accessors for these properties, based on the KVC accessor method templates described in [Maintain KVC Compliance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona). Depending on the implementation, some examples might require additional application-dependent code that is not shown here.

To provide scriptable access to the boolean property of the `DrawingCanvas` class, based on the key `"modified"`, you can define a KVC-compliant getter method like the following:

__Listing 5-1__  Boolean property getter

```objc
- (BOOL)modified
{
    // If necessary, obtain or update value
    return modified;
}
```

If the `modified` property were settable (if the property were defined as read/write, the default), you could define a KVC-compliant setter method like the following:

__Listing 5-2__  Boolean property setter

```objc
- (void)setModified:(BOOL)flag
{
    modified = flag;
}
```

As noted in [On Omitting KVC Accessors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvonq), in cases where you are providing KVC access to your data solely to support scriptability, you might choose to omit accessor methods. If so, you need only name your instance variables to match the keys in your sdef—in this case, `modified` or `_modified`.

For simple scriptable access to a to-many relationship, you can implement accessor methods like those in Listing 5-3. However, the setter method may not be efficient, for reasons described in [Performance Considerations With KVC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvony).

__Listing 5-3__  Simple array element accessors

```objc
- (NSArray *)shapes
{
    return [[shapes retain]autorelease];
}
- (void)setShapes:(NSArray *)newShapes
{
    if (shapes != newShapes)
    {
        [shapes release];
        shapes = [newShapes copy];
    }
}
```

You can support KVC access for to-many relationships by implementing indexed accessor methods. These accessors work whether or not the related objects are stored in an array—Cocoa automatically creates an array proxy for you if needed.

For best performance, you should implement the two KVC-compliant methods shown in the next listing, instead of the `setShapes:` method:

__Listing 5-4__  Array element insert/delete accessors (by index)

```objc
-(void)insertObject:(id)anObject inShapesAtIndex:(unsigned)index
{
    [shapes insertObject:anObject atIndex:index];
}

-(void)removeObjectFromShapesAtIndex:(unsigned)index
{
    [shapes removeObjectAtIndex:index];
}
```

And finally, to provide even more efficient mutation of the array, you can also implement a KVC-compliant method like the following:

__Listing 5-5__  Array element replacement accessor (by index)

```objc
-(void)replaceObjectInShapesAtIndex:(unsigned)index withObject:(id)anObject
{
    // possible implementation-specific code
    [shapes replaceObjectAtIndex:index withObject:anObject];
}
```


Sometimes an accessor method must do something special to support scripting. For example, consider the documents managed by a document-based application. When a script asks for an application’s documents, the application could invoke the `documents` method of the `NSDocumentController` object to obtain all currently opened documents, ordered by creation.

However, this is not what is expected by the scripter. AppleScript has the notion of a `first document` and a `last document` (as well as `front document`, `document 1`, and related notations), and this implies an ordering of documents visible on the screen. The `NSApplication` class therefore implements the `orderedDocuments` method, which, in response to a request for its documents, returns an array of document objects, where the position of a document in the array is based on the front to back ordering of its associated (on-screen) window.

Sometimes an application's object model provides scripting access to objects at a level of granularity that would be impractical to implement with individual objects. For example, an AppleScript script can ask for the `characters` of a text document, but it would be quite expensive for an application to represent each character as an object. The `NSTextStorage` class handles this case with a special accessor method, `characters`

It is common for good scriptable applications to make the complete set of properties for each scriptable object available in the form of a single record that is the value of the `properties` property. A category on `NSObject` (defined in the Foundation file `NSObjectScripting.h`) declares the following public KVC accessor methods for this property:

```objc
- (NSDictionary *)scriptingProperties;
- (void)setScriptingProperties:(NSDictionary *)properties;
```

For all scriptable classes that inherit from `item`, Cocoa scripting provides automatic scriptability support for the `properties` property. So if your scriptable classes that descend from `NSObject` provide KVC-compliant accessors for their individual scriptable properties and elements, you will automatically have support for the `properties` property.

Coercion is the process of converting data from one type to another. AppleScript provides many default (or built-in) coercions. For example, when it executes the statement `set theValue to "20.05" as number`, AppleScript converts the string `"20.05"` to the numeric value `20.05`.

Cocoa scripting supports the types shown in [Built-in Support for Basic AppleScript Types](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfvjvomjs), and makes use of the default coercions as needed when it handles Apple events received by a Cocoa application. For information on the default coercions, see [Default Coercion Handlers](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/appendix3_aepg/appendix3_aepg.html#//apple_ref/doc/uid/TP40001449-CH213) in _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

[Next](Object%20Specifiers.md)[Previous](Preparing%20a%20Scripting%20Definition%20File.md)

