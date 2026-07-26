---
title: 'execute(withAppleEvent:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuserapplescripttask/execute(withappleevent:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuserapplescripttask/execute(withappleevent:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserapplescripttask/execute%28withappleevent%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:bc59aea2ebc5a04f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserAppleScriptTask](../nsuserapplescripttask.md)

# execute(withAppleEvent:completionHandler:)

<sub>Instance Method</sub>

Execute the AppleScript script by sending it the specified Apple event.

<sub>macOS</sub>

```swift
func execute(withAppleEvent event: NSAppleEventDescriptor?, completionHandler handler: NSUserAppleScriptTask.CompletionHandler? = nil)
```

<sub>macOS</sub>

```swift
func execute(withAppleEvent event: NSAppleEventDescriptor?) async throws -> NSAppleEventDescriptor
```

## Parameters

- `event` — The Apple event.

- `handler` — The completion handler Block that returns the result or an error. See [CompletionHandler](completionhandler.md).

## Discussion

Pass `nil` as `event` to execute the script’s default “run” handler.

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## See Also

### Related Documentation

- [- initWithURL:error:](<../nsuserscripttask/init(url_)-2qgls.md>) — Return a user script task instance given a URL for a script file.
