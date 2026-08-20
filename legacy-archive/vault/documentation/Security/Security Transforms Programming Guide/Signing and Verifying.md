---
title: Security Transforms Programming Guide
apple_id: TP40010801
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/SigningandVerifying/SigningandVerifying.html
archived_at: '2026-07-18T02:06:17.379987Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Transforms Programming Guide](About%20Security%20Transforms.md)


[Next](Creating%20Custom%20Transforms.md)[Previous](Encrypting%20and%20Decrypting%20Data.md)

# Signing and Verifying

Signing and verifying are similar to encryption, but are somewhat more complex due to the nature of public key formats.

As described further in _[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_, public key cryptography is designed for secure communications with a potentially untrusted party. It uses two keys—a public key and a private key—that are mathematically related. You provide your public key to the untrusted party. If that party uses the public key to encrypt data, you can later decrypt it using your private key, and vice versa.

Signing is used to prove that a message has not been altered in transit. You sign a message by first taking a hash of that message, then using your private key to encrypt that hash. The recipient can later compute his or her own hash, use your public key to decrypt the original hash, and compare the two values. If they match, the recipient can be reasonably assured that the message has not been modified (assuming that the hashing scheme is sufficiently robust). This comparison and decryption process is referred to as _verifying a signature_.

As with basic encryption and decryption, signing and verification have two parts: obtaining `SecKeyRef` objects for the key or keys and performing the signing or verification transform itself.

If you are using existing public and private keys from your keychain, read [Certificate, Key, and Trust Services](https://developer.apple.com/documentation/security/certificate_key_and_trust_services) to learn how to retrieve a `SecKeychainItemRef` object for that key.

Once you have obtained a `SecKeychainItemRef`, you can cast it to a `SecKeyRef` for use with this API.

Importing and exporting public and private key pairs is somewhat more complicated than generating new keys because of the number of different key formats in common use.

This example describes how to import and export a key pair in PEM (Privacy Enhanced Mail) format.

Before you can import keys, you must read the key data into a `CFDataRef` object. If your key data is in a file, the easiest way to read the key is with a read transform, as described in [Reading Files](Reading%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqnjnknltc).

Once you have your key data in a `CFDataRef` object, you can construct key and identity objects based on that data.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create parameter objects for import and export

1. Create and populate the parameters object with a basic set of values.

```
    SecItemImportExportKeyParameters params;

    params.version = SEC_KEY_IMPORT_EXPORT_PARAMS_VERSION;
    params.flags = 0; // See SecKeyImportExportFlags for details.
    params.passphrase = NULL;
    params.alertTitle = NULL;
    params.alertPrompt = NULL;
    params.accessRef = NULL;

    /* These two values are for import. */
    params.keyUsage = NULL;
    params.keyAttributes = NULL;
```
2. Add a passphrase, if desired.

   You can add a passphrase in two ways:

   - Tell macOS to prompt the user for a passphrase by setting the `kSecKeySecurePassphrase` flag in the flags field. You can customize this dialog box by specifying appropriate (`CFStringRef`) values for `alertTitle` and `alertPrompt`.

     This is the recommended way to support user-entered passphrases because the passphrase is never stored in your application’s address space.
   - Obtain the password yourself (from a keychain or some other source), then provide the passphrase in a `CFStringRef` or `CFDataRef` object by assigning it to the `params.passphrase` field.
3. If desired, specify an initial access control list for the key using the `accessRef` field.

   To learn about access control lists for keys, read the documentation for [SecAccessCreate](https://developer.apple.com/documentation/security/1393522-secaccesscreate) and related functions.

From here on out, the process is slightly different depending on whether you are exporting a key or are importing a public key (stored as a standalone key) or a private key (traditionally stored as a public/private key pair in a single container).

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To export keys to a CFDataRef object

1. Create and populate the key usage array.

```
    CFMutableArrayRef keyUsage = CFArrayCreateMutable(
        kCFAllocatorDefault,
        0,
        &kCFTypeArrayCallBacks
    );

    /* This example sets a lot of usage values.
       Choose usage values that are appropriate
       to your specific task. Possible values begin
       with kSecAttrCan, and are defined in
       SecItem.h */
    CFArrayAppendValue(keyUsage, kSecAttrCanEncrypt);
    CFArrayAppendValue(keyUsage, kSecAttrCanDecrypt);
    CFArrayAppendValue(keyUsage, kSecAttrCanDerive);
    CFArrayAppendValue(keyUsage, kSecAttrCanSign);
    CFArrayAppendValue(keyUsage, kSecAttrCanVerify);
    CFArrayAppendValue(keyUsage, kSecAttrCanWrap);
    CFArrayAppendValue(keyUsage, kSecAttrCanUnwrap);
```
2. Create and populate the key attributes array.

```
    CFMutableArrayRef keyAttributes = CFArrayCreateMutable(
        kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks
    );
```

   In this case, the attributes dictionary is empty. However, any attribute key constants other than those beginning with `kSecAttrCan` are potentially legal (or at least any constants that make sense for the particular key type).
3. Set the key usage and attributes fields in the parameters object.

```
    params.keyUsage = keyUsage;
    params.keyAttributes = keyAttributes;
```
4. Set the external format and flag values appropriately.

```
    SecExternalFormat externalFormat = kSecFormatPEMSequence;
    int flags = 0;
```

   In general, the value of `flags` should be zero. If the specified format requires PEM armor, it is automatically provided.
5. Export the key.

```
    OSStatus oserr = SecItemExport(publickey,
        externalFormat, // See SecExternalFormat for details
        flags, // See SecItemImportExportFlags for details
        &params,
        (CFDataRef *)&pkdata);
    if (oserr) {
        fprintf(stderr, "SecItemExport failed (oserr=%d)\n", oserr);
        exit(-1);
    }
```
![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To import an identity (containing a public/private key pair) from a CFDataRef object

1. Set the key usage and attributes to `NULL`.

```
    params.keyUsage = NULL;
    params.keyAttributes = NULL;
```
2. Set the item type, external format, and flag values appropriately.

```
    SecExternalItemType itemType = kSecItemTypeCertificate;
    SecExternalFormat externalFormat = kSecFormatPEMSequence;
    int flags = 0;
```

   The item type should generally be `kSecItemTypeCertificate` because the identity is typically serialized in a form that contains both the private and public keys.

   The value of `flags` should generally be zero. If PEM armor is present, it is automatically stripped off.
3. Import the private key.

```
    oserr = SecItemImport(cfdataprivatekey,
        NULL, // filename or extension
        &externalFormat, // See SecExternalFormat for details
        &itemType, // item type
        flags, // See SecItemImportExportFlags for details
        &params,
        NULL, // Don't import into a keychain
        &temparray);
    if (oserr) {
        fprintf(stderr, "SecItemImport failed (oserr=%d)\n", oserr);
        CFShow(temparray);
        exit(-1);
    }

    privatekey = (SecKeyRef)CFArrayGetValueAtIndex(temparray, 0);
```
![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To import a public key certificate from a CFDataRef object

1. Set the key usage and attributes to `NULL`.

```
    params.keyUsage = NULL;
    params.keyAttributes = NULL;
```
2. Set the item type, external format, and flag values appropriately.

```
    SecExternalItemType itemType = kSecItemTypePublicKey;
    SecExternalFormat externalFormat = kSecFormatPEMSequence;
    int flags = 0;
```

   In general, the value of `flags` should be zero. If PEM armor is present, it is automatically stripped off.
3. Import the public key.

```
    oserr = SecItemImport(cfdatapublickey,
        NULL, // filename or extension
        &externalFormat, // See SecExternalFormat for details
        &itemType, // item type
        flags, // See SecItemImportExportFlags for details
        &params,
        NULL, // Don't import into a keychain
        &temparray);
    if (oserr) {
        fprintf(stderr, "SecItemImport failed (oserr=%d)\n", oserr);
        CFShow(temparray);
        exit(-1);
    }

    publickey = (SecKeyRef)CFArrayGetValueAtIndex(temparray, 0);
```


More often than not, public/private key pairs are generated outside the scope of your application—either manually using the Certificate Assistant or by advanced end users or system administrators running openssl commands. In such situations, either you or the user or administrator then sends a certificate signing request to a certificate authority, which signs the public key.

In some cases, however, your application might need to generate public/private key pairs on behalf of the user. Under these circumstances, you may choose to launch the Certificate Assistant or you may choose to generate the key pair yourself and handle everything within to your application.

Although there are many ways to generate a key pair for public key cryptography, the preferred way is with the [SecKeyGeneratePair](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair) function.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To generate a public/private key pair

1. Create the parameters dictionary.

```
    CFMutableDictionaryRef parameters = CFDictionaryCreateMutable(
        kCFAllocatorDefault,
        0,
        &kCFTypeDictionaryKeyCallBacks,
        &kCFTypeDictionaryValueCallBacks);
```
2. Populate the parameters dictionary.

   For example, to create a 4096-bit RSA key, you would use code like the following:

```
    CFDictionarySetValue(parameters,
        kSecAttrKeyType,
        kSecAttrKeyTypeRSA);

    int rawnum = 4096;
    CFNumberRef num = CFNumberCreate(
        kCFAllocatorDefault,
        kCFNumberIntType, &rawnum);

    CFDictionarySetValue(
        parameters,
        kSecAttrKeySizeInBits,
        num);
```

   You must specify (at least) the key size and key type. For a list of other optional parameters, see [SecKeyGeneratePair](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair).
3. Generate the key pair.

```
    SecKeyGeneratePair(parameters, &publickey, &privatekey);
```


Once you have obtained a public or private key in the form of a `SecKeyRef` (or `SecKeychainItemRef`) object, you are ready to verify signatures or sign data. The signing process itself is relatively straightforward.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To sign the contents of a CFDataRef object

1. Create the transform object.

```
    /* Create the transform objects */
    signer = SecSignTransformCreate(privatekey, &error);
    if (error) { CFShow(error); exit(-1); }
```
2. Specify the `CFDataRef` object to use as the data source.

```
    SecTransformSetAttribute(
                             signer,
                             kSecTransformInputAttributeName,
                             sourceData,
                             &error);
    if (error) { CFShow(error); exit(-1); }
```
3. Perform the transform.

```
    signature = SecTransformExecute(signer, &error);
    if (error) { CFShow(error); exit(-1); }

    if (!signature) {
        fprintf(stderr, "Signature is NULL!\n");
        exit(-1);
    }
```
![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To verify a signature

1. Create the transform object.

```
    verifier = SecVerifyTransformCreate(publickey, signature, &error);
    if (error) { CFShow(error); exit(-1); }
```

   Notice that the previously obtained signature is provided when creating the transform.
2. Specify the `CFDataRef` object to use as the data source.

```
    SecTransformSetAttribute(
                             verifier,
                             kSecTransformInputAttributeName,
                             sourceData,
                             &error);
    if (error) {
        CFShow(error);
        exit(-1);
    }
```
3. Perform the transform.

```
    result = SecTransformExecute(verifier, &error);
    if (error) {
        CFShow(error);
        exit(-1);
    }
```
4. Check the result.

```
    if (result == kCFBooleanTrue) {
        /* Signature was valid. */
    } else {
        /* Signature was invalid. */
    }
```

[Next](Creating%20Custom%20Transforms.md)[Previous](Encrypting%20and%20Decrypting%20Data.md)

