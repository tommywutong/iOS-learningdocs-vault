---
title: GroupSessionJournal
framework: Group Activities
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/groupactivities/groupsessionjournal
source_url: 'https://developer.apple.com/documentation/groupactivities/groupsessionjournal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/groupactivities/groupsessionjournal.json'
content_hash: 'sha256:6c199ac811f618a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Group Activities](../groupactivities.md)

# GroupSessionJournal

<sub>Class</sub>

An object that manages file and data transfers between participants joined in a group session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
final class GroupSessionJournal
```

## Overview

A [GroupSessionJournal](groupsessionjournal.md) object lets you transfer files and other data objects between participants of a shared activity. A journal object isn’t a replacement for a [GroupSessionMessenger](groupsessionmessenger.md) object, which you use to transfer time-sensitive messages and commands between participants. Instead, use it to associate files and other data objects with the activity. For example, you might share images that people drag into your app as part of the activity. The journal makes these data objects available to all participants, regardless of when they joined the session.

After your app joins an activity and receives a session object, create a [GroupSessionJournal](groupsessionjournal.md) object and store a strong reference to it. To add a file or data object to the group’s journal, call the [add(_:)](<groupsessionjournal/add(__).md>) or [add(_:metadata:)](<groupsessionjournal/add(__metadata_).md>) method with the data you want to share. The types you specify must adopt the [Transferable](../coretransferable/transferable.md) protocol from the Core Transferable framework. The journal object uses that protocol to package a version of your data suitable for sending to other devices.

To receive data that a participant added to the journal, configure a task to listen for asynchronous updates to the [attachments](groupsessionjournal/attachments-swift.property.md) property of your [GroupSessionJournal](groupsessionjournal.md) object. When someone adds or removes an attachment, the journal updates the array and executes your task. Load the contents of an attachment using the [load(_:)](<groupsessionjournal/attachment/load(__).md>) method of that type. You can also retrieve any attachment-specific metadata, such as a shared ID or display name, that you included with the attached file. The following example creates a task that waits on a custom image type. The `journal` variable contains a previously configured [GroupSessionJournal](groupsessionjournal.md) object.

```swift
let attachmentListener = Task {
   for await attachments in journal.attachments {
       for attachment in attachments {
           let receivedItem = try await attachment.load(MyImageItem.self)
           // Do something with the item you receive.
       }
   }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an attachment manager

- [init(session:)](<groupsessionjournal/init(session_).md>) — Creates a journal and associates it with the specified session of a group activity.

### Uploading content to the session

- [add(_:)](<groupsessionjournal/add(__).md>) — Adds the specified item to the journal and begins transferring the item’s data to the other participants’ devices so they can access it.
- [add(_:metadata:)](<groupsessionjournal/add(__metadata_).md>) — Adds the specified item and metadata to the journal and begins transferring the data to the other participants’ devices so they can access it.

### Downloading content from the session

- [attachments](groupsessionjournal/attachments-swift.property.md) — The currently available attachments for you to download and incorporate into your app.
- [Attachments](groupsessionjournal/attachments-swift.struct.md) — An asynchronous sequence that contains one or more incoming attachment containers for you to process.
- [Attachment](groupsessionjournal/attachment.md) — A container for the data you download.

### Removing content from the session

- [remove(attachment:)](<groupsessionjournal/remove(attachment_).md>) — Removes the specified attachment from the journal on all sessions.

## See Also

### File and data transfer

- [Creating a collaborative photo gallery with SharePlay](creating-a-collaborative-photo-gallery-with-shareplay.md) — Build a shared photo gallery by using SharePlay to synchronize images among participants.
- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md) — Send custom messages and data between devices to synchronize content for your activity, and incorporate messages your app receives from other participants.
- [GroupSessionMessenger](groupsessionmessenger.md) — An object that transfers app-specific data between the devices joined in a group session.
