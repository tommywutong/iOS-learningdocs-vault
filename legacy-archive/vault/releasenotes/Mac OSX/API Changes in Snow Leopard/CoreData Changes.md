---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/CoreData.html
archived_at: '2026-07-18T02:58:42.546864Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# CoreData Changes

## CoreData

CoreDataErrors.hAdded [NSInferredMappingModelError](https://developer.apple.com/documentation/coredata/nsinferredmappingmodelerror)NSAttributeDescription.hAdded [NSObjectIDAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/objectidattributetype)NSEntityDescription.hAdded [-[NSEntityDescription renamingIdentifier]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425135-renamingidentifier)Added [-[NSEntityDescription setRenamingIdentifier:]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425135-renamingidentifier)NSEntityMigrationPolicy.hAdded [NSMigrationEntityPolicyKey](https://developer.apple.com/documentation/coredata/nsmigrationentitypolicykey)NSExpressionDescription.hAdded [NSExpressionDescription](https://developer.apple.com/documentation/coredata/nsexpressiondescription)Added [-[NSExpressionDescription expression]](https://developer.apple.com/documentation/coredata/nsexpressiondescription/1506817-expression)Added [-[NSExpressionDescription expressionResultType]](https://developer.apple.com/documentation/coredata/nsexpressiondescription/1506706-expressionresulttype)Added [-[NSExpressionDescription setExpression:]](https://developer.apple.com/documentation/coredata/nsexpressiondescription/1506817-expression)Added [-[NSExpressionDescription setExpressionResultType:]](https://developer.apple.com/documentation/coredata/nsexpressiondescription/1506706-expressionresulttype)NSFetchRequest.hAdded [-[NSFetchRequest fetchOffset]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506770-fetchoffset)Added [-[NSFetchRequest includesPendingChanges]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506724-includespendingchanges)Added [-[NSFetchRequest propertiesToFetch]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506851-propertiestofetch)Added [-[NSFetchRequest returnsDistinctResults]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506344-returnsdistinctresults)Added [-[NSFetchRequest setFetchOffset:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506770-fetchoffset)Added [-[NSFetchRequest setIncludesPendingChanges:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506724-includespendingchanges)Added [-[NSFetchRequest setPropertiesToFetch:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506851-propertiestofetch)Added [-[NSFetchRequest setReturnsDistinctResults:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506344-returnsdistinctresults)Added [NSDictionaryResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/1506237-dictionaryresulttype)NSManagedObjectContext.hAdded [NSManagedObjectContextWillSaveNotification](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextwillsavenotification)NSMappingModel.hAdded [+[NSMappingModel inferredMappingModelForSourceModel:destinationModel:error:]](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506468-inferredmappingmodel)NSPersistentStore.hAdded [-[NSPersistentStore loadMetadata:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506273-loadmetadata)Added [+[NSPersistentStore migrationManagerClass]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506361-migrationmanagerclass)NSPersistentStoreCoordinator.hAdded +[NSPersistentStoreCoordinator elementsDerivedFromSupportURL:]Added [NSEntityNameInPathKey](https://developer.apple.com/documentation/coredata/nsentitynameinpathkey)Added [NSExternalRecordsDirectoryOption](https://developer.apple.com/documentation/coredata/nsexternalrecordsdirectoryoption)Added [NSInferMappingModelAutomaticallyOption](https://developer.apple.com/documentation/coredata/nsinfermappingmodelautomaticallyoption)Added [NSModelPathKey](https://developer.apple.com/documentation/coredata/nsmodelpathkey)Added [NSObjectURIKey](https://developer.apple.com/documentation/coredata/nsobjecturikey)Added [NSPersistentStoreCoordinatorWillRemoveStoreNotification](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinatorwillremovestorenotification)Added [NSSQLiteAnalyzeOption](https://developer.apple.com/documentation/coredata/nssqliteanalyzeoption)Added [NSSQLiteManualVacuumOption](https://developer.apple.com/documentation/coredata/nssqlitemanualvacuumoption)Added NSSpotlightFileExtensionOptionAdded [NSStorePathKey](https://developer.apple.com/documentation/coredata/nsstorepathkey)Added [NSStoreUUIDInPathKey](https://developer.apple.com/documentation/coredata/nsstoreuuidinpathkey)NSPropertyDescription.hAdded [-[NSPropertyDescription isIndexedBySpotlight]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506784-indexedbyspotlight)Added -[NSPropertyDescription isStoredInTruth]Added [-[NSPropertyDescription renamingIdentifier]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506641-renamingidentifier)Added [-[NSPropertyDescription setIndexedBySpotlight:]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506784-isindexedbyspotlight)Added [-[NSPropertyDescription setRenamingIdentifier:]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506641-renamingidentifier)Added -[NSPropertyDescription setStoredInTruth:]

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
