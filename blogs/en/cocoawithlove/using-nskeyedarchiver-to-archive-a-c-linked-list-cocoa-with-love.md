---
title: 'Using NSKeyedArchiver to archive a C linked-list | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/03/using-nskeyedarchiver-to-archive-c.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c1e31eefead0911e'
translated: false
---

> 原文：[Using NSKeyedArchiver to archive a C linked-list | Cocoa with Love](https://www.cocoawithlove.com/2009/03/using-nskeyedarchiver-to-archive-c.html)　·　Cocoa with Love (Matt Gallagher)

`NSKeyedArchiver` provides some support for archiving C primitive types but provides no support for pointers to C structs. I'll show you how you can archive a linked list of C structs, despite the lack of support in `NSKeyedArchiver`.

## Standard C

Cocoa contains very little support for standard C data structures. The reason for this is pretty simple: introspection. An Objective-C object can report on what it is, its block size, its ivars and methods. Protocols can be implemented to provide further metadata about the object. With a pointer to an arbitrary block of standard C data, you have no information at all about the type and structure of the block.

While keeping all your data in Objective-C objects works well most of the time, sometimes you'll need to work with standard C data structures — for example when working with data produced by third party libraries.

To show how to use C data structures with libraries that expect Objective-C objects, I'll show you how to archive a linked-list of C structs using `NSKeyedArchiver`.

## Metadata and wrappers

As I mentioned, the real problem with arbitrary C data is that it offers no introspection — we must be able to ask our data about its metadata. Specifically, we will need to know the size of the list node structs (we can copy the whole struct as a block of data) and the offsets within the struct of pointers to other list nodes.

In addition to metadata, we need a way to deal with pointers. `NSKeyedArchiver` provides no way to encode an arbitrary pointer.

To handle both these problems, the solution will use one Objective-C "wrapper" object to represent each struct, and one extra "context" object to encode data about the overall archive operation.

The context object will encode the size of the struct and byte offsets of each pointer within the struct (since this data is stored once, not per object, we assume that every node in the linked list is the same type).

The wrapper objects for each struct will serve two purposes: they will handle the encoding of each struct's data but they will also act as proxies for the pointers between structs — allowing us to encode pointers to objects (permitted by `NSKeyedArchiver`) instead of pointers to structs (not permitted).

To allow the wrapper objects to act as proxies for each pointer, we will also need a dictionary that stores the mapping from struct to associated proxy object — this mapping will be held in the context object.

## Interface design

```objc
@interface BlockWrapper : NSObject &lt;NSCoding&gt;
{
    BlockContext *blockContext;
    void *blockPointer;
}

@property (readonly) void *blockPointer;

- (id)initWithBlockContext:(BlockContext *)aBlockContext
    blockPointer:(void *)aBlockPointer;

@end
```

The data for the wrapper object is very simple: a `blockPointer` that points to the data that the object will encode and `blockContext` which points to the context object for the archive operation.

I decided to name this class `BlockWrapper` instead of `StructWrapper` to properly reflect how the class handles the data it wraps — as an arbitrary block of bytes.

```objc
@interface BlockContext : NSObject &lt;NSCoding&gt;
{
    CFMutableDictionaryRef blockToBlockWrapperMappings;
    void *startingBlock;
    size_t blockSize;
    NSArray *pointerOffsets;
}

@property (readonly) size_t blockSize;
@property (readonly) void *startingBlock;
@property (readonly, retain, nonatomic) NSArray *pointerOffsets;

- (id)initWithStartingBlock:(void *)aStartingBlock
    blockSize:(size_t)aBlockSize
    pointerOffsets:(NSArray *)aPointerOffsets;
- (BlockWrapper *)wrapperForBlock:(void *)aBlock;

@end
```

The `BlockContext` class is fairly straightforward as well: it encodes all the previously discussed metadata about the block.

Since I wanted this code to work for _any_ linked list node, I haven't hard-coded the number or location of pointers within each block — I store the offsets of each pointer as an array.

The `wrapperForBlock:` will be the correct way to find the `BlockWrapper` object for any of our list node pointers. This method will return the corresponding `BlockWrapper` from the `blockToBlockWrapperMappings`, creating a new `BlockWrapper` if one does not already exist for the given list node pointer.

Notice that I use a `CFMutableDictionaryRef` instead of an `NSDictionary`. This is because the keys in this dictionary will be the pointers to the blocks, not Objective-C objects, and `NSDictionary` requires that its keys be Objective-C objects. With `CFMutableDictionaryRef`, we can configure the dictionary to handle raw pointers.

Despite containing all this metadata during the encoding process, for its own encoding, the `BlockContext` only needs to save the `startingBlock` and `pointerOffsets`. The `NSKeyedArchiver` will implicitly store the `blockSize` for each encoded block and the mappings from `BlockWrapper` to pointer.

## Encoding and decoding the BlockWrapper

```objc
- (void)encodeWithCoder:(NSCoder *)encoder
{
    [encoder encodeBytes:blockPointer length:[blockContext blockSize] forKey:@"block"];
    [encoder encodeObject:blockContext forKey:@"blockContext"];

    NSMutableArray *blockWrapperArray =
        [NSMutableArray arrayWithCapacity:[[blockContext pointerOffsets] count]];

    for (NSNumber *offsetNumber in [blockContext pointerOffsets])
    {
        NSUInteger offset = [offsetNumber integerValue];
        void *childBlock = *(void **)((NSUInteger)blockPointer + offset);
        if (!childBlock)
        {
            [blockWrapperArray addObject:[NSNull null]];
            continue;
        }

        BlockWrapper *childWrapper = [blockContext wrapperForBlock:childBlock];
        [blockWrapperArray addObject:childWrapper];
    }
    
    [encoder encodeObject:blockWrapperArray forKey:@"childBlocks"];
}
```

Encoding the block itself and storing a pointer to the `BlockContext` is simple. Most of the work in encoding relates to handling pointers to other nodes:

- get each pointer offset
- reading the value of the pointer from the block
- map the pointer's value to a `BlockWrapper` object using the `blockContext`
- encoding each referenced `BlockWrapper` in an `NSArray` using the `childBlocks` key

Notice that `NULL` pointers still require a `NSNull` object in the `childBlocks` array so that the indices in this array always correspond to the indices in the `pointerOffsets` array.

The decode process for `BlockWrapper` is mostly the same work in reverse: decode the block, decode the reference to the context object and then set all of the pointers according to the decoded `childBlocks` array.

```objc
- (id)initWithCoder:(NSCoder *)decoder
{
    self = [super init];
    if (self != nil)
    {
        NSUInteger blockSize;
        const void *bytes =
            [decoder decodeBytesForKey:@"block" returnedLength:&blockSize];
        blockPointer = malloc(blockSize);
        memcpy(blockPointer, bytes, blockSize);
        
        BlockContext *context = [decoder decodeObjectForKey:@"blockContext"];

        NSArray *childBlocks = [decoder decodeObjectForKey:@"childBlocks"];
        NSArray *pointerOffsets = [context pointerOffsets];
        NSInteger i;
        NSInteger count = [childBlocks count];
        
        NSAssert(count == [pointerOffsets count],
            @"Mismatch between childBlocks and pointerOffsets");
        
        for (i = 0; i &lt; count; i++)
        {
            BlockWrapper *wrapperObject = [childBlocks objectAtIndex:i];
            NSNumber *offsetNumber = [pointerOffsets objectAtIndex:i];
            NSUInteger offset = [offsetNumber integerValue];
            
            void *childPointer = 0;
            if (![wrapperObject isEqual:[NSNull null]])
            {
                childPointer = [wrapperObject blockPointer];
            }
            
            *(void **)((NSUInteger)blockPointer + offset) = childPointer;
        }
    }
    return self;
}
```

The biggest difference between decoding and encoding is that in decoding, we need to `malloc` the memory for the list node (pointed to by `blockPointer`). When encoding, this memory was allocated externally before we began.

The result is that the code which unarchives the linked list is also responsible for `free`-ing it.

## Conclusion

> Download the complete solution (which includes a trivial sample program) [LinkedListCoding.zip](https://www.cocoawithlove.com/assets/objc-era/LinkedListCoding.zip) (48kB)

This solution will let you archive an arbitrary linked list of C structs using `NSKeyedArchiver`. The solution does make some assumptions — specifically, your list nodes must all be the same type and the only pointers must point to other list nodes or `NULL`. Other list arrangements would require changes to the solution.

Of course, this solution is not as elegant as avoiding linked lists altogether. If you have control over the code and it's simple enough, storing `NSObject` in an `NSMutableArray` is much better supported by Cocoa.
