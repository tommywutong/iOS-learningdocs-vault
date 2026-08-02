---
title: Security Transforms Programming Guide
apple_id: TP40010801
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/ReadingFiles/ReadingFiles.html
archived_at: '2026-07-18T02:06:17.200301Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Transforms Programming Guide](About%20Security%20Transforms.md)


[Next](Encrypting%20and%20Decrypting%20Data.md)[Previous](Security%20Transforms%20Basics.md)

# Reading Files

To make file access easier, the security transforms API provides read transforms that return the contents of a file in a `CFData` object. By chaining this transform with other transforms, you can effectively use a readable file stream as input to any other transform.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create a read transform object

1. If you do not already have a read stream, create or obtain a `CFURLRef` object for the source file.

   For example, to read the file `encrypt2_key` in the current working directory, you could write code like the following:

```
CFURLRef url = CFURLCreateFromFileSystemRepresentation (
        kCFAllocatorDefault,
        "encrypt2_key",
        12,
        false);
```
2. If you do not already have a read stream, create a `CFReadStreamRef` object from that `CFURLRef`.

   For example:

```
    CFReadStreamRef cfrs = CFReadStreamCreateWithFile(
                                kCFAllocatorDefault,
                                url);
```
3. Call [SecTransformCreateReadTransformWithReadStream](https://developer.apple.com/documentation/security/1394302-sectransformcreatereadtransformw) to create the read transform.

   For example:

```
    SecTransformRef readTransform = SecTransformCreateReadTransformWithReadStream(cfrs);
```

If your encryption key is a series of raw bytes, you can now get the contents of a file as a `CFData` object by calling [SecTransformExecute](https://developer.apple.com/documentation/security/1395776-sectransformexecute) or [SecTransformExecuteAsync](https://developer.apple.com/documentation/security/1397425-sectransformexecuteasync) on the transform object as follows:

```
CFDataRef cfdatacryptokey = SecTransformExecute(readTransform, &error);
```

If your encryption key is in Base64 encoding, you may find it useful to group this transform with a Base64 decoder object. For example:

```
    /* Create the Base64 encoder object. */
    SecTransformRef decoder = SecDecodeTransformCreate(kSecBase64Encoding, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Create the group transform object. */
    SecGroupTransformRef group = SecTransformCreateGroupTransform();

    /* Connect the output of the read transform
       to the input of the decoder using the
       group transform object. */
    SecTransformConnectTransforms(readTransform, kSecTransformOutputAttributeName,
        decoder, kSecTransformInputAttributeName, group, &error);

    /* Perform the group transform. */
    CFDataRef cfdatacryptokey = SecTransformExecute(group, &error);
```

[Next](Encrypting%20and%20Decrypting%20Data.md)[Previous](Security%20Transforms%20Basics.md)

