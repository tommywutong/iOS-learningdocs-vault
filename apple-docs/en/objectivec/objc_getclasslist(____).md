---
title: 'objc_getClassList(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getclasslist(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getclasslist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getclasslist%28_%3A_%3A%29.json'
content_hash: 'sha256:12bc2999ce64899f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getClassList(_:_:)

<sub>Function</sub>

Obtains the list of registered class definitions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getClassList(_ buffer: AutoreleasingUnsafeMutablePointer<AnyClass>?, _ bufferCount: Int32) -> Int32
```

## Parameters

- `buffer` — An array of `Class` values. On output, each `Class` value points to one class definition, up to either `bufferCount` or the total number of registered classes, whichever is less. You can pass `NULL` to obtain the total number of registered class definitions without actually retrieving any class definitions.

- `bufferCount` — An integer value. Pass the number of pointers for which you have allocated space in `buffer`. On return, this function fills in only this number of elements. If this number is less than the number of registered classes, this function returns an arbitrary subset of the registered classes.

## Return Value

An integer value indicating the total number of registered classes.

## Discussion

The Objective-C runtime library automatically registers all the classes defined in your source code. You can create class definitions at runtime and register them with the `objc_addClass` function.

The code listing below demonstrates how to use this function to retrieve all the class definitions that have been registered with the Objective-C runtime in the current process.

```objc
int numClasses;
Class * classes = NULL;
 
classes = NULL;
numClasses = objc_getClassList(NULL, 0);
 
if (numClasses > 0 )
{
    classes = malloc(sizeof(Class) * numClasses);
    numClasses = objc_getClassList(classes, numClasses);
    free(classes);
}
```

### Special Considerations

You can’t assume that class objects you get from this function are classes that inherit from [NSObject](nsobject-swift.class.md), so you can’t safely call any methods on such classes without detecting that the method is implemented first.

## See Also

### Obtaining Class Definitions

- [objc_copyClassList](<objc_copyclasslist(__).md>) — Creates and returns a list of pointers to all registered class definitions.
- [objc_lookUpClass](<objc_lookupclass(__).md>) — Returns the class definition of a specified class.
- [objc_getClass](<objc_getclass(__).md>) — Returns the class definition of a specified class.
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — Returns the class definition of a specified class.
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — Returns the metaclass definition of a specified class.
