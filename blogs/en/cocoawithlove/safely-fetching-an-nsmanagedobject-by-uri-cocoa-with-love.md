---
title: 'Safely fetching an NSManagedObject by URI | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/08/safely-fetching-nsmanagedobject-by-uri.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:98306dd3af7ef225'
translated: false
---

> 原文：[Safely fetching an NSManagedObject by URI | Cocoa with Love](https://www.cocoawithlove.com/2008/08/safely-fetching-nsmanagedobject-by-uri.html)　·　Cocoa with Love (Matt Gallagher)

If you need to store a reference to an NSManagedObject outside of an NSManagedObjectContext, then you'll need to convert NSManagedObjects to URIs and back again. At first glance it looks like [a simple method](http://developer.apple.com/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSPersistentStoreCoordinator_Class/Reference/NSPersistentStoreCoordinator.html#//apple_ref/doc/uid/TP30001180-CJBCHFIC) will do all the work for you but in reality you must be careful when getting the object back. I'll show you the way to convert an object to a URI and get it back safely.

## Why store an NSManagedObject reference outside a context?

Perhaps you want to store cross-store relationships. Perhaps you want to copy references via the clipboard or a dragging pasteboard. Maybe you want to store the last accessed object in your preferences.

None of these storage locations are within an NSManagedObjectContext. So if you want to store an NSManagedObject reference reliably, you can't just store a pointer.

If one of the attributes on your entity is guaranteed unique, you could store that attribute and use it to find the NSManagedObject later. But you don't need to add a unique attribute: every object already has one provided automatically — the objectID.

> _— Matt, if you love Core Data so much, why don't you marry it?_  
>  Okay, I've written quite a few Core Data related posts now (relative to other frameworks within Cocoa). That's because it's an amazing API: free file reading/writing, free undo, scaleable, highly optimised. Unless you have explicit reasons to avoid it, every program you write should use it.

## The easy part: convert to a URI

It's very easy to create a URI from an NSManagedObject and the documentation explains this well.

```objc
NSURL *uri = [[myObject objectID] URIRepresentation];
```

Once it's an NSURL, you can serialize it (for use in pasteboards, etc) with:

```objc
NSData *uriData = [NSKeyedArchiver archivedDataWithRootObject:uri];
```

## What is a URI?

In Core Data, a URI uniquely identifies an object. It is normally viewed as a string:

e.g. x-coredata:///MyEntity/t03BF9735-A005-4ED9-96BA-462BD65FA25F118 (temporary ID)  
 or x-coredata://EB8922D9-DC06-4256-A21B-DFFD47D7E6DA/MyEntity/p3 (permanent ID)

In a more general context, it stands for "Uniform Resource Identifier" and could be a URL ("Uniform Resource Locator") or a URN ("Uniform Resource Name") or both.

A URN uniquely identifies an entity (for example an ISBN number uniquely identifies a book) but doesn't tell you where to find that entity. A URL tells you a location but doesn't let you uniquely identify the object that you find there (for example, you may be able to download the PDF of a book from a web address but without extra information can't tell if it matches a given ISBN).

If you duplicate a Core Data file on disk, then you end up with two files that have the same persistent store ID. So Core Data URIs are not always globally unique but in practice that distinction rarely matters.

## Problems getting the NSManagedObject back

NSPersistentStoreCoordinator has the method:

```objc
-(<span class="monospace">NSManagedObjectID</span> *)managedObjectIDForURIRepresentation:(NSURL *)uri;
```

and NSManagedObjectContext has:

```objc
-(<span class="monospace">NSManagedObject</span> *)objectWithID:(<span class="monospace">NSManagedObjectID</span> *)objectID;
```

so it would seem that all you need to do is convert your string to an NSURL, convert the NSURL to an NSManagedObjectID and the NSManagedObjectID to the NSManagedObject.

But there's a catch: these methods do not actually fetch the object from the persistent store. **If the object doesn't exist, these methods will still succeed**, giving you an NSManagedObjectID or NSManagedObject referencing a non-existent entry in the persistent store (which will throw an  NSObjectInaccessibleException if you try to fault it). The reality is that, despite their appearance, these methods are for constructing object ID's, they don't search the persistent store.

Obviously, we will need to combine these methods with a proper search of the persistent store.

## Safely getting the object back

If the NSManagedObject for the URI does eixist and has already been faulted by the NSManagedObjectContext, then the result from objectWithID: will be the correct object. The question is how to handle the situation where isFault returns NO (and the object may not exist).

The answer is: even though the NSManagedObject returned by objectWithID: may not exist in the persistent store, we can still use the NSManagedObject to search the persistent store.

Time for a whole chunk of code. This is an NSManagedObjectContext category that returns the faulted object for the given URI string, if it exists, or nil if it doesn't.

You may notice that I construct the NSPredicate for the search directly in code (instead of using a predicate string. I wanted to waste as little CPU time as possible.

```objc
@implementation NSManagedObjectContext (FetchedObjectFromURI)
- (NSManagedObject *)objectWithURI:(NSURL *)uri
{
    NSManagedObjectID *objectID =
        [[self persistentStoreCoordinator]
            managedObjectIDForURIRepresentation:uri];
    
    if (!objectID)
    {
        return nil;
    }
    
    NSManagedObject *objectForID = [self objectWithID:objectID];
    if (![objectForID isFault])
    {
        return objectForID;
    }

    NSFetchRequest *request = [[[NSFetchRequest alloc] init] autorelease];
    [request setEntity:[objectID entity]];
    
    // Equivalent to
    // predicate = [NSPredicate predicateWithFormat:@"SELF = %@", objectForID];
    NSPredicate *predicate =
        [NSComparisonPredicate
            predicateWithLeftExpression:
                [NSExpression expressionForEvaluatedObject]
            rightExpression:
                [NSExpression expressionForConstantValue:objectForID]
            modifier:NSDirectPredicateModifier
            type:NSEqualToPredicateOperatorType
            options:0];
    [request setPredicate:predicate];

    NSArray *results = [self executeFetchRequest:request error:nil];
    if ([results count] > 0 )
    {
        return [results objectAtIndex:0];
    }

    return nil;
}
@end
```

That's it. By executing the search when the object is a fault, we correctly guarantee its existence.
