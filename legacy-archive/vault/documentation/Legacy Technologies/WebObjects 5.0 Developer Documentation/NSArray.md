---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSArray.html
archived_at: '2026-07-15T08:13:55.565986Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSArray

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable: java.io.Serializable: NSCoding: NSKeyValueCoding: NSKeyValueCodingAdditions

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSArray and its subclass NSMutableArray manage collections of objects called arrays. NSArray creates static arrays and NSMutableArray creates dynamic arrays.

[Table 0-1](#apple-ijbuqskkincec) describes the NSArray methods that provide the basis for all NSArray's other methods; that is, all other methods are implemented in terms of these three. If you create a subclass of NSArray, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-1 NSArray's Base API__

| __Method__ | __Description__ |
| [count](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rw65looq) | Returns the number of elements in the array. |
| [objectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2ec5cjnzsgk6a) | Provides access to the array elements by index. |
| [objectsNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2hgttpinxxa6i) | Returns a natural language array containing the NSArray's objects. |

The methods [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2ek3tvnvsxeylun5za) and [reverseObjectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zgk5tfojzwkt3cnjswg5cfnz2w2zlsmf2g64q) grant sequential access to the elements of the array, differing only in the direction of travel through the elements. These methods are provided so that arrays can be traversed in a manner similar to that used for objects of other collection classes in both the Java API and the Foundation Kit, such as java.util.Hashtable or NSDictionary. See the __objectEnumerator__ method description for a code excerpt that shows how to use these methods to access the elements of an array.

NSArray provides methods for querying the elements of the array. [indexOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw4zdfpbhwmt3cnjswg5a) searches the array for the object that matches its argument. To determine whether the search is successful, each element of the array is sent an __equals__ message. Another method, [indexOfIdenticalObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw4zdfpbhwmslemvxhi2ldmfwe6ytkmvrxi), is provided for the less common case of determining whether a specific object is present in the array. __indexOfIdenticalObject__ tests each element in the array to see its the exact same instance as the argument.

To act on the array as a whole, a variety of other methods are defined. You can extract a subset of the array ( [subarrayWithRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zxkytbojzgc6kxnf2gqutbnztwk)) or concatenate the elements of an array of Strings into a single string ( [componentsJoinedByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rw63lqn5xgk3tuonfg62lomvsee6ktorzgs3th)). In addition, you can compare two arrays using the [isEqualToArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uxgrlrovqwyvdpifzheylz) and [firstObjectCommonWithArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5tgs4ttorhwe2tfmn2eg33nnvxw4v3joruec4tsmf4q) methods. Finally, you can create new arrays that contain the objects in an existing array and one or more additional objects with [arrayByAddingObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5qxe4tbpfbhsqlemruw4z2pmjvgky3u) and [arrayByAddingObjectsFromArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5qxe4tbpfbhsqlemruw4z2pmjvgky3uondhe33nifzheylz).

## Operators

An NSArray works with [NSArray.Operator](NSArray.Operator.md#apple-ijbukssjjjaus)s to perform operations on the array's elements. By default, an array has operators defined for the following keys:

|  |  |
| --- | --- |
| __Key__ | __Operator Description__ |
| `count` | Returns the number of elements in an array. |
| `max` | Returns the element in the array with the highest value. |
| `min` | Returns the element in the array with the lowest value. |
| `avg` | Returns the average of the array's elements' values. |
| `sum` | Returns the sum of the array's element's values. |

To compute an operation on an array's elements, you use key-value coding methods with a specially formatted key. The character "@" introduces the name of the operator you want to perform. For example, to compute the average salary of an array's elements, you could use the method [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf53gc3dvmvdg64slmv4vayluna) with "@avg.salary" as the key path. For more information, see the [NSArray.Operator](NSArray.Operator.md#apple-ijbukssjjjaus) interface specification.

If you write your own operator class, you can make it available for use with NSArrays with the method [setOperatorForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3tmv2e64dfojqxi33sizxxes3fpe). The [operatorNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3pobsxeylun5ze4ylnmvzq) method returns the keys for the operators that NSArray knows about, and [operatorForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3pobsxeylun5zem33sjnsxs) returns the operator for a specified key.

## Constants

---

NSArray defines the following constants:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| AverageOperatorName | `String` | A key representing the operator (an [NSArray.Operator](NSArray.Operator.md#apple-ijbukssjjjaus)) that computes the average of the elements in an array. |
| CountOperatorName | `String` | A key representing the operator (an [NSArray.Operator](NSArray.Operator.md#apple-ijbukssjjjaus)) that computes the number of elements in an array. |
| NotFound | `int` | Returned in the place of an index when an object is not found in an array. For example, [indexOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw4zdfpbhwmt3cnjswg5a) returns `NotFound` if none of the receiver's objects are equal to the specified object. |
| MaximumOperatorName | `String` | A key representing the operator (an [NSArray.Operator](NSArray.Operator.md#apple-ijbukssjjjaus)) that computes the largest element in an array. |
| MinimumOperatorName | `String` | A key representing the operator (an [NSArray.Operator](NSArray.Operator.md#apple-ijbukssjjjaus)) that computes the smallest element in an array. |
| EmptyArray | `NSArray` | An empty array, which can be shared to save memory. |
| SumOperatorName | `String` | A key representing the operator (an [NSArray.Operator](NSArray.Operator.md#apple-ijbukssjjjaus)) that computes the sum of the elements in an array. |

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rwy33omu)
>
> :
>
> : java.io.Serializable:
>
> : NSCoding
>
> : [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3emvrw6zdfj5rguzldoq): [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rwyyltondg64sdn5sgk4q): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5sw4y3pmrsvo2lunbbw6zdfoi)
>
> :
>
> : NSKeyValueCoding
>
> : [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf52gc23fkzqwy5lfizxxes3fpe): [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf53gc3dvmvdg64slmv4q)
>
> :
>
> : NSKeyValueCodingAdditions
>
> : [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf52gc23fkzqwy5lfizxxes3fpfigc5di): [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf53gc3dvmvdg64slmv4vayluna)
>
> :

## Method Types

---

> **Creating arrays**
>
> : [NSArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5hfgqlsojqxs): [immutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw23lvorqwe3dfinwg63tf): [mutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5wxk5dbmjwgkq3mn5xgk): [arrayByAddingObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5qxe4tbpfbhsqlemruw4z2pmjvgky3u): [arrayByAddingObjectsFromArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5qxe4tbpfbhsqlemruw4z2pmjvgky3uondhe33nifzheylz): [sortedArrayUsingComparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zw64tumvsec4tsmf4vk43jnztug33nobqxeylun5za): [subarrayWithRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zxkytbojzgc6kxnf2gqutbnztwk)
>
> **Querying the array**
>
> : [containsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rw63tumfuw442pmjvgky3u): [count](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rw65looq): [getObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5twk5cpmjvgky3uom): [indexOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw4zdfpbhwmt3cnjswg5a): [indexOfIdenticalObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw4zdfpbhwmslemvxhi2ldmfwe6ytkmvrxi): [lastObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5wgc43uj5rguzldoq): [objectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2ec5cjnzsgk6a): [objects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2hg): [objectsNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2hgttpinxxa6i): [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2ek3tvnvsxeylun5za): [reverseObjectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zgk5tfojzwkt3cnjswg5cfnz2w2zlsmf2g64q): [vector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf53gky3un5za)
>
> **Comparing arrays**
>
> : [firstObjectCommonWithArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5tgs4ttorhwe2tfmn2eg33nnvxw4v3joruec4tsmf4q): [isEqualToArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uxgrlrovqwyvdpifzheylz)
>
> **Working with string elements**
>
> : [componentsJoinedByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rw63lqn5xgk3tuonfg62lomvsee6ktorzgs3th): [componentsSeparatedByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3dn5wxa33omvxhi42tmvygc4tborswiqtzkn2he2lom4)
>
> **Operations**
>
> : [operatorForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3pobsxeylun5zem33sjnsxs): [operatorNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3pobsxeylun5ze4ylnmvzq): [setOperatorForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3tmv2e64dfojqxi33sizxxes3fpe): [removeOperatorForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3smvww65tfj5ygk4tborxxertpojfwk6i)
>
> **Methods inherited from Object**
>
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5sxc5lbnrzq): [hashCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5ugc43iinxwizi): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf52g6u3uojuw4zy)
>
> **Sending messages to elements**
>
> : [makeObjectsPerformSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5wwc23fj5rguzldorzvazlsmzxxe3ktmvwgky3un5za)

## Constructors

---

### NSArray

`public NSArray()`

Creates an empty, immutable array. After an immutable array has been initialized in this way, it can't be modified. If you need an empty, immutable array, use [EmptyArray](#apple-ijaucrccirbuo) instead. This method is used by mutable subclasses of NSArray.

`public NSArray(NSArray anArray)`

Creates an array containing the objects in _anArray_. After an immutable array has been initialized in this way, it can't be modified.

`public NSArray(Object anObject)`

Creates an array containing the single element _anObject_. After an immutable array has been initialized in this way, it can't be modified. Throws an IllegalArgumentException if _anObject_ is null.

`public NSArray(Object[] objects)`

Creates an array containing _objects_. Ignores any `null` values it encounters in _objects_. After an immutable array has been initialized in this way, it can't be modified.

`public NSArray( Object[] objects, NSRange aRange)`

Creates an array containing the objects from _objects_ in the range specified by _aRange_. Ignores any `null` values it encounters in _objects_. After an immutable array has been initialized in this way, it can't be modified.

`public NSArray( java.util.Vector aVector, NSRange aRange, boolean checkForNull)`

Creates an array containing the objects from _aVector_ in the range specified by _aRange_. After an immutable array has been initialized in this way, it can't be modified. The _checkForNull_ argument controls the method's behavior when it encounters a `null` value in the vector: if _checkForNull_ is `true`, the `null` value is simply ignored. If _checkForNull_ is false, the method raises an IllegalArgumentException.

---

## Static Methods

---

### componentsSeparatedByString

`public static NSArray componentsSeparatedByString( String string, String separator)`

Returns an array containing substrings from _string_ that have been divided by _separator_. The substrings in the array appear in the order they did in the receiver. If the string begins or ends with the separator, the first or last substring, respectively, is empty. For example, this code excerpt:
> ```
> String list = "wrenches, hammers, saws";
> NSArray listItems = NSArray.componentsSeparatedByString (", ");
> ```

produces an array with these contents:

|  |  |
| --- | --- |
| __Index__ | __Substring__ |
| 0 | wrenches |
| 1 | hammers |
| 2 | saws |

If _list_ begins with a comma and space the array has these contents:

|  |  |
| --- | --- |
| __Index__ | __Substring__ |
| 0 | (empty string) |
| 1 | wrenches |
| 2 | hammers |
| 3 | saws |

If _list_ has no separators-for example, "wrenches"-the array contains the string itself, in this case "wrenches".

__See Also:__ [componentsJoinedByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rw63lqn5xgk3tuonfg62lomvsee6ktorzgs3th)

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates and returns an NSArray from the data in _coder._

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq) Interface Description

---

### operatorForKey

`public static NSArray.Operator operatorForKey(String operatorName)`

Returns the operator for the operator named _operatorName_.

__See Also:__ ["Operators" (page 4)](#apple-ijbuqqsgivcuo)

---

### operatorNames

`public static NSArray operatorNames()`

Returns the names of the operations that can be performed on array elements. By default the operations are `count`, `max`, `min`, `avg`, and `sum`.

__See Also:__ ["Operators" (page 4)](#apple-ijbuqqsgivcuo)

---

### removeOperatorForKey

`public static void removeOperatorForKey(String operatorName)`

Removes the operator identified by _operatorName_ from the list of operators that can be performed on array elements.

__See Also:__ ["Operators" (page 4)](#apple-ijbuqqsgivcuo)

---

### setOperatorForKey

`public static void setOperatorForKey( String key, NSArray.Operator operator)`

Sets the operator for _key_ to _operator_. Throws an IllegalArgumentException if either _key_ or _operator_ are null.

__See Also:__ ["Operators" (page 4)](#apple-ijbuqqsgivcuo)

---

## Instance Methods

---

### arrayByAddingObject

`public NSArray arrayByAddingObject(Object anObject)`

Returns a new array that is a copy of the receiver with _anObject_ added to the end. If _anObject_ is `null`, an IllegalArgumentException is thrown.

__See Also:__ [addObject](NSMutableArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6ylemrhwe2tfmn2a) (NSMutableArray)

---

### arrayByAddingObjectsFromArray

`public NSArray arrayByAddingObjectsFromArray(NSArray otherArray)`

Returns a new array that is a copy of the receiver with the objects contained in _otherArray_ added to the end.

__See Also:__ [addObjectsFromArray](NSMutableArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6ylemrhwe2tfmn2hgrtsn5wuc4tsmf4q) (NSMutableArray)

---

### classForCoder

`public Class classForCoder()`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). NSArray's implementation returns the class NSArray, so subclasses that don't override this method (such as [NSMutableArray](NSMutableArray.md#apple-ineeoq2gi5eeq)) are encoded as instances of NSArray.

__See Also:__ [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) (NSCoding)

---

### clone

`public Object clone()`

Simply returns the receiver. Since NSArrays are immutable, there's no need to make an actual clone.

---

### componentsJoinedByString

`public String componentsJoinedByString(String separator)`

Constructs and returns a String that is the result of interposing _separator_ between the elements of the receiver's array. For example, this code excerpt writes the path `System/Developer` to the console:
> ```
> NSArray pathArray = new NSArray(new Object[] {'System', 'Developer'});
> System.out.println('The path is '+ pathArray.componentsJoinedByString('/') + '.');
> ```

Each element in the receiver's array must handle either __description__, or if it is not implemented, __toString__. If the receiver has no elements, a String representing the empty string is returned.

__See Also:__ [componentsSeparatedByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqlsojqxsl3dn5wxa33omvxhi42tmvygc4tborswiqtzkn2he2lom4)

---

### containsObject

`public boolean containsObject(Object anObject)`

Returns true if the receiver contains an object equal to _anObject_. This method determines whether an object is present in the array by sending an __equals__ message to each of the array's objects (and passing _anObject_ as the parameter to each __equals__ message).

---

### count

`public int count()`

Returns the number of objects currently in the array.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description for [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the NSCoding interface specification.

---

### equals

`public boolean equals(Object anObject)`

Returns `true` if anObject is an NSArray and its contents are equal to the receiver's or `false` otherwise. If you know that _anObject_ is an NSArray, use the more efficient method [isEqualToArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uxgrlrovqwyvdpifzheylz) instead.

---

### firstObjectCommonWithArray

`public Object firstObjectCommonWithArray(NSArray otherArray)`

Returns the first object contained in the receiver that's equal to an object in _otherArray_, or `null` if no such object is found. This method uses __equals__ to check for object equality.

---

### getObjects

`public void getObjects(Object[] buffer[])`

Deprecated. Use __public Object[] objects()__ instead.

`public void getObjects( Object[] buffer[], NSRange aRange)`

Deprecated. Use __public Object[] objects(NSRange)__ instead.

---

### hashCode

`public int hashCode()`

See the method description for __hashCode__ in the Object class specification.

---

### immutableClone

`public NSArray immutableClone()`

Returns an immutable copy of the receiver. Since an NSArray is immutable, NSArray's implementation simply returns the receiver. Subclasses such as [NSMutableArray](NSMutableArray.md#apple-ineeoq2gi5eeq) should override this method to create an immutable copy of the reciever.

---

### indexOfIdenticalObject

`public int indexOfIdenticalObject(Object anObject)`

Searches all objects in the receiver for _anObject_ (testing for equality by comparing object addresses) and returns the lowest index whose corresponding array value is identical to _anObject_. If none of the objects in the receiver are identical to _anObject_, this method returns [NotFound](#apple-ijaucq2ei5bek).

`public int indexOfIdenticalObject( Object anObject, NSRange aRange)`

Searches the specified range within the receiver for _anObject_ (testing for equality by comparing object addresses) and returns the lowest index whose corresponding array value is identical to _anObject_. If none of the objects in the range are identical to _anObject_, this method returns [NotFound](#apple-ijaucq2ei5bek). Throws an IllegalArgumentException if _aRange_ is out of bounds.

---

### indexOfObject

`public int indexOfObject(Object anObject)`

Searches all objects in the receiver for _anObject_ and returns the lowest index whose corresponding array value is equal to _anObject_. Objects are considered equal if __equals__ returns `true`. If none of the specified objects are equal to _anObject_, returns [NotFound](#apple-ijaucq2ei5bek).

`public int indexOfObject( Object anObject, NSRange aRange)`

Searches the specified range within the receiver for _anObject_ and returns the lowest index whose corresponding array value is equal to _anObject_. Objects are considered equal if __equals__ returns `true`. If none of the specified objects are equal to _anObject_, returns [NotFound](#apple-ijaucq2ei5bek). Throws an IllegalArgumentException if _aRange_ is out of bounds.

---

### isEqualToArray

`public boolean isEqualToArray(NSArray otherArray)`

Compares the receiving array to _otherArray_, returning `true` if the contents of _otherArray_ are equal to the contents of the receiver, `false` otherwise. Two arrays have equal contents if they each hold the same number of objects and objects at a given index in each array satisfy the __equals__ test.

---

### lastObject

`public Object lastObject()`

Returns the object in the array with the highest index value. If the array is empty, __lastObject__ returns `null`.

---

### makeObjectsPerformSelector

`public void makeObjectsPerformSelector( NSSelector selector, Object[] anObject[])`

Invokes the method specified by _selector_ on each object in the receiver. The method is invoked each time with the values in _anObject_ as the method's parameters. The method shouldn't, as a side effect, modify the receiver's collection of objects. The messages are sent using NSSelector's [invoke](NSSelector.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f) method.

---

### mutableClone

`public NSMutableArray mutableClone()`

Returns a mutable copy of the receiver. NSArray's implementation creates an NSMutableArray with the receiver's elements, not copies.

---

### objectAtIndex

`public Object objectAtIndex(int index)`

Returns the object located at _index_. If the receiver is empty or if _index_ is beyond the end of the array (that is, if _index_ is greater than or equal to the value returned by __count__), an IllegalArgumentException is thrown.

__See Also:__ [count](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5rw65looq)

---

### objectEnumerator

`public java.util.Enumeration objectEnumerator()`

Returns an enumeration that lets you access each object in the array, in order, starting with the element at index 0. For example, consider the following code excerpt:
> ```
> java.util.Enumeration enumerator = myArray.objectEnumerator();
>
> while (enumerator.hasMoreElements()) {
>     Object anObject = enumerator.nextElement();
>     /* code to act on each element */
> }
> ```

When this method is used with mutable subclasses of NSArray, your code shouldn't modify the array during enumeration.

__See Also:__ [reverseObjectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zgk5tfojzwkt3cnjswg5cfnz2w2zlsmf2g64q)

---

### objects

`public Object[] objects()`

Returns copies of the receiver's elements in a natural language array.

`public Object[] objects(NSRange aRange)`

Returns copies of the receiver's elements that fall within the limits specified by _aRange_ in a natural language array.

---

### objectsNoCopy

`protected Object[] objectsNoCopy()`

Returns the receiver's actual elements-not copies-in a natural language array.

---

### reverseObjectEnumerator

`public java.util.Enumeration reverseObjectEnumerator()`

Returns an enumeration that lets you access each object in the array, in order, from the element at the highest index down to the element at index 0. For example, consider the following code excerpt:
> ```
> java.util.Enumeration enumerator = myArray.reverseObjectEnumerator();
>
> while (enumerator.hasMoreElements()) {
>     Object anObject = enumerator.nextElement();
>     /* code to act on each element */
> }
> ```

When this method is used with mutable subclasses of NSArray, your code shouldn't modify the array during enumeration.

__See Also:__ [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5xwe2tfmn2ek3tvnvsxeylun5za)

---

### sortedArrayUsingComparator

`public NSArray sortedArrayUsingComparator(NSComparator comparator) throws NSComparator.ComparisonException`

Returns an array that lists the receiver's elements, as determined by _comparator_. The new array contains the receiver's elements, not copies of them. Throws if the comparator's [compare](NSComparator.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxw24dbojqxi33sf5rw63lqmfzgk) method throws for any reason.

---

### sortedArrayUsingSelector

`public NSArray sortedArrayUsingSelector(NSSelector selector) throws NSComparator.ComparisonException`

Deprecated. Use [sortedArrayUsingComparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zw64tumvsec4tsmf4vk43jnztug33nobqxeylun5za) instead.

---

### subarrayWithRange

`public NSArray subarrayWithRange(NSRange aRange)`

Returns a new array containing the receiver's elements that fall within the limits specified by _aRange_. If _aRange_ isn't within the receiver's range of elements, an IndexOutOfBoundsException is thrown.

For example, the following code example creates an array containing the elements found in the first half of _wholeArray_ (assuming _wholeArray_ exists).

> ```
> NSRange theRange = new NSRange(0, wholeArray.count()/2);
> NSArray halfArray = wholeArray.subarrayWithRange(theRange);
> ```

---

### takeValueForKey

`public void takeValueForKey( Object value, String key)`

Conformance to [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu). For each element in the receiver, NSArray's implementation sets the element's value for _key_ to _value_. For example, if key is "firstName" and value is "Unknown", this method sets the __firstName__ property of each of the receiver's elements to "Unknown".

---

### takeValueForKeyPath

`public void takeValueForKeyPath( Object value, String key)`

Conformance to [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek). For more information, see the [takeValueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3umfvwkvtbnr2wkrtpojfwk6kqmf2gq) method description in the NSKeyValueCodingAdditions interface specification.

---

### toString

`public String toString()`

Returns a string representation of the receiver.

---

### valueForKey

`public Object valueForKey(String key)`

Conformance to [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu). NSArray's implementation is more complex than the default:

- If _key_ indicates an operation that doesn't require an argument (such as returning the array's count), __valueForKey__ performs the operation and returns the result. _key_ indicates an operation if its first character is "@". For example, if _key_ is "@count", __valueForKey__ invokes [compute](NSArray.Operator.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstifzheylzfzhxazlsmf2g64rpmnxw24dvorsq) on the "count" operator. This has the effect of computing and returning the number of elements in the receiver. Don't use __valueForKey__ for operations that take arguments; instead use [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf53gc3dvmvdg64slmv4vayluna).
- For any other key, __valueForKey__ creates an array with the same number of elements as the receiver. For each element in the receiver, the corresponding element in the new array is the value for _key_ of the receiver's element. For example, if key is "firstName", this method returns an array containing the __firstName__ values for the receiver's elements. The _key_ argument can be a key path of the form relationship.property; for example, "department.name". __valueForKey__ replaces null values with an instance of [NSKeyValueCoding.Null](NSKeyValueCoding.Null.md#apple-ijceqrsgivduc).

__See Also:__ ["Operators" (page 4)](#apple-ijbuqqsgivcuo)

---

### valueForKeyPath

`public Object valueForKeyPath(String keyPath)`

Conformance to [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek). NSArray's implementation is more complex than the default:

- If _key_ indicates an operation takes an argument (such as computing an average), __valueForKeyPath__ performs the operation and returns the result. _key_ indicates an aggregate operation if its first character is "@". For example, if _key_ is "@avg.salary", __valueForKey__ invokes [compute](NSArray.Operator.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstifzheylzfzhxazlsmf2g64rpmnxw24dvorsq) on the "avg" operator specifying the receiver and "salary" as arguments. This has the effect of computing and returning the average salary of the receiver's elements.
- Otherwise, __valueForKeyPath__ invokes the default implementation of valueForKeyPath. For more information see the method description for [valueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3wmfwhkzkgn5zewzlzkbqxi2a) in the [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek) interface specification.

__See Also:__ ["Operators" (page 4)](#apple-ijbuqqsgivcuo)

---

### vector

`public java.util.Vector vector()`

Returns the receiver as a Vector.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
