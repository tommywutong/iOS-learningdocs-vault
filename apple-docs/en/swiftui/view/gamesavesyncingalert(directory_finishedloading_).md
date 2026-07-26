---
title: 'gameSaveSyncingAlert(directory:finishedLoading:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/gamesavesyncingalert(directory:finishedloading:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/gamesavesyncingalert(directory:finishedloading:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/gamesavesyncingalert%28directory%3Afinishedloading%3A%29.json'
content_hash: 'sha256:381390c49029696d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# gameSaveSyncingAlert(directory:finishedLoading:)

<sub>Instance Method</sub>

Presents a modal view while the game synced directory loads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func gameSaveSyncingAlert(directory: Binding<GameSaveSyncedDirectory?>, finishedLoading: @escaping @MainActor @Sendable () -> Void) -> some View

```

## Parameters

- `directory` — A binding to an optional game synced directory that was returned by calling `GameSaveSyncedDirectory/openDirectory(containerIdentifier:)`. If this value is `nil`, the view doesn’t display.

- `finishedLoading` — The closure to execute after the loading process completes.

## Discussion

Use this method when you want to present a modal loading view to the user when a Boolean value you provide is true.
