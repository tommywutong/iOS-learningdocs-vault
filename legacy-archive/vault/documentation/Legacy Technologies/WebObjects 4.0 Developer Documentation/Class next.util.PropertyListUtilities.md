---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/next.util.PropertyListUtil.html
archived_at: '2026-07-18T01:23:30.546639Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)



Class next.util.PropertyListUtilities

```
All Packages  Class Hierarchy  This Package  Previous  Next
```

---

# Class next.util.PropertyListUtilities

```
java.lang.Object

   |

   +----next.util.PropertyListUtilities
```

---

**public class __PropertyListUtilities__

**extends [Object](http://www.javasoft.com/products/JDK/1.0.2/api/java.lang.Object.html)****

The PropertyListUtilities class provides a collection of utility
methods that deal with property lists. One method, __propertyListFromString(__String__)__
converts string objects containing ASCII encoded property lists to
property-list objects. Another method, __stringFromPropertyList(__Object__)__
does the opposite conversion, and the third __propertyListsAreEqual(__Object, Object__)__
compares property-list objects. These methods are useful for serializing and deserializing property lists in and out of string objects.

**__See Also:__**
: [KeyValueCoding](Interface%20next.util.KeyValueCoding.md)

---

## Method Index

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/green-ball-small.gif)
[__propertyListFromString__](#apple-obzg64dfoj2hstdjon2em4tpnvjxi4tjnztsq2tbozqs43dbnzts4u3uojuw4zzj)(String)**
: Returns a property-list object derived from interpreting the ASCII property-list representation _stringRep_.

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/green-ball-small.gif)
[__propertyListsAreEqual__](#apple-obzg64dfoj2hstdjon2hgqlsmvcxc5lbnquguylwmexgyylom4xe6ytkmvrxilbanjqxmyjonrqw4zzoj5rguzldoquq)(Object, Object)**
: Returns TRUE if _plist1_ and _plist2_ are the same, FALSE if they are not.

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/green-ball-small.gif)
[__stringFromPropertyList__](#apple-on2he2lom5dhe33nkbzg64dfoj2hstdjon2cq2tbozqs43dbnzts4t3cnjswg5bj)(Object)**
: Returns a string object, which has only characters from the ASCII subset of Unicode.

## Methods

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/green-ball.gif)
__stringFromPropertyList__

```
  public static String stringFromPropertyList(Object plist)
```

: Returns a string object, which has only characters from the ASCII subset of Unicode. The _plist_ object must be one of the other permitted property-list types: Vector, Hashtable, or byte[].

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/green-ball.gif)
__propertyListFromString__

```
  public static Object propertyListFromString(String stringRep)
```

: Returns a property-list object derived from interpreting the ASCII property-list representation _stringRep_. The string object should encode only one top-level object. The return object is one of Vector, Hashtable, String, or byte[].

**__Throws:__ [RuntimeException](http://www.javasoft.com/products/JDK/1.0.2/api/java.lang.RuntimeException.html)**
: Throws a RuntimeException if there is an error parsing the property-list representation.

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/green-ball.gif)
__propertyListsAreEqual__

```
  public static boolean propertyListsAreEqual(Object plist1,

                                              Object plist2)
```

: Returns TRUE if _plist1_ and _plist2_ are the same, FALSE if they are not. The compared objects must be of the same type (else FALSE is always returned). This method performs recursive compare operations on collections such as Vectors and Hastables. If anything is different, the method returns FALSE.

---

```
All Packages  Class Hierarchy  This Package  Previous  Next
```
