---
title: Starting and Terminating Tasks During Development
framework: Background Tasks
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/starting-and-terminating-tasks-during-development
source_url: 'https://developer.apple.com/documentation/backgroundtasks/starting-and-terminating-tasks-during-development'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/starting-and-terminating-tasks-during-development.json'
content_hash: 'sha256:c0765b87ff037fe2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# Starting and Terminating Tasks During Development

<sub>Article</sub>

Use the debugger during development to start tasks and to terminate them before completion.

## Overview

The delay between the time you schedule a background task and when the system launches your app to run the task can be many hours. While developing your app, you can use two private functions to start a task and to force early termination of the task according to your selected timeline. The debug functions work only on devices.

> [!important] Important
> Use private functions only during development. Including a reference to these functions in apps submitted to the App Store is cause for rejection.

### Launch a Task

To launch a task:

1. Set a breakpoint in the code that executes after a successful call to [- submitTaskRequest:error:](<bgtaskscheduler/submit(__).md>).
2. Run your app on a device until the breakpoint pauses your app.
3. In the debugger, execute the line shown below, substituting the identifier of the desired task for `TASK_IDENTIFIER`.
4. Resume your app. The system calls the launch handler for the desired task.

```other
e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateLaunchForTaskWithIdentifier:@"TASK_IDENTIFIER"]
```

### Force Early Termination of a Task

To force termination of a task:

1. Set a breakpoint in the desired task.
2. Launch the task using the debugger as described in the previous section.
3. Wait for your app to pause at the breakpoint.
4. In the debugger, execute the line shown below, substituting the identifier of the desired task for `TASK_IDENTIFIER`.
5. Resume your app. The system calls the expiration handler for the desired task.

```other
e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateExpirationForTaskWithIdentifier:@"TASK_IDENTIFIER"]
```
