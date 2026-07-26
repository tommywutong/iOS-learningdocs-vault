---
title: Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime
framework: Messages
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime
source_url: 'https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.json'
content_hash: 'sha256:a50da179e2de8bba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Messages](../messages.md)

# Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime

<sub>Article</sub>

Enable your Sticker pack or iMessage app in the media context.

## Overview

In iOS 12 and later, Sticker packs and iMessage apps can appear in multiple contexts.

- **[MSMessagesAppPresentationContextMessages](msmessagesapppresentationcontext/messages.md) context** — The Sticker pack or iMessage app appears in the list of iMessage apps that appears when you press the plus button.
- **[MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md) context** — The sticker pack or iMessage app appears in the Stickers app throughout iOS, and in effect in FaceTime and the Messages camera.

People can access stickers throughout iOS through the emoji keyboard. To access effects in the Messages camera or FaceTime, a person taps the effects button. The system then displays all the iMessage apps and Sticker packs that support the media context. A person can launch an app, and use it to add images or stickers to the camera.

iMessage apps only appear in the `messages` context. To enable support for the `media` context, set the `MSSupportedPresentationContexts` key in your extension’s `Info.plist` file. If you indicate support for both `messages` and `media`, your Stickers only present in the `media` context including in Messages.

A Sticker pack or iMessage app’s context limits its available features. For example, In the [MSMessagesAppPresentationContextMessages](msmessagesapppresentationcontext/messages.md) context, a person can peel off stickers and attach them to any bubbles in the current conversation. Your app can also programatically send stickers, images, text, or interactive messages.

In the [MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md) context, your app appears in effects in Messages and FaceTime. Therefore, the system limits your app to features that make sense over a photo or video. For instance, a person can’t play an interactive game while taking a photo; however, they can add stickers or images to the picture.

### Specify the supported contexts

To specify the supported contexts:

1. Open the `Info.plist` file for your Sticker pack or iMessage app extension.
2. Add the `MSSupportedPresentationContexts` key, using an Array type.
3. Add String values for the supported contexts. For the [MSMessagesAppPresentationContextMessages](msmessagesapppresentationcontext/messages.md) context, add the `MSMessagesAppPresentationContextMessages` value. For [MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md), add `MSMessagesAppPresentationContextMedia`.

You must specify one of the contexts, but if you specify both contexts, they only present in the [MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md) context.

For more information on setting I`nfo.plist` keys, see [Edit property lists](https://help.apple.com/xcode/mac/9.3/#/dev3f399a2a6).

### Work with the media context

The [MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md) context supports only a subset of the features provided by the Messages framework. People can peel stickers from a sticker browser view, and place them in the Messages camera or FaceTime. They can reposition, resize, rotate, or remove stickers from the viewfinder.

iMessage apps can also insert stickers or images into the viewfinder using the [- insertSticker:completionHandler:](<msconversation/insert(__completionhandler_)-7fpdd.md>) or [- insertAttachment:withAlternateFilename:completionHandler:](<msconversation/insertattachment(__withalternatefilename_completionhandler_).md>) methods. However, if the attachment isn’t an image supported by [MSSticker](mssticker.md), then the [- insertAttachment:withAlternateFilename:completionHandler:](<msconversation/insertattachment(__withalternatefilename_completionhandler_).md>) method fails with an [MSMessageErrorCodeAPIUnavailableInPresentationContext](msmessageerrorcode/apiunavailableinpresentationcontext.md) error.

Additionally, you can’t insert interactive messages or text into the media context. You also can’t send items automatically. Therefore, the following methods from the [MSConversation](msconversation.md) class aren’t available:

- [- insertMessage:completionHandler:](<msconversation/insert(__completionhandler_)-3g248.md>)
- [- insertText:completionHandler:](<msconversation/inserttext(__completionhandler_).md>)
- [- sendAttachment:withAlternateFilename:completionHandler:](<msconversation/sendattachment(__withalternatefilename_completionhandler_).md>)
- [- sendMessage:completionHandler:](<msconversation/send(__completionhandler_)-9krz.md>)
- [- sendSticker:completionHandler:](<msconversation/send(__completionhandler_)-4kje0.md>)
- [- sendText:completionHandler:](<msconversation/sendtext(__completionhandler_).md>)

If you call these methods, they fail with an [MSMessageErrorCodeAPIUnavailableInPresentationContext](msmessageerrorcode/apiunavailableinpresentationcontext.md) error.

Additionally, because you can’t send or receive interactive messages, the system never calls the following methods in the [MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md) context:

- [- willSelectMessage:conversation:](<msmessagesappviewcontroller/willselect(__conversation_).md>)
- [- didSelectMessage:conversation:](<msmessagesappviewcontroller/didselect(__conversation_).md>)
- [- didReceiveMessage:conversation:](<msmessagesappviewcontroller/didreceive(__conversation_).md>)
- [- didStartSendingMessage:conversation:](<msmessagesappviewcontroller/didstartsending(__conversation_).md>)
- [- didCancelSendingMessage:conversation:](<msmessagesappviewcontroller/didcancelsending(__conversation_).md>)

Finally, the [MSMessagesAppPresentationContextMedia](msmessagesapppresentationcontext/media.md) context is already inside the Messages camera or FaceTime; therefore, you can’t display another camera inside the current viewfinder.

### Detect the current context

Use the [MSMessagesAppViewController](msmessagesappviewcontroller.md) object’s [presentationContext](msmessagesappviewcontroller/presentationcontext.md) property to determine your iMessage app’s current context. Enable only the features that make sense in that context.

```swift
if presentationContext == .messages {
    // The system is presenting your iMessage app inside the Messages app.
    // You have full access to the Messages framework.
    // You can insert or send stickers, text, attachments, or interactive messages.
} else if presentationContext == .media {
    // The system is presenting your iMessage app in effects.
    // You can only insert stickers and images.
}
```

## See Also

### Custom sticker packs

- [Adding your sticker packs to Messages](adding-your-sticker-packs-to-messages.md) — Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [MSStickerBrowserViewController](msstickerbrowserviewcontroller.md) — A view controller that provides dynamic content to the standard sticker browser.
- [MSStickerBrowserView](msstickerbrowserview.md) — A browser view that displays a dynamically generated list of stickers.
- [MSStickerView](msstickerview.md) — A view for displaying a sticker.
- [MSStickerSize](msstickersize.md) — The size of the stickers in the browser view.
