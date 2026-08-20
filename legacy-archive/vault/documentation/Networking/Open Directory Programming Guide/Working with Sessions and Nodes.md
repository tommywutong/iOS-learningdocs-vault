---
title: Open Directory Programming Guide
apple_id: TP40000917
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2009-08-12'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Directory/workingWithNodes/workingWithNodes.html
archived_at: '2026-07-27T06:57:05.674688Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Programming Guide](Introduction.md)


[Next](Working%20with%20Records%20and%20Queries.md)[Previous](Concepts.md)

# Working with Sessions and Nodes

This chapter provides sample code that shows how to work with nodes. Opening a session, finding a node, and authenticating a user to the node are fundamental Open Directory tasks.

## Listing a Session’s Registered Nodes

The sample code in Listing 2-1 demonstrates how to initialize a session object and retrieve a list of all registered nodes. Corresponding C API for this and all other Cocoa examples in this document can be found in _[Open Directory Reference](https://developer.apple.com/documentation/opendirectory/opendirectory_functions)_.

__Listing 2-1__  Listing registered nodes

```
ODSession *mySession = [ODSession defaultSession];
NSError *err;
NSArray *nodeNames = [mySession nodeNamesAndReturnError:&err];
```

## Finding a Node

Open Directory nodes can be found by type or by name. Listing 2-2 demonstrates how to find the authentication node of a session by its type.

__Listing 2-2__  Finding a node by type

```
ODNode *myNode = [ODNode nodeWithSession:mySession type:kODNodeTypeAuthentication error:&err];
```

The sample code in Listing 2-3 demonstrates how to find the node for a specific pathname.

__Listing 2-3__  Finding the node for a pathname

```
NSString *nodeName = @"/LDAPv3/127.0.0.1";
ODNode *myNode = [ODNode nodeWithSession:mySession name:nodeName error:&err];
```

## Authenticating a User to a Node

To authenticate itself to the Open Directory for the purposes of reading, writing, or making changes to a node, an Open Directory client application calls one of the three following methods of an ODNode object:

- [setCredentialsWithRecordType:recordName:password:error:](https://developer.apple.com/documentation/opendirectory/odnode/1427290-setcredentialswithrecordtype) authenticates using standard username-password authentication.
- [setCredentialsUsingKerberosCache:error:](https://developer.apple.com/documentation/opendirectory/odnode/1427785-setcredentialsusingkerberoscache) authenticates using a provided Kerberos cache..
- [setCredentialsWithRecordType:authenticationType:authenticationItems:continueItems:context:error:](https://developer.apple.com/documentation/opendirectory/odnode/1426987-setcredentialswithrecordtype) allows the application to authenticate using one of several other types of authentication supported by the node. See `Authentication Types` for a list of possible authentication types.

[Next](Working%20with%20Records%20and%20Queries.md)[Previous](Concepts.md)
