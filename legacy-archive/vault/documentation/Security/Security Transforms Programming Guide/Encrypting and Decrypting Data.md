---
title: Security Transforms Programming Guide
apple_id: TP40010801
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/EncryptionandDecryption/EncryptionandDecryption.html
archived_at: '2026-07-18T02:06:17.095520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Transforms Programming Guide](About%20Security%20Transforms.md)


[Next](Signing%20and%20Verifying.md)[Previous](Reading%20Files.md)

# Encrypting and Decrypting Data

The encryption and decryption transforms provide various symmetric block cipher encryption algorithms, with optional padding (PKCS #1, #5, and #7) and support for multiple block modes (ECB, CBC, CFB, OFB, or single-block). These transforms also allow you to specify an initialization vector, if appropriate for the desired block mode.

The basic encryption and decryption process consists of two parts: obtaining or generating a key object in the appropriate format and performing the transform itself.

Before you can encrypt or decrypt data, you must create or obtain a [SecKeyRef](https://developer.apple.com/documentation/security/seckeyref) object for the encryption key. In addition to storing the bytes of the key itself, this object stores information about the type of key stored within.

First, read [Certificate, Key, and Trust Services](https://developer.apple.com/documentation/security/certificate_key_and_trust_services) to learn how to retrieve a public key from the keychain. Once you have obtained a `SecKeychainItemRef`, you can cast it to a `SecKeyRef` for use with this API.

If you do not already have an encryption key, you can ask macOS to generate one for you by calling `SecKeyGenerateSymmetric`.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To generate a random symmetric key

1. Create a parameters dictionary that tells the function what kind of key to generate.

   For example, you can create a minimal parameters dictionary for an AES key like this:

```
    CFMutableDictionaryRef parameters = CFDictionaryCreateMutable(
    kCFAllocatorDefault, 0, &kCFTypeDictionaryKeyCallBacks,
    &kCFTypeDictionaryValueCallBacks);

    CFDictionarySetValue(parameters, kSecAttrKeyType, kSecAttrKeyTypeAES);
```
2. Set the key size to 256 bits.

```
    int32_t rawnum = 256;
    CFNumberRef num = CFNumberCreate(kCFAllocatorDefault,
        kCFNumberSInt32Type, &rawnum);

    CFDictionarySetValue(parameters, kSecAttrKeySizeInBits, num);
```
3. Generate the key.

```
    cryptokey = SecKeyGenerateSymmetric(parameters, &error);
```


Before you can import or generate a key, you must create a parameters dictionary to describe the expected contents of that key.

For example, you can create a minimal parameters dictionary for an AES key as follows:

```
    CFMutableDictionaryRef parameters = CFDictionaryCreateMutable(
    kCFAllocatorDefault, 0, &kCFTypeDictionaryKeyCallBacks,
    &kCFTypeDictionaryValueCallBacks);

    CFDictionarySetValue(parameters, kSecAttrKeyType, kSecAttrKeyTypeAES);
```

If you have an existing key that you want to use for encryption, you must load that key into a `CFData` object. Two techniques are described below.

- If you have a key in a block of memory, you can create the object from a raw array of bytes like this:

```
    CFDataRef cfdatacryptokey = NULL;

    /*
       128-bit AES key.  This is for demonstration purposes
       only.  Do NOT hard-code a key into your code.
     */
    const uint8_t rawcryptokeyarr[16] = {
        63, 17, 27, 99, 185, 231, 1, 191,
        217, 74, 141, 16, 12, 99, 253, 41
    };
    size_t keylen = sizeof(rawcryptokeyarr);

    cfdatacryptokey = CFDataCreate(
                                   kCFAllocatorDefault,
                                   rawcryptokeyarr,
                                   keylen);
```
- If the key is in a file, you can use a read transform to get the contents of a file in a `CFDataRef` object, as described in [Reading Files](Reading%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqnjnknltc).

  Once you have the key in a `CFData` object, you must call `SecKeyCreateFromData` to create the key object.

```
    SecKeyRef cryptokey;
    CFErrorRef error = NULL;

    cryptokey = SecKeyCreateFromData(parameters,
                                     cfdatacryptokey,
                                     &error);
    if (error) { CFShow(error); exit(-1); }
```


Once you have the encryption key object, you can create transform objects and use them to encrypt and decrypt the contents of `CFData` objects.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To perform the actual encryption and decryption

1. Create the encryption objects.

```
    SecTransformRef encrypt = NULL, decrypt = NULL;

    /* Create the transform objects */
    encrypt = SecEncryptTransformCreate(cryptokey, &error);
    if (error) { CFShow(error); exit(-1); }
    decrypt = SecDecryptTransformCreate(cryptokey, &error);
    if (error) { CFShow(error); exit(-1); }
```
2. Set attributes on those objects to specify padding, initialization vectors, and so on, as desired.

   For example, to use PKCS #7 padding, you would use the following code:

```
    SecTransformSetAttribute(
                             encrypt,
                             kSecPaddingKey,
                             kSecPaddingPKCS7Key,
                             &error);
    if (error) { CFShow(error); exit(-1); }

    SecTransformSetAttribute(
                             decrypt,
                             kSecPaddingKey,
                             kSecPaddingPKCS7Key,
                             &error);
    if (error) { CFShow(error); exit(-1); }
```
3. Set the input attributes and execute the transforms.

```
    CFDataRef sourceData = ...

    CFDataRef encryptedData = NULL;
    CFDataRef decryptedData = NULL;
    CFErrorRef error = NULL;

    /* Use the sourceData object as input to the encryption object. */
    SecTransformSetAttribute(encrypt, kSecTransformInputAttributeName,
                             sourceData, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Encrypt the data. */
    encryptedData = SecTransformExecute(encrypt, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Use the encrypted data as input to the decryption object. */
    SecTransformSetAttribute(decrypt, kSecTransformInputAttributeName,
                             encryptedData, &error);
    if (error) { CFShow(error); exit(-1); }

    /* Decrypt the data. */
    decryptedData = SecTransformExecute(decrypt, &error);
    if (error) { CFShow(error); exit(-1); }
```

[Next](Signing%20and%20Verifying.md)[Previous](Reading%20Files.md)

