---
title: HIArchive Programming Guide
apple_id: TP40002481
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HIArchiveProgrammingGuide/HIArchive_hiobj/HIArchive_hiobj.html
archived_at: '2026-07-15T05:22:33.447761Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HIArchive Programming Guide](Introduction%20to%20HIArchive%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Archiving%20and%20Unarchiving%20Objects.md)

# Making HIObjects Archivable

If you want your custom HIObjects (such as
custom HIViews) to support HIArchiving, you need to implement some
additional code to do so. This chapter describes the modifications
you need to make.

To support HIArchive encoding, your HIObject must be able
to respond to the `kEventHIObjectEncode` event.
Your custom HIObject receives this event during encoding, and it
is the responsibility of the HIObject to encode its instance data
into the provided HIArchive.

You encode your HIObject instance data just as you would any
other data, using the `HIArchiveEncodeBoolean`, `HIArchiveEncodeNumber`,
or `HIArchiveEncodeCFType` functions, giving
each value a unique key.

In addition to supporting the `kEventHIObjectEncode` event,
your HIObject must also indicate that it supports archiving by passing `false` to
the HIObject function `HIObjectSetArchivingIgnored`.
Typically you do so in your HIObject’s `kEventHIObjectInitialize` event
handler. If you don’t call this function, your HIObject will never
receive the encoding event.

[Listing 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqguwueq2jjjcegscg) shows how you can implement the handler for the `kEventHIObjectEncode` event.

__Listing 2-1__  An `kEventHIObjectEncode` event
handler

```swift
OSStatus MyHIObjectEncode(
  EventHandlerCallRef inCallRef,
  EventRef inEvent,
  void* inRefCon )
{
 OSStatus err;
 HIArchiveRef encoder;
 MyHIViewData* myData = (MyHIViewData*)inRefCon;

 err = CallNextEventHandler( inCallRef, inEvent ); // 1
 require_noerr( err, cantEncodeSuperclass );

 err = GetEventParameter( inEvent, kEventParamHIArchive, typeCFTypeRef, // 2
                         NULL, sizeof( HIArchiveRef ), NULL, &encoder );
 require_noerr (err, cantGetArchive);

 if (!CFEqual (myData->myFirstDataItem, kDefaultFirstItemValue))  // 3
 {
    err = HIArchiveEncodeCFType( encoder, kMyFirstDataItemArchiveKey,  // 4
                                    myData-> myFirstDataItem );
    require_noerr( err, cantEncodeItem );
 }

 if (!CFEqual( myData->mySecondDataItem, kDefaultSecondItemValue)) // 5
 {
    err = HIArchiveEncodeNumber ( encoder, kMySecondDataItemArchiveKey,
                     kCFNumberCFIndexType, &(myData->mySecondDataItem ));
    require_noerr( err, cantEncodeItem );
 }

cantEncodeItem:
cantEncodeSuperclass:
cantGetArchive:

  return err;
}
```

Here is how the code works:

1. As usual,
   your event handler must call the Carbon Event Manager function `CallNextEventHandler` to
   allow the superclass a chance to encode its data into the archive.
   If you are subclassing from HIView, the HIView base class will archive
   basic HIView data such as the view’s size, bounds, and so on.
2. Obtains the HIArchive reference to encode into. This reference
   is packaged in the `kEventHIObjectEncode` event.
3. Checks to see if the value of the first instance data item
   is the same as some default value. If so, you don’t need to encode
   this item (as long as your decoder knows to assign the default value
   for any nonexistent keys) Doing so saves space in the archive (and minimizes
   processing time).
4. Encodes the first instance data item. HIView. You must call `HIArchiveEncodeCFType` or
   one of its wrapper variants (for CFBooleans or CFNumbers) for each
   field in your instance data structure. In this example, the instance
   data structure would look something like this:

```
typedef struct
{
    HIViewRef view;
    CFStringRef myFirstDataItem;
    CFIndex mySecondDataItem;
} MyHIViewData;
```

   Notice that
   you don’t have to encode the HIView reference (`HIViewRef`),
   because HIArchive does this for you automatically.

   The
   archive keys (for example, `kMyFirstDataItemArchiveKey`),
   are application-defined CFString constants that uniquely identify
   each data item you want to archive (and later retrieve).
5. Repeat for the second instance data item.

To support HIArchive decoding, your HIObject must be able
to instantiate itself from archive data. Doing so requires that
your `kEventHIObjectInitialize` event
handler be able to extract instance data for your object from an
HIArchive.

When your custom HIObject receives the `kEventHIObjectInitialize` event,
you could check to see if an HIArchive parameter was passed to you.
If so, you should unarchive the instance data before proceeding
with any standard initalization.

[Listing 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqguwueq2jirceqrsk) shows how to decode archive information within your `kEventHIObjectInitialize` event
handler.

__Listing 2-2__  Decoding items in a `kEventHIObjectInitialize` event
handler

```swift
OSStatus MyHIObjectInitialize(
    EventHandlerCallRef inCallRef,
    EventRef inEvent,
    void* inRefCon )
{
    OSStatus err = noErr;
    HIArchiveRef decoder = NULL;
    MyHIViewData* myData = (MyHIViewData*)inRefCon;

    err = CallNextEventHandler( inCallRef, inEvent );
    require_noerr( err, cantInitializeSuperclass );

    GetEventParameter( inEvent, kEventParamHIArchive, typeCFTypeRef, NULL,  // 1
                        sizeof( HIArchiveRef ), NULL, &decoder );

    if ( decoder != NULL ) // 2
        err = HIArchiveCopyDecodedCFType( decoder,
        kMyFirstDataItemArchiveKey, (CFTypeRef*)&myData->myFirstDataItem );

    if (decoder == NULL || err == hiArchiveKeyNotAvailableErr)  // 3
        myData->myFirstDataItem = CFRetain ( kDefaultFirstItem );

    err = HIArchiveDecodeNumber( decoder, kMySecondDataItemArchiveKey, // 4
                     kCFNumberCFIndexType, &(myData->mySecondDataItem ));

    if (decoder == NULL || err == hiArchiveKeyNotAvailableErr)
        myData->mySecondDataItem = CFRetain( kDefaultSecondItem );

    //perform any common initialization here

    HIObjectSetArchivingIgnored ( myData->view, false );  // 5

cantInitializeSuperclass:

    return err;
}
```

Here is how the code works:

1. Attempts
   to obtain the HIArchive parameter. If the initialization is occurring
   in response to an unarchiving attempt, HIArchive automatically supplies
   the appropriate HIArchive reference in the initialization event.
2. Attempts to decode the first archive object by key name.
3. If the decoder did not exist (that is, this is a standard
   initialization) or if the key did not exist, sets the first item
   to its default value.
4. Repeat for the second item.
5. Sets the archiving ignored attribute to `false` to
   indicate that this HIObject supports the HIArchive protocol. Doing
   so ensures that the HIObject receives `kEventHIObjectEncode` events.

Sometimes you want to associate additional information with
an HIObject before you archive it. For example, you may want to
store initialization parameters with the HIObject, or metadata that
is useful to your application. In most cases, this archive data
is useful only if you are writing an HIArchive editor.

Use the HIObject function `HIObjectSetCustomArchiveData` to
associate a CFDictionary with an HIObject:

```
OSStatus HIObjectSetCustomArchiveData (
   HIObjectRef inObject,
   CFDictionaryRef inCustomData
);
```

When you set this archive information, the dictionary is automatically
archived by the HIObject base class when it receives the `kEventHIObjectEncode` event.
(Remember to call `CallNextEventHandler` if
you handle the encoding event.)

To retrieve archived data, you use the `HIObjectCopyCustomArchiveData` function:

```
OSStatus HIObjectCopyCustomArchiveData (
   HIObjectRef inObject,
   CFDictionaryRef* outCustomData
);
```

HIObject defines several keys to use when adding standard
data (such as initialization parameters or class IDs) to an archive
dictionary. You can also define your own keys if necessary. For
example, you use the following keys to store initialization parameters:

```
const CFStringRef kHIObjectCustomDataParameterNamesKey;
const CFStringRef kHIObjectCustomDataParameterTypesKey;
const CFStringRef kHIObjectCustomDataParameterValuesKey;
```

Each key represents a CFArray of initialization parameter
names, types, or values. These keys correspond to the initialization
parameters you can set for a custom HIView in Interface Builder
(in the Attributes pane of the Inspector window).

Internally, when unarchiving your custom HIObject, HIArchive
automatically extracts any initialization parameter information
from the archive data, packages that in a `kEventHIObjectInitialize` event,
and sends the event to your object. If for some reason HIArchive
chooses to instantiate your HIObject superclass instead (your HIObject
class was not registered), you can still access the initialization
parameters through this archive dictionary. An HIArchive editor
can obtain the data in this manner so that the user can view or
change it.

You can also store the HIObject class and superclass IDs:

```
const CFStringRef kHIObjectCustomDataClassIDKey;
const CFStringRef kHIObjectCustomDataSuperClassIDKey;
```

Note that HIArchive automatically stores the class ID of a
custom HIObject during the archiving process. As a result, you need
to use the class and superclass keys only if you are editing an
existing archive.

For more information about custom archiving keys, see _HIObject Reference_.

[Next](Document%20Revision%20History.md)[Previous](Archiving%20and%20Unarchiving%20Objects.md)

