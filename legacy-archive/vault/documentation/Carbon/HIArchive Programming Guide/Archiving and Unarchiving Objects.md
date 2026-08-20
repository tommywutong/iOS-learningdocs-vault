---
title: HIArchive Programming Guide
apple_id: TP40002481
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HIArchiveProgrammingGuide/HIArchive_archiving/HIArchive_archiving.html
archived_at: '2026-07-15T05:22:33.436390Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HIArchive Programming Guide](Introduction%20to%20HIArchive%20Programming%20Guide.md)


[Next](Making%20HIObjects%20Archivable.md)[Previous](Introduction%20to%20HIArchive%20Programming%20Guide.md)

# Archiving and Unarchiving Objects

HIArchive provides a convenient way to store
data objects in a portable format. This chapter describes the basics
of archiving and unarchiving objects using HIArchive APIs.

You can use HIArchive to archive any CFPropertyList data types. Some
examples:

- CFArray
- CFData
- CFString
- CFDictionary
- CFDate
- CFBoolean
- CFNumber

CFPropertyList collection types are archivable if they contain
only archivable objects.

You can also archive any HIObject that supports the HIArchive
protocol. All the standard HIViews (menus, controls) and windows
support archiving. If you use custom views, you need to add some
additional code to support archiving. See [Making HIObjects Archivable](Making%20HIObjects%20Archivable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqguwueqsdi5bugrsf) for
details.

In addition, you can archive other CFTypes by manually serializing
them to CFData objects (which are archivable).

All data is stored in the HIArchive as key value pairs.

Often when archiving data, you may find that certain item
values are unchanged from their initial or default values. For example,
a custom view may have bounds that, while modifiable, are more often
left in their initial state. In cases where you would encode known
default values into an archive, you can leave such items out. Then
during decoding, if an expected key does not exist, you should assign
that item its default value. Doing so minimizes archive space and
encoding/decoding time.

However, keep the following thoughts in mind:

- If you choose
  to not write a key value pair to the archive if the object data
  has the default value, make sure you don’t change the default
  value in a future version of your software.
- You should not change the meaning of a key, as this could
  cause problems for older software unarchiving newer objects. If
  you feel you need to change a key, consider using a new one instead,
  and write both keys to the archive. Older software can read the
  old key. Newer software can read the new key, if present, or the
  old key if not.

The examples in this document check for default values and
do not write them to the archive.

To write data to an archive, your application must first create
a write-only archive (specified by an `HIArchiveRef` object) by
calling `HIArchiveCreateForEncoding`.

To add data to the archive, you call the appropriate encoding
function:

- `HIArchiveEncodeBoolean` for
  Boolean values
- `HIArchiveEncodeNumber` for
  any numerical values
- `HIArchiveEncodeCFType` for
  any CFPropertyList types. You also use this function to encode HIObjects
  or their subclasses.

All data is encoded with a (CFStringRef) key, which uniquely
identifies the data within the archive. The keys must be unique
only within the current object you are encoding. For example, keys
used by object A do not conflict with keys used by object B, even
if A and B are instances of the same class. Within a single object,
however, keys used by a subclass can conflict with keys used by
its superclass. If you overwrite a superclass key, HIArchive warns
you by sending a message to the console output; it is up to you
to decide whether this message indicates an error.

System-supplied HIObjects always have an `HI` prefix
in the key name; your custom HIObject subclasses should avoid using
this prefix unless you are explicitly overriding a value written
to the archive by the superclass. With careful use of keys, your
archives can support versioning; on older versions, newly keyed
data written on a more recent version of software or OS is ignored.

If you call `HIArchiveEncodeCFType` on
your own custom HIObject, the system sends a `kEventHIObjectEncode` Carbon
event to the object. It is then your custom object’s responsibility
to encode the appropriate instance data into the archive specified
in the `kEventParamHIArchive` parameter
using the `HIArchiveEncodeXXX` calls.
To receive the `kEventHIObjectEncode` event,
your HIObject must indicate that it supports archiving by passing `false` to
the HIObject function `HIObjectSetArchivingIgnored`.
For more details, see [Making HIObjects Archivable](Making%20HIObjects%20Archivable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqguwueqsdi5bugrsf).

After you have encoded all the data into the archive, call `HIArchiveCopyEncodedData` to compress
the data. After compression, you handle the archive using the returned
Core Foundation data reference (`CFDataRef`).
You can use this reference to write the archive to disk, pass it
to another application, copy it to a pasteboard, and so on. After
compression, you can no longer write to the archive, and you must
release the original archive reference (`HIArchiveRef`)
by calling `CFRelease`.

[Listing 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqgiwueq2jjjbekscg) shows how you might encode data items into an archive
and then write the archive to a file specified by a URL.

__Listing 1-1__  Encoding items and writing to a file

```
#define kFirstItemKey CFSTR("myFirstItemKey");
#define kSecondItemKey CFSTR("mySecondItemKey");

OSStatus ArchiveObjectsInFile (CFTypeRef firstItem,
                                CFTypeRef secondItem, CFURLRef inFileURL )
{
    OSStatus err = noErr;
    HIArchiveRef encoder;
    CFDataRef encodedData;

    err = HIArchiveCreateForEncoding( &encoder ); // 1
    require_noerr (err, cantCreateEncoder);

    if (!CFEqual( firstItem, kDefaultFirstItem))  // 2
    {
        err = HIArchiveEncodeCFType( encoder, kFirstItemKey, firstItem ); // 3
        require_noerr (err, cantEncodeObject);
    }

    if (!CFEqual( secondItem, kDefaultSecondItem))  // 4
    {
        err = HIArchiveEncodeCFType( encoder, kSecondItemKey, secondItem );
        require_noerr (err, cantEncodeObject);
    }

    err = HIArchiveCopyEncodedData( encoder, &encodedData ); // 5
    require_noerr (err, cantCopyEncodedData);

    verify(
        CFURLWriteDataAndPropertiesToResource( inFileURL, encodedData,  // 6
                                NULL, NULL ));

    CFRelease ( encodedData ); // 7

cantEncodeObject:
cantCopyEncodedData:

    CFRelease ( encoder ); // 8

cantCreateEncoder:

    return err;
}
```

Here is how the code works:

1. Creates an
   HIArchive to hold the encoded data.
2. Checks to see if the value to be archived is the same as the
   default value. The default value could be any value you would commonly
   expect to see for this archivable item; an initial position or setting,
   standard size, default attribute, and so on. If the value to be
   archived is the same as the default, you can skip the archiving
   procedure, which saves space and processing time. Of course, you
   must make sure that your unarchiving function automatically inserts
   default values for items that do not appear in the archive.
3. Calls the `HIArchiveEncodeCFType` function to
   add the item to the archive by key.
4. Repeats the archiving process for the second item.
5. After encoding all the items, calls `HIArchiveCopyEncodedData` to
   flatten the archived items into a CFData object.
6. Writes the CFData object to a file URL.
7. Releases the CFData object.
8. Releases the archive.

To read data from an archive, your application must create
a read-only archive from the specified `CFDataRef` by
calling `HIArchiveCreateForDecoding`.
You retrieve data from the archive using the appropriate decoding
functions:

- `HIArchiveDecodeBoolean`
- `HIArchiveDecodeNumber`
- `HIArchiveCopyDecodedCFType`

If you call `HIArchiveCopyDecodedCFType` to
retrieve a custom HIObject from an archive, the system sends a `kEventHIObjectInitialize` event
to the object. Your HIObject’s initialization handler must then
retrieve data for its custom HIObject from the `kEventParamHIArchive` parameter
using the `HIArchiveDecodeXXX` calls.
See see [Making HIObjects Archivable](Making%20HIObjects%20Archivable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqguwueqsdi5bugrsf) for
details.

When you finish retrieving data from the archive, call `CFRelease` to
release the archive reference.

[Listing 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqgiwueq2jirceqrsk) shows how you might unarchive data using a CFData
reference. This data may be the reference obtained from a `HIArchiveCopyEncodedData` call or
a copy obtained from a file, URL, or other source. For example,
you could call `CFURLCreateDataAndPropertiesFromResource`,
to load the XML data from an arbitrary URL.

__Listing 1-2__  Decoding items from a CFData reference

```
OSStatus LoadObjectsFromCFData( CFTypeRef* firstItem,
                            CFTypeRef* secondItem, CFDataRef inData )
{
    OSStatus err = noErr;
    HIArchiveRef decoder;

    err = HIArchiveCreateForDecoding( inData, 0, &decoder ); // 1
    require_noerr( err, cantCreateDecoder );

    err = HIArchiveCopyDecodedCFType( decoder, kFirstItemKey, firstItem); // 2

    if (err == hiArchiveKeyNotAvailableErr)  // 3
        *firstItem = CFRetain( kDefaultFirstItem);
    else
        require_noerr( err, cantDecodeObjectFromData );

    err = HIArchiveCopyDecodedCFType( decoder, kSecondItemKey, secondItem ); // 4

    if (err == hiArchiveKeyNotAvailableErr)
        *secondItem = CFRetain( kDefaultSecondItem);
    else
        require_noerr( err, cantDecodeObjectFromData );

cantDecodeObjectFromData:

    CFRelease( decoder ); // 5

cantCreateDecoder:

    return err;
}
```

Here is how the code works:

1. Creates an
   HIArchive for decoding items.
2. Attempts to decode the first archive object by key name.
3. Assigns a default value for this item if the error indicates
   that the specified key does not exist in the archive . If you are
   opening an older archive that does not contain the latest items,
   you can also use defaults to populate the missing values.
4. Repeats the unarchiving for the second item.
5. Releases the archive.

If you want to create a generic HIArchive editor, you should
keep the following in mind:

- Because the
  editor does not have any prior knowledge of what keys and data exist, you
  may want to obtain the archive as a CFPropertyList, which you can
  then parse to obtain key names. You can do so by calling the Core
  Foundation function `CFPropertyListCreateFromXMLData`.
- A generic editor will probably encounter archives containing
  custom HIObject subclasses that have not been registered with the
  system. In such cases, you should make sure to specify the `kHIArchiveDecodeSuperClassForUnregisteredObject` option when
  calling `HIArchiveCreateForDecoding`.
  When HIArchive encounters an unregistered subclass, it instantiates
  its superclass instead and attaches any custom data to that object.
  The custom data is comparable to the information available in the Attributes
  pane of the Inspector window for custom HIViews in Interface Builder.
  You can obtain the custom (that is, subclass-specific) data by calling
  the HIObject function `HIObjectCopyCustomArchiveData`.You
  receive the data as a CFDictionary with keys defined in `HIObject.h`.
  See HIObject Reference for more details.
- When writing an unregistered subclass object to an archive,
  your editor must call the HIObject function `HIObjectSetCustomArchiveData`,
  passing a CFDictionary containing subclass-specific data. You should
  write the dictionary data as key value pairs using the dictionary
  keys supplied in `HIObject.h` (specifying,
  for example, initialization parameters, and class and superclass
  identifiers).

[Next](Making%20HIObjects%20Archivable.md)[Previous](Introduction%20to%20HIArchive%20Programming%20Guide.md)

