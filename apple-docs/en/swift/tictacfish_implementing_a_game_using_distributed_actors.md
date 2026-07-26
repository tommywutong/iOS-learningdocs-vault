---
title: 'TicTacFish: Implementing a game using distributed actors'
framework: Distributed
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.0+, iPadOS 16.0+, Xcode 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/tictacfish_implementing_a_game_using_distributed_actors
source_url: 'https://developer.apple.com/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors.json'
content_hash: 'sha256:0ff3af1d88522c7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# TicTacFish: Implementing a game using distributed actors

<sub>Sample Code</sub>

Use distributed actors to take your Swift concurrency and actor-based apps beyond a single process.

## Overview

> [!note] Note
> This sample code project is associated with WWDC22 session [110356: Meet distributed actors in Swift](../https_/developer.apple.com/wwdc22/110356.md).

### Configure the sample code project

Because the sample app uses new Swift language features introduced in Swift 5.7, you need at least the following versions of iOS, macOS, and Xcode to edit and run the samples:

To run the iOS app:

- iOS 16
- macOS 13
- Xcode 14

To run the server-side application on your local Mac:

- macOS 13
- Xcode 14

To run the server-side application on a Linux server, compile and run the `Server` package using:

- Any supported Linux distribution
- Swift 5.7

You can try out the peer-to-peer local networking part of the sample app by starting multiple simulators (such as an iPhone 13 and an iPhone 13 Pro) from the same Xcode project.

## See Also

### Standard Library

- [Int](int.md) — A signed integer value type.
- [Double](double.md) — A double-precision, floating-point value type.
- [String](string.md) — A Unicode string value that is a collection of characters.
- [Array](array.md) — An ordered, random-access collection.
- [Dictionary](dictionary.md) — A collection whose elements are key-value pairs.
- [Swift Standard Library](swift-standard-library.md) — Solve complex problems and write high-performance, readable code.
- [Updating an App to Use Swift Concurrency](updating_an_app_to_use_swift_concurrency.md) — Improve your app’s performance by refactoring your code to take advantage of asynchronous functions in Swift.

## Download

- [TicTacFishImplementingAGameUsingDistributedActors.zip](https://docs-assets.developer.apple.com/published/b583f10d72/TicTacFishImplementingAGameUsingDistributedActors.zip)
