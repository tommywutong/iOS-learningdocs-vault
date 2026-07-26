---
title: launch()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/process/launch()
source_url: 'https://developer.apple.com/documentation/foundation/process/launch()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/launch%28%29.json'
content_hash: 'sha256:dcac8842844d9467'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# launch()

<sub>Instance Method</sub>

Launches the task represented by the receiver.

> [!warning] Deprecated
> Use [- launchAndReturnError:](<run().md>) instead.

<sub>macOS</sub>

```swift
func launch()
```

## Discussion

Raises an `NSInvalidArgumentException` if the launch path has not been set or is invalid or if it fails to create a process.

## See Also

### Related Documentation

- [- waitUntilExit](<waituntilexit().md>) — Blocks the process until the receiver is finished.
- [- terminate](<terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.

### Deprecated

- [+ launchedTaskWithLaunchPath:arguments:](<launchedprocess(launchpath_arguments_).md>) — Creates and launches a task with a specified executable and arguments. _(deprecated)_
- [currentDirectoryPath](currentdirectorypath.md) — Sets the current directory for the receiver. _(deprecated)_
- [launchPath](launchpath.md) — Sets the receiver’s executable. _(deprecated)_
