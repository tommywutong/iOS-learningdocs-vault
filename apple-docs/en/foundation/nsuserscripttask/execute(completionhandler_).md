---
title: 'execute(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuserscripttask/execute(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuserscripttask/execute(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserscripttask/execute%28completionhandler%3A%29.json'
content_hash: 'sha256:03fd64e1fd4fdbde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserScriptTask](../nsuserscripttask.md)

# execute(completionHandler:)

<sub>Instance Method</sub>

Executes the script with no input and ignoring any result.

<sub>macOS</sub>

```swift
func execute(completionHandler handler: NSUserScriptTask.CompletionHandler? = nil)
```

<sub>macOS</sub>

```swift
func execute() async throws
```

## Parameters

- `handler` — The completion handler Block that returns the result or an error. See [CompletionHandler](completionhandler.md).

## Discussion

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## See Also

### Related Documentation

- [- initWithURL:error:](<init(url_)-2qgls.md>) — Return a user script task instance given a URL for a script file.
