---
title: publish()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/publish()
source_url: 'https://developer.apple.com/documentation/foundation/progress/publish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/publish%28%29.json'
content_hash: 'sha256:be7060ae0b2aa8ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# publish()

<sub>Instance Method</sub>

Publishes the progress object for other processes to observe it.

<sub>macOS</sub>

```swift
func publish()
```

## Discussion

Entries in the user info dictionary determine whether another process can discover the progress object to observe it, and how it does that. For example, a [NSProgressFileURLKey](../progressuserinfokey/fileurlkey.md) entry makes a progress object discoverable by corresponding invokers of [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>). The system constrains access to the published progress URL with your app sandbox. If you can’t see the file due to the app’s sandbox restrictions, you can’t observe the progress on it.

When you make a progress object observable by other processes, you must ensure that at least [localizedDescription](localizeddescription.md), [indeterminate](isindeterminate.md), and [fractionCompleted](fractioncompleted.md) always work when you send proxies of your progress object in other processes. You make [indeterminate](isindeterminate.md) and [fractionCompleted](fractioncompleted.md) work by accurately setting the total and completed unit counts of the progress. You make [localizedDescription](localizeddescription.md) work by setting the value of the kind property to something valid, like [NSProgressKindFile](../progresskind/file.md), and then fulfilling the requirements for that kind of progress.

You can instead set the value of [localizedDescription](localizeddescription.md) directly, but that’s not perfectly reliable because other processes might be using a different localization than yours.

You can publish an instance of [Progress](../progress.md) one time only.

## See Also

### Reporting Progress to Other Processes

- [- unpublish](<unpublish().md>) — Removes a progress object from publication, making it unobservable by other processes.
