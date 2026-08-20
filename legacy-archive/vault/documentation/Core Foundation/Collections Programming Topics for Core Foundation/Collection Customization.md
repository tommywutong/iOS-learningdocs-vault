---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/custom.html
archived_at: '2026-07-15T07:22:14.137835Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Creating%20and%20Copying%20Collections.md)[Previous](Types%20of%20Collections.md)

# Collection Customization

Core Foundation permits you to customize
how collections operate on the values they contain. When you create
a collection object you must pass in an initialized structure that includes
pointers to callback functions that define much of the behavior
of the collection. The type of structure passed in for tree objects
is different from the structure passed in for the other types of
collection objects.

For arrays, dictionaries, sets, and bags, you pass a pointer
to a callback structure (for example, `CFArrayCallBacks`)
into the creation function. This structure contains pointers to functions
that are invoked by Core Foundation to retain, release, describe,
and compare the values put into the collection. Ideally the behavior
of a collection is to somehow retain a value put into it so that,
in case the code that put the value there later frees it, the value still
remains in the collection. (You can elect not to retain values put
into a collection, but this can lead to undefined behavior in your
program.) A collection should release values removed from it if
they were earlier retained, or free them if they were earlier allocated. The
callback that compares values is used in sorting and searching operations.
The callback that describes values is invoked by the `CFCopyDescription` (which
is invoked in turn by `CFShow`)
to print debugging information to the console.

For trees, you pass an initialized context structure (`CFTreeContext`)
into the creation function. This structure has pointers to the same
kinds of functions as the callback structure—retain, release,
compare, and describe—but these functions operate on an `info` member
of the context structure, which holds or points to the data associated
with the tree.

You may assign `NULL` to
a callback or context function pointer if the operation is not required
for the values in the collection (such as retaining certain types
of data). In addition, each collection object created with a callback
structure—arrays, dictionaries, sets, and bags—allows you to
specify a predefined structure initialized with default callbacks when
the collection contains Core Foundation objects.

[Next](Creating%20and%20Copying%20Collections.md)[Previous](Types%20of%20Collections.md)

