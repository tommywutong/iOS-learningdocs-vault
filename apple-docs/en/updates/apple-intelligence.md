---
title: Apple Intelligence updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/apple-intelligence
source_url: 'https://developer.apple.com/documentation/updates/apple-intelligence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/apple-intelligence.json'
content_hash: 'sha256:c17a2c0e2e562bb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# Apple Intelligence updates

<sub>Article</sub>

Learn about important changes to Apple Intelligence.

## Overview

Browse notable changes in [Apple Intelligence](https://developer.apple.com/apple-intelligence/).

## February 2025

- Use [ImageCreator](../imageplayground/imagecreator.md) to generate images programmatically from your app on devices that support the capability.  The system’s generative models use your provided description to generate one or more images and return them to your code. The [ImagePlaygroundConcept](../imageplayground/imageplaygroundconcept.md) type includes text you use to describe the image you wish to create, and [ImagePlaygroundStyle](../imageplayground/imageplaygroundstyle.md) sets the style to apply to that image.
- Start [Generating summary and priority data for indexed items](../corespotlight/generating-summary-and-priority-data-for-indexed-items.md) using a Spotlight delegate app extension in your app.
- Learn about  [Adopting Smart Reply in your messaging or email app](../uikit/adopting-smart-reply-in-your-messaging-or-email-app.md) to give Apple Intelligence the context of your messaging or mail thread, and insert the generated response back into your app’s UI. Use [UIMessageConversationContext](../uikit/uimessageconversationcontext.md) for messaging, and [UIMailConversationContext](../uikit/uimailconversationcontext.md) for email.

## January 2025

Writing Tools in UIKit:

- Display a bar button item to launch Writing Tools using [UIBarButtonItem.SystemItem.writingTools](../uikit/uibarbuttonitem/systemitem/writingtools.md).
- Integrate Writing Tools into your custom text engine using the API in [Writing Tools](../uikit/writing-tools.md).

Writing Tools in AppKit:

- Display a toolbar item to launch Writing Tools using [writingToolsItemIdentifier](../appkit/nstoolbaritem/identifier/writingtoolsitemidentifier.md).
- Integrate Writing Tools into your custom text engine using the API in [Writing Tools](../appkit/writing-tools.md).

## November 2024

- Make onscreen content available to Siri and Apple Intelligence with App Intents. Describe content as an [AppEntity](../appintents/appentity.md) and adopt an assistant schema. Conform the entity to the [Transferable](../coretransferable/transferable.md) protocol, and associate it with a [NSUserActivity](../foundation/nsuseractivity.md) using the activity’s [appEntityIdentifier](../foundation/nsuseractivity/appentityidentifier.md) property.

## July 2024

> [!note] Note
> Testing and using Apple Intelligence features requires iOS 18.1 or later, or macOS 15.1 or later.

### Writing Tools

- In SwiftUI, adjust the level of support for Writing Tools features using the [writingToolsBehavior(_:)](<../swiftui/view/writingtoolsbehavior(__).md>) modifier on the [Text](../swiftui/text.md), [TextField](../swiftui/textfield.md), and [TextEditor](../swiftui/texteditor.md) types.
- In UIKit, detect activity using new [UITextViewDelegate](../uikit/uitextviewdelegate.md) methods. Set your text view’s level of support for Writing Tools features using the [writingToolsBehavior](../uikit/uitextinputtraits/writingtoolsbehavior.md) property of [UITextInputTraits](../uikit/uitextinputtraits.md).
- In AppKit, detect activity using new [NSTextViewDelegate](../appkit/nstextviewdelegate.md) methods. Set your text view’s level of support for Writing Tools features using the [writingToolsBehavior](../appkit/nstextinputtraits/writingtoolsbehavior.md) property of [NSTextInputTraits](../appkit/nstextinputtraits.md).

### Genmoji

- Handle Genmoji in text content using [NSAdaptiveImageGlyph](../uikit/nsadaptiveimageglyph.md).

### Siri and App Intents

- Conform your [AppIntent](../appintents/appintent.md), [AppEntity](../appintents/appentity.md), and [AppEnum](../appintents/appenum.md) implementations to the assistant schemas by applying the [relevant macros](https://developer.apple.com/documentation/appintents/app-intent-domains) to your types.

### Core Spotlight

- Search your indexed content for items that are similar in meaning to the query string, but not necessarily a lexical match, using [CSUserQuery](../corespotlight/csuserquery.md). Disable this semantic search support using the [disableSemanticSearch](../corespotlight/csuserquerycontext/disablesemanticsearch.md) property of [CSUserQueryContext](../corespotlight/csuserquerycontext.md).

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
- [Background Tasks updates](backgroundtasks.md) — Learn about important changes in Background Tasks.
