---
title: GameSave
framework: GameSave
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/gamesave
source_url: 'https://developer.apple.com/documentation/gamesave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamesave.json'
content_hash: 'sha256:c771c4bd762597c0'
translated: false
---

> Navigation: [Technologies](technologies.md)

# GameSave

<sub>Framework</sub>

Store and sync your application’s save files in iCloud.

## Overview

GameSave uses iCloud Drive to synchronize your application’s save data across devices. The framework provides a set of APIs for reading and writing one or more files to a directory, while abstracting away iCloud concepts. It handles common save syncing scenarios like conflict resolution and offline play. Additionally, it provides a set of convenience UI alerts for these typical scenarios. GameSave also supports local saving for when the device isn’t signed into iCloud Drive.

> [!important] Important
> For GameSave to store the game data in the player’s iCloud account, you need to provide an identifier for the iCloud container that stores the data. Add the iCloud capability to your project and select the iCloud Documents checkbox. For more information, see [Configuring iCloud services](xcode/configuring-icloud-services.md).

## Topics

### Synced directory

- [GameSaveSyncedDirectory](gamesave/gamesavesynceddirectory.md) — A cloud-synced directory for game-save data.

### Error domain

- [GameSaveErrorDomain](gamesave/gamesaveerrordomain.md) — The error domain name for GameSave errors.

### Synced directory (Objective-C)

- [GSSyncedDirectory](gamesave/gssynceddirectory.md) — A cloud-synced directory for game-save data.
