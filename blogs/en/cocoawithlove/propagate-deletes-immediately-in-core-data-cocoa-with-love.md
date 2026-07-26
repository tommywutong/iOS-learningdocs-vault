---
title: 'Propagate deletes immediately in Core Data | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/04/propagate-deletes-immediately-in-core.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:a373cc4a79a498fe'
translated: false
---

> 原文：[Propagate deletes immediately in Core Data | Cocoa with Love](https://www.cocoawithlove.com/2008/04/propagate-deletes-immediately-in-core.html)　·　Cocoa with Love (Matt Gallagher)

Learn some limitations associated with cascading deletes in Core Data and find out how to immediately propagate deletes in Core Data, overcoming these potential problems.

> **Correction**: this post previously indicated that NSManagedObject deletes would fail inside processPendingChanges. This issue was fixed in Mac OS X 10.5. The post has been edited to reflect that in Mac OS X 10.5 it is only processPendingChanges that cannot be invoked inside itself.

## Limitations to the default "deleteObject" for change propagation

Core Data has the ability to perform full object-graph deletes through the "cascade" delete rule available to each entity in the object model.

If you have overridden the Key Value Coding methods for relationships on your model entities you can encounter the following issues.

### Always deferred

Deletes in Core Data are always deferred, either to the end of the event (when -[NSManagedObjectContext processPendingChanges] is next called) or until the context is saved.

This means that if you want to read a value changed by a delete, you must:

- not be inside a -[NSManagedObjectContext processPendingChanges] invocation (i.e. during a delete propagation)
- call -[NSManagedObjectContext processPendingChanges] after the delete to flush the work through

If you are inside processPendingChanges (or you otherwise don't want to call it) but you need to see changes immediately, then you will need to implement your own change propagation instead of relying on the default deleteObject: to apply changes.

### Relationships deleted in no particular order

The "cascade" Delete Rule does not cascade through relationships in any particular order. If you need relationships to be deleted in a specific order (i.e. if you may read from the object during deletion), you will need to implement your own change propagation.

### No recursive deletes in 10.4

In Mac OS X 10.4, Core Data's delete propagation is incompatible with recursively invoked deletes. If a delete propagation triggers another delete propagation while it is doing its work, the second propagation won't work (it will have no effect).

## An example of how these problems can occur

Consider the following .xcdatamodel:

![](https://www.cocoawithlove.com/assets/objc-era/propagatedelete.png)

In this example, "A" uses a "cascade" Delete Rule for its properties but "B" and "C" use "nullify".

Our program must obey the following rule:

Our program maintains this rule by overriding the Key Value Coding methods for the "A" class.

The addBObject: method is overridden to create a C object and add it to the "A" object's "c" property before the "b" property is changed. Similarly, the removeBObject: method is overridden to delete the matching C object in the "A" object's "c" property after the "b" property is changed.

By adding the "C" object _before_ the "b" property is changed and removing the "C" object _after_ the "b" property is changed, we ensure that while a "B" object is attached to an "A" object, there is _always_ a matching "C" object attached.

Once we've deleted the "C" object, we use NSAssert to check that the number of "B" objects and "C" objects attached to "A" are the same. To ensure that the "C" object has been deleted before this read, we must call processPendingChanges to flush through the delete.

### Problems with nested processPendingChanges

The above described example will work fine, unless it is invoked from inside a delete propagation.

If we delete a "B" object, instead of simply removing it from "A", then the removal happens inside the processPendingChanges for the "B" object's delete.

In Mac OS X 10.4, the deleteObject: invocation in removeBObject: will not work correctly from inside processPendingChanges. This is a documented limitation. Any use of deleteObject: in an overridden accessor in Mac OS X 10.4 should propagate deletes itself.

In Mac OS X 10.5, the call to processPendingChanges in removeBObject: will have no effect. This means that the NSAssert will fail.

In this trivial example, the NSAssert isn't important but it shows that if you need to flush deletes to read back immediately and may need this functionality during a delete propagation, then you will need to propagate this delete yourself.

### Problems with order of delete

If you delete an "A" object, then you have no control over whether the "b" property or "c" property is deleted first.

The "C" property could be deleted first. If this occurs, then the rule _"must have a matching C object attached to the same A object at all times"_ is violated.

If you need control over the order that relationships are deleted, then you must propagate the delete yourself.

## Solution: actively perform the delete propagation yourself

A solution to the above listed problems is to actively perform the delete propagation yourself. This means iterating over all relationships on the object and using the deleteRule information from the relationship to decide how to handle the object on the other end.

This is going to be slower than the default delete propagation but we are deliberately replicating its behavior so that we can have greater control over what is done during the propagation.

Objects will still be deleted using -[NSMangedObjectContext deleteObject:] but before this occurs, they will be correctly disconnected from the object graph. To ensure that no infinite loops occur, all relationships in affected objects are set to nil as propagation passes through.

A brief warning: the following method doesn't handle the "Deny" delete rule. You would need to add support for this yourself.

So here's the big block of code. This is intended to be a Category method on NSManagedObject (otherwise it won't work as written). The  priorityDeletionRelationships method should be overridden by classes which need some relationships deleted first — the array returned should be the ordered list of relationship keys to delete first.

```objc
- (NSArray *)priorityDeletionRelationships
{
   return nil;
}

- (void)propagateDelete
{
   NSEntityDescription *entityDescription = [self entity];
  
   // Get the set of relationships
   NSDictionary *relationships = [entityDescription relationshipsByName];
   NSArray *unsortedKeys = [relationships allKeys];
   NSArray *priorityKeys = [self priorityDeletionRelationships];
   NSArray *keys;
   if ([priorityKeys count] > 0)
   {
       keys = [[unsortedKeys mutableCopy] autorelease];
       [(NSMutableArray *)keys
           removeObjectsInArray:priorityKeys];
       [(NSMutableArray *)keys
           replaceObjectsInRange:NSMakeRange(0, 0)
           withObjectsFromArray:priorityKeys];
   }
   else
   {
       keys = unsortedKeys;
   }
  
   // Iterate over the set of relationships
   NSEnumerator *relationshipEnumerator = [keys keyEnumerator];
   NSString *relationshipName;
   while ((relationshipName = [relationshipEnumerator nextObject]) != nil)
   {
       NSRelationshipDescription *relationshipDescription =
           [relationships objectForKey:relationshipName];
      
       // If the relationship is not "cascade", then just nullify it.
       if ([relationshipDescription deleteRule] != NSCascadeDeleteRule)
       {
           if (![relationshipDescription isToMany])
           {
               [self setValue:nil forKey:relationshipName];
           }
           else
           {
               NSMutableSet *relationshipSet =
                   [self mutableSetValueForKey:relationshipName];
               [relationshipSet removeAllObjects];
           }
           continue;
       }
      
       // Propagate the delete to the object at the other end of the
       // relationship
       if (![relationshipDescription isToMany])
       {
           NSManagedObject *destination = [self valueForKey:relationshipName];
           [self setValue:nil forKey:relationshipName];
           [destination propagateDelete];
           continue;
       }
      
       // Propagate the delete to every object in the to-many relationship.
       // We copy the set because we plan to change it during iteration.
       NSMutableSet *mutableRelationship =
           [self mutableSetValueForKey:relationshipName];
       NSSet *iterateSet = [[mutableRelationship copy] autorelease];
       NSEnumerator *enumerator = [iterateSet objectEnumerator];
       NSManagedObject *setObject;
       while ((setObject = [enumerator nextObject]) != nil)
       {
           [mutableRelationship removeObject:setObject];
           [setObject propagateDelete];
       }
   }
  
   // Delete this object
   [[self managedObjectContext] deleteObject:self];

}
```
