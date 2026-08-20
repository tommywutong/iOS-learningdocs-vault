---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/Types.html
archived_at: '2026-07-15T07:23:46.527279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Types and Dictionaries

The types and dictionaries listed below are used by multiple CloudKit web service requests that correspond to types or classes in CloudKit JS and the native API.

### Types

### CKValue

A `CKValue` represents a field type value. The table shows the supported field types.

| Schema field type | JavaScript type | Description |
| --- | --- | --- |
| Asset | `Asset` dictionary | A large file that is associated with a record but stored separately. Represented by a dictionary, described in [Asset Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltg). |
|  | `Boolean` | A `true` or `false` value. |
| Bytes | `String` | A wrapper for byte buffers that is stored with the record. Represented by a Base64-encoded string. |
| Date/Time | `Number` | A date or time value. Represented as a number in milliseconds between midnight on January 1, 1970, and the specified date or time. |
| Double | `Number` | A double. |
| Int(64) | `Number` | An integer. |
| Location | `Location` dictionary | A geographical coordinate and altitude, represented by a dictionary, described in [Location Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltk). |
| Reference | `Reference` dictionary | A relationship from one object to another, represented by a dictionary, described in [Reference Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlti). |
| String | `String` | A text string. |
| List | `Array` | An array containing any of the above field types. |

### Dictionaries

Several common dictionaries are used by multiple requests and responses throughout CloudKit web services.

### Asset Dictionary

An asset dictionary represents an Asset field type with the following keys:

| Key | Description |
| --- | --- |
| `fileChecksum` | The signature of a file returned from the file upload step. This key is required for the public and private database. |
| `size` | The size of the file, calculated by the asset upload step. This key is required for the public and private database. |
| `referenceChecksum` | The checksum of the wrapping key returned from the upload step. This key is required for the private database. |
| `wrappingKey` | The secret key used to encrypt the asset. This key is required for the private database. |
| `receipt` | The receipt for uploading the asset, described in [Upload Asset Data](UploadAssets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqobnknltq). This key is required for the public and private database when saving the enclosing record. |
| `downloadURL` | The location of the asset data to download. This key is present only when fetching the enclosing record. |

### Filter Dictionary

A filter dictionary defines the logical conditions for determining whether a record matches the query.

| Key | Description |
| --- | --- |
| `comparator` | A string representing the filter comparison operator. Possible values are described in [Comparator Values](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcoa). This key is required. |
| `fieldName` | The name of a field belonging to the record type. |
| `fieldValue` | A field-value dictionary, described in [Record Field Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcna), representing the value of the field that you want all fetched records to match. This key is required. |
| `distance` | A radius in meters used to determine whether a field of type `Location` is inside a circular area. The center of the circle is `fieldValue` and the radius is `distance`. The key is used only if `fieldName` is a `Location` type. |

### Comparator Values

The following values are allowed for the `comparator` key in a filter dictionary.

| Key | Description |
| --- | --- |
| `EQUALS` | The left-hand value is equal to the right-hand value. |
| `NOT_EQUALS` | The left-hand value is not equal to the right-hand value. |
| `LESS_THAN` | The left-hand value is less than the right-hand value. |
| `LESS_THAN_OR_EQUALS` | The left-hand value is less than or equal to the right-hand value. |
| `GREATER_THAN` | The left-hand value is greater than the right-hand value. |
| `GREATER_THAN_OR_EQUALS` | The left-hand value is greater than or equal to the right-hand value. |
| `NEAR` | The left-hand location is within the specified distance of the right-hand location. |
| `CONTAINS_ALL_TOKENS` | The records have text fields that contain all specified tokens. |
| `IN` | The left-hand value is in the right-hand list. |
| `NOT_IN` | The left-hand value is not in the right-hand list. |
| `CONTAINS_ANY_TOKENS` | The records with text fields contain any of the specified tokens. |
| `LIST_CONTAINS` | The records contain values in a list field. |
| `NOT_LIST_CONTAINS` | The records don’t contain the specified values in a list field. |
| `NOT_LIST_CONTAINS_ANY` | The records don’t contain any of the specified values in a list field. |
| `BEGINS_WITH` | The records with a field that begins with a specified value. |
| `NOT_BEGINS_WITH` | The records with a field that doesn’t begin with a specified value. |
| `LIST_MEMBER_BEGINS_WITH` | The records contain a specified value as the first item in a list field. |
| NOT_LIST_MEMBER_BEGINS_WITH | The records don’t contain a specified value as the first item in a list field. |
| `LIST_CONTAINS_ALL` | The records contain all values in a list field. |
| `NOT_LIST_CONTAINS_ALL` | The records don’t contain all specified values in a list field. |

### Location Dictionary

A location dictionary represents values used to set a field of type Location with the following keys:

| Key | Description |
| --- | --- |
| `latitude` | The latitude of the coordinate point. This key is required. |
| `longitude` | The longitude of the coordinate point. This key is required. |
| `horizontalAccuracy` | The radius of uncertainty for the location, measured in meters. |
| `verticalAccuracy` | The accuracy of the altitude value in meters. |
| `altitude` | The altitude measured in meters. |
| `speed` | The instantaneous speed of the device in meters per second. |
| `course` | The direction in which the device is traveling. |
| `timestamp` | The time at which this location was determined. |

### Name Components Dictionary

A user dictionary describes a user's name with the following keys:

| Key | Description |
| --- | --- |
| `namePrefix` | The user’s prefix. |
| `givenName` | The user’s first name. |
| `familyName` | The user’s last name. |
| `nickname` | The user’s nickname. |
| `nameSuffix` | The user’s suffix. |
| `middleName` | The user’s middle name. |
| `phoneticRepresentation` | A phonetic representation of the user’s name. |

### Notification Info Dictionary

A notification info dictionary represents information about a notification with the following keys:

| Key | Description |
| --- | --- |
| `alertBody` | The text of the alert message. |
| `alertLocalizationKey` | A key to a localized alert message. |
| `alertLocalizationArgs` | An array of strings to appear as variables if `alertLocalizationKey` is a format specifier. (For details, read Localized Formatted Strings in _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_.) |
| `alertActionLocalizationKey` | A key to get a localized right button title that appears in the alert dialog. |
| `alertLaunchImage` | The filename of an image file located in the app bundle to use as a launch image. |
| `soundName` | The name of a sound file located in the app bundle to use as an alert sound. |
| `shouldBadge` | A Boolean value indicating whether a badge should be displayed. If `true`, a badge is displayed; otherwise, it is not. The default value is `false`. |
| `shouldSendContentAvailable` | A Boolean value indicating whether new content is available. If `true`, new content is available; otherwise, it is not. The default value is `false`. |

For more information on these keys and push notifications, read The Notification Payload in _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_.

### Query Dictionary

Use the following search parameters when fetching records from the database:

| Key | Description |
| --- | --- |
| `recordType` | The name of the record type. This key is required. |
| `filterBy` | An Array of filter dictionaries (described in [Filter Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcnq)) used to determine whether a record matches the query. |
| `sortBy` | An Array of sort descriptor dictionaries (described in [Sort Descriptor Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcny)) that specify how to order the fetched records. |

### Record Dictionary

A record dictionary describes a record in a database. Some keys in the record dictionary are used in requests and others appear in responses. Also, some keys are specific to whether the record is shared or is a share, a record of type `cloudKit.shared`.

### Common Record Keys

These record keys appear in requests and responses:

| Key | Description |
| --- | --- |
| `recordName` | The unique name used to identify the record within a zone. The default value is a random UUID. |
| `recordType` | The name of the record type. This key is required for certain operations if the record doesn’t exist. |
| `recordChangeTag` | A string containing the server change token for the record. Use this tag to indicate which version of the record you last fetched.  This key is required if the operation type is `update`, `replace`, or `delete`. This key is not required if the operation is `forceUpdate`, `forceReplace`, or `forceDelete`. |
| `fields` | The dictionary of key-value pairs whose keys are the record field names and values are field-value dictionaries, described in [Record Field Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcna). The default value is an empty dictionary.  If the operation is `create` and this key is omitted or set to `null`, all fields in a newly created record are set to `null`. |

### Request Keys

Some keys are specific to the request of an endpoint.

### Shared Record Request Keys

To share a record, set the `createShortGUID` key to `true` in a request. To create collections of records to share, include the `parent` key.

| Key | Description |
| --- | --- |
| `createShortGUID` | A Boolean value indicating whether to create a short GUID for sharing this record. The default value is `false`. |
| `parent` | A dictionary with a single `recordName` key that is a reference to the parent record. |

### Share Request Keys

To create a share record (a record of type `cloudKit.share`), include these keys in the request:

| Key | Description |
| --- | --- |
| `forRecord` | A dictionary indicating the record that is being shared. The dictionary keys are `recordName` and `recordChangeTag`. Use this key when creating a share record. |
| `publicPermission` | Indicates the public read-write permissions of the shared record. Possible values are `NONE`, `READ_ONLY`, `READ_WRITE`, and `UNKNOWN`. |
| `participants` | An array of participants in the shared record. Participants are represented by a dictionary, described in [Share Participant Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltena). |

A share record dictionary also contains the `parent`, `publicPermission`, and `participants` keys in the response.

### Response Keys

### Common Response Keys

These record keys appear in responses:

| Key | Description |
| --- | --- |
| `created` | The dictionary representation of the date the record was created. The dictionary keys are:   - `timestamp`—the number representing the date/time. - `userRecordName`—the record name representing the user. - `deviceID`—the device where the change occurred. |
| `modified` | The dictionary representation of the date the record was modified. The dictionary keys are:   - `timestamp`—the number representing the date/time. - `userRecordName`—the record name representing the user. - `deviceID`—the device where the change occurred. |
| `deleted` | A Boolean value indicating whether the record was deleted. If `true`, it was deleted; otherwise, it was not deleted. |
| `shortGUID` | A global ID that identifies the record, described in [ShortGUID Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcoi).  NOTE: A `cloudKit.share` record has a `shortGUID` key with the same value as the shared record. The key is used to identify and resolve the share. |

### Shared Record Response Keys

These record keys appear in a response for a record that is shared:

| Key | Description |
| --- | --- |
| `parent` | A dictionary with a single `recordName` key that is a reference to the parent record. |

The `parent` key also appears in the request to create a collection of shared records.

### Share Response Keys

These keys appear in a response for a share record, a record of type `cloudKit.share`.

| Key | Description |
| --- | --- |
| `share` | A dictionary with a single `recordName` key that is a reference to the shared record. |
| `owner` | The owner of a shared record, described in [Share Participant Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltena). |
| `publicPermission` | Indicates the public read-write permissions of the shared record. Possible values are `NONE`, `READ_ONLY`, `READ_WRITE`, and `UNKNOWN`. |
| `participants` | An array of participants in the shared record. Participants are represented by a dictionary, described in [Share Participant Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltena). |
| `currentUserParticipant` | Information on the current user’s participation in the share, described in [Share Participant Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltena). |

The `publicPermission`, and `participants` keys, also appear in the request.

### Record Field Dictionary

A record field dictionary represents the value of a field and is of the form `{ value: CKValue, type: string (optional) }`. [CKValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltc) represents field values of type String, Number, Boolean, Reference, Asset, and Location.

### Reference Dictionary

A reference dictionary represents a Reference field type with the following keys:

| Key | Description |
| --- | --- |
| `recordName` | The unique name used to identify the record within a zone. This key is required. |
| `zoneID` | The dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `action` | The delete action for the reference object. Possible values are:   - `NONE`  No action when a referenced record is deleted. See [CKReferenceActionNone](https://developer.apple.com/documentation/cloudkit/ckreferenceaction/ckreferenceactionnone) in _[CloudKit Framework Reference](https://developer.apple.com/documentation/cloudkit)_. - `DELETE_SELF`  Deletes a source record when the target record is deleted. See [CKReferenceActionDeleteSelf](https://developer.apple.com/documentation/cloudkit/ckrecord_reference_action/deleteself). - `VALIDATE`  Deletes a target record only after all source records are deleted. Verifies that the target record exists before creating this type of reference. If it doesn’t exist, creating the reference fails.   This key is required unless the dictionary is included in a query. |

### Share Participant Dictionary

A dictionary that represents a participant in a shared record.

| Value | Description |
| --- | --- |
| `userIdentity` | A user identity dictionary representing the participant in a shared record, described in [User Identity Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltemy). |
| `permission` | The participant’s read and write permissions. Possible values are: `NONE`, `READ_ONLY`, `READ_WRITE`, and `UNKNOWN`. |
| `type` | Type of participant. Possible values are: `OWNER`, `ADMINISTRATOR`, `USER`, `PUBLIC_USER`, and `UNKNOWN`. |
| `acceptanceStatus` | Indicates the status of accepting the shared record. Possible values are: `INVITED`, `ACCEPTED`, `REMOVED`, and `UNKNOWN`. |

### ShortGUID Dictionary

A global identifier for a record.

| Value | Description |
| --- | --- |
| `value` | String representing the value of the short global ID. This key is required. |
| `shouldFetchRootRecord` | A Boolean value that indicates whether the root record should be fetched with this record. This key is required. |
| `rootRecordDesiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned in the root record. The default is `null`, which fetches all record fields. |

### ShortGUID Result Dictionary

A dictionary representing the result of fetching a shared record.

| Value | Description |
| --- | --- |
| `containerIdentifier` | A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| `databaseScope` | The type of database. Possible values are: `PRIVATE` and `SHARED`. |
| `rootRecordName` | The name of the root record that was shared. |
| `ownerIdentity` | A user identity dictionary representing the owner of the shared record, described in [User Identity Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltemy). |
| `environment` | The version of the app’s container. Possible values are `development` and `production`. |
| `rootRecord` | A record dictionary, described in [Record Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm), that represents the shared record. |
| `zoneID` | A dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `share` | The _share record_, a record dictionary, described in [Record Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm), where the `recordType` is `cloudKit.share`. |
| `shortGUID` | A short GUID, described in [ShortGUID Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcoi). |
| `potentialMatchList` | If the participant is not identifiable, this array contains potential participants that the user can choose from.  The array contains dictionaries with the following keys: `participantId` (`String`) and `contactInformation` (`Dictionary`).  The `contactInformation` dictionary contains keys: `emailAddress` (`String`) and `phoneNumber` (`String`). |
| `participantPermission` | The participant’s read and write permissions. Possible values are: `NONE`, `READ_ONLY`, `READ_WRITE`, and `UNKNOWN`. |
| `participantStatus` | Indicates the status of accepting the shared record. Possible values are: `INVITED`, `ACCEPTED`, `REMOVED`, and `UNKNOWN`. |
| `participantType` | Type of participant. Possible values are: `OWNER`, `ADMINISTRATOR`, `USER`, `PUBLIC_USER`, and `UNKNOWN`. |
| `webpageURL` | This is the fallback webpage (`String`) you may specify using CloudKit Dashboard to direct users to a webpage when an operation fails; for example, a `resolve/accept` endpoint doesn’t succeed. |

### ShortGUID Fetch Error Dictionary

A dictionary representing the result of fetching a shared record.

| Value | Description |
| --- | --- |
| `reason` | A string indicating the reason for the error. |
| `retryAfter` | The suggested time to wait before trying this operation again. If this key is not set, the operation can’t be retried. |
| `serverErrorCode` | A string containing the code for the error that occurred. For possible values, see [Error Codes](ErrorCodes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnbnknltc). |

### Sort Descriptor Dictionary

A sort descriptor dictionary determines the order of the fetched records.

| Value | Description |
| --- | --- |
| `fieldName` | The name of a field belonging to the record type. Used to sort the fetched records. This key is required. |
| `ascending` | A Boolean value that indicates whether the fetched records should be sorted in ascending order. If `true`, the records are sorted in ascending order. If `false`, the records are sorted in descending order. The default value is `true`. |
| `relativeLocation` | A field-value dictionary, described in [Record Field Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcna), that is the reference location to use when sorting. Records are sorted based on their distance to this location. Used only if `fieldName` is a `Location` type. |

### Subscription Dictionary

A subscription dictionary describes a successful subscription fetch containing the following keys:

| Key | Description |
| --- | --- |
| `zoneID` | A dictionary that identifies a record zone to monitor in the database, described in [Zone ID Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `subscriptionID` | A unique identifier for the subscription. |
| `subscriptionType` | The type of subscription. Possible values are: `"zone"`, and `"query"`. This key is required. |
| `query` | A dictionary containing the matching criteria to apply to records, described in [Query Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcni). |
| `firesOn` | An array of keywords that specifies the actions that should trigger push notifications. Possible values in the array are: `"create"`, `"update"`, and `"delete"`. This key is not used if `query` is null. |
| `firesOnce` | A Boolean value indicating whether push notifications should be triggered once. If `true`, push notifications are sent once. If `false`, they can be sent multiple times. The default value is `false`. |
| `notificationInfo` | A dictionary containing information about how the system should alert the user, described in [Notification Info Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcmy). |
| `zoneWide` | A Boolean value determining whether all zones should be searched. If `true`, CloudKit searches all zones. If `false`, CloudKit searches the default zone only. |

### User Dictionary

A user dictionary describes a user with the following keys:

| Key | Description |
| --- | --- |
| `userRecordName` | The record name field in the associated `Users` record. |
| `firstName` | The user’s first name. If not found, `firstName` is `null`. |
| `lastName` | The user’s last name. If not found, `lastName` is `null`. |
| `emailAddress` | This key is included only when fetching users by email, described in [Fetching Users by Email (users/lookup/email)](LookupUsersbyEmail.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjufvjvomi). |

### User Identity Dictionary

A dictionary that identifies a user with the following keys:

| Key | Description |
| --- | --- |
| `lookupInfo` | A dictionary identifying the user, described in [User Identity Lookup Information Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltemi). |
| `userRecordName` | The record name field in the associated `Users` record. |
| `nameComponents` | A dictionary representing the user’s name, described in [Name Components Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltemq). |

### User Identity Lookup Information Dictionary

A dictionary used to lookup user information:

| Key | Description |
| --- | --- |
| `emailAddress` | A string representing user’s email address. |
| `phoneNumber` | A string representing user’s phone number. |
| `userRecordName` | The record name field in the associated `Users` record. |

### Zone Dictionary

A zone dictionary describes a successful zone fetch containing the following keys:

| Key | Description |
| --- | --- |
| `zoneID` | The dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `syncToken` | The current point in the zone’s change history. |
| `atomic` | A Boolean value indicating whether this zone supports atomic operations. |

### Zone ID Dictionary

The zone ID identifies an area for organizing related records in a database.

| Key | Description |
| --- | --- |
| `zoneName` | The name that identifies the record zone. The default value is `_defaultZone`, which indicates the default zone of the current database. This key is required. |
| `ownerRecordName` | String representing the zone owner’s user record name. Use this key to identify a zone owned by another user. The default value is the current user’s record name. |

[Registering Tokens (tokens/register)](RegisterTokens.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrqfvjvomi)

[Error Codes](ErrorCodes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnbnknltc)
