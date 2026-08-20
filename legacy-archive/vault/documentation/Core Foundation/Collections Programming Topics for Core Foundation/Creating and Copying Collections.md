---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/creating.html
archived_at: '2026-07-15T07:22:13.638261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Getting%20the%20Values%20of%20Collections.md)[Previous](Collection%20Customization.md)

# Creating and Copying Collections

You have more options for creating and copying collection objects than with most other Core Foundation types. Collection objects can be immutable or mutable, and, if the latter, can be either fixed-size or variable-size (immutable objects are, of course, always fixed-size). Each of these variants has its own possibilities and limitations.

Because the values (including, for dictionaries, keys) in an immutable collection cannot change once the collection is created, you must supply these values when you create the object. The acceptable form for these initializing values is a C array (unless the collection is to hold only one value). The input parameters must specify the address of this C array. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezteljrgaydsnzwfvbuqrceizfeqqy) illustrates how a CFArray object might be created.

__Listing 1__  Creating an immutable CFArray object

```
CFStringRef strs[3];
CFArrayRef anArray;

strs[0] = CFSTR("String One");
strs[1] = CFSTR("String Two");
strs[2] = CFSTR("String Three");

anArray = CFArrayCreate(NULL, (void *)strs, 3, &kCFTypeArrayCallBacks);
CFShow(anArray);
CFRelease(anArray);
```

Notice the final parameter of the `CFArrayCreate` call, the address of the `kCFTypeArrayCallBacks` constant.
This constant identifies a predefined _callback structure_ for the CFArray type. The functions that create and copy collection objects such as arrays, dictionaries, sets, and bags require you to specify callback structures. These structures contain pointers to callbacks function that control how values (and keys) of a collection are kept, evaluated, and described. Each of the collection types listed above defines one or more predefined callback structures that you can use when the values of the collection are Core Foundation objects. All of the pre-defined collection callback structures use `CFRetain` as the retain callback and `CFRelease` as the release callback so that objects added to the collection are retained, and objects removed from the collection are released.

The `CFDictionaryCreate` function, which creates an immutable dictionary object, is somewhat different from the related collection functions. It requires you to specify not only one or more values but a matching set of keys for these values. The typical means for specifying these lists of values and keys are two C arrays. [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezteljrgaytanrzfvbuqrccizdeeqq) provides a simple example.

__Listing 2__  Creating an immutable CFDictionary object

```
CFStringRef keys[3];
CFStringRef values[3];
CFDictionaryRef aDict;

keys[0] = CFSTR("Key1");
keys[1] = CFSTR("Key2");
keys[2] = CFSTR("Key3");
values[0] = CFSTR("Value1");
values[1] = CFSTR("Value2");
values[2] = CFSTR("Value3");

aDict = CFDictionaryCreate(NULL, (void **)keys, (void **)values, 3, &kCFCopyStringDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks);
CFShow(aDict);
CFRelease(aDict);
```

The keys in one array are positionally matched with the values in the other array. Thus, in the example above, the third element in the `keys` C array is the key for the third element in the `values` array. Note that for creating dictionary objects you must specify initialized callback structures for both the keys and the values.

To create a mutable collection object you call the `CreateMutable` function appropriate to a given type. This call creates an empty (that is, valueless) collection to which you then add values.

```
CFMutableDictionaryRef myDictionary = CFDictionaryCreateMutable(NULL, 0, &kCFCopyStringDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks);
CFDictionaryAddValue(myDictionary, CFSTR(“Age”), CFSTR(“35”));
```

A similar interface exists for creating mutable copies, except that these functions do not require you to specify callbacks. The reason for this omission—applicable to both mutable and immutable copies—is that the callbacks used by the original object are used by the copy to retain, release, compare, and describe its values.

```
/* props is an existing dictionary */
CFMutableArrayRef urls = CFArrayCreateMutableCopy(NULL, 0, (CFArrayRef)CFDictionaryGetValue(props, kCFURLFileDirectoryContents));
```

In functions that create or copy mutable collection objects the second parameter is an integer that specifies the _capacity_ of the collection, or the maximum number of values that the collection can safely store. A mutable collection with a capacity greater than 0 is said to be fixed-size. If this parameter is 0, as in the above example, the call requests a variable-size collection. A variable-size collection can contain any number of values, limited only by address
space and available memory.

All the code excerpts listed so far in this task show creation functions with one of the predefined collection callback structures specified in a parameter. However, you can define and use your own custom callback structures for your collection objects. There are at least two occasions when you might want to do this. One is when the values stored in the collection are custom data structures that require their own retaining, releasing, equality-testing, or descriptive behavior. Another occasion is when you want to use a predefined callback structure but need to modify an aspect of its behavior.

[Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezteljrgaytenjxfvbuqrcdirfeiqi) shows an instance of the latter case. It defines a
custom `CFDictionaryValueCallBacks` structure based on the predefined `kCFTypeDictionaryValueCallBacks` structure. But then it sets the `retain` and `release` function pointers to `NULL`. The values added to and removed from this collection will not be retained or released. This might be the desired behavior for some types of data.

__Listing 3__  Creating a CFDictionary object with modified predefined callbacks

```
CFMutableDictionaryRef bundlesByURL;
{CFDictionaryValueCallBacks nonRetainingDictionaryValueCallbacks = kCFTypeDictionaryValueCallBacks;
nonRetainingDictionaryValueCallbacks.retain = NULL;
nonRetainingDictionaryValueCallbacks.release = NULL;
bundlesByURL = CFDictionaryCreateMutable(NULL, 0, &kCFTypeDictionaryKeyCallBacks, &nonRetainingDictionaryValueCallbacks);
/* assume url and bundle come from somewhere */
CFDictionarySetValue(bundlesByURL, url, bundle);
```

The extended code example in [Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezteljrgaytgmjufvbuqrccijeuusi) illustrates the creation of a mutable CFDictionary object whose keys are integers and whose values are a program-defined structure; custom callbacks are defined for both value and keys.

__Listing 4__  Creating a CFDictionary object with custom value and key callbacks

```swift
typedef struct {
    int someInt;
    float someFloat;
} MyStructType;

const void *myStructRetain(CFAllocatorRef allocator, const void *ptr) {
    MyStructType *newPtr = (MyStructType *)CFAllocatorAllocate(allocator, sizeof(MyStructType), 0);
    newPtr->someInt = ((MyStructType *)ptr)->someInt;
    newPtr->someFloat = ((MyStructType *)ptr)->someFloat;
    return newPtr;
}

void myStructRelease(CFAllocatorRef allocator, const void *ptr) {
    CFAllocatorDeallocate(allocator, (MyStructType *)ptr);
}

Boolean myStructEqual(const void *ptr1, const void *ptr2) {
    MyStructType *p1 = (MyStructType *)ptr1;
    MyStructType *p2 = (MyStructType *)ptr2;
    return (p1->someInt == p2->someInt) && (p1->someFloat == p2->someFloat);

}
CFStringRef myStructCopyDescription(const void *ptr) {
    MyStructType *p = (MyStructType *)ptr;
    return CFStringCreateWithFormat(NULL, NULL, CFSTR("[%d, %f]"), p->someInt, p->someFloat);
}

Boolean intEqual(const void *ptr1, const void *ptr2) {
    return (int)ptr1 == (int)ptr2;
}

CFHashCode intHash(const void *ptr) {
    return (CFHashCode)((int)ptr);
}

CFStringRef intCopyDescription(const void *ptr) {
    return CFStringCreateWithFormat(NULL, NULL, CFSTR("%d"), (int)ptr);
}

void customCallBackDictionaryExample(void) {
    CFDictionaryKeyCallBacks intKeyCallBacks = {0, NULL, NULL, intCopyDescription, intEqual, intHash};
    CFDictionaryValueCallBacks myStructValueCallBacks = {0, myStructRetain, myStructRelease, myStructCopyDescription, myStructEqual};
    MyStructType localStruct;
    CFMutableDictionaryRef dict;
    CFTypeRef value;
    /* Create a mutable dictionary with int keys and custom struct values
    ** whose ownership is transferred to and from the dictionary. */
    dict = CFDictionaryCreateMutable(NULL, 0, &intKeyCallBacks, &myStructValueCallBacks);

    /* Put some stuff in the dictionary
    ** Because the values are copied by our retain function, we just
    ** set some local struct and pass that in as the value. */

    localStruct.someInt = 1000; localStruct.someFloat = -3.14;
    CFDictionarySetValue(dict, (void *)42, &localStruct);

    localStruct.someInt = -1000; localStruct.someFloat = -3.14;
    CFDictionarySetValue(dict, (void *)43, &localStruct);

    /* Because the same key is used, this next call ends up replacing the earlier value (which is freed). */
    localStruct.someInt = 44; localStruct.someFloat = -3.14;
    CFDictionarySetValue(dict, (void *)42, &localStruct);
    show(CFSTR("Dictionary: %@"), dict);

    value = CFDictionaryGetValue(dict, (void *)43);

    if (value) {
        MyStructType result = *(MyStructType *)value;
        CFStringRef description = myStructCopyDescription(&result);
        show(CFSTR("Value for key 43: %@"), description);
        CFRelease(description);
    }
    CFRelease(dict);
}
```

The collection types CFArray, CFDictionary, CFSet, and CFBag
declare the following structure types for callbacks:

- `CFArrayCallBacks`
- `CFDictionaryKeyCallBacks`
- `CFDictionaryValueCallBacks`
- `CFSetCallBacks`
- `CFBagCallBacks`

The function-pointer members of these structures are similar
in acceptable values, expected behavior of pointed-to functions,
and caveats. [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezteljrgaztcnjrfvbuuqsji5deuri) describes some of the general characteristics of these
callbacks; for detailed information, see the reference documentation
for the callback structure types.

__Table 1__

| Function- pointer variable | Collection type | Description of callback function |
| `retain` | All | Invoked to retain values as they are added to the collection. The nature of reference counting can vary according to the type of the data and the purpose of the collection; for example, it could increment a reference count. The function returns the value to store in the collection, which is usually the value passed, but can be a different value if that value should be stored. The function pointer can be `NULL`. |
| `release` | All | Invoked when values are removed from the collection. It reverses the effect of the `retain` callback by, for example, decrementing a reference count or freeing the memory allocated to a value. The function pointer can be `NULL`. |
| `equal` | all | A callback function that compares two values. It is invoked when some operation requires the comparison of values in the collection. For collection values, the function pointer can be `NULL`. Can be `NULL` for collection keys, in which case pointer equality is used as the basis of comparison. |
| `copyDescription` | all | A callback function that creates and returns a description (as a CFString object) of each value in the collection. This callback is invoked by the `CFCopyDescription` and `CFShow` functions. The function pointer can be `NULL`, in which case the collection composes a simple description. |
| `hash` | CFDictionary keys, CFSet, CFBag | A callback function invoked to compute a hash code for keys as they are used to access, add, or remove values in the collection. If `NULL` is assigned, the default implementation is to use the pointer addresses as hash codes. See [Dictionaries](Types%20of%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezdsljrgazdonzz) for more on the relation between the `equal` and `hash` function callbacks. |

[Next](Getting%20the%20Values%20of%20Collections.md)[Previous](Collection%20Customization.md)

