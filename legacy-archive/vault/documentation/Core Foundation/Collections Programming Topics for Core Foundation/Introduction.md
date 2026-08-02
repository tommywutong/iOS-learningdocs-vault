---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html
archived_at: '2026-07-15T07:22:16.656660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Common%20Characteristics%20of%20Collections.md)

# Introduction

Core Foundation collection objects help you store, organize, and retrieve “quantities” of data of virtually all types. This topic describes objects that let you group together other types of objects in, for example, arrays, sets, or dictionaries.

Developers using Core Foundation for their base functionality need to understand how collections work.

In addition to organizing data for quick and accurate retrieval, collection objects bring several benefits to programming:

- They allow you to customize the automatic behavior of collections to suit the type of data stored ([Collection Customization](Collection%20Customization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztalkdjjbeksscjbea)).
- They can apply program-defined logic to all data elements in a collection ([Applying Program-Defined Functions to Collections](Applying%20Program-Defined%20Functions%20to%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztmlkdjjbekscbifdq)).
- They can ensure the uniqueness of data elements added to a collection.
- They enable you to modify (add, insert, delete, sort, and so forth) the data elements in a collection.
- They are essential to Core Foundation property lists, along with string objects (CFString), number objects (CFNumber and CFBoolean), and data objects (CFData). See _[Property List Programming Topics for Core Foundation](../Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i)_ for details.

Core Foundation defines several types of collection objects:

- Array objects (of the opaque type CFArray) organize elements by sequential position.
- Dictionary objects (of the opaque type CFDictionary) identify elements through an arbitrary key.
- Set objects (of the opaque type CFSet) are a collection of elements in which there are no duplicates.
- Bag objects (of the opaque type CFBag) are a collection of elements in which there can be duplicates.
- Tree objects (of the opaque type CFTree) organize elements in hierarchical (parent-children) relationships.

Collection objects, to some degree, are containers of values. (In this document, the word “value” denotes an element contained by a collection.) But there are wide differences in how collections contain and dispense their values. The organization of the concepts in this topic reflects these differences. What might be termed the “true collections”—arrays, dictionaries, sets, and bags—are described together because of their strong similarities. Then this topic goes on to describe trees, which are structurally quite different from the true collections.

The collections API allow you to do expected things with collection objects: create them, add values to them, extract values from them, and so on. Because the programming interfaces of CFArray, CFDictionary, CFSet, and CFBag are very much alike in what they do and how they do it, the following sections include all these types in their discussions. However, the programming interfaces of CFTree objects are sufficiently different that tasks related to these objects are described in [Creating and Using Tree Structures](Creating%20and%20Using%20Tree%20Structures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztolkdjjbekscbifdq).

[Next](Common%20Characteristics%20of%20Collections.md)

