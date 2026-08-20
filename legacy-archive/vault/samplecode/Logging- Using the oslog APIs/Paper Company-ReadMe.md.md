---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/Paper_Company_ReadMe_md.html
archived_at: '2026-07-18T03:13:47.664373Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](Paper%20Company%20%28Swift%29-Paper%20Company%20%28Swift%29-ViewController.swift.md)[Previous](Paper%20Company-Paper%20Company-APLViewController.m.md)

# Paper Company/ReadMe.md

```

# Paper Company (Swift)

The Paper Company sample application shows how to use the Logging APIs to record information about what an application is doing. This information can help to troubleshoot and fix bugs later.


## Logging Levels

For information on the different logging levels, read the [Logging Reference guide][1].

[1]: <https://developer.apple.com/reference/os/1891852-logging>


## Activities

Activity tracing provides the ability to follow the chain of work done before a crash, including work done asynchronously. Since Paper Company uses activity tracing, it is possible to view just the logs generated as the direct result of a button press.    


## Components

Logging components are used to tag logs as coming from one part of your application. In Paper Company, there is a component for the UI and another component for the model (as in model-view-controller). This allows for filtering of logged messages later on. For example, if it is suspected that the application's data model is being updated incorrectly, it is possible to see the logs from just the model, filtering out logs from the UI.


## Viewing Logs

Log messages can be viewed in Xcode's console, in the Console application, or via the `log` tool. To view logs while Paper Company is running in the iOS Simulator, run this behemoth of a command in Terminal: `xcrun simctl spawn booted log stream --level debug --predicate '(subsystem == "com.example.apple-samplecode.Paper-Company-Swift") && (category == "Model")'`. To break down the command:

  - `xcrun simctl spawn booted` requests that the iOS Simulator run a command, in this case the `log` tool. This portion of the command is only necessary when running in the simulator.

  - `log stream` serves to view the live stream of log messages produced by a running application. To view saved logs (after the application has stopped running), use `log show` instead.

  - The `--level debug` option captures all messages logged at a level up to and including debug. (Debug is the most verbose level, so this enables all log messages.)

  - The predicate searches for the subsystem and component used in Paper Company's model (in `APLPaperCompany.m`). The `log` tool fully supports [NSPredicate][2] for filtering logs.

For a detailed explanation of the `log` tool and its usage, read its manual page.

[2]: <https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html>


## Main Files

APLPaperCompany.{h,m}
  - The model-view-controller model of our application's paper company. Demonstrates use of a custom logging component and produces log messages to help demonstrate the Activity APIs.

APLViewController.{h,m}
  - A simple view controller that enables interaction with our application's model. Demonstrates the Activity APIs and uses a custom logging component.


Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](Paper%20Company%20%28Swift%29-Paper%20Company%20%28Swift%29-ViewController.swift.md)[Previous](Paper%20Company-Paper%20Company-APLViewController.m.md)

