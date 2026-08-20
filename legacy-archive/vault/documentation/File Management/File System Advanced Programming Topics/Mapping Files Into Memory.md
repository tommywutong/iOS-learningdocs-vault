---
title: File System Advanced Programming Topics
apple_id: TP40010765
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemAdvancedPT/MappingFilesIntoMemory/MappingFilesIntoMemory.html
archived_at: '2026-07-15T07:31:56.774733Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Advanced Programming Topics](About%20Advanced%20File%20System%20Topics.md)



# Mapping Files Into Memory

File mapping is the process of mapping the disk sectors of a file into the virtual memory space of a process. Once mapped, your app accesses the file as if it were entirely resident in memory. As you read data from the mapped file pointer, the kernel pages in the appropriate data and returns it to your app.

Although mapping files can offer tremendous performance advantages, it’s not appropriate in all cases. The following sections explain when file mapping can help you and how you go about doing it in your code.

The goal is to reduce transfers between disk and memory. File mapping can help you in some cases, but not all. The more of a file you map into memory, the less useful file mapping becomes.

Before you map any files into memory, make sure you understand your typical file usage patterns. Use instruments to help you identify where your application accesses files and how long those operations take.

File mapping is effective when:

- You have a large file whose contents you want to access randomly one or more times.
- You have a small file whose contents you want to read into memory all at once and access frequently. This technique is best for files that are no more than a few virtual memory pages in size.
- You want to cache specific portions of a file in memory. File mapping eliminates the need to cache the data at all, which leaves more room in the system disk caches for other data.

When randomly accessing a very large file, it’s often a better idea to map only a small portion of the file at a time. The problem with mapping large files is that the file consumes active memory. If the file is large enough, the system might be forced to page out other portions of memory to load your file. Mapping more than one file into memory just compounds this problem.

Don’t use file mapping when:

- You want to read a file sequentially from start to finish only once.
- The file is several hundred megabytes or more in size. Mapping large files into memory fills memory quickly and may lead to paging, which would negate the benefits of mapping the file in the first place. For large sequential read operations, disable disk caching and read the file into a small memory buffer instead.
- The file is larger than the available contiguous virtual memory address space. This is less of an issue for 64-bit applications but can be an issue for 32-bit applications.
- The file is located on a removable drive.
- The file is located on a network drive.

If you map files on a removable or network drive and that drive is unmounted, or disappears for another reason, accessing the mapped memory can cause a bus error and crash your program.

Listing 1-1 demonstrates memory mapping using the BSD-level `mmap` and `munmap` functions. The mapped file occupies a system-determined portion of the application’s virtual address space until `munmap` is used to unmap the file. For more information about these functions, see [mmap](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mmap.2.html#//apple_ref/doc/man/2/mmap) and [munmap](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/munmap.2.html#//apple_ref/doc/man/2/munmap).

__Listing 1-1__  Mapping a file into virtual memory

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


