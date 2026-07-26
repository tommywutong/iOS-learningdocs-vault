---
title: Debugging focus issues in your app
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/debugging-focus-issues-in-your-app
source_url: 'https://developer.apple.com/documentation/uikit/debugging-focus-issues-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/debugging-focus-issues-in-your-app.json'
content_hash: 'sha256:e9c535738f528a77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Focus-based navigation](focus-based-navigation.md)

# Debugging focus issues in your app

<sub>Article</sub>

Find errors and determine why the next focused item isn’t what you expected.

## Overview

With the use of indirect controls for your tvOS app, it’s imperative that focus works correctly. To help you find focus problems, Apple provides two debugging tools: `UIFocusLoggingEnabled` and [UIFocusDebugger](uifocusdebugger.md).

### Turn on live focus logging

See how the focus engine determines which view is currently in focus by turning on live focus logging. As you move focus, the log updates, showing how the new view came into focus.

In your Xcode project, select Edit Scheme and add `-UIFocusLoggingEnabled YES` to the Arguments Passed On Launch section.

![Screenshot that shows adding the UIFocusLoggingEnabled argument in Xcode.](../../../attachments/c04b32a94b4e27d5867f5e688ab7b741/debugging-focus-issues-in-your-app-1@2x.png)

On launch, the debugger logs all focus events and displays the events in the Xcode console and the Console app. The debugger updates the log as focus changes in your app.

![Screenshot of focus debugging logs.](../../../attachments/46aad53b865fe480fd66a3dac088ff77/debugging-focus-issues-in-your-app-2@2x.png)

### Find focus issues using UIFocusDebugger

The [UIFocusDebugger](uifocusdebugger.md) class contains several methods to help you find focus issues. You don’t use this class or its methods directly from your code. Instead, during a debugging session, you call the methods of this class from the LLDB debugger command line to obtain information about the state of the focus system. For example, `po UIFocusDebugger.status()` returns the state of the focus engine.

## See Also

### Focus debugging

- [UIFocusDebugger](uifocusdebugger.md) — A runtime object for debugging focus-related interactions.
