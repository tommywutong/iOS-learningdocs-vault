---
title: Open Directory Programming Guide
apple_id: TP40000917
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2009-08-12'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Directory/workingWithRecords/workingWithRecords.html
archived_at: '2026-07-27T06:57:05.701655Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Working%20with%20Sessions%20and%20Nodes.md)

# Working with Records and Queries

Querying and manipulating records is an essential part of using Open Directory. This chapter covers basic examples of how to interact with records and queries.

## Searching for Records

The sample code in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjxfvbuqnrnguytmmrx) demonstrates how to search for records in a node with a query. First, the sample code creates an ODQuery object, passing it the following parameters:

- `myNode`, a reference to the node to query.
- `kODRecordTypeUsers`, a record type indicating that the query should return user records.
- `kODAttributeTypeRecordName`, an attribute type indicating that the query should search the name attribute of records.
- `kODMatchContains`, a match type indicating that the query should return records whose attribute contains the search value.
- `searchValue`, an NSString reference indicating the string to search for.
- `kODAttributeTypeStandardOnly`, an attribute type indicating that the results of the query should only include standard attributes.
- `0`, an integer indicating the maximum number of results to return from the query (passing zero indicates that all results should be returned).
- `&err`, an optional error reference.

The code then sets the query’s delegate object to its containing object to allow for asynchronous querying. The delegate must implement the `query:foundResults:error:` method of the ODQueryDelegate protocol. The query is finally scheduled in a run loop. As ODRecord results are returned asynchronously by the query, the delegate method is called, and the application can process the results.

__Listing 3-1__  Searching for records in a node

```objc
- (void) search:(NSString *)searchValue
{
    ODQuery *myQuery = [ODQuery  queryWithNode: myNode
                                forRecordTypes: kODRecordTypeUsers
                                     attribute: kODAttributeTypeRecordName
                                     matchType: kODMatchContains
                                   queryValues: searchValue
                              returnAttributes: kODAttributeTypeStandardOnly
                                maximumResults: 0
                                         error: &err];
    [myQuery retain];
    [myQuery setDelegate: self];
    [myQuery scheduleInRunLoop: [NSRunLoop currentRunLoop] forMode:NSDefaultRunLoopMode];
}

- (void)query:(ODQuery *)inSearch foundResults:(NSArray *)inResults error:(NSError *) inError
{
    // Process the results of the query
}
```

It is also possible to execute a query synchronously with the [resultsAllowingPartial:error:](https://developer.apple.com/documentation/opendirectory/odquery/1391702-resultsallowingpartial) method. This is not recommended, as unexpectedly large result sets can cause your application to block for a long time.

## Getting Information About a Record’s Attribute

After you have obtained an `ODRecord` object through a query, accessing its attributes is straightforward. Listing 3-2 shows an implementation of the delegate method in Listing 3-1 that obtains the phone numbers of all returned user records. In this example, if a user record has more than one phone number, only the first phone number is obtained. If _inResults_ and _inError_ are both `nil`, the query has returned all results, and it should be removed from the run loop and released.

__Listing 3-2__  Getting information about a record’s attribute

```objc
- (void)query:(ODQuery *)inSearch foundResults:(NSArray *)inResults error:(NSError *)inError
{

    if (!inResults && !inError) }
        [inSearch removeFromRunLoop:[NSRunLoop currentRunLoop] forMode:NSDefaultRunLoopMode];
        [inSearch release]
    }

    NSMutableArray *phoneNumbers = [NSMutableArray arrayWithCapacity:[inResults count]];
    ODRecord *record;
    for (record in inResults) {
        NSError *err;
        NSArray *recordPhoneNumber = [record valuesForAttribute:kODAttributeTypePhoneNumber error:&err];

        if ([recordPhoneNumber count]) {
            [phoneNumbers addObject:[recordPhoneNumber objectAtIndex:0]];
        }
    }

    // Process phone number data

}
```

## Creating a Record and Adding an Attribute

The sample code in Listing 3-3 demonstrates how to create a record with the node that contains it. The _attributes_ parameter of the [createRecordWithRecordType:name:attributes:error:](https://developer.apple.com/documentation/opendirectory/odnode/1427031-createrecord) method is an NSDictionary object of attribute types with their corresponding values. Additional attributes can subsequently be added to the record. In order to commit changes made to a record, [synchronizeAndReturnError:](https://developer.apple.com/documentation/opendirectory/odrecord/1427579-synchronizeandreturnerror) must be called on the record after the changes are made. This example assumes the user has already set credentials with the node and is authorized to create and edit records.

__Listing 3-3__  Creating a record and adding an attribute

```
NSDictionary *recordAttributes = [NSDictionary dictionaryWithObject:@"Cupertino" forKey:kODAttributeTypeCity];
ODRecord *myRecord = [myNode createRecordWithRecordType:kODRecordTypeUsers name:@"foo" attributes:recordAttributes error:&err];
[myRecord setValue:@"CA" forAttribute:kODAttributeTypeState error:&err];
[myRecord synchronizeAndReturnError:&err];
```

## Adding Members to a Group Record

The sample code in Listing 3-4 demonstrates how to create a group record and add user records to the group.

__Listing 3-4__  Creating a group record and adding a member

```
NSNumber *gid;  // Assume this has been set to a desired group identifier value
ODRecord *myGroup = [myNode createRecordWithRecordType:kODRecordTypeGroups name:@"foo" attributes:nil error:&err];
[myGroup setValue:gid forAttribute:kODAttributeTypePrimaryGroupID error:&err];
[myGroup sychronizeAndReturnError:&err];  // Commit the newly created group

[myGroup addMemberRecord:myRecord error:&err];
[myGroup synchronizeAndReturnError:&err];  // Commit the new group member information
```

## Deleting a Record

The sample code in Listing 3-5 demonstrates how to delete a record. Records should be released after they are deleted.

__Listing 3-5__  Deleting a record

```
[myRecord deleteRecordAndReturnError:&err];
[myRecord release];
```

## Setting the Name of a Record

The Open Directory framework does not offer a direct method for changing the name of a record after it is created. To achieve the same effect, obtain all of a record’s attributes and values with [recordDetailsForAttributes:error:](https://developer.apple.com/documentation/opendirectory/odrecord/1427081-recorddetails), passing `kODAttributeTypeAllAttributes` as the attribute type to request. Then, delete the record and create a new record with the desired name and attributes.

[Next](Document%20Revision%20History.md)[Previous](Working%20with%20Sessions%20and%20Nodes.md)
