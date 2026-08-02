---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/Messages.html
archived_at: '2026-07-18T02:54:57.256084Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# Messages Changes for Objective-C

### Messages (Added)

#### MessagesDefines.h (Added)

Added #def MESSAGES_EXTERN

#### MSConversation.h (Added)

Added [MSConversation](https://developer.apple.com/documentation/messages/msconversation)Added [-[MSConversation insertAttachment:withAlternateFilename:completionHandler:]](https://developer.apple.com/documentation/messages/msconversation/1648184-insertattachment)Added [-[MSConversation insertMessage:completionHandler:]](https://developer.apple.com/documentation/messages/msconversation/2102270-insertmessage)Added [-[MSConversation insertSticker:completionHandler:]](https://developer.apple.com/documentation/messages/msconversation/1648187-insert)Added [-[MSConversation insertText:completionHandler:]](https://developer.apple.com/documentation/messages/msconversation/1648188-inserttext)Added [MSConversation.localParticipantIdentifier](https://developer.apple.com/documentation/messages/msconversation/1648185-localparticipantidentifier)Added [MSConversation.remoteParticipantIdentifiers](https://developer.apple.com/documentation/messages/msconversation/1648183-remoteparticipantidentifiers)Added [MSConversation.selectedMessage](https://developer.apple.com/documentation/messages/msconversation/1648186-selectedmessage)

#### MSMessage.h (Added)

Added [MSMessage](https://developer.apple.com/documentation/messages/msmessage)Added [MSMessage.accessibilityLabel](https://developer.apple.com/documentation/messages/msmessage/1649735-accessibilitylabel)Added [MSMessage.error](https://developer.apple.com/documentation/messages/msmessage/1649737-error)Added [-[MSMessage init]](https://developer.apple.com/documentation/messages/msmessage/1649740-init)Added [-[MSMessage initWithSession:]](https://developer.apple.com/documentation/messages/msmessage/1649731-initwithsession)Added [MSMessage.layout](https://developer.apple.com/documentation/messages/msmessage/1649738-layout)Added [MSMessage.senderParticipantIdentifier](https://developer.apple.com/documentation/messages/msmessage/1649734-senderparticipantidentifier)Added [MSMessage.session](https://developer.apple.com/documentation/messages/msmessage/1649733-session)Added [MSMessage.shouldExpire](https://developer.apple.com/documentation/messages/msmessage/1649741-shouldexpire)Added [MSMessage.summaryText](https://developer.apple.com/documentation/messages/msmessage/2132092-summarytext)Added [MSMessage.URL](https://developer.apple.com/documentation/messages/msmessage/1649739-url)

#### MSMessageError.h (Added)

Added [MSMessageErrorCode](https://developer.apple.com/documentation/messages/msmessageerrorcode)Added [MSMessageErrorCodeFileNotFound](https://developer.apple.com/documentation/messages/msmessageerrorcode/msmessageerrorcodefilenotfound)Added [MSMessageErrorCodeFileUnreadable](https://developer.apple.com/documentation/messages/msmessageerrorcode/msmessageerrorcodefileunreadable)Added [MSMessageErrorCodeImproperFileType](https://developer.apple.com/documentation/messages/msmessageerrorcode/msmessageerrorcodeimproperfiletype)Added [MSMessageErrorCodeImproperFileURL](https://developer.apple.com/documentation/messages/msmessageerrorcode/improperfileurl)Added [MSMessageErrorCodeStickerFileImproperFileAttributes](https://developer.apple.com/documentation/messages/msmessageerrorcode/msmessageerrorcodestickerfileimproperfileattributes)Added [MSMessageErrorCodeStickerFileImproperFileFormat](https://developer.apple.com/documentation/messages/msmessageerrorcode/msmessageerrorcodestickerfileimproperfileformat)Added [MSMessageErrorCodeStickerFileImproperFileSize](https://developer.apple.com/documentation/messages/msmessageerrorcode/msmessageerrorcodestickerfileimproperfilesize)Added [MSMessageErrorCodeURLExceedsMaxSize](https://developer.apple.com/documentation/messages/msmessageerrorcode/msmessageerrorcodeurlexceedsmaxsize)Added [MSMessagesErrorDomain](https://developer.apple.com/documentation/messages/msmessageserrordomain)Added [MSStickersErrorDomain](https://developer.apple.com/documentation/messages/msstickerserrordomain)

#### MSMessageLayout.h (Added)

Added [MSMessageLayout](https://developer.apple.com/documentation/messages/msmessagelayout)

#### MSMessagesAppViewController.h (Added)

Added [MSMessagesAppViewController](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller)Added [MSMessagesAppViewController.activeConversation](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649188-activeconversation)Added [-[MSMessagesAppViewController didBecomeActiveWithConversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649187-didbecomeactivewithconversation)Added [-[MSMessagesAppViewController didCancelSendingMessage:conversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649186-didcancelsendingmessage)Added [-[MSMessagesAppViewController didReceiveMessage:conversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649189-didreceive)Added [-[MSMessagesAppViewController didResignActiveWithConversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649177-didresignactivewithconversation)Added [-[MSMessagesAppViewController didSelectMessage:conversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1833298-didselect)Added [-[MSMessagesAppViewController didStartSendingMessage:conversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649191-didstartsending)Added [-[MSMessagesAppViewController didTransitionToPresentationStyle:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649192-didtransition)Added [-[MSMessagesAppViewController dismiss]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649179-dismiss)Added [MSMessagesAppViewController.presentationStyle](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649182-presentationstyle)Added [-[MSMessagesAppViewController requestPresentationStyle:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649184-requestpresentationstyle)Added [-[MSMessagesAppViewController willBecomeActiveWithConversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649180-willbecomeactivewithconversation)Added [-[MSMessagesAppViewController willResignActiveWithConversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649185-willresignactive)Added [-[MSMessagesAppViewController willSelectMessage:conversation:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1833297-willselectmessage)Added [-[MSMessagesAppViewController willTransitionToPresentationStyle:]](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/1649178-willtransitiontopresentationstyl)Added [MSMessagesAppPresentationStyle](https://developer.apple.com/documentation/messages/msmessagesapppresentationstyle)Added [MSMessagesAppPresentationStyleCompact](https://developer.apple.com/documentation/messages/msmessagesapppresentationstyle/msmessagesapppresentationstylecompact)Added [MSMessagesAppPresentationStyleExpanded](https://developer.apple.com/documentation/messages/msmessagesapppresentationstyle/msmessagesapppresentationstyleexpanded)

#### MSMessageTemplateLayout.h (Added)

Added [MSMessageTemplateLayout](https://developer.apple.com/documentation/messages/msmessagetemplatelayout)Added [MSMessageTemplateLayout.caption](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648046-caption)Added [MSMessageTemplateLayout.image](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648040-image)Added [MSMessageTemplateLayout.imageSubtitle](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648044-imagesubtitle)Added [MSMessageTemplateLayout.imageTitle](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648042-imagetitle)Added [MSMessageTemplateLayout.mediaFileURL](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648043-mediafileurl)Added [MSMessageTemplateLayout.subcaption](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648041-subcaption)Added [MSMessageTemplateLayout.trailingCaption](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648038-trailingcaption)Added [MSMessageTemplateLayout.trailingSubcaption](https://developer.apple.com/documentation/messages/msmessagetemplatelayout/1648039-trailingsubcaption)

#### MSSession.h (Added)

Added [MSSession](https://developer.apple.com/documentation/messages/mssession)

#### MSSticker.h (Added)

Added [MSSticker](https://developer.apple.com/documentation/messages/mssticker)Added [MSSticker.imageFileURL](https://developer.apple.com/documentation/messages/mssticker/1648209-imagefileurl)Added [-[MSSticker initWithContentsOfFileURL:localizedDescription:error:]](https://developer.apple.com/documentation/messages/mssticker/1829445-initwithcontentsoffileurl)Added [MSSticker.localizedDescription](https://developer.apple.com/documentation/messages/mssticker/1648208-localizeddescription)

#### MSStickerBrowserView.h (Added)

Added [MSStickerBrowserView](https://developer.apple.com/documentation/messages/msstickerbrowserview)Added [MSStickerBrowserView.contentInset](https://developer.apple.com/documentation/messages/msstickerbrowserview/2102479-contentinset)Added [MSStickerBrowserView.contentOffset](https://developer.apple.com/documentation/messages/msstickerbrowserview/2102478-contentoffset)Added [MSStickerBrowserView.dataSource](https://developer.apple.com/documentation/messages/msstickerbrowserview/1649375-datasource)Added [-[MSStickerBrowserView initWithFrame:]](https://developer.apple.com/documentation/messages/msstickerbrowserview/1649376-initwithframe)Added [-[MSStickerBrowserView initWithFrame:stickerSize:]](https://developer.apple.com/documentation/messages/msstickerbrowserview/1649383-init)Added [-[MSStickerBrowserView reloadData]](https://developer.apple.com/documentation/messages/msstickerbrowserview/1649378-reloaddata)Added [-[MSStickerBrowserView setContentOffset:animated:]](https://developer.apple.com/documentation/messages/msstickerbrowserview/2102480-setcontentoffset)Added [MSStickerBrowserView.stickerSize](https://developer.apple.com/documentation/messages/msstickerbrowserview/1649380-stickersize)Added [MSStickerSize](https://developer.apple.com/documentation/messages/msstickersize)Added [MSStickerSizeLarge](https://developer.apple.com/documentation/messages/msstickersize/msstickersizelarge)Added [MSStickerSizeRegular](https://developer.apple.com/documentation/messages/msstickersize/msstickersizeregular)Added [MSStickerSizeSmall](https://developer.apple.com/documentation/messages/msstickersize/small)

#### MSStickerBrowserViewController.h (Added)

Added [MSStickerBrowserViewController](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller)Added [-[MSStickerBrowserViewController initWithStickerSize:]](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller/1649710-init)Added [MSStickerBrowserViewController.stickerBrowserView](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller/1649709-stickerbrowserview)Added [MSStickerBrowserViewController.stickerSize](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller/1649711-stickersize)

#### MSStickerBrowserViewDataSource.h (Added)

Added [MSStickerBrowserViewDataSource](https://developer.apple.com/documentation/messages/msstickerbrowserviewdatasource)Added [-[MSStickerBrowserViewDataSource numberOfStickersInStickerBrowserView:]](https://developer.apple.com/documentation/messages/msstickerbrowserviewdatasource/1649904-numberofstickers)Added [-[MSStickerBrowserViewDataSource stickerBrowserView:stickerAtIndex:]](https://developer.apple.com/documentation/messages/msstickerbrowserviewdatasource/1649905-stickerbrowserview)

#### MSStickerView.h (Added)

Added [MSStickerView](https://developer.apple.com/documentation/messages/msstickerview)Added [MSStickerView.animationDuration](https://developer.apple.com/documentation/messages/msstickerview/1935075-animationduration)Added [-[MSStickerView initWithFrame:sticker:]](https://developer.apple.com/documentation/messages/msstickerview/1648432-init)Added [-[MSStickerView isAnimating]](https://developer.apple.com/documentation/messages/msstickerview/1935072-isanimating)Added [-[MSStickerView startAnimating]](https://developer.apple.com/documentation/messages/msstickerview/1935073-startanimating)Added [MSStickerView.sticker](https://developer.apple.com/documentation/messages/msstickerview/1648434-sticker)Added [-[MSStickerView stopAnimating]](https://developer.apple.com/documentation/messages/msstickerview/1935074-stopanimating)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
