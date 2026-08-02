---
title: File-System Performance Guidelines
apple_id: 10000161i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/FileSystem/Articles/MappingFiles.html
archived_at: '2026-07-18T01:48:44.019159Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File-System Performance Guidelines](Introduction%20to%20File-System%20Performance%20Guidelines.md)


[Next](Iterating%20Directory%20Contents.md)[Previous](Examining%20File-System%20Usage.md)

# Mapping Files Into Memory

File mapping is the process of mapping the disk sectors of a file into the virtual memory space of a process. Once mapped, your application accesses the file as if it were entirely resident in memory. As you read data from the mapped file pointer, the kernel pages in the appropriate data and returns it to your application.

Although mapping files can offer tremendous performance advantages, it is not appropriate in all cases. The following sections explain when file mapping can help you and how you go about doing it in your code.

When deciding whether or not to map files, keep in mind that the overall goal is to reduce transfers between disk and memory. File mapping can help you in some cases, but not all. The more of a file you map into memory, the less useful file mapping becomes.

Another thing to remember about mapped files is that they share the process space with system libraries, your application code, and allocated memory. Most applications have around 2 gigabytes of addressable memory, depending on the number of libraries they load. In order to map a file, there must be an available address range big enough to fit the file. Finding this much space can be difficult if your application’s virtual memory space is fragmented or you attempt to map a very large file.

Before you map any files into memory, make sure you understand your typical file usage patterns. Tools such as Shark and `fs_usage` can help you identify where your application accesses files and how long those operations take. For any operations that are taking longer than expected, you can then look at your code to determine if file mapping might be of use.

File mapping is effective in the following situations:

- You have a large file whose contents you want to access randomly one or more times.
- You have a small file whose contents you want to read into memory all at once and access frequently. This technique is best for files that are no more than a few virtual memory pages in size.
- 

  You want to cache specific portions of a file in memory. File mapping eliminates the need to cache the data at all, which leaves more room in the system disk caches for other data.

You should not use file mapping in the following situations:

- You want to read a file sequentially from start to finish only once.
- The file is several hundred megabytes or more in size. (Mapping large files fills virtual memory space quickly. In addition, your program may not have the available space if it has been running for a while or its memory space is fragmented.)

For large sequential read operations, you are better off disabling disk caching and reading the file into a small memory buffer. See [Cache Files Selectively](File-System%20Performance%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljzhe3tgmq) for more information.

Even in situations where you think file mapping is ideal, there are still some caveats that may apply. In particular, you may not want to map files in the following situations:

- The file is larger than the available contiguous virtual memory address space. Files whose size is several hundred megabytes or more fall into this category.
- The file is located on a removable drive.
- The file is located on a network drive.

When randomly accessing a very large file, it’s often a better idea to map only a small portion of the file at a time. The problem with mapping large files is that the file can occupy a significant portion of your application’s virtual address space. The address space for a single process is currently limited to 4 gigabytes, with some portions of that space reserved for various system frameworks and libraries. If you try to map a very large file, you might find there isn’t enough room to map the entire file anyway. This problem can also occur if you map too many files into your process space.

For files on removable or network drives, you should avoid mapping files altogether. If you map files on a removable or network drive and that drive is unmounted, or disappears for another reason, accessing the mapped memory can cause a bus error and crash your program. If you insist on mapping these types of files, be sure to install a signal handler in your application to trap and handle the bus error condition. Even with the signal handler installed, your application’s current thread may block until it receives a timeout from trying to access a network file. This timeout period can make your application appear hung and unresponsive and is easily avoided by not mapping the files in the first place.

Mapping a file on the root device is always safe. (If the root device is somehow removed or unavailable, the system cannot continue running.) Note that the user’s home directory is not required to be on the root device.

Mapping your data fork-based resource files into memory is often a good idea. Resource files typically contain frequently-used data that your application needs to operate. Because of its usefulness, OS X includes a mechanism to map resources automatically. To enable this mechanism, add the following lines to your `Info.plist` file:

```
<key>CSResourcesFileMapped</key>
<true/>
```

The CFBundle resource file functions (`CFBundleOpenBundleResourceMap` and `CFBundleOpenBundleResourceFiles`) check for the `CSResourcesFileMapped` key before opening a resource file. If this key is present and set to true, the functions map the resource file into memory. The resource data is mapped read-only, so you cannot write to the file or any of its resources directly. For example, the following will cause an memory access exception if the `PICT` resource comes from a mapped resource file:

```
PicHandle picture = (PicHandle)GetResource(‘PICT’, 128);
(**picture).rect = myRect; // crash here attempting to write
                            // to read-only memory
```


[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4taljrga2dknbxfvbecssiiffeoqi) demonstrates the BSD routines `mmap` and `munmap` to map and unmap files. The mapped file occupies a system-determined portion of the application’s virtual address space until `munmap` is used to unmap the file.

__Listing 1__  Mapping a file into virtual memory

```
void ProcessFile( char * inPathName )
{
    size_t dataLength;
    void * dataPtr;

    if( MapFile( inPathName, &dataPtr, &dataLength ) == 0 )
    {
        //
        // process the data and unmap the file
        //

        // . . .

        munmap( dataPtr, dataLength );
    }
}


// MapFile
// Return the contents of the specified file as a read-only pointer.
//
// Enter:inPathName is a UNIX-style “/”-delimited pathname
//
// Exit:    outDataPtra     pointer to the mapped memory region
//          outDataLength   size of the mapped memory region
//          return value    an errno value on error (see sys/errno.h)
//                          or zero for success
//
int MapFile( char * inPathName, void ** outDataPtr, size_t * outDataLength )
{
    int outError;
    int fileDescriptor;
    struct stat statInfo;

    // Return safe values on error.
    outError = 0;
    *outDataPtr = NULL;
    *outDataLength = 0;

    // Open the file.
    fileDescriptor = open( inPathName, O_RDONLY, 0 );
    if( fileDescriptor < 0 )
    {
       outError = errno;
    }
    else
    {
        // We now know the file exists. Retrieve the file size.
        if( fstat( fileDescriptor, &statInfo ) != 0 )
        {
            outError = errno;
        }
        else
        {
            // Map the file into a read-only memory region.
            *outDataPtr = mmap(NULL,
                                statInfo.st_size,
                                PROT_READ,
                                0,
                                fileDescriptor,
                                0);
            if( *outDataPtr == MAP_FAILED )
            {
                outError = errno;
            }
            else
            {
                // On success, return the size of the mapped file.
                *outDataLength = statInfo.st_size;
            }
        }

        // Now close the file. The kernel doesn’t use our file descriptor.
        close( fileDescriptor );
    }

    return outError;
}
```

[Next](Iterating%20Directory%20Contents.md)[Previous](Examining%20File-System%20Usage.md)

