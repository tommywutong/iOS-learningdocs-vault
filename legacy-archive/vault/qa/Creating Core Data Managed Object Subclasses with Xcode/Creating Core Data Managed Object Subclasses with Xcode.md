---
title: Creating Core Data Managed Object Subclasses with Xcode
apple_id: DTS40017616
resource_type: QA
platform: tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: CoreBluetooth
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/qa/qa1952/_index.html
archived_at: '2026-07-18T02:37:35.230380Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1952

# Creating Core Data Managed Object Subclasses with Xcode

## Q:  How do I create Core Data managed object subclasses for my entities with Xcode?

A: Follow these steps to create Core Data managed object subclasses with Xcode:

1. Select your Core Data model in the project navigator.

   Xcode displays all your entities in the outline view of the editor area.
2. Select an entity in the outline view, and verify that the Codegen pop-up menu is set to `Manual/None` in the Data Model inspector as shown in Figure 1. Repeat this step for all entities you want to create Core Data managed object subclasses.

__Figure 1__  Setting the Codegen pop-up menu to Manual/None for the Person entity. The numbers in this figure correspond to the steps above.

!!

1. Choose Editor > Create NSManagedObject Subclass… as shown in Figure 2.

__Figure 2__  Select Create NSManagedObject Subclass... to start generating a Core Data managed object subclass.

!!

1. In the sheet that appears, select the data model that contain your entities, and click Next.

__Figure 3__  Select your data model from the list.

!!

1. In the sheet that appears, select the entities whose Core Data managed object subclasses you want to create, and click Next.

__Figure 4__  Select your entities from the list.

!!

1. In the sheet that appears, select a location to save your files, and click Create.

__Figure 5__  Select a location for your files.

!!

Xcode creates and saves files named ClassName+CoreDataClass and ClassName+CoreDataProperties for each of your selected entity in the selected location where ClassName is the name of your entity's `NSManagedObject` subclass. ClassName+CoreDataClass implements the `NSManagedObject` subclass as shown in Figure 6.

__Figure 6__  Viewing PersonMO+CoreDataClass, a Core Data managed object subclass.

!!

ClassName+CoreDataProperties implements a ClassName+CoreDataClass extension (for Swift apps) or category (for Objective-C apps) as shown in Figure 7.

__Figure 7__  Viewing PersonMO+CoreDataProperties, a PersonMO+CoreDataClass extension.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-03-09 | New document that describes how to create Core Data managed object subclasses with Xcode. |

