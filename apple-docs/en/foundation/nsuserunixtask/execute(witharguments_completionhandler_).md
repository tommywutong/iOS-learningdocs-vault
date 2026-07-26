---
title: 'execute(withArguments:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuserunixtask/execute(witharguments:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuserunixtask/execute(witharguments:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserunixtask/execute%28witharguments%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:a7930ffb94ff8de0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserUnixTask](../nsuserunixtask.md)

# execute(withArguments:completionHandler:)

<sub>Instance Method</sub>

Execute the unix script with the specified arguments.

<sub>macOS</sub>

```swift
func execute(withArguments arguments: [String]?, completionHandler handler: NSUserUnixTask.CompletionHandler? = nil)
```

<sub>macOS</sub>

```swift
func execute(withArguments arguments: [String]?) async throws
```

## Parameters

- `arguments` — An array of `NSString` objects containing the script arguments. The arguments do not undergo shell expansion, so you do not need to do special quoting, and shell variables are not resolved.

- `handler` — The completion handler Block that returns the result. See [CompletionHandler](completionhandler.md).

## Discussion

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## See Also

### Related Documentation

- [standardOutput](standardoutput.md) — The standard output stream.
- [standardError](standarderror.md) — The standard error stream.
- [- initWithURL:error:](<../nsuserscripttask/init(url_)-2qgls.md>) — Return a user script task instance given a URL for a script file.
- [standardInput](standardinput.md) — The standard input stream.
