---
title: Responding to memory warnings
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/responding-to-memory-warnings
source_url: 'https://developer.apple.com/documentation/uikit/responding-to-memory-warnings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/responding-to-memory-warnings.json'
content_hash: 'sha256:55bcadc896923c01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)

# Responding to memory warnings

<sub>Article</sub>

Free up memory when asked to do so by the system.

## Overview

If the system runs low on free memory and is unable to reclaim memory by terminating suspended apps, UIKit sends a low-memory warning to running apps. UIKit delivers low-memory warnings in the following ways:

- It calls the [- applicationDidReceiveMemoryWarning:](<uiapplicationdelegate/applicationdidreceivememorywarning(__).md>) method of your app delegate.
- It calls the [- didReceiveMemoryWarning](<uiviewcontroller/didreceivememorywarning().md>) method of any active [UIViewController](uiviewcontroller.md) classes.
- It posts a [UIApplicationDidReceiveMemoryWarningNotification](uiapplication/didreceivememorywarningnotification.md) object to any registered observers.
- It delivers a warning to dispatch queues of type [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](../dispatch/dispatch_source_type_memorypressure.md).

When your app receives a low-memory warning, free up as much memory as possible, as quickly as possible. Remove references to images, media files, or any large data files that already have an on-disk representation and can be reloaded later. Remove references to any temporary objects that you no longer need. If active tasks might consume significant amounts of memory, pause dispatch queues or restrict the number of simultaneous operations that your app performs.

> [!important] Important
> Failure to reduce your app’s memory usage may result in your app’s termination. Therefore, consider writing any unsaved data to disk as part of your cleanup efforts.

To test your app’s response to a low-memory warning, use the Simulate Memory Warning command in iOS Simulator.
