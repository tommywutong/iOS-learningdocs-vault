---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/usingtrees.html
archived_at: '2026-07-15T07:22:16.647436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Applying%20Program-Defined%20Functions%20to%20Collections.md)

# Creating and Using Tree Structures

With the CFTree opaque type you can create tree structures in memory to represent hierarchical organizations of information. In such structures, each tree node has exactly one parent tree (except for the root tree, which has no parent) and can have multiple child trees. Each CFTree object in the extended structure has a context associated with it; this context includes some program-defined data as well as callbacks that operate on that data. The program-defined data is often used to store information about each node in the structure.

This task discusses how to create CFTree objects, fit them into the structure of trees, and then later find, get, and modify them. The first parameter of most CFTree functions is a reference to a _parent_ CFTree object; the operation itself usually involves one or more children of that parent. In other words, most CFTree routines work “down” the hierarchy from a given parent but affect only the children of that parent.

One important fact to remember with working with CFTree objects is that functions that operate on children are not recursive. They affect only the immediate child trees. If you want to traverse all subtrees from any given parent node, your code must supply the traversal
logic.

Before you can create a CFTree object you must define its context. This means you must declare and initialize a structure of `CFTreeContext`. This structure has the following definition:

```
typedef struct {
    CFIndex version;
    void *info;
    const void *(*retain)(const void *info);
    void (*release)(const void *info);
    CFStringRef (*copyDescription)(const void *info);
} CFTreeContext;
```

The `info` member of this structure points to data that you define (and allocate, if necessary). The other members of the context structure (except for the version member) point to functions that take the `info` pointer as an argument and perform specific operations related to the pointed-to data, such as retaining it, releasing it, and describing it.

When you’ve properly initialized a `CFTreeContext` structure, call the `CFTreeCreate` function, passing in a pointer to the structure. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztoljrgaytanztfvbuqrceircusri) gives an example of this technique.

__Listing 1__  Creating a CFTree object

```swift
static CFTreeRef CreateMyTree(CFAllocatorRef allocator) {
    MyTreeInfo *info;
    CFTreeContext ctx;
    info = CFAllocatorAllocate(allocator, sizeof(MyTreeInfo), 0);
    info->address = 0;
    info->symbol = NULL;
    info->countCurrent = 0;
    info->countTotal = 0;
    ctx.version = 0;
    ctx.info = info;
    ctx.retain = AllocTreeInfo;
    ctx.release = FreeTreeInfo;
    ctx.copyDescription = NULL;
    return CFTreeCreate(allocator, &ctx);
}
```

As this example shows, you can initialize the function-pointer members of the `CFTreeContext` structure to `NULL` if you do not want to define callback functions for the CFTree object’s
context.

To be of any use, a CFTree object must be inserted into the tree structure; it must be placed in a hierarchical relationship to other CFTree objects. To do this, you must use one of the following CFTree functions to make the object a child or sibling tree in relation to some other tree:

- `CFTreeAppendChild`
- `CFTreePrependChild`
- `CFTreeInsertSibling`

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztoljrgaytemryfvbuqrccifdumqi) shows a child tree being appended to its parent’s list of children.

__Listing 2__  Adding a child CFTree to its parent

```swift
/* assume anAddress and curTree already exist */
CFTreeRef child = FindTreeChildWithAddress(curTree, anAddress);if (NULL == child) {
    CFTreeContext ctx;
    child = CreateMyTree(CFGetAllocator(curTree));
    CFTreeGetContext(child, &ctx);
    ((MyTreeInfo *)ctx.info)->address = anAddress;
    CFTreeAppendChild(curTree, child);
    CFRelease(child);
}
```

The code example also illustrates another aspect of the CFTree programming interface. Sometimes you may need to modify the program-defined data associated with a CFTree object that is already created. To do this, call the `CFTreeGetContext` function on that object to get the tree’s context. Once you have this structure, you can access the program-defined data through the `info` pointer.

The CFTree type has several functions that obtain child trees. Because sibling trees are in sequential order, you typically use only two of these methods to traverse the child trees of one parent, `CFTreeGetFirstChild` and `CFTreeGetNextSibling`. [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztoljrgaytgnjxfvbuqrceinauqsq) shows how you do this.

__Listing 3__  Traversing the child trees of a parent tree

```swift
static CFTreeRef FindTreeChildWithAddress(CFTreeRef tree, UInt32 addr) {
    CFTreeRef curChild = CFTreeGetFirstChild(tree);
    for (; curChild; curChild = CFTreeGetNextSibling(curChild)) {
        CFTreeContext ctx;
        CFTreeGetContext(tree, &ctx);
        if (((MyTreeInfo *)ctx.info)->address == addr) {
            return curChild;
        }
    }
    return NULL;
}
```

Not all CFTree functions act on or return child trees. The `CFTreeGetParent` function, for example, obtains the parent tree of a given tree. The `CFTreeFindRoot` function obtains the root CFTree object of the current tree structure—that is, the tree of the structure that has no parent tree.

The CFTree type includes two functions that are very similar to other collection functions. The `CFTreeApplyFunctionToChildren` function applies a program-defined applier function to the children of a parent CFTree object. The `CFTreeSortChildren` function sorts the children of a parent CFTree object using a comparator function that you can define (or employ, as long as it conforms to the `CFComparatorFunction` type).

- See [Applying Program-Defined Functions to Collections](Applying%20Program-Defined%20Functions%20to%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztmlkdjjbekscbifdq) for usage details pertinent to `CFTreeApplyFunctionToChildren`.
- See [Working With Mutable Collections](Working%20With%20Mutable%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztklkdjjbekscbifdq) for information on using the `CFArraySortValues` function; much of this information is applicable to the `CFTreeSortChildren` function.

[Next](Document%20Revision%20History.md)[Previous](Applying%20Program-Defined%20Functions%20to%20Collections.md)

