---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Concepts/process.html
archived_at: '2026-07-15T07:17:35.560963Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interacting with the Operating System](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)


[Next](Task%20Management.md)[Previous](Host%20Information.md)

# Process Information

The `NSProcessInfo` class provides methods to access process-wide information. An `NSProcessInfo` object can return such information as the current process’s arguments, environment variables, host name, and process name.

The `NSProcessInfo` class is available in Objective-C only. In Java, the `NSSystem` class provides the same information as `NSProcessInfo` as well as information obtained from function calls in Objective-C. The `NSSystem` class object can return such additional information as the user’s name, full name, and home directory. The class also provides a method, `log`, to send strings to `stderr`.

[Next](Task%20Management.md)[Previous](Host%20Information.md)

