---
title: PermissionKit
framework: PermissionKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/permissionkit
source_url: 'https://developer.apple.com/documentation/permissionkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/permissionkit.json'
content_hash: 'sha256:47dc51ecfdf96e26'
translated: false
---

> Navigation: [Technologies](technologies.md)

# PermissionKit

<sub>Framework</sub>

Create communication experiences between a child and their parent or guardian.

## Overview

Use `PermissionKit` in your app to adjust communication rules for a child account on iCloud. `PermissionKit` provides a way to create consistent asking experiences between a child and their parent or guardian that maintains UI consistency with other communication experiences across the system.

> [!important] Important
> Communication experiences using the `PermissionKit` framework are only available using iMessage.

## Topics

### Essentials

- [Creating a communication experience](permissionkit/creating-a-communication-experience.md) — Request permission from a parent or guardian to modify a child’s communication rules.
- [AskCenter](permissionkit/askcenter.md) — A class that manages permission requests you send to parents or guardians for approval.
- [PermissionQuestion](permissionkit/permissionquestion.md) — A class that captures a permission question posed by a person.

### Permission topics

- [SignificantAppUpdateTopic](permissionkit/significantappupdatetopic.md) — A topic for requesting permission for significant app updates.
- [CommunicationTopic](permissionkit/communicationtopic.md) — A topic for requesting communication permission with specific people.

### Presentation

- [PermissionButton](permissionkit/permissionbutton.md) — A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits.

### Response management

- [responses(for:)](<permissionkit/askcenter/responses(for_).md>) — Registers the topic type with the system and returns an asynchronous sequence of responses.
- [PermissionResponse](permissionkit/permissionresponse.md) — A full permission response that includes the original question and chosen answer.
- [CommunicationHandle](permissionkit/communicationhandle.md) — Contact information for identifying and communicating with a person.
- [PermissionChoice](permissionkit/permissionchoice.md) — A class that uniquely identifies a specific, statically defined permission choice.
- [CommunicationLimits](permissionkit/communicationlimits.md) — A type that encapsulates the communication limits for your app.

### Supporting types

- [QuestionTopic](permissionkit/questiontopic.md) — A protocol that defines a question topic that can be used to interpret what a person is asking for.

### Errors

- [AskError](permissionkit/askerror.md) — Represents errors you encounter when asking a person to send a communication permission question.

### Deprecated APIs

- [CommunicationLimitsButton](permissionkit/communicationlimitsbutton.md) — A button that presents a system UI to a parent or guardian to ask for an exception to a child’s communication limits. _(deprecated)_

### Structures

- [AskPermissionAction](permissionkit/askpermissionaction.md) — An action that sends a permission question to a parent or guardian.
