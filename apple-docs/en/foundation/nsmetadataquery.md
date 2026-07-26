---
title: NSMetadataQuery
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery.json'
content_hash: 'sha256:a7291122a6f191a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQuery

<sub>Class</sub>

A query that you perform against Spotlight metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMetadataQuery
```

## Overview

The [NSMetadataQuery](nsmetadataquery.md) class encapsulates the functionality provided by the [MDQuery](../coreservices/file_metadata/mdquery.md) opaque type for querying the Spotlight metadata.

[NSMetadataQuery](nsmetadataquery.md) objects provide metadata query results in several ways:

- As individual attribute values for requested attributes.
- As value lists that contain the distinct values for given attributes in the query results.
- As a result array proxy, containing all the query results. This is suitable for use with Cocoa bindings.
- As a hierarchical collection of results, grouping together items with the same values for specified grouping attributes. This is also suitable for use with Cocoa bindings.

Queries have two phases: the initial gathering phase that collects all currently matching results and a second live-update phase.

By default, the receiver has no limitation on its search scope. Use the [searchScopes](nsmetadataquery/searchscopes.md) property to customize.

By default, notification of updated results occurs at 1.0 seconds. Use the [notificationBatchingInterval](nsmetadataquery/notificationbatchinginterval.md) property to customize.

You must set a predicate with the [predicate](nsmetadataquery/predicate.md) property before starting a query.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring queries

- [searchScopes](nsmetadataquery/searchscopes.md) — An array containing the search scopes.
- [predicate](nsmetadataquery/predicate.md) — The predicate used to filter query results.
- [sortDescriptors](nsmetadataquery/sortdescriptors.md) — An array of sort descriptor objects.
- [valueListAttributes](nsmetadataquery/valuelistattributes.md) — An array of attributes whose values are gathered by the query.
- [groupingAttributes](nsmetadataquery/groupingattributes.md) — An array of grouping attributes. (read-only)
- [notificationBatchingInterval](nsmetadataquery/notificationbatchinginterval.md) — The interval at which notification of updated results occurs.
- [delegate](nsmetadataquery/delegate.md) — The query’s delegate.
- [searchItems](nsmetadataquery/searchitems.md) — An array of objects that define the query’s scope.

### Running queries

- [started](nsmetadataquery/isstarted.md) — A Boolean value that indicates whether the query has started. (read-only)
- [- startQuery](<nsmetadataquery/start().md>) — Attempts to start the query.
- [gathering](nsmetadataquery/isgathering.md) — A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [stopped](nsmetadataquery/isstopped.md) — A Boolean value that indicates whether the query has stopped.
- [- stopQuery](<nsmetadataquery/stop().md>) — Stops the receiver’s current query from gathering any further results.

### Getting query results

- [results](nsmetadataquery/results.md) — An array containing the query’s results.
- [resultCount](nsmetadataquery/resultcount.md) — The number of results returned by the query. (read-only)
- [- resultAtIndex:](<nsmetadataquery/result(at_).md>) — Returns the query result at a specific index.
- [- indexOfResult:](<nsmetadataquery/index(ofresult_).md>) — Returns the index of a query result object in the receiver’s results array.
- [groupedResults](nsmetadataquery/groupedresults.md) — An array containing hierarchical groups of query results. (read-only)
- [NSMetadataQueryResultGroup](nsmetadataqueryresultgroup.md) — The `NSMetadataQueryResultGroup` class represents a collection of grouped attribute results returned by an [NSMetadataQuery](nsmetadataquery.md) object.
- [- enumerateResultsUsingBlock:](<nsmetadataquery/enumerateresults(__).md>) — Enumerates the current set of results using the given block.
- [- enumerateResultsWithOptions:usingBlock:](<nsmetadataquery/enumerateresults(options_using_).md>) — Enumerates the current set of results using the given options and block.
- [valueLists](nsmetadataquery/valuelists.md) — A dictionary containing the value lists generated by the query.
- [NSMetadataQueryAttributeValueTuple](nsmetadataqueryattributevaluetuple.md) — The `NSMetadataQueryAttributeValueTuple` class represents attribute-value tuples, which are objects that contain the attribute name and value of a metadata attribute.
- [- valueOfAttribute:forResultAtIndex:](<nsmetadataquery/value(ofattribute_forresultat_).md>) — Returns the value for the attribute name `attrName` at the index in the results specified by `idx`.
- [- enableUpdates](<nsmetadataquery/enableupdates().md>) — Enables updates to the query results.
- [- disableUpdates](<nsmetadataquery/disableupdates().md>) — Disables updates to the query results.
- [operationQueue](nsmetadataquery/operationqueue.md) — The queue on which query result notifications are posted.

### Working with notifications

- [NSMetadataQueryDidFinishGatheringNotification](nsnotification/name-swift.struct/nsmetadataquerydidfinishgathering.md) — Posted when the receiver has finished with the initial result-gathering phase of the query.
- [NSMetadataQueryDidStartGatheringNotification](nsnotification/name-swift.struct/nsmetadataquerydidstartgathering.md) — Posted when the receiver begins with the initial result-gathering phase of the query.
- [NSMetadataQueryDidUpdateNotification](nsnotification/name-swift.struct/nsmetadataquerydidupdate.md) — Posted when the receiver’s results have changed during the live-update phase of the query.
- [NSMetadataQueryGatheringProgressNotification](nsnotification/name-swift.struct/nsmetadataquerygatheringprogress.md) — Posted as the receiver is collecting results during the initial result-gathering phase of the query.

### Working with notification messages

- [DidFinishGatheringMessage](nsmetadataquery/didfinishgatheringmessage.md) — A message a metadata query sends when it finishes the initial result-gathering phase of the query.
- [DidStartGatheringMessage](nsmetadataquery/didstartgatheringmessage.md) — A message a metadata query sends when it starts the initial result-gathering phase of the query.

### Constants

- [Metadata Query Search Scopes](metadata-query-search-scopes.md) — Constants for the predefined search scopes used by [searchScopes](nsmetadataquery/searchscopes.md).
- [Content Relevance](content-relevance.md) — In addition to including the requested metadata attributes, a query result also includes content relevance, accessed with the following key.
- [Keys for Use with a Notification Info Dictionary](keys-for-use-with-a-notification-info-dictionary.md) — Constants for keys to retrieve the collection of changed items from a notification’s user info dictionary.

## See Also

### File Search

- [NSMetadataQueryDelegate](nsmetadataquerydelegate.md) — An interface that enables the delegate of a metadata query to provide substitute results or attributes.
- [NSMetadataItem](nsmetadataitem.md) — The metadata associated with a file.
