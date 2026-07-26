---
title: CFTree
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftree
source_url: 'https://developer.apple.com/documentation/corefoundation/cftree'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftree.json'
content_hash: 'sha256:e5cfe6c7132c6184'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTree

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFTree
```

## Overview

You use CFTree to create tree structures that represent hierarchical organizations of information. In such structures, each tree node has exactly one parent tree (except for the root tree, which has no parent) and can have multiple children. Each CFTree object in the structure has a context associated with it; this context includes some program-defined data as well as callbacks that operate on that data. The program-defined data is often used as the basis for determining where CFTree objects fit within the structure. All CFTree objects are mutable.

You create a CFTree object using the [CFTreeCreate](<cftreecreate(____).md>) function. This function takes an allocator and pointer to a [CFTreeGetContext](<cftreegetcontext(____).md>) structure as parameters. The [CFTreeContext](cftreecontext.md) structure contains the program-defined data and callbacks needed to describe, retain, and release that data. If you do not implement these callbacks, your program-defined data will not be retained or released when trees are added and removed from a parent.

Each CFTree object has a parent and list of children, all of which may be `NULL`. CFTree provides functions for adding and removing tree objects from the tree structure. Use the [CFTreeAppendChild](<cftreeappendchild(____).md>), [CFTreeInsertSibling](<cftreeinsertsibling(____).md>), or [CFTreePrependChild](<cftreeprependchild(____).md>) functions to add trees to a tree structure, and the [CFTreeRemove](<cftreeremove(__).md>) or [CFTreeRemoveAllChildren](<cftreeremoveallchildren(__).md>) functions to remove trees.

For the purposes of memory management, CFTree can be thought of as a collection. Typically the only object that retains a child tree is its parent. Usually, therefore, when you remove a child tree from a tree, the child tree is destroyed. If you want to use a child tree after you remove it from its parent, you should retain the child tree first, prior to removing it.

Releasing a tree releases its child trees, and all of their child trees (recursively). Note also that the final release of a tree (when its retain count decreases to zero) causes all of its child trees, and all of their child trees (recursively), to be destroyed, regardless of their retain counts. Releasing a child that is still in a tree is therefore a programming error, and may cause your application to crash.

You can use any of the get functions (functions containing the word “Get”) to obtain the parent, children, or attributes of a tree. For example, use [CFTreeGetChildAtIndex](<cftreegetchildatindex(____).md>) to obtain a child of a tree at a specified location. In common with other Core Foundation “Get” functions, these functions do not retain the tree that is returned. If you are making other modifications to the tree, you should either retain or make a deep copy of the child tree returned.

You can apply a function to all children of a tree using the [CFTreeApplyFunctionToChildren](<cftreeapplyfunctiontochildren(______).md>) function, and sort children of a tree using the [CFTreeSortChildren](<cftreesortchildren(______).md>) function.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Trees

- [CFTreeCreate](<cftreecreate(____).md>) — Creates a new CFTree object.

### Modifying a Tree

- [CFTreeAppendChild](<cftreeappendchild(____).md>) — Adds a new child to a tree as the last in its list of children.
- [CFTreeInsertSibling](<cftreeinsertsibling(____).md>) — Inserts a new sibling after a given tree.
- [CFTreeRemoveAllChildren](<cftreeremoveallchildren(__).md>) — Removes all the children of a tree.
- [CFTreePrependChild](<cftreeprependchild(____).md>) — Adds a new child to the specified tree as the first in its list of children.
- [CFTreeRemove](<cftreeremove(__).md>) — Removes a tree from its parent.
- [CFTreeSetContext](<cftreesetcontext(____).md>) — Replaces the context of a tree by releasing the old information pointer and retaining the new one.

### Sorting a Tree

- [CFTreeSortChildren](<cftreesortchildren(______).md>) — Sorts the immediate children of a tree using a specified comparator function.

### Examining a Tree

- [CFTreeFindRoot](<cftreefindroot(__).md>) — Returns the root tree of a given tree.
- [CFTreeGetChildAtIndex](<cftreegetchildatindex(____).md>) — Returns the child of a tree at the specified index.
- [CFTreeGetChildCount](<cftreegetchildcount(__).md>) — Returns the number of children in a tree.
- [CFTreeGetChildren](<cftreegetchildren(____).md>) — Fills a buffer with children from the tree.
- [CFTreeGetContext](<cftreegetcontext(____).md>) — Returns the context of the specified tree.
- [CFTreeGetFirstChild](<cftreegetfirstchild(__).md>) — Returns the first child of a tree.
- [CFTreeGetNextSibling](<cftreegetnextsibling(__).md>) — Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [CFTreeGetParent](<cftreegetparent(__).md>) — Returns the parent of a given tree.

### Performing an Operation on Tree Elements

- [CFTreeApplyFunctionToChildren](<cftreeapplyfunctiontochildren(______).md>) — Calls a function once for each immediate child of a tree.

### Getting the Tree Type ID

- [CFTreeGetTypeID](<cftreegettypeid().md>) — Returns the type identifier of the CFTree opaque type.

### Callbacks

- [CFTreeApplierFunction](cftreeapplierfunction.md) — Type of the callback function used by the CFTree apply function.
- [CFTreeCopyDescriptionCallBack](cftreecopydescriptioncallback.md) — Callback function used to provide a description of the program-defined information pointer.
- [CFTreeReleaseCallBack](cftreereleasecallback.md) — Callback function used to release a previously retained program-defined information pointer.
- [CFTreeRetainCallBack](cftreeretaincallback.md) — Callback function used to retain a program-defined information pointer.

### Data Types

- [CFTreeContext](cftreecontext.md) — Structure containing program-defined data and callbacks for a CFTree object.

## See Also

### Related Documentation

- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
