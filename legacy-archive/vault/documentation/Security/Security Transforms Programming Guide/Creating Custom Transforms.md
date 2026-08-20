---
title: Security Transforms Programming Guide
apple_id: TP40010801
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/CustomTransforms/CustomTransforms.html
archived_at: '2026-07-18T02:06:16.889003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Transforms Programming Guide](About%20Security%20Transforms.md)


[Next](Document%20Revision%20History.md)[Previous](Signing%20and%20Verifying.md)

# Creating Custom Transforms

Although macOS provides a number of common security transforms, you can also create your own. This chapter shows how to create and use a custom transform.

As mentioned in previous chapters, transforms are based on blocks and Grand Central Dispatch (GCD). GCD schedules each transform independently, allowing transforms to run in parallel. Although you do not need to understand GCD to write a custom transform, you do need to understand blocks.

Transforms are based on Core Foundation objects. This document assumes a basic knowledge of how these objects work. To learn more, read _[Core Foundation Design Concepts](../../Core%20Foundation/Core%20Foundation%20Design%20Concepts/Introduction%20to%20Core%20Foundation%20Design%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezde2i)_.

The sample custom transform described in this chapter, `CaesarXform.c`, is a transform that implements a simple Caesar (ROT-N) cipher. The complete source code for this transform is included at the end of this chapter in [Complete Code Listing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqnrnknltcmi).

All transforms need a unique name to identify it when creating a new instance. As a general rule, you should use reverse-DNS-style naming. For example, this cipher is called `com.apple.caesarcipher`.

First, create a source file and include (at least) the following headers:

```c
#include <CoreFoundation/CoreFoundation.h>
#include <Security/SecCustomTransform.h>
#include <Security/SecTransform.h>
```

Next declare the name. The name must be a [CFStringRef](https://developer.apple.com/documentation/corefoundation/cfstringref) instance, and should be declared as a global variable in a header file so that it can be used by other code. For this cipher, the name declaration is shown below:

```
const CFStringRef kCaesarCipher = CFSTR("com.apple.caesarcipher");
```


A transform can take any number of arguments, but the last argument should always be a pointer to a [CFErrorRef](https://developer.apple.com/documentation/corefoundation/cferror) object. The Caesar cipher transform takes only one argument (the encryption key), which is of type [CFIndex](https://developer.apple.com/documentation/corefoundation/cfindex) because the key is a small number. (The useful range is the same as that of `uint8_t` value.) Thus, the function is declared as follows:

```
SecTransformRef CaesarTransformCreate(CFIndex k, CFErrorRef* error)
```

This function registers the transform, then creates an instance of it.

Registering the transform initializes the transform and tells the framework code that it exists. Because this initialization must be performed exactly once during a program’s lifetime, this example uses GCD to place the initialization block on a dispatch queue exactly once, as shown below:

```
dispatch_once(&registeredOK, ^{block});
```

The function needs a flag to see if the transform has been initialized, and needs to return a value to indicate that the transform was successfully registered. These variables are defined outside the block, as follows:

```
__block Boolean result = 1;
static dispatch_once_t registeredOK = 0;
```

Note that the result variable has been declared to be a block (`__block`) variable so that it can be used inside the initialization block.

Inside the initialization block, you must call [SecTransformRegister](https://developer.apple.com/documentation/security/1393997-sectransformregister) with three arguments: the name of the transform, an implementation function that binds the transform’s actions to the actual handler blocks, and a pointer to storage for a [CFErrorRef](https://developer.apple.com/documentation/corefoundation/cferror) object. For example:

```
result = SecTransformRegister(kCaesarCipher, &CaesarImplementation, error);
```

If registration fails, [SecTransformRegister](https://developer.apple.com/documentation/security/1393997-sectransformregister) returns a Boolean to us and modifies the `CFErrorRef` object passed in by the caller.

The way you implement the transform itself is described in the next section.

After you have written a creation function, you can implement the transform itself. You do this by writing an implementation function. This function is called every time a new instance of your transform is created. It returns an instance block in which the transform performs its work.

At the core of this function are the following statements:

```
SecTransformInstanceBlock instanceBlock = ^{instance-block};
return Block_copy(instanceBlock);
```

Inside the instance block, you must declare any variables that the transform needs. Ciphers might use these variables for internal buffers, state variables, and so on. The Caesar cipher transform requires only one context variable, the key:

```
__block int _key;
```

Note that the variable is declared to be `__block`, which causes it to be preserved within the block. A transform group can contain multiple instances of a transform, so all data specific to an instance of your transform _must_ be encapsulated within this instance block.

In addition to providing storage for values specific to each instance of the transform, the instance block also sets an action for each message type that the transform implements. The Caesar cipher transform supports only two actions:

- __The notification routine for setting an attribute.__ This action takes an attribute name (of type [SecTransformAttributeRef](https://developer.apple.com/documentation/security/sectransformattributeref), which happens to be a `CFStringRef` object) and a `CFTypeRef` object that contains the value.

  The Caesar cipher transform supports only one attribute, the key attribute. For consistency with other transforms, this transform uses the `kKeyAttributeName` constant to identify that key.

```
result = SecTransformSetAttributeAction(ref,
   		kSecTransformActionAttributeNotification,
   		kKeyAttributeName,
   		^(SecTransformAttributeRef name,
   		CFTypeRef d){action-block});
```

  The action block for this action (represented by the _action-block_ placeholder in the last line above) contains the code to be executed when the key attribute is set. For the purposes of this example, it uses [CFNumberGetValue](https://developer.apple.com/documentation/corefoundation/1543114-cfnumbergetvalue) to copy the value into the block variable `_key`. In a complete implementation, it should use the `isKindOfClass:` method to verify the type and should then return an appropriate error if the value is not of an expected type.
- __The__ `ProcessData` __action__. This action is called with a `CFDataRef` object when new data becomes ready to process. This action returns a `CFDataRef` containing the results.

  When this action receives a `NULL` pointer as its input, it means that either the caller or a transform earlier in the chain has indicated that it will pass no further data. This usually occurs when a read transform reaches the end of its input stream. At this point, if there is any final output to emit, you should compute that output and send it to the output attribute (`kSecTransformOutputAttributeName`) before returning `NULL` from the block.

```
result = SecTransformSetDataAction(ref,
   			kSecTransformActionProcessData,
   			^(CFTypeRef d){action-block});
```

  The Caesar cipher example allocates a [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) instance using [malloc(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc), encrypts the plaintext, stores the results in that new object, and returns it.

Note that all action routines are called with the most generic of all Core Foundation objects, a [CFTypeRef](https://developer.apple.com/documentation/corefoundation/cftyperef) object. To be as flexible as possible, you can use the `isKindOfClass:` method to determine the type of the argument.

As an exception, the framework code filters any CF objects sent to the input attribute and passes only `CFDataRef` objects to your action. Thus, it is not necessary to use the `isKindOfClass:` method in your `ProcessData` action. You can safely assume that you will be sent a `CFDataRef` object (or `NULL`). You should return a `CFDataRef` object, but you must cast it to a `CFTypeRef` object.

Transforms use [CFErrorRef](https://developer.apple.com/documentation/corefoundation/cferror) objects to signal and describe errors in execution. Any block or routine can return a `CFErrorRef` object to signal an error. This is most useful in a `ProcessData` action. The most direct way to signal an error is to send a `CFErrorRef` object to the abort attribute ([kSecTransformAbortAttributeName](https://developer.apple.com/documentation/security/ksectransformabortattributename)). Doing so shuts down the chain of transforms.

After you dispatch the transform registration, there are still a few things left to do in your transform creation function.

First, create the transform instance by calling [SecTransformCreate](https://developer.apple.com/documentation/security/1395256-sectransformcreate). This call causes the framework code to call your implementation function (the one that you registered in [The Transform Creation Function, Part I](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbrfvbuqnrnknltc)), which in turn creates the actual transform. The transform creation function eventually returns the resulting transform instance to the caller.

In this example, the creation call looks like this:

```
caesarCipher = SecTransformCreate(kCaesarCipher, error);
```

The first parameter is the name of the transform. The second is the address of a `CFErrorRef` variable, taken from the last parameter of the creation function.

After creating the transform instance, if your transform creation function takes additional parameters for encryption keys or other transform settings, it must set the appropriate attributes on the transform instance by calling [SecTransformSetAttribute](https://developer.apple.com/documentation/security/1393861-sectransformsetattribute). (The Caesar cipher example takes no such parameters.)

Finally, the transform creation function returns the transform instance to the caller:

```
return caesarCipher;
```


To modify the behavior of a transform, you set attributes of the transform object. The Caesar cipher transform has a single creation function that passes no parameters to the transform. However, it is possible to have multiple creation functions that take additional parameters to set specific attributes. Attribute values can also be set after the transform object is created, and can even be set by other transforms.

With the exception of input and output attributes, all attributes are equal. Their data can be any Core Foundation object (though they are most commonly `CFDataRef` objects). The framework transparently provides flow control and buffing for any data sent to an attribute. If the input queue for an attribute reaches a depth of ten objects, the sender blocks (stalls) until one or more of the objects is processed.

The input attribute is special in three ways:

- An input attribute accepts only `CFDataRef` objects (which the caller must cast to `CFTypeRef` objects).
- When the input attribute of a transform is set, its `ProcessData` block is automatically scheduled. This mechanism includes buffering and flow control. The `CFDataRef` object that is returned from `ProcessData` is automatically forwarded to the output attribute, which by default is then forwarded to the input of the next transform in the chain.
- Any initial data sent to the input attribute is enqueued until `SecTransformExecute` is called.

The output attribute is similarly special:

- The output attribute must receive a series of `CFDataRef` objects cast to `CFTypeRef` objects.
- Sending a `CFErrorRef` object or `NULL` to the output indicates that the transform has finished processing data.
- `SecTransformExecute` requires that exactly one transform have an unconnected output attribute. That output attribute provides the value returned to the caller.

The `ProcessData` action performs most of the work in a transform.

When you process data, be aware that the [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) input can be of any size. Thus, your transform must be able to handle _any_ data size, including a single byte or even a zero-length string (which is distinct from receiving a `NULL` pointer).

If your `ProcessData` action receives source data that is too short to process, it must buffer the data inside the transform and return a zero-length string. It can then process that data along with any future data once the transform has received enough bytes.

If your `ProcessData` action receives data from any attribute (including the input attribute) but is not ready to process that data because of missing input data from other attributes, it can call [SecTransformPushbackAttribute](https://developer.apple.com/documentation/security/1400559-sectransformpushbackattribute) to push the data back onto the front of the input queue. You can push back only a single data item per attribute. When any other attribute provides data, you will be presented with the pushed back data again. Although you would typically push back the data item you just received, this is not a requirement; you can push back any object of any CF type.

The complete code listing for the Caesar cipher is shown in Complete Code Listing. You can use this as a starting point for learning how to create your own transforms.

__Listing 5-1__  Caesar cipher (complete listing)

```c
/*
 *  CaesarXform.c
 */

#include <Security/SecCustomTransform.h>
#include <Security/SecTransform.h>

// =========================================================================
//  Declaring the Transform Name
// =========================================================================

/* This is the unique name for the custom transform type. */
const CFStringRef kCaesarCipher = CFSTR("com.apple.caesarcipher");

/* Name of the "key" attribute. */
const CFStringRef kKeyAttributeName = CFSTR("key");

/* Helper that returns a CFError. */
CFErrorRef invalid_input_error(void)
{
    return CFErrorCreate(kCFAllocatorDefault, kSecTransformErrorDomain,
                         kSecTransformErrorInvalidInput, NULL);
}

// =========================================================================
//  The Transform Implementation Function
// =========================================================================
static SecTransformInstanceBlock CaesarImplementation(CFStringRef name,
                                            SecTransformRef newTransform,
                                            SecTransformImplementationRef ref)
{

    /* Instance Block:

       Every time a new instance of this custom transform class is
       created, this block is called. This behavior means that any
       block variables created in this block act like instance
       variables for the new custom transform instance.
     */
    SecTransformInstanceBlock instanceBlock =
    ^{
        CFErrorRef result = NULL;

        /* Data local to each instance: */
        __block int _key = 0;

        /****************************************
         *            Action Blocks:            *
         ****************************************/

        /* Key attribute action:

           This action is called when the key is set.
         */
        result = SecTransformSetAttributeAction(
                        ref,
                        kSecTransformActionAttributeNotification,
                        kKeyAttributeName,
                        ^(SecTransformAttributeRef name,
                        CFTypeRef d) {
                            CFNumberGetValue(
                                     (CFNumberRef)d,
                                     kCFNumberIntType,
                                     &_key
                            );
                            return d;
                        }
                    );

        if (result)
            return result;

        /* Input attribute action:

           This action is called for each piece of
           data posted on the input attribute.  It
           writes data to the output attribute.
         */
        result = SecTransformSetDataAction(
                    ref,
                    kSecTransformActionProcessData,
                    ^(CFTypeRef d) {
                        if (NULL == d)               // End of stream?
                            return (CFTypeRef) NULL; // Just return a null.

                        /* At this point, if desired, you
                           can check whether the key is available
                           and if not, you can call
                           SecTransformPushbackAttribute. */

                        char *dataPtr = (char *)CFDataGetBytePtr((CFDataRef)d);

                        CFIndex dataLength = CFDataGetLength((CFDataRef)d);

                        // Do the processing in a buffer generated by
                        // malloc for simplicity.
                        char *buffer = (char *)malloc(dataLength);
                        if (NULL == buffer) {
                            // Return a CFErrorRef
                            return (CFTypeRef) invalid_input_error();
                        }

                        // Do the work of the Caesar cipher (Rot(n))

                        CFIndex i;
                        for (i = 0; i < dataLength; i++)
                            buffer[i] = dataPtr[i] + _key;

                        return (CFTypeRef)CFDataCreateWithBytesNoCopy(
                                                NULL,
                                                (UInt8 *)buffer,
                                                dataLength,
                                                kCFAllocatorMalloc);
                    }
            );
        return result;
    };

    return Block_copy(instanceBlock);
}

// =========================================================================
//  The Transform Creation Function
// =========================================================================
SecTransformRef CaesarTransformCreate(CFIndex k, CFErrorRef* error)
{
    SecTransformRef caesarCipher;
    __block Boolean result = 1;
    static dispatch_once_t registeredOK = 0;

    dispatch_once(&registeredOK,
                  ^{
                     result = SecTransformRegister(
                                    kCaesarCipher,
                                    &CaesarImplementation,
                                    error);
                  });

    if (!result)
        return NULL;

    caesarCipher = SecTransformCreate(kCaesarCipher, error);
    if (NULL != caesarCipher)
    {
        CFNumberRef keyNumber =  CFNumberCreate(kCFAllocatorDefault,
                                                kCFNumberIntType, &k);
        SecTransformSetAttribute(caesarCipher, kKeyAttributeName,
                                 keyNumber, error);
        CFRelease(keyNumber);
    }

    return caesarCipher;
}


// The second function shows how to use custom transform defined in the
// previous function

// =========================================================================
//  Testing the transform
// =========================================================================
CFDataRef TestCaesar(CFDataRef theData, int rotNumber)
{
    CFDataRef result = NULL;
    CFErrorRef error = NULL;

    if (NULL == theData)
        return result;

    // Create an instance of the custom transform
    SecTransformRef caesarCipher = CaesarTransformCreate(rotNumber, &error);
    if (NULL == caesarCipher || NULL != error)
        return result;

    // Set the data to be transformed as the input to the custom transform
    SecTransformSetAttribute(caesarCipher,
                             kSecTransformInputAttributeName, theData, &error);

    if (NULL != error)
    {
        CFRelease(caesarCipher);
        return result;
    }

    // Execute the transform synchronously
    result = (CFDataRef)SecTransformExecute(caesarCipher, &error);
    CFRelease(caesarCipher);

    return result;
}

#include <CoreFoundation/CoreFoundation.h>

int main (int argc, const char *argv[])
{
    CFDataRef testData, testResult;
    UInt8 bytes[26];
    int i;

    // Create some test data, a string from A-Z

    for (i = 0; i < sizeof(bytes); i++)
        bytes[i] = 'A' + i;

    testData = CFDataCreate(kCFAllocatorDefault, bytes, sizeof(bytes));
    CFRetain(testData);
    CFShow(testData);

    // Encrypt the test data
    testResult = TestCaesar(testData, 3);

    CFShow(testResult);
    CFRelease(testData);
    CFRelease(testResult);
    return 0;
}
```

[Next](Document%20Revision%20History.md)[Previous](Signing%20and%20Verifying.md)

