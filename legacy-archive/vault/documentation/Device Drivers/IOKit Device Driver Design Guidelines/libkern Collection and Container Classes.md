---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/ContainerClasses/Libkern_Classes.html
archived_at: '2026-07-15T07:31:49.206689Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [IOKit Device Driver Design Guidelines](Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md)


[Next](The%20IOService%20API.md)[Previous](The%20libkern%20C%2B%2B%20Runtime.md)

# libkern Collection and Container Classes

Your driver’s information property list contains at least one personality dictionary that specifies the type of device your driver can manage. A personality dictionary can also contain information pertinent to your driver’s runtime configuration. When your driver is instantiated, it receives a copy of the I/O Kit personality for which it was loaded and it can use this information to make sure it is suitable to drive the device and, optionally, to configure itself to meet the device’s needs.

The I/O Kit personality your driver receives is in the form of an OSDictionary, which is one of the libkern collection classes. The libkern C++ library defines container classes, which hold primitive values, such as numbers and strings, and collection classes, which hold groups of both container objects and other collection objects. This chapter first describes ways in which your driver can use the libkern collection and container classes, then it gives an overview of these classes and their methods. The chapter concludes with code samples that illustrate how your driver can use the libkern classes to configure itself.

For more information on the libkern library and how it supports loadable kernel modules, see [The libkern C++ Runtime](The%20libkern%20C%2B%2B%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojvfvbecssjijdeiri) and _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_. For API reference documentation on the libkern classes, see Device Drivers Documentation. On OS X, you can find the libkern library in `/System/Library/Frameworks/Kernel.framework/Headers/libkern/c++`.

The libkern collection and container classes offer powerful services your driver can use to configure its runtime environment. Although these services may seem perfect for use in your driver’s I/O routines, they are too costly to use outside your driver’s dynamic configuration phases. During your driver’s `init`, `start`, and `probe` routines, however, the trade-off between cost and benefit make the libkern container and collection classes attractive.

The libkern classes offer many benefits, such as object introspection, encapsulation, and ability to serialize. In addition, the libkern container and collection classes closely correspond to the Core Foundation classes in both name and behavior. This allows the system to automatically translate between libkern and Core Foundation classes of the same type. For example, the libkern collection object OSDictionary is converted into the Core Foundation object CFDictionary when crossing the user-kernel boundary.

For a driver, one of the greatest benefits of the libkern classes lies in their ability to make a driver’s XML property list available to the driver during its life span. There are three general ways your driver can use the OSDictionary representation of its I/O Kit personality.

- A driver can configure itself to drive a particular type of device by reading the contents of its property list and performing the appropriate set-up.
- A driver can modify its property list (and, optionally, that of its provider) based on information it receives from the device or other service objects currently in the I/O Registry. It can then use that information to customize its runtime environment.
- A user-space process can access a driver’s property list and use it to send small amounts of data that the driver can use to customize its runtime environment.

Although this chapter’s information on the libkern collection and container classes is applicable to all three situations, the code examples in [Configuring Your Driver Using the libkern Classes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkdjbeucsq) focus on the first two uses. For more information on user space–driver communication using the property list (including a code sample), see [Making Hardware Accessible to Applications](Making%20Hardware%20Accessible%20to%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojyfvbeeq2djjceksa).

It is important to distinguish between manipulating the OSDictionary representation of your driver’s I/O Kit personality and manipulating the information property list (or `Info.plist` file) itself. Note that all property list manipulation this chapter discusses concerns the OSDictionary representation of your driver’s personality, _not_ the XML personality defined in your driver’s bundle settings. You cannot modify your driver’s `Info.plist` file in any way during your driver’s life span. When you manipulate your driver’s personality during its `start` or `init` routines, you are only manipulating a kernel representation of the personality that exists in the IORegistryEntry parent class of your driver. Your driver (and other objects currently residing in the I/O Registry) can access this property list and even make changes to it, but those changes will be lost when your driver terminates and the I/O Kit removes the corresponding IORegistryEntry object from the I/O Registry.

Although the libkern collection and container classes inherit from OSMetaClassBase, it’s more helpful to think of them as inheriting from OSObject. OSObject defines the dynamic typing and allocation features loadable kernel modules need and its virtual methods and overridden operators define how objects are created, retained, and disposed of in the kernel. For more information on the OSObject class, see _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

With the exception of Date (which is not used in the kernel because of overhead associated with routines needed to support date formats), the XML tags you use to specify data types in your driver’s `Info.plist` file have a direct, one-to-one relationship with the libkern container and collection classes of similar names. [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkii5duisi) shows this relationship.

__Table 2-1__  XML tags and libkern class names

| XML tag | libkern class |
| Array | OSArray |
| Boolean | OSBoolean |
| Data | OSData |
| Date | No libkern equivalent |
| Dictionary | OSDictionary |
| Number | OSNumber |
| String | OSString |

The libkern library defines container classes that hold primitive values or raw data, similar to C scalar types. [Table 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbecqsejjeekqi) shows the libkern container classes along with the types of values they can hold.

__Table 2-2__  The libkern container classes

| Container class name | Contents |
| OSBoolean | Boolean values `true` and `false` |
| OSData | arrays of bytes |
| OSNumber | numeric values |
| OSString | arrays of characters |
| OSSymbol | references to unique strings |

OSData, OSNumber, and OSString objects are mutable objects, however, you can make them unchangeable by declaring them to be `const`. This is useful if you know your code should never change a particular object: Declare the object to be `const` and the compiler will catch any attempts to modify it.

OSSymbol and OSBoolean are different from the other container classes. An OSSymbol object is an immutable object representing a unique string value that usually resides in the OSSymbol Pool. Although the creation of OSSymbols is not cheap, they provide great efficiency when you need to access the same strings many times. For example, if you examine the I/O Registry, you’ll see the same strings used over and over, such as “IOProviderClass” and “IOProbeScore”. In fact, all these strings are OSSymbol objects. Because kernel space is limited, it is efficient to keep a pool of commonly used strings for ready access rather than to waste space storing the same strings more than once. For more information on how to create and use OSSymbol objects, see [Container Object Creation and Initialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkejbdegsq) and [Container Object Introspection and Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkiijcuury).

OSBoolean is a variation of OSSymbol. Because there are only two values associated with an OSBoolean object, `true` and `false`, there is no need to create multiple copies of the same values.

Each container class defines several methods to manage the data it holds. Common among them are methods to initialize an instance with a particular value, return the current value, and compare the current value with a passed-in value. [Using the libkern Collection and Container Classes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkkizeuuqy) describes some of these methods in more detail.

The libkern collection classes manage groups of OSObject-derived objects, including both container objects and other collection objects. Inheriting from the libkern class OSCollection, the collection classes make their contents accessible through a positional or associative key and provide iteration services that allow you to peruse their contents one member at a time. All collection class objects are mutable. [Table 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbecqsdineegqi) shows the libkern collection classes along with the types of objects they can hold.

__Table 2-3__  The libkern collection classes

| Collection class name | Contents |
| OSArray | A list of references to OSObject-derived objects, each accessible by positional index |
| OSDictionary | A list of OSObject-derived objects, each accessible by unique associative key |
| OSOrderedSet | A sorted list of unique OSObject-derived objects, each accessible by numeric order or member function |
| OSSet | An unsorted list of unique OSObject-derived objects, each accessible by member function |

Although you can use OSSet and OSOrderedSet in your driver (for statistics-gathering perhaps) you will probably be more interested in OSArray and OSDictionary because they are direct counterparts of the XML tags Array and Dictionary you use in your driver’s property list.

The libkern collection classes have in common methods that retrieve objects, check for the presence of objects, and create instances with predefined groups of objects. [Collection Object Creation and Initialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkcjjeuora) and [Collection Object Introspection and Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkcjbfeoqi) describe some of these methods in more detail.

Because they inherit from OSCollection, the libkern collection classes also provide access to their contents through an iterator. OSCollectionIterator defines a consistent mechanism that iterates over any given collection. When you instantiate an OSCollectionIterator for your particular collection object, you automatically have access to each collection member without having to be concerned about how the collection object organizes its contents.

The libkern collection and container classes implement a variety of methods that create, initialize, access, and examine instances. This section presents an overview of these methods, along with information on libkern class reference-counting and thread safety.

All container classes implement one or more static methods for creating instances. These method names follow the form `with`_Arguments_ where _Arguments_ describes the initialization arguments. For example, OSData defines a static creation method `withBytes` that creates an instance of OSData and initializes it with the provided buffer of data.

This example uses OSData’s `withCapacity` creation method to create an empty OSData object initialized to a given size:

```
OSData *tmpData;
int size = 16; //Initial capacity of tmpData in bytes.
tmpData = OSData::withCapacity( size );
```

Some of the static creation methods specify a “no copy” variant, such as OSData’s `withBytesNoCopy` and OSString’s `withCStringNoCopy`. These creation methods create an instance of the container object but do not actually copy the provided initialization data into it. Instead, the method gives the container object a reference to the provided data.

To see why this is useful, suppose your driver needs to use the string `device_type`. You instantiate an OSString object to contain the string with the creation method `withCString`, as in the following

```
OSString * myString;
myString = OSString::withCString("device_type");
```

But because you define `device_type` as a literal string in your driver’s executable code, bytes are already wired down for it and creating an OSString object to contain it simply wastes kernel space. Therefore, if you need to reference data that you define in your driver’s executable code, such as the string `device_type`, and no one will need that data after your driver unloads, you should use the “no copy” creation methods. When you create libkern container objects with a “no copy” creation method, the resulting objects are immutable because they contain only a pointer to the data, not the data itself.

When you create an OSSymbol object, you pass a string (either an OSString object or a simple C-string) to one of OSSymbol’s static creation methods. If your string already exists in the OSSymbol Pool, you receive a reference to the original string. The OSSymbol representing that string then increments its retain count to keep track of the additional reference to the string. If your string does not already exist in the symbol pool, you receive a pointer to a fresh OSSymbol object and your string is added to the pool.

If your driver defines a string that will be needed by other IORegistryEntry objects after your driver terminates, you can create an OSSymbol for it using OSSymbol’s `withCStringNoCopy` creation method. If your string does not already exist in the OSSymbol Pool, the `withCStringNoCopy` method does not immediately add it. Instead, OSSymbol uses the string in your driver as its own, unique pool for as long as your driver stays loaded. During this time, if other IORegistryEntry objects create the same symbol, they receive a pointer to your string. When your driver is about to unload, OSSymbol then copies your string into the general OSSymbol Pool so it remains available to the other objects that have references to it.

The container classes OSData, OSString, and OSNumber also implement initialization methods that initialize existing instances of the container objects with the provided data. For example, OSString implements three initialization methods. The first two, `initWithCString` and `initWithString`, copy the provided C string or OSString object, respectively, into an instance of OSString. The third, `initWithCStringNoCopy`, is a “no copy” variant that initializes an instance of OSString but does not copy the provided C string into it. Similarly, OSData implements several initialization methods that initialize an OSData object with a block of data, including the variant `initWithBytesNoCopy` that initializes the OSData object but does not copy the bytes into it.

OSBoolean and OSSymbol do not implement `init` methods. OSBoolean can only be one of two predefined values and OSSymbol is never instantiated without referring to a particular string value.

All container objects implement various methods that provide access to the values they contain. For example, all container classes implement at least one `isEqualTo` method that tests the equality of the container’s contents and the value of a provided object. Each `isEqualTo` method handles one of the different types of data a container object can hold. OSString, for example, implements four `isEqualTo` methods that test equality with simple C strings, other OSString objects, OSData objects, and unknown OSObject-derived objects.

OSSymbol implements three `isEqualTo` methods, two that test equality with string or OSObject-derived objects and one that tests equality with other OSSymbol objects. Because two OSSymbol objects are equal only if they reference the same string in the OSSymbol pool, this `isEqualTo` method merely performs an economical pointer comparison.

Most of the container classes implement `get` methods that return both information about their contents and the contents itself. OSString, for example, implements `getLength`, which returns the length of the string, and `getChar`, which returns the character at the provided position in the string. It also implements `getCStringNoCopy`, which returns a pointer to the internal string representation, rather than the string itself.

OSData implements several `get` methods you can use to find out the size of the object’s internal data buffer and how much it will grow, and to get a pointer to the data buffer.

As with the container classes, the libkern collection classes each implement a number of creation methods of the form `with`_Arguments_. Each creation method uses the passed-in object described by _Arguments_ to initialize a fresh object. OSArray, for example, implements three creation methods, `withArray`, `withCapacity`, and `withObjects`. As its name suggests, the `withArray` method creates a fresh OSArray object and populates it with the provided OSArray object. The `withCapacity` method creates an OSArray object that can hold the given number of references and the `withObjects` method creates an OSArray object and populates it with the members of a static array of OSObjects.

The OSDictionary `withCapacity` and `withDictionary` creation methods are similar to OSArray’s but its two `withObjects` creation methods require a little more explanation. Because an OSDictionary object contains a collection of key-value pairs, you must supply both the keys and the values to populate a fresh OSDictionary object. The `withObjects` creation methods each require two static arrays, one of OSObject values and one of either OSString or OSSymbol keys. Both methods then create a fresh OSDictionary object and populate it with key-value pairs consisting of a member of the key array and the member of the value array at the same index.

The initialization methods mirror the creation methods except that they operate on existing collection objects instead of creating new ones first.

All collection classes implement several methods that give you information about their contents and allow you to get references to particular members. In addition, the libkern library provides the OSCollectionIterator class which implements methods that allow you to iterate over any collection object and access its members. Because the collection classes inherit from OSCollection, an OSCollectionIterator object automatically knows how to iterate over all types of collection objects.

The collection classes each implement several `get` methods that give you information about the collection itself or about specific objects within the collection. OSDictionary, for example, implements six `get` methods, three of which get the value associated with a key of type OSString, OSSymbol, or `const char`. The other three return information about the dictionary itself, such as its storage capacity, the size of increment by which it grows, and the current number of objects it contains.

The collection classes implement methods to both set an object into and remove an object from a collection. Each collection class implements at least one `set` method that inserts a passed-in object into a collection object. Additionally, each collection class implements a `setCapacityIncrement` method that sets the increment size by which the collection will grow. Each collection class also implements at least one `removeObject` method that removes the specified object and automatically releases it. In the case of OSArray, the contents shift to fill the vacated spot.

OSObject provides the retain-release mechanism the libkern container and collection objects use. A common source of problems in driver development is unmatched reference counting.

When you first create a libkern object, its reference count is equal to one. Therefore, if you created an object, you should also release it when you no longer need it. You do this by calling the `release`method and then setting the object’s pointer to `NULL` so you can’t accidentally refer to the released object again. If you have a pointer to an object that you did not create, you should retain that object only if you need to rely on its presence and release it when you no longer need it.

Some confusion arises with the use of the `get` and`set` methods common to all libkern collection classes. When you use a `get` method to get a member object from a collection, that member object’s reference count is _not_ incremented. Unless you also retain the object, you should not release the object you receive from a `get` method. Although this isn’t a general feature of dictionaries, it is a feature of IORegistryEntry objects.

The collection classes also implement a range of `set` methods that allow you to place an object into a collection. The `set` methods do increment the new member object’s reference count. If, for example, you create an OSString object and then use `setObject` to set it into an OSDictionary object, the OSString object will have a reference count of 2, one from its creation and one from OSDictionary’s `setObject` method.

[Table 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkkizbuiqi) summarizes the retain behavior of the collection classes’s methods.

__Table 2-4__  libkern methods and reference-counting behavior

| Method | Retain behavior |
| get | Never retains |
| set | Always retains |
| `remove` | Always releases |

None of the libkern container and collection class methods are thread-safe. If, for example, you use a `get` method to get an object from a dictionary and then you call `retain` on it, there is no guarantee that the object is still valid by the time you perform the `retain`. This is because the object you received is only valid as long as the collection containing it exists. If you do not also hold a reference to the collection, you cannot be sure that it won’t be released before you get a chance to retain the object in it.

In most cases, however, you will be modifying your own dictionaries and you can use your driver’s locking mechanism to protect them, if necessary. If you hold a reference to a collection whose member objects you are modifying, you can be reasonably sure that those objects will continue to exist as long as you don’t release the collection. Because the I/O Kit will not free any of your objects until your driver terminates (implements its `free` method), you are responsible for maintaining your collection objects and not releasing them prematurely.

All container and collection objects, with the exception of OSSymbol and OSOrderedSet, implement a `serialize` method. You use a serialization method when you want to represent an arbitrarily complex data structure in a location-independent way. Each time you call `serialize` on a libkern object, an OSSerialize object is created that contains both the XML (in an array of bytes) and the state of the serialization.

A good example of serialization is the output of the `ioreg` tool. The I/O Registry is a collection of interconnected dictionaries. When you type `ioreg` on the command line, the entire collection is serialized for output on your screen.

As described in [The libkern Classes and Your Driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbuuqkciveukri), the best uses for the libkern classes are in your driver’s dynamic configuration phase, during routines such as `init`, `probe`, and `start`. This section presents code samples that illustrate how you can use the libkern container and collection classes to configure your driver’s runtime environment.

The PhantomAudioDevice is an example subclass of IOAudioDevice (the PhantomAudioDriver project is available in `/Developer/Examples/Kernel/IOKit/Audio/PhantomAudioDriver` and on the CVSWeb at [http://developer.apple.com/darwin/tools/cvs](https://developer.apple.com/darwin/tools/cvs)). In its `createAudioEngines` method, PhantomAudioDevice uses libkern objects and methods to access its property list and create a new audio engine for each audio engine array in its personality. The `createAudioEngines` method is shown in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbecqsfizeeksa).

__Listing 2-1__  Using libkern objects and methods in audio-engine creation

```swift
bool PhantomAudioDevice::createAudioEngine()
{
    bool result = false;
    OSArray *audioEngineArray;

    audioEngineArray = OSDynamicCast(OSArray,
                            getProperty(AUDIO_ENGINES_KEY));

    if (audioEngineArray) {
        OSCollectionIterator *audioEngineIterator;

        audioEngineIterator =
                OSCollectionIterator::withCollection(audioEngineArray);
        if (audioEngineIterator) {
            OSDictionary *audioEngineDict;

            while (audioEngineDict = (OSDictionary*)
                                audioEngineIterator->getNextObject()) {
                if (OSDynamicCast(OSDictionary, audioEngineDict) != NULL) {
                    PhantomAudioEngine *audioEngine;

                    audioEngine = new PhantomAudioEngine;
                    if (audioEngine) {
                        if (audioEngine->init(audioEngineDict)) {
                            activateAudioEngine(audioEngine);
                        }
                        audioEngine->release();
                    }
                }
            }
            audioEngineIterator->release();
        }
    } else {
        IOLog("PhantomAudioDevice[%p]::createAudioEngine() - Error:
                        no AudioEngine array in personality.\n", this);
        goto Done;
    }
    result = true;
Done:
    return result;
}
```


The IOUSBMassStorageClass driver matches on mass storage class–compliant interfaces of USB devices that declare their device class to be composite. Sometimes, however, USB devices that have mass storage class–compliant interfaces declare their device class to be vendor-specific instead of composite. The IOUSBMassStorageClass driver can still drive these interfaces, but because the device’s reported class type is vendor-specific, the IOUSBMassStorageClass driver won’t match on them.

The solution is to provide a KEXT that consists of only an `Info.plist` file containing a personality for the device. This personality acts as a sort of bridge between the interface and the IOUSBMassStorageClass driver: It matches on the interface and causes the I/O Kit to instantiate the IOUSBMassStorageClass driver. The IOUSBMassStorageClass driver then examines the personality for a special dictionary named “USB Mass Storage Characteristics” that contains interface subclass and protocol values. If the dictionary is present, the IOUSBMassStorageClass driver uses these values instead of the corresponding values reported by the device.

[Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbecqsdirducsq) shows the portion of the IOUSBMassStorageClass `start` method that locates the USB Mass Storage Characteristics dictionary and gets its contents.

__Listing 2-2__  Partial listing of IOUSBMassStorageClass start method

```swift
bool IOUSBMassStorageClass::start( IOService * provider )
{
    // Code calling super::start, opening the interface,
    // and initializing some member variables not shown here.

    // Make sure provider is an IOUSBInterface object.
    SetInterfaceReference(OSDynamicCast(IOUSBInterface, provider));
    if (GetInterfaceReference() == NULL)
        return false;

    // Check if the personality for this device specifies a preferred
    // protocol.
    if (getProperty(kIOUSBMassStorageCharacteristics) == NULL)
    {
        // This device does not specify a preferred protocol, use the
        // protocol defined in the descriptor.
        // fPreferredProtocol and fPreferredSubclass are private member
        // variables of the IOUSBMassStorageClass class.
        fPreferredProtocol =
             GetInterfaceReference()->GetInterfaceProtocol();
        fPreferredSubclass =
             GetInterfaceReference()->GetInterfaceSubClass();
    } else {
        OSDictionary * characterDict;
        characterDict = OSDynamicCast(OSDictionary,
             getProperty(kIOUSBMassStorageCharacteristics));
        // Check if the personality for this device specifies a preferred
             protocol
        if (characterDict->getObject(kIOUSBMassStoragePreferredProtocol)
             == NULL)
        {
            // This device does not specify a preferred protocol, use the
            // protocol defined in the descriptor.
            fPreferredProtocol =
                 GetInterfaceReference()->GetInterfaceProtocol();
        } else {
            OSNumber * preferredProtocol;
            preferredProtocol = OSDynamicCast(OSNumber, characterDict->
                getObject(kIOUSBMassStoragePreferredProtocol);
            // This device has a preferred protocol, use that.
            fPreferredProtocol = preferredProtocol->unsigned32BitValue();
        }
        // Check if the personality for this device specifies a preferred
        // subclass.
        if (characterDict->getObject(kIOUSBMassStoragePreferredSubclass)
             == NULL)
        {
            // This device does not specify a preferred subclass, use the
            // subclass defined in the descriptor.
            fPreferredSubclass =
                 GetInterfaceReference()->GetInterfaceSubClass();
        } else {
            OSNumber * preferredSubclass;
            preferredSubclass = OSDynamicCast(OSNumber, characterDict->
                getObject(kIOUSBMassStoragePreferredSubclass));
            // This device has a preferred subclass, use that.
            fPreferredSubclass = preferredSubclass->unsigned32BitValue();
        }
    }
```

[Next](The%20IOService%20API.md)[Previous](The%20libkern%20C%2B%2B%20Runtime.md)

