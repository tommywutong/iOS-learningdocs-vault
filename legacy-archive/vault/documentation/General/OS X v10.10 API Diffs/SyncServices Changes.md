---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/SyncServices.html
archived_at: '2026-07-15T07:34:47.524670Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# SyncServices Changes

## SyncServices

ISyncChange.hModified ISyncChangeTypeAdd

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncChangeTypeDelete

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncChangeTypeModify

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncChangeTypeNone

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.7 |

ISyncClient.hModified ISyncStatusCancelled

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncStatusErrors

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncStatusFailed

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncStatusNever

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncStatusRunning

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncStatusSuccess

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

Modified ISyncStatusWarnings

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.7 |

ISyncCoreData.hModified -[NSPersistentStoreCoordinatorSyncing managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didApplyChange:toManagedObject:inSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didCancelSyncSession:error:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didCommitChanges:inSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didFinishSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didPullChangesInSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didPushChangesInSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willApplyChange:toManagedObject:inSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willDeleteRecordWithIdentifier:inSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willPullChangesInSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willPushChangesInSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willPushRecord:forManagedObject:inSyncSession:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinatorShouldStartSyncing:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

ISyncSessionDriver.hModified -[ISyncSessionDriverDataSource changedRecordsForEntityName:moreComing:error:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource changesForEntityName:moreComing:error:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource entityNamesToPull]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource entityNamesToSync]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource identifiersForRecordsToDeleteForEntityName:moreComing:error:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource lastAnchorForEntityName:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource nextAnchorForEntityName:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource sessionBeginTimeout]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ISyncSessionDriverDataSource sessionPullChangesTimeout]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

SyncServicesErrors.hModified ISyncSessionClientAlreadySyncingError

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.7 |

Modified ISyncSessionDriverFatalError

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.7 |

Modified ISyncSessionDriverPullFailureError

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.7 |

Modified ISyncSessionDriverRegistrationError

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.7 |

Modified ISyncSessionUserCanceledSessionError

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.4 | OS X 10.7 |

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
