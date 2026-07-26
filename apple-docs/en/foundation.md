---
title: Foundation
framework: Foundation
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation
source_url: 'https://developer.apple.com/documentation/foundation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation.json'
content_hash: 'sha256:c8fe9df838099279'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Foundation

<sub>Framework</sub>

Access essential data types, collections, and operating-system services to define the base layer of functionality for your app.

## Overview

The Foundation framework provides a base layer of functionality for apps and frameworks, including data storage and persistence, text processing, date and time calculations, sorting and filtering, and networking. The classes, protocols, and data types defined by Foundation are used throughout the macOS, iOS, watchOS, and tvOS SDKs.

## Topics

### Fundamentals

- [Numbers, Data, and Basic Values](foundation/numbers-data-and-basic-values.md) — Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](foundation/strings-and-text.md) — Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](foundation/collections.md) — Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](foundation/dates-and-times.md) — Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](foundation/units-and-measurement.md) — Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](foundation/data-formatting.md) — Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](foundation/filters-and-sorting.md) — Use predicates, expressions, and sort descriptors to examine elements in collections and other services.

### App Support

- [Task Management](foundation/task-management.md) — Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](foundation/resources.md) — Access assets and other data bundled with your app.
- [Notifications](foundation/notifications.md) — Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](foundation/app-extension-support.md) — Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](foundation/errors-and-exceptions.md) — Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](foundation/scripting-support.md) — Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.

### Files and Data Persistence

- [File System](foundation/file-system.md) — Create, read, write, and examine files and folders in the file system.
- [Archives and Serialization](foundation/archives-and-serialization.md) — Convert objects and values to and from property list, JSON, and other flat binary representations.
- [Settings](foundation/settings.md) — Configure your app using data you store persistently on the local disk or in iCloud.
- [Spotlight](foundation/spotlight.md) — Search for files and other items on the local device, and index your app’s content for searching.
- [iCloud](foundation/icloud.md) — Manage files and key-value data that automatically synchronize among a user’s iCloud devices.
- [Optimizing Your App’s Data for iCloud Backup](foundation/optimizing-your-app-s-data-for-icloud-backup.md) — Minimize the space and time that backups take to create by excluding purgeable and nonpurgeable data from backups.

### Networking

- [URL Loading System](foundation/url-loading-system.md) — Interact with URLs and communicate with servers using standard Internet protocols.
- [Bonjour](foundation/bonjour.md) — Advertise services for easy discovery on local networks, or discover services advertised by others.

### Low-Level Utilities

- [XPC](foundation/xpc.md) — Manage secure interprocess communication.
- [Object Runtime](foundation/object-runtime.md) — Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Processes and Threads](foundation/processes-and-threads.md) — Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](foundation/streams-sockets-and-ports.md) — Use low-level Unix features to manage input and output among files, processes, and the network.

### Reference

- [Foundation Enumerations](foundation/foundation-enumerations.md)
- [Foundation Data Types](foundation/foundation-data-types.md) — This document describes the data types and constants found in the Foundation framework.

### Classes

- [ProgressManager](foundation/progressmanager.md) — An object that conveys ongoing progress to the user for a specified task. _(beta)_
- [ProgressReporter](foundation/progressreporter.md) — ProgressReporter is a wrapper for ProgressManager that carries information about ProgressManager. _(beta)_

### Protocols

- [NSPredicateValidating](foundation/nspredicatevalidating.md)

### Structures

- [Subprogress](foundation/subprogress.md) — Subprogress is used to establish parent-child relationship between two instances of `ProgressManager`. _(beta)_
