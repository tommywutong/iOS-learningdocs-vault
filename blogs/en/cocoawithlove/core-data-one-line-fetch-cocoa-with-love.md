---
title: 'Core Data: one line fetch | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/core-data-one-line-fetch.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:5b07a4e05f0f0348'
translated: false
---

> 原文：[Core Data: one line fetch | Cocoa with Love](https://www.cocoawithlove.com/2008/03/core-data-one-line-fetch.html)　·　Cocoa with Love (Matt Gallagher)

It's a lot easier to get your data out of Core Data than the documentation will tell you. This simple 1-line fetch will work just as well as Apple's suggested 10-line approach for most uses.

## What does Core Data do?

The Core Data documentation avoids giving a simple explanation of what it does. I'm going to help them out.

Lets make the assumption that it holds the data very well. Fair assumption, it's a pretty good API. Once that's done, what would a typical programmer like to do next? I think the following is fair:

Wow, what a revelation! I think this could catch on. Programmers might even want to do this **_all the time_**.

## Fetching data, according to Core Data

It's a very common task. A good API should have a nice simple option for doing this. Let's look at what Core Data suggests. According to the [Core Data Programming Guide](http://developer.apple.com/documentation/Cocoa/Conceptual/CoreData/Articles/cdFetching.html):

```objc
NSManagedObjectContext *moc = [self managedObjectContext];
NSEntityDescription *entityDescription = [NSEntityDescription entityForName:@"Employee" inManagedObjectContext:moc];
NSFetchRequest *request = [[[NSFetchRequest alloc] init] autorelease];
[request setEntity:entityDescription];
 
// Set example predicate and sort orderings...
NSNumber *minimumSalary = ...;
NSPredicate *predicate = [NSPredicate predicateWithFormat:
    @"(lastName LIKE[c] 'Worsley') AND (salary > %@)", minimumSalary];
[request setPredicate:predicate];
 
NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc]
    initWithKey:@"firstName" ascending:YES];
[request setSortDescriptors:[NSArray arrayWithObject:sortDescriptor]];
[sortDescriptor release];
 
NSError *error = nil;
NSArray *array = [moc executeFetchRequest:request error:&error];
if (array == nil)
{
    // Deal with error...
}
```

Really, Core Data designers? Really? It's a common task, programmers need to do it all the time, essential for using Core Data and **_it requires 13 lines for the most common single task?_**

## One line, thanks

I think they got it wrong. All of the above code should be reduced to:

```objc
[[self managedObjectContext] fetchObjectsForEntityName:@"Employee" withPredicate:
    @"(lastName LIKE[c] 'Worsley') AND (salary > %@)", minimumSalary];
```

That line would perform all the work of the previous code monstrosity except sorting which would still be a separate step, if needed. 10 lines, down to 1 through providing a better method for the common case.

Obviously, looking up the Entity and building the NSPredicate each time isn't going to be the optimal fast case and other special NSFetchRequest options aren't accessible, but for most other cases, 10 times shorter equals 10 times better.

You'll also realise that since we've removed sorting, all of the objects returned are unique and in no particular order. This is an NSSet, not an NSArray and the return type has been changed accordingly. Creating an NSSet has a slightly higher overhead than creating an NSArray but again, we're considering quick and simple fetches and this approach allows easy testing of set membership in the results (a very useful logic case).

## Make it so

A good thing about Objective-C is that limitations in the default API are no real hinderance. Put the following in a NSManagedObjectContext category and all these wonders can be yours.

```objc
// Convenience method to fetch the array of objects for a given Entity
// name in the context, optionally limiting by a predicate or by a predicate
// made from a format NSString and variable arguments.
//
- (NSSet *)fetchObjectsForEntityName:(NSString *)newEntityName
    withPredicate:(id)stringOrPredicate, ...
{
    NSEntityDescription *entity = [NSEntityDescription
        entityForName:newEntityName inManagedObjectContext:self];

    NSFetchRequest *request = [[[NSFetchRequest alloc] init] autorelease];
    [request setEntity:entity];
    
    if (stringOrPredicate)
    {
        NSPredicate *predicate;
        if ([stringOrPredicate isKindOfClass:[NSString class]])
        {
            va_list variadicArguments;
            va_start(variadicArguments, stringOrPredicate);
            predicate = [NSPredicate predicateWithFormat:stringOrPredicate
                arguments:variadicArguments];
            va_end(variadicArguments);
        }
        else
        {
            NSAssert2([stringOrPredicate isKindOfClass:[NSPredicate class]],
                @"Second parameter passed to %s is of unexpected class %@",
                sel_getName(_cmd), [stringOrPredicate className]);
            predicate = (NSPredicate *)stringOrPredicate;
        }
        [request setPredicate:predicate];
    }
     
    NSError *error = nil;
    NSArray *results = [self executeFetchRequest:request error:&error];
    if (error != nil)
    {
        [NSException raise:NSGenericException format:[error description]];
    }
    
    return [NSSet setWithArray:results];
}
```

Keen coders will notice that the second parameter can be an NSPredicate or an NSString, allowing a little extra lazy freedom there if needed. It was a spur of the moment choice which seemed convenient, I'll decide later if it constitutes bad design.
