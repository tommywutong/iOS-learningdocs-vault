---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/QueryingRecords.html
archived_at: '2026-07-15T07:23:42.471053Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Records Using a Query (records/query)

You can fetch records using a query.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/records/query`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID should begin with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to store the data within the container. The possible values are:  |  |  | | --- | --- | | **`public`** | : The database that is accessible to all users of the app. | | **`private`** | : The database that contains private data that is visible only to the current user. | | **`shared`** | : The database that contains records shared with the current user. | |

### Request

The POST request is a JSON dictionary containing the following keys:

| Key | Description |
| --- | --- |
| `zoneID` | A dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `resultsLimit` | The maximum number of records to fetch. The default is the maximum number of records in a response that is allowed, described in [Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi). |
| `query` | The query to apply, described in [Query Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcni). This key is required. |
| `continuationMarker` | The location of the last batch of results. Use this key when the results of a previous fetch exceeds the maximum. See [Response](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnjnknltq). The default value is `null`. |
| `desiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields. |
| `zoneWide` | A Boolean value determining whether all zones should be searched. This key is ignored if `zoneID` is non-`null`. To search all zones, set to `true`. To search the default zone only, set to `false`. |
| `numbersAsStrings` | A Boolean value indicating whether number fields should be represented by strings. The default value is `false`. |

### Response

An array of dictionaries describing the results of the operation. The dictionary contains the following keys:

| Key | Description |
| --- | --- |
| `records` | An array containing a result dictionary for each record requested. If successful, the result dictionary contains the keys described in [Record Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm). If unsuccessful, the result dictionary contains the keys described in [Record Fetch Error Dictionary](ModifyRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknlto). |
| `continuationMarker` | If included, indicates that there are more results matching this query. To fetch the other results, pass the value of the `continuationMarker` key as the value of the `continuationMarker` key in another query. |

### Discussion

A request to fetch records performs a query on indexed fields for a particular record type. At least one field in the record needs to be indexed to perform an empty query that fetches all records. Because indexes are updated asynchronously, they are not guaranteed to be current. If more than the maximum results are found, use `continuationMarker` in the response to fetch more records in batches.

Queries can be configured against system fields as well as developer-defined fields. The system fields are special fields on which an index can be defined. These fields have a special mapping such that the `___` prefix does not need to be used.

| fieldName | systemFieldName |
| ___recordId | recordName |
| ___share | share |
| ___parent | parent |
| ___createdBy | createdUserRecordName |
| ___createTime | createdTimestamp |
| ___modTime | modifiedTimestamp |
| ___modifiedBy | modifiedUserRecordName |

The filter dictionary can take a key `systemFieldName` instead of `fieldName`. This can take one of the mapped values to query for these system field names.

The sort descriptor dictionary can take a key `systemFieldName` instead of `fieldName` where the mapped values can be used.

A sample query request:

1. `"{`
2. `"zoneID": {`
3. `"zoneName": "myCustomZone",`
4. `},`
5. `"query": {`
6. `"recordType": "myRecordType",`
7. `"filterBy": [`
8. `{`
9. `"systemFieldName": "createdUserRecordName",`
10. `"comparator": "EQUALS",`
11. `"fieldValue": {`
12. `"value": {`
13. `"recordName": "recordA",`
14. `},`
15. `"type": "REFERENCE"`
16. `}`
17. `}`
18. `],`
19. `"sortBy": [`
20. `{`
21. `"systemFieldName": "createdTimestamp",`
22. `"ascending": false`
23. `}`
24. `]`
25. `}`
26. `}"`

### Related Framework API

This request is similar to using the [CKQueryOperation](https://developer.apple.com/documentation/cloudkit/ckqueryoperation) class in the CloudKit framework.

[Modifying Records (records/modify)](ModifyRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknlts)

[Fetching Records by Record Name (records/lookup)](LookupRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnrnknlte)
