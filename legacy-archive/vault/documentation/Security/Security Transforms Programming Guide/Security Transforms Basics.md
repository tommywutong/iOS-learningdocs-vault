---
title: Security Transforms Programming Guide
apple_id: TP40010801
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/SecurityTransformsBasics/SecurityTransformsBasics.html
archived_at: '2026-07-18T02:06:17.283566Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Transforms Programming Guide](About%20Security%20Transforms.md)


[Next](Reading%20Files.md)[Previous](About%20Security%20Transforms.md)

# Security Transforms Basics

Security transforms can perform many tasks, including encoding and decoding, encryption and decryption, and signing and verifying. In this chapter, Base64 encoding and decoding are used as an example of how to use transforms because they are the simplest transforms.

Although your specific use of the API may not involve Base64 encoding, the basic steps for any security transform are similar; only the transform-specific parameters (encryption keys, for example) are different.

To avoid confusion, this document uses Core Foundation data types throughout. However, because the Foundation and Core Foundation types used by this API are toll-free bridged, you can substitute `NSData` objects for `CFDataRef`, `NSString` for `CFString`, and so on.

Base64 transforms are demonstrated in two different forms in the sections that follow:

- [Performing Basic Transforms](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqmrnknltg) describes how to perform Base64 encoding and decoding using a `CFDataRef` object as input and output.
- [Performing Chained Transforms](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqmrnknlte) describes how to chain multiple transforms together to perform Base64 encoding and re-decoding in a single step.

The basic steps for performing a transform are relatively straightforward:

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To perform a basic transform

1. Create data objects or streams to use for your source data.

   For most transforms, these must be [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) or [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) objects.

   If you are reading data from a file using a read transform, you must provide an [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) or [CFReadStreamRef](https://developer.apple.com/documentation/corefoundation/cfreadstream) object.

   This trivial example creates a CFData object from a C string as shown below:

```
sourceData = CFDataCreate(
                    kCFAllocatorDefault,
                    (const unsigned char *)sourceCString,
                    (strlen(sourceCString) + 1));
```
2. Create a transform object by calling one of the `*Create*` functions, including:

   - [SecEncodeTransformCreate](https://developer.apple.com/documentation/security/1399382-secencodetransformcreate)
   - [SecDecodeTransformCreate](https://developer.apple.com/documentation/security/1395244-secdecodetransformcreate)
   - [SecDigestTransformCreate](https://developer.apple.com/documentation/security/1394846-secdigesttransformcreate)
   - [SecEncryptTransformCreate](https://developer.apple.com/documentation/security/1399605-secencrypttransformcreate)
   - [SecDecryptTransformCreate](https://developer.apple.com/documentation/security/1399526-secdecrypttransformcreate)
   - [SecSignTransformCreate](https://developer.apple.com/documentation/security/1398780-secsigntransformcreate)
   - [SecVerifyTransformCreate](https://developer.apple.com/documentation/security/1393414-secverifytransformcreate)
   - [SecTransformCreateFromExternalRepresentation](https://developer.apple.com/documentation/security/1397563-sectransformcreatefromexternalre)
   - [SecTransformCreateReadTransformWithReadStream](https://developer.apple.com/documentation/security/1394302-sectransformcreatereadtransformw)

   This example creates Base64 encoder and decoder objects as follows:

```
encoder = SecEncodeTransformCreate(kSecBase64Encoding, &error);
if (error) { CFShow(error); exit(-1); }
decoder = SecDecodeTransformCreate(kSecBase64Encoding, &error);
if (error) { CFShow(error); exit(-1); }
```
3. Set parameters for the transform by calling [SecTransformSetAttribute](https://developer.apple.com/documentation/security/1393861-sectransformsetattribute).

   In general, all transforms except for [SecTransformCreateReadTransformWithReadStream](https://developer.apple.com/documentation/security/1394302-sectransformcreatereadtransformw) require a value for [kSecTransformInputAttributeName](https://developer.apple.com/documentation/security/ksectransforminputattributename). You can find a list of other required and optional attributes for each type of transform in the documentation for that transform.

   For example, this transform sets the input attribute to the encoder as follows:

```
SecTransformSetAttribute(encoder, kSecTransformInputAttributeName,
                         sourceData, &error);
if (error) { CFShow(error); exit(-1); }
```
4. Execute the transform by calling [SecTransformExecute](https://developer.apple.com/documentation/security/1395776-sectransformexecute) or [SecTransformExecuteAsync](https://developer.apple.com/documentation/security/1397425-sectransformexecuteasync).

   For example:

```
encodedData = SecTransformExecute(encoder, &error);
if (error) { CFShow(error); exit(-1); }
```

Listing 1-1 demonstrates a very simple use of transforms to encode and subsequently decode a block of data using Base64 encoding.

__Listing 1-1__  Basic security transform

```c
#include <CoreFoundation/CoreFoundation.h>
#include <Security/Security.h>

void ShowAsString(CFDataRef data);

char *sourceCString = "All these worlds are yours except Europa.";

/* Encrypts and decrypts a blob of data. */

main(int argc, char *argv[])
{
    SecTransformRef encoder, decoder;
    CFDataRef sourceData = NULL, encodedData = NULL, decodedData = NULL;
    CFErrorRef error = NULL;

    /* Create a CFData object for the source C string. */
    sourceData = CFDataCreate(
                        kCFAllocatorDefault,
                        (const unsigned char *)sourceCString,
                        (strlen(sourceCString) + 1));

    ShowAsString(sourceData);

    /* Create the transform objects */
    encoder = SecEncodeTransformCreate(kSecBase64Encoding, &error);
    if (error) { CFShow(error); exit(-1); }
    decoder = SecDecodeTransformCreate(kSecBase64Encoding, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Tell the encode transform to get its input from the
       sourceData object. */
    SecTransformSetAttribute(encoder, kSecTransformInputAttributeName,
                             sourceData, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Execute the encode transform. */
    encodedData = SecTransformExecute(encoder, &error);
    if (error) { CFShow(error); exit(-1); }

    ShowAsString(encodedData);

    CFRelease(encoder);
    CFRelease(sourceData);

    /* Tell the decode transform to get its input from the
       encodedData object. */
    SecTransformSetAttribute(decoder, kSecTransformInputAttributeName,
                             encodedData, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Execute the decode transform. */
    decodedData = SecTransformExecute(decoder, &error);
    if (error) { CFShow(error); exit(-1); }

    ShowAsString(decodedData);

    CFRelease(decoder);
    CFRelease(encodedData);
    CFRelease(decodedData);

}


/* Creates a CFString from a CFData object, does a CFShow
   on that string, then releases the CFString.
 */
void ShowAsString(CFDataRef data)
{
    CFStringRef str = CFStringCreateFromExternalRepresentation(
                                kCFAllocatorDefault,
                                data,
                                kCFStringEncodingUTF8);

    CFShow(str);
    CFRelease(str);
}
```


In addition to individual transforms, the security transforms API also provides a way to chain multiple transforms in sequence, with each transform operating on the results from the previous transform.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To chain multiple transforms

1. Create the transforms and set their attributes appropriately, as described in [Performing Basic Transforms](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqmrnknltg).
2. Create a group transform by calling [SecTransformCreateGroupTransform](https://developer.apple.com/documentation/security/1400301-sectransformcreategrouptransform).
3. Wire the transforms together by calling [SecTransformConnectTransforms](https://developer.apple.com/documentation/security/1401298-sectransformconnecttransforms).

   In this call, you tell the group which property of the source transform it should wire to which property of the destination transform. Typically, you connect the [kSecTransformOutputAttributeName](https://developer.apple.com/documentation/security/ksectransformoutputattributename) property of the first transform object in your pipeline to the [kSecTransformInputAttributeName](https://developer.apple.com/documentation/security/ksectransforminputattributename) property of the second transform object. For example:

```
SecTransformConnectTransforms(encoder, kSecTransformOutputAttributeName,
            decoder, kSecTransformInputAttributeName, group, &error);
```
4. Start the transform by calling [SecTransformExecute](https://developer.apple.com/documentation/security/1395776-sectransformexecute) or [SecTransformExecuteAsync](https://developer.apple.com/documentation/security/1397425-sectransformexecuteasync) on the _group_.

Listing 1-2 is a replacement for the contents of the `main` function in [Listing 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqmrnknltc). This version performs the Base64 encode and decode operations in a pipeline instead of as two separate tasks. (This is not a set of operations that is commonly performed together, but it is a good way to demonstrate the basic chaining process without having to first explain multiple transform types.)

__Listing 1-2__  Chained security transform

```
    SecTransformRef encoder, decoder;
    CFDataRef sourceData = NULL, decodedData = NULL;
    CFErrorRef error = NULL;
    SecGroupTransformRef group;

    sourceData = CFDataCreate(
                              kCFAllocatorDefault,
                              (unsigned char *)sourceCString,
                              (strlen(sourceCString) + 1));

    /* Create the transform objects */
    encoder = SecEncodeTransformCreate(kSecBase64Encoding, &error);
    if (error) { CFShow(error); exit(-1); }
    decoder = SecDecodeTransformCreate(kSecBase64Encoding, &error);
    if (error) { CFShow(error); exit(-1); }


    /* Tell the encode transform to get its input from the
       sourceData object. */
    SecTransformSetAttribute(encoder, kSecTransformInputAttributeName, sourceData, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Tell the decode transform to get its input from the
       encode transform's output. */
    group = SecTransformCreateGroupTransform();
    SecTransformConnectTransforms(encoder, kSecTransformOutputAttributeName,
    decoder, kSecTransformInputAttributeName, group, &error);

    /* Execute both transforms. */
    decodedData = SecTransformExecute(group, &error);
    if (error) { CFShow(error); exit(-1); }

    ShowAsString(sourceData);
    ShowAsString(decodedData);

    CFRelease(sourceData);
    CFRelease(group);
```

[Next](Reading%20Files.md)[Previous](About%20Security%20Transforms.md)

