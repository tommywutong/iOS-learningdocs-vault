---
title: 'Implementing countByEnumeratingWithState:objects:count: | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/implementing-countbyenumeratingwithstat.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:09990ef4b0c1ecb0'
translated: false
---

> 原文：[Implementing countByEnumeratingWithState:objects:count: | Cocoa with Love](https://www.cocoawithlove.com/2008/05/implementing-countbyenumeratingwithstat.html)　·　Cocoa with Love (Matt Gallagher)

If you want to use fast enumeration on your own classes, you must implement countByEnumeratingWithState:objects:count:. Unfortunately, it's a confusing method. Here are two sample implementations that show the steps needed to implement this method in most cases.

## Some sample NSFastEnumeration implementations

You need to implement NSFastEnumeration if you want to use your own classes in the Objective-C 2.0 "for...in" fast-enumeration language feature.

The documentation for its only method (countByEnumeratingWithState:objects:count:) is pretty cryptic and overwhelming — mostly because the method needs to be flexible and Apple don't want to tell you how to write your code. I have no such qualms and since there aren't many examples on the Internets at the moment I thought I'd show you some easy approaches for implementing it in your own programs.

There are two different ways to enumerate. The first is where your class already has, or is willing to create, a C array of Objective-C id values which point to the objects being enumerated. The second is where you don't have this storage and want to use storage passed to you.

> These examples do not use the
> 
> mutationsPtr
> 
> and are therefore only safe for use with
> 
> collections. If the enumerated collection is
> 
> , you will need to point
> 
> mutationsPtr
> 
> to an appropriate mutation guard value (normally a mutations count value).

## First case: already have a C array of storage

Our class looks like this:

```objc
@interface SimpleStringArray : NSObject &lt;NSFastEnumeration&gt;
{
    NSString *stringArray[ARRAY_LENGTH];
}
```

In this case, the implementation of countByEnumeratingWithState:objects:count: would look like this:

```objc
- (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len
{
    if (state->state >= ARRAY_LENGTH)
    {
        return 0;
    }

    state->itemsPtr = stringArray;
    state->state = ARRAY_LENGTH;
    state->mutationsPtr = (unsigned long *)self;
    
    return ARRAY_LENGTH;
}
```

Quick explanation:

- stackbuf

  and

  count

  (because we already have storage)
- state-\>state

  to a non zero value (the iteration index after the current items are iterated)
- state-\>mutationsPtr

  to a non zero value (the self pointer since we have no "array has changed" flag that we can point it to)
- state-\>state

  will equal ARRAY_LENGTH and we'll return "0", ending the loop)

## Second case: need storage

If our class' data is a collection of NSString objects stored in a list of linearly connected C structs, then we might have no C array value to return.

Assume our list is declared like this:

```objc
typedef struct
{
    NSString * stringPtr;
    struct MyList * nextNode;
} MyList;
```

and our class is declared like this:

```objc
@interface StringList : NSObject &lt;NSFastEnumeration&gt;
{
    MyList * _startOfListNode;
    MyList * _endOfListPlusOneNode;
}
```

This is more complicated example because we need to actually gather the data from the list and store our traversal state between iterations. Here is how it might look:

```objc
- (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len
{
    MyList *currentNode;
    if (state->state == 0)
    {
        // Set the starting point. _startOfListNode is assumed to be our
        // object's instance variable that points to the start of the list.
        currentNode = _startOfListNode;
    }
    else
    {
        // Subsequent iterations, get the current progress out of state->state
        currentNode = (struct MyList *)state->state;
    }
    
    // Accumulate nodes from the list until we reach the object's
    // _endOfListPlusOneNode
    NSUInteger batchCount = 0;
    while (currentNode != _endOfListPlusOneNode && batchCount < len)
    {
        stackbuf[batchCount] = currentNode->stringPtr;
        currentNode = currentNode->nextNode;
        batchCount++;
    }

    state->state = (unsigned long)currentNode;
    state->itemsPtr = stackbuf;
    state->mutationsPtr = (unsigned long *)self;

    return batchCount;
}
```

Explanation of this example:

- stackbuf

  to store the data accumulated from the list and we return it in

  state-\>itemsPtr

  .
- len

  is used now because it is the maximum number of objects we can accumulate in

  stackbuf

  each time.
- state-\>state == 0

  ), we set the

  currentNode

  to our object's private

  _startOfListNode

  — that we assume we have correctly set to the start of our list.
- state-\>state

  will hold our

  currentNode

  , saved from the last iteration.
- currentNode == _endOfListPlusOneNode

  at the end of the list — remember that

  state-\>state

  is not allowed to be nil, which is why we use this non-nil end marker node. If you use a list that ends in nil, then you should detect this and set

  state-\>state

  to a special non-nil "end" flag so that you won't get trapped in an infinite loop.
