---
title: Core Data Snippets
apple_id: TP40008285
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2009-07-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CoreDataSnippets/Articles/fetchExpressions.html
archived_at: '2026-07-15T07:23:47.147345Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data Snippets](Introduction.md)


[Next](Creating%20and%20Deleting%20Managed%20Objects.md)[Previous](Fetching%20Managed%20Objects.md)

# Fetching Specific Property Values

This article contains snippets for fetching specific attribute values for a given entity.

Sometimes you don’t want to fetch actual managed objects; instead, you just want to retrieve—for example—the largest or smallest value of a particular attribute, or distinct values for a given attribute. On iOS, you can use `NSExpressionDescription` objects to specify a function for a fetch request, and [setReturnsDistinctResults:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506344-returnsdistinctresults) to return unique values.

To perform the fetch, you minimally need a managed object context against which to execute the fetch, and an entity description to specify the entity you want. How you get the managed object context depends on your application architecture—see [Getting a Managed Object Context](Accessing%20the%20Core%20Data%20Stack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobtfvjvomq). Once you have the context, you can get the entity using `NSEntityDescription`’s convenience method, [entityForName:inManagedObjectContext:](https://developer.apple.com/documentation/coredata/nsentitydescription/1425111-entity).

To fetch the unique values of a particular attribute across all instances of a given entity, you configure a fetch request with the method [setReturnsDistinctResults:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506344-returnsdistinctresults) (and pass `YES` as the parameter). You also specify that the fetch should return dictionaries rather than managed objects, and the name of the property you want to fetch.

```
NSManagedObjectContext *context = <#Get the context#>;

NSEntityDescription *entity = [NSEntityDescription  entityForName:@"<#Entity name#>" inManagedObjectContext:context];

NSFetchRequest *request = [[NSFetchRequest alloc] init];
[request setEntity:entity];
[request setResultType:NSDictionaryResultType];
[request setReturnsDistinctResults:YES];
[request setPropertiesToFetch:@[@"<#Attribute name#>"]];

// Execute the fetch.
NSError *error;
id requestedValue = nil;
NSArray *objects = [context executeFetchRequest:request error:&error];
if (objects == nil) {
    // Handle the error.
}
```


To fetch values that satisfy a particular function (such as the maximum or minimum value), you use an instance of [NSExpressionDescription](https://developer.apple.com/documentation/coredata/nsexpressiondescription) to specify the property or properties you want to retrieve.

```
NSManagedObjectContext *context = <#Get the context#>;

NSFetchRequest *request = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"<#Entity name#>" inManagedObjectContext:context];
[request setEntity:entity];

// Specify that the request should return dictionaries.
[request setResultType:NSDictionaryResultType];

// Create an expression for the key path.
NSExpression *keyPathExpression = [NSExpression expressionForKeyPath:@"<#Key-path for the property#>"];

// Create an expression to represent the function you want to apply
NSExpression *expression = [NSExpression expressionForFunction:@"<#Function name#>"
    arguments:@[keyPathExpression]];

// Create an expression description using the minExpression and returning a date.
NSExpressionDescription *expressionDescription = [[NSExpressionDescription alloc] init];

// The name is the key that will be used in the dictionary for the return value.
[expressionDescription setName:@"<#Dictionary key#>"];
[expressionDescription setExpression:expression];
[expressionDescription setExpressionResultType:<#Result type#>]; // For example, NSDateAttributeType

// Set the request's properties to fetch just the property represented by the expressions.
[request setPropertiesToFetch:@[expressionDescription]];

// Execute the fetch.
NSError *error;
id requestedValue = nil;
NSArray *objects = [context executeFetchRequest:request error:&error];
if (objects == nil) {
    // Handle the error.
}
else {
    if ([objects count] > 0) {
        requestedValue = [[objects objectAtIndex:0] valueForKey:@"<#Dictionary key#>"];
    }
}
```

For a full list of supported functions, see [expressionForFunction:arguments:](https://developer.apple.com/documentation/foundation/nsexpression/1413747-init).

If you want to retrieve multiple values simultaneously, create multiple instances of `NSExpressionDescription` to represent the different values you want to retrieve, and add them all to the array you pass in `setPropertiesToFetch:`. They must all, of course, apply to the same entity.

[Next](Creating%20and%20Deleting%20Managed%20Objects.md)[Previous](Fetching%20Managed%20Objects.md)

