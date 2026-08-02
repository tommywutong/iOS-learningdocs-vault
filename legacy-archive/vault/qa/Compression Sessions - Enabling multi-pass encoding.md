---
title: Compression Sessions - Enabling multi-pass encoding
apple_id: DTS10003814
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-12'
source_url: https://developer.apple.com/library/archive/qa/qa1450/_index.html
archived_at: '2026-07-18T02:30:49.142541Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1450

# Compression Sessions - Enabling multi-pass encoding

## Q:  When configuring a Compression Session how do you enable multi-pass encoding?

A: Multi-pass encoding is enabled for a compression session by performing two steps:

- Create a temporary multi-pass storage location.
- Add this reference to a compression session options object used when creating the ICM compression session.

__Specifying a temporary storage location__

To create a temporary storage location call `ICMMultiPassStorageCreateWithTemporaryFile`. This API will return a `ICMMultiPassStorageRef` which you can then add to the compression sessions configuration object. See listing 1.


```
OSStatus ICMMultiPassStorageCreateWithTemporaryFile(
                                        CFAllocatorRef allocator,
                                        FSRef *directoryRef,
                                        CFStringRef fileName,
                                        ICMMultiPassStorageCreationFlags flags,
                                        ICMMultiPassStorageRef *multiPassStorageOut)

Discussion:

Creates multi-pass storage using a temporary file and returns a ICMMultiPassStorageRef
object. You own the returned object.

Parameter Descriptions:

allocator - An allocator for this task. Pass kCFAllocatorDefault to use the default
            allocator.

directoryRef - A reference to a file directory. If you pass NULL, the Image Compression
               Manager will use the user's Temporary Items folder.

fileName - A file name to use for the storage. If you pass NULL, the Image Compression
           Manager will pick a unique name. This file will be deleted
           when the multi-pass storage is released, unless you set the
           kICMMultiPassStorage_DoNotDeleteWhenDone flag.

flags - Flag controlling this process:

kICMMultiPassStorage_DoNotDeleteWhenDone - The temporary file should not be deleted when
                                           the multi-pass storage is released.

multiPassStorageOut - A reference to the new multi-pass storage.

Returns noErr if there is no error.
```



```
void ICMMultiPassStorageRelease(ICMMultiPassStorageRef multiPassStorage)

Discussion:

Decrements the retain count of a multi-pass storage object. If the retain count drops to
0, the object is disposed.

Parameter Descriptions:

multiPassStorage - A reference to a multi-pass storage object. If you pass NULL, nothing
                   happens.
```

__Adding the reference to a compression session options object__

Once a multi-pass storage reference has been created, add this reference to the compression session options object by calling `ICMCompressionSessionOptionsSetProperty`. Use the `kICMCompressionSessionOptionsPropertyID_MultiPassStorage` key and pass in the `ICMMultiPassStorageRef`. See listing 1.


```
kICMCompressionSessionOptionsPropertyID_MultiPassStorage - Storage for multi-pass compression.

Discussion:

To enable multi-pass compression, the client must provide a storage location for
multi-pass data. Use ICMMultiPassStorageCreateWithTemporaryFile to have the ICM store it
in a temporary file. Note that the amount of multi-pass data to be stored can be
substantial; it could be greater than the size of the output movie file.

If this property has been set for a Compression Session (i.e. not NULL), the client must
call ICMCompressionSessionBeginPass and ICMCompressionSessionEndPass around groups of
calls to ICMCompressionSessionEncodeFrame. By default, this property is NULL and
multi-pass compression is not enabled.

The Compression Session Options Object retains the multi-pass storage object when one is
set, a client can therefore release it.

This property is read/write.
```


__Listing 1__  Enabling Multi-pass compression.

```
OSStatus EnableMultiPassWithTemporaryFile(
                    ICMCompressionSessionOptionsRef inCompressionSessionOptions,
                    ICMMultiPassStorageRef *outMultiPassStorage);
{
    FSRef tempDirRef;
    ICMMultiPassStorageRef multiPassStorage = NULL;

    OSStatus status;

    *outMultiPassStorage = NULL;

    // users temp directory
    status = FSFindFolder(kUserDomain, kTemporaryFolderType,
                          kCreateFolder, &tempDirRef);
    if (noErr != status) goto bail;

    // create storage using a temporary file with a unique file name
    status = ICMMultiPassStorageCreateWithTemporaryFile(kCFAllocatorDefault,
                                                        &tempDirRef,
                                                        NULL, 0,
                                                        &multiPassStorage);
    if (noErr != status) goto bail;

    // enable multi-pass by setting the compression session options
    // note - the compression session options object retains the multi-pass
    // storage object
    status = ICMCompressionSessionOptionsSetProperty(
                       inCompressionSessionOptions,
                       kQTPropertyClass_ICMCompressionSessionOptions,
                       kICMCompressionSessionOptionsPropertyID_MultiPassStorage,
                       sizeof(ICMMultiPassStorageRef),
                       &multiPassStorage);

bail:
    if (noErr != status) {
        // this api is NULL safe so we can just call it
        ICMMultiPassStorageRelease(multiPassStorage);
    } else {
        *outMultiPassStorage = multiPassStorage;
    }

    return status;
}
```


__Listing 2__  Typical usage of Listing 1.

```
ICMCompressionSessionRef session = NULL;
ICMCompressionSessionOptionsRef sessionOptions = NULL;
CodecQ compressionQuality = codecNormalQuality;
ICMMultiPassStorageRef multiPassStorage = NULL;
OSStatus status;

...

// create the compression session options object
ICMCompressionSessionOptionsCreate(kCFAllocatorDefault, &sessionOptions);

// some configuration
ICMCompressionSessionOptionsSetAllowTemporalCompression(sessionOptions, true);
ICMCompressionSessionOptionsSetAllowFrameReordering(sessionOptions, true);

ICMCompressionSessionOptionsSetProperty(sessionOptions,
                                    kQTPropertyClass_ICMCompressionSessionOptions,
                                    kICMCompressionSessionOptionsPropertyID_Quality,
                                    sizeof(compressionQuality),
                                    &compressionQuality);

// turn on multi-pass encoding
status = EnableMultiPassWithTemporaryFile(sessionOptions, &multiPassStorage);
if (noErr != status) goto bail;

// you can choose to release the multi-pass storage here or keep it around
// and release it later - note that the compression session option object retains it
ICMMultiPassStorageRelease(multiPassStorage);

// perform other configuration as required
...

// create a compression session using the configured options which include multi-pass
ICMCompressionSessionCreate(kCFAllocatorDefault,
                            width,
                            height,
                            cType,
                            timescale,
                            sessionOptions,  // <- Pass in Compression Session Configuration Options Object
                            sourcePixelBufferOptions,
                            &encodedFrameOutputRecord,
                            &compressionSessionOut);

...
```

__References:__

- [ICMMultiPassStorageCreateWithTemporaryFile](https://developer.apple.com/documentation/QuickTime/APIREF/icmmultipassstoragecreatewithtemporaryfile.htm)
- [ICMCompressionSessionOptionsSetProperty](https://developer.apple.com/documentation/QuickTime/APIREF/icmcompressionsessionoptionssetproperty.htm)
- [ICM Compression Session Options](https://developer.apple.com/documentation/QuickTime/APIREF/ICMCompressionSessionOptions.htm)
- [ICMMultiPassStorageRelease](https://developer.apple.com/documentation/QuickTime/APIREF/icmmultipassstoragerelease.htm)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-12 | New document that describes how to enable multi-pass encoding when using ICM compression sessions. |

