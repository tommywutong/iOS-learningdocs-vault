---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/CloudKit.html
archived_at: '2026-07-18T02:53:50.508981Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# CloudKit Changes for Swift

### CloudKit

Removed CKOperation.activityStart() -> os_activity_tAdded [CKContainer.fetchAllLongLivedOperationIDsWithCompletionHandler(_: ([String]?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399160-fetchalllonglivedoperationidswit)Added [CKContainer.fetchLongLivedOperationWithID(_: String, completionHandler: (CKOperation?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399164-fetchlonglivedoperationwithid)Added [CKFetchWebAuthTokenOperation](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation)Added [CKFetchWebAuthTokenOperation.APIToken](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/1515095-apitoken)Added [CKFetchWebAuthTokenOperation.fetchWebAuthTokenCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/1514980-fetchwebauthtokencompletionblock)Added [CKFetchWebAuthTokenOperation.init(APIToken: String)](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/1515266-initwithapitoken)Added [CKOperation.longLived](https://developer.apple.com/documentation/cloudkit/ckoperation/1452374-longlived)Added [CKOperation.longLivedOperationWasPersistedBlock](https://developer.apple.com/documentation/cloudkit/ckoperation/1452366-longlivedoperationwaspersistedbl)Added [CKOperation.operationID](https://developer.apple.com/documentation/cloudkit/ckoperation/1452362-operationid)Modified [CKContainer](https://developer.apple.com/documentation/cloudkit/ckcontainer)

|  | Declaration |
| --- | --- |
| From | ``` class CKContainer : NSObject {     init()     class func defaultContainer() -> CKContainer      init(identifier containerIdentifier: String)     class func containerWithIdentifier(_ containerIdentifier: String) -> CKContainer     var containerIdentifier: String? { get }     func addOperation(_ operation: CKOperation) } extension CKContainer {     var privateCloudDatabase: CKDatabase { get }     var publicCloudDatabase: CKDatabase { get } } extension CKContainer {     func accountStatusWithCompletionHandler(_ completionHandler: (CKAccountStatus, NSError?) -> Void) } extension CKContainer {     func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock)     func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) } extension CKContainer {     func fetchUserRecordIDWithCompletionHandler(_ completionHandler: (CKRecordID?, NSError?) -> Void)     func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: ([CKDiscoveredUserInfo]?, NSError?) -> Void)     func discoverUserInfoWithEmailAddress(_ email: String, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void)     func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) } ``` |
| To | ``` class CKContainer : NSObject {     init()     class func defaultContainer() -> CKContainer      init(identifier containerIdentifier: String)     class func containerWithIdentifier(_ containerIdentifier: String) -> CKContainer     var containerIdentifier: String? { get }     func addOperation(_ operation: CKOperation) } extension CKContainer {     var privateCloudDatabase: CKDatabase { get }     var publicCloudDatabase: CKDatabase { get } } extension CKContainer {     func accountStatusWithCompletionHandler(_ completionHandler: (CKAccountStatus, NSError?) -> Void) } extension CKContainer {     func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock)     func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) } extension CKContainer {     func fetchUserRecordIDWithCompletionHandler(_ completionHandler: (CKRecordID?, NSError?) -> Void)     func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: ([CKDiscoveredUserInfo]?, NSError?) -> Void)     func discoverUserInfoWithEmailAddress(_ email: String, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void)     func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) } extension CKContainer {     func fetchAllLongLivedOperationIDsWithCompletionHandler(_ completionHandler: ([String]?, NSError?) -> Void)     func fetchLongLivedOperationWithID(_ operationID: String, completionHandler completionHandler: (CKOperation?, NSError?) -> Void) } ``` |

Modified [CKOperation](https://developer.apple.com/documentation/cloudkit/ckoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKOperation : NSOperation {     init()     func activityStart() -> os_activity_t     var container: CKContainer?     var usesBackgroundSession: Bool     var allowsCellularAccess: Bool } ``` |
| To | ``` class CKOperation : NSOperation {     init()     var container: CKContainer?     var usesBackgroundSession: Bool     var allowsCellularAccess: Bool     var operationID: String { get }     var longLived: Bool     var longLivedOperationWasPersistedBlock: () -> Void } ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
