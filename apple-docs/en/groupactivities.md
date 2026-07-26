---
title: Group Activities
framework: Group Activities
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/groupactivities
source_url: 'https://developer.apple.com/documentation/groupactivities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/groupactivities.json'
content_hash: 'sha256:a16db233d9784d1d'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Group Activities

<sub>Framework</sub>

Create app-specific activities your users can share and experience together.

## Overview

With the Group Activities framework, you can provide your app’s content in SharePlay experiences, which create a sense of connection and immediacy for your users. For example, a video-streaming app might offer the ability to attend movie-watching parties in which participants watch simultaneously from their personal devices. The app handles the playback on each device, but the Group Activities framework synchronizes that playback and facilitates communication between the devices.

This framework leverages the FaceTime infrastructure to synchronize your app’s activities and to invite other participants to join those activities. When your app’s UI contains shareable activities, adopt the [GroupActivity](groupactivities/groupactivity.md) protocol in the objects you use to represent those activities. When a group activity begins, use the [GroupSession](groupactivities/groupsession.md) object to synchronize your app’s behavior with other participating devices.

> [!note] Note
> The Group Activities framework uses end-to-end encryption on all session data that the [GroupSession](groupactivities/groupsession.md) object synchronizes between devices. Apple doesn’t have the keys to decrypt this data. Your use of the Group Activities framework doesn’t provide Apple with visibility into the content your app shares, or information related to playback of media content in your app, such as where in the content a user starts, pauses, or skips a session. Apple servers facilitating Group Activities sessions don’t know the identity of your app. Occasionally, Apple may ask a small number of users to help troubleshoot issues, such as by [capturing a sysdiagnose or installing a debugging profile](https://developer.apple.com/bug-reporting/profiles-and-logs/), which may incidentally result in Apple collecting some information related to content shared in your app.

## Topics

### Essentials

- [com.apple.developer.group-session](bundleresources/entitlements/com.apple.developer.group-session.md) — A Boolean value that indicates whether the app may implement shared group experiences.

### Activity definition

- [Defining your app’s SharePlay activities](groupactivities/defining-your-apps-shareplay-activities.md) — Configure your app’s SharePlay support and define the activities that people can perform from your app.
- [Supporting coordinated media playback](avfoundation/supporting-coordinated-media-playback.md) — Create synchronized media experiences that enable users to watch and listen across devices.
- [GroupActivity](groupactivities/groupactivity.md) — A type that can advertise your app’s activities to other participants.
- [GroupActivityMetadata](groupactivities/groupactivitymetadata.md) — Text and image content that describes an activity to potential participants.
- [GroupActivityActivationResult](groupactivities/groupactivityactivationresult.md) — The result of preparing to start a custom activity.
- [GroupActivityTransferRepresentation](groupactivities/groupactivitytransferrepresentation.md) — A type that lets you start a group activity from a known context.

### Interface presentation

- [Presenting SharePlay activities from your app’s UI](groupactivities/promoting-shareplay-activities-from-your-apps-ui.md) — Make it easy for people to start activities from your app’s UI, from the system share sheet, or using AirPlay over AirDrop.
- [GroupActivitySharingController](groupactivities/groupactivitysharingcontroller-4gtfk.md) — A macOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.
- [GroupActivitySharingController](groupactivities/groupactivitysharingcontroller-ybcy.md) — An iOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.

### Session management

- [Joining and managing a shared activity](groupactivities/joining-and-managing-a-shared-activity.md) — Configure the session when a SharePlay activity starts, and handle events that occur during the lifetime of the activity.
- [Drawing content in a group session](groupactivities/drawing_content_in_a_group_session.md) — Invite your friends to draw on a shared canvas while on a FaceTime call.
- [GroupSession](groupactivities/groupsession.md) — A session for an in-progress activity that synchronizes content among participant devices.
- [CustomMessageIdentifiable](groupactivities/custommessageidentifiable.md) — A type that assigns a custom ID string to messages you send to other devices.
- [Participant](groupactivities/participant.md) — An active participant in a group session.

### Spatial activities

- [Configure your visionOS app for sharing with people nearby](groupactivities/configure-your-app-for-sharing-with-people-nearby.md) — Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](groupactivities/adding-spatial-persona-support-to-an-activity.md) — Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [SystemCoordinator](groupactivities/systemcoordinator.md) — A type you use to coordinate your interface’s behavior when an active SharePlay session supports spatial placement of content.
- [ParticipantState](groupactivities/systemcoordinator/participantstate.md) — A structure that tells you whether a participant supports a shared simulation space for the current activity.
- [groupActivityAssociation(_:)](<swiftui/view/groupactivityassociation(__).md>) — Specifies how a view should be associated with the current SharePlay group activity.
- [GroupActivityAssociationInteraction](groupactivities/groupactivityassociationinteraction.md) — An interaction configures a view’s association with the current SharePlay group activity.
- [GroupActivityAssociationKind](groupactivities/groupactivityassociationkind.md) — An association a user-interface element can have with a SharePlay group activity.

### Custom spatial templates

- [Building a guessing game for visionOS](groupactivities/building-a-guessing-game-for-visionos.md) — Create a team-based guessing game for visionOS using Group Activities.
- [SpatialTemplate](groupactivities/spatialtemplate.md) — An interface you use to create custom arrangements of spatial Personas in a scene.
- [SpatialTemplatePreference](groupactivities/spatialtemplatepreference.md) — A structure that specifies the preferred arrangement of participant spatial Personas in a shared simulation space.
- [SpatialTemplateSeatElement](groupactivities/spatialtemplateseatelement.md) — A spatial template element that represents a seat for a participant in the activity.
- [SpatialTemplateElement](groupactivities/spatialtemplateelement.md) — An interface that defines an element in your spatial template.
- [SpatialTemplateElementPosition](groupactivities/spatialtemplateelementposition.md) — A type that defines the position of an element in a spatial template.
- [SpatialTemplateElementDirection](groupactivities/spatialtemplateelementdirection.md) — The initial direction a participant faces when an activity starts.
- [SpatialTemplateRole](groupactivities/spatialtemplaterole.md) — An interface for defining roles that you assign to the participants of a group activity.

### File and data transfer

- [Creating a collaborative photo gallery with SharePlay](groupactivities/creating-a-collaborative-photo-gallery-with-shareplay.md) — Build a shared photo gallery by using SharePlay to synchronize images among participants.
- [Synchronizing data during a SharePlay activity](groupactivities/synchronizing-data-during-a-shareplay-activity.md) — Send custom messages and data between devices to synchronize content for your activity, and incorporate messages your app receives from other participants.
- [GroupSessionMessenger](groupactivities/groupsessionmessenger.md) — An object that transfers app-specific data between the devices joined in a group session.
- [GroupSessionJournal](groupactivities/groupsessionjournal.md) — An object that manages file and data transfers between participants joined in a group session.

### System status

- [GroupStateObserver](groupactivities/groupstateobserver.md) — An object that contains information about the system’s ability to start SharePlay experiences.
