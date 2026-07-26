---
title: 'execute(withInput:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuserautomatortask/execute(withinput:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuserautomatortask/execute(withinput:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserautomatortask/execute%28withinput%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:ba4707538824b948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserAutomatorTask](../nsuserautomatortask.md)

# execute(withInput:completionHandler:)

<sub>Instance Method</sub>

Execute the Automator workflow by providing it as securely coded input.

<sub>macOS</sub>

```swift
func execute(withInput input: (any NSSecureCoding)?, completionHandler handler: NSUserAutomatorTask.CompletionHandler? = nil)
```

<sub>macOS</sub>

```swift
func execute(withInput input: (any NSSecureCoding)?) async throws -> Any
```

## Parameters

- `input` — The automator task.

- `handler` — The completion handler Block that returns the result or an error. See [CompletionHandler](completionhandler.md).

## Discussion

The Automator workflow will execute using the [variables](variables.md) property values.

This method should be invoked no more than once for a given instance of the class.

If the script completed normally, the completion handler’s `error` parameter will be `nil`.

## See Also

### Related Documentation

- [- initWithURL:error:](<../nsuserscripttask/init(url_)-2qgls.md>) — Return a user script task instance given a URL for a script file.

### Executing Automator Tasks

- [variables](variables.md) — The variables required by the Automator workflow.
