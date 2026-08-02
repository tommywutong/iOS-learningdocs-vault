---
title: Crash in ABAddPropertiesAndTypes
apple_id: DTS10003492
resource_type: QA
platform: macOS
topic: Data Management
technology: AddressBook
published: '2005-04-04'
source_url: https://developer.apple.com/library/archive/qa/qa1404/_index.html
archived_at: '2026-07-18T02:30:31.727615Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1404

# Crash in ABAddPropertiesAndTypes

## Q:  I've tried adding custom property types to Address Book, but my application crashes when I call `ABAddPropertiesAndTypes`. What's wrong?

A: I've tried adding custom property types to Address Book, but my application crashes when I call `ABAddPropertiesAndTypes`. What's wrong?

When constructing a dictionary of new properties to pass in to `ABAddPropertiesAndTypes`, you define the datatype of the new property (for example, `kABStringProperty`. These identifiers are of type `ABPropertyType`, but `ABAddPropertiesAndTypes` expects them to be wrapped in `CFNumber` objects. Code that explicitly adds the type constant into the dictionary of new properties will fail.

Two snippets of code are listed below to demonstrate the specifics of this problem. The code in Listing 1 will fail when run; the code in Listing 2 demonstrates how to correctly call `ABAddPropertiesAndTypes`.

__Listing 1__  The wrong way to call ABAddPropertiesAndTypes

```
ABAddressBookRef  abRef = ABGetSharedAddressBook(); ABPropertyType    type  = kABStringProperty;  CFMutableDictionaryRef propsAndTypes = CFDictionaryCreateMutable(NULL, 1, NULL, NULL);  // This is the problem. kABStringProperty is added as-is, when it should be wrapped in a CFNumber. CFDictionaryAddValue(propsAndTypes, CFSTR("my.new.property"), &type); printf("Added %d properties\n", ABAddPropertiesAndTypes(abRef, kABPersonRecordType, propsAndTypes));  CFRelease(propsAndTypes);
```


__Listing 2__  The right way to call ABAddPropertiesAndTypes

```
ABAddressBookRef  abRef = ABGetSharedAddressBook(); ABPropertyType    type  = kABStringProperty;  CFMutableDictionaryRef propsAndTypes = CFDictionaryCreateMutable(NULL, 1, NULL, NULL);  // Note the additional line here, and the passing of a CFNumberRef instead of an ABPropertyType CFNumberRef  numberRef = CFNumberCreate(NULL, kCFNumberSInt32Type, &type); CFDictionaryAddValue(propsAndTypes, CFSTR("my.new.property"), numberRef); printf("Added %d properties\n", ABAddPropertiesAndTypes(abRef, kABPersonRecordType, propsAndTypes));  CFRelease(numberRef); CFRelease(propsAndTypes);
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-04-04 | Fixed a typographical error. |
| 2005-03-15 | New document that how to correctly add custom Address Book properties using ABAddPropertiesAndTypes |

