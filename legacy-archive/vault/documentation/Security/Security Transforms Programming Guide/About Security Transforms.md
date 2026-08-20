---
title: Security Transforms Programming Guide
apple_id: TP40010801
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/Introduction/Introduction.html
archived_at: '2026-07-18T02:06:17.165880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Security%20Transforms%20Basics.md)

# About Security Transforms

The security transforms application programming interface (API) is a set of C-based functions in the Security framework, based on Core Foundation. It provides high-level functions for performing cryptographic tasks, such as encryption, signing, and verification. Security transforms also provide support for encodings that are commonly used in conjunction with cryptographic signatures, such as Base64.

At a high level, security transforms take data in the form of a series of [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) objects and return similar objects. These Core Foundation data types are toll-free bridged to their Foundation equivalent ([NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData)), so it is easy to use this API from within a Cocoa application.

As a special exception, because the read transform reads a file, it takes an [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) or [CFReadStreamRef](https://developer.apple.com/documentation/corefoundation/cfreadstream) object as its input and returns a [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) object that can be chained to the input of other transforms.

Each transform takes a parameters dictionary that you can use to specify encryption keys, input and output encoding, and so on. The specific dictionary keys and values supported by each transform type are described in the reference document for that specific transform type.

Security transforms can be used individually to perform a specific task, or can be used in a pipeline to perform a series of tasks on a single piece of data. For example, you might want to decode a Base64-encoded block of data, and then decrypt the resulting decoded data.

The underlying data flow architecture can also be extended to support custom transforms to perform custom encoding, encryption, or other data processing tasks specific to your application.

Begin by reading the chapter [Security Transforms Basics](Security%20Transforms%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqmrnknltk). This chapter provides the foundation for understanding the chapters that follow, including a full code listing that demonstrates how to perform basic transforms (Base64 encoding and decoding).

If you need to take data from a file, you should read [Reading Files](Reading%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqnjnknltc). Otherwise, you can skip directly to [Encryption and Decryption](Encrypting%20and%20Decrypting%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqmznknltc) (to learn how to encrypt and decrypt files) or [Signing and Verifying](Signing%20and%20Verifying.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqnbnknltc) (to learn how to use public keys for computing and verifying signatures).

If you want to learn about creating your own transform types, read [Creating Custom Transforms](Creating%20Custom%20Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqnrnknlte).

This document assumes a basic understanding of cryptography at a high level. It also assumes that you know what Base64 encoding is. Although detailed knowledge of cryptography or encoding formats is not required to understand the material in this book, you will likely need to know these things to some degree if you want to use what you learn.

For example, you need to have some idea of what types of encryption and padding formats (PKCS #7, for example) that your project requires.

Read _Security Transforms Reference_ for detailed information about the security transforms API.

Read _[Core Foundation Design Concepts](../../Core%20Foundation/Core%20Foundation%20Design%20Concepts/Introduction%20to%20Core%20Foundation%20Design%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezde2i)_ and _[Core Foundation Framework Reference](https://developer.apple.com/documentation/corefoundation)_ to learn more about Core Foundation.

[Next](Security%20Transforms%20Basics.md)

