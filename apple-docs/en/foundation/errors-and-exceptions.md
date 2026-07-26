---
title: Errors and Exceptions
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/errors-and-exceptions
source_url: 'https://developer.apple.com/documentation/foundation/errors-and-exceptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/errors-and-exceptions.json'
content_hash: 'sha256:1808293eda5fac18'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Errors and Exceptions

<sub>API Collection</sub>

Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.

## Topics

### User-Relevant Errors

- [Error](../swift/error.md) — A type representing an error value that can be thrown.
- [NSError](nserror.md) — Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [LocalizedError](localizederror.md) — A specialized error that provides localized messages describing the error and why it occurred.
- [RecoverableError](recoverableerror.md) — A specialized error that may be recoverable by presenting several potential recovery options to the user.
- [CustomNSError](customnserror.md) — A specialized error that provides a domain, error code, and user-info dictionary.

### Assertions

- [NSAssertionHandler](nsassertionhandler.md) — An object that logs an assertion to the console.

### Exceptions

- [NSException](nsexception.md) — An object that represents a special condition that interrupts the normal flow of program execution.

### Diagnostics and Debugging

- [NSLogv](<nslogv(____).md>) — Logs an error message to the Apple System Log facility.
- [NSLog(_:_:)](<nslog(____).md>) — Logs an error message to the Apple System Log facility.

## See Also

### App Support

- [Task Management](task-management.md) — Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](resources.md) — Access assets and other data bundled with your app.
- [Notifications](notifications.md) — Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](app-extension-support.md) — Manage the interaction between an app extension and its hosting app.
- [Scripting Support](scripting-support.md) — Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.
