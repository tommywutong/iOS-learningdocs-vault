---
title: Core Data Snippets
apple_id: TP40008285
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2009-07-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CoreDataSnippets/Articles/fetching.html
archived_at: '2026-07-15T07:23:47.155778Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data Snippets](Introduction.md)


[Next](Fetching%20Specific%20Property%20Values.md)[Previous](Accessing%20the%20Core%20Data%20Stack.md)

# Fetching Managed Objects

This article contains snippets for fetching managed objects.

To fetch managed objects, you minimally need a managed object context against which to execute the fetch, and an entity description to specify the entity you want. You create an instance of `NSFetchRequest` and specify its entity. You may optionally specify an array of sort orderings and/or a predicate.

How you get the managed object context depends on your application architecture—see [Getting a Managed Object Context](Accessing%20the%20Core%20Data%20Stack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobtfvjvomq). Once you have the context, though, you can get the entity using `NSEntityDescription`’s convenience method, [entityForName:inManagedObjectContext:](https://developer.apple.com/documentation/coredata/nsentitydescription/1425111-entity).

To get all the managed objects of a given entity, create a fetch request and specify just the entity:

```
NSManagedObjectContext *context = <#Get the context#>;

NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"<#Entity name#>"
    inManagedObjectContext:context];
[fetchRequest setEntity:entity];

NSError *error;
NSArray *fetchedObjects = [context executeFetchRequest:fetchRequest error:&error];
if (fetchedObjects == nil) {
    // Handle the error.
}
```


To fetch managed objects in a particular order, in addition to the components in the basic fetch (described in [Basic Fetch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobufvjvomq)) you need to specify an array of sort orderings:

```
NSManagedObjectContext *context = <#Get the context#>;

NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"<#Entity name#>"
    inManagedObjectContext:context];
[fetchRequest setEntity:entity];

NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc] initWithKey:@"<#Sort key#>"
    ascending:YES];
NSArray *sortDescriptors = @[sortDescriptor];
[fetchRequest setSortDescriptors:sortDescriptors];

NSError *error;
NSArray *fetchedObjects = [context executeFetchRequest:fetchRequest error:&error];
if (fetchedObjects == nil) {
    // Handle the error.
}
```


To fetch managed objects that meet given criteria, in addition to the components in the basic fetch (described in [Basic Fetch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobufvjvomq)) you need to specify a predicate:

```
NSManagedObjectContext *context = <#Get the context#>;

NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"<#Entity name#>"
    inManagedObjectContext:context];
[fetchRequest setEntity:entity];

NSPredicate *predicate = [NSPredicate predicateWithFormat:@"<#Predicate string#>",
    <#Predicate arguments#>];
[fetchRequest setPredicate:predicate];

NSError *error;
NSArray *fetchedObjects = [context executeFetchRequest:fetchRequest error:&error];
if (fetchedObjects == nil) {
    // Handle the error.
}
```

For more about predicates, see _[Predicate Programming Guide](../../Cocoa/Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_. For an alternative technique for creating the predicate that may be more efficient, see [Fetch with a Predicate Template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobufvjvona).

To fetch managed objects that meet given criteria, in addition to the components in the basic fetch (described in [Basic Fetch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobufvjvomq)) you need to specify a predicate.`NSPredicate`’s [predicateWithFormat:](https://developer.apple.com/documentation/foundation/nspredicate/1587997-predicatewithformat) method is typically the easiest way to use a predicate (as shown in [Fetch with a Predicate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobufvjvomy)), but it’s not the most efficient way to create the predicate itself. The predicate format string has to be parsed, arguments substituted, and so on. For performance-critical code, particularly if a given predicate is used repeatedly, you should consider other ways to create the predicate. For a predicate that you might use frequently, the easiest first step is to create a predicate template. You might create an [accessor method](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) that creates the predicate template lazily on demand:

```objc
// Assume an instance variable:
// NSPredicate *predicateTemplate;

- (NSPredicate *)predicateTemplate {
    if (predicateTemplate == nil) {
        predicateTemplate = [NSPredicate predicateWithFormat:@"<#Key#> <#Operator#> <#$Variable#>"];
    }
    return predicateTemplate;
}
```

When you need to use the template, you create a dictionary containing the substitution variables and generate the predicate using [predicateWithSubstitutionVariables:](https://developer.apple.com/documentation/foundation/nspredicate/1413227-withsubstitutionvariables).

```
NSManagedObjectContext *context = <#Get the context#>;

NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"<#Entity name#>"
    inManagedObjectContext:context];
[fetchRequest setEntity:entity];

NSDictionary *variables = @{ @"<#Variable#>" : <#Value#> };
NSPredicate *predicate = [[self predicateTemplate]
    predicateWithSubstitutionVariables:variables];
[fetchRequest setPredicate:predicate];

NSError *error;
NSArray *fetchedObjects = [context executeFetchRequest:fetchRequest error:&error];
if (fetchedObjects == nil) {
    // Handle the error.
}
```

For more about predicates, see _[Predicate Programming Guide](../../Cocoa/Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_.

To fetch managed objects that meet given criteria and in a particular order, in addition to the components in the basic fetch (described in [Basic Fetch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobufvjvomq)) you need to specify a predicate and an array of sort orderings.

```
NSManagedObjectContext *context = <#Get the context#>;

NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"<#Entity name#>" inManagedObjectContext:context];
[fetchRequest setEntity:entity];

NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc] initWithKey:@"<#Sort key#>" ascending:YES];
NSArray *sortDescriptors = @[sortDescriptor];
[fetchRequest setSortDescriptors:sortDescriptors];

NSPredicate *predicate = [NSPredicate predicateWithFormat:@"<#Predicate string#>",
    <#Predicate arguments#>];
[fetchRequest setPredicate:predicate];

NSError *error;
NSArray *fetchedObjects = [context executeFetchRequest:fetchRequest error:&error];
if (fetchedObjects == nil) {
    // Handle the error.
}
```

For more about predicates, see _[Predicate Programming Guide](../../Cocoa/Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_. For an alternative technique for creating the predicate that may be more efficient, see [Fetch with a Predicate Template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobufvjvona).

[Next](Fetching%20Specific%20Property%20Values.md)[Previous](Accessing%20the%20Core%20Data%20Stack.md)

