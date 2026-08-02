---
title: File-System Performance Guidelines
apple_id: 10000161i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/FileSystem/Articles/IteratingFiles.html
archived_at: '2026-07-18T01:48:41.532091Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File-System Performance Guidelines](Introduction%20to%20File-System%20Performance%20Guidelines.md)


[Next](Resolving%20Domain%20Names.md)[Previous](Mapping%20Files%20Into%20Memory.md)

# Iterating Directory Contents

Iterating the file system should be avoided whenever possible. Iterating the file system reads in metadata for a large number of files and fills up the system disk caches with data that will likely be used only once. If you must iterate directories repeatedly, consider caching the results from previous iterations to avoid repeated calls to the `stat` function.

When iterating over a large number of files, your best choice is to use the more efficient low-level routines provided by both Carbon and the BSD system. The following sections describe the basic techniques for using these routines.

The example in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4tcljzha4dsobnijauurkdi5dem) demonstrates how to use an HFS Plus bulk iterator to efficiently scan the contents of a directory. It does not descend into subdirectories, but you can open as many bulk iterators as necessary to handle recursive iteration. For information on scanning a directory repeatedly to watch for changes, [Tracking File-System Changes](Tracking%20File-System%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4tglkdjjbeursjirca).

__Listing 1__  Fast directory iteration

```c
#include <CoreServices/CoreServices.h>

// Forward declarations.
OSStatus IterateFolder( FSRef * inFolder );
void DoSomethingWithThisObject( const FSCatalogInfo * inCatInfo );

int main(void)
{
    OSStatus    outStatus;
    FSRef       folderRef;

    printf("begin file iteration!\n");
    fflush( stdout );

    //
    // Get the current user’s documents folder,
    // make it into an FSRef, and iterate it
    //
    outStatus = FSFindFolder(kUserDomain, kDocumentsFolderType, false, &folderRef);
    if( outStatus == noErr )
    {
        outStatus = IterateFolder( &folderRef );
    }

    printf( "final error status is (#%d)\n", (int)outStatus );
    return 0;
}

OSStatus IterateFolder( FSRef * inFolder )
{
    OSStatus outStatus;

    // Get permissions and node flags and Finder info
    //
    // For maximum performance, specify in the catalog
    // bitmap only the information you need to know
    FSCatalogInfoBitmap kCatalogInfoBitmap = (kFSCatInfoNodeFlags |
                                             kFSCatInfoFinderInfo);

    // On each iteration of the do-while loop, retrieve this
    // number of catalog infos
    //
    // We use the number of FSCatalogInfos that will fit in
    // exactly four VM pages (#113). This is a good balance
    // between the iteration I/O overhead and the risk of
    // incurring additional I/O from additional memory
    // allocation
    const size_t kRequestCountPerIteration = ((4096 * 4) / sizeof(FSCatalogInfo));
    FSIterator iterator;
    FSCatalogInfo * catalogInfoArray;

    // Create an iterator
    outStatus = FSOpenIterator( inFolder, kFSIterateFlat, &iterator );

    if( outStatus == noErr )
    {
        // Allocate storage for the returned information
        catalogInfoArray = (FSCatalogInfo *) malloc(sizeof(FSCatalogInfo) *
                            kRequestCountPerIteration);

        if( catalogInfoArray == NULL )
        {
            outStatus = memFullErr;
        }
        else
        {
            // Request information about files in the given directory,
            // until we get a status code back from the File Manager
            do
            {
                ItemCount actualCount;

                outStatus = FSGetCatalogInfoBulk(iterator, kRequestCountPerIteration,
                                    &actualCount, NULL, kCatalogInfoBitmap,
                                    catalogInfoArray, NULL, NULL, NULL );

                // Process all items received
                if( outStatus == noErr || outStatus == errFSNoMoreItems )
                {
                    UInt32  index;

                    for( index = 0; index < actualCount; index += 1 )
                    {
                        // Do something interesting with the object found
                        DoSomethingWithThisObject( &catalogInfoArray[ index ] );
                    }
                }


            }
            while( outStatus == noErr );

            // errFSNoMoreItems tells us we have successfully processed all
            // items in the directory -- not really an error
            if( outStatus == errFSNoMoreItems )
            {
                outStatus = noErr;
            }

            // Free the array memory
            free( (void *) catalogInfoArray );
        }
    }

    FSCloseIterator(iterator);

    return outStatus;
}

void DoSomethingWithThisObject( const FSCatalogInfo * inCatInfo )
{
    if( (inCatInfo->nodeFlags & kFSNodeIsDirectoryMask) == kFSNodeIsDirectoryMask )
    {
        printf( "Found a folder\n" );
    }
    else
    {
        FInfo * theFinderInfo;
        OSType type;

        theFinderInfo = (FInfo *)&inCatInfo->finderInfo[0];
        type = theFinderInfo->fdType;

        printf( "Found a file (type %c%c%c%c)\n",
                (char) ((type & 0xFF000000) >> 24),
                (char) ((type & 0x00FF0000) >> 16),
                (char) ((type & 0x0000FF00) >> 8),
                (char) (type & 0x000000FF)
                 );
    }
}
```


A reasonably fast way to traverse a directory hierarchy is to use the BSD-level `fts` routines. Like the Carbon catalog iterators, these routines let you walk a file hierarchy and examine each file and directory. Unlike the Carbon catalog iterators, you cannot use the `fts` routines to retrieve a file’s Finder type or a directory’s valence. To gather information of that nature, you must call additional routines, which adds an additional expense.

For detailed information on how to use the BSD `fts` routines, see the `fts(3)` man page entry.

If you need to search for information on a hard disk, consider using the Carbon `FSCatalogSearch` function. This function is optimized for reading the disk catalog information and is significantly faster than iterating the directories yourself and searching for the information.

Whenever you iterate the contents of a directory, you should be careful to check your virtual memory usage in `top`. If you notice your memory usage increasing during the iteration cycle, you may want to use Shark, MallocDebug, or ObjectAlloc to investigate your allocation patterns further. A significant increase in the number of resident memory pages during your iteration could cause paging to occur in low-memory situations.

If you find your memory allocation or usage increasing during an iteration, you should examine ways to reduce your overall memory consumption. Rather than allocating new memory for storing data, try to recycle existing memory blocks or eliminate specific allocations altogether. The example in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4tcljzha4dsobnijauurkdi5dem) shows an efficient way to maintain a low memory footprint for Carbon-based iterators. For Cocoa applications using an NSFileManager object to walk the items in a directory, consider adding an NSAutoreleasePool inside your iteration loop to reclaim any released objects.

[Next](Resolving%20Domain%20Names.md)[Previous](Mapping%20Files%20Into%20Memory.md)

