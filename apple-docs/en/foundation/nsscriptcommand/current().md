---
title: current()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/current()
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/current()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/current%28%29.json'
content_hash: 'sha256:d968b92220d7b2c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# current()

<sub>Type Method</sub>

If a command is being executed in the current thread by Cocoa scripting’s built-in Apple event handling, return the command.

<sub>Mac Catalyst, macOS</sub>

```swift
class func current() -> NSScriptCommand?
```

## Discussion

A command is being executed in the current thread by Cocoa scripting’s built-in Apple event handling if an instance of `NSScriptCommand` is handling an [- executeCommand](<execute().md>) message at this instant as the result of the dispatch of an Apple event. Returns `nil` otherwise. [scriptErrorNumber](scripterrornumber.md) and [scriptErrorString](scripterrorstring.md) messages sent to the returned command object will affect the reply event sent to the sender of the event from which the command was constructed, if the sender has requested a reply.

A suspended command is not considered the current command. If a command is suspended and no other command is being executed in the current thread, [+ currentCommand](<current().md>) returns `nil`.
