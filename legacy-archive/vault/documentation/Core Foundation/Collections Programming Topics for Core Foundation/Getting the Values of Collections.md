---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/getting.html
archived_at: '2026-07-15T07:22:14.642613Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Searching%20Collections.md)[Previous](Creating%20and%20Copying%20Collections.md)

# Getting the Values of Collections

As described in [Common Characteristics of Collections](Common%20Characteristics%20of%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezdqlkdjjbeksscjbea), with CFArray, CFDictionary, CFSet,
and CFBag collection objects, you use keys (as understood in a general
sense) to retrieve stored values. The key used to retrieve values
varies according to the type of collection.

- In CFArray objects the key is an index integer
  identifying relative position in the array.
- In CFDictionary objects the key is an arbitrary though constant
  piece of data associated with the value in the dictionary. The term
  “key” is conventionally used to designate this piece of associated
  data.
- In CFSet and CFBag objects the key is the value itself.

All collection objects define value-obtaining functions whose
names contain the substring “GetValue”. These functions take
the key of the appropriate kind as a parameter.

For accessing the values of arrays, a common technique is
to iterate over the collection in a loop, incrementing the index
at each pass. Within the body of the loop you access a value using
the current index as the key and test or use the value as necessary. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztgljrgaytambufvbuqrccjbbukqi) gives
an example of this technique.

__Listing 1__  Getting
the values in a CFArray object

```
if (URLs != NULL) { /* URLs is a CFArray object */
    CFIndex i, c = CFArrayGetCount(URLs);
    CFURLRef curURL;
    CFBundleRef curBundle;

    for (i=0; i<c; i++) {
        curURL = CFArrayGetValueAtIndex(URLs, i);
        curBundle = CFBundleCreate(alloc, curURL);
        if (curBundle != NULL) {
            CFArrayAppendValue(bundles, curBundle);
            CFRelease(curBundle);
        }
    }
    CFRelease(URLs);
}
```

The primary function for obtaining values in CFDictionary
objects is `CFDictionaryGetValue`,
which requires you to specify a value’s key. [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztgljrgaytcmbvfvbuqrcdjffeori) gives an example of this.

__Listing 2__  Getting
a value in a CFDictionary object

```
CFStringRef theName = mappingTable ? (CFStringRef)CFDictionaryGetValue(mappingTable, (const void*)encoding) : NULL;
```

To get values from CFSet and CFBag objects, you must specify
the value itself as the key. This might seem odd, but remember,
you can define the callbacks that determine equality for created
objects (`hash` and `equal`),
so the value used as a key doesn’t have to be exactly identical
to a stored value.

CFSet, CFBag, and CFDictionary all define functions that get
a specified value only if it exists in the collection. Because `NULL` can
be a valid value in these collections, the `CF`_Type_`GetValueIfPresent` functions
accurately report the existence of a contained value. [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztgljrgaytcnrvfvbuqrcdi5fecqq) shows
the application of the function `CFSetGetValueIfPresent` within
a function that uses a CFSet object to ensure the uniqueness of
strings.

__Listing 3__  Using
a CFSet object to unique values

```
static CFMutableSetRef uniquedStrings = NULL;

CFStringRef uniqueString(CFStringRef string, Boolean addIfAbsent) {
    CFStringRef member = NULL;
    Boolean present;
    if (!string) {
        return NULL;
    }
    if (!uniquedStrings) {
        if (addIfAbsent) {
            uniquedStrings = CFSetCreateMutable(NULL, 0, & kCFTypeSetCallBacks);
        } else {
            return NULL;
        }
    }
    present = CFSetGetValueIfPresent(uniquedStrings, string, (void **)&member);
    if (!present) {
        if (addIfAbsent) {
            string = CFStringCreateCopy(NULL, string);
            CFSetAddValue(uniquedStrings, string);
            CFRelease(string);
        }
        member = string;
    }
    return member;
}
```

The collection types CFArray, CFDictionary, CFSet, and CFBag
include other Get functions. Some functions obtain all values (and
keys) in a collection, some return the count of values (or keys)
in a collection, and some get the index or key associated with a specified
value.

[Next](Searching%20Collections.md)[Previous](Creating%20and%20Copying%20Collections.md)

