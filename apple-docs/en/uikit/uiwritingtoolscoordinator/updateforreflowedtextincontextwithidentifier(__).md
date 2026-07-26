---
title: 'updateForReflowedTextInContextWithIdentifier(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/updateforreflowedtextincontextwithidentifier%28_%3A%29.json'
content_hash: 'sha256:df8eb6a66f388b18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# updateForReflowedTextInContextWithIdentifier(_:)

<sub>Instance Method</sub>

Informs the coordinator that a change occurred to the view or its text that requires a layout update.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func updateForReflowedTextInContextWithIdentifier(_ contextID: UUID)
```

## Parameters

- `contextID` — The unique identifier of the context object affected by the change. Pass the identifier for the context object that comes after the changes.

## Discussion

Use this method to inform Writing Tools when the geometry of your view changes, or when the text that precedes one of your context objects changes. Changes to the view’s geometry or text can affect the flow of any remaining text, and require a layout update. Writing Tools uses this method to refresh any layout-dependent information it’s currently tracking. For example, it uses it to refresh the location of proofreading marks it’s displaying in your view.

If a text change affects the text inside a context object, call the [- updateRange:withText:reason:forContextWithIdentifier:](<updaterange(__with_reason_forcontextwithidentifier_).md>) method to report that change instead.

## See Also

### Reporting changes to Writing Tools

- [- updateRange:withText:reason:forContextWithIdentifier:](<updaterange(__with_reason_forcontextwithidentifier_).md>) — Informs the coordinator about changes your app made to the text in the specified context object.
- [TextUpdateReason](textupdatereason.md) — Constants that specify the reason you updated your view’s content outside of the Writing Tools workflow.
