---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/08_Media_Example/MS_Media_Example.html
archived_at: '2026-07-15T07:31:32.885571Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mass Storage Device Driver Programming Guide](Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Subclassing%20Protocol%20Services%20Drivers.md)

# Developing a Filter Scheme

On OS X, a filter-scheme driver provides a filtering mechanism between generic I/O requests and content on a media. A media-filter scheme matches on an `IOMedia` object representing the content present in a partition and publishes in the I/O Registry another `IOMedia` object that represents the unfiltered content. Because filter-scheme drivers are both consumers and producers of `IOMedia` objects, there can be an arbitrary number of filter schemes in the mass storage driver stack.

To create your own filter-scheme driver, you subclass `IOStorage` and implement your filtering functionality in the `read` and `write` methods. Other methods you implement, such as `init`, `start`, and `free`, create and initialize the new `IOMedia` object, attach it to the I/O Registry, and release it.

As described in [Filter Schemes](Mass%20Storage%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzufvkfawcsivddcmbt), a filter-scheme driver should not produce an `IOCDMedia` or `IODVDMedia` object, because these objects have provider requirements specific to CD and DVD media that can be met only by an `IOCDBlockStorageDriver` or `IODVDBlockStorageDriver`, respectively.

This chapter guides you through the process of creating a filter-scheme driver. It also describes how to test the driver by creating a disk image that contains a partition the driver can match on. The sample code in this chapter is generic and emphasizes the form your driver should take, rather than the implementation of specific filtering functionality. When you use this code as a basis for your own filter-scheme driver, you should replace the generic values, such as `MySoftwareCompany`, with your own values and add your filtering code to the appropriate methods.

The sample filter scheme described in this chapter includes code that allows you to install the filter scheme on the boot partition. If you do not need to do this, you can skip the portions of the code that implement this.

The sample code in this chapter is from an Xcode project that builds a filter-scheme driver. To download the complete project (which includes debugging and installation information), see _[SampleFilterScheme](../../../samplecode/SampleFilterScheme/SampleFilterScheme.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbtgi)_ in the ADC Reference Library. Note that the _SampleFilterScheme_ project defines two different targets, one of which allows you to install the filter scheme on the boot partition. Be sure to read the comments in the project’s files before you decide which target to build.

For more information on how to develop kernel extensions in general and I/O Kit drivers in particular, see _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_ and _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

Every driver has an `Info.plist` file that contains information about the driver and what it needs, including its personalities. A filter-scheme driver matches on content in a partition rather than on a device, so its personality contains information that identifies specific content. As described in [Filter-Scheme Driver Matching](Mass%20Storage%20Driver%20Matching%20and%20Loading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbegskcifbuosa), a filter-scheme driver uses the `Content Hint` property to match on the content-hint string a disk utility program places in a partition. To make sure your driver loads for your content, you add the `Content Hint` property and associated content-hint value to its personality dictionary. You can also add other properties that identify media characteristics, such as ejectability and writability.

For step-by-step instructions that describe how to create a personality dictionary for a driver and add children to it, see the [Hello I/O Kit](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIOKit/iokit_tutorial.html#//apple_ref/doc/uid/20002366) tutorial in _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_.

The sample code uses the following five property keys:

- `CFBundleIdentifier`
- `IOClass`
- `IOProviderClass`
- `Content Hint`
- `IOMatchCategory`

Create five new children of the `MyFilterScheme` personality dictionary, one for each of the five properties you’ll be adding. [Table 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzzfvbucscgjjceiri) shows the properties, along with their classes and values. To test the sample code with your device, replace values such as `MySoftwareCompany_MyContentHint` with actual values for your content.

__Table 7-1__  Personality properties for MyFilterScheme

| Property | Class | Value |
| `CFBundleIdentifier` | String | `com.MySoftwareCompany.driver.MyFilterScheme` |
| `IOClass` | String | `com_MySoftwareCompany_driver_MyFilterScheme` |
| `IOProviderClass` | String | `IOMedia` |
| `Content Hint` | String | `MySoftwareCompany_MyContent` |
| `IOMatchCategory` | String | `IOStorage` |

A driver declares its dependencies on other loadable kernel extensions and in-kernel components in the `OSBundleLibraries` dictionary. Each dependency has a string value that declares the earliest version of the dependency the driver is compatible with.

The sample driver depends on one loadable extension from the Storage family and three kernel components. To add these dependencies to the `OSBundleLibraries` dictionary, you create a new child for each dependency. [Table 7-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzzfvbucscjircuira) shows the dependencies you add for the sample driver.

__Table 7-2__  Dependencies for MyFilterScheme

| Property | Class | Value |
| `com.apple.iokit.IOStorageFamily` | String | `1.1` |
| `com.apple.kernel.iokit` | String | `1.1` |
| `com.apple.kernel.libkern` | String | `1.1` |
| `com.apple.kernel.mach` | String | `1.1` |

Finally, to allow this filter scheme to filter the boot volume, you must ensure that it is loaded at boot time so that it can be installed on top of the boot volume. To do this, you add the `OSBundleRequired` property to the top level of your `Info.plist` file and give it the string value `Local-Root`. If you do not need to filter the boot partition, do not add this property-value pair to your `Info.plist` file.

This section describes some of the elements that must be included in your driver’s source files. To demonstrate the process of creating a filter-scheme driver, the sample driver implements most of the needed methods by acting as a pass-through, in other words, calling through to its provider media. You should replace these trivial implementations with your own code that supports your filtering functionality.

The header file for the sample filter-scheme driver includes ten method declarations and two external header files. In the interests of brevity, the sample code includes only a condensed version of the standard comments accompanying each method declaration. You can find fully commented versions of these method declarations in `IOMedia.h` and `IOStorage.h` (both of which are in `/System/Library/Frameworks/IOKit.framework/Headers/storage`).

Edit the `MyFilterScheme.h` file to match the code in [Listing 7-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzzfvbuurckjfduuqq).

__Listing 7-1__  The MyFilterScheme header file

```c
#include <IOKit/storage/IOMedia.h>
#include <IOKit/storage/IOStorage.h>

class com_MySoftwareCompany_driver_MyFilterScheme : public IOStorage {

    OSDeclareDefaultStructors(com_MySoftwareCompany_driver_MyFilterScheme)

protected:

    IOMedia*    _childMedia;

    // Free all of this object's outstanding resources.

    virtual void free(void);

    // The handleOpen method grants or denies permission to access this
    // object to an interested client.

    virtual bool handleOpen(IOService*   client,
                            IOOptionBits options,
                            void*        access);

    // The handleIsOpen method determines whether the specified client,
    // or any client if none is specified, presently has an open
    // on this object.

    virtual bool handleIsOpen(const IOService* client) const;

     // The handleClose method closes the client's access to this object.

    virtual void handleClose(IOService* client, IOOptionBits options);

    // Attach the passed-in media object to the device tree plane.
    // This is necessary if you want to stack this filter scheme on top
    // of the boot volume. You do not need to include this method if you
    // do not need to filter the boot volume.

    virtual bool attachMediaObjectToDeviceTree(IOMedia* media);

    // Detach the passed-in media object from the device tree plane.
    // This is necessary if you want to stack this filter scheme on top
    // of the boot volume. You do not need to include this method if you
    // do not need to filter the boot volume.

    virtual void detachMediaObjectFromDeviceTree(IOMedia* media);

public:

     // Initialize this object's minimal state.

    virtual bool init(OSDictionary* properties = 0);

     // Publish the new IOMedia object that represents the filtered content.

    virtual bool start(IOService* provider);

    // Clean up after the published media object before terminating.

    virtual void stop(IOService* provider);

    // Read data from the storage object at the specified byte offset into
    // the specified buffer, asynchronously.   When the read completes,
    // the caller will be notified via the specified completion action.
    // The buffer will be retained for the duration of the read.

    virtual void read(IOService*           client,
                      UInt64               byteStart,
                      IOMemoryDescriptor*  buffer,
                      IOStorageCompletion  completion);

    // Write data into the storage object at the specified byte offset from
    // the specified buffer, asynchronously.   When the write completes, the
    // caller will be notified via the specified completion action.
    // The buffer will be retained for the duration of the write.

    virtual void write(IOService*           client,
                       UInt64               byteStart,
                       IOMemoryDescriptor*  buffer,
                       IOStorageCompletion  completion);

    // Flush the cached data in the storage object, if any, synchronously.
    // The I/O Kit provides for data caches at the driver level, but
    // Apple discourages this because it is rarely needed. In the majority
    // of cases, a pass-through implementation is sufficient.

    virtual IOReturn synchronizeCache(IOService* client);

    // Obtain this object's provider.  This method returns IOMedia,
    // rather than the less-specific OSObject, as a convenience.

    virtual IOMedia* getProvider() const;
};
```


The C++ file provides the code to implement the chosen methods. The sample driver’s C++ file contains all the elements required for a subclassed filter-scheme driver even though it performs no filtering. To implement your filtering scheme, add code to the `read` and `write` methods.

The sample code in includes two methods you must implement if you want your filter scheme to filter the boot volume:

- `attachMediaObjectToDeviceTree`
- `detachMediaObjectFromDeviceTree`

The `attachMediaObjectToDeviceTree` method, is called in your `start` routine after the call to the standard `attach` method that attaches the new media to your filter scheme. This method detaches your filter scheme’s parent object from the Open Firmware device tree and attaches the filter scheme’s child object to the Open Firmware device tree in its place. This must be done before you publish the new media object in the I/O Registry using the `registerService` method. The second method, the `detachMediaObjectFromDeviceTree` method, performs the operation in reverse in your `stop` routine.

To understand why this rearranging of device tree nodes is necessary, it helps to know more about the OS X boot process. When you turn on your computer, Open Firmware determines which volume to boot from. It then loads the secondary booter (named BootX) from that volume and jumps to it. BootX loads and runs the kernel, passing to it parameters it inherits from Open Firmware, including the device tree.

After the kernel comes up, it must mount the root volume. By this time, Open Firmware is no longer running, so the kernel determines the root volume by interpreting a parameter Open Firmware passed to it earlier. The parameter contains the root path property of the `/chosen` node in the Open Firmware device tree. The kernel searches the I/O Registry for a node whose Open Firmware path matches the root path. The kernel uses this node as the root device.

If there is a filter scheme installed on top of this node, the kernel is not aware of it and it continues to boot from the unfiltered node. Later on in the process, the system notices that the filter scheme is publishing a new child node that hasn’t been mounted on, so it mounts the file system on that node. This results in the appearance of two copies of the boot volume on the Desktop, each with a separate data path, which is an undesirable outcome.

Edit the `MyFilterScheme.cpp` file to match the code in [Listing 7-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzzfvbuurckjjbeiry).

__Listing 7-2__  The MyFilterScheme C++ file

```c
#include <IOKit/assert.h>   // For debugging purposes.
#include <IOKit/IOLib.h>
#include "MyFilterScheme.h"

// This definition allows you to use the more convenient "super" in
// place of "IOStorage", where appropriate.
#define super IOStorage

// This macro must appear before you define any of your class's methods.
// Note that you must use the literal name of the superclass here,
// not "super" as defined above.
OSDefineMetaClassAndStructors(com_MySoftwareCompany_driver_MyFilterScheme,
                                IOStorage)

// Define the methods to implement.
bool com_MySoftwareCompany_driver_MyFilterScheme::init(OSDictionary*
                                            properties = 0)
{
    //
    // Initialize this object's minimal state.
    //

    // Call superclass's init.

    if (super::init(properties) == false)  return false;

    // Initialize state.

    _childMedia = 0;

    return true;
}


void com_MySoftwareCompany_driver_MyFilterScheme::free(void)
{
    //
    // Free all of this object's outstanding resources.
    //

    if ( _childMedia )  _childMedia->release();

    // Call superclass's free.
    super::free();
}


IOMedia* com_MySoftwareCompany_driver_MyFilterScheme::getProvider(void)
    const
{

    return (IOMedia*) IOService::getProvider();
}


bool com_MySoftwareCompany_driver_MyFilterScheme::start(IOService* provider)
{
    //
    // Publish the new media object that represents the filtered content.
    //

    IOMedia* media = OSDynamicCast (IOMedia, provider);

    // State assumptions.

    assert(media);

    // Call superclass's start.

    if ( super::start(provider) == false )
        return false;

    // Attach and register the new media object.

    IOMedia* childMedia = new IOMedia;

    if ( childMedia )
    {
        if ( childMedia->init(
                /* base               */ 0,
                /* size               */ media->getSize(),
                /* preferredBlockSize */ media->getPreferredBlockSize(),
                /* isEjectable        */ media->isEjectable(),
                /* isWhole            */ false,
                /* isWritable         */ media->isWritable(),
                /* contentHint        */ "Apple_HFS" ) )
        {
            // Set a name for this partition.

            UInt32 partitionID = 1;

            char name[24];
            sprintf(name, "MySoftwareCompany_Filtered %ld", partitionID);
            childMedia->setName(name);

            // Set a location value (partition number) for this partition.

            char location[12];
            sprintf(location, "%ld", partitionID);
            childMedia->setLocation(location);

            // Attach the new media to this driver

            _childMedia = childMedia;

            childMedia->attach(this);

            // Move parent node to child node.
            (void) attachMediaObjectToDeviceTree(childMedia);

            // Publish the new media object.
            childMedia->registerService();

            return true;
        }
        else
        {
            childMedia->release();
            childMedia = 0;
        }
    }

    return false;
}

void com_MySoftwareCompany_driver_MyFilterScheme::stop(IOService* provider)
{
    // Clean up after the media object before terminating.

    // State assumptions.
    assert(_childMedia);

    // Detach the media object previously attached in start().
    if (_childMedia)
        detachMediaObjectFromDeviceTree(_childMedia);

    super::stop(provider);
}

bool com_MySoftwareCompany_driver_MyFilterScheme::handleOpen(IOService*
                                            client,
                                            IOOptionBits options,
                                            void* argument)
{
    return getProvider()->open(this, options, (IOStorageAccess) argument);
}


bool com_MySoftwareCompany_driver_MyFilterScheme::handleIsOpen(const
                                            IOService* client) const
{
    return getProvider()->isOpen(this);
}


void com_MySoftwareCompany_driver_MyFilterScheme::handleClose(IOService*
                                        client, IOOptionBits options)
{
    getProvider()->close(this, options);
}

bool com_MySoftwareCompany_driver_MyFilterScheme::attachMediaObjectToDeviceTree(
                                            IOMedia* media)
{
    //
    // Attach the given media object to the device tree plane.
    //

    IORegistryEntry* child;

    if ((child = getParentEntry(gIOServicePlane))) {

        IORegistryEntry* parent;

        if ((parent = child->getParentEntry(gIODTPlane))) {

            const char* location = child->getLocation(gIODTPlane);
            const char* name     = child->getName(gIODTPlane);

            if (media->attachToParent(parent, gIODTPlane)) {
                media->setLocation(location, gIODTPlane);
                media->setName(name, gIODTPlane);

                child->detachFromParent(parent, gIODTPlane);

                return true;
            }
        }
    }

    return false;
}

void com_MySoftwareCompany_driver_MyFilterScheme::detachMediaObjectFromDeviceTree
                                            (IOMedia* media)
{
    //
    // Detach the given media object from the device tree plane.
    //

    IORegistryEntry* child;

    if ((child = getParentEntry(gIOServicePlane))) {

        IORegistryEntry * parent;

        if ((parent = media->getParentEntry(gIODTPlane))) {

            const char* location = media->getLocation(gIODTPlane);
            const char* name     = media->getName(gIODTPlane);

            if (child->attachToParent(parent, gIODTPlane)) {
                child->setLocation(location, gIODTPlane);
                child->setName(name, gIODTPlane);
            }

            media->detachFromParent(parent, gIODTPlane);
        }
    }
}

void com_MySoftwareCompany_driver_MyFilterScheme::read(IOService* __attribute__ ((unused)) client,
                                        UInt64 byteStart,
                                        IOMemoryDescriptor* buffer,
                                        IOStorageCompletion completion)
{
    // Add filtering code here.
       getProvider()->read(this, byteStart, buffer, completion);
}


void com_MySoftwareCompany_driver_MyFilterScheme::write(IOService* __attribute__ ((unused)) client,
                                        UInt64 byteStart,
                                        IOMemoryDescriptor* buffer,
                                        IOStorageCompletion completion)
{
   // Add filtering code here.
    getProvider()->write(this, byteStart, buffer, completion);
}


IOReturn com_MySoftwareCompany_driver_MyFilterScheme::synchronizeCache(
                                                    IOService* client)
{
    return getProvider()->synchronizeCache(this);
}
```


To test the sample filter-scheme driver, you must first create a disk image for it to match on. You do this using the command-line tools `hdiutil`, which creates and manipulates disk images and `newfs_hfs`, which builds a file system on the disk image. For full documentation on these commands, see the `man` pages.

To create the disk image, open a window in the Terminal application (located at `/Applications/Utilities/Terminal`) and type the following commands.

```
$ hdiutil create -megabytes 5 -partitionType MySoftwareCompany_MyContent
                            ~/MySoftwareCompany_MyContent_Example.dmg
```

Then, you attach the disk image without mounting it, because it doesn’t yet contain a valid file system. In OS X version 10.2 and later, use this command:

```
$ hdiutil attach -nomount ~/MySoftwareCompany_MyContent_Example.dmg
```

In version of OS X prior to 10.2, use this command (the `-nomount` option was added in OS X version 10.2):

```
$ hdiutil attach ~/MySoftwareCompany_MyContent_Example.dmg
```

The `hdiutil attach` command displays the special device name that is associated with each partition on the disk image:

```
/dev/disk1          Apple_partition_scheme
/dev/disk1s1        Apple_partition_map
/dev/disk1s2        MySoftwareCompany_MyContent
```

Then, use the `newfs_hfs` command to create the file system on your disk image. Because you should always use the raw, uncached disk, you add an `r` to the disk node representing the partition with your content.

```
$ newfs_hfs -v "My_Volume_Name" /dev/rdisk1s2
```

The `-v` option allows you to specify a volume name.

After you’ve created the disk image and its file system, you can assume super user (or `root`) privileges and use the `kextload` command to load the sample filter-scheme driver. Alternately, if the `root` account owns the filter-scheme driver, you can copy it to `/System/Library/Extensions`, reboot, and the driver will load automatically.

To use the `kextload` command, type the following line in a Terminal window:

```
$ kextload -v MyFilterScheme.kext
```

The `-v` option makes `kextload` provide more verbose information.

After you’ve successfully loaded the driver, you can use Disk Copy to open the disk image (double-click on the disk image in the Finder).

[Next](Document%20Revision%20History.md)[Previous](Subclassing%20Protocol%20Services%20Drivers.md)

